#!/usr/bin/env python3
"""Seed src/content/agencies/*.yaml from the Rio Texas Standing Rules.

Single source of truth for the agency spine. Edit AGENCIES and re-run:

    python3 scripts/seed_agencies.py

Re-running overwrites the generated YAML files (it does not touch agenda,
process, annotations, or questions).
"""
from pathlib import Path
import yaml

OUT = Path(__file__).resolve().parents[1] / "src" / "content" / "agencies"

# General-church bodies, spelled out for readability in `relatesTo`.
COB   = "Council of Bishops"
GCORR = "General Commission on Religion and Race"
GCSRW = "General Commission on the Status and Role of Women"
GBOD  = "General Board of Discipleship"
GBGM  = "General Board of Global Ministries"
GBHEM = "General Board of Higher Education and Ministry"
GBCS  = "General Board of Church and Society"
GCFA  = "General Council on Finance and Administration"
GBPHB = "General Board of Pensions and Health Benefits (Wespath)"
GCAH  = "General Commission on Archives and History"

AGENCIES = [
    {
        "slug": "uniting-table",
        "name": "Uniting Table",
        "type": "uniting-table",
        "votesOn": "both",
        "agendaOrder": 5,
        "summary": (
            "Coordinates the mission and ministry of the conference through the four "
            "Vision Teams. Fulfills all Book of Discipline references to a conference "
            "council on ministries. Includes seven at-large members and a Mission Field "
            "Advocate."
        ),
    },
    {
        "slug": "uniting-peoples",
        "name": "Uniting Peoples Vision Team",
        "type": "vision-team",
        "parent": "uniting-table",
        "relatesTo": [COB, GCORR, GCSRW],
        "summary": "Facilitates unity, witness, communication, justice, and intercultural competency across conference life.",
        "subBodies": [
            {"name": "Commission on Christian Unity and Interreligious Relationships", "bodRefs": ["¶642"]},
            {"name": "Commission on Religion and Race", "bodRefs": ["¶643"]},
            {"name": "Commission on the Status and Role of Women", "bodRefs": ["¶644"],
             "note": "Chair is a woman; a majority of members are women."},
            {"name": "Commission on Communications", "bodRefs": ["¶646"]},
            {"name": "Committee on Disability Concerns", "bodRefs": ["¶653"]},
        ],
    },
    {
        "slug": "vitalizing-congregations",
        "name": "Vitalizing Congregations Vision Team",
        "type": "vision-team",
        "parent": "uniting-table",
        "relatesTo": [GBOD, GBGM],
        "summary": "Develops and deploys resources for the mission of the local church and the restoring of congregational vitality.",
        "subBodies": [
            {"name": "Board of Discipleship", "bodRefs": ["¶629"]},
            {"name": "Committee on Congregational Development and Revitalization", "bodRefs": ["¶632.5e"]},
            {"name": "Committee on Ethnic Local Church Concerns", "bodRefs": ["¶631"]},
            {"name": "Committee on Parish and Community Development", "bodRefs": ["¶632.5"]},
            {"name": "Commission on the Small Membership Church", "bodRefs": ["¶645", "¶632.5i"]},
            {"name": "Committee on New Church Development", "bodRefs": ["¶633.5e-h", "¶630.3"]},
            {"name": "Council on Children's Ministries",
             "note": "Plans, visions, and advocates for children within the conference."},
            {"name": "Council on Older Adult Ministries", "bodRefs": ["¶651.3a-j"]},
            {"name": "Committee on Hispanic/Latino Ministries", "bodRefs": ["¶655"],
             "note": "At least one-third of members are Hispanic/Latino persons."},
            {"name": "Youth Ministries Council", "bodRefs": ["¶649"],
             "note": "3–5 youth per district; no more than one-third adults."},
            {"name": "Young Adult Ministry Council", "bodRefs": ["¶650"]},
        ],
    },
    {
        "slug": "developing-leaders",
        "name": "Developing Leaders Vision Team",
        "type": "vision-team",
        "parent": "uniting-table",
        "relatesTo": [GBHEM, GBOD],
        "summary": "Calls and equips lay and clergy leaders for the mission field, especially younger leaders.",
        "subBodies": [
            {"name": "Board of Higher Education and Campus Ministry", "bodRefs": ["¶633"]},
            {"name": "Board of Ordained Ministry", "bodRefs": ["¶634"],
             "note": "Nominated by the Bishop, elected by the Annual Conference. Reports directly to the conference. Candidate for its own page."},
            {"name": "Lay Leadership Team (Board of Laity)", "bodRefs": ["¶630"]},
        ],
    },
    {
        "slug": "transforming-communities",
        "name": "Transforming Communities Vision Team",
        "type": "vision-team",
        "parent": "uniting-table",
        "relatesTo": [GBCS, GBGM],
        "summary": "Equips and supports congregations around mission, The Advance, ethnic concerns, and justice issues. Includes the Peace with Justice and Caretaker of God's Creation coordinators.",
        "subBodies": [
            {"name": "Board of Church and Society", "bodRefs": ["¶628"],
             "note": "Names the Peace with Justice Coordinator and the Caretaker of God's Creation Coordinator."},
            {"name": "Board of Global Ministries", "bodRefs": ["¶632"]},
            {"name": "Committee on Native American Ministries", "bodRefs": ["¶654"]},
            {"name": "Committee on The Advance", "bodRefs": ["¶823"]},
            {"name": "Committee on Criminal Justice and Mercy Ministries", "bodRefs": ["¶657"]},
        ],
    },
    {
        "slug": "finance-table",
        "name": "Finance Table",
        "alsoKnownAs": "Council on Finance and Administration (CF&A)",
        "type": "administrative-agency",
        "bodRefs": ["¶¶611-627"],
        "membershipSize": 16,
        "relatesTo": [GCFA],
        "votesOn": "action",
        "agendaOrder": 30,
        "alsoFulfills": [{"name": "Commission on Equitable Compensation", "bodRefs": ["¶625"]}],
        "subBodies": [
            {"name": "Personnel Committee", "bodRefs": ["¶613.13"], "membershipSize": 4,
             "note": "Plus a Finance Table representative and a district superintendent."},
        ],
        "summary": "Builds the conference budget, sets apportionments, and manages conference money. Also serves as the Commission on Equitable Compensation.",
    },
    {
        "slug": "board-of-trustees",
        "name": "Board of Trustees",
        "type": "administrative-agency",
        "bodRefs": ["¶2512"],
        "membershipSize": 12,
        "summary": "Holds and manages conference property. Twelve members in four classes of three; also directors of the conference Trustees corporation.",
    },
    {
        "slug": "standing-rules",
        "name": "Committee on Standing Rules",
        "type": "administrative-agency",
        "bodRefs": ["¶604.1"],
        "membershipSize": 6,
        "votesOn": "both",
        "agendaOrder": 10,
        "summary": "Oversees the rules of the Annual Conference and reports during the first business session each year.",
    },
    {
        "slug": "agenda-and-worship",
        "name": "Agenda and Worship Committee",
        "type": "administrative-agency",
        "bodRefs": ["¶605.2"],
        "summary": "Sets the agenda and plans worship. Composed largely of ex-officio members (bishop, superintendents, officers) plus a Worship Team Coordinator.",
    },
    {
        "slug": "committee-on-the-episcopacy",
        "name": "Committee on the Episcopacy",
        "type": "administrative-agency",
        "bodRefs": ["¶636"],
        "membershipSize": 12,
        "summary": "Supports the bishop and the work of the episcopal office.",
    },
    {
        "slug": "episcopal-residence",
        "name": "Episcopal Residence Committee",
        "type": "administrative-agency",
        "bodRefs": ["¶637"],
        "membershipSize": 6,
        "summary": "Oversees the episcopal residence.",
    },
    {
        "slug": "board-of-pensions",
        "name": "Board of Pensions (and Health Benefits)",
        "type": "administrative-agency",
        "bodRefs": ["¶638"],
        "membershipSize": 16,
        "relatesTo": [GBPHB],
        "summary": "Administers clergy pensions and health benefits. Sixteen members on eight-year staggered terms; also directors of the conference Pensions corporation.",
    },
    {
        "slug": "archives-and-history",
        "name": "Commission on Archives and History",
        "type": "administrative-agency",
        "bodRefs": ["¶641"],
        "membershipSize": 8,
        "relatesTo": [GCAH],
        "summary": "Preserves the records and history of the conference and its predecessor conferences.",
    },
    {
        "slug": "nominations",
        "name": "Committee on Nominations",
        "type": "administrative-agency",
        "bodRefs": ["¶610.5"],
        "votesOn": "action",
        "agendaOrder": 20,
        "summary": "Identifies nominees for elected leadership positions and works toward inclusiveness and district balance. Six at-large members plus ex-officio.",
    },
    {
        "slug": "administrative-review",
        "name": "Administrative Review Committee",
        "type": "review-committee",
        "bodRefs": ["¶635"],
        "membershipSize": 3,
        "accountableTo": "Clergy Session of the Annual Conference",
        "summary": "Reviews the fairness of certain clergy processes. Three members and two alternates, nominated by the Bishop and elected by the clergy session.",
    },
]

OPTIONAL_EMPTY = ("relatesTo", "alsoFulfills", "subBodies", "bodRefs")

def prune(d: dict) -> dict:
    out = {}
    for k, v in d.items():
        if v is None:
            continue
        if k in OPTIONAL_EMPTY and not v:
            continue
        out[k] = v
    return out

def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    order = ["name", "alsoKnownAs", "type", "parent", "bodRefs", "membershipSize",
             "relatesTo", "alsoFulfills", "subBodies", "votesOn", "agendaOrder",
             "accountableTo", "summary"]
    for a in AGENCIES:
        slug = a["slug"]
        data = {k: a[k] for k in order if k in a}
        data = prune(data)
        path = OUT / f"{slug}.yaml"
        with path.open("w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=100)
    print(f"Wrote {len(AGENCIES)} agency files to {OUT}")

if __name__ == "__main__":
    main()
