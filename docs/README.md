# Normative documentation map

Tento adresář obsahuje autoritativní pravidla agentního systému. Každá rodina pravidel má jedno kanonické místo. Ostatní dokumenty ji mohou pouze stručně shrnout pro orientaci a odkázat na jejího vlastníka; shrnutí není druhou normativní definicí.

## Povinné minimum pro každého agenta

Každý agent čte:

1. `/AGENTS.md`,
2. své GitHub Issue,
3. níže uvedený dokument pro svoji roli nebo fázi práce.

`AGENTS.md` je povinný provozní router. Jeho stručná připomenutí pravidel jsou orientační; kanonickým vlastníkem detailního pravidla je dokument uvedený v mapě níže.

## Kanoničtí vlastníci pravidel

| Rodina pravidel | Kanonický vlastník |
|---|---|
| celkový model spolupráce a agentního toku | [`operating-model.md`](operating-model.md) |
| autorita, rozhodování, konflikty a produktová autonomie | [`governance.md`](governance.md) |
| role, kompetence a jejich hranice | [`roles.md`](roles.md) |
| pořadí fází a předávání mezi nimi | [`workflow.md`](workflow.md) |
| Issue kontrakt, lifecycle/status semantics, DoR, concurrency, completion a control gates | [`issue-standard.md`](issue-standard.md) |
| nezávislé review, severity/disposition a corrective loop | [`review-model.md`](review-model.md) |
| durable agent-to-agent handoff a cílové GitHub artefakty | [`handoff-protocol.md`](handoff-protocol.md) |
| automatické spouštění/chaining rolí, least privilege a provider adapters | [`automation-model.md`](automation-model.md) |
| načítání, persistence a minimalizace kontextu | [`context-policy.md`](context-policy.md) |
| informační architektura a umístění artefaktů | [`repository-structure.md`](repository-structure.md) |
| zavedení modelu do jiného repozitáře | [`adoption-guide.md`](adoption-guide.md) |

Pokud by dvě místa odpovídala na stejnou normativní otázku, platí vlastník uvedený v této mapě a duplicitní formulace se má změnit na odkaz nebo orientační shrnutí.

## Kontext podle potřeby

| Dokument | Kdy jej číst |
|---|---|
| [`operating-model.md`](operating-model.md) | při pochopení celkového způsobu spolupráce rolí |
| [`governance.md`](governance.md) | při nejasnosti autority, rozhodování, konfliktu pravidel nebo scope |
| [`roles.md`](roles.md) | vždy při převzetí role; načti relevantní sekci |
| [`workflow.md`](workflow.md) | při zahájení nebo předání práce mezi fázemi |
| [`issue-standard.md`](issue-standard.md) | analytik, orchestrátor a každý agent před zahájením práce |
| [`review-model.md`](review-model.md) | developer, tester, reviewer a orchestrátor při kontrole změny |
| [`handoff-protocol.md`](handoff-protocol.md) | před dokončením role nebo převzetím práce od jiné role |
| [`automation-model.md`](automation-model.md) | při automatizaci triggerů, orchestrace, provider adapterů nebo role chainingu |
| [`context-policy.md`](context-policy.md) | při práci s větším repozitářem nebo při hledání kontextu |
| [`repository-structure.md`](repository-structure.md) | při zakládání nebo reorganizaci projektu |
| [`adoption-guide.md`](adoption-guide.md) | při zavádění tohoto modelu do jiného repozitáře |

## Pravidlo proti duplicitám

Pokud normativní informace již existuje u svého kanonického vlastníka, jiný dokument ji nesmí znovu nezávisle definovat. Může ji stručně připomenout pouze pro routing nebo lokální srozumitelnost, musí však zachovat stejný význam a odkázat na kanonického vlastníka.

## Typy informací

- **Aktuální normativní pravidla:** příslušné kanonické dokumenty `docs/*.md` podle mapy výše.
- **Agentní a lidské entrypointy:** `AGENTS.md` a kořenový `README.md`; orientují a odkazují, ale nevytvářejí paralelní vlastnictví detailních pravidel.
- **Provider/tool adapters:** například `CLAUDE.md`, Codex/IDE instrukce nebo workflow prompty; technicky mapují kanonický model na nástroj, ale nejsou vyšší autoritou než `docs/`.
- **Rozhodovací záznamy:** `docs/decisions/` a GitHub decision artefakty; uchovávají kontext, rozhodnutí a auditní historii. Po propsání rozhodnutí nejsou aktuální provozní specifikací; tu vlastní příslušný kanonický normativní dokument.
- **Pracovní úkoly:** GitHub Issues.
- **Návrhy změn, implementační handoff a jejich kontrola:** branches, Pull Requests, reviews, checks a jejich komentáře.
- **Historické nebo pomocné materiály:** pouze pokud jsou jasně označené jako neautoritativní pro aktuální provozní stav.
