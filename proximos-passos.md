# SICRAT: próximos passos

**Autor do projeto:** Heitor Mouta Almeida (17 anos) · **Apoio:** Raphael Almeida · **Contato:** [contato]  
Preparado em 21/11/2026. Nada foi enviado a ninguém. **Licença:** Projeto aberto, CC BY 4.0 — use livremente, citando a origem. Os rascunhos estão em `contatos/`.

## 1. Ordem recomendada

1. **Publicar o projeto aberto antes dos contatos** (ver `nota-licenca-aberta.md`): repositório público no GitHub e depósito no Zenodo (DOI gratuito), sob CC BY 4.0. Assim o SICRAT vira referência pública (estado da técnica) e ninguém consegue patenteá-lo e fechá-lo.
2. **Fase 1 em casa:** simulação e demonstrador a ar comprimido (`plano-teste-fase1.md`).
3. **Aproximação acadêmica:** Mauá, FEI, ITA e Univap, enviando o link público do projeto.
4. **Feiras e bolsas:** FEBRACE 2028, Mostratec 2027 e PIBIC-EM via universidade.
5. **Indústria e divulgação:** Embraer (Embraer-X) por e-mail e mensagem direta (DM) no X para o Elon Musk, em inglês, sempre com o link público. Boeing e SpaceX ficam fora: a Boeing transfere os direitos do que recebe e a SpaceX não aceita ideias não solicitadas.

## 2. Roteiro por fases

| Fase | Duração | Entregáveis | Orçamento aprox. [E] | Com quem |
|---|---|---|---|---|
| 0. Publicação aberta | 2–4 semanas | Repositório público (dossiê, contas, desenhos, código) com licença CC BY 4.0 / MIT; DOI no Zenodo; diário de bordo | R$ 0 | GitHub, Zenodo |
| 1. Simulação e demonstrador | 2–6 meses | Simulador Python; cápsula com freio a ar; bancada de empuxo e torque; vídeo e relatório | R$ 750–1.400 | Em casa, com adulto responsável |
| 2. Drone de 5–25 kg (paraquedas + retro) | 6–12 meses | Quedas de drone com lógica de 3 fases em hardware; retro sólido só no laboratório parceiro | R$ 10–40 mil | Mauá / FEI / ITA / Univap (laboratórios, equipes AeroDesign); bolsa PIBIC-EM |
| 3. Aeronave leve (SR22/C172) | 2–4 anos | Módulo retro integrado ao BRS/CAPS; ensaios de queda instrumentados; plano de certificação STC/ANAC | US$ 0,5–2 mi | Fabricante do paraquedas (BRS/Cirrus), ANAC, universidade |
| 4. Caravan / eVTOL | 3–6 anos | Gás frio antiparafuso em túnel e simulador; protótipo instalado | US$ 3–10 mi | Embraer / Eve, operadores de táxi aéreo, ANAC (sandbox) |
| 5. Aviação comercial (pesquisa) | 6+ anos | Estudo de integração com fly-by-wire | a definir com o fabricante | Embraer e outros fabricantes interessados |

## 3. Plano de 8 semanas para o Heitor (3–4 h por semana)

| Semana | Tarefas (3–4 h) | Resultado da semana |
|---|---|---|
| 1 | Abrir o **diário de bordo** (caderno numerado ou documento datado). Ler o dossiê e anotar dúvidas. Instalar Python (ou usar Google Colab). | Diário iniciado; lista de dúvidas |
| 2 | Escrever a **calculadora de amortecimento** (a, F, t, I, mₚ) e reproduzir 3 linhas da tabela do dossiê. | Script que bate com o dossiê |
| 3 | Com o pai, **publicar o projeto aberto**: criar o repositório no GitHub (dossiê, desenhos, scripts, arquivos LICENSE) e gerar o DOI no Zenodo (ver `nota-licenca-aberta.md`). | Link público e DOI |
| 4 | **Simulação 1D da queda** da cápsula (passo de tempo, gravidade, arrasto, jato). Achar a melhor altura de disparo. | Gráfico v(t) e h(t) |
| 5 | Comprar as peças. Montar **Arduino + VL53L1X + MPU-6050** e gravar quedas **sem jato** (linha de base). | Dados de 10 quedas de base |
| 6 | Montar a **bancada de empuxo** (célula de carga + válvula + bocal). Medir empuxo × pressão (2, 4, 6 bar). | Curva de empuxo real |
| 7 | Integrar a cápsula com o jato. Fazer **quedas com disparo** (começando em 0,5 m e subindo até 1,5 m). Comparar com o simulador. | Primeiros resultados com jato |
| 8 | Ajustar o bocal e a altura de disparo. Comparar com o simulador (`sim/index.html`). Gravar o **vídeo** e escrever um **relatório de 4 páginas**. Revisar os e-mails de `contatos/` com o pai. | Pacote para universidades e feiras |

Regras: segurança conforme o `plano-teste-fase1.md` (nada de pirotecnia em casa); adulto presente nos ensaios; tudo anotado no diário.

## 4. Contatos e canais (públicos, verificados em 21/11/2026)

| Quem | Canal | URL |
|---|---|---|
| Elon Musk (X) | Mensagem direta (DM) em inglês, não post público (`contatos/x-dm-elon.md`) | https://x.com/elonmusk |
| Univap | FEAU (Engenharia Aeronáutica e Espaço): feau@univap.br | https://www.univap.br/univap/graduacao/feau/feau |
| Mauá (IMT) | Fale Conosco e Engenharia Mecânica | https://maua.br/fale-conosco ; https://maua.br/graduacao/engenharia-mecanica |
| FEI | AGFEI, Agência de Inovação | https://fei.edu.br/agfei/contato.html |
| ITA | Pró-Reitoria de Pesquisa e Relacionamento Institucional (Gestão da Inovação) | https://www.ita.br/content/pro-reitoria-de-pesquisa-e-relacionamento-institucional |
| Embraer | Embraer-X: connect@embraerx.com (e-mail publicado na página oficial no LinkedIn) | https://embraerx.embraer.com/ |
| ANAC | Sandbox Regulatório e Fale com a ANAC | https://www.gov.br/anac/pt-br/assuntos/sandbox-regulatorio/saiba-mais/saiba-mais-sobre-sandbox |
| CNPq | PIBIC-EM (bolsa de IC júnior via universidade) | https://www.gov.br/cnpq/pt-br/acesso-a-informacao/acoes-e-programas/programas/programas-ict/pibic-em |
| FEBRACE | Feira (2028; o prazo da edição 2027 já passou) | https://febrace.org.br/calendario/datas-importantes/ |
| Mostratec | Feira (cronograma de 2027 ainda não publicado) | https://mostratec.liberato.com.br/cronograma/ |
| Zenodo | Publicação aberta com DOI gratuito | https://zenodo.org/ |
| Creative Commons | Licença CC BY 4.0 | https://creativecommons.org/licenses/by/4.0/deed.pt_BR |

Os detalhes de cada canal estão em `contatos/outros-canais.md`.

## 6. IA e testes para acelerar com segurança

Detalhes, ferramentas e referências na seção 8 do dossiê e em `ia-e-testes.md`.

- [ ] **Semanas 1–4:** instalar JSBSim (https://github.com/JSBSim-Team/jsbsim) e rodar o C172 de exemplo; acrescentar os jatos de N₂ como forças externas.
- [ ] **Semanas 5–8:** Monte Carlo simples em Python (altura, rotação, vento, tanque pela metade, válvula falhando) e comparar com `calc5.py`.
- [ ] **Mês 3:** ArduPilot SITL + Gazebo com o drone (https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html), antes de qualquer voo real.
- [ ] **Mês 4–6:** modelo substituto (scikit-learn) para varrer empuxo, braço, tanque e altura de disparo; hardware no laço com válvula de ar comprimido.
- [ ] **Depois:** aprendizado por reforço só como pesquisa, sempre limitado por lógica simples e verificada.
- [ ] Toda conclusão do computador precisa ser confirmada em bancada, drone, túnel ou ensaio de queda. Certificação (ANAC/FAA, ASTM F2316, DO-178C) continua exigindo ensaios físicos.
- Economia estimada [E]: 20–40% do tempo das fases 1–4 (≈ 6–18 meses); a certificação muda pouco.

## 7. Checklist imediato

- [x] Publicar o projeto aberto no GitHub (CC BY 4.0): https://github.com/phalmeida-dot/sicrat · simulador: https://phalmeida-dot.github.io/sicrat/sim/
- [ ] Depositar no Zenodo para obter DOI (requer login no navegador).
- [ ] Revisar e aprovar a DM para o Elon (`contatos/x-dm-elon.md`) e os e-mails para Mauá, FEI, ITA, Univap e Embraer. Só enviar com aprovação.
- [ ] Preencher o [contato] nos dossiês e e-mails.
- [ ] Iniciar a semana 1 do plano.
- [ ] Marcar no calendário a abertura da Mostratec 2027 (por volta de julho [?]) e da FEBRACE 2028.
