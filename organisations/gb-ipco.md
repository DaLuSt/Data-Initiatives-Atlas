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
verification: search-only

start_date: null
end_date: null
last_verified: "2026-08-18"
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
relationships:
  - type: governed-by
    target: GB-IPA-2016
    source: fact
    evidence: "The Investigatory Powers Commissioner's Office is an independent oversight role created by the Investigatory Powers Act 2016, and replaces various other commissioner roles related to surveillance; the role merged the previous offices of the Office of the Surveillance Commissioners, the Interception of Communications Commissioner's Office and the Intelligence Service Commissioner's Office into one office (ipco.org.uk 'What we do'; en.wikipedia.org 'Investigatory Powers Commissioner'; wiki.openrightsgroup.org). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: GB-MI5
    source: fact
    evidence: "IPCO oversees the use of covert powers by over 600 public authorities, which can be broadly categorised into six groups, of which the first is the intelligence agencies (ipco.org.uk 'What we do'; ipco.org.uk 'Investigatory Powers'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: GB-SIS
    source: fact
    evidence: "IPCO oversees the use of covert powers by over 600 public authorities, of which the first category is the intelligence agencies (ipco.org.uk 'What we do'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null
  - type: applies-to
    target: GB-GCHQ
    source: fact
    evidence: "IPCO oversees the use of covert powers by over 600 public authorities, of which the first category is the intelligence agencies; GCHQ's own legal framework page places the Investigatory Powers Act 2016 regime at the centre of its governance (ipco.org.uk 'What we do'; gchq.gov.uk 'Legal Framework'). NOT READ — search-only."
    confidence: medium
    valid_from: null
    valid_until: null

sources:
  - title: "What we do"
    url: "https://www.ipco.org.uk/what-we-do/"
    publisher: "Investigatory Powers Commissioner's Office (IPCO)"
  - title: "Investigatory Powers"
    url: "https://www.ipco.org.uk/investigatory-powers/"
    publisher: "Investigatory Powers Commissioner's Office (IPCO)"
  - title: "Investigatory Powers Commissioner"
    url: "https://en.wikipedia.org/wiki/Investigatory_Powers_Commissioner"
    publisher: "Wikipedia"
---

# Investigatory Powers Commissioner's Office (IPCO)

> **Sourcing caveat.** Compiled from search-engine results only; the cited
> pages were confirmed to exist but were not read. `verification:
> search-only`.

## Description

IPCO is the UK's independent oversight body for covert investigatory powers,
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

## Not modelled

- The **Investigatory Powers Tribunal**, the judicial body that hears
  complaints. IPCO oversees; the Tribunal adjudicates. They are separate,
  and only IPCO is modelled here.
- The **double lock**, the IPA's warrant mechanism under which a Secretary
  of State's decision is reviewed by a Judicial Commissioner. This is the UK
  analogue of [[NL-TIB]]'s binding prior review, and it is **not asserted**
  because no source read in this batch describes the mechanism.

## Relationships

- `governed-by` [[GB-IPA-2016]].
- `applies-to` [[GB-MI5]], [[GB-SIS]] and [[GB-GCHQ]].

## Sources

Listed in frontmatter.
