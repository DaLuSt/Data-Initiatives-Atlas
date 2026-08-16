# Re-verification Allowlist

> **Generated file — do not hand-edit.** Regenerate with
> `python tools/source_hosts.py --markdown -o discovery/reverification-allowlist.md`

Generated: 2026-08-16

## Why this exists

**172 of the Atlas's 178 entities have never had a cited source read.** Their `sources:` URLs were confirmed to exist by a search index and nothing more, which is what `verification: search-only` records.

Closing that debt — the re-verification pass — needs outbound HTTPS to the hosts those URLs point at. In an environment with a restricted egress policy, this is the allowlist to request. A denial shows up as `403 to CONNECT` from the proxy, which is an environment-level network policy and cannot be changed from inside a session. See `discovery/unresolved.md` for the standing record of the sourcing debt.

The Atlas currently cites **533 source URLs** across **202 hosts**, collapsing to **158 registrable domains**.

## Highest value first

Allowing just these covers the bulk of the pass:

| Domain | URLs | Entities |
|---|---|---|
| `europa.eu` | 68 | 43 |
| `bund.de` | 34 | 16 |
| `wikipedia.org` | 31 | 31 |
| `digitaleoverheid.nl` | 28 | 19 |
| `belgium.be` | 17 | 9 |
| `rijksoverheid.nl` | 14 | 10 |
| `forumstandaardisatie.nl` | 12 | 5 |
| `fitko.de` | 11 | 6 |
| `vng.nl` | 10 | 6 |
| `iso.org` | 10 | 8 |
| `un.org` | 9 | 5 |
| `overheid.nl` | 9 | 9 |
| `noraonline.nl` | 9 | 9 |
| `eerstekamer.nl` | 8 | 8 |
| `logius.nl` | 7 | 4 |
| `geonovum.nl` | 7 | 3 |
| `officielebekendmakingen.nl` | 5 | 5 |
| `github.com` | 5 | 4 |
| `w3.org` | 5 | 2 |
| `brandenburg.de` | 4 | 4 |

## Institutional domains

Government, EU, UN and standards-body sources — the ones that carry evidential weight.

```
artificialintelligenceact.eu
belgif.be
belgium.be
bio-overheid.nl
bund.de
cencenelec.eu
destatis.de
digitaleoverheid.nl
europa.eu
fitko.de
forumstandaardisatie.nl
gdi-de.org
geonovum.nl
gesetze-im-internet.de
gov.be
govdata.de
government.nl
iso.org
it-planungsrat.de
itu.int
itzbund.de
just.fgov.be
ksz-bcss.fgov.be
legislation.gov.uk
logius.nl
noraonline.nl
open-government-deutschland.de
overheid.nl
rijksoverheid.nl
statbel.fgov.be
un.org
verwaltungsvorschriften-im-internet.de
w3.org
```

## Remaining domains

Trade press, law firms, encyclopedias and vendor pages. Lower value, but cited somewhere in the Atlas — several entities rest on them entirely and say so in their own bodies.

```
activemind.de
ad4gd.eu
aftermarket-trends.de
agoria.be
anwalt.org
arena2036.de
atlassian.net
automotiveit.eu
autoriteitpersoonsgegevens.nl
b3-it.de
bayern.de
bho-legal.com
bipt.be
bmv.de
bosa.be
bpb.de
brandenburg.de
bundesrechnungshof.de
bundesregierung.de
bundestag.de
buzer.de
communicatierijk.nl
d-velop.de
data-spaces-symposium.eu
dcat-ap.de
de.digital
deloitte.com
digigo.nu
digitale-verwaltung.de
dnb.de
dnb.nl
dnv.de
dsgvo-gesetz.de
dssc.eu
e-recht24.de
earonline.nl
ecp.nl
edustandaard.nl
eerstekamer.nl
epc.ac.uk
errin.eu
eubelius.com
europadecentraal.nl
europeansources.info
ey.com
forschungsinformationssystem.de
fraunhofer.de
gabler.de
gaia-x-hub.de
gaia-x.at
gaia-x.eu
gegevensbeschermingsautoriteit.be
geostandaarden.nl
github.com
github.io
glomas.de
grokipedia.com
haufe.de
health-ri.nl
hessen.de
ictu.nl
informationssicherheitsbeauftragter-dresden.de
ing-ism.de
ipo.nl
ishare.eu
its-mobility.de
jtc1info.org
kadaster.nl
kbvg.nl
legiscope.com
medialaws.eu
mobilithek.info
mobility-data-space.de
mobility-dataspace.eu
nationaalarchief.nl
nationaalgroeifonds.nl
ncsc.nl
nctv.nl
ndw.nu
nen.nl
netzpolitik.org
nictiz.nl
niedersachsen.de
oecd-ilibrary.org
oecd.org
officielebekendmakingen.nl
om.nl
openjustice.be
openkritis.de
opennederland.nl
parlementairemonitor.nl
pdok.nl
personalausweisportal.de
prosoz.de
quality.de
rdw.nl
rehm-verlag.de
rijksbegroting.nl
rijksfinancien.nl
rlp.de
roraonline.nl
rvig.nl
sachsen-anhalt.de
safeonweb.be
secjur.com
security-insider.de
smartcountry.berlin
springerprofessional.de
surf.nl
sva.nl
taylorwessing.com
tcontas.pt
telusio.com
twobirds.com
un-dco.org
unctad.org
unievanwaterschappen.nl
unsceb.org
vbo-feb.be
vng.nl
vngrealisatie.nl
walhalla.de
whitecase.com
wikipedia.org
xoev.de
```

## After the pass

For each entity whose sources have been read: confirm or correct the claims, then set `verification: primary-source`, populate `last_verified`, and add per-source `accessed:` dates. Close the corresponding rows in `discovery/unresolved.md`. Then re-run Batches 6, 11 and 15, which `validation/reports.md` records as **partial by necessity** for exactly this reason.

