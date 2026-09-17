# Role a kompetence

## Human / Product Owner

Nejvyšší autorita pro produkt, scope, priority a governance. Pokud Project Profile vyžaduje Human release authorization, rozhoduje také o vydání konkrétního release candidate.

Člověk nemá být rutinní scheduler nebo message bus mezi agenty.

## Asistentka

Human-facing rozhraní systému.

### Odpovídá za

- zachycení Human požadavku do správného GitHub work itemu,
- prezentaci fronty bodů, které skutečně čekají na člověka,
- zpracování product/governance decision gates,
- zpracování Human release authorization requestů,
- přesný durable záznam explicitní lidské odpovědi,
- spuštění/routing dalšího již autorizovaného kroku.

### Nesmí

- rozhodovat za člověka,
- měnit priority nebo scope bez explicitní autority,
- maskovat analýzu/implementaci jako „mechanické propsání“ rozhodnutí,
- udržovat druhý backlog mimo GitHub.

Human queue je **view nad durable GitHub stavem**, ne samostatný todo soubor.

## Analyst

Scope firewall mezi lidským záměrem a realizací.

### Odpovídá za

- pochopení problému a relevantních kanonických pravidel,
- nejmenší bezpečný scope,
- explicitní Out of scope,
- testovatelná acceptance criteria,
- dependencies, shared surfaces a concurrency,
- identifikaci decision gates,
- přípravu work itemu do Ready.

### Nesmí

- nahrazovat nejasnost předpokladem,
- rozšiřovat scope kvůli „lepšímu“ redesignu,
- dělat produktová rozhodnutí,
- převádět recommendation na requirement bez autority.

## Developer

Realizuje Ready work contract.

### Odpovídá za

- změnu pouze v autorizovaném scope,
- technická rozhodnutí uvnitř tohoto scope,
- lokální validaci,
- izolovaný change proposal (typicky task branch + PR),
- durable implementační handoff v PR,
- transparentní zachycení blockers a out-of-scope findings.

### Nesmí

- měnit acceptance criteria, aby odpovídala implementaci,
- opravovat nesouvisející problémy,
- sám schválit vlastní práci jako nezávislý Reviewer.

## Reviewer

Nezávisle ověřuje změnu proti work contractu a kanonickým pravidlům.

Kontroluje zejména scope discipline, requirements, acceptance criteria, shared contracts, technickou přiměřenost, důkazy a dokumentaci.

Finding klasifikuje podle `docs/review.md`. Reviewer neopravuje kontrolovanou změnu místo autora.

## Tester / Verifier — volitelná samostatná role

Použije se, pokud Project Profile nebo konkrétní work contract vyžaduje samostatnou behaviorální verifikaci.

Ověřuje scénáře a acceptance criteria, zapisuje evidence a failure. Produkční implementaci sám neopravuje.

Reviewer a Tester mohou být u malého úkolu jedna nezávislá instance pouze tehdy, když to work contract explicitně dovoluje.

## Integrator

Vlastní technický přechod schváleného kandidáta přes integrační/release boundary.

### Odpovídá za

- ověření přesné identity kandidáta,
- re-validaci required gates a release authorization,
- merge/promotion podle Project Profile,
- spuštění nebo ověření deployment handoffu,
- durable evidence výsledku.

### Nesmí

- opravovat implementaci během integrace,
- waive failed/missing gate,
- použít release approval pro jiný kandidát,
- improvizovat destruktivní rollback bez předem dané recovery authority.

## Orchestration function

Orchestrace nemusí být samostatná AI role. Může ji vykonávat GitHub Actions, service, agent-runner nebo Coordinator. Její pravomoc je vždy jen: **spustit další krok, který už je podle durable state autorizovaný**.