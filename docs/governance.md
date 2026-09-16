# Governance and authority

## Purpose

Tento dokument určuje, kdo smí o čem rozhodovat a co dělat při nejasnosti nebo konfliktu.

## 1. Nejvyšší autorita

Člověk je Product Owner a jediný autor produktových rozhodnutí.

Za produktové rozhodnutí se považuje zejména změna nebo volba týkající se:

- cíle produktu,
- chování vůči uživateli,
- business pravidel,
- funkčního scope,
- priorit,
- UX významu,
- akceptovaného trade-offu mezi variantami produktu,
- toho, co má nebo nemá být považováno za správné chování.

Agent může připravit varianty, dopady, rizika a doporučení k rozhodnutí, ale nesmí produktové rozhodnutí vydávat za přijaté bez lidského potvrzení.

V tomto referenčním repozitáři je produktem samotný agentní systém. Změny governance, rolí, workflow a základních principů jsou proto produktovými rozhodnutími a vyžadují lidské schválení.

## 2. Technická autonomie agentů

Agent může samostatně učinit technické rozhodnutí, pokud současně platí:

1. nemění produktový kontrakt ani přijaté požadavky,
2. je v kompetenci jeho role,
3. je uvnitř scope issue,
4. respektuje existující architekturu a normativní pravidla,
5. rozhodnutí je přiměřené významu změny zdokumentováno v issue, PR nebo technickém rozhodnutí.

Jakmile technická volba začne měnit produktové chování nebo požadovaný výsledek, stává se produktovou otázkou a musí být eskalována člověku.

## 3. Hierarchie zdrojů pravdy

Při rozporu se používá toto pořadí:

1. aktuální explicitní lidské rozhodnutí zaznamenané v kanonickém místě,
2. normativní dokumentace na `main`,
3. schválené rozhodovací záznamy,
4. konkrétní GitHub Issue jako kontrakt daného úkolu,
5. implementace a testy na `main`,
6. otevřené PR, komentáře a pracovní diskuse.

Issue nesmí tiše přepisovat normativní pravidlo. Pokud je mezi nimi konflikt, práce se blokuje do vyřešení konfliktu.

## 4. Co není zdroj pravdy

Za autoritativní se nepovažuje:

- předchozí chat s agentem,
- paměť modelu,
- nezdokumentovaná ústní dohoda,
- lokální poznámky,
- necommitnuté změny,
- tvrzení v komentáři, které nebylo promítnuto do kanonického artefaktu.

Relevantní externí informace musí být před zahájením práce přenesena do issue nebo do příslušného kanonického dokumentu.

## 5. Konflikt nebo nejasnost

Agent nejprve určí typ problému:

- **produktová nejasnost:** připraví přesnou otázku, varianty a dopady a čeká na lidské rozhodnutí,
- **technická nejasnost:** vyřeší ji kompetentní role, pokud tím nemění produktový kontrakt,
- **rozpor ve zdrojích pravdy:** zastaví dotčenou práci a nechá rozpor opravit na kanonickém místě,
- **nález mimo scope:** neopravuje jej oportunisticky; předá jej jako samostatný nález nebo issue.

## 6. Zákaz implicitních rozhodnutí

Absence odpovědi, starý chat, předpoklad „tohle asi uživatel chtěl“ ani dosavadní implementace nejsou platným produkovým rozhodnutím.
