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

## Completion semantics

Dokončení se určuje podle **typu výsledku práce**, nikoli jednotným pravidlem pro všechna Issues. Jedno Issue může kombinovat více typů výsledku; v takovém případě musí splnit podmínky všech relevantních typů.

### Společné podmínky dokončení

Každé dokončené Issue musí mít:

- splněný cíl a relevantní acceptance criteria,
- provedené ověření předepsané pracovním kontraktem,
- změny uvnitř schváleného scope,
- relevantní kanonickou dokumentaci v souladu s výsledným stavem,
- nesouvisející nové nálezy odděleně zaznamenané,
- dostatečný důkaz o výsledku a handoff pro další roli.

### Implementace nebo změna produktu / normativního stavu

Pokud výsledkem práce je změna kódu, konfigurace, dat, šablon nebo kanonické normativní dokumentace:

- musí být splněné všechny kontrolní brány předepsané pro daný work item,
- autor změny nesmí být jejím nezávislým reviewerem,
- blocking nálezy z požadovaných kontrol musí být vyřešené před dokončením.

Konkrétní pravidlo pro výběr review/testovacích bran je samostatná governance otázka; dokud není kanonicky určeno, work item musí požadované brány deklarovat explicitně.

### Analýza

Analytické Issue je dokončené, pokud je hotový jeho analytický výstup, jsou splněná jeho acceptance criteria, nejasnosti jsou buď vyřešené, nebo explicitně eskalované správnému rozhodovateli, a další práce je předaná přes GitHub artefakty. Samotná skutečnost, že jde o Issue, nevytváří další povinné nezávislé review.

### Review nebo audit

Review/audit Issue je dokončené podle pravidel [`review-model.md`](review-model.md): reviewer zaznamenal závěr a důkazy, blocking nálezy jsou vypořádané způsobem vyžadovaným daným review a follow-up práce je evidovaná tam, kde je potřeba.

Review nebo audit **nevyžaduje další review pouze proto, že jeho výsledkem je review**. Další nezávislá kontrola se provádí jen tehdy, pokud ji výslovně požaduje pracovní kontrakt nebo jiné platné pravidlo.

### Testování nebo verifikace

Testovací/verifikační Issue je dokončené, pokud bylo provedeno předepsané ověření, existují doložitelné výsledky a nalezené defekty nebo blokace byly předány správné roli. Další review testu není automaticky vyžadováno, pokud není explicitně předepsané.

### Orchestrace a handoff

Orchestrační Issue je dokončené, pokud byly provedeny jeho routingové, závislostní a handoff povinnosti, stav je zachycen v GitHubu a navazující práce má jednoznačné vlastníky nebo blokace. Samotná orchestrace automaticky nevyžaduje další nezávislé review.

### Rozhodovací liaison / Asistentka

Pokud je výsledkem pouze zpracování rozhodovací fronty a záznam lidského rozhodnutí, práce končí po úplném záznamu a handoffu. Pokud Asistentka přímo mění kanonický normativní artefakt, tato část práce je současně **změnovým** výsledkem a vztahují se na ni i podmínky pro implementaci nebo změnu.

## Procesní výjimky

Bootstrap nebo jiná odchylka od běžného procesu nesmí být dovozena zpětně. Musí být explicitně zaznamenaná v příslušném Issue nebo decision artefaktu, včetně:

- které běžné pravidlo nebo kontrolní brána se nepoužije,
- proč je výjimka nutná,
- kdo ji schválil, pokud zasahuje do product/governance pravidel.

Výjimka platí pouze pro uvedený případ a nevytváří nový obecný precedent.

## Pravidla kvality zadání

- Nepoužívej vágní formulace typu „oprav“, „dolaď“, „udělej správně“ bez definice výsledku.
- Nevkládej do issue celý obsah dokumentace, pokud stačí odkaz.
- Nevynucuj implementační detail bez důvodu.
- Pokud existuje více produktově odlišných variant, issue není Ready, dokud člověk variantu nevybere.
- Nález mimo scope se nestává součástí issue jen proto, že je poblíž měněného kódu.
