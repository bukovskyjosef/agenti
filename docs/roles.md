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
- jasné rozlišení blokujících a neblokujících nálezů.

### Nesmí
- opravovat kontrolovanou změnu místo autora,
- rozšiřovat review o své preferované redesigny mimo scope,
- měnit produktové požadavky,
- schválit změnu jen proto, že „vypadá rozumně“, pokud nesplňuje issue.

## Human / Product Owner

Člověk není agentní role, ale nejvyšší rozhodovací autorita pro produkt. Rozhoduje zejména produktové nejasnosti, priority, scope a změny governance.

## Společné pravidlo separace rolí

Jedna logická instance práce nesmí současně vystupovat jako autor změny a její nezávislý reviewer. U významných změn má být nezávislá i testovací kontrola.

Pokud agent při své práci zjistí problém patřící jiné roli, má ho předat nebo zaznamenat, ne automaticky řešit.
