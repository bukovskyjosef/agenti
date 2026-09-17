# Consumer agent entrypoint

Tento repozitář je **read-only referenční standard**. Pokud jsi sem byl poslán kvůli bootstrapu nebo adopci agentního workflow, čti jej jako specifikaci a změny prováděj v cílovém projektu, nikoli zde.

## Když máš připravit nový nebo existující projekt

1. Přečti [`docs/README.md`](docs/README.md).
2. Přečti celý standard v pořadí doporučeném mapou dokumentace.
3. Načti cílový repozitář a jeho existující produktové/governance zdroje.
4. Podle [`docs/adoption.md`](docs/adoption.md) vytvoř projektový **Project Profile** a lokální agentní dokumentaci.
5. Nevymýšlej projektové volby, které nejsou z cílového repozitáře zřejmé. Pokud jsou nutné, připrav Human decision gate.
6. Zachovej existující produktová pravidla a nepřepisuj je generickým etalonem.
7. Výsledný projekt musí být po bootstrapu cold-startable bez nutnosti znovu číst tento repozitář nebo soukromý chat.

## Absolutní invarianty adopce

- GitHub/repozitář cílového projektu je durable source of truth.
- Human/Product Owner rozhoduje produktové, governance a explicitně vyhrazené release otázky.
- Analyst minimalizuje scope a nesmí nahrazovat nejasnost předpokladem.
- Agent nesmí opravovat věci mimo scope jen proto, že si jich všiml.
- Autor změny nesmí být její nezávislý Reviewer.
- Review severity sama nevytváří oprávnění k novému scope.
- Automatizační trigger není autorita; agent před akcí rekonstruuje aktuální durable stav.
- Human release authorization, pokud je vyžadována, se váže na konkrétní release candidate a nesmí schvalovat jiný artefakt.
- Production-affecting práce není Done před požadovaným deploymentem a post-release verification.

## Tento repozitář neměň

Pokud zjistíš problém nebo navrhneš změnu **tohoto standardu**, nevytvářej zde Issue ani branch. Práce nad standardem patří do `bukovskyjosef/agenti-lab`.

## Kontextová disciplína

Při práci v cílovém projektu načítej minimum **úplného** kontextu potřebného pro roli a work item. Nekopíruj celý standard do každého Issue; projektová agentní dokumentace má obsahovat trvalá pravidla a Issue pouze task-specific kontrakt.