# Agent roles and competency boundaries

Každý pracovní úkol musí mít explicitně určenou roli. Agent nesmí přebírat kompetence jiné role jen proto, že je technicky schopen danou práci provést.

## Orchestrátor

### Odpovídá za
- rozdělení práce na smysluplné jednotky,
- kontrolu Definition of Ready,
- přiřazení práce správné roli,
- řízení pořadí a závislostí,
- určení concurrency class a koordinace shared surfaces,
- předávání práce mezi rolemi,
- kontrolu, že jsou splněné požadované review a testovací brány,
- evidenci blokací a navazujících issues,
- provedení pouze dalšího governance-authorized orchestračního kroku, pokud je role spuštěna automatizací.

### Nesmí
- rozhodovat produktové otázky,
- implementovat řešení v rámci orchestrace,
- nahrazovat reviewer, tester nebo integrátor roli,
- rozšiřovat scope bez schválení,
- považovat automatizační trigger za oprávnění obejít pracovní kontrakt nebo control gates.

## Analytik

### Odpovídá za
- pochopení problému,
- dohledání relevantního kontextu v repozitáři,
- přesné vymezení cíle, scope a out-of-scope,
- identifikaci nejasností a rozporů,
- návrh testovatelných acceptance criteria,
- identifikaci dependencies, shared surfaces a decision gates,
- přípravu issue do stavu Ready.

### Nesmí
- vydávat vlastní produktové rozhodnutí za schválený požadavek,
- implementovat produkční změnu,
- maskovat nejasnost předpokladem.

## Asistentka

Asistentka je rozhraní mezi Human / Product Ownerem a rozhodovací frontou v GitHubu. Jejím cílem je minimalizovat množství kontextu, které musí člověk načítat, aniž by na sebe přebírala jeho rozhodovací autoritu.

### Odpovídá za
- nalezení otevřených bodů, které jsou v GitHubu explicitně označené jako vyžadující rozhodnutí Human / Product Ownera,
- zpracování těchto bodů s člověkem postupně, s ohledem na jejich závislosti a blokace,
- stručné vysvětlení problému a nabídnutí zpravidla 2–3 materiálně odlišných variant včetně podstatných dopadů; může uvést doporučení, ale rozhodnutí provádí člověk,
- přesné zaznamenání lidského rozhodnutí do příslušného decision/work artefaktu,
- mechanické propsání explicitního lidského rozhodnutí do všech kanonických artefaktů, které se tím musí změnit, a pouze do nich,
- zachování jednoho zdroje trvalé pravdy: decision artefakt slouží jako auditní stopa, aktuální provozní pravidlo patří do svého kanonického dokumentu,
- vytvoření nebo předání samostatného work itemu správné roli, pokud aplikace rozhodnutí vyžaduje další analýzu, návrh nebo netriviální implementaci,
- zanechání úplného GitHub handoffu, aby další agent nepotřeboval kontext z chatu s člověkem.

### Nesmí
- rozhodnout produktovou nebo governance otázku místo člověka ani považovat absenci odpovědi za rozhodnutí,
- svévolně měnit produktové priority, rozšiřovat scope nebo přidávat další požadavky,
- skrývat pod označením „propsání rozhodnutí“ práci, která ve skutečnosti vyžaduje analýzu, návrh nebo netriviální implementaci jiné role,
- vytvářet paralelní normativní kopie stejné informace,
- vystupovat jako nezávislý reviewer vlastních změn.

## Vývojář

### Odpovídá za
- implementaci schváleného issue,
- technická rozhodnutí uvnitř povoleného scope,
- průběžné lokální ověření změn,
- úpravu implementačně související dokumentace, pokud to vyžaduje pracovní kontrakt,
- transparentní uvedení odchylek nebo nových nálezů,
- vytvoření durable implementačního handoffu v PR nebo jiném předepsaném artefaktu.

### Nesmí
- měnit požadavky nebo acceptance criteria tak, aby odpovídaly jeho implementaci,
- opravovat nesouvisející problémy mimo scope,
- sám schválit vlastní práci jako nezávislý reviewer,
- nahrazovat chybějící produktové rozhodnutí vlastním předpokladem,
- implementovat `RECOMMENDATION` nebo `DECISION_REQUIRED` finding jen proto, že se objevil v review; oprávnění dalšího kroku určuje [`review-model.md`](review-model.md).

## Tester

### Odpovídá za
- nezávislé ověření acceptance criteria,
- testování očekávaného i hraničního chování,
- dokumentaci důkazů o výsledku,
- přesnou formulaci selhání a defektů,
- případnou tvorbu testovacích artefaktů, pokud jsou explicitně ve scope,
- durable testovací handoff podle [`handoff-protocol.md`](handoff-protocol.md).

### Nesmí
- opravovat produkční implementaci, kterou testuje,
- měnit očekávané chování podle skutečného výsledku,
- uzavírat produktovou nejasnost vlastním rozhodnutím.

## Reviewer

### Odpovídá za
- nezávislou kontrolu změny proti issue a normativním pravidlům,
- kontrolu scope discipline,
- kontrolu konzistence, udržovatelnosti a zbytečných změn,
- kontrolu, že tvrzené testy a dokumentační změny odpovídají realitě,
- klasifikaci substantive findings podle severity a disposition definovaných v [`review-model.md`](review-model.md),
- durable review handoff na kontrolovaném PR/artefaktu,
- věrné zaznamenání vlastního review nálezu jako navazujícího **Intake Issue**, pokud jde o skutečný samostatný follow-up; nové Issue musí odkazovat na původní review/nález.

### Nesmí
- opravovat kontrolovanou změnu místo autora,
- rozšiřovat review o své preferované redesigny mimo scope,
- měnit produktové požadavky,
- považovat vysokou severity za oprávnění vytvořit nový produktový/architektonický scope,
- měnit `RECOMMENDATION` na povinnou opravu bez nové autorizace,
- schválit změnu jen proto, že „vypadá rozumně“, pokud nesplňuje issue,
- považovat založení finding-derived Intake Issue za oprávnění určit jeho produktové řešení, prioritu, rozšířený scope nebo Ready stav.

## Integrátor

Integrátor vlastní technický krok, kterým se **schválená práce** začlení do integračního/produkčního stavu projektu. Konkrétní branch/release topologii definuje adoptující projekt.

### Odpovídá za
- ověření, že přesný integrovaný head/artefakt má všechny pracovní kontraktem požadované control gates,
- kontrolu relevantních CI/checks, review/test outcomes, dependencies a nevyřešených blokací,
- merge, promotion nebo jiný projektově definovaný integrační krok,
- zaznamenání integrovaného SHA/verze, cíle a gate evidence,
- aktualizaci work itemu do terminalního stavu pouze tehdy, když je integrace skutečně dokončená.

### Nesmí
- nahrazovat autora opravou implementace během integračního kroku,
- waive failed/missing control gate jen kvůli rychlosti,
- považovat chatové „approved“ za durable gate evidence,
- rozhodovat produktové nebo governance otázky,
- integrovat změnu, která má nevyřešený blocking `DEFECT` nebo required decision gate.

## Human / Product Owner

Člověk není agentní role, ale nejvyšší rozhodovací autorita pro produkt. Rozhoduje zejména produktové nejasnosti, priority, scope a změny governance.

Cílem systému je, aby člověk nemusel ručně předávat agentní reporty ani spouštět rutinní další kroky, pokud je lze bezpečně automatizovat.

## Společné pravidlo separace rolí

Jedna logická instance práce nesmí současně vystupovat jako autor změny a její nezávislý reviewer. U významných změn má být nezávislá i testovací kontrola, pokud ji pracovní kontrakt předepisuje.

Automatické chaining rolí tuto separaci neruší. Provider nebo service account může být technicky společný, ale role, context a pracovní instance musí zůstat logicky oddělené podle [`automation-model.md`](automation-model.md).

Pokud agent při své práci zjistí problém patřící jiné roli, má ho předat nebo zaznamenat, ne automaticky řešit.
