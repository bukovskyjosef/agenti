# Agent entrypoint

Tento soubor je povinný vstupní bod pro každého agenta pracujícího v repozitáři. Slouží jako provozní router a stručné připomenutí pravidel; nevytváří paralelní kanonické definice tam, kde má daná rodina pravidel vlastníka v [`docs/README.md`](docs/README.md).

## 1. Než začneš pracovat

1. Přečti GitHub Issue, na kterém máš pracovat.
2. Urči svoji explicitní roli podle issue.
3. Načti pouze normativní dokumenty potřebné pro tuto roli a úkol podle [`docs/README.md`](docs/README.md).
4. Ověř stav Issue, dependencies, concurrency a podmínky Ready podle [`docs/issue-standard.md`](docs/issue-standard.md).
5. Pokud chybí produktové nebo governance rozhodnutí, nezačínej implementovat. Eskaluj otázku podle [`docs/governance.md`](docs/governance.md) a decision loopu ve [`docs/workflow.md`](docs/workflow.md).
6. Před dokončením role persistuj výsledek podle [`docs/handoff-protocol.md`](docs/handoff-protocol.md).

## 2. Absolutní pravidla

Následující body jsou startup souhrn. Jejich kanonické vlastníky určuje [`docs/README.md`](docs/README.md):

- GitHub prostor tohoto repozitáře je jediný zdroj pravdy. Externí chat není autoritativní handoff kanál.
- `main` je autoritativní stav tohoto referenčního repozitáře. Otevřená branch nebo PR je návrh změny.
- Pracuj pouze v kompetenci své role podle [`docs/roles.md`](docs/roles.md).
- Neměň nic mimo scope issue jen proto, že sis všiml problému.
- Nevytvářej nové produktové požadavky ani nerozhoduj produktové nejasnosti.
- Severity nálezu sama není oprávnění k nové implementaci; disposition určuje [`docs/review-model.md`](docs/review-model.md).
- Neduplicuj kanonické informace. Odkazuj na ně.
- Načítej minimum úplného kontextu potřebného pro úkol.
- Každá změna musí být dohledatelná k issue a ověřitelná proti acceptance criteria.
- Automatizace ani provider-specific adapter nesmí rozšířit pravomoci role nebo obejít control gates; viz [`docs/automation-model.md`](docs/automation-model.md).

## 3. Standardní workflow

Řiď se [`docs/workflow.md`](docs/workflow.md), pracovním kontraktem v [`docs/issue-standard.md`](docs/issue-standard.md), pravidly nezávislé kontroly v [`docs/review-model.md`](docs/review-model.md) a durable handoffem v [`docs/handoff-protocol.md`](docs/handoff-protocol.md).

## 4. Když narazíš na problém mimo scope

Neopravuj jej oportunisticky. Zaznamenej finding podle jeho skutečné disposition a předej ho správné roli. Samostatné Issue zakládej jen pokud to tvoje role dovoluje a finding skutečně vyžaduje samostatný follow-up.

## 5. Když si pravidla odporují

Nevol si vlastní interpretaci. Označ konflikt, zastav dotčenou část práce a postupuj podle kanonických pravidel autority a konfliktů v [`docs/governance.md`](docs/governance.md).

## 6. Pokud tě spustila automatizace

Trigger je pouze technický vstup. Nejdřív rekonstruuj aktuální stav z repozitáře/GitHubu a proveď jen krok, který je podle trvalého kontraktu a tvé role již autorizovaný. Selhání nebo blocker zanech durable podle [`docs/automation-model.md`](docs/automation-model.md).
