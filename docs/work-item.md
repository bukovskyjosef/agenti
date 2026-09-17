# Work item contract

GitHub Issue je task-local pracovní kontrakt. Stejné Issue typicky dozrává z Intake přes Analysis do Ready; nevytváří se nový Issue pouze kvůli změně fáze.

## Povinný obsah před Ready

Implementační nebo změnový work item musí obsahovat:

### Goal
Jedna jednoznačná formulace výsledku.

### Context
Pouze kontext nutný pro pochopení problému; trvalá pravidla se odkazují z kanonických dokumentů.

### Scope
Co přesně do úkolu patří.

### Out of scope
Explicitní hranice proti scope creep.

### Requirements
Normativní požadavky, které musí řešení splnit.

### Acceptance criteria
Pozorovatelné a testovatelné podmínky dokončení.

### Constraints
Relevantní technická, kompatibilitní, bezpečnostní nebo procesní omezení.

### Dependencies
Blokující nebo pořadové závislosti; případně explicitně `None`.

### Canonical references
Autoritativní dokumenty, rozhodnutí a kontrakty relevantní pro práci.

### Responsible role
Role aktuální executable fáze.

### Required control gates
Např. Independent Review, Review + Verification nebo projektově definovaná brána.

Minimální invariant: změna kódu, konfigurace, dat, šablon nebo kanonické dokumentace vyžaduje nezávislé Review. Samostatný Tester není univerzálně povinný.

### Validation
Jak má být výsledek ověřen.

### Documentation impact
Co se musí změnit v durable dokumentaci nebo proč nic.

### Concurrency class

- `PARALLEL_SAFE` — bez očekávaného konfliktu shared surface,
- `COORDINATION_REQUIRED` — souběh vyžaduje ownership/sequencing/merge rule,
- `EXCLUSIVE` — souběžná změna na dotčeném povrchu je nepřijatelná.

### Shared surfaces / coordination rule
Schema, API, domain contract, auth, governance, dependencies, stejné moduly apod.; nebo `None`.

### Decision gates
Nevyřešené otázky nutné k realizaci; nebo `None`.

### Release policy
Odkaz na Project Profile a případná task-specific odchylka: zda kandidát vyžaduje Human release authorization a pro jaký target.

## Definition of Ready

Work item je Ready pouze pokud:

- Goal je jednoznačný,
- Scope a Out of scope jsou jasné,
- neexistuje required unresolved decision gate,
- acceptance criteria jsou testovatelná,
- dependencies a constraints jsou známé,
- canonical references jsou uvedené,
- responsible role je známá,
- required control gates jsou explicitní,
- concurrency/shared surfaces jsou deklarované,
- release policy je určitelná,
- kompetentní nová instance může začít pouze z repo/GitHub stavu.

Analyst nesmí označit Issue Ready jen proto, že existuje nebo obsahuje vyplněnou šablonu.

## Handoff destinations

- Analyst/Asistentka aktualizují work contract v Issue a decision comments/artefaktech projektu.
- Developer předává implementaci přes PR + commit(s).
- Reviewer zapisuje durable PR review/comment.
- Tester zapisuje result proti přesnému testovanému headu.
- Integrator zapisuje integrated/released candidate a target evidence.

Soukromý chatový kontext není handoff.