# Avisos de terceiros

Este arquivo lista o conteúdo de terceiros copiado, referenciado ou usado neste repositório, e os avisos que as licenças exigem. Atualize-o sempre que uma skill for adicionada, removida ou atualizada.

## 1. Skills copiadas

| Skill(s) | Origem | Autor ou titular | Licença | Observações |
| --- | --- | --- | --- | --- |
| `frontend-design` | anthropics/skills | Anthropic | Apache-2.0 | Texto completo em `frontend-design/LICENSE.txt`. |
| `design-md` (SKILL.md escrito neste repositório; `references/` copiado) | google-labs-code/design.md | Google Labs | Apache-2.0 | Texto completo em `design-md/LICENSE.txt`. |
| `android-compose-styles` | android/skills | Projeto android/skills | Apache-2.0 | Texto completo em `android-compose-styles/LICENSE.txt`. **Modificação:** o campo `name` do frontmatter de `SKILL.md` foi alterado de `styles` para `android-compose-styles`, para casar com o nome da pasta. |
| `gsap-core`, `gsap-frameworks`, `gsap-performance`, `gsap-plugins`, `gsap-react`, `gsap-scrolltrigger`, `gsap-timeline`, `gsap-utils` | greensock/gsap-skills | GreenSock | MIT | Texto MIT na seção 2. |
| `material-3` | hamen/material-3-skill | CWTI Ltd | MIT | Texto MIT na seção 2. |
| `expo-overview`, `expo-router`, `expo-ui`, `expo-native-ui`, `expo-design-system` | expo/skills (plugins/expo/skills/) | 650 Industries, Inc. (Expo) | MIT | Texto MIT na seção 2. |
| `expo-animation` | expo/skills (plugins/expo/skills/) | Emil Kowalski | MIT | Licença própria na pasta: `expo-animation/LICENSE`. Texto MIT na seção 2. |
| `motion` | pacote npm `motion-ai` 14.1.0 | Matt Perry (motion.dev) | MIT | O pacote declara MIT no `package.json` e não inclui arquivo LICENSE. Texto MIT na seção 2. |
| `shadcn` (com `rules/`) | shadcn-ui/ui, pasta `skills/shadcn` | shadcn | MIT | Texto MIT na seção 2. |

## 2. Texto da licença MIT

Aplica-se às skills marcadas como MIT acima. Cada aviso de copyright é mantido junto com o texto da permissão:

- Copyright (c) 2026 GreenSock: skills `gsap-*`.
- Copyright (c) 2026 CWTI Ltd: skill `material-3`.
- Copyright (c) 2025-present 650 Industries, Inc. (aka Expo): skills `expo-overview`, `expo-router`, `expo-ui`, `expo-native-ui` e `expo-design-system`.
- Copyright (c) 2026 Emil Kowalski: skill `expo-animation`.
- Copyright (c) 2023 shadcn: skill `shadcn`.
- Matt Perry (motion.dev), conforme o campo `author` do pacote `motion-ai`: skill `motion`.

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 3. Apache License 2.0

Os textos completos estão nos arquivos de licença de cada pasta: `frontend-design/LICENSE.txt`, `design-md/LICENSE.txt` e `android-compose-styles/LICENSE.txt`.

## 4. Apenas ponteiros, sem conteúdo copiado

Estas skills são só ponteiros para ferramentas de terceiros. O conteúdo do fornecedor não foi copiado:

- `figma-mcp`: as skills oficiais do Figma não foram copiadas. O repositório `figma/mcp-server-guide` não tem arquivo de licença, e o uso é regido pelos Termos do Desenvolvedor do Figma.
- `mobbin-mcp`: sujeito aos termos do Mobbin, com plano pago necessário.
- `higgsfield-mcp`: sujeito aos termos da Higgsfield.
- `transitions-dev`: a biblioteca de Jakubantalik tem licença própria. É gratuita para uso pessoal e comercial, sem redistribuição. Não foi copiada.

## 5. Fontes do projeto de demonstração

Em `clientes/ponto-torrefacao/fontes/`, as fontes Fraunces e Instrument Sans estão em WOFF2. Foram obtidas dos pacotes `@fontsource-variable`. Os arquivos de fonte são distribuídos sob SIL Open Font License 1.1, com os textos em `LICENSE-fraunces.txt` e `LICENSE-instrument-sans.txt`.

## 6. Dependências de build do projeto de demonstração

Estas dependências são instaladas localmente com `npm install` e `pip3`. Não são redistribuídas neste repositório:

| Dependência | Versão | Licença |
| --- | --- | --- |
| `@resvg/resvg-js` | 2.6.2 | MPL-2.0 |
| `puppeteer-core` | 25.13.0 | Apache-2.0 |
| `@sparticuz/chromium` | 153.0.0 | MIT (o pacote inclui um binário do Chromium, sujeito às licenças do Chromium) |
| `fonttools` | 4.66.1 | MIT |
| `brotli` | 1.2.0 | MIT |
| `uharfbuzz` | 0.56.3 | Apache-2.0 |

Ferramenta usada para validar e exportar o DESIGN.md, não incluída no repositório: `@google/design.md` 0.4.0, do projeto google-labs-code/design.md. O repositório tem licença Apache-2.0 (ver `design-md/LICENSE.txt`). O pacote npm 0.4.0 não declara o campo `license`.
