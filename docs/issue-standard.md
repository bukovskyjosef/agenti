# GitHub Issue standard

GitHub Issue je pracovní kontrakt konkrétního úkolu. Musí být dostatečně přesné, aby kompetentní agent mohl začít bez kontextu z externího chatu ve chvíli, kdy je označeno jako Ready.

## Lifecycle state

Jeden work item se průběžně vyvíjí ve stejném GitHub Issue. Jeho aktuální stav musí být explicitně uveden. Referenční lifecycle používá tyto stavy:

- **Intake** — požadavek je zachycený, ale nemusí ještě splňovat kompletní pracovní kontrakt,
- **Analysis** — Issue se dopracovává, řeší se scope, nejasnosti, rozhodnutí, dependencies a podmínky dokončení,
- **Blocked** — další autorizovaný krok nelze provést; Issue musí uvést důvod, evidence, potřebnou autoritu/roli a stav, do kterého se má po odblokování vrátit,
- **Ready** — Issue splňuje kompletní pracovní kontrakt a Definition of Ready a může být předáno vykonávající roli,
- **In Progress** — autorizovaná vykonávající role práci aktivně provádí,
- **In Review** — probíhá předepsaná nezávislá kontrola nebo testování,
- **Changes Required** — existuje autorizovaný corrective loop pro defect v rámci současného kontraktu,
- **Approved** — všechny required control gates jsou splněné a práce je připravená k integraci/uzavření podle svého typu,
- **Done** — typově specifické completion podmínky jsou splněné; pokud změnová práce vyžaduje integraci, výsledek je již skutečně integrovaný.

Ne každý typ práce musí použít všechny stavy. Například samostatná analýza nebo audit mohou po dokončení svého terminal deliverable přejít do Done bez integračního kroku. Workflow sekvenci vlastní [`workflow.md`](workflow.md).

Přechod do Ready je explicitní změna stavu téhož Issue, nikoli vznik nového Issue. Samotná existence Issue ani odeslání šablony Ready stav nevytváří.

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

### Required control gates
Kontrolní brány, které musí proběhnout před dokončením work itemu. Volba musí být explicitní.

### Validation
Jakým způsobem má být výsledek ověřen.

### Documentation impact
Které kanonické dokumenty se musí změnit nebo explicitní konstatování, že změna dokumentace není potřeba.

### Concurrency class
Každý Ready work item musí být zařazen do jedné z těchto tříd:

- **PARALLEL_SAFE** — může běžet souběžně s jinými tasky bez očekávaného konfliktu shared contract/surface,
- **COORDINATION_REQUIRED** — souběh je možný pouze s explicitním ownershipem, sequencingem, merge pořadím nebo stabilním společným kontraktem,
- **EXCLUSIVE** — souběžné změny na dotčeném povrchu jsou nepřijatelné nebo by byly neúměrně rizikové/drahé na reconciliaci.

Klasifikace neslouží k hodnocení důležitosti; řídí bezpečný paralelismus.

### Shared surfaces / coordination rule
Issue pojmenuje sdílené povrchy, které mohou kolidovat, například:

- database/schema/migrations,
- API/domain contracts,
- auth/security policy,
- governance a templates,
- dependency/runtime konfigurace,
- stejné moduly nebo generated artifacts.

U `PARALLEL_SAFE` může být explicitně uvedeno `None`. U `COORDINATION_REQUIRED` nebo `EXCLUSIVE` musí Issue uvést pravidlo ownershipu, pořadí nebo blokace.

### Decision gates
Issue musí uvést nevyřešené decision gates nebo explicitně `None`.

Ready work item nesmí mít nevyřešený decision gate, jehož výsledek je nutný pro vykonání autorizovaného scope. Decision gate se nesmí „vyřešit“ předpokladem implementujícího agenta.

## Definition of Ready

Issue je Ready pouze pokud současně platí:

- cíl je jednoznačný,
- scope a out-of-scope jsou jasné,
- neexistuje nevyřešená produktová/governance otázka nutná k provedení práce,
- acceptance criteria jsou testovatelná,
- povinné části pracovního kontraktu relevantní pro daný typ práce jsou doplněné,
- jsou uvedené relevantní kanonické zdroje,
- dependencies jsou splněné nebo jasně deklarované,
- je známá odpovědná role,
- požadované control gates jsou explicitně deklarované,
- concurrency class je uvedená,
- shared surfaces a coordination rule jsou popsané nebo explicitně `None`,
- decision gates jsou vyřešené nebo explicitně `None`,
- agent nepotřebuje neveřejný kontext z předchozí konverzace.

Readiness checklist v Issue šabloně je pouze provozní kontrola těchto podmínek; kanonickou definicí zůstává tento dokument.

Pokud některá podmínka neplatí, stav Issue nesmí být Ready. Issue zůstává v Intake/Analysis nebo přejde do Blocked podle důvodu.

## Control gate selection

Reference model nepoužívá univerzální risk skóre ani pevnou doménovou tabulku změn. Požadované control gates se určují během Analysis/Ready přípravy pro konkrétní work item a jsou součástí jeho pracovního kontraktu.

Platí minimální invarianty:

- každý Ready work item explicitně uvádí své `Required control gates`,
- každá implementace nebo změna kódu, konfigurace, dat, šablon nebo kanonické normativní dokumentace vyžaduje alespoň **Independent Review**,
- samostatné **Test / Verification** není univerzálně povinné; pokud je požadováno, musí být uvedeno v kontraktu,
- pokud má jedna nezávislá kontrolní instance spojit Reviewer a Tester/Verification funkci, musí to work item explicitně povolit; autor změny touto nezávislou kontrolní instancí být nesmí,
- u analytické, review/auditní, testovací, orchestrační nebo čistě rozhodovací práce mohou být control gates `None`, pokud její typově specifická completion pravidla další bránu nevyžadují,
- control gate nesmí být po přechodu do Ready vypuštěna jen kvůli rychlosti; změna gate kontraktu vyžaduje explicitní aktualizaci Issue a návrat do odpovídající fáze.

Adoptující repozitář smí definovat přísnější projektové defaulty nebo povinné testovací brány.

## Post-Ready status transitions

Po Ready se stav mění pouze podle durable evidence:

- `Ready → In Progress` při převzetí autorizovanou vykonávající rolí,
- `In Progress → In Review` po durable implementačním/execution handoffu, pokud jsou control gates požadované,
- `In Review → Changes Required` při unresolved `DEFECT`, který vyžaduje opravu současného kontraktu,
- `Changes Required → In Review` po corrective změně a předepsaném ověření,
- `In Review → Approved` po splnění všech požadovaných gate podmínek,
- `Approved → Done` po integračním/terminal kroku relevantním pro daný typ práce,
- kterákoli neterminální fáze může přejít do `Blocked`, pokud další krok není autorizovaně/prokazatelně možný.

Automation může tyto přechody provést pouze podle [`automation-model.md`](automation-model.md); trigger sám o sobě není evidence.

## Completion semantics

Dokončení se určuje podle **typu výsledku práce**, nikoli jednotným pravidlem pro všechna Issues. Jedno Issue může kombinovat více typů výsledku; v takovém případě musí splnit podmínky všech relevantních typů.

### Společné podmínky dokončení

Každé dokončené Issue musí mít:

- splněný cíl a relevantní acceptance criteria,
- provedené ověření předepsané pracovním kontraktem,
- změny uvnitř schváleného scope,
- relevantní kanonickou dokumentaci v souladu s výsledným stavem,
- nesouvisející nové nálezy odděleně zaznamenané,
- durable evidence a handoff podle [`handoff-protocol.md`](handoff-protocol.md).

### Implementace nebo změna produktu / normativního stavu

Pokud výsledkem práce je změna kódu, konfigurace, dat, šablon nebo kanonické normativní dokumentace:

- musí být splněné všechny control gates předepsané pro daný work item,
- autor změny nesmí být jejím nezávislým reviewerem,
- blocking `DEFECT` findings musí být vyřešené,
- required decision gates musí být vyřešené,
- pokud projekt pro daný typ změny vyžaduje merge/promotion/integration, Done nastává až po tomto kroku a jeho durable evidenci.

### Analýza

Analytické Issue je dokončené, pokud je hotový jeho analytický výstup, jsou splněná acceptance criteria, nejasnosti jsou vyřešené nebo explicitně eskalované správnému rozhodovateli a další práce je durable předaná. Samotná skutečnost, že jde o Issue, nevytváří další povinné review.

### Review nebo audit

Review/audit Issue je dokončené podle [`review-model.md`](review-model.md). Review nebo audit nevyžaduje další review pouze proto, že jeho výsledkem je review.

### Testování nebo verifikace

Testovací/verifikační Issue je dokončené, pokud bylo provedeno předepsané ověření, existují doložitelné výsledky a nalezené defekty/blokace byly durable předány správné roli.

### Orchestrace a handoff

Orchestrační Issue je dokončené, pokud byly provedeny jeho routingové, dependency, concurrency a handoff povinnosti, stav je zachycen v GitHubu a navazující práce má jednoznačný další krok nebo durable blocker.

### Rozhodovací liaison / Asistentka

Pokud je výsledkem pouze zpracování decision queue a záznam lidského rozhodnutí, práce končí po úplném durable záznamu a handoffu. Pokud Asistentka přímo mění kanonický normativní artefakt, tato část je současně změnovým výsledkem.

### Integrace

Integrační work item je dokončený, pokud byly ověřené všechny předepsané gates pro přesný integrovaný artefakt, proběhl autorizovaný merge/promotion a výsledek je durable zaznamenaný. Integrátor nesmí completion odvodit pouze z chatového souhlasu.

## Procesní výjimky

Bootstrap nebo jiná odchylka od běžného procesu nesmí být dovozena zpětně. Musí být explicitně zaznamenaná v příslušném Issue nebo decision artefaktu, včetně:

- které běžné pravidlo nebo control gate se nepoužije,
- proč je výjimka nutná,
- kdo ji schválil, pokud zasahuje do product/governance pravidel.

Výjimka platí pouze pro uvedený případ a nevytváří nový obecný precedent.

## Pravidla kvality zadání

- Nepoužívej vágní formulace typu „oprav“, „dolaď“, „udělej správně“ bez definice výsledku.
- Nevkládej do Issue celý obsah dokumentace, pokud stačí odkaz.
- Nevynucuj implementační detail bez důvodu.
- Pokud existuje více produktově odlišných variant, Issue není Ready, dokud člověk variantu nevybere.
- Nález mimo scope se nestává součástí Issue jen proto, že je poblíž měněného kódu.
- Review recommendation se nestává novým scope, dokud není explicitně povýšena do autorizovaného work contractu.
