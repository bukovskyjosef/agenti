# Reference repository structure

Cílem struktury je, aby agent rychle rozpoznal, kde hledat autoritativní informaci, kam uložit durable handoff a které soubory jsou pouze provider/tool adaptéry.

## Doporučený kořen projektu

```text
/
├── README.md
├── AGENTS.md
├── docs/
│   ├── README.md
│   ├── ... normativní projektová dokumentace ...
│   └── decisions/
├── scripts/
│   └── check_governance.py      # nebo projektový ekvivalent
├── src/                         # pokud jde o softwarový produkt
├── tests/                       # podle technologie projektu
├── <provider-adapter files>     # např. CLAUDE.md, IDE/Codex instructions
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── workflows/
    └── pull_request_template.md
```

Konkrétní produkt může strukturu rozšířit, ale neměl by vytvářet paralelní místa se stejnou odpovědností.

## README.md

Je vstupním bodem pro člověka. Vysvětluje účel projektu, základní orientaci a odkazuje na kanonické zdroje. Může stručně shrnout pravidlo pro orientaci, ale nesmí se stát druhým kanonickým vlastníkem pravidla definovaného jinde.

## AGENTS.md

Je vstupním bodem pro agenta. Má být krátký a stabilní. Obsahuje:

- povinný startovací postup,
- stručná provozní připomenutí důležitých invariantů,
- odkazy na kanonické vlastníky detailních pravidel podle `docs/README.md`,
- instrukci, jak reagovat na konflikt nebo chybějící kontext,
- routing na durable handoff pravidla.

Shrnutí v `AGENTS.md` slouží pro routing a cold start; pokud detailní pravidlo vlastní jiný dokument, `AGENTS.md` jej nesmí nezávisle redefinovat.

## docs/

Obsahuje trvalé znalosti projektu. `docs/README.md` mapuje rodiny pravidel na jejich jednotlivé kanonické vlastníky.

Každý dokument má mít jasnou odpovědnost. Pokud dva dokumenty odpovídají na stejnou normativní otázku, jeden z nich musí být kanonický vlastník a druhý smí pouze odkázat nebo stručně shrnout jeho význam.

## docs/decisions/

Obsahuje významná přijatá rozhodnutí, jejich kontext a důvod. Rozhodovací záznam je auditní a historický artefakt: vysvětluje, proč aktuální stav vznikl, ale po propsání rozhodnutí nenahrazuje aktuální provozní specifikaci u kanonického vlastníka pravidla.

## GitHub Issues

Issues obsahují pracovní kontrakt, decision/blocker stav a task-local auditní stopu. Po dokončení issue musí všechna trvalá fakta, která vznikla, skončit na příslušném kanonickém místě v repozitáři.

Issue nesmí být jediným místem, kde je popsáno aktuální dlouhodobé chování produktu.

## Pull Requests a reviews

PR je implementační/execution handoff a návrh změny. Review/test threads jsou durable evidence kontrolních rolí. Přesné role artefaktů vlastní [`handoff-protocol.md`](handoff-protocol.md).

Po merge nesmí být nutné číst diskusi v PR, aby bylo možné pochopit současný produkt; trvalá specifikace musí být v kanonické dokumentaci/kódu.

## Provider/tool adapters

Nástrojově specifické soubory, například `CLAUDE.md`, IDE rules, Codex instrukce nebo workflow prompt, jsou adaptéry obecného modelu.

Musí být zřetelně podřízené kanonickým pravidlům v `docs/`. Smějí popsat konkrétní nástroje a příkazy, ale nesmějí:

- redefinovat role,
- měnit product authority,
- oslabit control gates,
- vytvořit druhý lifecycle,
- přidat providerovi širší oprávnění než má role.

Adapter by měl pokud možno začínat explicitním odkazem na obecné canonical workflow, které mapuje.

## Automation workflows

`.github/workflows/` nebo ekvivalent platformy obsahuje technickou realizaci automatizace. Workflow je mechanismus, ne zdroj governance autority.

Automatizační implementace se řídí [`automation-model.md`](automation-model.md) a má být navržena tak, aby:

- používala least privilege,
- rekonstruovala authoritative state,
- zanechávala durable success/failure,
- byla idempotentní nebo chráněná concurrency mechanismem,
- nepřeskakovala human decision gates.

## Governance checker

Projekt má mít automaticky spustitelnou kontrolu strukturálních governance invariantů, pokud je proces dostatečně stabilní na jejich strojovou validaci.

Checker může například ověřovat:

- přítomnost kanonických dokumentů a templates,
- konzistenci povinných status/concurrency/control-gate markerů,
- existenci provider-neutral workflow entrypointů,
- že CI skutečně governance checker spouští.

Checker nesmí předstírat, že umí rozhodnout produktovou semantiku, která vyžaduje lidský nebo analytický úsudek.

## Branching

Reference model nevyžaduje konkrétní názvy větví. Adoptující projekt musí durable určit branch authority a integrační cestu.

Minimálně musí být jasné:

- který stav/větev je autoritativní,
- odkud vzniká izolovaná práce,
- kam se navrhuje integrace,
- kdo provádí merge/promotion,
- jaké gates musí být splněné před integrací.

## Archivace

Historické dokumenty mohou existovat pouze pokud:

- mají jasný důvod zachování,
- jsou zřetelně označeny jako neautoritativní pro aktuální stav,
- nejsou v běžné kontextové cestě agenta,
- nehrozí jejich záměna za aktuální pravidla.

Historický nebo rozhodovací artefakt může být autoritativní jako záznam toho, co bylo v minulosti rozhodnuto, ale není tím automaticky autoritativní pro současné provozní pravidlo.
