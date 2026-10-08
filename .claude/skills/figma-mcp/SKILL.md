---
name: figma-mcp
description: Ponteiro para o servidor MCP oficial do Figma. Use quando o usuário quiser ler arquivos do Figma, extrair variáveis ou escrever no canvas a partir do Claude Code. Explica como conectar, as condições de uso e onde estão as skills oficiais, que não são copiadas neste repositório.
---

# Figma MCP (ponteiro)

Esta skill não contém conteúdo do Figma. Ela aponta para a configuração oficial e para as condições de uso.

As skills oficiais do Figma não foram copiadas. O repositório `figma/mcp-server-guide` não tem arquivo de licença, e o uso é regido pelos Termos do Desenvolvedor do Figma.

## Conectar

Opção recomendada, pelo plugin do Claude Code:

```bash
claude plugin install figma@claude-plugins-official
```

Alternativa manual:

```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
```

Depois, no Claude Code, rode `/mcp`, escolha o servidor `figma` e clique em Authenticate. A autenticação acontece no navegador, com a sua conta Figma.

## Condições (verificadas em outubro de 2026)

- O servidor está em beta. Interface e limites podem mudar.
- Escrever no canvas é gratuito durante a beta.
- Assentos Starter e View têm limite de taxa.
- É preciso ter acesso ao arquivo Figma que será lido.

## Skills oficiais

As skills oficiais estão no repositório `figma/mcp-server-guide`, nas pastas `skills-figquery/` e `skills/`. Consulte a versão atual no repositório em vez de copiar.

## Documentação

- Catálogo do MCP: figma.com/mcp-catalog
- Instalação do servidor remoto: developers.figma.com, seção de instalação do servidor remoto

Se algum comando falhar, confira a documentação oficial antes de tentar outra alternativa. Os comandos desta skill podem ficar desatualizados.
