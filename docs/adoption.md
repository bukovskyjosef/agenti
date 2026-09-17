# Adoption guide

Cílem adopce je vytvořit v cílovém projektu **samostatný a cold-startable agentní systém** podle tohoto standardu. Běžný agent v cílovém projektu nemá potřebovat znovu číst `agenti`.

## 1. Nejprve audituj cílový repozitář

Než něco vytvoříš:

- najdi existující README/AGENTS/governance,
- identifikuj business/domain/API/data dokumenty,
- zjisti branch a release model,
- zjisti CI/CD, environments a deployment platformu,
- najdi existující Issues/PR conventions,
- odstraň nebo explicitně vyřeš konkurenční zdroje pravdy místo jejich slepého duplikování.

## 2. Vytvoř Project Profile

Project Profile je projektově konkrétní instancí tohoto standardu. Musí určit alespoň:

```text
Repository / source of truth:
Canonical documentation map:
Human / Product Owner:
Production-authoritative boundary:
Task branch policy:
PR target policy:
Required default control gates:
Human release authorization policy:
Deployment trigger:
Environments:
Post-release verification minimum:
Retry / rollback / recovery authority:
Agent/provider/runner mapping:
Concurrency / shared-surface conventions:
Target-drift policy after release approval:
```

Pokud některá nutná volba není z projektu zřejmá, nevymýšlej ji — vytvoř Human decision gate.

## 3. Doporučená lokální struktura cílového projektu

Přizpůsob názvy existujícím conventions, ale zachovej odpovědnosti:

```text
/
├── README.md
├── AGENTS.md
├── docs/
│   ├── agent/
│   │   ├── README.md              # mapa agentních pravidel
│   │   ├── PROJECT_PROFILE.md
│   │   ├── ROLES.md
│   │   ├── WORKFLOW.md
│   │   ├── ISSUE_STANDARD.md
│   │   ├── REVIEW.md
│   │   └── AUTOMATION.md
│   └── ... produktová/domain dokumentace ...
└── .github/
    ├── ISSUE_TEMPLATE/
    ├── pull_request_template.md
    └── workflows/
```

Nevytvářej soubor jen proto, že je v příkladu. Pokud existující kanonický dokument už odpovědnost bezpečně vlastní, odkaž na něj a neduplikuj jej.

## 4. AGENTS.md cílového projektu

Má být krátký router, ne druhá specifikace. Musí agentovi říct:

1. přečti své Issue,
2. urč svou roli,
3. načti relevantní canonical docs podle mapy,
4. ověř lifecycle/Ready/dependencies/concurrency,
5. při decision gate zastav a eskaluj přes Asistentku/Human flow,
6. pracuj jen v scope,
7. před dokončením zanech durable handoff.

## 5. GitHub work contract

V cílovém projektu vytvoř Issue template/form odpovídající `work-item.md` a PR template podporující:

- linked Issue,
- implementovaný scope + intentionally out of scope,
- acceptance criteria evidence,
- validation/checks,
- shared-contract impact,
- decision gates,
- exact candidate/head SHA pro review/release,
- durable Reviewer/Tester/Integrator handoff.

Template je provozní pomůcka; kanonický význam polí vlastní projektová dokumentace.

## 6. Branch a integration policy

Pro malý projekt preferuj nejjednodušší bezpečný model, často:

```text
production-authoritative main
↑
PR
↑
task branch
```

Nepřidávej `develop`, release train nebo environment matrix bez konkrétní potřeby.

Chraň production-authoritative boundary tak, aby ji nebylo možné běžně měnit mimo definované gates.

## 7. Release policy

Project Profile musí říct, zda Human release authorization platí:

- pro každou production změnu,
- pouze pro určité risk/work classes,
- pouze pro vybraná environments,
- nebo není požadována.

Pokud je požadována, implementuj exact-candidate binding a stale semantics z `delivery-cycle.md`.

## 8. Automatizuj postupně

Doporučené pořadí:

1. přesný Issue/work contract,
2. durable Developer → Reviewer handoff,
3. CI/checks,
4. automatický Analyst/Developer/Reviewer routing,
5. Human decision queue přes Asistentku,
6. Human release queue,
7. automatic integration/deployment + verification.

Vyšší autonomie se zapíná až tehdy, když nižší vrstva zachovává scope, authority a durable state.

## 9. Bootstrap validation

Projekt je připravený, pokud nová agentní instance dostane například pouze:

> Jsi Reviewer. Pracuj na Issue #N. Řiď se repozitářem.

…a dokáže bez externího chatu zjistit relevantní kontrakt, role boundaries, evidence, next action a místo durable handoffu.

Pokročilý test: běžný work item projde od Human intake přes Analysis, Developer, Review a release až do produkce bez ručního přeposílání agentních reportů člověkem; Human vstupuje pouze na skutečné decision/release gates.