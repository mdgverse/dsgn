# Índice de skills de design

Skills para o Claude Code usadas no trabalho de design gráfico. Cada pasta tem um `SKILL.md` com a descrição de uso. O Claude Code carrega a skill quando a tarefa combina com essa descrição.

Os avisos de licença e de autoria estão em [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## Tipos

- **Cópia:** conteúdo do upstream, sem alterações (salvo quando indicado). A licença original acompanha a pasta ou está no aviso de terceiros.
- **Customizada:** escrita neste repositório, em português.
- **Ponteiro:** só explica como conectar ou instalar uma ferramenta de terceiros. O conteúdo do fornecedor não foi copiado, por restrição de licença.

## Skills de identidade e documentação

| Skill | Tipo | Origem | Licença | Para que serve |
| --- | --- | --- | --- | --- |
| `identidade-visual` | Customizada | Este repositório | Conteúdo autoral | Fluxo completo de identidade: briefing, conceito, logotipo, sistema visual, aplicações, manual, tokens e escopo. |
| `design-md` | Customizada, com `references/` copiado | google-labs-code/design.md | Apache-2.0 | Criar, validar, comparar e exportar um DESIGN.md. As referências da especificação ficam em `design-md/references/`. |
| `frontend-design` | Cópia | anthropics/skills | Apache-2.0 | Direção estética distintiva para UI e para peças. Ajuda a evitar padrões de template. |

## Skills de frameworks e ferramentas de interface

| Skill | Tipo | Origem | Licença | Para que serve |
| --- | --- | --- | --- | --- |
| `material-3` | Cópia | hamen/material-3-skill | MIT | Material Design 3: tokens, componentes, layout, temas e acessibilidade. |
| `android-compose-styles` | Cópia, com nome do frontmatter ajustado | android/skills | Apache-2.0 | Jetpack Compose Styles API. O campo `name` foi alterado de `styles` para `android-compose-styles`. |
| `shadcn` | Cópia, com `rules/` | shadcn-ui/ui (`skills/shadcn`) | MIT | Componentes shadcn/ui: adicionar, configurar, depurar e compor. |

## Skills de animação

| Skill | Tipo | Origem | Licença | Para que serve |
| --- | --- | --- | --- | --- |
| `motion` | Cópia | Pacote npm `motion-ai` 14.1.0 | MIT | Animações com Motion (ex-Framer Motion) e CSS: boas práticas, springs em CSS e auditoria. |
| `gsap-core` | Cópia | greensock/gsap-skills | MIT | API principal do GSAP: `to`, `from`, `fromTo`, easing, stagger e `matchMedia`. |
| `gsap-timeline` | Cópia | greensock/gsap-skills | MIT | Timelines do GSAP: posição, aninhamento e controle de reprodução. |
| `gsap-scrolltrigger` | Cópia | greensock/gsap-skills | MIT | Animações ligadas ao scroll: pin, scrub e gatilhos. |
| `gsap-react` | Cópia | greensock/gsap-skills | MIT | GSAP com React: hook `useGSAP`, refs, `gsap.context()` e limpeza. |
| `gsap-frameworks` | Cópia | greensock/gsap-skills | MIT | GSAP com Vue, Svelte e outros frameworks, com ciclo de vida e escopo de seletores. |
| `gsap-plugins` | Cópia | greensock/gsap-skills | MIT | Plugins do GSAP: ScrollToPlugin, Flip, Draggable, SplitText, entre outros. |
| `gsap-performance` | Cópia | greensock/gsap-skills | MIT | Animações com bom desempenho: transforms, evitar layout thrashing e `will-change`. |
| `gsap-utils` | Cópia | greensock/gsap-skills | MIT | Utilitários do `gsap.utils`: clamp, mapRange, snap, wrap e outros. |

## Skills do Expo

| Skill | Tipo | Origem | Licença | Para que serve |
| --- | --- | --- | --- | --- |
| `expo-overview` | Cópia | expo/skills | MIT | Ponto de entrada para qualquer tarefa de Expo ou EAS. Carregue primeiro. |
| `expo-router` | Cópia | expo/skills | MIT | Roteamento com Expo Router: rotas, grupos, links, stack, modais e tabs. |
| `expo-ui` | Cópia | expo/skills | MIT | Componentes nativos com `@expo/ui`: SwiftUI no iOS e Jetpack Compose no Android. |
| `expo-native-ui` | Cópia | expo/skills | MIT | Telas nativas no estilo Apple HIG: cores semânticas, controles e layout responsivo. |
| `expo-design-system` | Cópia | expo/skills | MIT | Design system dentro de um app Expo: tokens, variantes e estados de componentes. |
| `expo-animation` | Cópia | expo/skills | MIT, com licença própria na pasta | Animações em React Native e Expo: quando animar, em qual thread e com qual mola. |

## Ponteiros para ferramentas de terceiros

| Skill | Tipo | Origem | Licença | Para que serve |
| --- | --- | --- | --- | --- |
| `figma-mcp` | Ponteiro | figma/mcp-server-guide | Termos do Desenvolvedor Figma | Conectar o servidor MCP oficial do Figma. As skills oficiais não foram copiadas. |
| `mobbin-mcp` | Ponteiro | Mobbin | Termos do Mobbin, plano pago | Conectar o MCP do Mobbin para pesquisa de telas e fluxos. |
| `higgsfield-mcp` | Ponteiro | Higgsfield | Termos da Higgsfield | Conectar o MCP da Higgsfield para geração de imagem e vídeo. |
| `transitions-dev` | Ponteiro | Jakubantalik/transitions.dev | Licença própria, sem redistribuição | Instalar a biblioteca de transições, na versão gratuita. |

## Como manter esta pasta

- **Cópias.** Não edite o conteúdo copiado. Para atualizar, substitua a pasta pela versão nova da origem e revise o aviso de licença.
- **Customizadas.** `identidade-visual` e `design-md` são nossas. Edite com cuidado e mantenha o frontmatter válido.
- **Ponteiros.** Confira a documentação oficial antes de usar. Os comandos e os limites de plano podem mudar.
- **Avisos.** Ao adicionar uma skill de terceiros, inclua a entrada em `THIRD_PARTY_NOTICES.md` com o texto da licença.
