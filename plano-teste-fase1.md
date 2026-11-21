# SICRAT: plano de teste da Fase 1 (simulação + demonstrador)

**Autor do projeto:** Heitor Mouta Almeida · **Apoio:** Raphael Almeida · **Contato:** [contato]  
**Licença:** Projeto aberto, CC BY 4.0 — use livremente, citando a origem.

## 1. Objetivo

Mostrar, em escala de bancada, os dois princípios do SICRAT:

1. **Amortecimento terminal:** jatos acionados na altura certa reduzem a velocidade de toque de uma cápsula em queda.
2. **Controle de reação:** um pulso de gás frio gera torque e para uma rotação. Isso é medido em bancada giratória.

Os resultados também validam um **simulador** que serve para as fases seguintes.

## 2. Simulação (Python, gratuito)

| Etapa | Entrega |
|---|---|
| S1 | Calculadora de amortecimento (a, F, t, I, mₚ) para qualquer massa, a partir das fórmulas do dossiê |
| S2 | Simulação 1D da queda com arrasto e jato: v(t), h(t), altura de disparo ótima |
| S3 | Modelo de esvaziamento do tanque de ar (pressão caindo com o uso) para prever o empuxo real |
| S4 | Rotação 1 eixo: I·dω/dt = F·braço, para dimensionar os pulsos da bancada giratória |
| S5 (opcional) | 6DOF simplificado (ex.: biblioteca Python ou MATLAB/Octave) |

## 3. Demonstrador A: cápsula com freio a jato de ar

**Dimensionamento** [E]:

- Cápsula de 1 kg solta de 1,5 m chega a 5,4 m/s.
- Meta: frear para 1 m/s nos últimos 0,4 m, uma desaceleração de 35,5 m/s² (3,6 g).
- Isso exige 45 N de empuxo por 0,13 s, um impulso de cerca de 5,7 N·s.
- **Gargalo** de cerca de 8 mm com ar a 6 bar manométricos e cerca de 0,011 kg de ar por disparo. Um reservatório de 5 L a 6 bar guarda cerca de 0,04 kg.

**Montagem:**

- A cápsula desce guiada por **trilho vertical** (cano ou perfil), para não tombar.
- Um **sensor laser VL53L1X** mede a altura, e o **Arduino** abre a válvula solenoide na altura calculada.
- A **IMU MPU-6050** registra a desaceleração.
- O ar vai do reservatório para a cápsula por mangueira leve. Na versão 2 o reservatório vai embarcado.

**Ensaio:** 10 quedas sem jato (linha de base), depois 10 com jato, depois variações de altura de disparo.

## 4. Demonstrador B: bancada de empuxo e torque

- **Célula de carga 5 kg + HX711**: mede o empuxo do bocal em função da pressão. Isso calibra o simulador.
- **Bancada giratória:** braço de cerca de 0,5 m sobre um rolamento, com um bocal na ponta. A meta é parar uma rotação de cerca de 1 volta/s com pulsos controlados por IMU.

## 5. Lista de peças (preços aproximados, consultados em 21/11/2026; sujeitos a mudança)

| Item | Qtd. | Preço aprox. | Fonte |
|---|---|---|---|
| Arduino Nano V3 (sem cabo) | 1 | R$ 32,90 | Eletrogate: https://www.eletrogate.com/nano-v3-0-sem-cabo-usb |
| IMU MPU-6050 (GY-521) | 1 | R$ 19,90 | Eletrogate: https://www.eletrogate.com/acelerometro-e-giroscopio-3-eixos-6-dof-mpu-6050-gy-521 |
| Sensor laser VL53L1X | 1 | R$ 69,90 | MakerHero: https://www.makerhero.com/produto/sensor-de-distancia-a-laser-vl53l1x-de-alta-precisao/ |
| (alternativa mais barata) VL53L0X, alcance menor | 1 | R$ 20,90 | Eletrogate: https://www.eletrogate.com/modulo-gy-vl53l0xv2-sensor-de-distancia-laser-black |
| Célula de carga 5 kg | 1 | R$ 18,90 | Eletrogate: https://www.eletrogate.com/celula-de-carga-5kg-sensor-de-peso |
| Módulo HX711 | 1 | R$ 8,90 | Eletrogate: https://www.eletrogate.com/modulo-conversor-24bit-hx711-p-celula-de-carga |
| Válvula solenoide 2/2 vias NF, 1/4", 12 V | 1–2 | R$ 64,34 cada | KFF Automação: https://www.kffautomacao.com.br/valvula-solenoide-para-agua-ar-oleo/valvula-solenoide-pneumatica-2-vias-14-normal-fechada |
| Mini compressor portátil com manômetro (12 V ou recarregável) | 1 | R$ 57–130 | Cefeq / Magazine Luiza (anúncios variados) |
| Reservatório de ar metálico 5–20 L com **válvula de segurança e manômetro** (certificado) | 1 | R$ 150–400 [?] | Lojas de ferramentas; confirmar a pressão máxima de trabalho de ≥ 8 bar |
| Módulo MOSFET ou relé para a válvula, diodo, fios, protoboard | — | R$ 30–60 [?] | Eletrogate / RoboCore |
| Bateria 12 V (selada 7 Ah ou pack Li-ion 3S com BMS) | 1 | R$ 80–150 [?] | Lojas de eletrônica |
| Mangueira PU 6–8 mm, engates rápidos, bocais (latão) | — | R$ 50–120 [?] | Lojas de pneumática |
| Trilho, cápsula, base (PVC, MDF, perfil de alumínio) | — | R$ 50–120 [?] | Material de construção |
| Módulo microSD para gravar dados | 1 | R$ 10–20 [?] | Eletrogate / RoboCore |
| Óculos de proteção e protetor auricular | 2 | R$ 30–60 [?] | Lojas de EPI |
| **Total estimado** | | **R$ 750–1.400** [E] | |

Itens marcados com [?] não têm o preço confirmado numa loja específica, porque o valor varia muito por anúncio.

## 6. Regras de segurança (obrigatórias)

1. **Nada de pirotecnia em casa.** Isso inclui motores-foguete, pólvora, propelente caseiro e cartuchos de CO₂ perfurados à força. A parte "retrofoguete sólido" só será testada **em laboratório parceiro** (universidade, com responsável técnico) ou com motores comerciais certificados, operados por adultos habilitados e dentro das regras locais.
2. **Use só ar comprimido a baixa pressão (até 6 bar manométricos)**, em reservatório metálico certificado com válvula de segurança e pressão de trabalho de pelo menos 8 bar. **Nunca use garrafa PET ou plástico como vaso de pressão.**
3. **Óculos de proteção** para todos e distância mínima de 2 m durante disparos. Ninguém fica na linha do bocal.
4. **Adulto responsável** presente em todos os ensaios.
5. Despressurize o sistema antes de mexer em conexões. Teste vazamentos com água e sabão.
6. Quedas sempre em **trilho guiado**, de no máximo 2 m, sobre colchão ou espuma.
7. Nada de drones grandes voando em casa. O drone da Fase 2 só voa em área autorizada (regras da ANAC/DECEA) ou no campo do laboratório parceiro.
8. Registre tudo num **diário de bordo** (data, configuração, resultado, fotos). É exigido pela FEBRACE e documenta autoria e resultados para a publicação aberta.

## 7. Métricas de sucesso

| Métrica | Meta |
|---|---|
| Redução da velocidade de toque, comparada com queda sem jato | ≥ 50% (meta: 5,4 → < 2,5 m/s) |
| Precisão da altura de disparo | ± 5 cm |
| Repetibilidade | 8 de 10 quedas dentro da meta |
| Concordância simulador × ensaio (velocidade de toque e empuxo) | erro ≤ 20% |
| Bancada giratória: parar 1 volta/s | em ≤ 2 s, sem ultrapassar 10° do alvo |
| Incidentes de segurança | zero |

## 8. Entregáveis da Fase 1

- Código do simulador (repositório) e gráficos.
- Vídeo de 1–2 min (câmera lenta) das quedas com e sem jato.
- Relatório de 4–6 páginas, anexado ao dossiê.
- Diário de bordo.
