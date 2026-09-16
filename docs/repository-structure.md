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

Je vstupním bodem pro člověka. Vysvětluje účel projektu, základní orientaci a odkazuje na kanonické zdroje. Nemá duplikovat kompletní agentní instrukce.

## AGENTS.md

Je vstupním bodem pro agenta. Má být krátký a stabilní. Obsahuje:

- povinný startovací postup,
- nejdůležitější invarianty,
- odkazy na detailní pravidla,
- instrukci, jak reagovat na konflikt nebo chybějící kontext.

Nemá se z něj stát encyklopedie projektu.

## docs/

Obsahuje trvalé znalosti projektu. Doporučené členění má vycházet z domény konkrétního produktu, ne z náhodného historického růstu dokumentace.

Každý dokument má mít jasnou odpovědnost. Pokud dva dokumenty odpovídají na stejnou normativní otázku, struktura je pravděpodobně chybná.

## docs/decisions/

Obsahuje významná přijatá rozhodnutí, jejich kontext a důvod. Rozhodovací záznam nenahrazuje aktuální specifikaci; vysvětluje, proč aktuální stav vznikl.

Pokud se rozhodnutí změní, aktuální normativní dokumentace se aktualizuje a nový rozhodovací záznam popíše změnu. Starý záznam zůstává historickým dokladem.

## GitHub Issues

Issues obsahují práci, ne trvalou specifikaci. Po dokončení issue musí všechna trvalá fakta, která vznikla, skončit na příslušném kanonickém místě v repozitáři.

Issue nesmí být jediným místem, kde je popsáno aktuální dlouhodobé chování produktu.

## Pull Requests

PR je návrh změny a auditní stopa jejího ověření. Po merge nesmí být nutné číst diskusi v PR, aby bylo možné pochopit současný produkt.

## Archivace

Historické dokumenty mohou existovat pouze pokud:

- mají jasný důvod zachování,
- jsou zřetelně označeny jako neautoritativní,
- nejsou v běžné kontextové cestě agenta,
- nehrozí jejich záměna za aktuální pravidla.

Pokud historický dokument nemá hodnotu, je lepší spoléhat na Git historii než udržovat druhou zastaralou kopii v repozitáři.
