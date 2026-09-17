# Durable agent handoff protocol

Tento dokument je kanonickým vlastníkem pravidel pro **předávání výsledků mezi rolemi**. Cílem je, aby člověk nebyl message bus mezi agenty a aby každý další agent mohl navázat pouze z trvalého GitHub stavu.

## Základní pravidlo

Agentní handoff je dokončený teprve tehdy, když je výsledek zapsán do správného trvalého GitHub artefaktu.

Chat může člověku stručně shrnout stav, ale nesmí být jediným místem, kde zůstane:

- výsledek práce,
- review nebo testovací závěr,
- blocker,
- rozhodnutí,
- změna závislosti nebo pořadí,
- informace nutná pro další roli.

Pokud agent má oprávnění zapisovat do GitHubu, musí handoff persistovat před tím, než práci označí jako dokončenou. Pokud zápis technicky není možný, musí výstup označit `NOT PERSISTED — HANDOFF INCOMPLETE` a dodat přesný text a cílový artefakt; nesmí tvrdit, že další role může bezpečně pokračovat pouze z chatu.

## Kanonické cíle podle role nebo události

| Role / událost | Trvalý cíl | Minimální obsah |
|---|---|---|
| Orchestrátor vytváří nebo mění pracovní kontrakt | GitHub Issue body | lifecycle stav, goal, scope/out-of-scope, acceptance criteria, dependencies, concurrency, shared surfaces, decision gates, required control gates |
| Orchestrátor mění pořadí, ownership nebo blocker | Issue comment a podle potřeby aktualizovaný Issue body | co se změnilo, proč, co je nyní vykonatelné a kdo je další role |
| Analytik dokončuje analýzu | Issue body / linked decision artifact | doplněný kontrakt, nejasnosti, rozhodovací body a readiness stav |
| Asistentka zpracuje lidské rozhodnutí | decision/work Issue a podle potřeby kanonický normativní artefakt | přesné lidské rozhodnutí, dopad a další vykonatelný krok |
| Vývojář předává implementaci | Pull Request body + commit(y) | linked Issue, implementovaný scope, záměrně neprovedený scope, ověření, shared-contract dopad, rizika/follow-up |
| Vývojář narazí na blocker | Issue comment; pokud existuje PR, odkaz nebo zrcadlení v PR | minimální blocker, evidence, dotčené AC/kontrakt a potřebná další autorita |
| Reviewer předává review | formální PR review, pokud je dostupné; jinak PR comment | celkový outcome, findingy se severity + disposition, důkazy a autorizovaný další krok |
| Tester předává ověření | PR comment nebo testovací Issue podle kontraktu | testovaný head/artefakt, prostředí/commands, scénáře, PASS/FAIL/INCONCLUSIVE a evidence |
| Integrátor provádí merge/promotion | PR/release PR comment + výsledný Issue stav | integrovaný SHA, cílová větev/prostředí, splněné gates, případné blokace |
| Automatizace selže tak, že workflow nemůže pokračovat | trvalý blocker Issue nebo ekvivalentní GitHub artefakt | zdroj práce, role/workflow, identifikátor běhu, bezpečný popis selhání a požadovaný další krok bez secret/log dumpu |

Rutinní agentní report se nemá ukládat jako nový committed `*-report.md`, pokud samotný report není schváleným projektovým deliverablem nebo kanonickou specifikací. Issue/PR a jejich review vlákna jsou task-local auditní stopa.

## Standardní report headers

Stabilní hlavičky zlepšují čitelnost i budoucí automatizaci. Doporučený formát:

```text
## AGENT REPORT — COORDINATOR
## AGENT REPORT — ANALYST
## AGENT REPORT — ASSISTANT
## AGENT REPORT — DEVELOPER
## AGENT REPORT — REVIEWER
## AGENT REPORT — TESTER
## AGENT REPORT — INTEGRATOR
```

Projekt může lokalizovat zobrazované názvy, ale strojově rozpoznatelná struktura má zůstat stabilní.

## Read-before-act

Přebírající role nesmí spoléhat na předávací prompt jako na aktuální stav. Před akcí rekonstruuje potřebný stav z GitHubu.

Minimálně:

- vykonávající role čte aktuální Issue body, relevantní komentáře/rozhodnutí a deklarované dependencies,
- Reviewer čte linked Issue, PR body, skutečný diff/commity, předchozí review/test evidence a aktuální checks,
- Tester čte acceptance criteria, testovaný head a relevantní review findingy,
- Integrátor čte linked Issue, přesný PR head, required gates, review/test outcomes a nevyřešená vlákna,
- automatizovaný Orchestrátor vždy rekonstruuje stav z repozitáře/GitHubu a nepovažuje trigger text za náhradu governance.

## Handoff a scope

Předání výsledku samo o sobě nerozšiřuje oprávnění další role. Reviewer finding, tester failure ani automatizační trigger nejsou autorizací k implementaci nového scope. Autoritu dalšího kroku určuje pracovní kontrakt, [`review-model.md`](review-model.md), [`roles.md`](roles.md) a případné explicitní lidské rozhodnutí.
