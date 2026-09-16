# agenti

Referenční repozitář pro návrh, řízení a kontrolu práce AI agentů v dalších projektech.

Tento repozitář **není reálný aplikační produkt**. Produktem je samotný způsob práce: governance, role, workflow, informační architektura a šablony, které mají být znovu použitelné v jiných repozitářích.

## Základní principy

- GitHub prostor projektu je jediným zdrojem pravdy.
- Nový agent musí být schopen začít práci bez neveřejného kontextu z předchozího chatu.
- Práce se eviduje v GitHub Issues.
- Každý agent pracuje v explicitní roli a nepřekračuje její kompetence.
- Agenti se vzájemně kontrolují, ale nekonkurují si a neopravují oportunisticky práci jiných rolí.
- Produktová a governance rozhodnutí dělá Human / Product Owner.
- Normativní informace má mít jedno kanonické místo.
- Scope práce se připravuje tak, aby realizace nevznikala z domněnek.
- Kontext se načítá cíleně; cílem je nejmenší úplný kontext, ne co největší množství dokumentace.
- Dokončení práce se posuzuje podle typu výsledku; kontrolní práce nevytváří automaticky nekonečný řetězec dalších kontrol.

## Pro agenty

Začni v [`AGENTS.md`](AGENTS.md). Ten je krátkým routerem do relevantních kanonických pravidel.

## Pro člověka

Normativní dokumentace je mapována v [`docs/README.md`](docs/README.md). Významná rozhodnutí a jejich historie patří do `docs/decisions/`, zatímco konkrétní práce a aktuální rozhodovací fronta jsou evidované v GitHub Issues.

## Účel použití

Tento repozitář má sloužit jako:

- etalon pro nové projekty,
- zdroj best practices pro agentní práci,
- výchozí governance model,
- testovací prostředí pro zlepšování spolupráce více agentních rolí,
- návod, jak udržet předání práce mezi agentními instancemi deterministické a levné na kontext.

Při přebírání modelu do konkrétního projektu se kopírují principy a odpovědnosti, ne nutně každý soubor beze změny. Praktický postup popisuje [`docs/adoption-guide.md`](docs/adoption-guide.md).
