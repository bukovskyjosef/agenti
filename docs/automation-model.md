# Automation model

Tento dokument je kanonickým vlastníkem pravidel pro **automatizované spouštění a řetězení agentních rolí**. Popisuje cílový provozní model nezávisle na konkrétním AI providerovi, CLI, GitHub App nebo branch strategii.

## Cílová architektura

```text
Human / Product Owner
        ↕
    Asistentka
        ↕
      GitHub
        ↕
automatizovaný Orchestrátor
        ↕
Analyst / Developer / Reviewer / Tester / Integrator
```

Člověk má zůstat rozhodovací autoritou, ne ručním schedulerem ani message bus mezi rolemi.

## 1. Trigger není autorita

Automatizace může být spuštěna například:

- machine-readable komentářem,
- změnou Issue stavu,
- dokončením PR/review/checku,
- explicitním workflow dispatch,
- jinou projektově definovanou událostí.

Trigger pouze žádá o zpracování. Nesmí přepsat pracovní kontrakt, role boundaries, control gates ani lidskou autoritu. Spuštěný agent nejprve rekonstruuje aktuální stav z repozitáře a GitHubu.

## 2. Pouze další governance-authorized krok

Automatizovaný Orchestrátor smí provést pouze nejbližší krok, který je podle aktuálního trvalého stavu již autorizovaný, například:

- uznat dokončený handoff,
- změnit task status podle doloženého výsledku,
- připravit nebo aktivovat další Ready work item,
- spustit/předat další roli,
- vytvořit decision request,
- zaznamenat blocker.

Nesmí z pohodlnosti přeskočit chybějící gate, sám vyřešit produktovou nejasnost ani implementovat práci, pokud jeho role implementaci nepovoluje.

## 3. Least privilege

Technická oprávnění mají odpovídat roli.

Příklady:

- Coordinator automation běžně potřebuje číst repository/GitHub state a zapisovat Issues, ale nemusí mít právo měnit produkční kód,
- Reviewer potřebuje číst změny a zapisovat review, nikoli tiše commitovat opravy do autorovy větve,
- Integrátor potřebuje merge/promotion oprávnění až po splnění gate podmínek,
- provider adapter nesmí agentovi přidat pravomoc, kterou mu nedává kanonická role.

Pokud platforma neumí oprávnění jemně oddělit, pravidla role zůstávají závazná a technická omezení mají být co nejbližší tomuto modelu.

## 4. Izolace rolí a nezávislost

Automatické chaining nesmí zrušit nezávislost kontrolních rolí.

- Author a independent Reviewer nesmí být jedna logická pracovní instance.
- Reviewer má dostat durable artefakty a skutečný diff, ne skrytý chain-of-thought autora.
- Samostatné role mají mít oddělené runs/sessions/context, pokud je to technicky možné.
- Sdílený service account nebo provider sám o sobě neznamená porušení nezávislosti, pokud jsou role, context a oprávnění logicky oddělené.

## 5. Idempotence a concurrency ochrana

Automatizace musí předcházet dvojímu provedení stejného kroku.

Doporučené mechanismy:

- per-Issue/per-PR concurrency group nebo lock,
- kontrola aktuálního lifecycle stavu před write akcí,
- machine-readable run/command marker,
- deduplikace follow-up/blocker artefaktů,
- opakovatelné kroky, které při retry nevytvoří druhou implementaci nebo druhé rozhodnutí.

Konkrétní technika je projektová volba; invariantem je, že souběžné nebo opakované triggery nesmí rozbít pracovní kontrakt.

## 6. Durable success i durable failure

Úspěšný automatizovaný krok musí zanechat handoff podle [`handoff-protocol.md`](handoff-protocol.md).

Selhání, které zastaví agentní tok, nesmí existovat pouze v dočasném logu CI/Actions. Automatizace má vytvořit nebo aktualizovat trvalý blocker artefakt s:

- zdrojovým Issue/PR,
- rolí nebo workflow, které selhalo,
- bezpečným identifikátorem běhu/odkazem na log,
- stručným stavem,
- dalším požadovaným krokem.

Do blockeru se nekopírují secrets ani nepotřebné raw logy.

## 7. Human decision interrupt

Pokud další krok vyžaduje produktové nebo governance rozhodnutí:

1. automatizace nesmí vybrat variantu,
2. rozhodovací bod se zapíše jako trvalý decision artefakt,
3. tok se označí jako blokovaný rozhodnutím,
4. Asistentka zpracuje decision queue s člověkem podle [`roles.md`](roles.md) a [`workflow.md`](workflow.md),
5. po trvalém záznamu rozhodnutí může automatizace znovu vyhodnotit další autorizovaný krok.

Toto je hlavní hranice mezi autonomní orchestration a lidskou produktovou autoritou.

## 8. Provider adapters

Soubory nebo konfigurace specifické pro nástroj/provider (například `CLAUDE.md`, Codex instrukce, IDE agent rules nebo workflow prompt) jsou **adaptéry**.

Adaptér smí:

- přeložit obecnou roli do konkrétních příkazů/nástrojů,
- popsat bezpečné provider-specific operations,
- optimalizovat startup/context loading,
- definovat technický způsob persistence výsledku.

Adaptér nesmí:

- měnit governance,
- rozšiřovat kompetence role,
- oslabit control gates,
- vytvořit druhý kanonický workflow,
- rozhodnout produktovou otázku.

Při konfliktu má přednost kanonický model v `docs/`.

## 9. Branch a release strategie je konfigurovatelná

Reference model nevyžaduje konkrétní topologii typu `develop → main`.

Adoptující projekt musí explicitně určit:

- autoritativní/integration branch nebo branches,
- odkud vznikají task branches,
- kam míří implementační PR,
- kdo a za jakých gates smí merge/promotion provést,
- co znamená production/release stav.

Automatizace se této projektové branch authority musí podřídit.

## 10. Postupná adopce automatizace

Cílový model lze zavádět po vrstvách:

1. durable handoff bez automatického spouštění,
2. automatizovaný Coordinator,
3. automatické předávání vykonávajícím rolím,
4. automatické review/test/integration triggery,
5. plný event-driven řetězec s člověkem pouze na decision gates.

Vyšší úroveň autonomie se zapíná až tehdy, když nižší úroveň opakovaně zachovává scope, handoff a autoritu.
