# Operating model

Tento dokument shrnuje, jak role spolupracují jako jeden systém. Detailní pravomoci rolí jsou kanonicky popsány v [`roles.md`](roles.md); tento dokument je znovu nedefinuje.

## Cílová smyčka

```text
Human intent
    ↓
Analysis / scope definition
    ↓
Decision gate? ── ano ──→ Asistentka ↔ Human / Product Owner
    │                         ↓
    └──────────── ne / resolved
                              ↓
                         Ready Issue
                              ↓
                    Orchestration / assignment
                              ↓
                    Implementation / execution
                              ↓
                 Durable implementation handoff
                              ↓
                  Independent review / testing
                              ↓
                     Approved work state
                              ↓
                    Integration / promotion
                              ↓
                             Done
                              ↓
                 Canonical knowledge current
```

Cílový model počítá s tím, že rutinní přechody mezi rolemi mohou být automatizované. Automatizace se řídí [`automation-model.md`](automation-model.md) a nesmí měnit autoritu role ani lidská rozhodovací práva.

## GitHub jako message bus

Člověk nesmí být nutným prostředníkem pro předání reportu mezi agenty. Issue, PR, review, check a další definované GitHub artefakty jsou sdíleným komunikačním kanálem. Přesné cíle handoffů vlastní [`handoff-protocol.md`](handoff-protocol.md).

Chat může sloužit jako uživatelské rozhraní, ale nesmí být jediným místem, kde zůstane stav potřebný další roli.

## Princip nekonkurujících agentů

Systém nepoužívá více agentů k paralelnímu řešení stejného úkolu bez explicitního důvodu. Výchozí model je spolupráce přes specializované role a kontrolní brány.

Důvodem je:

- menší plýtvání tokeny,
- jasná odpovědnost,
- menší počet konfliktních návrhů,
- jednodušší auditní stopa,
- lepší oddělení tvorby a kontroly.

Paralelní nezávislé řešení může být použito pouze jako explicitně zadaná metoda například pro průzkum variant, kritické review nebo ověření nejisté hypotézy.

## Paralelní práce různých úkolů

Nekonkurující role neznamenají sériové zpracování celého projektu. Různé work itemy mohou běžet souběžně, pokud jejich pracovní kontrakty deklarují concurrency class a shared surfaces podle [`issue-standard.md`](issue-standard.md).

Orchestrátor má umožnit paralelismus tam, kde je bezpečný, a zabránit souběžným změnám tam, kde by sdílený kontrakt nebo merge pořadí vytvářely konflikt.

## Princip jedné aktivní odpovědnosti

V každé fázi má práce jednoznačnou odpovědnou roli. Ostatní role mohou poskytovat vstupy nebo kontrolu, ale nesmí současně přepisovat výsledek role, která práci vlastní.

Automatické spuštění role tuto odpovědnost nemění. Technická schopnost workflow zapisovat do více povrchů není oprávněním převzít více rolí.

## Self-correction bez chaosu

Agenti se mají vzájemně kontrolovat, ale oprava probíhá návratem práce kompetentní roli, ne převzetím její práce kontrolorem.

Typický cyklus:

```text
Developer → Reviewer DEFECT → Developer fix → Reviewer re-check
Developer → Tester failure → Developer fix → Tester re-test
Reviewer → DECISION_REQUIRED → Asistentka/Human decision → updated contract → authorized execution
Reviewer → RECOMMENDATION → optional Intake/future triage, current work continues if otherwise approved
Analyst → Product question → Human decision → Analyst updates issue
```

Severity findingu sama neurčuje, co se smí implementovat. Autoritu dalšího kroku určuje disposition podle [`review-model.md`](review-model.md).

## Integration boundary

Výsledek implementace není automaticky integrovaný jen proto, že autor dokončil kód. Požadované gates musí být doložené a integrační krok provádí role s integrační odpovědností podle [`roles.md`](roles.md) a projektové branch/release politiky.

Reference model nevnucuje konkrétní `develop/main` topologii; vyžaduje pouze explicitní autoritu integračních cílů a zákaz obejití gate podmínek.

## Autonomie

Cílem není odstranit člověka ze systému. Cílem je odstranit člověka z mechanického předávání kontextu, ručního scheduleru a rutinní koordinace.

Člověk zůstává v místech, kde je potřeba:

- produktové rozhodnutí,
- změna priorit,
- významná změna scope,
- změna governance,
- vědomé přijetí zásadního trade-offu nebo rizika.

Ostatní handoffy mají být proveditelné přímo mezi agenty prostřednictvím GitHub artefaktů a v cílovém stavu mohou být spouštěny automaticky.
