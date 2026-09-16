# ADR-0001: Core principles of the agent system

**Status:** Accepted

## Context

Tento repozitář slouží jako referenční etalon pro způsob, jakým mají AI agenti pracovat v dalších projektech. Neobsahuje reálný aplikační produkt; produktem je samotný agentní systém, jeho governance, role, workflow a informační architektura.

## Decision

Přijímají se následující základní principy:

1. GitHub prostor projektu je jediným zdrojem pravdy.
2. Nový agent musí být schopen začít práci bez neveřejného kontextu mimo repozitář a související Issues/PRs.
3. Úkoly se evidují v GitHub Issues.
4. Každý agent vstupuje do práce v explicitní roli.
5. Agenti se vzájemně kontrolují, ale nekonkurují si a nepřekračují kompetence své role.
6. Agent nesmí oportunisticky opravovat věci mimo své oprávnění a scope.
7. Produktová rozhodnutí dělá člověk.
8. Minimální sada rolí je orchestrátor, analytik, vývojář, tester a reviewer.
9. Informace mají jedno kanonické místo a průběžně se aktualizují spolu se změnou produktu.
10. Při definici problému se scope připravuje dostatečně detailně, aby následná realizace nevznikala z domněnek.
11. Kontext se načítá cíleně a agent má spotřebovávat nejmenší množství tokenů slučitelné se správným provedením práce.
12. Tento repozitář má být použitelný jako vzor a návod pro další projekty.

## Consequences

- Chat může sloužit k práci a diskusi, ale nesmí být jediným nositelem trvalé informace.
- Governance dokumentace musí být sama udržována jako produkt.
- Role musí mít explicitní hranice pravomocí.
- Issue musí fungovat jako samostatný pracovní kontrakt.
- Repo musí podporovat nezávislý handoff mezi agentními instancemi.
- Duplicitní normativní informace jsou považované za strukturální problém.
