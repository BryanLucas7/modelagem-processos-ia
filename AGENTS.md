# Instruções para IA — Modelagem de processos

Este é um kit reutilizável. Não existe empresa, grupo, dono de processo ou etapa escolhida previamente.

## Fontes e escopo
1. Leia o enunciado do novo trabalho em `trabalho/enunciado/` e o briefing em `trabalho/briefing.md`.
2. Priorize enunciado atual > aulas atuais e orientações do professor > modelo docente > exemplos genéricos > documentação externa.
3. Consulte `materiais/aulas/`, `materiais/tarefas/` e `materiais/modelo-apresentacao-as-is.pdf` conforme a atividade. Os enunciados de tarefas contêm casos próprios e não são requisitos automáticos do novo trabalho.
4. `templates/` contém exemplos gerados de estrutura; não são respostas oficiais nem processos reais.
5. Confirme a etapa solicitada: apresentação inicial, descoberta, AS-IS, análise ou TO-BE. Não avance automaticamente para etapas seguintes.

## Antes de desenhar
- Levante participantes, responsabilidades, entradas, atividades, decisões, mensagens, exceções, saídas e sistemas.
- Separe fatos confirmados, hipóteses e lacunas. Pergunte apenas o que altera materialmente o modelo; continue as partes independentes.
- Crie uma especificação textual em `trabalho/especificacao.md` e confira sua aderência às fontes.
- Não atribua entrevistas, métricas ou validações que não ocorreram.
- Modele AS-IS como é hoje, inclusive trabalho manual, esperas e retrabalho; não introduza melhorias ou automações presumidas.
- O TO-BE deve derivar dos problemas identificados e das heurísticas ensinadas.

## Ferramentas e arquivos
- BPMN: arquivo BPMN 2.0 `.bpmn` editável no Camunda Desktop Modeler, `isExecutable="false"`, sem extensões de engine por padrão.
- Landscape, cadeia de valor e arquitetura organizacional: `.drawio` editável no Draw.io Desktop.
- MCP `camunda-docs` consulta documentação; não desenha nem controla o Desktop Modeler.
- Plugin/MCP Draw.io é opcional para mapas conceituais; não substitui BPMN quando o enunciado exige BPMN.
- Não instale ou inicie Camunda Run, Docker, Java, Operate, Tasklist, clusters ou deploy sem pedido de execução.
- Preserve materiais originais e edições manuais. Faça alterações localizadas e cópia antes de regeneração significativa.
- Saídas: `trabalho/fontes/`, `trabalho/exports/` e `trabalho/entrega/`. Nomes simples em minúsculas com hífens.

## Conferência
- XML bem-formado, IDs únicos, referências e BPMN DI válidos.
- Sequência dentro da mesma pool; mensagem entre participantes distintos.
- Gateways e alternativas coerentes; prazos apenas quando sustentados pelo caso.
- Eventos simples não recebem mensagens como se fossem eventos de mensagem. Use eventos/atividades adequados ao ponto de contato.
- Consulte as aulas sobre múltiplos inícios; não crie gatilhos ou condições apenas para contornar uma regra gráfica.
- Percorra cenários nas duas pools e confira quem produz/recebe cada mensagem.
- Evite cruzamentos, sobreposições, textos cortados e diagramas ilegíveis em escala de apresentação.
- Execute `python scripts/validar-bpmn.py trabalho/fontes` quando Python estiver disponível. Isso verifica estrutura, não certifica semântica nem layout.
- Abra na ferramenta desktop e revise visualmente. Não afirme abertura, renderização ou validação que não realizou.
- Use imagens exportadas dos arquivos atuais na apresentação; mantenha os arquivos editáveis.
- Entregue o formato pedido, inclusive PDF consolidado quando solicitado. Pedidos explícitos de somente fontes/PPTX prevalecem sobre padrões do projeto.
- Não envie arquivos, publique ou submeta em sistemas externos sem autorização explícita.

## Dados pessoais
Não inclua credenciais, CPF, telefones pessoais, matrículas, nomes de clientes, arquivos de autenticação ou caminhos locais identificáveis em publicação pública. Preencha os dados pessoais do seu grupo apenas na sua cópia/entrega.
