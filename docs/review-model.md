# Independent review model

Cílem review není vytvořit druhou implementaci ani redesignovat řešení podle vkusu reviewera. Cílem je nezávisle ověřit, že změna je správná, úplná, přiměřená a zůstala uvnitř schváleného scope.

## 1. Nezávislost

Autor změny nesmí být jejím nezávislým reviewerem. Reviewer má pracovat z Issue, skutečného PR diffu/commitů, relevantní kanonické dokumentace a durable test/check evidence, nikoli z neveřejného kontextu autora.

Automatizovaný review run musí být logicky oddělený od implementační instance podle [`automation-model.md`](automation-model.md).

## 2. Pořadí kontroly

Reviewer kontroluje zejména:

1. **Scope:** změna řeší právě schválený problém a nepřidává nesouvisející úpravy.
2. **Requirements:** implementace odpovídá autoritativním požadavkům a rozhodnutím.
3. **Acceptance criteria:** existuje důkaz, že jsou splněná.
4. **Shared contracts:** změna nemění schema/API/domain/governance/dependency surface bez autorizace.
5. **Konzistence:** změna nevytváří rozpor s jinými částmi systému nebo dokumentace.
6. **Technická kvalita:** řešení je přiměřeně jednoduché, udržovatelné a neobsahuje zjevné vady.
7. **Testovatelnost a důkazy:** uvedené testy a validace skutečně podporují tvrzení autora.
8. **Dokumentace:** kanonické dokumenty byly změněny tam, kde se změnila trvalá pravda.
9. **Concurrency/integration:** změna respektuje deklarované dependencies, shared surfaces a merge/coordination pravidla.

## 3. Finding má dvě nezávislé osy

Každý substantive finding se klasifikuje alespoň podle **severity** a **disposition**.

### Severity — jak velký je dopad

- **BLOCKER** — problém znemožňuje bezpečné/správné dokončení současného work itemu nebo integraci.
- **MAJOR** — významný problém s reálným dopadem na správnost, bezpečnost, udržovatelnost nebo kontrakt.
- **MINOR** — omezený problém, který má být přesně zaznamenán, ale dopad je lokální/malý.
- **NIT** — drobná připomínka nebo kosmetická záležitost.

Severity popisuje dopad. **Severity sama nikdy neuděluje oprávnění implementovat nové řešení.**

### Disposition — co je autorizovaný další krok

#### `DEFECT`

Použij pouze tehdy, když změna prokazatelně porušuje již autorizovaný kontrakt, například:

- nesplňuje acceptance criterion,
- odporuje existujícímu kanonickému invariant/pravidlu,
- required check/test selhává,
- zavádí regresi proti existujícímu podporovanému chování,
- mění shared contract bez autorizace,
- porušuje existující bezpečnostní/privacy/isolation kontrakt.

`DEFECT` se opravuje jako nejmenší in-scope corrective change v rámci stejného work itemu/PR, pokud finding neodhalil skutečně nový scope.

#### `DECISION_REQUIRED`

Použij, když existuje materiální riziko, mezera nebo trade-off, ale náprava by vyžadovala **nové** produktové/governance/architektonické/scope rozhodnutí nebo nový bezpečnostní/auth/data-policy kontrakt.

Reviewer:

- popíše riziko a evidence,
- uvede, jaká autorita musí rozhodnout,
- nesmí vybrat jednu variantu jako implicitně schválenou,
- nesmí přikázat implementaci nového řešení před durable rozhodnutím.

Pokud je rozhodnutí nutné před integrací současné práce, celkový review outcome je `DECISION_REQUIRED` a task se blokuje. Pokud rozhodnutí může být řešeno později bez porušení současného kontraktu, může být zaznamenáno jako follow-up decision Intake a současná práce může být jinak Approved.

#### `RECOMMENDATION`

Použij pro volitelné zlepšení, hardening, refactoring, optimalizaci, maintainability nebo defense-in-depth nad rámec současného kontraktu.

Recommendation je non-blocking pro současnou práci. Implementer ji nesmí oportunisticky zapracovat během corrective loopu. Stane se prací teprve poté, co ji Human/Orchestrator/Analyst podle kompetencí povýší do autorizovaného work contractu.

## 4. Severity není authority

Toto pravidlo je záměrné a platí i pro bezpečnostní findingy.

Příklad:

- konkrétní bypass existujícího authorization pravidla je `DEFECT`,
- názor, že MVP bez účtů by měl dostat kompletní nový auth/authz subsystém, je `DECISION_REQUIRED` nebo `RECOMMENDATION`, pokud takový kontrakt dosud neexistuje.

Reviewer má materiální rizika aktivně pojmenovat, ale nesmí z nich sám vytvořit nový produktový scope.

## 5. Celkový review outcome

Reviewer zaznamená právě jeden durable outcome:

- **APPROVED** — současný kontrakt je splněný, required checks/gates jsou doložené a neexistuje unresolved blocking defect ani required decision gate,
- **CHANGES_REQUIRED** — existuje unresolved `DEFECT`, který musí být opraven pro splnění současného kontraktu,
- **DECISION_REQUIRED** — další postup nebo integrace současné práce vyžaduje rozhodnutí správné autority, nikoli pouhou opravu existujícího kontraktu.

`APPROVED` může obsahovat `RECOMMENDATION` follow-up body; ty samy approval neblokují.

## 6. Corrective loop

Pro `DEFECT` platí:

```text
review finding
   ↓
stejný Issue / stejný PR nebo autorizovaný task branch
   ↓
nejmenší corrective change
   ↓
required verification
   ↓
updated PR/handoff
   ↓
independent re-review
```

Ordinary defect se nepřeklápí do nového tasku pouze proto, aby se „uklidil“ review report. Nové Issue je vhodné až tehdy, když finding odhaluje nový scope, decision gate nebo nezávislou budoucí práci.

## 7. Finding-derived Intake Issues

Reviewer smí podle [`roles.md`](roles.md) založit finding-derived Intake Issue, pokud je potřeba samostatný follow-up.

Nové Issue musí:

- věrně odkázat na původní finding/review,
- nezačínat jako Ready, pokud vyžaduje další analýzu/rozhodnutí,
- neprezentovat Reviewerovu preferovanou variantu jako schválený requirement,
- zachovat disposition findingu.

Typicky:

- current-contract `DEFECT` → stejný task corrective loop,
- `DECISION_REQUIRED` → decision artefakt nebo Intake blokovaný rozhodnutím,
- `RECOMMENDATION` → volitelný Intake/future triage.

## 8. Tester versus Reviewer

Reviewer a Tester nejsou totožné funkce:

- Reviewer kontroluje správnost změny jako změny a její soulad s kontraktem,
- Tester adversariálně ověřuje chování výsledného systému proti acceptance criteria a relevantním scénářům.

U malého nebo nízkorizikového úkolu může pracovní kontrakt explicitně povolit sloučení těchto kontrol do jedné nezávislé instance, ale nesmí se z toho stát implicitní výchozí stav pro významné změny.

## 9. Durable review handoff

Review výsledek se persistuje podle [`handoff-protocol.md`](handoff-protocol.md), přednostně jako formální GitHub PR review a inline comments pro line-specific findingy.

Doporučená summary struktura:

```text
## AGENT REPORT — REVIEWER

Outcome: APPROVED | CHANGES_REQUIRED | DECISION_REQUIRED
Reviewed head: <SHA/version>

Findings:
- MAJOR / DEFECT: ...
- BLOCKER / DECISION_REQUIRED: ...
- MINOR / RECOMMENDATION: ...

Evidence:
- ...

Authorized next action:
- ...
```

Review pouze v chatu nesplňuje gate, pokud Reviewer má GitHub write capability.

## 10. Review completion

Review je dokončeno, pokud:

- Reviewer zkontroloval přesný aktuální artefakt,
- všechny substantive findingy mají evidence a disposition,
- celkový outcome je durable zaznamenaný,
- při re-review je jasné, které dřívější defects byly opravené a co zůstává otevřené,
- required decision/recommendation follow-up je durable zachycený bez implicitní implementační autority.

Dokončené review se nereviewuje znovu pouze proto, že je samo pracovním Issue nebo review artefaktem. Typově specifická completion pravidla vlastní [`issue-standard.md`](issue-standard.md).
