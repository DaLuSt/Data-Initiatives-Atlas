#!/usr/bin/env python3
"""Build a throw-away copy of the repository with about 195 country anchors, to check the site at
that size (roadmap #508, docs/scale-check.md).

    python tools/scale_fixture.py /tmp/atlas195     # copy, add fixture countries, build the graph
    python -m http.server 8766 --directory /tmp/atlas195/site

Every added country has an anchor and one to five placeholder organisations, so the Atlas holds
about 1,090 entities. The copy is outside the repository and nothing here touches the real data.
The placeholders say "test authority" and carry no claim about the country.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Countries that have no anchor in the Atlas yet (names as the UN writes them).
NAMES = dict(
    AF="Afghanistan", AG="Antigua and Barbuda", AO="Angola", AU="Australia", BB="Barbados",
    BD="Bangladesh", BF="Burkina Faso", BH="Bahrain", BI="Burundi", BN="Brunei Darussalam",
    BO="Bolivia (Plurinational State of)", BR="Brazil", BS="Bahamas", BT="Bhutan", BZ="Belize",
    CD="Democratic Republic of the Congo", CF="Central African Republic", CG="Congo",
    CI="Côte d'Ivoire", CM="Cameroon", CN="China", CO="Colombia", CR="Costa Rica", CU="Cuba",
    DJ="Djibouti", DM="Dominica", DO="Dominican Republic", DZ="Algeria", EC="Ecuador",
    ER="Eritrea", FJ="Fiji", FM="Micronesia (Federated States of)", GD="Grenada", GH="Ghana",
    GN="Guinea", GQ="Equatorial Guinea", GT="Guatemala", GW="Guinea-Bissau", HN="Honduras",
    ID="Indonesia", IL="Israel", IN="India", IR="Iran (Islamic Republic of)", JO="Jordan",
    JP="Japan", KH="Cambodia", KI="Kiribati", KM="Comoros", KN="Saint Kitts and Nevis",
    KP="Democratic People's Republic of Korea", KW="Kuwait", KZ="Kazakhstan",
    LA="Lao People's Democratic Republic", LB="Lebanon", LC="Saint Lucia", LR="Liberia",
    LS="Lesotho", LY="Libya", MG="Madagascar", MH="Marshall Islands", ML="Mali", MM="Myanmar",
    MN="Mongolia", MR="Mauritania", MV="Maldives", MY="Malaysia", MZ="Mozambique", NA="Namibia",
    NE="Niger", NG="Nigeria", NI="Nicaragua", NR="Nauru", NZ="New Zealand", OM="Oman", PA="Panama",
    PE="Peru", PG="Papua New Guinea", PK="Pakistan", PW="Palau", QA="Qatar", RW="Rwanda",
    SA="Saudi Arabia", SC="Seychelles", SD="Sudan", SL="Sierra Leone", SR="Suriname",
    SV="El Salvador", SY="Syrian Arab Republic", SZ="Eswatini", TD="Chad", TH="Thailand",
    TJ="Tajikistan", TM="Turkmenistan", TO="Tonga", TT="Trinidad and Tobago", TV="Tuvalu",
    TZ="United Republic of Tanzania", US="United States of America",
    VC="Saint Vincent and the Grenadines", VE="Venezuela (Bolivarian Republic of)", VN="Viet Nam",
    VU="Vanuatu", YE="Yemen", ZM="Zambia", ZW="Zimbabwe"
)
# A few larger countries get several organisations, as the real ones will.
HEAVY = {"US": 5, "IN": 4, "JP": 4, "BR": 4, "CN": 3, "AU": 4, "NG": 3, "ID": 3}
DATE = "2026-10-13"


def q(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def anchor(cc: str, name: str, ids: list[str]) -> str:
    related = "".join(f"  - {i}\n" for i in ids)
    return (f"---\nid: {cc}\ntype: country\nname: {q(name)}\n"
            f"description: >\n  Test fixture country anchor for {name}.\n\n"
            f"level: national\ncountry: {cc}\nregion: null\n\nstatus: active\nconfidence: medium\n"
            f"coverage: low\nverification: primary-source\n\nstart_date: null\nend_date: null\n"
            f'last_verified: "{DATE}"\nprevious_version: null\nsuccessor: null\n\n'
            f"domains: []\norganisations: []\nrelated_entities:\n{related}relationships: []\n\n"
            f'sources:\n  - title: "Test fixture"\n    url: "https://example.org/"\n'
            f'    publisher: "Example"\n    accessed: "{DATE}"\n---\n\n# {name}\n\nTest fixture.\n')


def organisation(cc: str, name: str, k: int) -> str:
    oid = f"{cc}-ORG{k}"
    return (f"---\nid: {oid}\ntype: organisation\nname: {q(f'{name} test authority {k}')}\n"
            f"description: >\n  Test fixture organisation for {name}.\n\n"
            f"level: national\ncountry: {cc}\nregion: null\n\nstatus: active\n"
            f"organisation_role: regulatory\nconfidence: medium\ncoverage: low\n"
            f"verification: primary-source\nstart_date: null\nend_date: null\n"
            f'last_verified: "{DATE}"\nprevious_version: null\nsuccessor: null\n\n'
            f"domains:\n  - DOMAIN-GOVERNMENT\norganisations: []\nrelated_entities:\n  - {cc}\n"
            f"relationships:\n  - type: part-of\n    target: {cc}\n    source: fact\n"
            f'    evidence: "Test fixture."\n    confidence: high\n    valid_from: null\n'
            f"    valid_until: null\n\n"
            f'sources:\n  - title: "Test fixture"\n    url: "https://example.org/"\n'
            f'    publisher: "Example"\n    accessed: "{DATE}"\n---\n\n# {name} test authority {k}\n')


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    dst = Path(sys.argv[1]).resolve()
    if dst.exists():
        print(f"{dst} exists; remove it first", file=sys.stderr)
        return 2
    skip = shutil.ignore_patterns(".git", "node_modules", "__pycache__", "graph.json", "details.json")
    shutil.copytree(REPO, dst, ignore=skip)
    for cc, name in NAMES.items():
        if (dst / "countries" / cc.lower()).exists():
            continue
        ids = []
        for k in range(1, HEAVY.get(cc, 1) + 1):
            ids.append(f"{cc}-ORG{k}")
            (dst / "organisations").mkdir(exist_ok=True)
            (dst / "organisations" / f"{cc.lower()}-org{k}.md").write_text(organisation(cc, name, k), encoding="utf-8")
        folder = dst / "countries" / cc.lower()
        folder.mkdir(parents=True)
        (folder / f"{cc.lower()}.md").write_text(anchor(cc, name, ids), encoding="utf-8")
        listing = "\n".join(f"- [[{i}]]" for i in ids)
        (folder / "index.md").write_text(
            f"# {name} — Index\n\nAnchor entity: [[{cc}]]\n\n## Organisations\n\n{listing}\n", encoding="utf-8")
    subprocess.run([sys.executable, "tools/build_graph.py"], cwd=dst, check=True)
    print(f"built {dst}/site; serve it with: python -m http.server 8766 --directory {dst}/site")
    return 0


if __name__ == "__main__":
    sys.exit(main())
