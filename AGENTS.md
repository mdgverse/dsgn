# Instruções para agentes

Este repositório é usado por um designer gráfico que cria identidades visuais para clientes. Responda ao usuário em português do Brasil.

## Estrutura

- `.claude/skills/`: skills de design. As cópias do upstream devem ficar sem alterações. Atualize-as pela origem, nunca editando o conteúdo copiado. As skills `identidade-visual` e `design-md` são customizadas. `figma-mcp`, `mobbin-mcp`, `higgsfield-mcp` e `transitions-dev` são ponteiros, sem conteúdo do fornecedor.
- `clientes/<cliente>/`: um diretório por cliente. Cada cliente segue o padrão de `clientes/ponto-torrefacao/`: `README.md`, `briefing.md`, `ESCOPO.md`, `DESIGN.md`, `tokens/`, `brand/`, `logo/`, `fontes/`, `manual/`, `site/`, `aplicacoes/` e `build/`.

## Regras de trabalho

- Dados de demonstração são fictícios. Não invente dados reais, como nomes de pessoas, telefones ou endereços. Para contatos fictícios, use domínios reservados (`.example`).
- Não copie conteúdo de skills de terceiros sem licença compatível. As skills oficiais do Figma e a biblioteca do transitions.dev não são redistribuídas. Use apenas o ponteiro.
- Registre toda origem externa em `.claude/skills/THIRD_PARTY_NOTICES.md` (skills) ou no README do cliente (fontes e demais recursos).
- Não commite `node_modules/`, ambientes virtuais, caches, logs nem binários de navegador. O `.gitignore` já cobre esses casos.
- PNG e SVG gerados ficam versionados apenas quando são entregáveis do cliente.
- O `DESIGN.md` é a fonte dos tokens. Depois de editá-lo, rode `npx @google/design.md lint DESIGN.md`, que deve terminar com 0 erros, e regenere `tokens/tokens.css`.
- Depois de editar `manual/index.html` ou `site/index.html`, confira a estrutura (tags balanceadas, âncoras e imagens existentes) e renderize a página para checar o layout. Mudanças de logotipo exigem regerar os PNG com `build/exportar.mjs`.
- Ao gerar peças longas, escreva o arquivo em partes e verifique se a última linha está completa. Um arquivo truncado pode parecer válido até ser renderizado.

## Preview

- Para o preview estático, rode `python3 -m http.server 8000 --bind 0.0.0.0` dentro de `clientes/ponto-torrefacao/`.
- Código que roda no navegador deve usar caminhos relativos. Nunca use `localhost` ou `127.0.0.1` para acessar outro serviço.

## Git

- A branch da sessão é `arena/761a16c7-dsgn`. Faça commit e push somente nela.
