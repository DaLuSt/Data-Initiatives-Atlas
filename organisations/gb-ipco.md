---
id: GB-IPCO
type: organisation
name: Investigatory Powers Commissioner's Office
alternative_names:
  - IPCO
  - Investigatory Powers Commissioner
description: >
  Independent UK oversight body created by the Investigatory Powers Act
  2016, which merged the Office of Surveillance Commissioners, the
  Interception of Communications Commissioner's Office and the Intelligence
  Services Commissioner's Office. It oversees the use of covert powers by
  over 600 public authorities, the intelligence agencies among them.

level: national
country: GB
region: null

status: active
confidence: medium
coverage: medium
verification: primary-source
start_date: null
end_date: null
last_verified: "2026-11-22"
previous_version: null
successor: null

domains:
  - DOMAIN-NATIONAL-SECURITY
organisations: []
related_entities:
  - GB-IPA-2016
  - GB-MI5
  - GB-SIS
  - GB-GCHQ
  - GB-ISC
  - GB-DI
  - GB-IPT
relationships:
  - type: governed-by
    target: GB-IPA-2016
    source: fact
    evidence: "The Investigatory Powers Act 2016, section 227, read directly 2026-11-22 on legislation.gov.uk: '(1) The Prime Minister must appoint— (a) the Investigatory Powers Commissioner, and (b) such number of other Judicial Commissioners as the Prime Minister considers necessary', and '(2) A person is not to be appointed ... unless the person holds or has held a high judicial office'. The office's history (the three offices it merged) is in the prose. A Wikipedia citation was dropped from this evidence on 2026-11-22 (roadmap #767)."
    confidence: high
    valid_from: null
    valid_until: null
  - type: applies-to
    target: GB-MI5
    source: fact
    evidence: "Confirmed by reading ipco.org.uk's 'What we do' page (2026-08-22): 'At IPCO, we oversee the use of covert investigatory powers by more than 600 public authorities, including the UK’s intelligence agencies, law enforcement agencies, police, councils and prisons.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: GB-SIS
    source: fact
    evidence: "Confirmed by reading ipco.org.uk's 'What we do' page (2026-08-22): 'At IPCO, we oversee the use of covert investigatory powers by more than 600 public authorities, including the UK’s intelligence agencies, law enforcement agencies, police, councils and prisons.'"
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: GB-GCHQ
    source: fact
    evidence: "Confirmed by reading ipco.org.uk's 'What we do' page and gchq.gov.uk's 'Legal Framework' page (2026-08-22): IPCO oversees 'more than 600 public authorities, including the UK's intelligence agencies', and GCHQ's own page names the Investigatory Powers Act 2016 as the regime governing its use of investigatory powers."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: GB-DI
    source: fact
    evidence: "CLOSES A PREVIOUSLY-FLAGGED GAP (GB-MI5's own 'Not modelled' section). Confirmed by reading gov.uk's own 'Defence Intelligence' group page directly (2026-09-06): DI's activity 'must comply with' the Investigatory Powers Act 2016, and external oversight is provided by 'the Investigatory Powers Commissioner.'"
    confidence: medium
    valid_from: null
    valid_until: null

  - type: related-to
    target: GB-IPA-AMENDMENT-2024
    source: fact
    evidence: "The Investigatory Powers (Amendment) Act 2024, read directly 2026-11-23 on legislation.gov.uk: its Part 2 is headed 'Oversight arrangements' (section 7, Deputy Investigatory Powers Commissioners; 8, delegation of functions; 9, Temporary Judicial Commissioners; 10, main functions of the Investigatory Powers Commissioner). Section 10 amends section 229 of the 2016 Act, inserting subsection (3E): 'The Investigatory Powers Commissioner must keep under review (including by way of audit, inspection and investigation) compliance by any part of His Majesty's forces, or by any part of the Ministry of Defence, with policies governing— (a) the use of surveillance outside the United Kingdom, and (b) the use and conduct of covert human intelligence sources outside the United Kingdom'. `related-to`, not `governed-by`: the 2024 Act amends the Commissioner's functions in [[GB-IPA-2016]], which is the governing edge. The commencement date of Part 2 was not read, so `valid_from` is unset."
    confidence: high
    valid_from: null
    valid_until: null
sources:
  - title: "Investigatory Powers (Amendment) Act 2024, section 10 (as enacted)"
    url: "https://www.legislation.gov.uk/ukpga/2024/9/section/10/enacted"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-11-23"
  - title: "Investigatory Powers Act 2016, section 227"
    url: "https://www.legislation.gov.uk/ukpga/2016/25/section/227"
    publisher: "legislation.gov.uk (The National Archives)"
    accessed: "2026-11-22"
  - title: "What we do"
    url: "https://www.ipco.org.uk/what-we-do/"
    publisher: "Investigatory Powers Commissioner's Office (IPCO)"
    accessed: "2026-08-22"
  - title: "Investigatory Powers"
    url: "https://www.ipco.org.uk/investigatory-powers/"
    publisher: "Investigatory Powers Commissioner's Office (IPCO)"
    accessed: "2026-08-22"
  - title: "Investigatory Powers Commissioner"
    url: "https://en.wikipedia.org/wiki/Investigatory_Powers_Commissioner"
    publisher: "Wikipedia"
    accessed: "2026-08-22"
  - title: "The Double Lock"
    url: "https://www.ipco.org.uk/what-we-do/the-double-lock/"
    publisher: "Investigatory Powers Commissioner's Office (IPCO)"
    accessed: "2026-09-05"
---

# Investigatory Powers Commissioner's Office (IPCO)

> **Verified 2026-08-22.** ipco.org.uk's own pages and en.wikipedia.org's
> "Investigatory Powers Commissioner" article were read directly and
> confirmed the claims below, verbatim in places.
>
> **Updated 2026-09-05**: IPCO's own dedicated "double lock" page,
> previously unread, describes the warrant-review mechanism this entity
> had flagged as unsourced.

## Description

Confirmed verbatim on ipco.org.uk's "What we do" page (2026-08-22): "At
IPCO, we oversee the use of covert investigatory powers by more than 600
public authorities, including the UK's intelligence agencies, law
enforcement agencies, police, councils and prisons." IPCO is the UK's
independent oversight body for covert investigatory powers,
created by [[GB-IPA-2016]].

## The widest remit of any oversight body in this batch

Every other overseer here watches intelligence services and nothing else.
IPCO oversees **over 600 public authorities**, in six broad groups:
intelligence agencies; police and law enforcement; local authorities;
prisons; warrant-granting departments; and other public authorities.

That difference follows from what the UK legislated. [[GB-IPA-2016]] governs
**powers**, not bodies — so its overseer necessarily follows the powers
wherever they are used, including into a local council. [[FR-CNCTR]], built
on the same powers-not-bodies principle in
[[FR-LOI-RENSEIGNEMENT-2015]], watches six named services; IPCO watches
whoever holds the power.

The three `applies-to` edges asserted here therefore cover the intelligence
agencies only, and are a small fraction of IPCO's actual remit — the rest of
those 600 authorities are not Atlas entities.

## It replaced three offices at once

IPCO merged:

- the Office of Surveillance Commissioners,
- the Interception of Communications Commissioner's Office, and
- the Intelligence Services Commissioner's Office,

along with the Office for Communications Data Authorisations. The UK's
pre-2016 oversight was **fragmented by power type**; the 2016 act
consolidated it into one office — the opposite of Germany's direction of
travel, where [[DE-UKR]] was added alongside [[DE-PKGR]] rather than
absorbing it.

## The double lock, described 2026-09-05

Confirmed by reading IPCO's own dedicated "The Double Lock" page directly:
"The 'double-lock' refers to the review of applications by our Judicial
Commissioners for warrants allowing public authorities to use the most
intrusive investigatory powers." The mechanism runs in two stages —
public authorities first submit applications to a minister (or, for
certain warrants, a senior officer); a Judicial Commissioner then
independently reviews the application, checking that the warrant "is
necessary" for one of the statutory purposes and "is proportionate to
what it intends" to achieve. **Only with the Commissioner's approval can
a warrant be issued.** A narrow urgency exception allows a warrant to be
issued first, with the Commissioner then notified and empowered to
"approve or quash the warrant or authorisation after it has been
issued."

This is the UK analogue of [[NL-TIB]]'s binding prior review — a body
independent of the executive with a genuine veto, not merely an
after-the-fact overseer. No relationship type or new entity is added for
the Judicial Commissioners: they are a function IPCO's own governance
carries, not a separate Atlas body, and the mechanism is recorded here in
prose rather than as a graph edge, since no relationship type in
`metadata/relationship-types.md` expresses a binding co-approval
requirement between an office and a class of decisions.

## Not modelled

- **Closed 2026-09-17**: the Investigatory Powers Tribunal is now
  [[GB-IPT]]. IPCO oversees; the Tribunal adjudicates. They are
  separate bodies with separate entities now.

## Relationships

- `governed-by` [[GB-IPA-2016]].
- `applies-to` [[GB-MI5]], [[GB-SIS]], [[GB-GCHQ]] and [[GB-DI]] — the
  last added 2026-09-06.

## Sources

Listed in frontmatter. The double-lock page added and read directly
2026-09-05.
