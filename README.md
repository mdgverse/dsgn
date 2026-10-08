# dsgn

Espaço de trabalho para um agente de design gráfico. Reúne skills para Claude Code e projetos de identidade visual para clientes.

## Estrutura

- `.claude/skills/`: skills de design. Algumas são cópias do upstream, com a licença original preservada. Outras são ponteiros para ferramentas que exigem conta ou licença própria. Há também skills customizadas em português. O índice está em [`.claude/skills/README.md`](.claude/skills/README.md), e os avisos de terceiros em [`.claude/skills/THIRD_PARTY_NOTICES.md`](.claude/skills/THIRD_PARTY_NOTICES.md).
- `clientes/`: um diretório por cliente. Hoje existe só `clientes/ponto-torrefacao/`, um projeto de demonstração com marca fictícia.
- `AGENTS.md` e `CLAUDE.md`: instruções para agentes que trabalham neste repositório.

## Projeto de demonstração

Abra `clientes/ponto-torrefacao/index.html` em um servidor estático, ou leia [`clientes/ponto-torrefacao/README.md`](clientes/ponto-torrefacao/README.md). O README explica o mapa de pastas, os comandos de regeneração e os limites do material.

## Skills

Cada skill tem um `SKILL.md` com a descrição de uso. O Claude Code carrega a skill quando a tarefa combina com essa descrição. Para identidade visual completa, comece por `identidade-visual`. Para o formato DESIGN.md, use `design-md`.

## Licenças

- As skills copiadas mantêm a licença de origem (MIT ou Apache-2.0). Os textos e avisos estão em `.claude/skills/THIRD_PARTY_NOTICES.md`.
- As fontes em `clientes/ponto-torrefacao/fontes/` são distribuídas sob SIL OFL 1.1.
- O conteúdo autoral deste repositório, como o manual, o site e os logotipos de demonstração, ainda não tem licença definida. Defina a licença antes de publicar ou de usar com um cliente.
