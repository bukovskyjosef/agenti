# Agent entrypoint

Tento soubor je povinný vstupní bod pro každého agenta pracujícího v repozitáři.

## 1. Než začneš pracovat

1. Přečti GitHub Issue, na kterém máš pracovat.
2. Urči svoji explicitní roli podle issue.
3. Načti pouze normativní dokumenty potřebné pro tuto roli a úkol podle [`docs/README.md`](docs/README.md).
4. Ověř, že issue splňuje Definition of Ready v [`docs/issue-standard.md`](docs/issue-standard.md).
5. Pokud chybí produktové rozhodnutí, nezačínej implementovat. Eskaluj otázku člověku podle [`docs/governance.md`](docs/governance.md).

## 2. Absolutní pravidla

- GitHub prostor tohoto repozitáře je jediný zdroj pravdy. Externí chat není autoritativní.
- `main` je autoritativní stav. Otevřená branch nebo PR je pouze návrh změny.
- Pracuj pouze v kompetenci své role podle [`docs/roles.md`](docs/roles.md).
- Neměň nic mimo scope issue jen proto, že sis všiml problému. Zaznamenej nový problém, neopravuj ho bez oprávnění.
- Nevytvářej nové produktové požadavky ani nerozhoduj produktové nejasnosti.
- Neduplicuj kanonické informace. Odkazuj na ně.
- Načítej minimum kontextu potřebného pro úkol.
- Každá změna musí být dohledatelná k issue a ověřitelná proti acceptance criteria.
- Dokončení určuj podle typu výsledku práce a pravidel v [`docs/issue-standard.md`](docs/issue-standard.md); review nebo test nevytváří automaticky nekonečný řetězec dalších review.

## 3. Standardní workflow

Řiď se [`docs/workflow.md`](docs/workflow.md) a pravidly nezávislé kontroly v [`docs/review-model.md`](docs/review-model.md).

## 4. Když narazíš na problém mimo scope

Neopravuj jej oportunisticky. Uveď ho jako samostatný nález a předej orchestrátorovi nebo založ samostatné issue, pokud to tvoje role dovoluje.

## 5. Když si pravidla odporují

Nevol si vlastní interpretaci. Označ konflikt, zastav dotčenou část práce a nech konflikt vyřešit na kanonickém místě.
