# Independent review model

Cílem review není vytvořit druhou implementaci ani redesignovat řešení podle vkusu reviewera. Cílem je nezávisle ověřit, že změna je správná, úplná, přiměřená a zůstala uvnitř schváleného scope.

## 1. Nezávislost

Autor změny nesmí být jejím nezávislým reviewerem. Reviewer má pracovat z issue, PR a kanonické dokumentace, nikoli z neveřejného kontextu autora.

## 2. Pořadí kontroly

Reviewer kontroluje zejména:

1. **Scope:** změna řeší právě schválený problém a nepřidává nesouvisející úpravy.
2. **Requirements:** implementace odpovídá autoritativním požadavkům a rozhodnutím.
3. **Acceptance criteria:** existuje důkaz, že jsou splněná.
4. **Konzistence:** změna nevytváří rozpor s jinými částmi systému nebo dokumentace.
5. **Technická kvalita:** řešení je přiměřeně jednoduché, udržovatelné a neobsahuje zjevné vady.
6. **Testovatelnost a důkazy:** uvedené testy a validace skutečně podporují tvrzení autora.
7. **Dokumentace:** kanonické dokumenty byly změněny tam, kde se změnila trvalá pravda projektu.

## 3. Typy nálezů

### Blocking
Změna nesplňuje požadavek, acceptance criterion, bezpečnostní nebo zásadní technické pravidlo, případně překročila scope tak, že nemá být sloučena.

### Non-blocking
Doporučení, zlepšení nebo budoucí práce, která není nutná pro splnění současného issue.

Reviewer nesmí označit osobní preferenci za blocking bez vazby na konkrétní požadavek, riziko nebo normativní pravidlo.

## 4. Způsob opravy

Reviewer popíše problém, důvod a očekávaný stav. Opravu provádí autor nebo jiná explicitně přiřazená kompetentní role.

Reviewer nesmí při review tiše opravovat kontrolovaný kód, protože tím zaniká oddělení autora a kontroly.

## 5. Tester versus reviewer

Reviewer a tester nejsou totožné funkce:

- reviewer kontroluje správnost změny jako změny,
- tester ověřuje chování výsledného systému proti acceptance criteria a relevantním scénářům.

U malého nebo nízkorizikového úkolu může proces explicitně povolit sloučení těchto kontrol do jedné agentní role, ale nesmí se z toho stát implicitní výchozí stav pro významné změny.

## 6. Review completion

Review je dokončeno, pokud:

- všechny blocking nálezy byly vyřešeny nebo explicitně rozhodnuty člověkem,
- reviewer znovu ověřil opravený stav,
- zbývající non-blocking body jsou podle potřeby převedeny do samostatných issues,
- reviewer může odkázat na konkrétní důkazy pro své závěry.

Dokončené review se **nereviewuje znovu pouze proto, že je samo pracovním Issue nebo review artefaktem**. Další nezávislá kontrola review vzniká jen tehdy, pokud ji explicitně požaduje pracovní kontrakt nebo jiné platné pravidlo. Typově specifická completion pravidla vlastní [`issue-standard.md`](issue-standard.md).
