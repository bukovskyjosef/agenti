# Work lifecycle

Tento dokument definuje standardní pořadí práce od nejasného záměru po integrovaný a doložený výsledek. Přesná status semantics a povinný Issue kontrakt vlastní [`issue-standard.md`](issue-standard.md).

Ne každé Issue musí projít všemi realizačními a kontrolními fázemi. Použitelné fáze se určují podle typu výsledku práce a předepsaných control gates.

## 1. Intake

Vstupem může být lidský požadavek, nalezený problém, review finding nebo návrh změny.

Orchestrátor nebo analytik zajistí, aby vzniklo GitHub Issue. Práce nesmí dlouhodobě existovat pouze v chatu.

Stejné Issue se dále dopracovává; nevytváří se nové Issue jen kvůli přechodu mezi Intake, Analysis a Ready.

## 2. Analysis

Analytik v témže Issue připraví pracovní kontrakt tak, aby bylo jednoznačné:

- proč se práce dělá,
- co je cílem,
- co je ve scope a out-of-scope,
- jaké kanonické zdroje se použijí,
- jaké jsou dependencies,
- jaké shared surfaces mohou kolidovat,
- jaká concurrency class platí,
- jak se pozná dokončení,
- jaké control gates jsou požadované,
- jaké otázky tvoří decision gates.

Produktové nejasnosti se řeší před označením práce jako Ready.

## Human decision loop

Pokud práce vyžaduje produktové nebo governance rozhodnutí člověka, musí být rozhodovací bod explicitně zachycen v GitHubu. Asistentka podle kompetencí v [`roles.md`](roles.md):

1. vyhledá otevřené explicitní decision body vyžadující Human / Product Ownera,
2. zpracovává je s člověkem po jednom s ohledem na závislosti a blokace,
3. u každého bodu stručně popíše problém, nabídne zpravidla 2–3 materiálně odlišné varianty a podstatné dopady,
4. zaznamená explicitní lidské rozhodnutí do původního decision/work artefaktu,
5. pokud rozhodnutí lze přímo a mechanicky propsat, aktualizuje pouze kanonické artefakty, jejichž aktuální pravda se rozhodnutím mění,
6. pokud rozhodnutí vyžaduje další analýzu, návrh nebo netriviální implementaci, vytvoří nebo předá navazující work item příslušné roli,
7. zanechá durable handoff podle [`handoff-protocol.md`](handoff-protocol.md).

Decision artefakt po rozhodnutí zůstává auditní stopou. Aktuální trvalé pravidlo musí být zachyceno u svého kanonického vlastníka.

## 3. Ready

Stejné Issue se označí jako **Ready** teprve po splnění kompletní Definition of Ready v [`issue-standard.md`](issue-standard.md).

Ready znamená, že nová kompetentní instance agenta může začít pouze z repozitáře a Issue bez doplňujícího kontextu z chatu.

## 4. Assignment a orchestrace

Orchestrátor:

- zkontroluje Ready stav a dependencies,
- potvrdí concurrency class a případnou koordinaci shared surfaces,
- určí vykonávající roli,
- předá nebo spustí další governance-authorized krok.

Tento krok může být automatizovaný podle [`automation-model.md`](automation-model.md). Automatizace však nesmí změnit pracovní kontrakt bez odpovídající autority.

## 5. Execution / In Progress

Vykonávající role:

1. načte povinný kontext,
2. ověří scope a dependencies,
3. pracuje pouze na autorizovaném výsledku,
4. průběžně ověřuje změny,
5. zaznamená nové nálezy mimo scope bez oportunistické opravy,
6. vytvoří předepsaný durable handoff.

Pro implementaci je běžným handoff boundary Pull Request, pokud projekt používá Git/PR workflow.

## 6. In Review

Pokud je předepsané review nebo testování, práce přechází do kontrolní fáze.

Reviewer pracuje podle [`review-model.md`](review-model.md). Tester provádí verification podle kontraktu. Obě role zapisují výsledky do durable GitHub artefaktů podle [`handoff-protocol.md`](handoff-protocol.md).

Kontrola se provádí proti skutečnému aktuálnímu headu/artefaktu, ne pouze proti shrnutí autora.

## 7. Changes Required corrective loop

Pokud kontrola nalezne autorizovaný `DEFECT`, práce se vrací kompetentní vykonávající roli ve stejném pracovním kontraktu, pokud nález nepředstavuje skutečně nový scope.

```text
DEFECT
  ↓
smallest in-scope correction
  ↓
required verification
  ↓
updated durable handoff
  ↓
independent re-review / re-test
```

Reviewer ani Tester defekt sami neopravují v rámci nezávislé kontroly.

Pokud finding vyžaduje nové rozhodnutí, corrective loop se nespustí před jeho explicitní autorizací. Pokud jde pouze o `RECOMMENDATION`, současná práce se kvůli ní neopravuje, pokud ji příslušná autorita nepromění v nový nebo aktualizovaný work contract.

## 8. Approved

Práce může být označena **Approved**, když jsou splněné všechny required control gates a nezůstává blocking defect nebo required decision gate.

Approved ještě nemusí znamenat, že změna je integrovaná do autoritativního cíle projektu.

## 9. Integration / promotion

Pokud typ práce vyžaduje merge, release nebo jinou integraci, Integrátor ověří přesný artefakt a gate evidence a provede projektově definovaný integrační krok.

Konkrétní branch/release topologii stanovuje adoptující projekt. Reference model nevyžaduje `develop/main` ani jinou konkrétní dvojici větví.

## 10. Done / completion

Issue se označí jako **Done** pouze podle typově specifických completion pravidel v [`issue-standard.md`](issue-standard.md).

U změnové práce, která vyžaduje integraci, znamená Done skutečně integrovaný výsledek. Samotné dokončení implementace nebo review není Done, pokud ještě chybí předepsaný integrační krok.

## Blocked interrupt

Blocker může přerušit kteroukoli ne-terminální fázi. Musí být durable zachycený s důvodem, evidencí, požadovanou další autoritou/rolí a stavem, ze kterého se po vyřešení pokračuje.

Typické příčiny:

- product/governance decision,
- dependency,
- technická překážka,
- konflikt shared surfaces/concurrency,
- selhání automatizace.

Blocker není oprávnění k improvizaci.

## Durable handoff contract

Při předání mezi rolemi se nepřenáší soukromý kontext agenta. Předává se stav zachycený v repozitáři a GitHub artefaktech podle [`handoff-protocol.md`](handoff-protocol.md).

Dobré předání musí umožnit následující roli pokračovat bez dotazu typu „co jste vlastně předtím řešili?“ a bez toho, aby člověk kopíroval report z jednoho agenta druhému.
