# Work lifecycle

Tento dokument definuje standardní životní cyklus práce od nejasného záměru po ověřený výsledek.

Ne každé Issue musí projít všemi níže uvedenými realizačními a kontrolními fázemi. Použitelné fáze se určují podle typu výsledku práce a předepsaných kontrolních bran. Typově specifická pravidla dokončení vlastní [`issue-standard.md`](issue-standard.md).

## 1. Intake

Vstupem může být lidský požadavek, nalezený problém nebo návrh změny.

Orchestrátor nebo analytik zajistí, aby vzniklo GitHub Issue. Práce nesmí dlouhodobě existovat pouze v chatu.

Work item vzniká ve stavu **Intake** a může být záměrně neúplný. Stejné Issue se dále dopracovává; nevytváří se nové Issue jen kvůli přechodu mezi Intake, Analysis a Ready.

## 2. Analysis

Při zahájení skutečného dopracování se stav work itemu změní na **Analysis**. Analytik v témže Issue připraví pracovní kontrakt tak, aby bylo jednoznačné:

- proč se práce dělá,
- co je cílem,
- co je ve scope,
- co je explicitně mimo scope,
- jaké kanonické zdroje se použijí,
- jaká pravidla a omezení platí,
- jaké jsou závislosti,
- jak se pozná dokončení,
- jaké otázky vyžadují lidské rozhodnutí.

Produktové nejasnosti se řeší před označením práce jako Ready.

## Human decision loop

Pokud práce vyžaduje produktové nebo governance rozhodnutí člověka, musí být rozhodovací bod explicitně zachycen v GitHubu. Asistentka podle kompetencí v [`roles.md`](roles.md):

1. vyhledá otevřené explicitní decision body vyžadující Human / Product Ownera,
2. zpracovává je s člověkem po jednom; pokud mezi nimi existují závislosti nebo blokace, použije jejich logické pořadí, nikoli vlastní produktovou prioritu,
3. u každého bodu stručně popíše problém, nabídne zpravidla 2–3 materiálně odlišné varianty a podstatné dopady; doporučení je volitelné,
4. zaznamená explicitní lidské rozhodnutí do původního decision/work artefaktu,
5. pokud rozhodnutí lze přímo a mechanicky propsat, aktualizuje pouze kanonické artefakty, jejichž aktuální pravda se rozhodnutím mění,
6. pokud rozhodnutí vyžaduje další analýzu, návrh nebo netriviální implementaci, vytvoří nebo předá navazující work item příslušné roli místo oportunistického provedení této práce,
7. do GitHubu zaznamená dostatečný handoff, aby další role nepotřebovala soukromý kontext z rozhovoru s člověkem.

Decision artefakt po rozhodnutí zůstává auditní stopou. Aktuální trvalé pravidlo musí být zachyceno ve svém kanonickém provozním dokumentu; decision artefakt se nesmí stát druhou paralelní specifikací.

## 3. Ready

Stejné Issue se označí jako **Ready** teprve po splnění kompletní Definition of Ready v [`issue-standard.md`](issue-standard.md).

Před přechodem do Ready musí být doplněný kompletní pracovní kontrakt relevantní pro daný typ práce a readiness checklist musí odpovídat skutečnému stavu. Analytik připravuje obsah; Orchestrátor při handoffu kontroluje Ready stav a závislosti podle kompetencí v [`roles.md`](roles.md). Samotná existence Issue ani odeslání Issue formuláře Ready stav nevytváří.

Ready znamená, že nová kompetentní instance agenta může začít pracovat pouze z repozitáře a Issue bez doplňujícího kontextu z chatu.

## 4. Assignment

Orchestrátor určí vykonávající roli a zkontroluje závislosti. Jedno Issue má mít jednoznačného vlastníka práce v dané fázi.

## 5. Implementation / execution

Pokud Issue vyžaduje implementaci nebo jinou vykonávající změnu, příslušná role:

1. načte povinný kontext,
2. ověří scope,
3. provede pouze změny potřebné pro Issue,
4. průběžně ověřuje výsledek,
5. zaznamená nové nálezy mimo scope bez jejich oportunistické opravy,
6. vytvoří odpovídající auditní stopu změny podle pravidel projektu.

## 6. Independent review

Pokud je pro daný work item předepsané nezávislé review, Reviewer ověří změnu podle [`review-model.md`](review-model.md). Kontroluje především soulad se zadáním, scope, konzistenci a rizika.

Blokující nálezy vrací autorovi. Reviewer je sám neopravuje.

Review-only nebo auditní Issue nezískává další review automaticky jen proto, že samo obsahuje review. Jeho completion se řídí typově specifickými pravidly v [`issue-standard.md`](issue-standard.md).

## 7. Verification / testing

Pokud je pro daný work item předepsané testování nebo nezávislá verifikace, Tester ověří acceptance criteria a relevantní hraniční případy. Výsledek musí být doložitelný.

Pokud najde defekt, popíše očekávané a skutečné chování a předá ho zpět. Produkční kód sám neopravuje.

Pořadí review a testování může být podle typu práce odlišné, ale předepsané kontrolní brány nesmí být vynechány jen kvůli rychlosti.

## 8. Completion

Issue lze uzavřít pouze podle typově specifických completion pravidel v [`issue-standard.md`](issue-standard.md). Workflow samo nepřidává univerzální review nebo testing požadavek ke každému typu práce.

## 9. Handoff contract

Při předání mezi rolemi se nepřenáší soukromý kontext agenta. Předává se pouze stav zachycený v repozitáři, Issue a PR.

Dobré předání musí umožnit následující roli pokračovat bez dotazu typu „co jste vlastně předtím řešili?“.
