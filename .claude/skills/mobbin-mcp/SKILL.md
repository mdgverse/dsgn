---
name: mobbin-mcp
description: Ponteiro para o MCP do Mobbin, biblioteca de telas e fluxos de apps e sites para pesquisa de UX. Use quando o usuário pedir referências de interface, padrões de fluxo ou exemplos de telas reais. Explica a conexão e as condições de uso. Não contém conteúdo do Mobbin.
---

# Mobbin MCP (ponteiro)

O Mobbin reúne telas e fluxos de produtos digitais. O MCP dá acesso a essa biblioteca pelo Claude. Esta skill explica só a conexão e as condições de uso. O conteúdo do Mobbin não é redistribuído aqui.

## Condições (verificadas em outubro de 2026)

- Requer plano pago do Mobbin: Pro ou Team.
- Está em beta. Segundo a documentação, o uso é ilimitado durante a beta.
- As telas são de terceiros. Não as reproduza em material de cliente sem permissão. Use-as como referência de padrão, não como peça final.

## Conectar

No Claude Desktop ou no Claude Web, adicione o conector do Mobbin nas configurações. É a forma recomendada pela documentação.

No Claude Code, pelo CLI:

```bash
claude mcp add mobbin --scope user --transport http https://api.mobbin.com/mcp
```

Depois rode `/mcp`, escolha o servidor `mobbin` e clique em Authenticate.

## Documentação

- Cliente Claude Code CLI: docs.mobbin.com, seção MCP, cliente Claude Code CLI
- Página do MCP: mobbin.com, seção MCP
