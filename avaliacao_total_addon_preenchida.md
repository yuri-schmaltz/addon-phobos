# Avaliacao Total de Add-on para Blender (Execucao em 04/02/2026, atualizado em 05/02/2026)

> Avaliacao iniciada em **quarta-feira, 04 de fevereiro de 2026** e atualizada em **quinta-feira, 05 de fevereiro de 2026**, com foco em evidencias reproduziveis do repositorio local.

---

## 0) Metadados do add-on

- **Nome do add-on:** Phobos  
- **Versao do add-on:** 2.0.0 (`phobos/__init__.py`, `codemeta.json`)  
- **Autor / Organizacao:** Kai von Szadkowski, Henning Wiedemann, Malte Langosz, Simon Reichel, Julius Martensen et al.; DFKI / University of Bremen  
- **Repositorio / Pagina:** https://github.com/dfki-ric/phobos  
- **Licenca:** BSD-3-Clause  
- **Tipo:** modelagem robotica, pipeline, IO, utilitario (Blender + CLI)  
- **Escopo declarado pelo autor:** Ferramenta WYSIWYG para modelagem robotica no Blender com import/export de formatos (URDF/SDF/SMURF) e scripts CLI para automacao.  
- **Dependencias externas:** `pyyaml`, `numpy`, `scipy`, `pycollada`, `pydot`, opcionais `lxml`, `networkx`, `trimesh`, `Pillow`, extras `pybullet`, `open3d`, `python-fcl`; Blender Python (`bpy`) para add-on completo.  
- **Recursos do Blender usados:** Operators, Panels, AddonPreferences, propriedades em `Scene/Object/WindowManager`, operadores modais, handlers de desenho (`draw_handler_add/remove`), IO/import/export.  
- **Nivel de maturidade (autor):** **ASSUMIDO: beta/estavel inicial** (ha `stage=0` no `manifest.xml`, mas README declara uso em Blender 3.3 LTS).  
- **Data da avaliacao:** 04/02/2026 (atualizada em 05/02/2026)  
- **Responsavel pela avaliacao:** Codex (avaliacao automatizada local)

---

## 1) Sumario executivo

- **Status geral:** ❌ Reprovado  
- **Pontuacao total:** **40/100** (ver Rubrica)  
- **Principais pontos fortes (3-5):**
  - Escopo funcional amplo para modelagem robotica e conversao de formatos.
  - Documentacao inicial de instalacao e uso esta presente (`README.md` + wiki).
  - Metadados de release (`bl_info`, `codemeta.json`, licenca) estao claros.
  - CLI agora inicializa e lista comandos (bootstrap OK).
  - IO API (import/export) passa na suite de testes.
  - Add-on ativa em Blender 5.0.0 headless e a suite Blender (`basics/testmodel/testutils`) executa sem erro.
- **Principais riscos/lacunas (3-7):**
  - Fluxo de empacotamento via `setup.py` depende de `git` em runtime e falha em ambiente limpo.
  - Registro/desregistro do add-on apresenta risco de residuos e re-registro inconsistente.
  - Superficie de seguranca com `shell=True`, `eval` e `os.system` sem endurecimento.
  - Cobertura CI insuficiente (workflow visivel apenas para publicacao de docs).
  - UX/undo/redo e integracao visual nao verificados (sem sessao GUI).
- **Recomendacoes imediatas (Top 5):**
  1) Consolidar testes API/Blender em CI para bloquear regressao.
  2) Revisar ciclo `register()/unregister()` para limpeza completa e idempotencia.
  3) Endurecer execucao de comandos (remover `shell=True`/`eval` em caminhos nao confiaveis).
  4) Melhorar empacotamento sem dependencia de git.
  5) Validar UX/Undo/Redo em sessao GUI.
- **Bloqueadores para release (se houver):**
  - Nenhum bloqueador funcional detectado; reprovado por score baixo e lacunas de QA/seguranca.
  - Pipeline de qualidade nao barra regressao funcional atualmente.

---

## 2) Escopo, suposicoes e "NAO VERIFICADO"

### 2.1 Escopo incluido nesta avaliacao

- [x] Instalacao e ativacao (Blender 5.0.0 headless OK)
- [x] Fluxos E2E criticos
- [x] Integracoes com Blender (UI, Operators, DataBlocks, handlers) - **analise estatica**
- [x] Import/Export e I/O de arquivos
- [x] Performance (tempo, memoria, UI) - **parcial**
- [x] Robustez (erros, edge cases, undo/redo) - **parcial**
- [x] Seguranca e privacidade (se aplicavel) - **analise estatica**
- [x] Qualidade de codigo e manutencao
- [x] Documentacao e suporte
- [x] Empacotamento e release

### 2.2 Itens NAO VERIFICADOS (e como verificar)

| Item | Motivo | Como verificar (passos objetivos) | Owner sugerido |
|---|---|---|---|
| Compatibilidade declarada com Blender 3.3 LTS | Ambiente disponivel estava em Blender 5.0.0 (nao 3.3) | Repetir testes E2E em Blender 3.3 LTS e comparar com 5.0.0 | Maintainer Blender |
| UX visual (125%/150% UI scale) | Sem sessao GUI do Blender | Testar em Windows/Linux com escala 125% e 150%, capturar clipping/overflow | QA UX |
| Undo/Redo e cancelamento em operacoes pesadas | Sem sessao GUI do Blender (apenas headless) | Repetir em Blender 3.3 LTS/4.x em sessao GUI | QA Blender |
| Compatibilidade cruzada Linux/macOS | Avaliacao executada so em Windows 11 | Rodar matriz de smoke em Linux e macOS com mesmo commit | CI/Release |
| Integracao com outros add-ons | Nao testado em sessao Blender multi-addon | Subir perfil Blender com add-ons comuns e validar keymaps/propriedades globais | QA Integracao |

---

## 3) Matriz de ambientes e reprodutibilidade

### 3.1 Versoes do Blender
- **Versao minima suportada (declarada):** Blender 3.3 (`bl_info["blender"] = (3, 3)`)  
- **Versoes testadas:**  
  - [ ] LTS: NAO VERIFICADO (3.3 nao disponivel neste host)
  - [x] Ultima estavel: Blender 5.0.0 (build 2025-11-18) — **PASS (headless OK)**
  - [ ] Beta/Alpha (opcional): NAO VERIFICADO

### 3.2 Sistemas operacionais
- [x] Windows (versao): Microsoft Windows 11 Pro 10.0.26100 (64 bits)  
- [ ] Linux (distro/DE/Wayland/X11): NAO VERIFICADO  
- [ ] macOS (versao): NAO VERIFICADO  

### 3.3 Hardware
- **CPU:** AMD Ryzen 5 PRO 8500GE (6C/12T, max 3401 MHz)  
- **RAM:** 33.4 GB  
- **GPU/Driver:** AMD Radeon 740M Graphics, driver 32.0.21016.3003  
- **Resolucao/escala UI:** 1920x1080 / escala NAO VERIFICADA

### 3.4 Como reproduzir o ambiente
- **Fonte do add-on:** repositorio local `c:\Users\u60897\Documents\addon-phobos`  
- **Procedimento de instalacao reproduzivel (avaliacao):**
  1. `python -m pip install pyyaml numpy scipy setuptools pycollada pydot lxml networkx trimesh Pillow`
  2. Executar testes/logs em `tests/` e comandos de smoke/analise.
  3. Copiar `phobos/` para `C:\Users\u60897\AppData\Roaming\Blender Foundation\Blender\5.0\scripts\addons\phobos`
  4. Executar `C:\Blender\blender.exe -b --factory-startup --addons phobos ...` para validacao de bootstrap.
  5. Consolidar evidencias em `avaliacao_evidencias/`.
- **Comandos/scripts usados:** ver arquivos `avaliacao_evidencias/E001...E049`.

---

## 4) Inventario funcional (ANTES) — o que o add-on promete fazer

| ID | Funcao / Acao do usuario | Onde aparece (UI/atalho/menu) | Entrada | Saida esperada | Aceite (PASS/FAIL) |
|---|---|---|---|---|---|
| F-001 | Importar modelo robotico (URDF/SDF/SMURF) | Operador `phobos.import_robot_model` | Arquivo de modelo | Estrutura de robot carregada no Blender/API | PASS PARCIAL (API) |
| F-002 | Exportar modelo (URDF/SDF/SMURF + malhas) | Operadores `phobos.export_model` / API | Cena/modelo valido | Arquivos exportados consistentes | PASS PARCIAL (API) |
| F-003 | Executar CLI `phobos` e listar comandos | Terminal (`phobos --help`) | Sem entrada obrigatoria | Lista de subcomandos disponiveis | PASS |
| F-004 | Editar propriedades/kinematica (links/joints/sensores/motores) | Operadores `phobos.*` em `editing.py` | Objetos selecionados + parametros | Modificacao da cena conforme operador | NAO VERIFICADO (GUI) |
| F-005 | Salvar/carregar poses | Operadores `phobos.store_pose`, `phobos.load_pose` | Pose e modelo | Persistencia e restauracao de pose | NAO VERIFICADO (GUI) |
| F-006 | Selecionar/nomear objetos/modelo | Operadores `selection.py` e `naming.py` | Objetos/cena | Selecao/renomeacao consistente | NAO VERIFICADO (GUI) |
| F-007 | Exibir overlays/visualizacao auxiliar | `phobos.display_information`, wireframe ops | Cena ativa em `VIEW_3D` | Overlay sem travar viewport | NAO VERIFICADO (GUI) |
| F-008 | Instalar dependencias automaticamente | `check_requirements` / `install_requirements.py` | Ambiente Python/Blender | Dependencias instaladas | PASS PARCIAL (fora do Blender) |

---

## 5) Avaliacao funcional (E2E) — testes e evidencias

### 5.1 Fluxos criticos (3-7)

#### Fluxo E2E-01 — Bootstrap da CLI
- **Objetivo do usuario:** obter ajuda da CLI para iniciar uso.
- **Pre-condicoes:** Python 3.12, repositorio local acessivel.
- **Passos:**
  1) Executar `python -m phobos.scripts.phobos --help`
- **Resultado esperado:** imprimir lista de comandos e sair com codigo 0.
- **Resultado observado:** comandos listados com sucesso.
- **Evidencia:** `avaliacao_evidencias/E032_cli_help_posfix.txt`, `avaliacao_evidencias/E043_cli_tempo_posfix.txt`
- **Status:** ✅ PASS
- **Observacoes/edge cases:** ainda ha warnings de `pkg_resources` e `runpy`.

#### Fluxo E2E-02 — Importacao URDF via API
- **Objetivo do usuario:** abrir URDF de exemplo e obter raiz do robo.
- **Pre-condicoes:** dependencias Python instaladas.
- **Passos:**
  1) Executar `python -m unittest test_io.py -v` em `tests/api`
- **Resultado esperado:** `TestURDFIO.test_import` PASS.
- **Resultado observado:** `TestURDFIO.test_import` PASS.
- **Evidencia:** `avaliacao_evidencias/E048_teste_api_unittest_posfix5.txt`
- **Status:** ✅ PASS
- **Observacoes/edge cases:** sem falhas observadas neste fluxo.

#### Fluxo E2E-03 — Exportacao SMURF/URDF via API
- **Objetivo do usuario:** exportar modelo e comparar com ground truth.
- **Pre-condicoes:** dataset de teste presente em `tests/api/test_data`.
- **Passos:**
  1) Rodar suite `test_io.py` completa.
- **Resultado esperado:** 5 testes PASS.
- **Resultado observado:** 5/5 PASS.
- **Evidencia:** `avaliacao_evidencias/E048_teste_api_unittest_posfix5.txt`
- **Status:** ✅ PASS
- **Observacoes/edge cases:** sem divergencias na fixture atual.

#### Fluxo E2E-04 — Smoke de import do pacote
- **Objetivo do usuario:** importar modulo para automacao Python.
- **Pre-condicoes:** dependencias minimas instaladas.
- **Passos:**
  1) `import phobos`
  2) Ler `__version__`
- **Resultado esperado:** import com versao legivel.
- **Resultado observado:** import OK (`2.0.0`) com warning de `pkg_resources` depreciado.
- **Evidencia:** `avaliacao_evidencias/E002_metadados_runtime.txt`, `avaliacao_evidencias/E012_import_tempo.txt`
- **Status:** ✅ PASS (com ressalva)
- **Observacoes/edge cases:** warning indica risco de compatibilidade futura.

#### Fluxo E2E-05 — Ativacao do add-on no Blender 5.0.0
- **Objetivo do usuario:** habilitar add-on em execucao headless.
- **Pre-condicoes:** Blender 5.0.0 em `C:\Blender\blender.exe`; add-on copiado para pasta de addons do usuario.
- **Passos:**
  1) Executar `python tests/testrunner.py "C:\Blender\blender.exe"`
  2) Executar `C:\Blender\blender.exe -b --factory-startup --addons phobos --python-expr "print('addon_boot_test')"`
- **Resultado esperado:** add-on habilita sem crash e testes Blender executam.
- **Resultado observado:** add-on habilita e os testes Blender concluem com sucesso.
- **Evidencia:** `avaliacao_evidencias/E040_blender_addon_boot_posfix.txt`, `avaliacao_evidencias/E042_testrunner_blender5_posfix2.txt`
- **Status:** ✅ PASS
- **Observacoes/edge cases:** apenas headless; UI interativa nao verificada.

### 5.2 Regressoes e compatibilidade
- **O add-on altera configuracoes globais do Blender?** **SIM (potencial)**: adiciona propriedades em `bpy.types.Object/Scene/WindowManager`.
- **O add-on interfere em outros add-ons?** **RISCO MEDIO**: adiciona propriedades globais e keymaps; nao foi observado crash apos correcoes.

---

## 6) Integracoes com o Blender (profundidade tecnica)

### 6.1 Registro e ciclo de vida
- [ ] `register()`/`unregister()` corretos e idempotentes (**FAIL**: registro e desregistro nao espelhados; operadores registrados em `phobos/__init__.py` nao sao desregistrados no mesmo nivel)
- [ ] Sem residuos apos desinstalar (**RISCO**: propriedades adicionadas em `Scene/Object/WindowManager` sem remocao explicita completa em `phobosgui.unregister`)
- [ ] Suporte a "Reload Scripts" sem duplicar registro (**RISCO**: comentario TODO indicando problema conhecido)

**Evidencia:** `avaliacao_evidencias/E018_registro_addon_init.txt`, `avaliacao_evidencias/E020_phobosgui_register_unregister.txt`, `avaliacao_evidencias/E019_generic_register_vazio.txt`

### 6.2 UI (Panels, Menus, UIList, Popovers)
- **Localizacao e consistencia:** existe painel e varios operadores; validacao visual **NAO VERIFICADA**.
- **Estados:** nao validado em runtime.
- **Responsividade:** **NAO VERIFICADA** (sem GUI Blender).
- **Acessibilidade minima:** **NAO VERIFICADA**.

### 6.3 Operators e UX operacional
- [x] `bl_options` adequado em parte dos operadores (ex.: `REGISTER`, `UNDO`) - **PASS PARCIAL**
- [ ] Compatibilidade Undo/Redo - **NAO VERIFICADO**
- [ ] Mensagens de erro legiveis - **FAIL** (stack traces brutos em falhas de CLI/API)
- [x] Cancelamento funciona em operadores modais analisados (`ESC/RIGHTMOUSE`) - **PASS PARCIAL**

### 6.4 Dados e DataBlocks
- [x] Uso intenso de `bpy.data/context` observado - **PASS PARCIAL**
- [ ] Integridade de cena/linked data/overrides - **NAO VERIFICADO**
- [x] Custom properties com namespace `phobos*` em varios pontos - **PASS PARCIAL**
- [ ] Operacoes batch sem travamento UI - **NAO VERIFICADO**

### 6.5 Dependencia do contexto e modo
- [x] Polls de operadores existem para alguns contextos - **PASS PARCIAL**
- [ ] Robustez em cena vazia/sem selecao/linkadas - **NAO VERIFICADO**
- [ ] Multi-object e multi-user data - **NAO VERIFICADO**

### 6.6 Handlers, Timers, Modal Operators
- [x] Sem uso extensivo de `bpy.app.handlers` persistentes - **PASS**
- [ ] Nao cria loops/CPU alta - **NAO VERIFICADO**
- [x] Nao degrada estabilidade do Blender - **PASS PARCIAL** (headless OK; GUI nao verificada)

### 6.7 Integracoes especificas (marcar se aplicavel)
- [ ] Geometry Nodes
- [x] Shader Nodes / Material Pipeline (indicativos em IO/material)
- [ ] Animation/Drivers/NLA (nao comprovado nesta execucao)
- [ ] Render (Cycles/Eevee), Compositor
- [ ] Grease Pencil
- [ ] Asset Browser
- [x] File Browser / IO (import/export URDF/SDF/SMURF)
- [x] Python deps via pip / `site-packages` embutido
- [x] Integracoes externas (ROS/Gazebo/pybullet/simulacao)

---

## 7) Robustez e confiabilidade

### 7.1 Testes de falha (fault injection) — minimo recomendado
- [x] Entradas/estados invalidos detectados por testes de API - **PASS PARCIAL** (suite cobre casos basicos)
- [ ] Arquivos grandes
- [ ] Cena complexa
- [ ] Execucao repetida (100x) sem leak/degeneracao
- [ ] Enable/disable repetido (10x) sem duplicar recursos
- [ ] Interromper operacao (cancelar) sem corromper estado
- [ ] "Salvar, fechar Blender, reabrir" preserva resultados

### 7.2 Gestao de erros
- [ ] `try/except` estrategico sem engolir excecoes (**PARCIAL**: ha `except` amplo em alguns pontos)
- [x] Logs de diagnostico existem (modulo de log + prints) - **PASS PARCIAL**
- [ ] Falhas nao deixam estado inconsistente - **NAO VERIFICADO**
- [ ] Mensagens ao usuario com acao recomendada - **FAIL** nos fluxos CLI/API avaliados

### 7.3 Estabilidade
- **Crash/hang observado?** **NAO** apos correcoes (headless OK).  
  **Historico:** crash ocorreu antes das correcoes (ver `E028`/`E029`/`E030`).
- **Stack trace relevante (historico):** `E029` (backtrace C) e `E028`/`E030` (logs de execucao).
- **Reprodutibilidade:** agora NAO reproduzido; crash anterior era consistente.

---

## 8) Performance (metrica antes/depois)

### 8.1 Metricas minimas
- **Tempo de execucao do fluxo critico (p50/p95):**
  - `import phobos`: ~1.131 s (amostra unica)
  - `python -m phobos.scripts.phobos --help`: ~3.404 s (sucesso)
  - Suite API (`5 testes`): 0.494 s (PASS)
- **Ativacao do add-on no Blender 5.0.0:** conclui sem crash (tempo nao medido)
- **Impacto no FPS/viewport:** NAO VERIFICADO (sem sessao GUI)
- **Uso de CPU/RAM pico e steady-state:** NAO VERIFICADO
- **Tempo de startup/ativacao do add-on:** conclui (tempo nao medido)
- **I/O (tamanho de outputs/caches):** NAO VERIFICADO (export OK)

### 8.2 Criterios PASS/FAIL sugeridos (ajustaveis)
- Ativar add-on <= 1s: **NAO VERIFICADO** (tempo nao medido)
- Operacao principal <= Xs/Ys: **PASS PARCIAL** (operacao base conclui)
- UI responsiva (sem travar > 250 ms): **NAO VERIFICADO** (sem sessao GUI)

### 8.3 Evidencias
- Comandos/roteiro de medicao: `avaliacao_evidencias/E012_import_tempo.txt`, `avaliacao_evidencias/E043_cli_tempo_posfix.txt`, `avaliacao_evidencias/E049_teste_api_tempo_posfix.txt`, `avaliacao_evidencias/E042_testrunner_blender5_posfix2.txt`
- Resultados (tabela):

| Cenario | Medida | Antes | Depois | Delta | Status |
|---|---:|---:|---:|---:|---|
| Pequeno (import modulo) | Tempo (s) | N/A | 1.131 | N/A | PASS PARCIAL |
| Grande (suite API de IO) | Tempo (s) | N/A | 0.494 (PASS) | N/A | PASS |
| Add-on enable (Blender 5.0.0) | Tempo (s) | N/A | N/A (conclui) | N/A | PASS PARCIAL |

---

## 9) Seguranca, privacidade e cadeia de suprimentos (quando aplicavel)

### 9.1 Superficies
- [x] Acesso a rede (pip/curl em utilitarios)
- [x] Execucao de binarios/`subprocess`
- [x] Leitura/escrita fora do projeto (operacoes de arquivo e shell utilitario)
- [x] Download de deps/assets (instalacao de pacotes)
- [ ] Telemetria / envio de dados (NAO EVIDENCIADO)

### 9.2 Checklist essencial
- [ ] Sem `shell=True` e sem concatenacao de comandos (**FAIL**: varios pontos em `misc.py`, `hyrodyn.py`)
- [ ] Validacao de caminhos (**NAO COMPROVADA / PARCIAL**)
- [ ] Limites de tamanho e tempo para I/O e downloads (**NAO COMPROVADA**)
- [ ] Dependencias pinned (versoes fixas/lockfile) (**FAIL**: sem pinning)
- [ ] Arquivos temporarios em diretorio seguro; limpeza (**PARCIAL/FAIL**)
- [ ] Politica de logs sem dados sensiveis (**NAO VERIFICADO**)

### 9.3 Licencas e compliance
- Licenca do add-on compativel com distribuicao pretendida? **SIM** (BSD-3-Clause).  
- Dependencias tem licencas compativeis? **NAO VERIFICADO COMPLETAMENTE** (sem auditoria automatizada de licencas).  
- Existe aviso de uso de terceiros? **PARCIAL** (`README`, `codemeta`, citacao).

---

## 10) UX, consistencia e acessibilidade (pratico e objetivo)

### 10.1 Heuristicas (PASS/FAIL)
- [ ] Descoberta <= 10s sem manual (**NAO VERIFICADO GUI**)
- [ ] Feedback de progresso/estado claro (**NAO VERIFICADO GUI**)
- [ ] Erros acionaveis (**FAIL** em CLI/API, stack trace tecnico)
- [ ] Consistencia com Blender (**NAO VERIFICADO visualmente**)
- [ ] Sem poluicao de UI (**NAO VERIFICADO**)

### 10.2 Acessibilidade minima (quando aplicavel)
- [ ] Labels claros e nao ambiguos (NAO VERIFICADO)
- [ ] Navegacao por teclado (NAO VERIFICADO)
- [ ] Suporte a escala UI 125%/150% sem clipping (NAO VERIFICADO)

---

## 11) Qualidade do codigo e manutencao

### 11.1 Estrutura e padroes
- [ ] Organizacao modular (evitar arquivo monolitico) - **PARCIAL/FAIL** (arquivos >2k linhas)
- [ ] Separacao UI vs logica vs IO - **PARCIAL**
- [ ] Tipagem/documentacao interna (docstrings) - **PARCIAL/FAIL** (muitos `TODO Missing documentation`)
- [ ] Evita estados globais perigosos - **PARCIAL/FAIL** (uso de globais e inicializacao condicional complexa)

### 11.2 Compatibilidade de API do Blender
- [ ] Sem uso de API depreciada sem fallback - **RISCO** (`newscene.objects.link`, `scene.layers`, etc.)
- [ ] Tratamento de diferencas entre versoes - **PARCIAL**
- [ ] Teste em versoes-alvo (matriz) - **NAO COMPROVADO**

### 11.3 Testabilidade e automacao
- [x] Testes automatizados existem (unit/integration) - **SIM**
- [ ] Smoke E2E scriptavel robusto - **PARCIAL** (`tests/testrunner.py`, depende de Blender local)
- [ ] CI (lint, testes, build do zip) - **FAIL** (workflow observado focado em docs)
- [ ] Verificacao de estilo (flake8/ruff/black) em CI - **NAO EVIDENCIADO**

### 11.4 Observabilidade
- [x] Logging configuravel basico existe
- [ ] Identificadores por execucao/fluxo (NAO EVIDENCIADO)
- [ ] Modo diagnostics dedicado (NAO EVIDENCIADO)

---

## 12) Documentacao, suporte e onboarding

### 12.1 Documentacao minima
- [x] Instalacao (zip, preferencias, dependencias)
- [x] Quickstart basico
- [ ] Troubleshooting estruturado (parcial)
- [x] Compatibilidade (Blender 3.3 declarado)
- [ ] Desinstalacao/limpeza detalhada (parcial)
- [x] Exemplos/ilustracoes

### 12.2 Qualidade da documentacao (PASS/FAIL)
- [ ] Executavel por alguem novo em <= 15 min (**RISCO**: fluxo atual quebra em pontos criticos)
- [x] Prints/GIFs para fluxo principal
- [x] Links principais funcionando (NAO auditado exaustivamente)

---

## 13) Empacotamento e release

### 13.1 Estrutura do pacote
- [x] Zip instalavel padrao Blender (instrucao documentada)
- [x] `bl_info` completo
- [ ] Sem arquivos desnecessarios (NAO VERIFICADO para artefato final)
- [ ] Dependencias inclusas/pinning seguro (**PARCIAL/FAIL**)

### 13.2 Upgrade/rollback
- [ ] Atualizar versao sem quebrar preferencias/salvos (NAO VERIFICADO)
- [ ] Migracao de dados com fallback (PARCIAL: README cita migracao via SMURF)
- [ ] Rollback para versao anterior funciona (NAO VERIFICADO)

---

## 14) Rubrica de pontuacao (0-5) e pesos

| Area | Peso | Nota (0-5) | Subtotal |
|---|---:|---:|---:|
| Funcionalidade E2E | 25 | 3 | 15 |
| Integracoes com Blender | 15 | 2 | 6 |
| Robustez/Confiabilidade | 15 | 2 | 6 |
| Performance | 10 | 1 | 2 |
| Seguranca/Privacidade (se aplicavel) | 10 | 1 | 2 |
| UX/Acessibilidade | 10 | 1 | 2 |
| Qualidade de codigo/manutencao | 10 | 2 | 4 |
| Documentacao/Onboarding | 5 | 3 | 3 |
| **TOTAL** | **100** |  | **40** |

### 14.1 Criterios de decisao
- ❌ **Reprovado**: < 65 ou com bloqueadores (aplicavel aqui: score 40).

---

## 15) Achados detalhados (formato obrigatorio)

- **ID:** A-001  
- **Categoria:** Funcionalidade  
- **Severidade:** Bloqueador  
- **Descricao objetiva:** CLI `phobos` falhava no bootstrap por `UnboundLocalError` em `check_pybullet_available`.  
- **Evidencia:** `avaliacao_evidencias/E021_pybullet_bug.txt`, `avaliacao_evidencias/E032_cli_help_posfix.txt`  
- **Impacto:** usuario nao conseguia descobrir/comandar scripts via CLI principal.  
- **Causa provavel:** typo/escopo em variavel (`PYBULLET_AVAILBABLE` vs `PYBULLET_AVAILABLE`).  
- **Recomendacao (acao):** corrigir nome/escopo de variavel, adicionar teste unitario para `check_pybullet_available()`.  
- **Validacao PASS/FAIL:** `python -m phobos.scripts.phobos --help` deve sair 0 e listar comandos.  
- **Risco de regressao + mitigacao:** medio; mitigar com teste em CI para bootstrap CLI.  
- **Owner sugerido:** Maintainer CLI/Core  
- **Status:** Resolvido (ver E032)

- **ID:** A-002  
- **Categoria:** Funcionalidade  
- **Severidade:** Alta  
- **Descricao objetiva:** Divergencias de exportacao API (URDF/SMURF/SDF) foram resolvidas; suite IO agora PASS.  
- **Evidencia:** `avaliacao_evidencias/E048_teste_api_unittest_posfix5.txt`  
- **Impacto:** exportacao agora coincide com ground truth; regressao monitoravel via testes.  
- **Causa provavel:** divergencias de serializacao (sensores, materiais, hfov, paths e precisao) corrigidas no export/import.  
- **Recomendacao (acao):** manter fixtures e adicionar round-trip URDF<->SMURF<->SDF com tolerancia numerica.  
- **Validacao PASS/FAIL:** `python -m unittest test_io.py -v` em `tests/api` deve passar integralmente.  
- **Risco de regressao + mitigacao:** medio; adicionar testes de round-trip e CI.  
- **Owner sugerido:** Maintainer IO/Core  
- **Status:** Resolvido

- **ID:** A-003  
- **Categoria:** Testes / Robustez  
- **Severidade:** Alta  
- **Descricao objetiva:** Testes `basics` e `testmodel` assumiam API em `phobos.blender` que nao existia (`bl_info`, `model`).  
- **Evidencia:** `avaliacao_evidencias/E042_testrunner_blender5_posfix2.txt`  
- **Impacto:** suite nao representava saude real; sinal obsoleto de qualidade.  
- **Causa provavel:** refatoracao da estrutura de pacotes sem atualizar testes legados.  
- **Recomendacao (acao):** atualizar imports e fixtures para arquitetura atual; separar testes Blender e nao-Blender.  
- **Validacao PASS/FAIL:** execucao automatizada dos testes deve concluir sem `AttributeError`.  
- **Risco de regressao + mitigacao:** medio; bloquear merge com CI obrigatorio.  
- **Owner sugerido:** QA + Maintainer  
- **Status:** Resolvido (basics/testmodel/testutils PASS)

- **ID:** A-004  
- **Categoria:** Integracao  
- **Severidade:** Alta  
- **Descricao objetiva:** Ciclo de `register/unregister` e incompleto/assimetrico, com risco de residuos de classes/propriedades.  
- **Evidencia:** `avaliacao_evidencias/E018_registro_addon_init.txt`, `avaliacao_evidencias/E020_phobosgui_register_unregister.txt`, `avaliacao_evidencias/E019_generic_register_vazio.txt`  
- **Impacto:** recarga de scripts pode duplicar estado, causar conflitos e comportamento instavel.  
- **Causa provavel:** desregistro parcial e modulo `generic` com `register()` vazio.  
- **Recomendacao (acao):** mapear todos os recursos registrados e garantir desregistro espelhado/idempotente.  
- **Validacao PASS/FAIL:** 10 ciclos enable/disable sem erros/residuos (classes, handlers, props).  
- **Risco de regressao + mitigacao:** alto em ambiente Blender; criar teste de lifecycle.  
- **Owner sugerido:** Maintainer Blender  
- **Status:** Aberto

- **ID:** A-005  
- **Categoria:** Seguranca  
- **Severidade:** Alta  
- **Descricao objetiva:** Uso de `shell=True`, `eval` e `os.system` com comandos concatenados eleva risco de injecao e comportamento inseguro.  
- **Evidencia:** `avaliacao_evidencias/E004_superficie_seguranca.txt`  
- **Impacto:** potencial execucao arbitraria em entradas nao confiaveis; risco em pipelines automatizados.  
- **Causa provavel:** utilitarios legados sem endurecimento de subprocessos.  
- **Recomendacao (acao):** migrar para `subprocess.run([...], shell=False)`, parser seguro para expressoes numericas, sanitizacao de paths.  
- **Validacao PASS/FAIL:** SAST sem achados criticos para execucao de shell/eval.  
- **Risco de regressao + mitigacao:** medio; cobrir comandos principais com testes de comportamento.  
- **Owner sugerido:** Maintainer Seguranca/Infra  
- **Status:** Aberto

- **ID:** A-006  
- **Categoria:** Release  
- **Severidade:** Media  
- **Descricao objetiva:** `setup.py` depende de metadata de `git`; sem git no PATH pode falhar em ambientes limpos.
- **Evidencia:** `avaliacao_evidencias/E007_setup_py.txt`, `avaliacao_evidencias/E031_setup_py_com_git.txt`  
- **Impacto:** quebra de empacotamento/distribuicao em CI/dev sem git instalado.  
- **Causa provavel:** dependencia obrigatoria de `git rev-parse` na geracao de metadados.  
- **Recomendacao (acao):** fallback robusto quando git nao estiver disponivel (ex.: `unknown`/env var).  
- **Validacao PASS/FAIL:** `python setup.py --name` e `pip install .` funcionam com e sem git.  
- **Risco de regressao + mitigacao:** baixo/medio; testes de build em matriz de ambientes.  
- **Owner sugerido:** Maintainer Release  
- **Status:** Aberto

- **ID:** A-007  
- **Categoria:** Qualidade/Automacao  
- **Severidade:** Media  
- **Descricao objetiva:** Workflow CI observado publica docs, sem gate claro de testes/lint/build do add-on.  
- **Evidencia:** `avaliacao_evidencias/E015_ci_arquivos.txt`, `avaliacao_evidencias/E016_workflow_gh_pages.yml.txt`  
- **Impacto:** regressao funcional pode chegar a release sem bloqueio automatico.  
- **Causa provavel:** pipeline de qualidade incompleto no repositorio avaliado.  
- **Recomendacao (acao):** adicionar workflows para testes API, smoke Blender headless e lint.  
- **Validacao PASS/FAIL:** PR deve falhar automaticamente em regressao funcional.  
- **Risco de regressao + mitigacao:** alto enquanto nao houver gate.  
- **Owner sugerido:** Maintainer CI  
- **Status:** Aberto

- **ID:** A-008  
- **Categoria:** Codigo/Manutencao  
- **Severidade:** Media  
- **Descricao objetiva:** base com modulos monoliticos e muitos TODOs/docstrings faltantes reduz manutenibilidade.  
- **Evidencia:** `avaliacao_evidencias/E013_tamanho_arquivos.txt`  
- **Impacto:** curva de manutencao alta, maior chance de regressao e baixa previsibilidade de mudancas.  
- **Causa provavel:** acoplamento historico e refatoracao parcial.  
- **Recomendacao (acao):** fatiar modulos grandes por dominio e completar docstrings criticas.  
- **Validacao PASS/FAIL:** reducao de tamanho/ciclomatica e melhora de cobertura de testes por modulo.  
- **Risco de regressao + mitigacao:** medio; refatorar com testes de caracterizacao antes.  
- **Owner sugerido:** Maintainer Arquitetura  
- **Status:** Aberto

- **ID:** A-009  
- **Categoria:** Integracao/Compatibilidade  
- **Severidade:** Alta  
- **Descricao objetiva:** codigo Blender ainda contem chamadas potencialmente legadas (`newscene.objects.link`, `scene.layers`).  
- **Evidencia:** `avaliacao_evidencias/E023_api_blender_legada.txt`  
- **Impacto:** risco de quebra em Blender 3.x dependendo do fluxo acionado.  
- **Causa provavel:** migracao incompleta de APIs antigas.  
- **Recomendacao (acao):** revisar APIs Blender usadas em `editing.py` e normalizar para padrao atual.  
- **Validacao PASS/FAIL:** smoke E2E em Blender 3.3 LTS sem `AttributeError`/`RNA` errors.  
- **Risco de regressao + mitigacao:** alto; exigir testes de fluxo principal no Blender alvo.  
- **Owner sugerido:** Maintainer Blender  
- **Status:** Aberto

- **ID:** A-010  
- **Categoria:** Robustez / Integracao  
- **Severidade:** Bloqueador  
- **Descricao objetiva:** Ativacao do add-on em Blender 5.0.0 encerrava o processo com `EXCEPTION_ACCESS_VIOLATION`.  
- **Evidencia:** `avaliacao_evidencias/E040_blender_addon_boot_posfix.txt`, `avaliacao_evidencias/E042_testrunner_blender5_posfix2.txt`  
- **Impacto:** impossibilitava uso do add-on no ambiente testado; risco de perda de sessao no Blender.  
- **Causa provavel:** incompatibilidade com API/runtime do Blender 5.0.0 durante bootstrap de UI/add-on (backtrace em `UI_popup_menu_end`).  
- **Recomendacao (acao):** manter guards/condicionais para headless e adicionar matriz CI Blender 3.3/4.x/5.x.  
- **Validacao PASS/FAIL:** `C:\Blender\blender.exe -b --factory-startup --addons phobos --python-expr "print('ok')"` deve sair 0 sem crash.  
- **Risco de regressao + mitigacao:** alto; mitigar com matriz CI em Blender 3.3 LTS + 4.x + 5.x.  
- **Owner sugerido:** Maintainer Blender/Core  
- **Status:** Resolvido (headless OK)

---

## 16) Backlog executavel (priorizado)

| Prioridade | Tarefa | Objetivo | Passos | Aceite | Esforco | Risco |
|---:|---|---|---|---|---|---|
| P1 | Revisar lifecycle `register/unregister` | Evitar residuos em Blender | Mapear recursos registrados e desregistrar de forma simetrica | 10 ciclos enable/disable sem erro | M | Alto |
| P1 | Hardening de seguranca em subprocess/eval | Reduzir superficie de ataque | Remover `shell=True`, trocar `eval`, sanitizar paths | SAST sem achados criticos | M | Medio |
| P1 | Pipeline CI de qualidade | Bloquear regressao em PR | Workflow para lint + testes API + smoke Blender headless | PR falha ao quebrar suite | M | Medio |
| P2 | Melhorar empacotamento sem dependencia de git | Facilitar release em ambiente limpo | Fallback em `setup.py` quando git indisponivel | `pip install .` funciona sem git | S | Baixo |
| P2 | Refatorar modulos monoliticos criticos | Melhorar manutencao | Quebrar `editing.py`/`phobosgui.py` por dominio | reducao de tamanho e melhor cobertura | L | Medio |

---

## 17) Apendice — roteiro rapido de teste (checklist)

### Instalacao/ativacao
- [ ] Instalar via Preferences > Add-ons > Install...
- [ ] Ativar; fechar/reabrir Blender; confirmar persistencia
- [ ] Desativar/reativar; confirmar ausencia de duplicacao (keymaps/handlers)

### Funcionalidade
- [x] Fluxo principal (E2E-01 CLI bootstrap) executado
- [x] Fluxos secundarios (API import/export) executados
- [ ] Undo/Redo (se aplicavel) PASS
- [ ] Cancelamento PASS (runtime Blender)

### Robustez
- [x] Entradas/estados invalidos revelam falhas trataveis (via testes)
- [ ] Execucao repetida 100x sem degradar
- [ ] Cena grande nao trava permanentemente

### Performance
- [x] Medicoes basicas coletadas e registradas (import/CLI)

### Seguranca (se aplicavel)
- [x] Achados de execucao insegura mapeados

### Documentacao
- [x] Quickstart lido e confrontado com execucao real

---

## 18) Registro de evidencias

| Evidencia | Tipo | Local (arquivo/URL/caminho) | Observacao |
|---|---|---|---|
| E-001 | Ambiente | `avaliacao_evidencias/E001_ambiente.txt` | Python, Blender (path explicito) e git disponiveis |
| E-002 | Metadados | `avaliacao_evidencias/E002_metadados_runtime.txt` | `bl_info` + `codemeta` |
| E-003 | Inventario | `avaliacao_evidencias/E003_inventario_operadores.txt` | Mapeamento de operadores |
| E-004 | Seguranca | `avaliacao_evidencias/E004_superficie_seguranca.txt` | `shell=True`/`eval`/`os.system` |
| E-005 | Log de teste | `avaliacao_evidencias/E005_teste_api_unittest.txt` | Falha 5/5 em API IO |
| E-006 | Log de teste | `avaliacao_evidencias/E006_testrunner_blender.txt` | Blender nao encontrado no host |
| E-007 | Log build | `avaliacao_evidencias/E007_setup_py.txt` | `setup.py` falha sem git |
| E-008 | Log CLI | `avaliacao_evidencias/E008_cli_help.txt` | Falha `UnboundLocalError` |
| E-009 | Log de teste | `avaliacao_evidencias/E009_teste_basics.txt` | Teste legados inconsistentes |
| E-010 | Log de teste | `avaliacao_evidencias/E010_teste_testmodel.txt` | Falhas por API ausente |
| E-011 | Log static | `avaliacao_evidencias/E011_compileall.txt` | Warnings de escapes invalidos |
| E-012 | Performance | `avaliacao_evidencias/E012_import_tempo.txt` | Tempo de import do pacote |
| E-013 | Codigo | `avaliacao_evidencias/E013_tamanho_arquivos.txt` | Arquivos monoliticos |
| E-014 | Testes | `avaliacao_evidencias/E014_arquivos_teste.txt` | Inventario de testes |
| E-015 | CI | `avaliacao_evidencias/E015_ci_arquivos.txt` | Arquivos em `.github` |
| E-016 | CI workflow | `avaliacao_evidencias/E016_workflow_gh_pages.yml.txt` | Pipeline focado em docs |
| E-017 | Documentacao | `avaliacao_evidencias/E017_readme.txt` | Escopo/documentacao de uso |
| E-018 | Codigo | `avaliacao_evidencias/E018_registro_addon_init.txt` | Registro/desregistro top-level |
| E-019 | Codigo | `avaliacao_evidencias/E019_generic_register_vazio.txt` | `register()` vazio em `generic.py` |
| E-020 | Codigo | `avaliacao_evidencias/E020_phobosgui_register_unregister.txt` | Propriedades/classes no lifecycle |
| E-021 | Codigo | `avaliacao_evidencias/E021_pybullet_bug.txt` | Bug de variavel pybullet |
| E-022 | Codigo | `avaliacao_evidencias/E022_xmlrobot_ctor_vs_property.txt` | Assinatura XMLRobot vs parser |
| E-023 | Codigo | `avaliacao_evidencias/E023_api_blender_legada.txt` | Uso potencial de API legada |
| E-024 | Ambiente | `avaliacao_evidencias/E024_os_info.txt` | OS da avaliacao |
| E-025 | Ambiente | `avaliacao_evidencias/E025_hw_info.txt` | CPU/RAM/GPU/resolucao |
| E-026 | Performance + erro | `avaliacao_evidencias/E026_cli_tempo_e_erro.txt` | Tempo/retorno da CLI com stack trace |
| E-027 | Log Blender | `avaliacao_evidencias/E027_testrunner_blender5.txt` | Blender 5.0.0 sem add-on instalado no path inicial |
| E-028 | Log Blender | `avaliacao_evidencias/E028_testrunner_blender5_instalado.txt` | Historico: testrunner com crash nativo |
| E-029 | Crash dump | `avaliacao_evidencias/E029_blender_crash.txt` | Historico: backtrace `EXCEPTION_ACCESS_VIOLATION` |
| E-030 | Log Blender | `avaliacao_evidencias/E030_blender_addon_boot.txt` | Historico: repro minima de crash com `--addons phobos` |
| E-031 | Log build | `avaliacao_evidencias/E031_setup_py_com_git.txt` | `setup.py --name` conclui quando git esta disponivel |
| E-032 | Log CLI | `avaliacao_evidencias/E032_cli_help_posfix.txt` | CLI `--help` OK apos correcao |
| E-033 | Log de teste | `avaliacao_evidencias/E033_teste_api_unittest_posfix.txt` | Historico: API IO falha (3/5) antes das correcoes |
| E-034 | Log Blender | `avaliacao_evidencias/E034_blender_addon_boot_posfix.txt` | Boot posfix (iteracao 1) |
| E-035 | Log Blender | `avaliacao_evidencias/E035_blender_addon_boot_posfix2.txt` | Boot posfix (iteracao 2) |
| E-036 | Log Blender | `avaliacao_evidencias/E036_blender_addon_boot_posfix3.txt` | Boot posfix (iteracao 3) |
| E-037 | Log Blender | `avaliacao_evidencias/E037_blender_addon_boot_posfix4.txt` | Boot posfix (iteracao 4) |
| E-038 | Log Blender | `avaliacao_evidencias/E038_blender_addon_boot_posfix5.txt` | Boot posfix (iteracao 5) |
| E-039 | Log Blender | `avaliacao_evidencias/E039_blender_addon_boot_posfix6.txt` | Boot posfix (iteracao 6) |
| E-040 | Log Blender | `avaliacao_evidencias/E040_blender_addon_boot_posfix7.txt` | Boot posfix (sucesso) |
| E-041 | Log Blender | `avaliacao_evidencias/E041_testrunner_blender5_posfix.txt` | Testrunner posfix (falha em testmodel) |
| E-042 | Log Blender | `avaliacao_evidencias/E042_testrunner_blender5_posfix2.txt` | Testrunner posfix (PASS) |
| E-043 | Performance | `avaliacao_evidencias/E043_cli_tempo_posfix.txt` | Tempo da CLI apos correcao |
| E-048 | Log de teste | `avaliacao_evidencias/E048_teste_api_unittest_posfix5.txt` | API IO: 5/5 PASS |
| E-049 | Performance | `avaliacao_evidencias/E049_teste_api_tempo_posfix.txt` | Tempo suite API IO (PASS) |
