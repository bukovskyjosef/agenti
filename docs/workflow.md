# Work lifecycle

Tento dokument definuje standardní životní cyklus práce od nejasného záměru po ověřený výsledek.

## 1. Intake

Vstupem může být lidský požadavek, nalezený problém nebo návrh změny.

Orchestrátor nebo analytik zajistí, aby vzniklo GitHub Issue. Práce nesmí dlouhodobě existovat pouze v chatu.

## 2. Analysis

Analytik připraví issue tak, aby bylo jednoznačné:

- proč se práce dělá,
- co je cílem,
- co je ve scope,
- co je explicitně mimo scope,
- jaké kanonické zdroje se použijí,
- jaká pravidla a omezení platí,
- jak se pozná dokončení,
- jaké otázky vyžadují lidské rozhodnutí.

Produktové nejasnosti se řeší před označením práce jako Ready.

## 3. Ready

Issue je Ready pouze tehdy, pokud splňuje [`issue-standard.md`](issue-standard.md).

Ready znamená, že nová kompetentní instance agenta může začít pracovat pouze z repozitáře a issue bez doplňujícího kontextu z chatu.

## 4. Assignment

Orchestrátor určí vykonávající roli a zkontroluje závislosti. Jedno issue má mít jednoznačného vlastníka práce v dané fázi.

## 5. Implementation

Vývojář nebo jiná vykonávající role:

1. načte povinný kontext,
2. ověří scope,
3. provede pouze změny potřebné pro issue,
4. průběžně ověřuje výsledek,
5. zaznamená nové nálezy mimo scope bez jejich oportunistické opravy,
6. vytvoří Pull Request navázaný na issue.

## 6. Independent review

Reviewer nezávisle ověří změnu podle [`review-model.md`](review-model.md). Kontroluje především soulad se zadáním, scope, konzistenci a rizika.

Blokující nálezy vrací autorovi. Reviewer je sám neopravuje.

## 7. Verification / testing

Tester nezávisle ověří acceptance criteria a relevantní hraniční případy. Výsledek musí být doložitelný.

Pokud najde defekt, popíše očekávané a skutečné chování a předá ho zpět. Produkční kód sám neopravuje.

Pořadí review a testování může být podle typu práce odlišné, ale požadované kontrolní brány nesmí být vynechány jen kvůli rychlosti.

## 8. Completion

Issue může být uzavřeno pouze tehdy, pokud:

- acceptance criteria jsou splněna,
- požadované review a testování proběhlo,
- blokující nálezy jsou vyřešeny,
- relevantní kanonická dokumentace byla aktualizována,
- nevznikl skrytý nový produktový požadavek,
- navazující problémy mimo scope jsou samostatně zaznamenané.

## 9. Handoff contract

Při předání mezi rolemi se nepřenáší soukromý kontext agenta. Předává se pouze stav zachycený v repozitáři, issue a PR.

Dobré předání musí umožnit následující roli pokračovat bez dotazu typu „co jste vlastně předtím řešili?“.
