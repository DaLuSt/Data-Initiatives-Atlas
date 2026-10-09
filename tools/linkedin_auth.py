#!/usr/bin/env python3
"""Get a LinkedIn access token for posting release notes (run on your own computer).

This is the one-off authorisation step of docs/credentials.md, section 2. You run
it, approve the consent screen in your browser, and it prints three values to paste
into the GitHub environment named `linkedin`:

    LINKEDIN_ACCESS_TOKEN     (a secret; lasts about 60 days)
    LINKEDIN_AUTHOR_URN       (urn:li:person:<id>; a secret in the same environment)
    LINKEDIN_TOKEN_EXPIRES    (a variable: the date the token runs out)

Nothing is written to disk. The Client Secret is read from the environment or typed
at a hidden prompt, never taken from the command line (it would end up in your shell
history) and never printed.

Before running it, in the LinkedIn developer portal:
  * the app has the products "Share on LinkedIn" and "Sign In with LinkedIn using
    OpenID Connect";
  * the Auth tab lists the redirect URL http://localhost:8080/callback (or the one you
    pass with --port).

    export LINKEDIN_CLIENT_ID=...        # the Client ID from the Auth tab
    python tools/linkedin_auth.py        # asks for the Client Secret

In a GitHub Codespace (or over SSH, or in any place where your browser cannot reach
the program's `localhost`), the redirect cannot arrive by itself. There the script
runs in **paste mode** (automatic when the CODESPACES variable is set; force it with
--manual, or force the local receiver with --listen): you approve in your browser, the
browser then shows "this site can't be reached" for an address starting
http://localhost:8080/callback?code=..., and you paste that whole address into the
terminal. The code in it is single-use and useless without the Client Secret.

Standard library only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import getpass
import hmac
import json
import os
import secrets
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer

AUTHORIZE_URL = "https://www.linkedin.com/oauth/v2/authorization"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
USERINFO_URL = "https://api.linkedin.com/v2/userinfo"
# openid + profile identify the member (the `sub` becomes the author ID);
# w_member_social is the permission to post on the member's behalf.
SCOPES = ("openid", "profile", "w_member_social")
DEFAULT_PORT = 8080
CALLBACK_PATH = "/callback"
WAIT_SECONDS = 300


class AuthError(Exception):
    """Something went wrong; the message is safe to print (it holds no secret)."""


def redirect_uri(port: int) -> str:
    return f"http://localhost:{port}{CALLBACK_PATH}"


def build_authorize_url(client_id: str, port: int, state: str) -> str:
    query = urllib.parse.urlencode({
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri(port),
        "state": state,
        "scope": " ".join(SCOPES),
    }, quote_via=urllib.parse.quote)
    return f"{AUTHORIZE_URL}?{query}"


def parse_callback(path: str, expected_state: str) -> str:
    """The authorisation code from the redirect, or an AuthError saying why not."""
    url = urllib.parse.urlsplit(path)
    if url.path != CALLBACK_PATH:
        raise AuthError(f"unexpected path {url.path!r}")
    q = urllib.parse.parse_qs(url.query)
    state = (q.get("state") or [""])[0]
    # Check the state first: a response we did not ask for is not trusted at all.
    if not hmac.compare_digest(state.encode(), expected_state.encode()):
        raise AuthError("the state value did not match; start again (possible forged redirect)")
    if "error" in q:
        why = (q.get("error_description") or q["error"])[0]
        raise AuthError(f"LinkedIn refused the request: {why}")
    code = (q.get("code") or [""])[0]
    if not code:
        raise AuthError("the redirect carried no authorisation code")
    return code


def expiry_date(expires_in: int, today: dt.date | None = None) -> str:
    """The date the token stops working, one day early so a reminder fires in time."""
    today = today or dt.date.today()
    return (today + dt.timedelta(seconds=int(expires_in)) - dt.timedelta(days=1)).isoformat()


# ── network (injectable) ─────────────────────────────────────────────────────

def _read(req: urllib.request.Request) -> dict:
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        # LinkedIn's error body names the problem; it never echoes our secret.
        detail = err.read().decode("utf-8", "replace")[:300]
        raise AuthError(f"HTTP {err.code} from {req.full_url.split('?')[0]}: {detail}") from None
    except (urllib.error.URLError, json.JSONDecodeError) as err:
        raise AuthError(f"could not read {req.full_url.split('?')[0]}: {err}") from None


def post_form(url: str, fields: dict) -> dict:
    data = urllib.parse.urlencode(fields).encode("ascii")
    req = urllib.request.Request(url, data=data, method="POST",
                                 headers={"Content-Type": "application/x-www-form-urlencoded"})
    return _read(req)


def get_json(url: str, token: str) -> dict:
    return _read(urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"}))


# ── the local redirect receiver ──────────────────────────────────────────────

def wait_for_code(port: int, state: str, wait: float = WAIT_SECONDS, ready=None) -> str:
    """Listen on 127.0.0.1 only, take exactly one request, return the code."""
    result: dict = {}

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802 (http.server's name)
            try:
                result["code"] = parse_callback(self.path, state)
                body, status = "Signed in. You can close this tab and go back to the terminal.", 200
            except AuthError as err:
                result["error"] = str(err)
                body, status = f"Not signed in: {err}", 400
            payload = f"<!doctype html><meta charset=utf-8><title>LinkedIn</title><p>{_esc(body)}</p>".encode()
            self.send_response(status)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def log_message(self, *args):  # keep the code and state out of the terminal
            pass

    server = HTTPServer(("127.0.0.1", port), Handler)
    server.timeout = wait
    if ready:
        ready(server.server_address[1])
    thread = threading.Thread(target=server.handle_request)
    thread.start()
    thread.join(wait + 1)
    server.server_close()
    if "error" in result:
        raise AuthError(result["error"])
    if "code" not in result:
        raise AuthError(f"no redirect arrived within {int(wait)} seconds")
    return result["code"]


def paste_for_code(port: int, state: str, ask=input, say=print) -> str:
    """Paste mode: the person copies the redirect address from the browser."""
    say("")
    say("After you approve, the browser will say the page cannot be reached. That is expected.")
    say(f"Copy the whole address from the browser's address bar (it starts with {redirect_uri(port)}?code=)")
    say("and paste it here.")
    text = ask("Address: ").strip()
    if not text:
        raise AuthError("nothing was pasted")
    url = urllib.parse.urlsplit(text)
    # A full address, or just the path and query: both end up as /callback?...
    path = url.path + ("?" + url.query if url.query else "")
    return parse_callback(path, state)


def _esc(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ── the whole flow ───────────────────────────────────────────────────────────

def authorise(client_id: str, client_secret: str, port: int = DEFAULT_PORT, *,
              open_browser=webbrowser.open, say=print, receive=wait_for_code,
              exchange=post_form, fetch=get_json, today: dt.date | None = None) -> dict:
    """Run the flow; return the three values. All I/O is injectable for tests."""
    state = secrets.token_urlsafe(24)
    url = build_authorize_url(client_id, port, state)
    say("Opening LinkedIn in your browser. If nothing opens, paste this address into it:")
    say(url)
    open_browser(url)
    code = receive(port, state)
    token = exchange(TOKEN_URL, {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri(port),
    })
    access = token.get("access_token")
    if not access:
        raise AuthError("LinkedIn's reply had no access_token")
    if "w_member_social" not in str(token.get("scope", "w_member_social")):
        raise AuthError("the token does not carry w_member_social; is the 'Share on LinkedIn' "
                        "product added to the app, and was it approved on the consent screen?")
    sub = fetch(USERINFO_URL, access).get("sub")
    if not sub:
        raise AuthError("the userinfo reply had no member ID; is 'Sign In with LinkedIn using "
                        "OpenID Connect' added to the app?")
    return {
        "LINKEDIN_ACCESS_TOKEN": access,
        "LINKEDIN_AUTHOR_URN": f"urn:li:person:{sub}",
        "LINKEDIN_TOKEN_EXPIRES": expiry_date(token.get("expires_in", 5184000), today),
        "refresh": "refresh_token" in token,
    }


def report(values: dict, say=print) -> None:
    say("")
    say("Done. In GitHub, open Settings > Environments > linkedin and add:")
    say("  Secret    LINKEDIN_ACCESS_TOKEN   (the token below)")
    say("  Secret    LINKEDIN_AUTHOR_URN     " + values["LINKEDIN_AUTHOR_URN"])
    say("  Variable  LINKEDIN_TOKEN_EXPIRES  " + values["LINKEDIN_TOKEN_EXPIRES"])
    say("")
    say("LINKEDIN_ACCESS_TOKEN (copy it now; this script does not save it):")
    say(values["LINKEDIN_ACCESS_TOKEN"])
    say("")
    if values["refresh"]:
        say("Note: LinkedIn also issued a refresh token. This script does not print or keep it;")
        say("tell the maintainer, because it may make automatic renewal possible (roadmap #515).")
    say("Do not paste the token into an issue, a chat or a file in the repository.")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--manual", action="store_true",
                      help="paste the redirect address instead of receiving it (automatic in a Codespace)")
    mode.add_argument("--listen", action="store_true",
                      help="receive the redirect on this computer, even in a Codespace")
    ap.add_argument("--port", type=int, default=DEFAULT_PORT,
                    help=f"local port for the redirect (default {DEFAULT_PORT}); the redirect URL "
                         "in the LinkedIn app must match")
    args = ap.parse_args(argv)

    client_id = os.environ.get("LINKEDIN_CLIENT_ID", "").strip()
    if not client_id:
        client_id = input("LinkedIn Client ID: ").strip()
    client_secret = os.environ.get("LINKEDIN_CLIENT_SECRET", "").strip()
    if not client_secret:
        client_secret = getpass.getpass("LinkedIn Client Secret (hidden): ").strip()
    if not client_id or not client_secret:
        print("error: the Client ID and Client Secret are both needed", file=sys.stderr)
        return 2
    manual = args.manual or (os.environ.get("CODESPACES") == "true" and not args.listen)
    try:
        report(authorise(client_id, client_secret, args.port,
                         receive=paste_for_code if manual else wait_for_code))
    except AuthError as err:
        print(f"error: {err}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
