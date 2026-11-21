# SICRAT — Sistema Integrado de Controle de Reação e Amortecimento Terminal

**Dossiê de projeto conceitual, versão 4 (novembro de 2026)**  
**Autor e idealizador:** Heitor Mouta Almeida (17 anos, estudante)  
**Apoio:** Raphael Almeida  
**Contato:** [contato]  
**Projeto público e simulador:** [link]  
**Licença:** Projeto aberto, CC BY 4.0 — use livremente, citando a origem.

> Convenção usada em todo o documento: **[F]** fato com fonte citada; **[E]** estimativa dos autores, com a conta mostrada; **[?]** dado a confirmar. Custos são faixas de ordem de grandeza. Este é um projeto conceitual em fase de pesquisa. Elaborado com apoio de ferramentas de IA e revisado pelos autores.

---

## 1. Sumário executivo

**Problema.** A perda de controle em voo (LOC-I) é a principal causa de mortes na aviação comercial: **41% dos acidentes fatais e 55% das mortes a bordo** entre 2015 e 2024 (995 de 1.825) [F, IATA]. Nas aeronaves leves, parafusos, perda de controle e pousos forçados sobre terreno hostil (floresta, rio) seguem sendo grandes riscos. Na Amazônia, o táxi aéreo é muitas vezes o único transporte disponível.

**Solução: SICRAT.** Concebido por Heitor Mouta Almeida e inspirado nos propulsores de gás frio do novo Tesla Roadster (outubro de 2026), o SICRAT combina dois subsistemas que atuam em **pulsos curtos**, sem tentar sustentar a aeronave:

1. **Controle de reação a gás frio (N₂):** recupera atitude e tira a aeronave de parafuso com jatos de guinada e arfagem. Funciona independentemente do ar e é inerte, modulável e recarregável.
2. **Retrofoguetes sólidos de amortecimento terminal:** reduzem a velocidade de descida nos últimos metros antes do toque, no princípio dos motores de pouso suave da Soyuz.

**Alvos prioritários:** aviação geral (Cirrus SR22, Cessna 172), **táxi aéreo amazônico (Cessna 208B Grand Caravan)**, **eVTOL** e **drones de carga**. A aviação comercial é a fase de pesquisa de longo prazo.

**Dimensionamento** [E]:

| Aplicação | Massa | Subsistema terminal | Subsistema de atitude | Massa do sistema |
|---|---|---|---|---|
| SR22 (com CAPS) | 1.633 kg | 5,3 kg de propelente (8→2 m/s) | — | 10–20 kg |
| C172 (com paraquedas BRS) | 1.157 kg | 3,8 kg de propelente | — | 45–60 kg (inclui BRS) |
| eVTOL | 2.500 kg | 8 kg (com paraquedas) a 18 kg (sem) | gás frio leve | 15–40 kg |
| Caravan 208B | 3.900 kg | 13–28 kg de propelente | 124 kg de N₂ a 300 bar | 220–310 kg |
| Drone de carga | 25 kg | 0,1–0,2 kg | — | < 1 kg |

**Custos** [E]: US$ 10–27 mil por SR22, US$ 44–73 mil por C172 (já com BRS), US$ 100–260 mil por Caravan e US$ 15–40 mil por eVTOL instalado de fábrica. Certificação: US$ 0,5–2 mi na aviação geral e US$ 3–10 mi no Caravan.

**Precedentes que mostram que o caminho existe** [F]:

- Motores de pouso suave da Soyuz.
- Cirrus CAPS: 153 salvamentos e 309 sobreviventes; certificado inclusive no jato SF50.
- Foguetes antiparafuso testados pela NASA e no T-28A em 1952.
- Gás frio demonstrado no Tesla Roadster.

---

## 2. Problema e dados

| Fonte | Período | Dado |
|---|---|---|
| IATA | 2015–2024 | 66 acidentes fatais, 1.825 mortes a bordo; LOC-I = 41% dos acidentes fatais e 55% das mortes [F] |
| IATA | 2024 | 7 acidentes fatais; 1 LOC-I (Vinhedo/SP, ATR 72, 62 mortes) [F] |
| Boeing StatSum | 2014–2023 | 706 de 1.078 mortes a bordo em jatos foram LOC-I [F] |
| CENIPA | Voepass 2283 | Parafuso chato por 68 s a ~14.000 ft/min (~71 m/s) [F] |

O caso Vinhedo mostra o cenário-alvo do subsistema de atitude: um **parafuso** do qual os comandos aerodinâmicos não conseguiram tirar a aeronave.

---

## 3. Arquitetura do SICRAT

### 3.1 Princípio: pulsar, não pairar

Manter no ar uma aeronave de 60 t só com propulsores exigiria cerca de 590 kN e cerca de 965 kg/s de gás. Por isso o SICRAT atua **apenas em pulsos de 0,5 a 4 s**, nos momentos críticos, enquanto as asas (ou o paraquedas) continuam sustentando a aeronave [E].

### 3.2 Subsistema A: controle de reação a gás frio

- **Bocais de guinada** nas pontas de asa ou na cauda, para sair de parafusos, e **bocais de arfagem** em binário nariz-cauda, para recuperar atitude.
- **Gás:** nitrogênio seco, inerte e sem risco de fogo, já disponível na infraestrutura de manutenção.
- **Armazenamento:** tanques COPV a 300 bar (N₂ a 302 kg/m³) ou 690 bar (495 kg/m³) [E, CoolProp].
- **Controle:** válvulas eletromagnéticas com modulação PWM e resposta abaixo de 10 ms.
- **Projeto pelo limite de carga:** a taxa de arfagem fica abaixo da que produz 2,5 g, ou seja, cerca de 7°/s a 120 m/s. O sistema recupera a aeronave em segundos e sem sobrecarregar a estrutura [E, 14 CFR 25.337 / Part 23].

**Dimensionamento no Caravan 208B** [E]:

- Inércia de guinada: I_zz ≈ 38.400 kg·m² (método de Roskam).
- Parar uma rotação de 1 rad/s em 2 s exige um momento de 19 kN·m, ou **2,4 kN por bocal** nas pontas de asa (braço de 7,9 m). Para 1,5 rad/s, 3,6 kN.
- **Orçamento de impulso:** guinada de 3 kN por 4 s mais arfagem de 2 kN por 3 s, com margem de 2×, dá 36 kN·s.
- **Gás:** com velocidade de exaustão de 580 m/s (gás resfriado na descarga), são 62 kg de N₂ utilizável. Considerando que 50% do armazenado é aproveitável, são **124 kg armazenados**, ou 410 L a 300 bar.
- **Tanques:** de 50 a 126 kg, conforme a tecnologia de COPV (PV/W de 25 a 10 km).
- **Instalação:** no cargo pod ventral (capacidade de 494 kg [?]), preservando os assentos.

**Precedente** [F]: em 1952, garrafas JATO de 363 kgf nas pontas de asa de um T-28A interromperam parafusos mesmo com os comandos contrários. A NASA usou foguetes de H₂O₂ num avião leve e recuperou parafusos irrecuperáveis em menos de 1 volta.

### 3.3 Subsistema B: retrofoguetes de amortecimento terminal

Fórmulas: a = (v₁² − v₂²)/(2h); F = m·(a + g); t = (v₁ − v₂)/a; I = F·t; mₚ = I/(Isp·g₀), com Isp = 250 s para propelente composto [E].

| Caso | Desacel. | Empuxo | Queima | Impulso | Propelente |
|---|---|---|---|---|---|
| C172 sob paraquedas, 8→2 m/s em 1 m | 3,1 g | 46 kN | 0,20 s | 9,2 kN·s | 3,8 kg |
| SR22 sob CAPS, 8→2 m/s em 1 m | 3,1 g | 65 kN | 0,20 s | 13 kN·s | 5,3 kg |
| eVTOL 2,5 t com paraquedas, 8→2 m/s em 1 m | 3,1 g | 100 kN | 0,20 s | 20 kN·s | 8,1 kg |
| eVTOL 2,5 t sem paraquedas, 15→3 m/s em 5 m | 2,2 g | 79 kN | 0,56 s | 44 kN·s | 17,8 kg |
| Caravan sob paraquedas, 8→2 m/s em 1 m | 3,1 g | 155 kN | 0,20 s | 31 kN·s | 12,7 kg |
| Caravan sem paraquedas, 15→3 m/s em 5 m | 2,2 g | 123 kN | 0,56 s | 68 kN·s | 27,8 kg |

![Propelente por aplicação](fig/prop_v4.png)

- **Ocupantes:** a desaceleração fica entre 2 e 3 g, muito abaixo dos limites de ensaio de assentos (14–16 g, 14 CFR 25.562 / 23.562) [F].
- **Disparo:** a lógica é a da Soyuz (altímetro de raios gama Kaktus: aviso a 15 m e disparo a 0,8 m) [F]. No SICRAT, a altura de disparo é calculada em tempo real: h_ign = v_z² / (2·a_líq), com a_líq = (F + L)/m − g.

### 3.4 Aviônica e lógica (máquina de 3 fases)

- **Hardware:** computador TMR (redundância modular tripla), bateria LiFePO4 de 28 V própria, IMU tripla, radioaltímetro e lidar duplos.
- **Fase 1, guarda de envelope:** acionamento ao detectar "upset" (mais de 25° nariz acima, mais de 10° abaixo ou mais de 45° de inclinação, AC 120-111 [F]) sem resposta dos comandos, com votação 2 de 3 dos sensores ou acionamento manual protegido.
- **Fase 2, conservação:** válvulas fechadas no planeio, reservando gás e propelente para o contato final.
- **Fase 3, ignição terminal:** disparo calculado, armado só em baixa altura e com inibição manual.

### 3.5 Ambiente de operação

- **Ar rarefeito:** a densidade é 74% da do nível do mar a 3 km e 25% a 12 km [F, ISA]. Os jatos não dependem do ar, e o empuxo até aumenta com a altitude.
- **Temperatura:** a −56,5 °C, o propelente sólido é qualificado tipicamente de −54 a +71 °C [?], e os tanques ficam em área aquecida. Na descarga rápida o N₂ esfria, o que já está considerado na velocidade de exaustão de 580 m/s.

### 3.6 Limites de uso: recursos finitos [E]

O SICRAT **não é um sistema de longa duração**. O gás frio dá **alguns segundos de jato no total**, e cada retrofoguete queima **uma única vez, por frações de segundo**. A tabela resume o que cada aeronave tem disponível (calc5.py):

| Aeronave | Impulso de N₂ | Tempo total de jato ≈ pulsos de 0,5 s | Parar 1 rad/s / nº de paradas | Altura mín. para sair de parafuso | Queima do retro (única) | Altura de disparo do retro |
|---|---|---|---|---|---|---|
| Drone de carga 25 kg | 0,1 kN·s (opcional) | 4,0 s ≈ 8 | 0,25 s / ~16,0 | ~37 m (~120 ft) | 0,46 s | ~3 m |
| Cessna 172 | 5,8 kN·s (opcional) | 11,6 s ≈ 23 | 1,49 s / ~7,8 | ~204 m (~670 ft) | 0,20 s | ~1 m |
| Cirrus SR22 | 8,0 kN·s (opcional) | 11,4 s ≈ 22 | 1,59 s / ~7,2 | ~229 m (~750 ft) | 0,20 s | ~1 m |
| eVTOL 2,5 t | 8,0 kN·s (opcional) | 8,0 s ≈ 16 | 1,67 s / ~4,8 | ~164 m (~540 ft) | 0,20 s | ~1 m |
| Cessna 208B Caravan | 36,0 kN·s | 12,0 s ≈ 24 | 1,62 s / ~7,4 | ~320 m (~1050 ft) | 0,20 s | ~1 m |

- **Altura mínima para sair de parafuso:** 1 s de reação + tempo para parar a rotação + arremetida limitada a 2,5 g, com margem de 1,5×. Abaixo dela, o recurso é o paraquedas com retrofoguete.
- **Retrofoguete:** o sensor (lidar/radioaltímetro) acompanha a descida desde cerca de 15 m e dispara na altura indicada. Não há segunda chance: se falhar, o toque acontece na velocidade do paraquedas (cerca de 8 m/s).
- **Tanque vazio:** se o N₂ acabar antes de a rotação parar, o resultado é o mesmo de não ter o sistema. Por isso a lógica de 3 fases economiza gás e o tanque é monitorado (pressão) antes de cada voo.
- O simulador (`sim/index.html`) mostra os tanques esvaziando e o que acontece quando o recurso acaba.

### 3.7 Cenário: superfície de comando travada por gelo [E]

Exemplo: no Caravan, um aileron trava por gelo e passa a produzir um momento de rolagem constante (≈ 3.5 kN·m, adotado para ilustração).

- **Sem ajuda:** com I_xx ≈ 15.122 kg·m², a aeronave passaria de 60° de inclinação em poucos segundos (≈ 3 s sem amortecimento aerodinâmico).
- **Com o SICRAT:** os bocais das pontas de asa (para cima/para baixo) aplicam um momento contrário. Bastam cerca de 443 N por bocal (braço de 7,9 m), enquanto o piloto ajusta leme, potência, velocidade e aproximação em cerca de 15 s. Isso consome ≈ 3.3 kN·s (9% do tanque); com o tanque cheio, o momento poderia ser segurado por ~81 s no máximo.
- **O que o SICRAT não faz:** ele **não remove o gelo** e **não devolve a sustentação**. O gelo pode reduzir o CLmax em cerca de 30% e aumentar o arrasto em cerca de 40% [F/?, FAA], o que eleva a velocidade de estol em cerca de 20% [E]. O sistema **só ganha segundos** para o piloto sair da condição de gelo e pousar.

---

## 4. Segurança e certificação

- **Caminho regulatório:** Part 23 / RBAC 23 com **STC** para retrofit, e **Special Condition** (14 CFR 21.16) para tecnologia nova, como aconteceu com o CAPS do Cirrus SF50 (23-275-SC) [F].
- **Falha crítica: disparo indevido.** Mitigações: votação 2 de 3, arme por altura e razão de descida, inibição manual, iniciadores duplos e detecção de assimetria. Lição histórica: no Credible Sport (C-130, 1980), o disparo manual precoce dos foguetes de frenagem causou um pouso duro [F]. Por isso a lógica é automática e redundante.
- **Gás frio:** TPRD e discos de ruptura com exaustão externa, manta de aramida, telemetria de pressão, ensaio hidrostático a cada 5 anos, sensor de O₂ nos compartimentos (risco de asfixia) e bocais com tampas articuladas.
- **Pirotecnia:** logística de explosivos classe 1.4 da ONU, troca a cada cerca de 10 anos (como o foguete do CAPS) e sinalização para equipes de resgate.

---

## 5. Custos e caso de negócio

### 5.1 Referências de mercado [F]

| Referência | Valor |
|---|---|
| BRS para Cessna 172, instalado | US$ 34.400; 40–60 h; +79 lb (Goodrich / AOPA) |
| Reempacotamento do CAPS (paraquedas + foguete, a cada 10 anos) | US$ 18.500–22.000 (Avias / All In) |
| Certificação | STC de grande porte ≈ US$ 250 mi; TC novo de Part 25 ≈ US$ 1 bi (MITRE para a FAA, 2022) |

### 5.2 Custos por aplicação prioritária [E]

Premissas: mão de obra de US$ 120–180/h, combustível de US$ 0,65–0,90/kg, penalidade de peso de 2,5–4% da massa extra por hora de voo.

| Aplicação | Custo por aeronave | Certificação | Parada | Combustível/ano | Manutenção/ano |
|---|---|---|---|---|---|
| SR22 (retro + CAPS existente) | US$ 10–27 mil | US$ 0,5–2 mi | 3–7 dias | < US$ 100 | US$ 300–900 |
| C172 (BRS + retro) | US$ 44–73 mil | US$ 0,5–2 mi | 5–10 dias | US$ 100–400 | US$ 800–1.500 |
| eVTOL (de fábrica) | US$ 15–40 mil | integrado ao TC do eVTOL | — | — | [?] |
| Caravan 208B (híbrido) | US$ 100–260 mil | US$ 3–10 mi | 5–10 dias | US$ 2–13 mil | US$ 2–6 mil |

![Custo por aeronave](fig/custo_v4.png)

### 5.3 Valor comercial

- **Cirrus:** o SR22 é o avião de aviação geral mais vendido do mundo todos os anos desde 2002–2003, com o CAPS no centro da marca [F, Aviation Week]. O SICRAT acrescenta ao paraquedas o pouso suave final, que hoje acontece a cerca de 9 m/s.
- **Táxi aéreo amazônico:** um diferencial claro para operadores e passageiros em rotas sobre floresta e rio, com um módulo instalável no cargo pod.
- **eVTOL:** as aeronaves de mobilidade aérea urbana voam baixo sobre cidades e têm planeio limitado. Um sistema de paraquedas com retrofoguetes é um argumento forte de certificação e de aceitação pública.
- **Mercado de referência:** 27.150 aviões comerciais em 2024 e 43.600 entregas previstas até 2044 (Boeing CMO 2025) [F], na fase de longo prazo.
- **Riscos a gerenciar:** percepção do público (comunicar o sistema como "airbag da aviação"), responsabilidade por disparo indevido e prazo regulatório.

---

## 6. Fase de longo prazo: aviação comercial

A pesquisa na aviação geral e no Caravan gera os dados de confiabilidade, sensores e lógica que permitem estudar, numa fase posterior, o SICRAT como **atuador de último recurso integrado ao fly-by-wire** de jatos regionais e narrowbodies. Isso cobre situações de baixa pressão dinâmica, como estol profundo e parafuso, e perda de comandos. Ordens de grandeza para essa fase [E]: sistema de 0,8–1,5 t, desenvolvimento de US$ 0,3–1 bi por família e custo unitário de US$ 0,5–1,5 mi em escala.

---

## 7. Roteiro e parceria

| Fase | Prazo | Entrega |
|---|---|---|
| 1. Simulação e demonstrador de bancada | 0–6 meses | Simulador 1D/6DOF aberto; cápsula de 1 kg com jatos de ar comprimido |
| 2. Drone de 5–25 kg (com laboratório parceiro) | 6–18 meses | Queda com paraquedas mais retro; lógica de 3 fases em hardware |
| 3. Aeronave leve (SR22/C172) | 2–4 anos | Módulo retro integrado ao BRS/CAPS; ensaios de queda; caminho de STC |
| 4. Caravan / eVTOL | 3–6 anos | Gás frio antiparafuso em túnel e simulador; protótipo instalado |
| 5. Comercial (pesquisa) | 6+ anos | Estudos com fabricante |

**Contribuições buscadas** (o projeto é aberto; qualquer pessoa pode contribuir):

- **Embraer / Embraer-X:** eVTOL (Eve), voo autônomo e aviação regional.
- **Univap:** Engenharia Aeronáutica e Espaço, com túnel de vento, simulador de voo e pista de aeromodelismo.
- **Universidades (Mauá, FEI, ITA, Univap):** bancada, túnel de vento, câmara fria, TCCs e iniciação científica (IC).

O SICRAT é um **projeto aberto**: dados, contas e desenhos ficam públicos para que qualquer equipe possa construir e melhorar as soluções.

---

## 8. Autoria

**Concepção original do SICRAT:** Heitor Mouta Almeida (17 anos, estudante).  
**Apoio, revisão e organização:** Raphael Almeida.  
Contato: [contato]

**Licença:** Projeto aberto, CC BY 4.0 — use livremente, citando a origem. Texto e desenhos sob CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/deed.pt_BR); código sob licença MIT. O objetivo é salvar vidas e aperfeiçoar a aviação: qualquer pessoa, universidade ou empresa pode usar, adaptar e melhorar o SICRAT.

---

## 9. Referências

1. IATA Safety Report 2024: recomendações. https://www.iata.org/contentassets/95e933e1ad794068812f073cf883cb08/recommendations-for-accident-prevention-2024_final.pdf
2. Boeing Statistical Summary. https://www.boeing.com/content/dam/boeing/v2/company/statsum.pdf
3. Boeing Commercial Market Outlook 2025–2044. https://www.boeing.com/content/dam/boeing/boeingdotcom/market/assets/downloads/2025-commercial-market-outlook.pdf
4. CENIPA, relatório final do PS-VPB. https://sistema.cenipa.fab.mil.br/cenipa/paginas/relatorios/rf/en/RF_PS-VPB_09_08_2024_Eng.PUB..pdf
5. Pouso da Soyuz. https://www.russianspaceweb.com/soyuz-landing.html
6. COPA, histórico de acionamentos do CAPS. https://www.cirruspilots.org/Safety/CAPS-Event-History
7. FAA, Special Conditions do CAPS do SF50. https://www.federalregister.gov/documents/2016/07/15/2016-16813/special-conditions-cirrus-design-corporation-model-sf50-whole-airplane-parachute-recovery-system
8. NASA, Rockets for Spin Recovery. https://ntrs.nasa.gov/api/citations/19800020866/downloads/19800020866.pdf ; NASA, foguetes de H₂O₂: https://ntrs.nasa.gov/citations/19790063866
9. Operation Credible Sport. https://en.wikipedia.org/wiki/Operation_Credible_Sport
10. 14 CFR Part 25. https://www.ecfr.gov/current/title-14/chapter-I/subchapter-C/part-25 ; ANAC RBAC 25: https://www.anac.gov.br/assuntos/legislacao/legislacao-1/rbha-e-rbac/rbac/rbac-25
11. BRS, preços. https://goodrichaviation.com/brs-parachutes ; AOPA: https://www.aopa.org/news-and-media/all-news/2017/october/04/brs-announces-cessna-parachute-installation-network
12. CAPS, preço de reempacotamento. https://aviasfly.com/caps/
13. MITRE para a FAA, custos de certificação. https://airgways.com/wp-content/uploads/2022/06/aw-mitre-report-for-faa-march-2022.pdf
14. Aviation Week, SR22. https://aviationweek.com/business-aviation/aircraft-propulsion/20twenty-cirrus-sr22-perennial-piston-best-seller
15. Tesla Roadster com gás frio. https://www.space.com/technology/spacex-thrusters-just-made-a-tesla-roadster-fly-and-elon-musks-car-is-still-out-there-in-space
16. Mauá, temas de pesquisa (laboratório IMT-Boeing). https://maua.br/img/upload/mechanical-engineering-research-topics-and-projetcs-1712934480.pdf
17. CoolProp. http://www.coolprop.org/
