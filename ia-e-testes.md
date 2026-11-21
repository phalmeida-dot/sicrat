# SICRAT — IA e testes para acelerar com segurança

**Autor e idealizador do SICRAT:** Heitor Mouta Almeida · **Apoio:** Raphael Almeida  
**Licença:** Projeto aberto, CC BY 4.0 — use livremente, citando a origem.

A ideia é fazer a maior parte das tentativas e erros **no computador e em escala pequena**, e reservar os ensaios caros e perigosos para o que já foi bem filtrado. Ferramentas gratuitas e abertas permitem começar já.

| Etapa | Ferramenta (gratuita) | Para que serve no SICRAT |
|---|---|---|
| Gêmeo digital e dinâmica de voo | JSBSim (JSBSim Team, 2026); FlightGear (FlightGear, 2026) | Modelo 6 graus de liberdade do C172/Caravan com os jatos de N₂ como forças externas; testar parafuso, aileron travado e janela de disparo do retro. |
| Drone em software (SITL) | ArduPilot SITL (ArduPilot, 2026) com Gazebo (Gazebo, 2026) | Rodar o mesmo código de controle que vai no drone real, com física e sensores simulados, antes de voar. |
| Modelos substitutos com aprendizado de máquina | Python (scikit-learn, PyTorch) sobre resultados do JSBSim | Treinar um modelo rápido que imita milhares de simulações; varrer parâmetros (empuxo, braço, tamanho do tanque, altura de disparo) e otimizar massa e custo. |
| Monte Carlo de falhas | Scripts em Python | Sortear milhares de cenários (altura, vento, rotação, falha de uma válvula, tanque pela metade, atraso do sensor) e medir a taxa de sucesso e os piores casos. |
| Hardware no laço (HIL) | Placa de voo (ArduPilot/PX4) + válvulas reais ligadas ao simulador | Testar eletrônica, válvulas e atrasos reais com o avião ainda virtual. |
| Aprendizado por reforço para o disparo dos jatos | Treino no simulador | Pode descobrir sequências de pulsos mais econômicas. **Cuidado:** o resultado precisa ser verificado e limitado por uma lógica simples e auditável; redes neurais são difíceis de certificar. |
| Progressão física | Bancada de ar comprimido → drone → aeromodelo em escala → túnel de vento e câmara fria (parceiros) | Cada degrau só começa quando o anterior bate as métricas; o risco e o custo crescem devagar. |
| Revisão de literatura e patentes com IA | Assistentes de busca + leitura humana | Acelera o levantamento (como o de `estado-da-arte.md`), mas cada citação precisa ser conferida na fonte. |

**O que a IA não substitui.** A certificação continua exigindo ensaios físicos e evidências formais. Paraquedas de aeronave inteira seguem normas como a ASTM F2316, que pede, entre outros itens, três ensaios de queda bem-sucedidos com carga última e verificação de razão de descida (ASTM International, 2022). O software embarcado segue a garantia de desenvolvimento da RTCA DO-178C, aceita pela FAA (Estados Unidos, 2017; RTCA, 2026). Uma análise por computador só vale como evidência se o método tiver sido **validado por ensaio**. A IA **reduz o número de iterações**, não a necessidade de validação.

**Quanto tempo pode economizar [E].** Estimativa dos autores: **de 20% a 40% do tempo das fases de projeto e protótipo** (fases 1 a 4 do roteiro), algo como **6 a 18 meses** num caminho de 4 a 6 anos até um protótipo instalado. O raciocínio: boa parte desse tempo vai em ciclos de projetar, construir, testar e corrigir; com gêmeo digital, Monte Carlo e HIL, muitos ciclos ruins são descartados antes de virar peça, e os ensaios físicos começam mais perto da configuração final. Já o tempo de certificação (ensaios formais, análise de segurança, auditorias de software) **muda pouco**. É uma faixa de ordem de grandeza, não uma promessa; depende de parceiros, recursos e de o simulador ser calibrado com dados reais.

## Referências (ABNT NBR 6023:2018)

ARDUPILOT. **SITL simulator (software in the loop)**. [S. l.]: ArduPilot Dev Team, 2026. Disponível em: https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html. Acesso em: 21 nov. 2026.

ASTM INTERNATIONAL. **ASTM F2316-12(2022)**: standard specification for airframe emergency parachutes. West Conshohocken: ASTM International, 2022. Disponível em: https://store.astm.org/f2316-12r22.html. Acesso em: 21 nov. 2026.

ESTADOS UNIDOS. Federal Aviation Administration. **Advisory Circular 20-115D**: airborne software development assurance using EUROCAE ED-12( ) and RTCA DO-178( ). Washington, DC: FAA, 21 jul. 2017. Disponível em: https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-115D.pdf. Acesso em: 21 nov. 2026.

FLIGHTGEAR. **FlightGear flight simulator**. [S. l.]: FlightGear, 2026. Disponível em: https://www.flightgear.org/. Acesso em: 21 nov. 2026.

GAZEBO. **Gazebo**: robot simulation. [S. l.]: Open Robotics, 2026. Disponível em: https://gazebosim.org/. Acesso em: 21 nov. 2026.

JSBSIM TEAM. **JSBSim**: an open source flight dynamics & control software library. [S. l.]: GitHub, 2026. Disponível em: https://github.com/JSBSim-Team/jsbsim. Acesso em: 21 nov. 2026.

RTCA. **DO-178()**: software considerations in airborne systems and equipment certification. Washington, DC: RTCA, 2026. Disponível em: https://www.rtca.org/do-178/. Acesso em: 21 nov. 2026.

---

## AI and testing to move faster, safely (English)

The idea is to do most of the trial and error **on the computer and at small scale**, and keep expensive and risky tests for what has already been filtered. Free, open tools make it possible to start now.

| Step | Tool (free) | What it does for SICRAT |
|---|---|---|
| Digital twin and flight dynamics | JSBSim; FlightGear | 6-DOF model of the C172/Caravan with the N₂ jets as external forces; test spin, jammed aileron and the retro firing window. |
| Software-in-the-loop drone | ArduPilot SITL with Gazebo | Run the same control code that will fly on the real drone, with simulated physics and sensors, before flying. |
| ML surrogate models | Python (scikit-learn, PyTorch) on JSBSim results | Train a fast model that mimics thousands of simulations; sweep parameters (thrust, arm, tank size, firing height) and optimise mass and cost. |
| Monte Carlo of failures | Python scripts | Sample thousands of scenarios (height, wind, rotation, one valve failed, half tank, sensor delay) and measure success rate and worst cases. |
| Hardware-in-the-loop (HIL) | Flight controller (ArduPilot/PX4) + real valves wired to the simulator | Test real electronics, valves and delays while the aircraft is still virtual. |
| Reinforcement learning for jet firing | Training in the simulator | May find more gas-efficient pulse sequences. **Caution:** results must be verified and bounded by simple, auditable logic; neural networks are hard to certify. |
| Physical progression | Compressed-air bench → drone → scale model → wind tunnel and cold chamber (partners) | Each step starts only when the previous one meets its metrics; risk and cost grow slowly. |
| AI-assisted literature and patent review | Search assistants + human reading | Speeds up surveys (like the prior-art survey), but every citation must be checked at the source. |

**What AI does not replace.** Certification still requires physical tests and formal evidence. Whole-aircraft parachutes follow standards such as ASTM F2316, which requires, among other items, three successful ultimate-load drop tests and descent-rate verification (ASTM F2316-12(2022)). Airborne software follows RTCA DO-178C development assurance, accepted by the FAA (AC 20-115D). Computer analysis only counts as evidence when the method has been **validated by testing**. AI **reduces the number of iterations**, not the need for validation.

**How much time it may save [E].** Authors' estimate: **20% to 40% of the design and prototype phases** (roadmap phases 1–4), roughly **6 to 18 months** on a 4–6-year path to an installed prototype. Rationale: much of that time goes into design-build-test-fix cycles; with a digital twin, Monte Carlo and HIL, many bad cycles are discarded before becoming hardware, and physical tests start closer to the final configuration. Certification time (formal tests, safety analysis, software audits) **changes little**. This is an order-of-magnitude range, not a promise; it depends on partners, funding and calibrating the simulator with real data.
