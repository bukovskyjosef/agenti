# Reference repository structure

Cílem struktury je, aby agent rychle rozpoznal, kde hledat autoritativní informaci a kam novou informaci uložit.

## Doporučený kořen projektu

```text
/
├── README.md
├── AGENTS.md
├── docs/
│   ├── README.md
│   ├── ... normativní projektová dokumentace ...
│   └── decisions/
├── src/                    # pokud jde o softwarový produkt
├── tests/                  # podle technologie projektu
└── .github/
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

Konkrétní produkt může strukturu rozšířit, ale neměl by vytvářet paralelní místa se stejnou odpovědností.

## README.md

Je vstupním bodem pro člověka. Vysvětluje účel projektu, základní orientaci a odkazuje na kanonické zdroje. Může stručně shrnout pravidlo pro orientaci, ale nesmí se stát druhým kanonickým vlastníkem pravidla definovaného jinde.

## AGENTS.md

Je vstupním bodem pro agenta. Má být krátký a stabilní. Obsahuje:

- povinný startovací postup,
- stručná provozní připomenutí důležitých invariantů,
- odkazy na kanonické vlastníky detailních pravidel podle `docs/README.md`,
- instrukci, jak reagovat na konflikt nebo chybějící kontext.

Shrnutí v `AGENTS.md` slouží pro routing a cold start; pokud detailní pravidlo vlastní jiný dokument, `AGENTS.md` jej nesmí nezávisle redefinovat. Nemá se z něj stát druhá governance vrstva ani encyklopedie projektu.

## docs/

Obsahuje trvalé znalosti projektu. `docs/README.md` mapuje rodiny pravidel na jejich jednotlivé kanonické vlastníky. Doporučené členění má vycházet z domény konkrétního produktu, ne z náhodného historického růstu dokumentace.

Každý dokument má mít jasnou odpovědnost. Pokud dva dokumenty odpovídají na stejnou normativní otázku, struktura je chybná; jeden z nich musí být kanonický vlastník a druhý smí pouze odkázat nebo stručně shrnout jeho význam.

## docs/decisions/

Obsahuje významná přijatá rozhodnutí, jejich kontext a důvod. Rozhodovací záznam je auditní a historický artefakt: vysvětluje, proč aktuální stav vznikl, ale po propsání rozhodnutí nenahrazuje aktuální provozní specifikaci u kanonického vlastníka pravidla.

Pokud se rozhodnutí změní, aktuální normativní dokumentace se aktualizuje a nový rozhodovací záznam popíše změnu. Starý záznam zůstává historickým dokladem a nesmí být interpretován jako konkurenční aktuální pravidlo.

## GitHub Issues

Issues obsahují práci, rozhodovací frontu a auditní stopu, ne trvalou provozní specifikaci. Po dokončení issue musí všechna trvalá fakta, která vznikla, skončit na příslušném kanonickém místě v repozitáři.

Issue nesmí být jediným místem, kde je popsáno aktuální dlouhodobé chování produktu.

## Pull Requests

PR je návrh změny a auditní stopa jejího ověření. Po merge nesmí být nutné číst diskusi v PR, aby bylo možné pochopit současný produkt.

## Archivace

Historické dokumenty mohou existovat pouze pokud:

- mají jasný důvod zachování,
- jsou zřetelně označeny jako neautoritativní pro aktuální stav,
- nejsou v běžné kontextové cestě agenta,
- nehrozí jejich záměna za aktuální pravidla.

Historický nebo rozhodovací artefakt může být autoritativní jako záznam toho, co bylo v minulosti rozhodnuto, ale není tím automaticky autoritativní pro současné provozní pravidlo. Pokud historický dokument nemá samostatnou auditní hodnotu, je lepší spoléhat na Git historii než udržovat druhou zastaralou kopii v repozitáři.
