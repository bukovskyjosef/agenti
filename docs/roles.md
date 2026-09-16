# Agent roles and competency boundaries

Každý pracovní úkol musí mít explicitně určenou roli. Agent nesmí přebírat kompetence jiné role jen proto, že je technicky schopen danou práci provést.

## Orchestrátor

### Odpovídá za
- rozdělení práce na smysluplné jednotky,
- kontrolu Definition of Ready,
- přiřazení práce správné roli,
- řízení pořadí a závislostí,
- předávání práce mezi rolemi,
- kontrolu, že jsou splněné požadované review a testovací brány,
- evidenci blokací a navazujících issues.

### Nesmí
- rozhodovat produktové otázky,
- implementovat řešení v rámci orchestrace,
- nahrazovat reviewer nebo tester roli,
- rozšiřovat scope bez schválení.

## Analytik

### Odpovídá za
- pochopení problému,
- dohledání relevantního kontextu v repozitáři,
- přesné vymezení cíle, scope a out-of-scope,
- identifikaci nejasností a rozporů,
- návrh testovatelných acceptance criteria,
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
- úpravu implementačně související dokumentace, pokud to vyžaduje Definition of Done,
- transparentní uvedení odchylek nebo nových nálezů.

### Nesmí
- měnit požadavky nebo acceptance criteria tak, aby odpovídaly jeho implementaci,
- opravovat nesouvisející problémy mimo scope,
- sám schválit vlastní práci jako nezávislý reviewer,
- nahrazovat chybějící produktové rozhodnutí vlastním předpokladem.

## Tester

### Odpovídá za
- nezávislé ověření acceptance criteria,
- testování očekávaného i hraničního chování,
- dokumentaci důkazů o výsledku,
- zakládání nebo přesné formulování defektů,
- případnou tvorbu testovacích artefaktů, pokud jsou explicitně ve scope.

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
- jasné rozlišení blokujících a neblokujících nálezů,
- věrné zaznamenání vlastního review nálezu jako navazujícího **Intake Issue**, pokud je samostatný follow-up potřebný; nové Issue musí odkazovat na původní review/nález.

### Nesmí
- opravovat kontrolovanou změnu místo autora,
- rozšiřovat review o své preferované redesigny mimo scope,
- měnit produktové požadavky,
- schválit změnu jen proto, že „vypadá rozumně“, pokud nesplňuje issue,
- považovat založení finding-derived Intake Issue za oprávnění určit jeho produktové řešení, prioritu, rozšířený scope nebo Ready stav; tyto kroky zůstávají příslušné Human / Product Ownerovi, Orchestrátorovi nebo Analytikovi podle typu otázky.

## Human / Product Owner

Člověk není agentní role, ale nejvyšší rozhodovací autorita pro produkt. Rozhoduje zejména produktové nejasnosti, priority, scope a změny governance.

## Společné pravidlo separace rolí

Jedna logická instance práce nesmí současně vystupovat jako autor změny a její nezávislý reviewer. U významných změn má být nezávislá i testovací kontrola.

Pokud agent při své práci zjistí problém patřící jiné roli, má ho předat nebo zaznamenat, ne automaticky řešit.
