# Adoption guide

Tento dokument popisuje, jak použít principy repozitáře `agenti` v reálném projektu.

## 1. Nevytvářej druhý systém pravdy

Při adopci nejprve zjisti, kde projekt již drží požadavky, dokumentaci, rozhodnutí a pracovní úkoly. Nový agentní model má existující informace konsolidovat, ne k nim přidat paralelní kopii.

## 2. Zaveď minimální kostru

Každý agentně řízený projekt by měl mít alespoň:

- `README.md` pro člověka,
- `AGENTS.md` jako vstupní bod pro agenta,
- mapu kanonické dokumentace,
- explicitní role a kompetence,
- workflow práce,
- standard GitHub Issue/work contract,
- pravidla review a testování,
- durable handoff protokol,
- místo pro významná rozhodnutí,
- issue a PR šablony odpovídající procesu,
- explicitní branch/integration authority,
- strojově spustitelný governance consistency check, pokud je proces stabilní.

Názvy a umístění lze přizpůsobit projektu, význam nikoli.

## 3. Přizpůsob kontextovou mapu

Agent nesmí pro každý úkol číst všechno. Do projektu proto doplň mapu, která odpoví:

- co čte každý agent vždy,
- co čte konkrétní role,
- kde jsou produktové požadavky,
- kde je architektura,
- kde jsou business pravidla,
- kde jsou API nebo datové kontrakty,
- kde jsou rozhodnutí,
- kde jsou testovací pravidla,
- kde je durable handoff předchozí role.

## 4. Vyčisti duplicity

Před autonomnější prací agentů odstraň nebo označ:

- staré specifikace konkurující aktuálním,
- duplicitní README/agent instrukce,
- pravidla ukrytá pouze v issues,
- dokumenty bez jasného statusu,
- historické soubory v běžné kontextové cestě,
- provider-specific instrukce, které fakticky přepisují obecnou governance.

Autonomie agentů zesiluje nejen dobrý pořádek, ale i existující nekonzistence.

## 5. Zaveď role

Cílový model typicky používá:

- Orchestrátora,
- Analytika,
- Asistentku pro lidské decision gates,
- Vývojáře / vykonávající roli,
- Reviewera,
- Testera/Verifiera tam, kde je gate potřeba,
- Integrátora pro merge/promotion.

Projekt může přidat další specializace, pokud mají skutečně odlišnou odpovědnost a pravomoci. Role nevytvářej pouze podle názvu technologie; vytvářej je podle odpovědnosti.

## 6. Přesuň úkoly do Issues

Nová práce má vznikat jako Issue a postupně dozrát do Ready. Před Ready musí mít explicitní dependencies, concurrency class, shared surfaces, decision gates a required control gates podle [`issue-standard.md`](issue-standard.md).

Pokud práce začíná v chatu, relevantní kontext a rozhodnutí se před zahájením realizace přenesou do GitHubu.

## 7. Zaveď durable handoff dříve než automatizaci

Nejdřív zajisti, aby role uměly správně předávat práci bez člověka jako message bus:

- implementer → PR,
- Reviewer → PR review,
- Tester → PR/test report,
- Orchestrátor/Analytik/Asistentka → Issue/decision artefakt,
- Integrátor → integration evidence.

Teprve když tento tok spolehlivě funguje ručně, má smysl jeho části automaticky spouštět.

## 8. Odděl autora, kontrolu a integraci

Změna má vzniknout v izolovaném pracovním prostoru/branchi podle politiky projektu, být ověřena jinou rolí a až poté integrována rolí, která zkontroluje gate evidence.

V malém projektu může stejný člověk technicky vykonávat více rolí v různých okamžicích, ale jedna logická instance agentní práce nesmí být současně autorem a nezávislým reviewerem své změny.

## 9. Zaveď concurrency model

Pro každý Ready task určuj:

- `PARALLEL_SAFE`,
- `COORDINATION_REQUIRED`,
- nebo `EXCLUSIVE`.

Uveď shared surfaces a merge/ownership rule. Tím lze paralelizovat různé úkoly bez toho, aby několik agentů nekontrolovaně měnilo stejný kontrakt.

## 10. Automatizuj Orchestrátora jako první

První vhodný automatizační krok je obvykle Coordinator/Orchestrator:

- trigger ho probudí,
- agent znovu načte authoritative GitHub/repo state,
- provede pouze další governance-authorized krok,
- zapíše durable výsledek,
- při decision gate vytvoří/předá rozhodovací artefakt a zastaví,
- při technickém selhání zanechá durable blocker.

Nepřidávej implementační oprávnění pouze proto, že workflow používá stejného providera nebo token.

## 11. Provider adapters drž pod governance

Pokud projekt používá konkrétní nástroj, může mít například `CLAUDE.md`, Codex instrukce nebo IDE rules.

Adapter:

- mapuje obecné role na konkrétní nástroje,
- optimalizuje startup a příkazy,
- ale nesmí redefinovat workflow nebo autoritu.

Při změně providera má obecný model zůstat použitelný.

## 12. Automatizuj postupně

Doporučené pořadí:

1. durable handoff a jasné work contracts,
2. governance checker/CI,
3. automatický Orchestrátor,
4. automatické spouštění vykonávajících rolí,
5. automatické review/test triggery,
6. integrace/promotion po doložených gates.

Každá úroveň autonomie musí zachovat least privilege, idempotence/concurrency ochranu a human decision interrupts podle [`automation-model.md`](automation-model.md).

## 13. Branch strategie je projektová konfigurace

Nepřebírej slepě `develop/main` nebo jiný konkrétní model. Projekt musí pouze explicitně definovat:

- autoritativní/integration branch,
- task branch pravidlo,
- PR target,
- integration/promotion roli,
- required gates před merge.

## 14. Test adopce

Projekt je připravený pro agentní práci, pokud můžeš nové instanci agenta říct pouze:

> Pracuj na issue #N v roli X. Řiď se repozitářem.

a agent dokáže bez dalšího neveřejného kontextu správně určit, co má dělat, co dělat nesmí, kde získat podklady, kam zapsat durable handoff a jak prokázat dokončení.

Pokročilý test cílového stavu je, že běžný task projde mezi rolemi bez ručního kopírování reportů člověkem a člověk je vyžádán pouze na skutečném product/governance decision gate.
