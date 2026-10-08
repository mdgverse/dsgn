---
name: higgsfield-mcp
description: Ponteiro para o MCP da Higgsfield, plataforma de geração de imagem e vídeo com pacotes para produção, anúncios pagos e motion design. Use quando o usuário quiser gerar imagens ou vídeos para campanhas com a Higgsfield. Explica o endereço do servidor, os pacotes e o que ainda não foi verificado.
---

# Higgsfield MCP (ponteiro)

Servidor MCP da Higgsfield. Esta skill não contém conteúdo da plataforma.

## Endereço do servidor

```
https://mcp.higgsfield.ai/mcp
```

## Pacotes

- Production
- Paid Ads
- Motion Design

A Higgsfield também oferece um plugin para ChatGPT.

## Conexão

**Não verificado.** O comando de configuração para o Claude Code não foi confirmado na documentação oficial quando esta skill foi preparada. Confira a documentação da Higgsfield antes de usar.

Se precisar de um ponto de partida, use o padrão genérico de servidor HTTP:

```bash
claude mcp add --transport http higgsfield https://mcp.higgsfield.ai/mcp
```

Depois rode `/mcp` e autentique.

## Cuidados

- Verifique na conta como a geração é cobrada antes de gerar em lote.
- Imagens com pessoas reais, marcas de terceiros ou músicas exigem direitos de uso. Confira a licença antes de publicar.
- Registre no projeto qual ferramenta gerou cada imagem ou vídeo.
