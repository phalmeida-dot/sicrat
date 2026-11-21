# SICRAT — Sistema Integrado de Controle de Reação e Amortecimento Terminal

**Conceito original: Heitor Mouta Almeida (17 anos, estudante, Brasil).** Apoio: Raphael Almeida.

🌐 **Simulador / simulator:** https://phalmeida-dot.github.io/sicrat/sim/  
📁 **Repositório / repository:** https://github.com/phalmeida-dot/sicrat

**Projeto aberto, CC BY 4.0 — use livremente, citando a origem.** O código (scripts Python e simulador) está sob licença MIT (`LICENSE-CODE`).

> ⚠️ **Projeto conceitual, em fase de pesquisa. Não é um sistema certificado** e não deve ser instalado em nenhuma aeronave. Os números são estimativas de ordem de grandeza ([F] fato com fonte, [E] estimativa, [?] a confirmar). Não faça ensaios com pirotecnia em casa: veja as regras de segurança em `plano-teste-fase1.md`.

## Resumo (PT)

O SICRAT combina dois recursos de curtíssima duração para emergências em voo:

1. **Pulsos de gás frio (N₂)**, inspirados nos propulsores do Tesla Roadster, para parar um parafuso ou segurar a atitude por alguns segundos (por exemplo, com um aileron travado por gelo).
2. **Retrofoguetes sólidos de queima única** (estilo Soyuz) que suavizam o toque final sob paraquedas, de cerca de 8 m/s para cerca de 2 m/s.

Os alvos viáveis são a aviação geral (SR22, C172), o táxi aéreo amazônico (Cessna Caravan), os eVTOL e os drones. Os recursos são finitos: cerca de **8–12 s de jato no total** e **0,2–0,6 s de queima do retro**. Veja a seção "Limites de uso" no dossiê.

**Estado da arte:** paraquedas balísticos, retrofoguetes sob paraquedas (Soyuz, PRSM-915), foguetes antiparafuso da NASA e sistemas combinados (Schubert, 2000; SkyRyse, 2018) já existem. O que parece original no SICRAT é a integração: gás frio N₂ pulsado para atitude + retro de queima única no toque, sobre paraquedas já certificados, e o uso dos jatos com superfície travada por gelo. Detalhes e referências ABNT em [`estado-da-arte.md`](estado-da-arte.md).

**IA e testes:** gêmeo digital (JSBSim, FlightGear), ArduPilot SITL/Gazebo, Monte Carlo, hardware no laço e modelos substitutos podem cortar iterações (estimativa: 20–40% das fases de projeto), mas a certificação continua exigindo ensaios físicos. Veja [`ia-e-testes.md`](ia-e-testes.md).

## Summary (EN)

SICRAT combines two very short-duration resources for in-flight emergencies:

1. **Cold-gas (N₂) pulses**, inspired by the Tesla Roadster thrusters, to stop a spin or hold attitude for a few seconds (for example with an ice-jammed aileron).
2. **Single-shot solid retro-rockets** (Soyuz-style) that soften parachute touchdown from about 8 m/s to about 2 m/s.

Prior art (ballistic parachutes, retro-rockets under parachutes, NASA spin rockets, combined systems such as SkyRyse 2018) is summarised in [`estado-da-arte.md`](estado-da-arte.md) (EN summary at the end). AI and testing plan: [`ia-e-testes.md`](ia-e-testes.md).

The viable targets are general aviation, the Amazon air taxi (Cessna Caravan), eVTOLs and drones. Resources are finite: about **8–12 s of total jet time** and a **0.2–0.6 s retro burn**.

**Open project, CC BY 4.0 — use freely, crediting the source. Conceptual project, not certified.**

## Conteúdo / Contents

| Arquivo | Descrição |
|---|---|
| `dossie-SICRAT.pdf` / `.md` | Dossiê (PT) |
| `dossie-SICRAT-EN.pdf` / `.md` | Dossier (EN) |
| `estado-da-arte.md` | Estado da arte e originalidade (ABNT) / prior art and novelty |
| `ia-e-testes.md` | IA e testes para acelerar com segurança / AI and testing |
| `sim/index.html` | Simulador ilustrativo 2D + 3D (abre offline no navegador) / illustrative 2D + 3D simulator |
| `proximos-passos.md` | Roteiro, orçamento e plano de 8 semanas |
| `plano-teste-fase1.md` | Demonstrador seguro com ar comprimido, peças e métricas |
| `calc.py`, `calc4.py`, `calc5.py`, `custos.py`, `limites.json` | Contas (Python) |
| `fig/` | Gráficos |
| `LICENSE` | CC BY 4.0 (texto, desenhos, dossiês) |
| `LICENSE-CODE` | MIT (código) |

## Como citar / How to cite

> SICRAT — conceito original de Heitor Mouta Almeida (2026). Projeto aberto, CC BY 4.0.

Contribuições, críticas técnicas e melhorias são bem-vindas (abra uma *issue*).
