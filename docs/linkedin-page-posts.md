# Posts for the LinkedIn Page

Drafts for the **Data Initiatives Atlas** LinkedIn Page, written 2026-10-09, with the figures of
that day (747 entities, 9,435 connections, 58 countries; the live counts are on the site). They
are plain text, because LinkedIn does not render Markdown, and each is under LinkedIn's
3,000-character limit. Read them, change what you like, and post them from the Page.

## How they get onto the Page

Posts to the **personal profile** are automated (the release workflow, `docs/credentials.md`
section 2). Posts to a **Page** are not, and probably should not be: a Page needs the
*Community Management API* product (permission `w_organization_social`), and LinkedIn reviews that
request. Its review looks at an approved use case, a verified business email, a verified
organisation and website domain, and an app verified by the Page (LinkedIn's own pages on access to
the Community Management API, read 2026-10-09). An unfunded open-data project may well not pass it,
and the token on file has the personal permission only (`w_member_social`), which does not post to a
Page. For about one post a month, posting by hand from the Page is the honest choice. If you would
rather apply, say so and it can be set up as a new roadmap item.

## 1. Introduction post

```text
Introducing the Data Initiatives Atlas: an open map of who governs data, and how it all connects.

Data rules do not stop at borders. A national open-data law may implement an EU directive, which sits beside a UN framework, which a standards body turns into practice. The Atlas puts all of that in one connected, searchable picture.

Right now it holds 747 entities and 9,435 connections across 58 countries: laws, policies, standards, frameworks, programmes, organisations and data spaces, at UN, Council of Europe, EU, national and regional level.

What makes it different:
• Every relationship says where it comes from: a sourced fact with its evidence, or the Atlas's own interpretation, labelled as such.
• Every entity is checked against a primary source that someone has actually opened and read.
• It is a plain Git repository of Markdown files, released under CC0. Take it, reuse it, build on it.
• The site needs no install and no account: search, filter, compare countries, follow a path from one instrument to another.

It is built in the open and it grows every week. If you spot a mistake or know a body we are missing, the GitHub repository has a correction form, and pull requests are welcome.

Explore the Atlas: https://dalust.github.io/Data-Initiatives-Atlas/
Source and data: https://github.com/DaLuSt/Data-Initiatives-Atlas

#opendata #datagovernance #digitalgovernment #knowledgegraph
```

## 2. The latest release (data release 2026.10.2)

This is the text that was posted from the profile on 2026-10-09. For later releases the release
workflow writes a fresh draft into the issue "Post data release X on LinkedIn"; copy it from there.

```text
Data Initiatives Atlas: data release 2026.10.2

In the Atlas now: 745 entities (+5), 1,576 typed relationships (+11), 58 countries.

What changed:
• The List view can be downloaded as a CSV file
• 26 more bodies and laws now show an English name, each taken from the body's own English site or an official translation
• The UK's new Information Commission (successor to the ICO since 30 September 2026) and three more UK network-security authorities are in
• France's link to the EU Open Data Directive now rests on the Commission's own list of notified measures

Explore the Atlas: https://dalust.github.io/Data-Initiatives-Atlas/
Release notes: https://github.com/DaLuSt/Data-Initiatives-Atlas/releases/tag/data-2026.10.2

#opendata #datagovernance #digitalgovernment
```

## Before posting

- The figures in post 1 are as of 2026-10-09; update them to the live counts on the site if you
  post later.
- A post on a Page can carry an image. The Atlas logo (a small network of five coloured nodes) was
  made for the LinkedIn app and suits it.
