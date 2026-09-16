# GitHub Issue standard

GitHub Issue je pracovní kontrakt konkrétního úkolu. Musí být dostatečně přesné, aby kompetentní agent mohl začít bez kontextu z externího chatu ve chvíli, kdy je označeno jako Ready.

## Lifecycle state

Jeden work item se průběžně vyvíjí ve stejném GitHub Issue. Jeho aktuální stav musí být v Issue explicitně uveden jako:

- **Intake** — požadavek je zachycený, ale nemusí ještě splňovat kompletní pracovní kontrakt; pro vznik Issue stačí jednoznačně zachytit alespoň Goal a nezbytný Context,
- **Analysis** — Issue se dopracovává, řeší se scope, nejasnosti, rozhodnutí, závislosti a podmínky dokončení,
- **Ready** — Issue splňuje kompletní pracovní kontrakt a Definition of Ready níže a může být předáno vykonávající roli.

Přechod do Ready je explicitní změna stavu téhož Issue, nikoli vznik nového Issue. Stav Ready nesmí být nastaven, pokud není splněná celá Definition of Ready. Za ověření této podmínky při přípravě/handoffu odpovídá role, která podle workflow připravuje nebo řídí Ready přechod; samotná Issue šablona není automatický validátor Ready stavu.

## Povinný obsah před Ready

Každé implementační nebo změnové Issue musí před označením jako Ready obsahovat:

### Goal
Jedna jasná formulace výsledku, kterého má být dosaženo.

### Context
Pouze kontext nezbytný k pochopení problému. Preferují se odkazy na kanonické dokumenty před kopírováním jejich obsahu.

### Scope
Explicitní seznam toho, co do úkolu patří.

### Out of scope
Explicitní hranice práce. Slouží proti oportunistickému rozšiřování změny.

### Requirements
Normativní požadavky, které musí řešení splnit. Pokud již existují jinde, Issue na ně odkazuje a neduplikuje je.

### Acceptance criteria
Pozorovatelné a testovatelné podmínky dokončení. Nemají popisovat preferovanou implementaci, pokud implementační způsob není součástí požadavku.

### Constraints
Technická, bezpečnostní, kompatibilitní nebo procesní omezení relevantní pro úkol. Pokud žádná zvláštní omezení nejsou, musí to Issue explicitně uvést.

### Dependencies
Závislosti, které musí být splněné, nebo explicitní konstatování, že žádné blokující závislosti nejsou.

### Canonical references
Konkrétní dokumenty, rozhodnutí, soubory nebo předchozí Issues, které jsou autoritativní pro tuto práci.

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
- neexistuje nevyřešená produktová otázka nutná k provedení práce,
- acceptance criteria jsou testovatelná,
- povinné části pracovního kontraktu relevantní pro daný typ práce jsou doplněné,
- jsou uvedené relevantní kanonické zdroje,
- závislosti jsou splněné nebo jasně deklarované,
- je známá odpovědná role,
- agent nepotřebuje neveřejný kontext z předchozí konverzace.

Readiness checklist v Issue šabloně je pouze provozní kontrola těchto podmínek; kanonickou definicí zůstává tento dokument.

Pokud některá podmínka neplatí, stav Issue nesmí být Ready. Issue zůstává v Intake nebo Analysis podle aktuální fáze.

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
- Nevkládej do Issue celý obsah dokumentace, pokud stačí odkaz.
- Nevynucuj implementační detail bez důvodu.
- Pokud existuje více produktově odlišných variant, Issue není Ready, dokud člověk variantu nevybere.
- Nález mimo scope se nestává součástí Issue jen proto, že je poblíž měněného kódu.
