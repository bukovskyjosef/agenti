# Agenti

Referenční repozitář pro návrh a provoz agentního systému v softwarových projektech.

Tento repozitář **neobsahuje reálný produkt**. Produktem je samotný způsob práce: pravidla, role, workflow, informační architektura a šablony, podle kterých mohou být řízeny další projekty s AI agenty.

## Základní princip

Projekt musí být pochopitelný a zpracovatelný agentem, který přichází bez kontextu z předchozí konverzace. Vše potřebné pro práci musí být dohledatelné v GitHub prostoru daného repozitáře.

- `main` obsahuje aktuální autoritativní stav.
- Trvalé znalosti, pravidla a rozhodnutí patří do verzovaných souborů repozitáře.
- Pracovní úkoly a jejich stav patří do GitHub Issues.
- Změny se připravují v branchech a Pull Requests.
- Chat, osobní paměť agenta ani externí poznámky nejsou zdrojem pravdy.
- Produktová rozhodnutí dělá člověk.
- Agenti pracují v explicitních rolích a nepřekračují své kompetence.
- Každá informace má jedno kanonické místo; ostatní dokumenty na ni pouze odkazují.
- Kontext se načítá cíleně, ne plošně, aby agent spotřeboval minimum tokenů potřebných pro kvalitní práci.

## Kde začít

Agent vždy začíná v [`AGENTS.md`](AGENTS.md).

Detailní normativní pravidla jsou v [`docs/`](docs/README.md).

## Co tento repozitář definuje

1. autoritu člověka a agentů,
2. role a jejich kompetence,
3. životní cyklus úkolu,
4. standard kvalitního GitHub Issue,
5. model nezávislé kontroly práce,
6. pravidla práce s kontextem a tokeny,
7. informační architekturu repozitáře,
8. způsob přenosu tohoto modelu do dalších projektů.

## Status

Repozitář je budován jako živý etalon. Změny jeho governance jsou produktovými změnami tohoto repozitáře a podléhají lidskému rozhodnutí.
