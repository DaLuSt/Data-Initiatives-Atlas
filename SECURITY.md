# Security Policy

## What this project is, and what that means for security

The Data Initiatives Atlas is **a dataset, not a service**. Understanding the
shape of it makes it much easier to tell what is worth reporting:

| Part | What it is | Security relevance |
|---|---|---|
| The entity files | Markdown + YAML in Git | Content integrity, not code execution |
| `validation/`, `tools/` | Python 3.12, PyYAML only | Runs locally and in CI, on repository content |
| `site/` | A **static** page — no backend, no database, no accounts | Client-side only |
| `.github/workflows/` | Validation on PRs, build + Pages deploy on `main` | Supply chain and permissions |

**There is no server.** The published Atlas is HTML, CSS, one JavaScript file
and two JSON payloads on GitHub Pages. It has no login, stores nothing about
you, and calls nothing but itself.

## Reporting a vulnerability

**Please report privately, not in a public issue.**

👉 **[Open a private security report](https://github.com/DaLuSt/Data-Initiatives-Atlas/security/advisories/new)**

That form is GitHub's private vulnerability reporting. Only the maintainer can
see it, and it lets us discuss and fix an issue before anything is public.

> **Maintainer note:** private reporting must be switched on for the link
> above to work — *Settings → Advanced Security → Private vulnerability
> reporting → Enable*. If it is off, the link 404s for reporters.

If you cannot use that form, message
[@DaLuSt](https://github.com/DaLuSt) on GitHub and ask for a private channel.
**Do not put vulnerability details in a public issue, pull request or
discussion.**

### What to include

Whatever you have. A useful report usually has:

* what you found and where (file, URL, or workflow);
* how to reproduce it, or a proof of concept;
* what an attacker could actually achieve;
* any suggested fix, if one is obvious to you.

### What to expect

This project is maintained by one person in their own time, so please read
these as honest intentions rather than a commercial SLA:

| | Target |
|---|---|
| First acknowledgement | within **7 days** |
| Assessment and a plan | within **30 days** |
| Fix for a confirmed issue | as fast as severity warrants |

If you have had no response in 14 days, please follow up — a missed
notification is far more likely than a decision to ignore you.

We will credit you in the advisory and the commit unless you would rather stay
anonymous. There is **no bug bounty**; this is an unfunded open-data project.

## Supported versions

There are no releases and no version branches. **`main` is the only supported
state**, and the deployed site is always built from it. Fixes land on `main`;
there is nothing to backport to.

## Scope

### In scope

* **The published site** — anything that lets a page from
  `dalust.github.io/Data-Initiatives-Atlas` execute unintended script, exfiltrate
  data, or attack a visitor. Cross-site scripting through entity content is the
  realistic case: entity names, labels, IDs and evidence strings come from
  repository files and are rendered into the DOM.
* **The generator and validators** — anything that makes `tools/build_graph.py`
  or the `validation/` scripts execute code, read or write outside the
  repository, or hang indefinitely when run against a crafted entity file.
  These scripts are run by contributors on branches they may not have written.
* **The GitHub Actions workflows** — privilege escalation, secret exposure, or
  a path by which a pull request from a fork could influence what is deployed
  to Pages.
* **The vendored dependency** — `site/vendor/cytoscape.min.js`
  (Cytoscape.js 3.34.1, MIT). If a vulnerability is published against that
  version, telling us is genuinely useful.

### Out of scope

* **Reports about the organisations, laws or systems the Atlas describes.**
  The Atlas is a catalogue. A vulnerability in a national identity platform
  described by an entity file is not a vulnerability in this repository —
  report it to that system's operator through their own disclosure process.
* **The external sites we link to.** The Atlas cites roughly 850 URLs across
  330-odd hosts. Their availability, TLS configuration and content are not
  ours.
* **Missing security headers on GitHub Pages.** We do not control the
  hosting's response headers.
* **Anything requiring push access to this repository.** A maintainer being
  able to commit a malicious file is the trust model, not a vulnerability.
* Automated scanner output with no demonstrated impact.

## Current posture of the published site

Verifiable from `site/` in a couple of minutes, and stated here so a reporter
does not have to rediscover it:

* **No cookies, no `localStorage`, no `sessionStorage`.** The page keeps no
  state between visits.
* **No analytics, no telemetry, no beacons, no third-party scripts or fonts.**
* **No external network requests.** The only `fetch()` calls are two
  same-origin requests, for `graph.json` and `details.json`.
* **No inline event handlers** in `index.html`.
* **No user input reaches a server**, because there is no server. The search
  box filters an already-downloaded JSON payload in memory.
* **Dependencies are vendored, not fetched from a CDN.** Cytoscape.js is
  committed at `site/vendor/` with its licence and version alongside it, so the
  deployed bytes are the reviewed bytes.
* `tools/test_build_graph.py` includes a check —
  `test_no_external_script_or_style_references` — that fails the build if a
  third-party script or stylesheet reference is ever introduced.

Content is escaped through a single `esc()` helper before being written into
the DOM. **If you find a path where entity content reaches the page
unescaped, that is exactly the kind of report this policy is for.**

## Dependencies

Deliberately few, and all pinned or vendored:

* **Python:** PyYAML (`validation/requirements.txt`). Nothing else.
* **JavaScript, runtime:** Cytoscape.js 3.34.1, MIT, **vendored** in
  `site/vendor/`. See `docs/graph-development.md` for the upgrade procedure.
* **JavaScript, test-only:** Playwright, installed with `--no-save` and never
  committed. It is not part of CI and not shipped.

## Data integrity — the other kind of report

For this project, the closest analogue to a vulnerability is often **a false
claim presented as sourced fact**: a citation that does not support the
statement attached to it, an `evidence` string describing something the source
does not say, a `source: fact` edge that is really an interpretation, or a
fabricated URL.

That is not a security vulnerability and does not need a private report.
**Please open a normal public issue**, or a pull request that fixes it. Public
is better here — the correction is the point, and the repository is designed to
show its own uncertainty rather than hide it.

Two things worth knowing before you report one:

* **Most entities are not verified, and say so.** As of the most recent batch,
  **251 of 258 entities** carry `verification: search-only`: their cited URLs
  were confirmed by a search index to exist but **were not read**, because the
  authoring environment blocked page retrieval. Every such entity carries a
  visible sourcing caveat, `last_verified: null` and no `accessed` dates. An
  entity being thinly sourced is a **known, documented state**, not a defect
  to report — see `discovery/unresolved.md` and
  `discovery/reverification-allowlist.md`.
* **A source that contradicts an entity is a good issue.** That is the useful
  report: "this entity says X, this primary source says Y." Include the URL.

Deliberate fabrication of sources or evidence is a `CODE_OF_CONDUCT.md`
matter, and is handled as one.

## Disclosure policy

We follow coordinated disclosure. We will agree a timeline with you, aiming to
publish a GitHub Security Advisory once a fix is available. If an issue is
being actively exploited, or a fix proves impossible, we will publish what
users need to protect themselves rather than stay quiet.

## Licence

This repository is CC0 1.0 (`LICENSE`). Nothing in this policy limits what you
may do with the data — it is about how to tell us when something is broken.
