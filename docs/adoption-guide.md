# Adoption guide

Tento dokument popisuje, jak použít principy repozitáře `agenti` v reálném projektu.

## 1. Nevytvářej druhý systém pravdy

Při adopci nejprve zjisti, kde projekt již drží požadavky, dokumentaci, rozhodnutí a pracovní úkoly. Nový agentní model má existující informace konsolidovat, ne k nim přidat paralelní kopii.

## 2. Zaveď minimální kostru

Každý agentně řízený projekt by měl mít alespoň:

- `README.md` pro člověka,
- `AGENTS.md` jako jediný vstupní bod pro agenta,
- mapu kanonické dokumentace,
- explicitní role a kompetence,
- workflow práce,
- standard GitHub Issue,
- pravidla review a testování,
- místo pro významná rozhodnutí,
- issue a PR šablony odpovídající procesu.

Názvy a umístění lze přizpůsobit projektu, význam nikoli.

## 3. Přizpůsob kontextovou mapu

Agent nesmí pro každý úkol číst všechno. Do projektu proto doplň mapu, která odpoví:

- co čte každý agent vždy,
- co čte konkrétní role,
- kde jsou produktové požadavky,
- kde je architektura,
- kde jsou business pravidla,
- kde jsou API nebo datové kontrakty,
- kde jsou rozhodnutí,
- kde jsou testovací pravidla.

## 4. Vyčisti duplicity

Před autonomnější prací agentů odstraň nebo označ:

- staré specifikace konkurující aktuálním,
- duplicitní README instrukce,
- pravidla ukrytá pouze v issues,
- dokumenty bez jasného statusu,
- historické soubory v běžné kontextové cestě.

Autonomie agentů zesiluje nejen dobrý pořádek, ale i existující nekonzistence.

## 5. Zaveď role

Minimální doporučené role jsou:

- orchestrátor,
- analytik,
- vývojář,
- tester,
- reviewer.

Projekt může přidat další specializace, pokud mají skutečně odlišnou odpovědnost. Role nevytvářej pouze podle názvu technologie; vytvářej je podle odpovědnosti a pravomocí.

## 6. Přesuň úkoly do Issues

Nová práce má vznikat jako issue. Než je předána vývojáři, musí projít Definition of Ready.

Pokud práce začíná v chatu, relevantní kontext a rozhodnutí se před zahájením realizace přenesou do GitHubu.

## 7. Odděl autora a kontrolu

Změna má vzniknout v branch/PR a být ověřena jinou rolí. Reviewer ani tester nemají tiše přebírat práci autora.

## 8. Začni s lidským dohledem

Autonomie se zvyšuje až tehdy, když:

- issues jsou opakovaně dostatečně přesná,
- role skutečně respektují hranice,
- review zachytává chyby,
- dokumentace zůstává aktuální,
- handoff mezi novými instancemi agentů funguje bez externího chatu.

## 9. Test adopce

Projekt je připravený pro agentní práci, pokud můžeš nové instanci agenta říct pouze:

> Pracuj na issue #N v roli X. Řiď se repozitářem.

a agent dokáže bez dalšího neveřejného kontextu správně určit, co má dělat, co dělat nesmí, kde získat podklady a jak prokázat dokončení.
