# Context and token policy

Agent má získat dostatek kontextu pro správnou práci, ale nesmí bezdůvodně načítat celý repozitář.

## 1. Progressive disclosure

Kontext se načítá po vrstvách:

1. `/AGENTS.md`,
2. konkrétní GitHub Issue,
3. relevantní normativní dokument podle `docs/README.md`,
4. konkrétní kanonické soubory odkazované z issue,
5. další části repozitáře pouze pokud vznikne konkrétní informační potřeba.

Výchozí strategie „přečti celý repozitář“ je nežádoucí.

## 2. Context locality

Issue má ukázat cestu ke kontextu, ne jej celý duplikovat. Agent má být schopen z issue určit, které části systému jsou relevantní.

Pokud je k pochopení úkolu nutné prohledat celý projekt bez vodítka, je to signál nedostatečné informační architektury nebo nekvalitního issue.

## 3. Canonical information

Jedna skutečnost má mít jedno autoritativní místo. Ostatní soubory mají používat odkazy místo kopírování.

Důvody:

- menší riziko zastarání,
- méně rozporů,
- méně tokenů,
- snazší aktualizace,
- jasnější odpovědnost.

## 4. Context persistence

Informace potřebná pro budoucího agenta nesmí zůstat pouze v:

- chatu,
- chain-of-thought nebo interní paměti modelu,
- lokálním terminálu,
- ústním předání.

Pokud ovlivňuje další práci, musí skončit v kanonickém dokumentu, issue, PR nebo jiném definovaném artefaktu.

## 5. Minimal sufficient context

Minimalizace tokenů neznamená přeskočit potřebné podklady. Agent má hledat **nejmenší úplnou množinu kontextu**, která mu umožní správně splnit úkol.

Při pochybnosti má před dalším širokým načítáním formulovat konkrétní otázku: „Jakou informaci mi chybí a kde je její kanonické místo?“

## 6. Shrnutí není nový zdroj pravdy

Agent může vytvořit pracovní shrnutí pro efektivitu, ale shrnutí nesmí začít konkurovat původnímu kanonickému zdroji. Pokud shrnutí obsahuje novou trvalou skutečnost, musí být tato skutečnost zapsána na správné kanonické místo.
