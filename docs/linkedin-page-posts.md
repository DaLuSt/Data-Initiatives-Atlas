# Posts for the LinkedIn Page

Drafts for the **Data Initiatives Atlas** LinkedIn Page. Sections 1 and 2 were written 2026-10-09,
with the figures of that day (747 entities, 9,435 connections, 58 countries). Section 3 is a bank of
45 **idea posts** written 2026-11-13 with the figures of that day (1,286 entities, 13,749 connections,
169 countries; the live counts are on the site). They are plain text, because LinkedIn does not
render Markdown, and each is under LinkedIn's 3,000-character limit. Read them, change what you
like, and post them from the Page or the profile.

## How they get onto the Page

Posts to the **personal profile** are automated (the release workflow, `docs/credentials.md`
section 2). Posts to the **Page** can be automated too, with a second, separate pipeline
(`.github/workflows/linkedin-page-post.yml`, "Post release on LinkedIn Page", built 2026-11-09,
`docs/credentials.md` section 3). It posts the *same text* as the profile, from the same draft issue,
after its own approval. It is **switched off** until the owner has done what only the owner can:
a Page needs the *Community Management API* product (permission `w_organization_social`), LinkedIn
reviews that request (an approved use case, a verified business email, a verified organisation and
website domain, and an app verified by the Page, per LinkedIn's own pages read 2026-10-09), and it
must sit on its own app because LinkedIn allows that product only on an app with no other product.
An unfunded open-data project may not pass the review. Until it does, or if it does not, post to the
Page by hand: paste the draft from the issue "Post data release X on LinkedIn" into the Page, which
is what the issue reminds you of. Nothing is lost either way.

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

## 3. Idea posts: findings from a European data architect's seat

A mix of findings, numbers, questions, confessions and observations, written in the first person of a
European data architect who works on policy and cares about metadata. They share a shape: a claim that
stops the scroll, two or three verified facts from the Atlas, one lesson for people who build data
registers, and a closing question. They are in English, like sections 1 and 2.

**Where the facts come from.** Every figure and date is taken from an Atlas entity (the IDs are listed
under each post) or from the Atlas's own statistics, and each entity cites its primary source. Opinions
are marked as such in the text ("in my reading", "I would plan against"). Where a fact rests on a
secondary source, or is likely to change, the line "Check before posting" under the post says so.

**Kinds:** Fact (a verified event), Number (a statistic of the graph), Metadata (a modelling lesson),
Observation (a pattern across entities), Policy (an instrument seen from a European angle), Architecture
(how data systems are built), Confession (a limit of the Atlas), Process (how it is made), Question.
**A suggested rhythm:** one post a week, alternating a Fact with a Metadata or Confession post, and
leave the Explore link out of every third post (LinkedIn tends to reach fewer people with links).

### Post 1. One regulation, three dates

*Kind: Observation. Atlas entities: EU-EURO-7, CH-BGEID, EU-KIDS Act (candidate C11).*

```text
One regulation, three dates. Which one goes in your metadata field?

I spend my days making data about data behave. Then I read European legislation and my "date" column gives up.

Three examples from the Data Initiatives Atlas, an open map of data governance:

• Euro 7 (Regulation 2024/1257): in force since 28 May 2024, but its type-approval requirements only apply from 29 November 2026. A law can be in force and not yet bite.
• The Swiss e-ID Act: adopted by parliament on 20 December 2024, approved by voters on 28 September 2025 (50.39%), and still not in force. The Federal Council sets the date, and on 30 June 2026 it delayed the launch; the trust infrastructure is now expected in the first half of 2027.
• The EU KIDS Act, proposed on 17 September 2026: enters into force on the twentieth day after publication, applies six months later, and within that one text some articles apply from day one and others twelve months on.

So "start_date" cannot mean one thing. Adopted, in force, applicable, and applied in practice are four different facts, and a compliance team, a regulator and a data catalogue each need a different one.

In the Atlas, a status of "adopted" means formally adopted but not yet in force, and every date is tied to the evidence for it. Boring? Yes. It is also the difference between a map and a rumour.

If you model legislation in a catalogue or a knowledge graph: how many date fields do you keep?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#datagovernance #metadata #EUregulation #knowledgegraph #opendata
```

*Check before posting: Euro 7 applies from 29 November 2026; check the Swiss e-ID and the KIDS Act have not moved.*

### Post 2. An adequacy decision is a record with a review clock

*Kind: Metadata. Atlas entities: EU-AD-ADEQUACY, EU-AR-, EU-BR-, EU-CA-, EU-JP-, EU-KR-, EU-NZ-, EU-US-, EU-UY-ADEQUACY, EU-ADEQUACY-REVIEW-2024.*

```text
An adequacy decision is not a permission slip. It is a record with a review clock.

When people say "the EU has adequacy with country X", they usually mean one fact. In a graph it is at least four:

1. a Commission decision (the instrument),
2. a national law it assesses (the thing it points at),
3. a jurisdiction it applies in,
4. a date by which someone has to look again.

The Data Initiatives Atlas now models nine of them: Andorra, Argentina, Brazil, Canada, Japan, Korea, New Zealand, the US and Uruguay.

What the sources show once you read them:
• Five were adopted under the old Directive 95/46/EC and carry on under the GDPR until amended or repealed. Their first review report, COM(2024) 7, arrived on 15 January 2024 and covered eleven countries and territories.
• The ones adopted under the GDPR itself have review clocks written into the text. Japan: within two years, then at least every four. Korea: three years, then every four.
• Brazil is the newest: the decision of 26 January 2026 points at Brazil's LGPD.

The metadata lesson: the interesting field is not "adequate: yes". It is "next review due". It is easy to overlook, and it is exactly the thing that tells you whether a data flow still stands on solid ground.

Do you track review dates for your transfer mechanisms, or only the day they were signed?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#GDPR #dataprotection #datagovernance #metadata #adequacy
```

### Post 3. A law without an owner

*Kind: Observation. Atlas entities: BF-LOI-037-2026, BF-LOI-ORG-038-2026, BF-ARCOD, BF-CIL, GN-LOI-2015-037, CG-LAW-29-2019, SV-ACE, TD-ANSICE, AG-INFORMATION-COMMISSIONER.*

```text
A law without an owner is just a text file.

Reading data protection and cyber laws country by country, the same question keeps coming up: who actually enforces this?

In the Data Initiatives Atlas, a law is linked to the body that governs it. For quite a few laws that link cannot be drawn, because the authority is not named, or is not yet set up. A few examples:

• Burkina Faso's two 2026 laws. Law 037-2026 repeals the 2021 data protection law and gives controllers six months to comply. A second, organic law creates a new regulator, ARCOD, which appears to take over from the CIL. But article 72 says the CIL stays in charge until ARCOD is effectively set up. The successor exists on paper, the predecessor still does the work.
• Guinea's 2015 cyber and data law and Congo's law 29-2019: a law, and no authority recorded in it.
• In El Salvador, Chad and Antigua and Barbuda the Atlas has a law and an authority it could not confirm, so the entity is recorded as unknown rather than guessed.

As a data architect I find this oddly familiar. It is the entity with no steward. The dataset with no owner. The schema nobody is accountable for.

So we model "successor" and "unknown" explicitly. A regulator in transition is a different fact from a regulator that is simply there, and "we could not find out" is an honest value, not a blank.

What does your catalogue say when ownership is unknown: a blank, or a status?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#dataprotection #governance #metadata #datastewardship #Africa
```

### Post 4. Africa's own data protection treaty

*Kind: Policy. Atlas entities: INTL-AU-MALABO-CONVENTION.*

```text
Europe's GDPR gets the headlines. Africa has its own data protection treaty, and it is in force.

The African Union's Malabo Convention on Cyber Security and Personal Data Protection was adopted on 27 June 2014. It entered into force on 8 June 2023, nine years later, once a 15th State had deposited its instrument. By the AU's status list of 2 February 2026, 21 States have signed and 20 have deposited.

The Data Initiatives Atlas now reads the treaty text (a scan, so page by page). Three things stand out to a European eye:

• One treaty, three subjects: electronic transactions, personal data protection and cybersecurity. Europe spreads these across the GDPR, the ePrivacy rules and NIS2.
• Each State Party must set up an independent national data protection authority (article 11).
• Article 10 keeps prior formalities: a declaration, or for sensitive processing like biometrics, an authorisation, before the national authority. Europe moved away from general notification when the GDPR replaced Directive 95/46; Malabo still has it.

The Atlas links the Convention to the 18 depositing States it has anchored, and separately marks the ones that only signed. "Signed", "ratified", "in force" and "applies in" are four different statements, and they should not share one column.

If your data flows reach African markets, your map of "the rules" may have a gap on it.

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#dataprotection #Africa #GDPR #datagovernance #crossborder
```

### Post 5. The missing arrow: Ireland and NIS2

*Kind: Fact. Atlas entities: IE-NCS-BILL, EU-NIS2, EU-CJEU.*

```text
A node stuck at "proposed" tells you more than ten that say "in force".

NIS2 had to be transposed by 17 October 2024. In the Data Initiatives Atlas, each national act that transposes it is linked to the Directive. Ireland's link ends at a bill, not a law: the National Cyber Security Bill, status "proposed".

The timeline, from the sources the Atlas cites:
• 17 October 2024: transposition deadline passes.
• 7 May 2025: the Commission sends Ireland a reasoned opinion.
• 8 July 2026: the Commission refers Ireland, Spain, France and the Netherlands to the Court of Justice of the EU, with an initial penalty of about 2.8 million euro reported for Ireland, plus daily fines.
• Autumn 2026: the Irish Government's own legislation programme lists the National Cyber Security Bill for priority publication, with the status "Work is ongoing."

What this shows as a data person: the gap between "the EU adopted it" and "it is law where you operate" is where a lot of compliance risk sits. A graph makes that gap visible.

And a modelling confession: the Atlas has a relationship type for "referred to court over", so the referral is on the graph. What it cannot hold yet is the procedure itself: the letter of formal notice, the reasoned opinion, the referral and the judgment as separate, dated steps. That is an open item in our own backlog, and I would rather show you the gap than hide it.

How do you track transposition status for the rules you comply with?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#NIS2 #cybersecurity #EUlaw #datagovernance #knowledgegraph
```

*Check before posting: The 2.8 million euro comes from press reports cited in the Atlas, not from a Commission page.*

### Post 6. 98 percent fact, 2 percent interpretation

*Kind: Number. Atlas entities: site statistics (provenance).*

```text
Of the 2,518 typed relationships in the Data Initiatives Atlas, 2,476 are sourced facts. 42 are our own interpretation.

That is 98.3 to 1.7, and the 1.7 is labelled.

Every relationship in the graph carries three things: a type (applies-in, governed-by, supersedes, and so on), a provenance (fact or interpretation) and the evidence for it, in words. If the Atlas reads a statute and it says "this Act implements that Directive", that is a fact with a quotation behind it. If we connect two things because it seems obvious to us, it is marked as an interpretation, so you can filter it out.

As a data architect, this is the part of lineage I wish every catalogue had. Not just "A is related to B", but "who says so, and how sure are we".

Most metadata models have a field for the source system. Very few have a field for "this link is a judgement call".

What share of the relationships in your catalogue are observed, and what share are somebody's opinion? Could you tell?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#metadata #datalineage #datagovernance #provenance #knowledgegraph
```

### Post 7. A link is not a relationship

*Kind: Metadata. Atlas entities: site statistics (edges).*

```text
The Data Initiatives Atlas has 13,749 connections. Only 2,518 of them are relationships.

The rest:
• 5,792 wikilinks: one entity mentions another in its text.
• 5,439 associations: links that come from an entity's own fields, such as related entities, domains and organisations.
• 2,518 typed relationships, each with a type, a provenance and the evidence behind it.

I keep three classes apart on purpose. "These two things are mentioned together" is a very different statement from "this regulation applies in this country", and mixing them is how knowledge graphs turn into hairballs that look impressive and answer nothing.

If you have ever been handed a graph with one kind of edge, you know the problem. Everything is connected, so nothing is explained.

My rule of thumb: the number of edge types you can explain to a lawyer in one minute is the number you should have.

How many kinds of edge does your graph have, and could you defend each one?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#knowledgegraph #metadata #datamodelling #linkeddata
```

### Post 8. The junk drawer: related-to

*Kind: Confession. Atlas entities: metadata/relationship-types.md, site statistics.*

```text
A confession from the data model of the Data Initiatives Atlas.

We have 29 relationship types. The most common is "applies-in" (721), then "part-of" (455). The third most common is "related-to" (369), about 15 percent of all typed relationships.

"related-to" is the junk drawer. It is what you reach for when you know two things belong together and cannot yet say how. Every data model has one: "other", "misc", "see also", "linked".

The honest approach we try to follow: use it when nothing more precise is sourced, and treat each one as a to-do. When a source later says "this decision implements that law", the vague edge becomes a precise one. When it never does, at least it is labelled as vague.

The danger is not having a junk drawer. The danger is not knowing how full it is.

What percentage of your relationships are "other"? And does anyone own shrinking it?

#datamodelling #metadata #knowledgegraph #ontology
```

### Post 9. A map of data governance is mostly a map of government

*Kind: Confession. Atlas entities: site facets (domains).*

```text
A coverage confession.

Of the 1,286 entities in the Data Initiatives Atlas, 898 are tagged with the domain "government". Cybersecurity has 96, health 28, energy 10, finance 10, space 6, chemicals 6, and built environment just 3.

That is not because data governance in energy or health does not matter. It is because we started where the sources are open and the instruments are visible: public-sector data, interoperability, open data and NIS2. The sector annexes of the NIS2 national laws then pulled in some food, chemicals, postal and space.

A map shows what its makers could reach. When you look at any data catalogue or knowledge graph, ask the same question: where is it dense, and is that because the world is dense there, or because that is where the cartographer happened to walk?

If you work in energy, finance, health or the built environment and you know where the data rules live, that is exactly where we want to hear from you.

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#datagovernance #opendata #coverage #crowdsourcing
```

### Post 10. Our database is a Git repository

*Kind: Process. Atlas entities: README, CONTRIBUTING.*

```text
The Data Initiatives Atlas has no database.

Every entity is a Markdown file with YAML frontmatter. Every relationship, with its provenance and its evidence, sits in that file. The whole thing lives in a Git repository, is released under CC0, and the website is generated from the files.

What you get for free:
• History. Every change to what we say about a law has an author, a date and a reason.
• Review. A correction is a pull request, and a reviewer sees exactly which sentence changed.
• Diffs. When a bill becomes an act, the change is one line in a status field and everyone can see it.
• No lock-in. Take the repository and walk away.

It also suits the subject. Legislation is itself versioned text: acts are amended, repealed and consolidated, and the Atlas holds twenty "amends" relationships between them. A repository is a natural home for a thing that is mostly diffs.

The price: no fancy queries until you build them, and humans have to be disciplined about frontmatter. We have validators for that.

Would you keep your policy register in Git? What would stop you?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#opendata #git #metadata #datagovernance #CC0
```

### Post 11. Three Dutch laws, three end dates

*Kind: Observation. Atlas entities: NL-WBP, NL-WOB, NL-WBNI, NL-UAVG, NL-CBW.*

```text
Three Dutch laws that no longer exist, and the day each one ended:

• Wet bescherming persoonsgegevens: in force from 1 September 2001 until 25 May 2018, when the GDPR took direct effect and the Uitvoeringswet AVG took over.
• Wet openbaarheid van bestuur (Wob): replaced on 1 May 2022 by the Wet open overheid.
• Wet beveiliging netwerk- en informatiesystemen: replaced on 15 August 2026 by the Cyberbeveiligingswet, which implements NIS2 and covers roughly 8,000 organisations.

In the Data Initiatives Atlas, none of these were deleted. They are kept, with a status of "superseded" and an end date. That sounds like a small thing, but it makes a big difference to anyone who has to ask "what applied to this dataset in 2019?"

Metadata people know this one: a valid-from date without a valid-to date is half a record.

Does your register keep the laws that used to apply, or only the ones that apply today?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#datagovernance #metadata #GDPR #NIS2 #Netherlands
```

### Post 12. When the regulator is replaced by a new legal person

*Kind: Fact. Atlas entities: GB-ICO, GB-INFORMATION-COMMISSION.*

```text
On 30 September 2026 the UK's data protection regulator stopped being one person.

The office of Information Commissioner was abolished by section 118 of the Data (Use and Access) Act 2025, and its functions passed to a new Information Commission under section 119. Both were brought into force on that date by SI 2026/1015. Where the Commissioner was a single office-holder, the Commission is a body corporate whose members share collective responsibility. On the day, it had an interim chief executive, seven new non-executive members, and a recruitment for the chair still going.

For a data architect that is a master-data question in disguise. When an authority is replaced, do you:
a) rename the old record,
b) end it and create a new one, linked to the first, or
c) keep both and hope nobody notices?

The Atlas does (b). The ICO is kept with an end date of 30 September 2026, marked "superseded", and the Information Commission starts that day. History stays queryable, and the arrow from one to the other says who took over from whom.

Which one does your organisation chart use?

#GDPR #UKGDPR #masterdata #datagovernance #metadata
```

### Post 13. Same Directive, four very different populations

*Kind: Number. Atlas entities: DE-NIS2UMSUCG, PL-KSC, NL-CBW, FR-NIS2-LOI.*

```text
NIS2 is one Directive. The number of organisations it reaches depends on who you ask.

What the national acts say, as read by the Data Initiatives Atlas:
• Germany: from roughly 4,500 supervised entities to roughly 29,500, across 18 sectors. In force 6 December 2025, no transition period.
• Poland: from roughly 400 to roughly 42,000. In force 3 April 2026, with self-identification replacing administrative designation.
• The Netherlands: roughly 8,000 organisations. In force 15 August 2026.
• France: roughly 15,000 entities, against about 500 under the first NIS regime. Still a bill when we last checked, in debate in the Assemblée nationale from 9 November 2026.

Nobody is wrong. Member States choose how to classify entities and whether to designate them or ask them to register themselves. The Directive is the same, and the effective scope differs by a factor of ten.

For anyone building a compliance register: "NIS2 applies" is not an attribute. "NIS2 applies in Poland, to you, because you self-identified in this sector" is.

How do you record scope when the same rule is applied differently per country?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#NIS2 #cybersecurity #compliance #EUlaw #datagovernance
```

*Check before posting: France's NIS2 bill: re-check its status before posting.*

### Post 14. Referred on 8 July, in force on 15 August

*Kind: Fact. Atlas entities: NL-CBW, NL-WBNI, EU-CJEU.*

```text
On 8 July 2026 the European Commission referred four Member States, including the Netherlands, to the Court of Justice for not fully transposing NIS2.

On 15 August 2026, five weeks later, the Dutch Cyberbeveiligingswet came into force.

Poland shows the other timeline: it received a reasoned opinion on 7 May 2025, one of 19 Member States, and completed transposition on 3 April 2026, before the referral stage.

An infringement procedure has a rhythm: formal notice, reasoned opinion, referral, judgment, possibly financial penalties. A national law can arrive at any point along that line, and when it does, the matter is not necessarily over. The Court may still need to decide whether the failure existed.

In the Data Initiatives Atlas a national act can carry a "referred to court over" edge towards the directive. That tells you a referral happened. It does not yet tell you at which stage the procedure stood when the act arrived, because we do not have the procedure as a thing. That is on our list.

How do you represent a process with stages when your data model only has states?

#NIS2 #EUlaw #infringement #datamodelling #cybersecurity
```

*Check before posting: Dutch law in force 15 August 2026 and the 8 July 2026 referral are both in the Atlas; the referral date is from secondary sources.*

### Post 15. Twenty-nine months late

*Kind: Fact. Atlas entities: BE-HERGEBRUIK-WET-2023, EU-OPEN-DATA-DIRECTIVE.*

```text
The Open Data Directive (2019/1024) had to be transposed by 17 July 2021.

Belgium's federal act amending the 2016 re-use law is dated 25 December 2023, twenty-nine months after the deadline. It reached the Belgian Official Gazette on 23 January 2024, about thirty months after, and eleven months after the Commission had referred Belgium to the Court of Justice for failing to transpose.

I like that this can be computed. Deadline minus date of the national act gives you a number of months. It is a derived metadata field, and it tells you something that no single date does.

A thought experiment for your own register: if you stored the deadline for every directive and the date of each national instrument, you could rank Member States by delay, flag the late ones as risk for cross-border contracts, and see whether the delay predicts anything else.

Most registers keep the deadline in a policy document and the date in a legal database. The interesting number lives between them.

What derived fields would you add to a register of laws?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#opendata #EUlaw #metadata #Belgium #datagovernance
```

### Post 16. A new directive does not update the old pointers

*Kind: Observation. Atlas entities: EU-PSI-DIRECTIVE, EU-OPEN-DATA-DIRECTIVE, DE-IWG.*

```text
The EU's first re-use of public sector information directive dates from 2003. In 2019 it was recast as the Open Data Directive, which repealed it.

You would think that is the end of it. It is not. The Data Initiatives Atlas notes that several national instruments still in force were written to transpose the old directive rather than its successor. The statute book keeps pointing at something that no longer exists.

This is a classic reference-data problem. A foreign key to a record that has been deprecated. The record is still there, the link is not broken, but it is stale.

In the Atlas this shows up as a "superseded" status on the old directive and edges from national laws that still lead to it. We do not hide them: we mark them. That helps with a real question, which is "which national laws have been brought in line with the new regime, and which still speak the language of the old one?"

How do you find the stale references in your catalogue when the thing they point to has been replaced?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#opendata #metadata #referencedata #EUlaw
```

### Post 17. Folding three data laws into one

*Kind: Fact. Atlas entities: EU-DIGITAL-OMNIBUS, EU-DGA, EU-OPEN-DATA-DIRECTIVE, EU-FREE-FLOW-NON-PERSONAL-DATA, EU-DATA-ACT.*

```text
The European Commission proposed the Digital Omnibus on 19 November 2025. If adopted as proposed, it would repeal three data laws and move their content into the Data Act:

• the Data Governance Act,
• the Open Data Directive,
• the Free Flow of Non-Personal Data Regulation.

It would also amend the GDPR, the ePrivacy Directive and the Data Act itself. Reportedly the Council's ambassadors approved a negotiating mandate on the data part on 21 October 2026.

For anyone modelling this, it raises a question I find fascinating: how do you represent a law that has not been adopted but says it will replace three others? The Data Initiatives Atlas has a relationship type for exactly this, "proposes to supersede", used three times. It does not change the status of the existing laws. They remain active. It only says that a proposal intends to replace them.

Trying to be clever and flipping the old laws to "superseded" early would be a mistake. The map should show what is law today and what is intended for tomorrow, on different layers.

How does your register show a repeal that is announced but not yet decided?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#DigitalOmnibus #DataAct #EUlaw #datagovernance #opendata
```

*Check before posting: Council mandate date comes from a law-firm article, not the Council. Re-check the Omnibus status before posting.*

### Post 18. The date you wrote in your compliance calendar moved 16 months

*Kind: Fact. Atlas entities: EU-DIGITAL-OMNIBUS-AI, EU-AI-ACT.*

```text
The AI Act's general application date for high-risk systems under Annex III was 2 August 2026.

It is now 2 December 2027.

That was done by the "Digital Omnibus on AI", adopted on 8 July 2026, published in the Official Journal on 24 July and in force from 27 July 2026, as Regulation (EU) 2026/1744. It amends the AI Act, the EASA Regulation and the Machinery Regulation. It was published on the same day as its sibling, the broader Digital Omnibus proposal, but negotiated and adopted independently.

Two lessons for people who keep compliance calendars:
1. A date in a regulation is not a constant. It is a property of the current consolidated version, and it can change under you.
2. When you copy a date out of a law into a spreadsheet, you also need to copy where you got it, and the date you checked it.

The Atlas stores the amending relationship between the two regulations and ties each date to evidence. That is the closest thing we have to a diff for a calendar.

Who owns the dates in your compliance calendar, and how do you find out when they move?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#AIAct #compliance #EUregulation #metadata #datagovernance
```

### Post 19. The wallet deadline: the end of 2026

*Kind: Fact. Atlas entities: EU-EIDAS2, EU-EUDI-WALLET, CH-E-ID.*

```text
Regulation (EU) 2024/1183, "eIDAS 2", was adopted on 11 April 2024 and entered into force on 20 May 2024. Its central reform is an EU-wide framework for European Digital Identity Wallets, which Member States must provide by the end of 2026.

In the Data Initiatives Atlas the law is "active" and the wallet itself is "planned". Two different statuses for two different things, and I think that distinction matters: a regulation can be fully in force while the thing it requires still does not exist.

Switzerland, outside the EU, shows the same gap from another side. Its e-ID Act was adopted by parliament on 20 December 2024 and approved by voters on 28 September 2025. Its wallet, swiyu, was in public beta and, on 30 June 2026, the launch was postponed. The trust infrastructure is now expected in the first half of 2027.

Law, deadline, thing. Three separate things, three separate dates, three different risks.

If your product depends on the wallet, which one are you tracking?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#eIDAS #digitalidentity #EUDI #interoperability #datagovernance
```

*Check before posting: Deadline is end of 2026: check progress in the Member States before posting.*

### Post 20. Same word, different thing: the data space

*Kind: Observation. Atlas entities: EU-EHDS, DE-CATENA-X, EU-DSSC-BLUEPRINT, NL-ISHARE.*

```text
"Data space" now means at least two things.

The European Health Data Space is a regulation: (EU) 2025/327, in force from 26 March 2025, applying in phases from 2027, with Member States creating health data access bodies.

Catena-X, the automotive data ecosystem, is an association: the Catena-X Automotive Network e.V. was founded in May 2021, builds on Gaia-X and the International Data Spaces reference architecture, and connects manufacturers, suppliers and service providers.

Same label. One is statute, with a legal basis and a supervisor. The other is a club, with a rulebook and members.

The Data Initiatives Atlas holds 26 data spaces, from Germany's Manufacturing-X family to the EU's agricultural, legal, tourism and skills data spaces. Whether each one is a statute, a contract or a community is exactly the kind of fact worth recording, because "what is it, legally?" decides who can enforce what.

The European blueprint from the Data Spaces Support Centre goes at this from the other direction: governance, legal, business and technical building blocks, and a "rulebook" model that lets a club behave like an institution.

When someone says "data space" to you, do you ask whether it is a law, a contract or a community?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#dataspaces #EHDS #Gaia-X #datagovernance #interoperability
```

*Check before posting: 'We tag each with its legal nature' is a claim about the Atlas: confirm the type/status fields you want to cite.*

### Post 21. One vocabulary, five dialects

*Kind: Metadata. Atlas entities: INTL-DCAT, EU-DCAT-AP, NL-DCAT-AP-NL, DE-DCAT-AP-DE, PL-DCAT-AP-PL, BE-DCAT-AP-BE, ES-NTI-RISP.*

```text
The W3C's DCAT is the world's common language for describing datasets in a catalogue. Europe added DCAT-AP, an application profile for the public sector. Then every country added its own:

• The Netherlands: DCAT-AP-NL, managed by Geonovum, version 3.0 adopted.
• Germany: DCAT-AP.de, set by an IT-Planungsrat resolution in June 2018. Since early 2019 the German portals accept metadata only in this standard. Its handbook has 41 MUST, SHOULD and CAN conventions.
• Poland: DCAT-AP-PL, a subprofile of DCAT-AP, published on dane.gov.pl.
• Belgium: a federal DCAT-AP-BE, with mandatory, recommended and optional fields, and a mapping between INSPIRE and DCAT-AP elements.
• Spain: DCAT-AP-ES, aligned with DCAT-AP 2.1.1 and the high-value datasets profile 2.2.0, still in administrative processing.

Same ancestor, five dialects. Each is a good-faith adaptation to local law and local portals, and together they define the actual interoperability of European open data.

The Atlas links each profile to its parent, so you can see the family tree.

In your organisation, who owns the application profile, and what happens when the parent profile releases a new version?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#DCAT #metadata #opendata #interoperability #FAIR
```

### Post 22. Europe wrote metadata into law in 2007

*Kind: Metadata. Atlas entities: EU-INSPIRE, BE-DCAT-AP-BE.*

```text
When we talk about metadata policy we tend to start with open data and FAIR. Europe actually wrote metadata into law much earlier.

The INSPIRE Directive of 14 March 2007 set up an Infrastructure for Spatial Information in the European Community. It covers 34 spatial data themes and is given effect through implementing rules on metadata, data specifications, network services, data and service sharing, and monitoring and reporting.

Metadata comes first in that list for a reason: if you cannot find a dataset, nothing else about it matters.

In the Data Initiatives Atlas, INSPIRE is among the most connected nodes, with 90 connections. National laws transpose it, portals implement it, and the Belgian federal DCAT-AP profile even contains a mapping between INSPIRE and DCAT-AP elements, so that geospatial and open data catalogues can talk to each other.

A reminder for anyone who thinks metadata governance is new: it has been a legal obligation for geospatial data in the EU for almost twenty years.

What did INSPIRE get right that today's data strategies could learn from?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#INSPIRE #metadata #geospatial #opendata #EUlaw
```

### Post 23. A semantic model that survives four syntaxes

*Kind: Metadata. Atlas entities: EU-EN-16931, DE-XRECHNUNG, FR-CIUS-FR, IT-FATTURAPA, INTL-PEPPOL-BIS-BILLING.*

```text
EN 16931 is the European standard for electronic invoicing, published on 28 June 2017 under Directive 2014/55/EU. The detail I like: it is a semantic data model, not a file format. It says what an invoice can contain. Two syntaxes, UBL and CII, say how to write it down.

Then countries add their own "core invoice usage specification" on top:
• Germany: XRechnung, with a German-specific mandatory routing identifier, the Leitweg-ID. Phased in between November 2018 and November 2020.
• France: CIUS-FR, required for invoices to public bodies through Chorus Pro.
• Peppol: its billing specification is itself a CIUS and is used across the network.
• Italy: FatturaPA predates EN 16931 and is not natively compliant. It is recognised as aligned through a national CIUS and the exchange system translates in both directions.

A clean separation of meaning and syntax, with local variants as constrained subsets. If you have ever struggled with a canonical data model, this is a working example at continental scale.

Where do you draw the line between the semantic model and the file format?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#einvoicing #EN16931 #semantics #interoperability #metadata
```

### Post 24. A code list in the Official Journal

*Kind: Metadata. Atlas entities: UN-LOCODE, UN-EDIFACT, EU-EMSWE.*

```text
Regulation (EU) 2019/1239 on the European Maritime Single Window environment provides for a common location database. It holds a reference list of location codes including UN/LOCODE, alongside SafeSeaNet-specific codes and IMO port facility codes.

So a code list maintained under the United Nations Economic Commission for Europe, through UN/CEFACT, is named in Union law.

Reference data governance in one paragraph:
• Someone outside the legislator maintains the list.
• The law points at it, and therefore at every future version.
• The people who use it have a legal reason to care when it changes.

The Data Initiatives Atlas records this in a modest way: UN/LOCODE is a standard, maintained under UN/CEFACT, and the EU regulation sits next to it as the instrument that gives it legal weight. UN/EDIFACT, the syntax standard from the same family, is there too.

Every large organisation has a list like this, usually in an Excel sheet someone maintains in a regional office.

Who governs the reference data your regulatory reporting depends on?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#referencedata #metadata #UNCEFACT #masterdata #EUlaw
```

### Post 25. Ten base registries and one feedback loop

*Kind: Metadata. Atlas entities: NL-BASISREGISTRATIES, NL-BAG, NL-BRK, NL-COMMON-GROUND.*

```text
The Netherlands has ten designated base registries: the BRP (persons), the Handelsregister (businesses), the BAG (addresses and buildings), the BRT (topography), the BRK (cadastre), the BRV (vehicles), the BRI (income), the WOZ (property values), the BGT (large-scale topography) and the BRO (subsurface).

The idea: core data of each kind is collected and managed in one authoritative place and reused across government, rather than re-collected.

What I admire as a data architect is the machinery around them. Each registry has an initiating organisation, a supervisor, a provider and one or more holders. One organisation can be provider, holder and user at the same time. And there is a system service called Digimelding for reporting suspected errors in the data.

That last one is the real metadata policy. An authoritative source without an error-reporting route is just a database with confidence issues. A registry with a feedback channel gets better when more people use it.

The Atlas keeps all ten and the framework itself, which, with 111 connections, is one of the most connected nodes in the graph.

Do your authoritative sources have an error-reporting channel, and who is obliged to answer it?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#basisregistraties #masterdata #datagovernance #egovernment #Netherlands
```

### Post 26. Do not copy, query

*Kind: Architecture. Atlas entities: EE-X-TEE, NL-COMMON-GROUND, DE-DEUTSCHLAND-STACK.*

```text
Three countries, one principle.

• Estonia's X-tee, the national data exchange layer (called X-Road in English until 2018): data is not held in a central repository. It flows directly from source to recipient.
• The Netherlands' Common Ground, the municipal information programme coordinated by the VNG: data are queried from source systems instead of repeatedly copied into applications.
• Germany's Deutschland-Stack: a sovereign platform of shared "Basiskomponenten" for federal, state and municipal government, targeted at 2028.

The first two say, in so many words, "leave the data where it is". The third is more about shared building blocks, but sits in the same family of thinking: reduce copies, increase interfaces.

From the metadata side, the shift matters. A copy-based architecture needs lineage to trace where each copy came from. A query-based one needs something else: a good description of what each source offers, and trust in who is allowed to ask.

Data catalogues were built for the first world. The second needs service catalogues, access rules and good versioning.

Are you still managing copies, or already managing contracts between sources?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#dataarchitecture #Xroad #CommonGround #egovernment #interoperability
```

### Post 27. The product of a data space is its rulebook

*Kind: Architecture. Atlas entities: EU-DSSC-BLUEPRINT, NL-ISHARE, DE-CATENA-X.*

```text
Look at what iSHARE and the European data spaces blueprint actually deliver.

iSHARE, introduced in 2018 by Topsector Logistiek, is an agreement system and trust framework: uniform agreements on identification, authentication and authorisation, so that parties can share data with counterparties they do not know, while keeping control of the data and who gets access.

The European blueprint from the Data Spaces Support Centre, funded under the Digital Europe Programme, offers business, governance, legal and technical building blocks, and introduces the idea of a data space governance framework and rulebook model.

The technical parts, connectors and catalogues, matter. But what makes them work is the rulebook: who may join, who is liable, what happens on a breach, how disputes are settled.

I read that as a hint for anyone building a data sharing initiative. Spend a third of your budget on the agreement and the governance, not just the software. The software is replaceable. The trust is not.

What is in the rulebook of your data sharing initiative, and who signed it?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#dataspaces #trust #iSHARE #governance #interoperability
```

### Post 28. Binding, model, framework: three layers in one region

*Kind: Policy. Atlas entities: INTL-ECOWAS-PDP-ACT-2010, INTL-SADC-DP-MODEL-LAW-2012, INTL-CEMAC-USERS-DIRECTIVE-2008, INTL-AU-DPF, INTL-AU-MALABO-CONVENTION.*

```text
Africa's data protection architecture has layers that Europeans might recognise from home.

• Continental, binding: the Malabo Convention, in force since 8 June 2023.
• Continental, non-binding: the AU Data Policy Framework, endorsed in February 2022, a guide and not a treaty.
• Regional, binding: the ECOWAS Supplementary Act of 16 February 2010 at Abuja, which asks each Member State for a legal framework and its own independent data protection authority. A revised text was validated by experts in Accra on 18 and 19 November 2024 and awaits ministers' approval.
• Regional, model: the SADC model law of 2012, prepared with the ITU and the EU, which Member States may use but which does not bind them.
• Regional, sectoral: the CEMAC Council of Ministers' directive of around 2008 on the rights of users of electronic communications.

The Data Initiatives Atlas keeps these apart with different entity types: agreements, legislation and soft law. "Does this bind a State?" is a first-class field, not a footnote.

If you map regulations in your organisation, do you separate what binds from what only advises?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#dataprotection #Africa #governance #metadata #policy
```

### Post 29. Thirty-four of thirty-eight

*Kind: Fact. Atlas entities: INTL-CONVENTION-108-PLUS, INTL-CONVENTION-108.*

```text
Convention 108+ opened for signature on 10 October 2018. It is the Council of Europe's modernised data protection treaty: stronger proportionality and data minimisation, controller duties on transparency, accountability and privacy by design, notification of breaches to supervisors and to the people affected.

It has not entered into force. Its entry-into-force clause needs ratification by all parties to the original Convention, or by 38 of them. When Moldova ratified on 15 May 2026 it became the 34th. Four more are needed.

Eight years, thirty-four of thirty-eight.

For me this is a good example of why "status" has to be more than a label. The Data Initiatives Atlas records the treaty as adopted, not in force, with the arithmetic in the description: the threshold, the count, the date of the count, the gap.

A reader in 2027 should not need to trust our update schedule. They should be able to see the date of the number and judge for themselves.

How do you record a threshold that moves, like a ratification count, so that it remains honest when nobody is watching?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#Convention108 #CouncilOfEurope #dataprotection #metadata
```

*Check before posting: Count is as of 15 May 2026; coe.int was unreadable for our tools, so re-check the current figure before posting.*

### Post 30. Data rules hide in trade agreements

*Kind: Policy. Atlas entities: INTL-USMCA, INTL-MERCOSUR-ECOMMERCE-2021, INTL-EAEU-PROTOCOL-3-2023.*

```text
If you only read data protection laws, you miss a fair share of the rules.

• USMCA, in force since 1 July 2020: among its 34 chapters, Chapter 19 on digital trade covers personal information protection, cross-border information transfers, computing facilities, cybersecurity, source code and open government data. A joint review falls due on every sixth anniversary.
• The Mercosur e-commerce agreement, signed in Montevideo on 29 April 2021 by Argentina, Brazil, Paraguay and Uruguay: customs duties on electronic transmissions, e-signatures, consumer protection, personal data, cross-border transfers and data location. In force for Argentina from January 2026.
• The 2023 protocol to the Eurasian Economic Union Treaty, which extends a "transboundary space of trust" from government-to-government to business-to-government exchange of electronic documents.

None of these is a data protection law. All of them constrain what you can do with data across borders.

The Data Initiatives Atlas treats agreements as a separate type for this reason: a trade chapter and a privacy act are different instruments with different enforcement, and the same dataset may fall under both.

Does your transfer assessment include the trade agreements, or only the privacy laws?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#digitaltrade #dataflows #USMCA #Mercosur #datagovernance
```

### Post 31. The grandparent of many privacy laws

*Kind: Policy. Atlas entities: INTL-APEC-PRIVACY-FRAMEWORK-2015.*

```text
The APEC Privacy Framework, in its 2005 original, was modelled on the OECD Guidelines of 1980. The 2015 update draws on the OECD Guidelines of 2013. It has nine information privacy principles, guidance on domestic and international implementation, and the APEC Cross Border Privacy Rules system.

A good sign that a lot of privacy architecture across the world traces back to a handful of short, principles-based texts from the early 1980s. In my reading, the GDPR sits in the same lineage, and so does APEC. Many national laws the Data Initiatives Atlas reads are cousins.

For data people the lesson is practical. When two regimes look incompatible, look at the principles and not the clauses. The legal vocabulary differs. The principles (purpose limitation, accuracy, security, accountability) are much the same.

A good test of a policy mapping exercise: if it can only match clause to clause, it will break at the first rewrite. If it can match principle to principle, it will survive a few revisions.

What is the stable layer in your own policy mapping, and what is just clause numbering?

#privacy #APEC #OECD #dataprotection #crossborder
```

### Post 32. The oldest open data law is about the environment

*Kind: Policy. Atlas entities: UN-AARHUS, EU-INSPIRE.*

```text
Before open data portals, before the GDPR, there was Aarhus.

The UNECE Convention on Access to Information, Public Participation in Decision-making and Access to Justice in Environmental Matters was adopted on 25 June 1998 in Aarhus and has been in force since 30 October 2001. Its three pillars: access to information, public participation and access to justice. Article 1 requires Parties to guarantee those rights.

It had 48 Parties on 6 September 2026 according to the UN Treaty Collection, including the European Union and all 27 Member States. The most recent accession: Uzbekistan, on 25 March 2025.

In my reading, Aarhus is the root of a family: the EU environmental information rules, which Member States transposed into national law, and INSPIRE, which gave spatial data a metadata obligation. In the Data Initiatives Atlas you can follow that line from a 1998 treaty to a 2007 directive to national statutes.

I find that a useful corrective. We tend to think of open data as a 2010s invention. In law, it started with air, water and land.

What other "data" rules in your organisation have older roots than you think?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#opendata #Aarhus #environment #transparency #datagovernance
```

### Post 33. Most laws are patches

*Kind: Observation. Atlas entities: BE-HERGEBRUIK-WET-2023, DE-NIS2UMSUCG, CH-BGEID, GB-IPA-AMENDMENT-2024, NZ-PRIVACY-AMENDMENT-ACT-2025.*

```text
Read a few new laws and you notice that most of them are not new. They are diffs.

• Germany's NIS2 implementation did not create a new statute: it comprehensively revised the existing BSI Act.
• Belgium's 2023 open data act amends the federal re-use act of 2016.
• Switzerland's e-ID Act amends two existing federal acts.
• The UK's Investigatory Powers Act 2016 was amended in 2024.
• New Zealand's Privacy Act 2020 was amended in 2025.

The Data Initiatives Atlas has twenty "amends" relationships. That is a small number against 355 laws, and it means two things. First, we have probably only recorded the amendments we happened to see. Second, anything that looks at a law as a single document and not as a stack of amendments is going to be wrong somewhere.

This is why the repository model suits the subject. In Git, a change is a diff on top of what came before. In law, it is much the same, with worse tooling.

If your register holds only the original text of each law, how do you know what actually applies today?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#legaltech #consolidation #metadata #datagovernance #Git
```

### Post 34. Eighteen days before a date that may move

*Kind: Fact. Atlas entities: CL-LEY-21719, CL-AGENCIA-PDP.*

```text
Chile rewrote its data protection regime with Law 21.719, published on 13 December 2024. It amends the old Law 19.628, adds a sanctions regime for all data controllers and creates a new Agencia de Protección de Datos Personales.

Its main provisions were due to enter into force on 1 December 2026. On 28 October 2026 the Senate passed, by 33 votes to 6, a bill to postpone that date to 15 October 2027. The bill is now before the Chamber of Deputies. Until a new law is published, 1 December 2026 still applies.

Two things in the Data Initiatives Atlas make me look at this case twice.
First, the law is "adopted", not "active": formally made, not fully in force. Second, the agency is "planned": it exists in the statute, and its council had not been appointed when we last looked.

A deadline that is not yet final, a regulator that is not yet staffed, and a law that is already published. Which of the three is the date you plan against?

I would plan against the earliest one, and track the other two.

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#Chile #dataprotection #compliance #LATAM #datagovernance
```

*Check before posting: Date-sensitive and partly from secondary reporting (Emol/PPC Land): re-check the Chamber's vote and the 1 December date before posting.*

### Post 35. Law, rules, regulator: India's three layers

*Kind: Fact. Atlas entities: IN-DPDP-ACT-2023, IN-DPDP-RULES-2025, IN-DPB.*

```text
India's Digital Personal Data Protection Act was enacted on 11 August 2023. It rests on seven principles, calls controllers "Data Fiduciaries" and individuals "Data Principals", and sets penalties of up to 250 crore rupees for failing to keep reasonable security safeguards.

The DPDP Rules followed in 2025. They make the Data Protection Board of India a fully digital body of four members, with an online complaint portal and a mobile app, and send appeals to the Telecom Disputes Settlement and Appellate Tribunal.

The Data Initiatives Atlas records the Act as adopted, the Rules as adopted, and the Board as "planned". When we last looked, we could not find that the Board had been constituted.

A law is not a regulator. Between the date a statute passes and the date a functioning authority opens its first complaint, there can be years. A compliance function that reads only the first date will think enforcement exists, and a function that waits for the second will be late.

What is the status of the regulators you rely on: named, appointed, or operating?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#India #DPDP #dataprotection #regulation #datagovernance
```

*Check before posting: Re-check whether the Data Protection Board has been constituted before posting.*

### Post 36. Three sources, three dates, one law

*Kind: Metadata. Atlas entities: GM-PDPP-BILL-2024.*

```text
The Gambia's data protection bill is a small lesson in provenance.

The National Assembly's own bill page lists it as "assented", with a timeline entry dated 15 July 2026. Other sources give a different date for the assent. The Data Initiatives Atlas records the Assembly's page as the primary source, moves the status from "proposed" to "adopted", and states plainly that the date the law took effect is not established.

We did not pick a winner between the sources. We put the disagreement on the record, in a row in our list of open questions.

I think that is a good rule for any registry that people rely on. When sources disagree, a confident wrong date is worse than an honest unknown. The reader can resolve an unknown. A wrong date misleads them silently.

In metadata terms: a field should be able to say "unknown", "disputed" and "reported", not only a value.

How does your register show a date that two reliable sources disagree about?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#provenance #metadata #dataquality #Gambia #datagovernance
```

*Check before posting: Gambia's status could have changed since 9 November; confirm on assembly.gm.*

### Post 37. The date a page was posted is not the date a law was made

*Kind: Metadata. Atlas entities: BD-PDPA-2026, BD-NDMA-2026, BD-CPA-2026, BD-CPA-AMENDMENT-2026.*

```text
Bangladesh passed a cluster of data and cyber laws in 2026. The Data Initiatives Atlas holds four: a Personal Data Protection Act, a National Data Management Act, a Cyber Protection Act and an amendment to it.

What the Atlas actually knows about two of them is a listing: the ICT Division's page of laws and rules shows their Bengali titles and a listing date of 15 April 2026. That is the date the Division posted them, not necessarily when they were enacted or came into force. The gazette PDFs linked from it show Acts numbered 63, 80 and 99 of 2026, with the President's assent on 10 April 2026 and 1 July 2026. Which number belongs to which Act, we could not establish.

So the entity says exactly that. It carries no start date, and its description says the English title is our rendering of the Bengali and the text was not read.

I find a missing date more honest than a plausible one. In every metadata project I have seen, the worst errors are the invented values, not the empty ones.

How many of the dates in your register are "date we noticed it" rather than "date it happened"?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#metadata #dataquality #Bangladesh #provenance #datagovernance
```

### Post 38. A bill can die without a vote

*Kind: Fact. Atlas entities: ES-PLO-IA, ES-LCGC.*

```text
Spain's bill to adapt national law to the EU AI Act was presented to the Congreso de los Diputados on 28 May 2026 and published on 12 June 2026. It would have designated the national competent authorities that article 70 of the Regulation requires.

It never became law. The Cortes Generales were dissolved by Real Decreto 806/2026 on 5 October 2026, and the Congreso's own file page now records the initiative as "caducado": lapsed. The expiry was published in the Boletín Oficial de las Cortes Generales on 4 November 2026.

Nobody voted it down. The clock simply stopped.

In the Data Initiatives Atlas it is "archived", with an end date of 6 October 2026, the first day the file shows as concluded. It sits next to Spain's other pending cybersecurity bill, which is an earlier-stage draft that never reached the Cortes at all.

For compliance and policy people the lesson is plain. "Pending" is not a stable state. A bill can pass, fail, or lapse, and a tracker that only knows "in progress" and "enacted" will show a dead bill as alive for months.

Does your tracker have a "lapsed" state?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#AIAct #Spain #legislation #compliance #datagovernance
```

### Post 39. Eleven days from vote to force

*Kind: Fact. Atlas entities: SV-LEY-PDP-2024.*

```text
El Salvador's personal data protection law, Decreto 144, shows how many dates one statute can have:

• 12 November 2024: passed by the Legislative Assembly.
• 14 November 2024: sanctioned by the President.
• 15 November 2024: published in the Diario Oficial, Tomo 445, number 219.
• 23 November 2024: in force. Article 64 says eight days after publication.

Four dates in eleven days. Which one is "the date of the law"? It depends on who is asking: a legislator, a lawyer, a compliance officer or a regulator.

The Data Initiatives Atlas uses the entry-into-force date as the start date and lists the others in the description, each with its source: the page images of the Diario Oficial itself, read page by page.

One more detail I like. The law refers to a body called the ACE, the State Cybersecurity Agency, as the one that issues sanction resolutions. A cybersecurity agency enforcing data protection is an interesting institutional choice. The Atlas marks the agency's own status as "unknown", because we could not confirm it from a page of its own.

How many "dates of the law" does your register hold, and does anyone know which one the downstream reports use?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#ElSalvador #dataprotection #metadata #LATAM #datagovernance
```

### Post 40. The law is the headline, the decree is the content

*Kind: Observation. Atlas entities: VN-LAW-91-2025.*

```text
Viet Nam's Law on Personal Data Protection, Law No. 91/2025/QH15, was adopted by the National Assembly on 26 June 2025 and took effect on 1 January 2026, according to a State Bank of Viet Nam page. The same page cites a Prime Minister's decision on an implementation plan, dated 29 November 2025, and notes that many articles leave the detail to the Government.

It names no state agency in charge and no implementing decree. So the Data Initiatives Atlas models the Law and nothing around it: no authority, no decree. We did not open the text of the Law itself, and the entity says so.

That is a common pattern. Framework laws state principles and delegate the specifics to subordinate legislation: decrees, regulations, ministerial orders. The Atlas has a separate entity type for those, with 18 so far, so a reader can tell the statute from the instrument that gives it teeth.

If your compliance register stops at the statute, you may be tracking the preamble and missing the content.

Do you follow the delegated layer too, and who tracks it when it changes?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#Vietnam #dataprotection #regulation #subordinatelegislation #datagovernance
```

### Post 41. Even standards have end dates

*Kind: Fact. Atlas entities: GB-BS-10012, INTL-ISO-IEC-27001.*

```text
BS 10012 was published by BSI on 31 July 2018. It specified requirements for a personal information management system, revised in line with the GDPR. BSI's own catalogue shows it as withdrawn on 24 April 2026.

In the Data Initiatives Atlas it is one of three entities marked "archived", with an end date.

This matters more than it sounds. Policies, procurement documents and certifications cite standards by number and often by year: "compliant with BS 10012:2017+A1:2018". When the standard is withdrawn, those references do not break. They simply become references to something that no longer gets maintained.

The Atlas holds 38 standards, from ISO/IEC 27001 and 27002 to DMARC, DKIM, SPF and DNSSEC, DCAT-AP and several national e-invoicing formats. Each has an end date field, and for most the field is empty. Empty means "still current", not "never checked".

Do you have a list of the standards your policies cite, and a date you last confirmed that each is still current?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#standards #ISO27001 #governance #metadata #compliance
```

### Post 42. Nine of the 21

*Kind: Observation. Atlas entities: NL-DATA-AGENDA-OVERHEID, NL-DIGIBETER, NL-WERKAGENDA-WAARDENGEDREVEN-DIGITALISEREN, NL-NOIV, NL-EAR, NL-WBP, NL-WOB, NL-WBNI, NL-CCS, DE-DIGITALSTRATEGIE.*

```text
The Data Initiatives Atlas has 21 entities marked "superseded". Nine of them are Dutch: three digital government agendas, two programmes and architecture bodies, three laws and a statistics commission.

The tempting reading is that the Netherlands renews its policy faster than everyone else. The more honest reading is that we have researched the Netherlands in depth, and depth is where you find the history.

Germany's Digitalstrategie, adopted by cabinet resolution on 31 August 2022 as the first complete digital strategy to be adopted that way, is in the Atlas as "archived". Its horizon was 2025: 25 fields of action, 135 targets, 20 flagship projects, and an aim to be in the top ten of the EU's digital economy index by 2025, up from 13th of 27 in 2022.

Strategies are the shortest-lived objects in this domain. They have a horizon, a name and a minister. When the minister changes, the name often does too.

A map of policy needs to keep the old strategies, because the interesting question is usually what replaced what.

How do you keep your own past strategies findable once they are replaced?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#digitalgovernment #strategy #policy #datagovernance #Netherlands #Germany
```

### Post 43. Measuring digital government by mystery shopping

*Kind: Metadata. Atlas entities: EU-EGOV-BENCHMARK.*

```text
The European Commission's eGovernment Benchmark is a methodology worth reading, not just a ranking.

The 2025 edition covers 35 countries: the 27 Member States plus Iceland, Norway, Switzerland, Albania, Montenegro, North Macedonia, Serbia and Türkiye. It assessed 14,104 government websites across nine key life events, with 20 indicators and 51 survey questions, using an EU-wide network of mystery shoppers in November 2024.

I like it because the method is part of the result. You cannot interpret "the score is 78" without knowing that humans were asked to complete a task on a live service in a particular month.

That is exactly what good metadata is for: the sampling period, the number of sites, the indicator definitions. Without them an index is a rumour with decimals.

The Data Initiatives Atlas lists the Benchmark as a publication, with 37 typed relationships to the countries and bodies it measures.

When you cite an index in a board paper, do you also cite its method and the date it was measured?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#egovernment #metadata #indicators #digitalpublicservices #datagovernance
```

### Post 44. A country page with nothing but an anchor is a promise

*Kind: Confession. Atlas entities: README, discovery/candidates.md.*

```text
The Data Initiatives Atlas has 169 country scopes. Only 134 of them have national entities beyond the anchor page itself. The other 35 are placeholders.

An anchor is the minimum: a country, its place in the UN, regional bodies and a link to the next thing. It is a promise that something will follow, not a statement that nothing exists.

We keep a plain count of which UN member states have no anchor at all. It was 106 in mid-October 2026 and 25 in early November, as we added small states one by one, from Eswatini and Antigua and Barbuda to Tuvalu and Guinea-Bissau. We do not pretend the long tail is deep. For several countries the only readable source for a law is a scan of a gazette or a copy on a law-firm site, and we say which.

Coverage honesty is a metadata field too. "Number of entities per country" is not a quality measure, and a map with the same level of detail everywhere would be a lie.

Where is your data catalogue a promise, and does it say so?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#coverage #opendata #metadata #datagovernance #transparency
```

*Check before posting: Counts change with every batch; update 134/35/25 from the live site before posting.*

### Post 45. Which law is the hub?

*Kind: Question. Atlas entities: EU-GDPR, EU-NIS2, EU-OPEN-DATA-DIRECTIVE, EU-EIDAS, EU-INSPIRE, EU-EDPB.*

```text
A small experiment. In the Data Initiatives Atlas, which legislative node has the most connections?

1. The GDPR, with 180.
2. NIS2, with 148.
3. The Open Data Directive, with 136.
4. eIDAS, with 105.
5. INSPIRE, with 90. The European Data Protection Board is close behind, with 89.

Would you have guessed that order? I would have put the Open Data Directive lower, and I would not have expected NIS2 to be that close to the GDPR in only two years.

Two honest caveats. First, a hub in a graph reflects what the graph's authors read. We read a lot of national NIS2 transpositions in 2026, and the NIS2 count probably rose with them. Second, degree is a blunt instrument: it counts links, not importance.

Still, I find the exercise useful as a check on your own assumptions. Before you build a data governance programme around a particular law, look at what actually touches it.

Which regulation do you think is the real hub of your own compliance landscape?

Explore: https://dalust.github.io/Data-Initiatives-Atlas/

#GDPR #NIS2 #datagovernance #knowledgegraph #networkanalysis
```

*Check before posting: Degrees are as of 2026-11-13 and move whenever entities are added.*

## Before posting

- Sections 1 and 2: the figures in post 1 are as of 2026-10-09; update them to the live counts on the site
  if you post later. Section 2 is the text posted from the profile for release 2026.10.2.
- Section 3: figures are as of 2026-11-13. The posts marked "Check before posting" depend on dates that
  move (Euro 7 applies from 29 November 2026; Chile's 1 December 2026 date and its postponement bill; the
  Swiss e-ID and the EU KIDS Act; the Irish and French NIS2 bills; India's Data Protection Board; the
  Convention 108+ ratification count; the Digital Omnibus). Re-check those on the day.
- Posts 5, 13 and 14 describe the NIS2 infringement procedure. The referral of 8 July 2026 and the 2.8
  million euro penalty come from secondary sources cited in the entities, not from a Commission page.
- A post on a Page can carry an image. The Atlas logo (a small network of five coloured nodes) was
  made for the LinkedIn app and suits it.
- To post the same text on the profile and the Page from a release draft, the release workflows do it
  (`docs/credentials.md` sections 2 and 3). The idea posts are not automated: post them by hand.
