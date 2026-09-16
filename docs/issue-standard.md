# GitHub Issue standard

GitHub Issue je pracovní kontrakt konkrétního úkolu. Musí být dostatečně přesné, aby kompetentní agent mohl začít bez kontextu z externího chatu.

## Povinný obsah

Každé implementační nebo změnové issue musí obsahovat:

### Goal
Jedna jasná formulace výsledku, kterého má být dosaženo.

### Context
Pouze kontext nezbytný k pochopení problému. Preferují se odkazy na kanonické dokumenty před kopírováním jejich obsahu.

### Scope
Explicitní seznam toho, co do úkolu patří.

### Out of scope
Explicitní hranice práce. Slouží proti oportunistickému rozšiřování změny.

### Requirements
Normativní požadavky, které musí řešení splnit. Pokud již existují jinde, issue na ně odkazuje a neduplikuje je.

### Acceptance criteria
Pozorovatelné a testovatelné podmínky dokončení. Nemají popisovat preferovanou implementaci, pokud implementační způsob není součástí požadavku.

### Constraints
Technická, bezpečnostní, kompatibilitní nebo procesní omezení relevantní pro úkol.

### Canonical references
Konkrétní dokumenty, rozhodnutí, soubory nebo předchozí issues, které jsou autoritativní pro tuto práci.

### Responsible role
Role, která má provést aktuální fázi práce.

### Validation
Jakým způsobem má být výsledek ověřen.

### Documentation impact
Které kanonické dokumenty se musí změnit nebo explicitní konstatování, že změna dokumentace není potřeba.

## Definition of Ready

Issue je Ready pouze pokud současně platí:

- cíl je jednoznačný,
- scope a out-of-scope jsou jasné,
- neexistuje nevyřešená produktová otázka nutná k implementaci,
- acceptance criteria jsou testovatelná,
- jsou uvedené relevantní kanonické zdroje,
- závislosti jsou splněné nebo jasně deklarované,
- je známá odpovědná role,
- agent nepotřebuje neveřejný kontext z předchozí konverzace.

Pokud některá podmínka neplatí, agent nemá nejasnost hádat. Issue se vrací do analýzy.

## Definition of Done

Issue je Done pouze pokud:

- změna splňuje acceptance criteria,
- bylo provedeno předepsané ověření,
- nezávislé review je uzavřené,
- případné požadované testování je úspěšné,
- relevantní dokumentace odpovídá novému stavu,
- všechny změny jsou uvnitř scope nebo mají explicitní schválení,
- nové nesouvisející nálezy jsou odděleně evidované,
- issue nebo PR obsahuje dostatečný důkaz o dokončení.

## Pravidla kvality zadání

- Nepoužívej vágní formulace typu „oprav“, „dolaď“, „udělej správně“ bez definice výsledku.
- Nevkládej do issue celý obsah dokumentace, pokud stačí odkaz.
- Nevynucuj implementační detail bez důvodu.
- Pokud existuje více produktově odlišných variant, issue není Ready, dokud člověk variantu nevybere.
- Nález mimo scope se nestává součástí issue jen proto, že je poblíž měněného kódu.
