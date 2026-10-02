# Instalação rápida

## Essencial
| Ferramenta | Link | Uso |
|---|---|---|
| Node.js LTS | https://nodejs.org/en/download | Necessário para instalar Codex CLI e MCPs baseados em `npx`. |
| Codex CLI | https://developers.openai.com/codex/cli/ | IA com acesso aos arquivos locais; use sua própria conta. |
| Camunda Desktop Modeler | https://docs.camunda.io/downloads/ | Baixe **Desktop Modeler**, não o pacote com runtime. Abre os BPMNs. |

Depois de instalar Node.js, abra o PowerShell:

```powershell
npm install -g @openai/codex
codex login
```

Extraia o ZIP, abra um terminal dentro da pasta e execute `codex`. Cole o prompt de `PROMPT-INICIAL.md`.

## MCP de documentação Camunda
Opcional para consultar a documentação oficial:

```powershell
codex mcp add camunda-docs --url https://camunda-docs.mcp.kapa.ai
codex mcp list
```

Reinicie a sessão da IA após adicionar um servidor. O MCP fornece documentação; quem gera o `.bpmn` é a IA e quem abre/revisa o arquivo é o Modeler. Não é necessário instalar um MCP de cluster.

Referências: [MCP no Codex](https://developers.openai.com/codex/mcp/) e [Camunda Docs MCP](https://docs.camunda.io/docs/8.8/reference/mcp-docs/).

## Draw.io: só para mapas e diagramas conceituais
Desktop: https://github.com/jgraph/drawio-desktop/releases/latest

Plugin oficial para Codex:

```powershell
codex plugin marketplace add jgraph/drawio-mcp
codex plugin add drawio@drawio
```

Se sua versão do Codex não oferecer plugins, atualize o CLI ou use o MCP oficial:

```powershell
codex mcp add drawio -- npx -y @drawio/mcp
```

Escolha plugin **ou** MCP; não é necessário instalar ambos. Referência: https://github.com/jgraph/drawio-mcp

## Alternativas e complementos
- Cursor/Claude Code: use o cliente que já possui; `config/mcp.json.example` mostra as entradas equivalentes. O local do arquivo varia por cliente.
- Python: https://www.python.org/downloads/ — opcional para o validador incluído e leitura programática de documentos.
- Git: https://git-scm.com/downloads/ — opcional; Download ZIP já funciona.
- PowerPoint: https://www.microsoft.com/microsoft-365/powerpoint — para revisar/editar PPTX; se já tem Office, não precisa instalar outro.
- LibreOffice: https://www.libreoffice.org/download/download-libreoffice/ — alternativa para documentos e apresentações, sujeita a diferenças de layout.

Camunda Run, Java, Docker e integrações de execução não são necessários para desenhar e revisar BPMN acadêmico.
