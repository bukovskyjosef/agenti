# Normative documentation map

Tento adresář obsahuje autoritativní pravidla agentního systému. Každé pravidlo má mít jedno kanonické místo.

## Povinné minimum pro každého agenta

Každý agent čte:

1. `/AGENTS.md`,
2. své GitHub Issue,
3. níže uvedený dokument pro svoji roli nebo fázi práce.

## Kontext podle potřeby

| Dokument | Kdy jej číst |
|---|---|
| [`operating-model.md`](operating-model.md) | při pochopení celkového způsobu spolupráce rolí a handoffů |
| [`governance.md`](governance.md) | při nejasnosti autority, rozhodování, konfliktu pravidel nebo scope |
| [`roles.md`](roles.md) | vždy při převzetí role; načti relevantní sekci |
| [`workflow.md`](workflow.md) | při zahájení nebo předání práce mezi rolemi |
| [`issue-standard.md`](issue-standard.md) | analytik, orchestrátor a každý agent před zahájením práce |
| [`review-model.md`](review-model.md) | developer, tester, reviewer a orchestrátor při kontrole změny |
| [`context-policy.md`](context-policy.md) | při práci s větším repozitářem nebo při hledání kontextu |
| [`repository-structure.md`](repository-structure.md) | při zakládání nebo reorganizaci projektu |
| [`adoption-guide.md`](adoption-guide.md) | při zavádění tohoto modelu do jiného repozitáře |

## Pravidlo proti duplicitám

Pokud informace již existuje v jednom z těchto dokumentů, jiný dokument ji nesmí znovu normativně definovat. Může pouze stručně vysvětlit kontext a odkázat na kanonické místo.

## Typy informací

- **Normativní pravidla:** `docs/*.md` a kořenový `AGENTS.md`.
- **Produktová a governance rozhodnutí:** `docs/decisions/`.
- **Pracovní úkoly:** GitHub Issues.
- **Návrhy změn a jejich diskuse:** branches a Pull Requests.
- **Historické nebo pomocné materiály:** pouze pokud jsou jasně označené jako neautoritativní.
