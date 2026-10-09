# Credentials that expire: plans for `PROJECT_TOKEN` and LinkedIn

Two automations need a credential that GitHub cannot supply by itself, and both
credentials expire. This page is the plan for each: what breaks, how the owner
renews it, and how a failure is made visible instead of silent. Nothing here is
built yet; the build items are the roadmap issues named in each section. Written
2026-10-08.

| Credential | For | Lifetime | Roadmap |
|---|---|---|---|
| `PROJECT_TOKEN` (classic personal access token, `project` scope) | `project-board.yml` keeps the public Project board in step with the roadmap issues | Chosen by the owner when the token was created (not readable from the repository) | [#496](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/496), 2026.12 |
| LinkedIn access token (OAuth, `w_member_social`) | Posting a data release to LinkedIn after the owner approves | **60 days** (LinkedIn's authorization-code flow documents 60 days for access tokens) | [#515](https://github.com/DaLuSt/Data-Initiatives-Atlas/issues/515), 2027.01 |

Common rules for both: the secret lives only in GitHub (*Settings → Secrets and
variables → Actions*), never in the repository, an issue, a workflow log or the
Claude environment; the **expiry date is not a secret** and is kept in a
repository *variable* beside it so a workflow can read it; and a workflow that
cannot do its job says so on a page the owner already looks at (an issue), not
only in a log.

---

## 1. `PROJECT_TOKEN` expiry plan (#496)

### What breaks, and what does not

Only the roadmap board goes stale. Releases, tags, the site, the validation
checks and the LinkedIn drafts do not use this token. Today an expired token
makes `tools/project_board.py` exit 1 (an HTTP 401 becomes a `GitHubError`), so
the *Roadmap board* run turns red; but a red scheduled run is easy to miss, and a
**missing** secret is reported as a success on purpose (the workflow does
nothing until the owner has set it up). That second case is the quiet one: a
deleted or renamed secret looks the same as "never set up".

### Decisions

1. **Expiry.** Give the token a fixed expiry (90 days is a reasonable middle:
   long enough not to nag, short enough that a leaked token dies). A token
   without an expiry removes the problem but leaves a long-lived credential with
   access to all of the owner's projects; not recommended.
2. **Record the date.** The owner stores the expiry date as the repository
   variable `PROJECT_TOKEN_EXPIRES` (`YYYY-MM-DD`). GitHub does not let a
   workflow read a token's own expiry, so this variable is the only way to know
   it in advance.
3. **Two alarms, one issue.** One open issue titled *Roadmap board sync needs
   attention* is the single place the owner is told. It is opened (or commented
   on) by the workflow and closed by it when a run succeeds again.
4. **Calendar reminder.** The owner also puts a reminder in their own calendar
   14 days before the date. This is the only alarm that does not depend on the
   workflow running.

### What to build (2026.12, #496)

All in `.github/workflows/project-board.yml` and `tools/project_board.py`, with
tests in `tools/test_project_board.py` and `tools/test_release.py`:

1. **Preflight step** (before the sync). Reads `PROJECT_TOKEN_EXPIRES`:
   - more than 14 days away: nothing;
   - 14 days or fewer away: a warning annotation, and the issue gets a comment
     "The token expires on DATE";
   - past: the step fails with a clear message.
   If the variable is unset, it prints a notice (as today) and does not fail.
2. **A missing secret is an error once the board is set up.** Add a repository
   variable `BOARD_SYNC_ENABLED=true` when the setup is finished. With it set, an
   empty `PROJECT_TOKEN` fails the run (a deleted secret is then visible).
3. **Failure issue.** A final step with `if: failure()` and `issues: write`:
   find the open issue by exact title; if there is none, open it with the run
   link and the first error line; if there is, add a comment. A step with
   `if: success()` closes it. Idempotent, like the LinkedIn-draft step in
   `release-publish.yml`.
4. **Tests.** The preflight date logic as a pure function (14-day boundary, past,
   unset, malformed); the workflow's safety properties as the existing tests do
   (the secret appears only in `env:`, `issues: write` only where needed).

### Rotation steps (owner, about 5 minutes; do it before the date)

1. Create a new classic token at <https://github.com/settings/tokens> with
   **only** the `project` scope and a new expiry. Copy it once.
2. *Settings → Secrets and variables → Actions → Secrets*: update `PROJECT_TOKEN`
   with the new value.
3. Same page, *Variables*: set `PROJECT_TOKEN_EXPIRES` to the new date.
4. *Actions → Roadmap board → Run workflow* with *dry_run* ticked; open the log
   and check it ends with "0 issue(s) would change" or a plausible list.
5. Delete the old token in GitHub's token settings.
6. Move the calendar reminder.

If the board has already gone stale, run the workflow once with *dry_run*
unticked; it catches up in one pass (it is idempotent).

### Longer term

A GitHub App would not expire this way, but as far as GitHub documents it an
App installation cannot be given access to a **user-owned** project; moving the
project (and probably the repository) to an organisation would allow it. Not
planned; revisit only if rotating the token every few months becomes a burden.

---

## 2. LinkedIn developer app plan (#515)

Goal: when a data release is published, the draft the workflow already writes
into a `linkedin`-labelled issue is posted to LinkedIn, **only after the owner
approves**. Until then posting by hand from the issue keeps working.

### Decision to make first: personal profile or company page

| | Personal profile | Company page |
|---|---|---|
| Permission | `w_member_social`, from the self-serve *Share on LinkedIn* product | `w_organization_social`, restricted to people with an admin-type role on the page |
| Setup | Quickest | Needs the page, a role on it, and (not confirmed) possibly LinkedIn's approval for the product; check when creating the app |
| Who the post is "from" | The owner | The Atlas |

**Recommendation:** start with the personal profile (nothing to wait for), keep
the author ID in a secret so a later move to a company page is a configuration
change plus one new permission, not a rewrite. The app form requires a LinkedIn
Page to associate the app with, even for personal posting; step 0 below creates one
for an individual developer. Check the API terms on the screen when creating the app.

### Steps for the owner (about 30 minutes, once; can be done at any time)

0. **Create a LinkedIn Page first if you have none** (an individual developer
   needs one; a registered company is not required). LinkedIn: *For Business →
   Create a Company Page*, type **Company**, free, desktop or iOS (not Android).
   Name it after the project ("Data Initiatives Atlas"), website
   `https://dalust.github.io/Data-Initiatives-Atlas/`, an industry such as
   "Technology, Information and Internet", and the Atlas logo. The box that
   confirms you may act on behalf of the organisation is true here: you own the
   project. You become the Page's super admin, so approving the app's link to it
   (which has 30 days) is yours. **The link is permanent**: an app cannot be moved
   to another Page, so pick a name you can live with. The Page is only formal
   here; posts still go to your own profile (`w_member_social`).
1. Go to <https://developer.linkedin.com/>, *My apps → Create app*. Name it
   after the Atlas; select that Page as the app's Page; upload the logo; accept
   the terms. If the portal asks you to verify the app with the Page, do it as the
   Page's admin (follow what the portal shows).
2. On the app's *Products* tab, add **Share on LinkedIn** (gives
   `w_member_social`) and **Sign In with LinkedIn using OpenID Connect** (gives
   the member's ID).
3. On the *Auth* tab, add one redirect URL. For a one-off local script,
   `http://localhost:8080/callback` is enough. Note the Client ID and Client
   Secret; the secret is a credential.
4. Run the authorisation once, on your own computer (`tools/linkedin_auth.py`,
   built 2026-10-09; see "Running the authorisation script" below). LinkedIn shows
   a consent screen asking for `openid profile w_member_social`; approve it.
5. Add to GitHub, *Settings → Environments → New environment* named `linkedin`,
   with **Required reviewers** set to the owner. Then in that environment:
   secrets `LINKEDIN_ACCESS_TOKEN` and `LINKEDIN_AUTHOR_URN`
   (`urn:li:person:<id>`), and a variable `LINKEDIN_TOKEN_EXPIRES` (`YYYY-MM-DD`,
   today plus 60 days).

Do not put the Client Secret in GitHub unless a refresh flow needs it (see the
open question below); the access token alone is enough to post.

### Running the authorisation script

`tools/linkedin_auth.py` is built (standard library only; tests in
`tools/test_linkedin_auth.py`). It opens the consent URL with a random `state`,
receives the redirect on `127.0.0.1` only, exchanges the code for the token, reads
the member ID from the OpenID *userinfo* endpoint, and prints the token, the
`urn:li:person:…` value and the expiry date for you to paste into GitHub. It
writes nothing to disk and never prints the Client Secret.

```
export LINKEDIN_CLIENT_ID=<the Client ID from the Auth tab>
python3 tools/linkedin_auth.py        # asks for the Client Secret (hidden)
```

**In a GitHub Codespace** (or anywhere your browser cannot reach the program's
`localhost`) the script switches to paste mode by itself: it prints the LinkedIn
address, you open it in your own browser and approve, the browser then says the page
cannot be reached, and you copy that address (it starts with
`http://localhost:8080/callback?code=`) from the address bar and paste it into the
terminal. The code in it is single-use and useless without the Client Secret. Force
it with `--manual`, or force the normal receiver with `--listen`. Set the Client ID
with `export LINKEDIN_CLIENT_ID=...` in the Codespace terminal; the Client Secret
is typed at the hidden prompt. Close the Codespace afterwards (the terminal
history holds the token) and delete it if you will not use it again.

Use `--port N` if 8080 is busy (and add that redirect URL in the app). If it
reports that the token lacks `w_member_social` or that no member ID came back,
the matching product has not been added to the app (step 2). Run it again in
about 50 days to renew the token.

### What is still to build (2027.01, #515)

1. ~~`tools/linkedin_auth.py`~~ built 2026-10-09 (above).
2. **`tools/linkedin_post.py`**: posts text to `POST https://api.linkedin.com/rest/posts`
   with the headers the Posts API requires (`Authorization: Bearer …`,
   `Linkedin-Version: YYYYMM`, `X-Restli-Protocol-Version: 2.0.0`), a text-only
   body (`author`, `commentary`, `visibility: PUBLIC`, `distribution.feedDistribution:
   MAIN_FEED`, `lifecycleState: PUBLISHED`), and treats `201` with an `x-restli-id`
   response header as success. HTTP is injectable, so it is tested against a
   mock, like `project_board.py`.
3. **Workflow job** after the draft step in `release-publish.yml`, with
   `environment: linkedin` (so it waits for the owner's approval), reading the
   **issue body at the moment of approval** so that anything the owner edited in
   the draft is what gets posted. Draft limit: 3,000 characters, which the draft
   rule already respects.
4. **Result.** On success: comment on the issue with the post link (built from
   the returned ID), close it. On failure: comment with the error (never the
   token), leave it open, and say "post by hand".
5. **Safety tests**, as for the board: the token appears only in `env:`, the job
   runs only through the protected environment, no other workflow can post, a
   draft over 3,000 characters is refused before any request.

### The 60-day token

LinkedIn issues access tokens with a 60-day life, so an ordinary app needs the
owner to authorise again about every two months. Plan:

- `LINKEDIN_TOKEN_EXPIRES` is read when the draft issue is opened; if it is within
  14 days, the issue starts with "The LinkedIn token expires on DATE; run
  `tools/linkedin_auth.py` and update the environment secret."
- A `401` on posting is reported on the issue in the same words, and the post
  is left for the owner to make by hand.
- Re-authorising is the owner's 5-minute step 4–5 above.
- **Open question for the build:** the token response may also carry a refresh
  token. LinkedIn's documentation says refresh tokens are available only to some
  products and partners; check what the Atlas's app receives. If it gets one,
  the job could renew the token itself and the reminder becomes a fallback; if
  not, the manual renewal above stays.

### Decision and alternatives considered

**Decided 2026-10-09: the owner's own LinkedIn developer app, as above.** It costs
nothing, keeps the account and the approval step inside GitHub, and needs a
re-authorisation about every 60 days.

Considered and set aside:

- **Metricool** (connected to Claude on 2026-10-09). Its free plan does not
  include LinkedIn; connecting LinkedIn needs a paid plan (Starter, about $20 a
  month on annual billing, per Metricool's own pricing page). The connection
  would also have needed a scheduled Claude session rather than a GitHub workflow.
  The connector can stay connected or be removed; nothing here depends on it.
- **Buffer, free plan.** Can schedule LinkedIn posts (3 channels, 10 queued posts
  per channel, per Buffer's published limits), but no Buffer connector is
  available to a Claude session, so the text would be pasted in by hand and
  nothing is automated.
- **A no-code connector (Zapier, Make).** Quicker, but it gives a third party
  access to the owner's LinkedIn account and has free-tier limits that were not
  checked.
- **Posting by hand** from the draft issue. Free and works today; this stays the
  fallback whenever the token has expired.

Posting without the approval step is excluded: a LinkedIn post is public and
cannot be fully retracted.

### Sources

LinkedIn, *Share on LinkedIn*, *Authorization code flow* (60-day access-token
life; the consent and `state` parameters) and *Posts API* (endpoint, required
headers, `201` with `x-restli-id`, `w_member_social` and `w_organization_social`),
on Microsoft Learn, read 2026-10-08. LinkedIn changes versions and products;
re-read them when building.
