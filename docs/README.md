# Mapa referenčního standardu

Každá rodina pravidel má jedno kanonické místo. Dokumenty se navzájem odkazují, ale nemají vytvářet konkurenční definice stejné otázky.

| Oblast | Kanonický dokument |
|---|---|
| autorita, source of truth, scope a obecné invarianty | [`principles.md`](principles.md) |
| role a jejich kompetence | [`roles.md`](roles.md) |
| end-to-end delivery, Human gates, integrace a release | [`delivery-cycle.md`](delivery-cycle.md) |
| Issue/work-item kontrakt, lifecycle, Ready a concurrency | [`work-item.md`](work-item.md) |
| nezávislé review, finding authority a corrective loop | [`review.md`](review.md) |
| automatické spouštění rolí, eventy, least privilege a durable failure | [`automation.md`](automation.md) |
| zavedení standardu do konkrétního repozitáře a Project Profile | [`adoption.md`](adoption.md) |

## Doporučené pořadí pro bootstrap

1. `principles.md`
2. `roles.md`
3. `delivery-cycle.md`
4. `work-item.md`
5. `review.md`
6. `automation.md`
7. `adoption.md`

## Co zde záměrně není

Tento publikovaný standard neobsahuje:

- historii rozhodnutí,
- auditní reporty,
- experimenty a rejected variants,
- Issues nebo PR kontrakty vývoje samotného etalonu,
- provider-specific implementaci,
- projektově konkrétní branch/deploy konfiguraci.

Tyto věci patří buď do `agenti-lab`, nebo do adoptujícího projektu.