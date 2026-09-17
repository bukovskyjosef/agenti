# Agenti — publikovaný referenční standard

`agenti` je **čistý publikovaný blueprint** pro nastavení agentního vývoje softwarového projektu. Není to pracovní repozitář pro vývoj samotného standardu.

Jeho účel je umožnit instrukci typu:

> Agente, přečti `bukovskyjosef/agenti` a připrav repozitář `<nové-repo>` přesně podle tohoto standardu.

## Status tohoto repozitáře

- `main` je jediný autoritativní publikovaný stav.
- Aktuální strom obsahuje pouze současný standard potřebný k jeho adopci.
- Issues, rozhodnutí, audity, experimenty, pracovní větve a review změn tohoto standardu patří do [`bukovskyjosef/agenti-lab`](https://github.com/bukovskyjosef/agenti-lab).
- Historické GitHub artefakty nebo Git historie nejsou součástí aktuálního standardu.
- Agent, který tento repozitář čte kvůli adopci, jej **nemá měnit**.

## Cílový delivery cyklus

```text
Human
  ↓
Asistentka — intake a Human queue
  ↓
Analyst — scope firewall
  ├─ decision needed → Asistentka ↔ Human → Analyst
  └─ Ready
        ↓
Developer
        ↓
PR + checks
        ↓
Independent Reviewer
  ├─ DEFECT → Developer corrective loop
  ├─ DECISION_REQUIRED → Asistentka ↔ Human
  └─ APPROVED
        ↓
Human release authorization, pokud ji projekt vyžaduje
        ↓
Integrator / automation
        ↓
production-authoritative boundary
        ↓
automatic deployment + post-release verification
        ↓
Done
```

Člověk je produktová a release autorita, ne ruční scheduler nebo message bus mezi agenty.

## Kde začít

Agent začíná v [`AGENTS.md`](AGENTS.md). Mapa standardu je v [`docs/README.md`](docs/README.md).

## Dokumenty

- [`docs/principles.md`](docs/principles.md) — základní invarianty a autorita,
- [`docs/roles.md`](docs/roles.md) — role a kompetence,
- [`docs/delivery-cycle.md`](docs/delivery-cycle.md) — end-to-end workflow a release model,
- [`docs/work-item.md`](docs/work-item.md) — pracovní kontrakt a Definition of Ready,
- [`docs/review.md`](docs/review.md) — nezávislé review a corrective loop,
- [`docs/automation.md`](docs/automation.md) — event-driven orchestrace a bezpečnost automatizace,
- [`docs/adoption.md`](docs/adoption.md) — jak standard zavést do nového nebo existujícího projektu.

## Co je projektově konfigurovatelné

Standard nevnucuje konkrétní AI provider, branch jména, deployment platformu ani univerzální testovací matici. Adoptující projekt musí tyto volby explicitně zaznamenat ve svém **Project Profile** podle `docs/adoption.md`.