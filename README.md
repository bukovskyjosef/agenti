# Agenti

Referenční repozitář pro cílový návrh a provoz agentního systému v softwarových projektech.

Tento repozitář **neobsahuje reálný produkt**. Produktem je samotný způsob práce: pravidla, role, workflow, informační architektura, durable handoff, automatizační kontrakt a šablony, podle kterých mohou být řízeny další projekty s AI agenty.

## Základní princip

Projekt musí být pochopitelný a zpracovatelný agentem, který přichází bez kontextu z předchozí konverzace. Vše potřebné pro práci musí být dohledatelné v GitHub prostoru daného repozitáře.

Tento README je lidský vstupní bod a orientační souhrn. Aktuální normativní pravidla vlastní kanonické dokumenty mapované v [`docs/README.md`](docs/README.md); tento soubor je nemá paralelně redefinovat.

- `main` obsahuje aktuální autoritativní stav tohoto referenčního modelu.
- Trvalé znalosti, pravidla a rozhodnutí patří do verzovaných souborů repozitáře na jejich kanonická místa.
- Pracovní úkoly a jejich stav patří do GitHub Issues.
- Změny se připravují v branchech a Pull Requests a před integrací procházejí předepsanými control gates.
- Chat, osobní paměť agenta ani externí poznámky nejsou zdrojem pravdy ani agent-to-agent message bus.
- Produktová rozhodnutí dělá člověk.
- Agenti pracují v explicitních rolích a nepřekračují své kompetence.
- Rutinní předávání a orchestrace mají být proveditelné durable přes GitHub a mohou být bezpečně automatizované.
- Severity review nálezu sama není oprávnění rozšířit scope; autoritu dalšího kroku určuje jeho disposition.
- Každá rodina pravidel má jedno kanonické místo; ostatní dokumenty ji pouze orientačně shrnují nebo odkazují.
- Kontext se načítá cíleně, ne plošně, aby agent spotřeboval minimum tokenů potřebných pro kvalitní práci.

## Kde začít

Agent vždy začíná v [`AGENTS.md`](AGENTS.md).

Mapa kanonických pravidel a detailní normativní dokumentace je v [`docs/README.md`](docs/README.md).

## Co tento repozitář definuje

1. autoritu člověka a agentů,
2. role a jejich kompetence,
3. životní cyklus a concurrency pracovních úkolů,
4. standard kvalitního GitHub Issue/work contractu,
5. model nezávislé kontroly včetně severity × disposition,
6. durable handoff mezi rolemi bez člověka jako message bus,
7. provider-neutral model automatické orchestrace a chainingu,
8. pravidla práce s kontextem a tokeny,
9. informační architekturu repozitáře a provider adapters,
10. způsob přenosu tohoto modelu do dalších projektů.

## Status

Repozitář je budován jako živý etalon cílového stavu. Změny jeho governance jsou produktovými změnami tohoto repozitáře a podléhají lidskému rozhodnutí a předepsanému review.

Návrhy, experimenty a diskuse nejsou součástí autoritativního cílového modelu, dokud nejsou přijaté a integrovány do `main`.
