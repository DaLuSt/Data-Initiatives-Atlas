#!/usr/bin/env python3
"""Tests for tools/linkedin_auth.py.

Pure functions, the real local redirect receiver on an ephemeral port (127.0.0.1
only), and the whole flow with LinkedIn replaced by fakes. No network.

    python tools/test_linkedin_auth.py
"""

from __future__ import annotations

import ast
import datetime as dt
import io
import sys
import threading
import unittest
import urllib.error
import urllib.parse
import urllib.request
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

import linkedin_auth as la  # noqa: E402

SECRET = "s3cr3t-client-secret"
TOKEN = "AQX-the-access-token"


class TestAuthorizeUrl(unittest.TestCase):
    def query(self, **kw):
        url = la.build_authorize_url("cid123", kw.get("port", 8080), "st4te")
        parts = urllib.parse.urlsplit(url)
        return parts, urllib.parse.parse_qs(parts.query)

    def test_points_at_linkedins_authorisation_endpoint(self):
        parts, _ = self.query()
        self.assertEqual(f"{parts.scheme}://{parts.netloc}{parts.path}", "https://www.linkedin.com/oauth/v2/authorization")

    def test_asks_for_a_code_with_the_three_scopes(self):
        _, q = self.query()
        self.assertEqual(q["response_type"], ["code"])
        self.assertEqual(q["client_id"], ["cid123"])
        self.assertEqual(q["state"], ["st4te"])
        self.assertEqual(q["scope"], ["openid profile w_member_social"])

    def test_redirect_uri_follows_the_port(self):
        _, q = self.query(port=9090)
        self.assertEqual(q["redirect_uri"], ["http://localhost:9090/callback"])

    def test_the_client_secret_is_never_in_the_url(self):
        url = la.build_authorize_url("cid123", 8080, "st4te")
        self.assertNotIn("secret", url.lower())


class TestParseCallback(unittest.TestCase):
    def test_returns_the_code(self):
        self.assertEqual(la.parse_callback("/callback?code=abc&state=ok", "ok"), "abc")

    def test_wrong_state_is_refused_even_with_a_code(self):
        with self.assertRaisesRegex(la.AuthError, "state"):
            la.parse_callback("/callback?code=abc&state=evil", "ok")

    def test_missing_state_is_refused(self):
        with self.assertRaisesRegex(la.AuthError, "state"):
            la.parse_callback("/callback?code=abc", "ok")

    def test_state_is_checked_before_the_error_is_believed(self):
        with self.assertRaisesRegex(la.AuthError, "state"):
            la.parse_callback("/callback?error=access_denied&state=evil", "ok")

    def test_linkedins_refusal_is_reported(self):
        with self.assertRaisesRegex(la.AuthError, "user cancelled"):
            la.parse_callback("/callback?error=user_cancelled_authorize&error_description=user%20cancelled&state=ok", "ok")

    def test_no_code_is_an_error(self):
        with self.assertRaisesRegex(la.AuthError, "no authorisation code"):
            la.parse_callback("/callback?state=ok", "ok")

    def test_other_paths_are_refused(self):
        with self.assertRaisesRegex(la.AuthError, "unexpected path"):
            la.parse_callback("/other?code=abc&state=ok", "ok")


class TestExpiryDate(unittest.TestCase):
    def test_sixty_days_less_a_day(self):
        self.assertEqual(la.expiry_date(5184000, dt.date(2026, 10, 10)), "2026-12-08")

    def test_crosses_a_year(self):
        self.assertEqual(la.expiry_date(5184000, dt.date(2026, 12, 20)), "2027-02-17")


class TestReceiver(unittest.TestCase):
    """The real HTTP server, on an ephemeral port, hit from this process."""

    def run_receiver(self, request_path, state="ok"):
        ports: list[int] = []
        ready = threading.Event()
        out: dict = {}

        def on_ready(port):
            ports.append(port)
            ready.set()

        def serve():
            try:
                out["code"] = la.wait_for_code(0, state, wait=10, ready=on_ready)
            except la.AuthError as err:
                out["error"] = str(err)

        t = threading.Thread(target=serve)
        t.start()
        self.assertTrue(ready.wait(5))
        status = body = None
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{ports[0]}{request_path}", timeout=5) as resp:
                status, body = resp.status, resp.read().decode()
        except urllib.error.HTTPError as err:
            status, body = err.code, err.read().decode()
        t.join(10)
        return out, status, body

    def test_a_good_redirect_gives_the_code(self):
        out, status, body = self.run_receiver("/callback?code=THECODE&state=ok")
        self.assertEqual(out, {"code": "THECODE"})
        self.assertEqual(status, 200)
        self.assertIn("close this tab", body)

    def test_a_forged_redirect_is_refused(self):
        out, status, _ = self.run_receiver("/callback?code=THECODE&state=forged")
        self.assertNotIn("code", out)
        self.assertIn("state", out["error"])
        self.assertEqual(status, 400)

    def test_the_page_escapes_what_it_shows(self):
        out, status, body = self.run_receiver("/callback?error=x&error_description=%3Cscript%3E&state=ok")
        self.assertNotIn("<script>", body)
        self.assertIn("&lt;script&gt;", body)

    def test_it_listens_on_localhost_only(self):
        src = (REPO_ROOT / "tools" / "linkedin_auth.py").read_text(encoding="utf-8")
        self.assertIn('HTTPServer(("127.0.0.1", port)', src)
        self.assertNotIn('HTTPServer(("0.0.0.0"', src)
        self.assertNotIn('HTTPServer(("", ', src)

    def test_times_out_when_nothing_arrives(self):
        with self.assertRaisesRegex(la.AuthError, "no redirect arrived"):
            la.wait_for_code(0, "ok", wait=0.2)


class TestPasteMode(unittest.TestCase):
    def paste(self, text, state="ok"):
        said = []
        return la.paste_for_code(8080, state, ask=lambda prompt: text, say=said.append), said

    def test_a_full_address_gives_the_code(self):
        code, _ = self.paste("http://localhost:8080/callback?code=THECODE&state=ok")
        self.assertEqual(code, "THECODE")

    def test_the_path_and_query_alone_also_work(self):
        code, _ = self.paste("/callback?code=THECODE&state=ok")
        self.assertEqual(code, "THECODE")

    def test_surrounding_spaces_are_ignored(self):
        code, _ = self.paste("  http://localhost:8080/callback?code=THECODE&state=ok \n")
        self.assertEqual(code, "THECODE")

    def test_a_forged_address_is_refused(self):
        with self.assertRaisesRegex(la.AuthError, "state"):
            self.paste("http://localhost:8080/callback?code=THECODE&state=forged")

    def test_a_refusal_from_linkedin_is_reported(self):
        with self.assertRaisesRegex(la.AuthError, "nope"):
            self.paste("http://localhost:8080/callback?error=access_denied&error_description=nope&state=ok")

    def test_nothing_pasted_is_an_error(self):
        with self.assertRaisesRegex(la.AuthError, "nothing was pasted"):
            self.paste("   ")

    def test_the_wrong_address_is_refused(self):
        with self.assertRaisesRegex(la.AuthError, "unexpected path"):
            self.paste("https://www.linkedin.com/feed/?code=THECODE&state=ok")

    def test_the_instructions_say_what_to_expect(self):
        _, said = self.paste("/callback?code=C&state=ok")
        text = "\n".join(said)
        self.assertIn("cannot be reached", text)
        self.assertIn("http://localhost:8080/callback?code=", text)


class TestModeChoice(unittest.TestCase):
    VALUES = {"LINKEDIN_ACCESS_TOKEN": TOKEN, "LINKEDIN_AUTHOR_URN": "urn:li:person:x",
              "LINKEDIN_TOKEN_EXPIRES": "2026-12-08", "refresh": False}

    def receiver_for(self, env, argv):
        base = {"LINKEDIN_CLIENT_ID": "cid", "LINKEDIN_CLIENT_SECRET": SECRET}
        with mock.patch.dict("os.environ", {**base, **env}, clear=False), \
                mock.patch.object(la, "authorise", return_value=self.VALUES) as auth, \
                redirect_stdout(io.StringIO()):
            la.main(argv)
        return auth.call_args.kwargs["receive"]

    def test_a_codespace_uses_paste_mode(self):
        self.assertIs(self.receiver_for({"CODESPACES": "true"}, []), la.paste_for_code)

    def test_elsewhere_the_local_receiver_is_used(self):
        env = {"CODESPACES": ""}
        self.assertIs(self.receiver_for(env, []), la.wait_for_code)

    def test_manual_forces_paste_mode(self):
        self.assertIs(self.receiver_for({"CODESPACES": ""}, ["--manual"]), la.paste_for_code)

    def test_listen_forces_the_local_receiver_in_a_codespace(self):
        self.assertIs(self.receiver_for({"CODESPACES": "true"}, ["--listen"]), la.wait_for_code)

    def test_the_two_flags_cannot_be_combined(self):
        with self.assertRaises(SystemExit), redirect_stderr(io.StringIO()):
            la.main(["--manual", "--listen"])


def fake_flow(token_reply=None, userinfo=None, receive_code="THECODE"):
    calls = {"exchange": [], "fetch": [], "opened": [], "said": []}

    def receive(port, state):
        calls["state"] = state
        return receive_code

    def exchange(url, fields):
        calls["exchange"].append((url, dict(fields)))
        return token_reply if token_reply is not None else {
            "access_token": TOKEN, "expires_in": 5184000, "scope": "openid,profile,w_member_social"}

    def fetch(url, token):
        calls["fetch"].append((url, token))
        return userinfo if userinfo is not None else {"sub": "782bbtaQ"}

    return calls, dict(open_browser=calls["opened"].append, say=calls["said"].append,
                       receive=receive, exchange=exchange, fetch=fetch, today=dt.date(2026, 10, 10))


class TestFlow(unittest.TestCase):
    def test_returns_the_three_values(self):
        calls, kw = fake_flow()
        v = la.authorise("cid", SECRET, 8080, **kw)
        self.assertEqual(v["LINKEDIN_ACCESS_TOKEN"], TOKEN)
        self.assertEqual(v["LINKEDIN_AUTHOR_URN"], "urn:li:person:782bbtaQ")
        self.assertEqual(v["LINKEDIN_TOKEN_EXPIRES"], "2026-12-08")
        self.assertFalse(v["refresh"])

    def test_exchanges_the_code_with_the_form_linkedin_documents(self):
        calls, kw = fake_flow()
        la.authorise("cid", SECRET, 8080, **kw)
        (url, fields), = calls["exchange"]
        self.assertEqual(url, "https://www.linkedin.com/oauth/v2/accessToken")
        self.assertEqual(fields, {"grant_type": "authorization_code", "code": "THECODE", "client_id": "cid",
                                  "client_secret": SECRET, "redirect_uri": "http://localhost:8080/callback"})

    def test_reads_the_member_id_with_the_new_token(self):
        calls, kw = fake_flow()
        la.authorise("cid", SECRET, 8080, **kw)
        self.assertEqual(calls["fetch"], [("https://api.linkedin.com/v2/userinfo", TOKEN)])

    def test_the_state_in_the_url_is_the_one_the_receiver_checks(self):
        calls, kw = fake_flow()
        la.authorise("cid", SECRET, 8080, **kw)
        url = calls["opened"][0]
        self.assertEqual(urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)["state"], [calls["state"]])
        self.assertGreaterEqual(len(calls["state"]), 24)

    def test_states_are_not_reused(self):
        states = set()
        for _ in range(5):
            calls, kw = fake_flow()
            la.authorise("cid", SECRET, 8080, **kw)
            states.add(calls["state"])
        self.assertEqual(len(states), 5)

    def test_the_secret_is_never_shown(self):
        calls, kw = fake_flow()
        la.authorise("cid", SECRET, 8080, **kw)
        self.assertFalse(any(SECRET in str(line) for line in calls["said"]))
        self.assertFalse(any(SECRET in url for url in calls["opened"]))

    def test_no_token_in_the_reply_is_an_error(self):
        calls, kw = fake_flow(token_reply={"expires_in": 1})
        with self.assertRaisesRegex(la.AuthError, "no access_token"):
            la.authorise("cid", SECRET, 8080, **kw)

    def test_a_token_without_the_posting_scope_is_explained(self):
        calls, kw = fake_flow(token_reply={"access_token": TOKEN, "scope": "openid,profile"})
        with self.assertRaisesRegex(la.AuthError, "Share on LinkedIn"):
            la.authorise("cid", SECRET, 8080, **kw)

    def test_no_member_id_is_explained(self):
        calls, kw = fake_flow(userinfo={})
        with self.assertRaisesRegex(la.AuthError, "OpenID Connect"):
            la.authorise("cid", SECRET, 8080, **kw)

    def test_a_refresh_token_is_noted_but_never_returned(self):
        calls, kw = fake_flow(token_reply={"access_token": TOKEN, "expires_in": 5184000,
                                           "refresh_token": "RT-should-not-leak", "scope": "w_member_social"})
        v = la.authorise("cid", SECRET, 8080, **kw)
        self.assertTrue(v["refresh"])
        self.assertNotIn("RT-should-not-leak", str(v))

    def test_a_missing_expiry_falls_back_to_sixty_days(self):
        calls, kw = fake_flow(token_reply={"access_token": TOKEN})
        v = la.authorise("cid", SECRET, 8080, **kw)
        self.assertEqual(v["LINKEDIN_TOKEN_EXPIRES"], "2026-12-08")


class TestReportAndMain(unittest.TestCase):
    VALUES = {"LINKEDIN_ACCESS_TOKEN": TOKEN, "LINKEDIN_AUTHOR_URN": "urn:li:person:x",
              "LINKEDIN_TOKEN_EXPIRES": "2026-12-08", "refresh": False}

    def test_report_names_each_value_and_where_it_goes(self):
        said = []
        la.report(self.VALUES, said.append)
        text = "\n".join(said)
        for needle in ("Settings > Environments > linkedin", "Secret    LINKEDIN_ACCESS_TOKEN",
                       "Secret    LINKEDIN_AUTHOR_URN     urn:li:person:x",
                       "Variable  LINKEDIN_TOKEN_EXPIRES  2026-12-08", TOKEN):
            self.assertIn(needle, text)

    def test_the_token_is_printed_once(self):
        said = []
        la.report(self.VALUES, said.append)
        self.assertEqual("\n".join(said).count(TOKEN), 1)

    def test_main_needs_both_credentials(self):
        err = io.StringIO()
        with mock.patch.dict("os.environ", {"LINKEDIN_CLIENT_ID": "cid", "LINKEDIN_CLIENT_SECRET": ""}), \
                mock.patch("getpass.getpass", return_value=""), redirect_stderr(err):
            self.assertEqual(la.main([]), 2)
        self.assertIn("both needed", err.getvalue())

    def test_main_reports_an_auth_error_without_the_secret(self):
        err = io.StringIO()
        with mock.patch.dict("os.environ", {"LINKEDIN_CLIENT_ID": "cid", "LINKEDIN_CLIENT_SECRET": SECRET}), \
                mock.patch.object(la, "authorise", side_effect=la.AuthError("LinkedIn refused the request: nope")), \
                redirect_stderr(err):
            self.assertEqual(la.main([]), 1)
        self.assertIn("nope", err.getvalue())
        self.assertNotIn(SECRET, err.getvalue())

    def test_main_prompts_for_the_secret_instead_of_taking_it_from_arguments(self):
        with mock.patch.dict("os.environ", {"LINKEDIN_CLIENT_ID": "cid", "LINKEDIN_CLIENT_SECRET": ""}), \
                mock.patch("getpass.getpass", return_value=SECRET) as gp, \
                mock.patch.object(la, "authorise", return_value=self.VALUES) as auth, \
                redirect_stdout(io.StringIO()):
            self.assertEqual(la.main([]), 0)
        gp.assert_called_once()
        self.assertEqual(auth.call_args[0][:2], ("cid", SECRET))


class TestSafetyOfTheSource(unittest.TestCase):
    SRC = (REPO_ROOT / "tools" / "linkedin_auth.py").read_text(encoding="utf-8")

    def test_it_writes_no_files(self):
        tree = ast.parse(self.SRC)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = getattr(node.func, "id", getattr(node.func, "attr", ""))
                self.assertNotIn(name, ("open", "write_text", "write_bytes", "mkdir"), ast.dump(node)[:80])

    def test_uses_only_the_standard_library(self):
        tree = ast.parse(self.SRC)
        stdlib = set(sys.stdlib_module_names)
        mods = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                mods |= {a.name.split(".")[0] for a in node.names}
            elif isinstance(node, ast.ImportFrom) and node.module:
                mods.add(node.module.split(".")[0])
        self.assertLessEqual(mods, stdlib | {"__future__"}, mods - stdlib)

    def test_the_secret_has_no_command_line_option(self):
        self.assertNotIn("--secret", self.SRC)
        self.assertNotIn("--client-secret", self.SRC)

    def test_the_credentials_page_points_at_this_tool(self):
        text = (REPO_ROOT / "docs" / "credentials.md").read_text(encoding="utf-8")
        self.assertIn("tools/linkedin_auth.py", text)


if __name__ == "__main__":
    unittest.main()
