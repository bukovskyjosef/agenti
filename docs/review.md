# Independent review

Cílem review je ověřit správnost změny proti autorizovanému work contractu, ne prosadit Reviewerův preferovaný redesign.

## 1. Nezávislost

Autor změny nesmí být její nezávislý Reviewer. Reviewer pracuje z Issue, skutečného diffu/commitů, kanonické dokumentace a check/test evidence.

## 2. Co Reviewer kontroluje

1. Scope — změna řeší právě autorizovaný problém.
2. Requirements — odpovídá kanonickým pravidlům a decisions.
3. Acceptance criteria — existuje evidence splnění.
4. Shared contracts — nebyly změněny bez autority.
5. Technickou přiměřenost — řešení není zbytečně široké nebo křehké.
6. Validation — test/check evidence podporuje tvrzení.
7. Documentation — durable truth byla aktualizována tam, kde se změnila.
8. Dependencies/concurrency — byla respektována koordinace.

## 3. Finding má dvě osy

### Severity

- `BLOCKER`
- `MAJOR`
- `MINOR`
- `NIT`

Severity popisuje dopad. **Nevytváří implementační autoritu.**

### Disposition

#### `DEFECT`
Změna porušuje již autorizovaný kontrakt: například AC, existující invariant, required check, podporované chování nebo autorizovaný shared contract.

Autorizovaný další krok je nejmenší in-scope corrective change ve stejném work itemu.

#### `DECISION_REQUIRED`
Riziko nebo mezera vyžaduje nový produktový/governance/scope/architecture kontrakt.

Reviewer popíše evidence a potřebnou autoritu; nesmí sám vybrat variantu jako schválenou.

#### `RECOMMENDATION`
Volitelné zlepšení nad současný kontrakt. Nezablokuje current work jen proto, že by bylo „lepší“.

Developer ji nesmí oportunisticky implementovat během corrective loopu bez nové autority.

## 4. Celkový outcome

Reviewer vydá právě jeden výsledek:

- `APPROVED`,
- `CHANGES_REQUIRED`,
- `DECISION_REQUIRED`.

`APPROVED` může obsahovat Recommendations.

## 5. Corrective loop

```text
DEFECT
  ↓
Developer: smallest in-scope correction
  ↓
required validation
  ↓
updated PR
  ↓
independent re-review
```

Reviewer sám neopravuje kontrolovaný kód.

## 6. New scope

Finding mimo current contract se nestává součástí PR jen proto, že byl objeven při review. Podle disposition se buď:

- vrací do stejného corrective loopu (`DEFECT`),
- routuje k Human decision (`DECISION_REQUIRED`),
- zachytí jako volitelný future Intake (`RECOMMENDATION`).