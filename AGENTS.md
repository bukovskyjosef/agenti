# Agent entrypoint

Tento soubor je povinný vstupní bod pro každého agenta pracujícího v repozitáři. Slouží jako provozní router a stručné připomenutí pravidel; nevytváří paralelní kanonické definice tam, kde má daná rodina pravidel vlastníka v [`docs/README.md`](docs/README.md).

## 1. Než začneš pracovat

1. Přečti GitHub Issue, na kterém máš pracovat.
2. Urči svoji explicitní roli podle issue.
3. Načti pouze normativní dokumenty potřebné pro tuto roli a úkol podle [`docs/README.md`](docs/README.md).
4. Ověř stav Issue a podmínky Ready podle [`docs/issue-standard.md`](docs/issue-standard.md).
5. Pokud chybí produktové rozhodnutí, nezačínej implementovat. Eskaluj otázku člověku podle [`docs/governance.md`](docs/governance.md).

## 2. Absolutní pravidla

Následující body jsou startup souhrn. Jejich kanonické vlastníky určuje [`docs/README.md`](docs/README.md):

- GitHub prostor tohoto repozitáře je jediný zdroj pravdy. Externí chat není autoritativní.
- `main` je autoritativní stav. Otevřená branch nebo PR je pouze návrh změny.
- Pracuj pouze v kompetenci své role podle [`docs/roles.md`](docs/roles.md).
- Neměň nic mimo scope issue jen proto, že sis všiml problému. Zaznamenej nový problém, neopravuj ho bez oprávnění.
- Nevytvářej nové produktové požadavky ani nerozhoduj produktové nejasnosti.
- Neduplicuj kanonické informace. Odkazuj na ně.
- Načítej minimum kontextu potřebného pro úkol.
- Každá změna musí být dohledatelná k issue a ověřitelná proti acceptance criteria.

## 3. Standardní workflow

Řiď se [`docs/workflow.md`](docs/workflow.md) a pravidly nezávislé kontroly v [`docs/review-model.md`](docs/review-model.md).

## 4. Když narazíš na problém mimo scope

Neopravuj jej oportunisticky. Uveď ho jako samostatný nález a předej orchestrátorovi nebo založ samostatné issue, pokud to tvoje role podle [`docs/roles.md`](docs/roles.md) dovoluje.

## 5. Když si pravidla odporují

Nevol si vlastní interpretaci. Označ konflikt, zastav dotčenou část práce a postupuj podle kanonických pravidel autority a konfliktů v [`docs/governance.md`](docs/governance.md).
