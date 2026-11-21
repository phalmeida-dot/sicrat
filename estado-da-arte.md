# SICRAT — Estado da arte e originalidade

**Autor e idealizador do SICRAT:** Heitor Mouta Almeida · **Apoio:** Raphael Almeida  
**Licença:** Projeto aberto, CC BY 4.0 — use livremente, citando a origem.

Levantamento feito em 21 nov. 2026 no Google Patents, no FreePatentsOnline (espelho de patentes alemãs e europeias), no servidor técnico da NASA (NTRS) e em fontes jornalísticas e institucionais. As citações seguem a ABNT NBR 10520:2023 (sistema autor-data) e as referências completas estão ao final, conforme a ABNT NBR 6023:2018.

## 1. O que já existe

| Tema | Anterioridade | O que faz | Como o SICRAT se diferencia |
|---|---|---|---|
| Paraquedas de aeronave inteira | Popov (1986); Cirrus CAPS (COPA, 2026; Estados Unidos, 2016) | Foguete ou carga extrai um paraquedas que desce a aeronave inteira. | O SICRAT **usa** esse paraquedas como etapa e acrescenta controle de atitude e amortecimento final. |
| Paraquedas com foguete de tração forte | Popov e Popov (2023) | Foguete de dois estágios; o 2º estágio pode ter empuxo maior que o peso da aeronave para frear a queda livre, puxando pelo paraquedas. | No SICRAT o freio final é um retrofoguete na própria aeronave, acionado perto do solo. |
| Paraquedas + retrofoguete no toque | Soyuz (Zak, [20--]); sistema PRSM-915 "Reaktavr", 1976 (Vasily…, 2026; Armor…, [20--]) | Paraquedas único e motores de pouso suave acionados por sondas perto do solo. | **O princípio não é novo.** O SICRAT o aplica a aviões leves que já têm paraquedas certificado (CAPS/BRS), com dimensionamento de 8→2 m/s. |
| Foguetes que freiam a aeronave perto do solo | Allen (1987) | Foguetes voltados para baixo no helicóptero, disparados por sensor de proximidade. | O SICRAT associa o freio a um paraquedas e a um subsistema separado de atitude. |
| Paraquedas + foguetes para manter a atitude | Schubert (2000) | Paraquedas principal e de frenagem; foguetes de direção mantêm a fuselagem nivelada e evitam rolamento na descida. | Anterioridade próxima da ideia de "corrigir a atitude com jatos durante a descida". O SICRAT usa gás frio pulsado e recarregável, também **antes** do paraquedas (parafuso). |
| Foguetes para reorientar **e** frear + paraquedas | Groden e Adler (2018; 2021), SkyRyse | Subsistema balístico com foguetes (inclusive retrofoguetes) para reorientar e/ou desacelerar o veículo antes do impacto, com paraquedas. Foco em helicópteros. | **É a anterioridade mais próxima.** O SICRAT separa as funções: gás frio N₂ (inerte, muitos pulsos) para atitude e retro sólido de queima única para o toque, com foco em asa fixa e táxi aéreo. |
| Foguetes antiparafuso | O'Bryan, Glover e Edwards (1979); Whipple (1980); Lucy (1985) | Foguetes de H₂O₂ ou sólidos na ponta da asa, testados pela NASA para tirar aviões leves de parafuso. | O SICRAT troca foguetes de uso único por pulsos de gás frio recarregável e soma o amortecimento final. |
| Controle de reação em aeronaves | X-15: Jarvis e Lock (1965); Harrier/Kestrel (Smithsonian Institution, [20--]) | Jatos de H₂O₂ (X-15) e de ar sangrado do motor (Harrier) controlam a atitude onde as superfícies não funcionam. | O SICRAT usa tanque de N₂ independente do motor, como reserva de emergência por poucos segundos. |
| Gás frio em veículo | Tesla Roadster (Wall, 2026) | Propulsores de gás frio em um carro. | Inspiração direta do Heitor; o SICRAT leva o conceito para a segurança de voo. |
| Cabine destacável | Giannakopoulos (2003); Tatarenko, 2016 (Atkin, 2016; Morvan, [2016]); Xia, Liao e Zhou (2022); Sandrapaty (2024); Laudrain (2015), Airbus, só para embarque | Separar a cabine e descê-la de paraquedas. | O SICRAT **não** separa a cabine: mantém a aeronave inteira, o que evita a massa e a complexidade estrutural criticadas nesses conceitos. |
| Airbags | Erickson (2017); Clarke (2021), Sikorsky; Park (2025) | Airbags para drones, VTOL e helicópteros. | Complementares; podem somar-se ao retro. |
| Recuperação automática por software | Zhu e Zhao (2022) | Piloto automático com modos de prevenção e recuperação de perda de controle. | O SICRAT pode usar lógica semelhante, mas acrescenta um atuador que não depende das superfícies de comando. |

## 2. Conclusão sobre a originalidade

**Não é novo:** o paraquedas de aeronave inteira; o retrofoguete sob paraquedas (Soyuz, PRSM-915); foguetes que freiam a aeronave perto do solo; foguetes antiparafuso; controle de reação em aeronaves; e a ideia de combinar foguetes de reorientação, frenagem e paraquedas (Schubert, 2000; Groden; Adler, 2018).

**Parece original, dentro dos limites desta busca:**

1. A **arquitetura híbrida específica**: gás frio N₂ pulsado e recarregável para atitude e parafuso, mais retro sólido de queima única só no toque, integrada a paraquedas já certificados (CAPS/BRS) na aviação geral e no táxi aéreo amazônico.
2. O uso dos jatos de gás frio como **torque de atitude temporário quando uma superfície de comando trava por gelo**. Não encontramos publicação com essa proposta.
3. O **dimensionamento aberto com orçamento de recursos explícito** (segundos de jato, número de pulsos, altura mínima, janela de disparo) por aeronave.

A contribuição do SICRAT é de **integração e aplicação**, não um princípio físico novo. Isso é normal e valioso em engenharia de segurança: a maior parte dos avanços vem de combinar soluções conhecidas de um jeito que caiba no avião e na operação.

**Limites desta busca:** palavras-chave em inglês e português; a base do INPI não oferece links permanentes e não foi consultada de forma sistemática; Google Scholar e a biblioteca da AIAA não foram varridos por completo; documentos chineses e russos foram lidos por resumo ou tradução automática; não encontramos fonte primária verificável sobre sistemas chineses de lançamento aéreo com retrofoguete. Este levantamento **não é parecer jurídico** de patenteabilidade nem de liberdade de operação: algumas patentes citadas (por exemplo, as da SkyRyse) podem estar em vigor, e quem for fabricar um produto deve verificar isso. A publicação aberta do SICRAT torna a ideia pública, mas não dá licença sobre patentes de terceiros.

## Referências

Referências conforme a ABNT NBR 6023:2018. Patentes com dados do Google Patents ou do FreePatentsOnline.

AGÊNCIA NACIONAL DE AVIAÇÃO CIVIL (Brasil). **RBAC nº 25**: requisitos de aeronavegabilidade: aviões categoria transporte. Brasília, DF: ANAC, [20--]. Disponível em: https://www.anac.gov.br/assuntos/legislacao/legislacao-1/rbha-e-rbac/rbac/rbac-25. Acesso em: 21 nov. 2026.

ALLEN, Sebree J. **Aircraft emergency landing system**. Depositante: Sebree J. Allen. US 4676457 A. Depósito: 21 jun. 1984. Concessão: 30 jun. 1987. Disponível em: https://patents.google.com/patent/US4676457A/en. Acesso em: 21 nov. 2026.

"ARMOR" airborne assault. **Military Review**, [s. l.], [20--]. Disponível em: https://military-review.com/12517033-armor-airborne-assault. Acesso em: 21 nov. 2026.

ATKIN, Charlie. This new invention could save your life during a plane crash. **The Independent**, London, 2016. Disponível em: https://www.independent.co.uk/travel/detachable-cabin-invented-to-save-lives-during-plane-crashes-a6814311.html. Acesso em: 21 nov. 2026.

AVIASFLY. **CAPS**: Cirrus Airframe Parachute System. [S. l.]: Aviasfly, [20--]. Disponível em: https://aviasfly.com/caps/. Acesso em: 21 nov. 2026.

AVIATION WEEK. 20Twenty: Cirrus SR22, perennial piston best-seller. **Aviation Week**, [s. l.], [20--]. Disponível em: https://aviationweek.com/business-aviation/aircraft-propulsion/20twenty-cirrus-sr22-perennial-piston-best-seller. Acesso em: 21 nov. 2026.

BELL, Ian H.; WRONSKI, Jorrit; QUOILIN, Sylvain; LEMORT, Vincent. Pure and pseudo-pure fluid thermophysical property evaluation and the open-source thermophysical property library CoolProp. **Industrial & Engineering Chemistry Research**, Washington, DC, v. 53, n. 6, p. 2498-2508, 2014. Disponível em: http://www.coolprop.org/. Acesso em: 21 nov. 2026.

BOEING. **Commercial market outlook 2025–2044**. Seattle: Boeing, 2025. Disponível em: https://www.boeing.com/content/dam/boeing/boeingdotcom/market/assets/downloads/2025-commercial-market-outlook.pdf. Acesso em: 21 nov. 2026.

BOEING. **Statistical summary of commercial jet airplane accidents**: worldwide operations. Seattle: Boeing, [2025]. Disponível em: https://www.boeing.com/content/dam/boeing/v2/company/statsum.pdf. Acesso em: 21 nov. 2026.

BRASIL. Comando da Aeronáutica. Centro de Investigação e Prevenção de Acidentes Aeronáuticos. **Relatório final**: PS-VPB, 9 ago. 2024. Brasília, DF: CENIPA, [2025]. Disponível em: https://sistema.cenipa.fab.mil.br/cenipa/paginas/relatorios/rf/en/RF_PS-VPB_09_08_2024_Eng.PUB..pdf. Acesso em: 21 nov. 2026.

CIRRUS OWNERS AND PILOTS ASSOCIATION. **CAPS event history**. [S. l.]: COPA, 2026. Disponível em: https://www.cirruspilots.org/Safety/CAPS-Event-History. Acesso em: 21 nov. 2026.

CLARKE, Charles W. **Airbag systems**. Depositante: Sikorsky Aircraft Corporation. US 11155354 B2. Depósito: 9 out. 2017. Concessão: 26 out. 2021. Disponível em: https://patents.google.com/patent/US11155354B2/en. Acesso em: 21 nov. 2026.

ERICKSON, Alan Jamal. **Inflatable parachute airbag system**. Depositante: Indemnis Inc. US 9611045 B2. Depósito: 10 set. 2015. Concessão: 4 abr. 2017. Disponível em: https://patents.google.com/patent/US9611045B2/en. Acesso em: 21 nov. 2026.

ESTADOS UNIDOS. Federal Aviation Administration. Special conditions: Cirrus Design Corporation Model SF50 airplane; whole-airplane parachute recovery system. **Federal Register**, Washington, DC, 15 jul. 2016. Disponível em: https://www.federalregister.gov/documents/2016/07/15/2016-16813/special-conditions-cirrus-design-corporation-model-sf50-whole-airplane-parachute-recovery-system. Acesso em: 21 nov. 2026.

ESTADOS UNIDOS. **Code of Federal Regulations**: title 14, chapter I, subchapter C, part 25: airworthiness standards: transport category airplanes. Washington, DC: eCFR, 2026. Disponível em: https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25. Acesso em: 21 nov. 2026.

GIANNAKOPOULOS, Pavlos. **An aircraft with a detachable passenger escape cabin and an aircraft with airbags**. Depositante: Pavlos Giannakopoulos. EP 1280699 B1. Depósito: 23 nov. 2000. Concessão: 5 nov. 2003. Disponível em: https://patents.google.com/patent/EP1280699B1/en. Acesso em: 21 nov. 2026.

GOODRICH AVIATION. **BRS parachutes**. [S. l.]: Goodrich Aviation, [20--]. Disponível em: https://goodrichaviation.com/brs-parachutes. Acesso em: 21 nov. 2026.

GRODEN, Mark; ADLER, Mitch. **Safety system for aerial vehicles and method of operation**. Depositante: SkyRyse Inc. US 10004652 B1. Depósito: 23 fev. 2018. Concessão: 26 jun. 2018. Disponível em: https://patents.google.com/patent/US10004652B1/en. Acesso em: 21 nov. 2026.

GRODEN, Mark; ADLER, Mitch. **Safety system for aerial vehicles and method of operation**. Depositante: SkyRyse Inc. US 11103392 B2. Depósito: 9 dez. 2019. Concessão: 31 ago. 2021. Disponível em: https://patents.google.com/patent/US11103392B2/en. Acesso em: 21 nov. 2026.

INSTITUTO MAUÁ DE TECNOLOGIA. **Mechanical engineering research topics and projects**. São Caetano do Sul: IMT, 2024. Disponível em: https://maua.br/img/upload/mechanical-engineering-research-topics-and-projetcs-1712934480.pdf. Acesso em: 21 nov. 2026.

INTERNATIONAL AIR TRANSPORT ASSOCIATION. **Recommendations for accident prevention**: 2024. Montreal: IATA, [2025]. Disponível em: https://www.iata.org/contentassets/95e933e1ad794068812f073cf883cb08/recommendations-for-accident-prevention-2024_final.pdf. Acesso em: 21 nov. 2026.

JARVIS, C. R.; LOCK, W. P. **Operational experience with the X-15 reaction control and reaction augmentation systems**. Washington, DC: NASA, 1965. (NASA Technical Note). Disponível em: https://ntrs.nasa.gov/api/citations/19650016124/downloads/19650016124.pdf. Acesso em: 21 nov. 2026.

LAUDRAIN, Yann-Henri. **Method for boarding and unloading of passengers of an aircraft with reduced immobilization time of the aircraft, aircraft and air terminal for its implementation**. Depositante: Airbus Operations SAS. US 9193460 B2. Depósito: 28 fev. 2013. Concessão: 24 nov. 2015. Disponível em: https://patents.google.com/patent/US9193460B2/en. Acesso em: 21 nov. 2026.

LUCY, M. H. **Miniature rocket motor for aircraft stall/spin recovery**. Washington, DC: NASA, 1985. (NASA Tech Brief). Disponível em: https://ntrs.nasa.gov/citations/19850000253. Acesso em: 21 nov. 2026.

MATHEWSON, George A. **Safety device for disabled airplanes**. Depositante: George A. Mathewson. US 3622108 A. Depósito: 27 fev. 1970. Concessão: 23 nov. 1971. Disponível em: https://patents.google.com/patent/US3622108A/en. Acesso em: 21 nov. 2026.

MITRE CORPORATION. **[Relatório da MITRE para a FAA sobre custos de certificação]**. McLean: MITRE, mar. 2022. Disponível em: https://airgways.com/wp-content/uploads/2022/06/aw-mitre-report-for-faa-march-2022.pdf. Acesso em: 21 nov. 2026.

MORVAN, Hervé. Why a detachable cabin probably won't save your life in a plane crash. **The Conversation**, [s. l.], [2016]. Disponível em: https://theconversation.com/why-a-detachable-cabin-probably-wont-save-your-life-in-a-plane-crash-53532. Acesso em: 21 nov. 2026.

O'BRYAN, T. C.; GLOVER, K. E.; EDWARDS, T. E. **Some results from the use of a control augmentation system to study the developed spin of a light plane**. [S. l.]: NASA, 1979. Trabalho de conferência. Disponível em: https://ntrs.nasa.gov/citations/19790063866. Acesso em: 21 nov. 2026.

OPERATION Credible Sport. In: WIKIPEDIA: the free encyclopedia. [San Francisco: Wikimedia Foundation], 2026. Disponível em: https://en.wikipedia.org/wiki/Operation_Credible_Sport. Acesso em: 21 nov. 2026.

PARK, Yubin. **Drone with stable landing and shock absorbing function**. Depositante: Yubin Park. US 12246862 B1. Depósito: 30 jan. 2024. Concessão: 11 mar. 2025. Disponível em: https://patents.google.com/patent/US12246862B1/en. Acesso em: 21 nov. 2026.

POPOV, Boris. **Ballistic recovery system**. Depositante: Ballistic Recovery Systems Inc. US 4607814 A. Depósito: 13 out. 1983. Concessão: 26 ago. 1986. Disponível em: https://patents.google.com/patent/US4607814A/en. Acesso em: 21 nov. 2026.

POPOV, Boris; POPOV, Urik. **Aircraft emergency parachute deployment system**. Depositante: Boris Popov; Urik Popov. US 11807370 B2. Depósito: 23 jun. 2021. Concessão: 7 nov. 2023. Disponível em: https://patents.google.com/patent/US11807370B2/en. Acesso em: 21 nov. 2026.

SANDRAPATY, Vivek. **Dynamic parachute reefing system for aircraft module**. Depositante: Vivek Sandrapaty. US 2024/0228047 A1. Depósito: 1 fev. 2024. Publicação: 11 jul. 2024. Disponível em: https://patents.google.com/patent/US20240228047A1/en. Acesso em: 21 nov. 2026.

SCHUBERT, Werner. **Emergency parachute for aircraft has main and braking parachutes and steering rockets to position fuselage**. Depositante: Werner Schubert. DE 19854410 C1. Depósito: 16 nov. 1998. Publicação: 16 mar. 2000. Disponível em: https://www.freepatentsonline.com/DE19854410.html. Acesso em: 21 nov. 2026.

SMITHSONIAN INSTITUTION. National Air and Space Museum. **Hawker Siddeley XV-6A Kestrel FGA Mk. 1**. Washington, DC: NASM, [20--]. Disponível em: https://airandspace.si.edu/collection-objects/hawker-siddeley-xv-6a-kestrel-fga-mk-1/nasm_A19740943000. Acesso em: 21 nov. 2026.

VASILY Margelov. In: WIKIPEDIA: the free encyclopedia. [San Francisco: Wikimedia Foundation], 2026. Disponível em: https://en.wikipedia.org/wiki/Vasily_Margelov. Acesso em: 21 nov. 2026.

WALL, Mike. SpaceX thrusters just made a Tesla Roadster 'fly' (and Elon Musk's car is still out there in space). **Space.com**, [s. l.], 16 out. 2026. Disponível em: https://www.space.com/technology/spacex-thrusters-just-made-a-tesla-roadster-fly-and-elon-musks-car-is-still-out-there-in-space. Acesso em: 21 nov. 2026.

WHIPPLE, R. D. **Rockets for spin recovery**. Hampton: NASA, 1980. (NASA Contractor Report). Disponível em: https://ntrs.nasa.gov/api/citations/19800020866/downloads/19800020866.pdf. Acesso em: 21 nov. 2026.

XIA, Qingyuan; LIAO, Hui; ZHOU, Lei. **An eVTOL manned unmanned aerial vehicle separation parachute emergency escape system**. Depositante: Nanjing Lihang Intelligent Technology Co., Ltd. CN 114248927 A. Depósito: 13 jan. 2022. Publicação: 29 mar. 2022. Disponível em: https://patents.google.com/patent/CN114248927A/en. Acesso em: 21 nov. 2026.

ZAK, Anatoly. **Soyuz landing**. [S. l.]: RussianSpaceWeb, [20--]. Disponível em: https://www.russianspaceweb.com/soyuz-landing.html. Acesso em: 21 nov. 2026.

ZHU, Jianchao; ZHAO, Yue. **Loss-of-control prevention and recovery flight controller**. Depositante: Ohio University. US 11360491 B2. Depósito: 21 mar. 2018. Concessão: 14 jun. 2022. Disponível em: https://patents.google.com/patent/US11360491B2/en. Acesso em: 21 nov. 2026.


---

## Prior art and novelty (English summary)

Search carried out on 21 Nov 2026 in Google Patents, FreePatentsOnline (mirror of German and European patents), NASA's technical server (NTRS) and press and institutional sources. Full references (ABNT) are listed above.

### 1. What already exists

| Topic | Prior art | What it does | How SICRAT differs |
|---|---|---|---|
| Whole-aircraft parachutes | Popov, US 4,607,814 (1986); Cirrus CAPS | A rocket or charge extracts a parachute that lowers the whole aircraft. | SICRAT **uses** that parachute as a stage and adds attitude control and final cushioning. |
| Parachute with high-thrust rocket | Popov & Popov, US 11,807,370 (2023) | Two-stage rocket; the 2nd stage may exceed aircraft weight to slow free fall, pulling through the parachute. | In SICRAT the final brake is a retro-rocket on the aircraft itself, fired near the ground. |
| Parachute + retro-rocket at touchdown | Soyuz; Soviet PRSM-915 "Reaktavr" (1976) | Single canopy and soft-landing motors fired by ground probes. | **The principle is not new.** SICRAT applies it to light aircraft that already carry certified parachutes (CAPS/BRS), sized for 8→2 m/s. |
| Rockets braking an aircraft near the ground | Allen, US 4,676,457 (1987) | Downward rockets on a helicopter, fired by a proximity sensor. | SICRAT pairs the brake with a parachute and a separate attitude subsystem. |
| Parachute + rockets holding attitude | Schubert, DE 19854410 C1 (2000) | Main and braking parachutes; steering rockets keep the fuselage level and prevent roll during descent. | Close prior art for "correcting attitude with jets during descent". SICRAT uses pulsed, refillable cold gas, also **before** the parachute (spin). |
| Rockets to reorient **and** decelerate + parachute | Groden & Adler (SkyRyse), US 10,004,652 (2018), US 11,103,392 (2021) | Ballistic subsystem with rockets (including retro-rockets) to reorient and/or decelerate the vehicle before impact, plus parachute; helicopter focus. | **Closest prior art.** SICRAT splits the jobs: inert N₂ cold gas (many pulses) for attitude, single-shot solid retro for touchdown, focused on fixed-wing and air taxi. |
| Spin-recovery rockets | NASA: O'Bryan et al. (1979); Whipple (1980); Lucy (1985) | Wingtip H₂O₂ or solid rockets tested to recover light aircraft from spins. | SICRAT replaces single-use rockets with refillable cold-gas pulses and adds terminal cushioning. |
| Reaction control on aircraft | X-15 (Jarvis & Lock, 1965); Harrier/Kestrel | H₂O₂ jets (X-15) and engine bleed air (Harrier) control attitude where surfaces don't work. | SICRAT uses an engine-independent N₂ tank as an emergency reserve for a few seconds. |
| Cold gas on a vehicle | Tesla Roadster (Wall, 2026) | Cold-gas thrusters on a car. | Heitor's direct inspiration; SICRAT brings it to flight safety. |
| Detachable cabins | Giannakopoulos, EP 1280699 B1 (2003); Tatarenko (2016); Xia et al., CN 114248927 A (2022); Sandrapaty, US 2024/0228047 A1; Airbus US 9,193,460 (boarding only) | Separate the cabin and lower it by parachute. | SICRAT does **not** separate the cabin; the aircraft stays whole, avoiding the mass and structural complexity criticised in these concepts. |
| Airbags | Indemnis US 9,611,045 (2017); Sikorsky US 11,155,354 (2021); Park US 12,246,862 (2025) | Airbags for drones, VTOL and helicopters. | Complementary; can be combined with the retro. |
| Automatic recovery in software | Zhu & Zhao (Ohio University), US 11,360,491 (2022) | Autopilot with loss-of-control prevention and recovery modes. | SICRAT can use similar logic but adds an actuator independent of the control surfaces. |

### 2. Novelty assessment

**Not new:** whole-aircraft parachutes; retro-rockets under a parachute (Soyuz, PRSM-915); rockets braking an aircraft near the ground; spin-recovery rockets; reaction control on aircraft; and combining reorientation rockets, braking and parachute (Schubert 2000; SkyRyse 2018).

**Appears original, within the limits of this search:**

1. The **specific hybrid architecture**: pulsed, refillable N₂ cold gas for attitude and spin, plus a single-shot solid retro only at touchdown, integrated with already-certified parachutes (CAPS/BRS) in general aviation and Amazon air taxi.
2. Using cold-gas jets as **temporary attitude torque when a control surface is jammed by ice**. We found no publication proposing this.
3. **Open sizing with an explicit resource budget** (seconds of jet, number of pulses, minimum height, firing window) per aircraft.

SICRAT's contribution is **integration and application**, not a new physical principle — which is normal and valuable in safety engineering.

**Search limits:** English and Portuguese keywords; the INPI database has no permanent links and was not searched systematically; Google Scholar and the AIAA library were not fully covered; Chinese and Russian documents were read via abstracts or machine translation; no verifiable primary source was found on Chinese retro-rocket airdrop systems. This is **not a legal opinion** on patentability or freedom to operate: some cited patents (e.g. SkyRyse) may be in force, and anyone building a product should check. Publishing SICRAT openly makes the idea public but grants no licence under third-party patents.
