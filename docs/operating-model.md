# Operating model

Tento dokument shrnuje, jak role spolupracují jako jeden systém. Detailní pravomoci rolí jsou kanonicky popsány v [`roles.md`](roles.md); tento dokument je znovu nedefinuje.

## Základní smyčka

```text
Human intent
    ↓
Analysis / scope definition
    ↓
Human product decision, pokud je potřeba
    ↓
Ready Issue
    ↓
Orchestration / assignment
    ↓
Implementation
    ↓
Independent review
    ↓
Independent verification
    ↓
Merge / completion
    ↓
Canonical knowledge updated
```

## Princip nekonkurujících agentů

Systém nepoužívá více agentů k paralelnímu řešení stejného úkolu bez explicitního důvodu. Výchozí model je spolupráce přes specializované role a kontrolní brány.

Důvodem je:

- menší plýtvání tokeny,
- jasná odpovědnost,
- menší počet konfliktních návrhů,
- jednodušší auditní stopa,
- lepší oddělení tvorby a kontroly.

Paralelní nezávislé řešení může být použito pouze jako explicitně zadaná metoda například pro průzkum variant, kritické review nebo ověření nejisté hypotézy.

## Princip jedné aktivní odpovědnosti

V každé fázi má práce jednoznačnou odpovědnou roli. Ostatní role mohou poskytovat vstupy nebo kontrolu, ale nesmí současně přepisovat výsledek role, která práci vlastní.

## Self-correction bez chaosu

Agenti se mají vzájemně kontrolovat, ale oprava probíhá návratem práce kompetentní roli, ne převzetím její práce kontrolorem.

Typický cyklus:

```text
Developer → Reviewer finding → Developer fix → Reviewer re-check
Developer → Tester defect → Developer fix → Tester re-test
Analyst → Product question → Human decision → Analyst updates issue
```

## Autonomie

Cílem není odstranit člověka ze systému. Cílem je odstranit člověka z mechanického předávání kontextu a rutinní koordinace.

Člověk zůstává v místech, kde je potřeba:

- produktové rozhodnutí,
- změna priorit,
- významná změna scope,
- změna governance,
- vědomé přijetí zásadního trade-offu nebo rizika.

Ostatní handoffy mají být proveditelné přímo mezi agenty prostřednictvím GitHub artefaktů.
