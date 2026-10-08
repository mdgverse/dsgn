---
name: design-md
description: Use ao criar, validar, comparar ou exportar um DESIGN.md, o formato do Google Labs para tokens e regras de design system. Cobre o front matter com cores, tipografia, raios, espaçamento e componentes, as seções em prosa e os comandos lint, diff, export e spec do pacote @google/design.md. Acione quando o usuário pedir tokens de design, um DESIGN.md, exportar variáveis CSS ou Tailwind a partir de um sistema visual, ou validar um sistema de design.
---

# DESIGN.md

O DESIGN.md é um arquivo Markdown com duas partes. O **front matter** em YAML guarda os tokens, valores lidos por máquina. O **corpo em prosa** explica como usar esses tokens, lido por pessoas e por agentes. A especificação completa, que é a referência normativa, está em `references/spec.md`. Os exemplos estão em `references/exemplo-DESIGN.md`. Ambos foram copiados do repositório upstream (Apache-2.0, ver `LICENSE.txt` nesta pasta).

## Quando usar

- Criar o DESIGN.md de um cliente ou de um produto a partir de um sistema visual já definido.
- Validar um DESIGN.md existente com `lint`.
- Comparar duas versões do sistema com `diff`, para revisar mudanças.
- Gerar variáveis CSS, Tailwind ou tokens W3C (DTCG) com `export`.

## Estrutura do arquivo

### Front matter

Começa e termina com uma linha `---`. Campos de topo usados neste repositório:

- `version: alpha`
- `name`: nome do sistema
- `description`: uma frase sobre o sistema

Grupos de tokens:

- `colors`: valores HEX entre aspas (`"#2B1D16"`).
- `typography`: níveis com `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing` e, quando precisar, `fontVariation`.
- `rounded`: raios (`sm`, `md`, `lg`, `full`).
- `spacing`: espaços (`xs`, `sm`, `md`, `lg`, `xl`, `xxl`, `xxxl`).
- `components`: componentes com propriedades como `backgroundColor`, `textColor`, `typography`, `rounded` e `padding`.

Referências entre tokens usam chaves: `"{colors.cereja}"` aponta para `colors.cereja`. Use referências em vez de repetir valores, para que uma mudança se propague.

### Corpo em prosa

Use as seções `##` nesta ordem. Pode omitir as que não se aplicam, mas as presentes precisam seguir a sequência:

1. Overview (ou "Brand & Style")
2. Colors
3. Typography
4. Layout (ou "Layout & Spacing")
5. Elevation & Depth (ou "Elevation")
6. Shapes
7. Components
8. Do's and Don'ts

Cada seção explica a intenção e os usos. Não repita os valores do front matter. Diga quando usar cada token e o que evitar.

## Comandos

Rode com `npx @google/design.md` na pasta do arquivo, ou com o caminho completo do DESIGN.md.

```bash
# Validar a estrutura e as referências (saída JSON; use --format=text para ler)
npx @google/design.md lint --format=text DESIGN.md

# Exportar tokens
npx @google/design.md export --format css-vars --prefix ponto DESIGN.md > tokens/tokens.css
npx @google/design.md export --format css-tailwind DESIGN.md > tailwind-theme.css
npx @google/design.md export --format json-tailwind DESIGN.md > tailwind.theme.json
npx @google/design.md export --format dtcg DESIGN.md > tokens.json

# Comparar duas versões
npx @google/design.md diff --format=text DESIGN-antigo.md DESIGN.md

# Imprimir a especificação do formato
npx @google/design.md spec
```

Formatos de export: `css-vars` gera variáveis CSS (`--prefix` define o prefixo), `css-tailwind` gera o `@theme` do Tailwind v4, `json-tailwind` (alias `tailwind`) gera o `theme.extend` do Tailwind v3 e `dtcg` gera tokens W3C.

## Lint: como ler o resultado

A saída lista itens com `severity` (`error`, `warning` ou `info`), uma `message` e uma `rule`. O resumo traz as contagens. Um DESIGN.md pronto termina com `errors: 0` e `warnings: 0`.

Regras que aparecem com mais frequência:

- **broken-ref** (erro): uma referência `{...}` aponta para um token que não existe. Corrija o caminho.
- **orphaned-tokens** (aviso): um token foi declarado e nenhum componente o usa. Ou use o token em um componente, ou remova-o.
- **missing-sections** (info): uma seção opcional, como `spacing` ou `rounded`, não foi definida. O consumidor usa valores padrão. Defina a seção se o sistema depender dela.
- **token-summary** (info): conta cores, escalas, raios, espaços e componentes. Não exige ação.

## Boas práticas

- **Tokens antes de prosa.** Defina cada cor e cada nível tipográfico no front matter, e só depois explique o uso.
- **Papel por cor.** Descreva cada cor pelo papel (texto, fundo, destaque), não pela aparência. Diga também os pares proibidos.
- **Níveis tipográficos com nome de função.** `display`, `headline-lg`, `lead`, `body-md`, `label-md` e `caption` são mais úteis do que `h1`, `h2`, `p`.
- **Componentes com estados.** Use as chaves `-hover`, `-pressed` ou `-disabled` quando o estado mudar de forma visível.
- **Sem valores soltos.** Se um valor aparece na prosa e não está no front matter, ele vira um token ou sai do texto.
- **Diff antes de publicar.** Ao mudar um token, rode `diff` para ver quais componentes mudam.

## Fluxo de trabalho

1. Defina a paleta, a tipografia e os raios a partir do sistema visual aprovado.
2. Escreva o front matter com esses valores.
3. Escreva a prosa, uma seção por vez, na ordem da especificação.
4. Rode `lint` até chegar a 0 erros e 0 avisos.
5. Exporte as variáveis CSS para o projeto (`tokens/tokens.css`).
6. Em revisões, rode `diff` entre a versão aprovada e a nova.

## Referências desta pasta

- `references/spec.md`: especificação completa do formato, com a ordem das seções, o esquema de tokens e o comportamento esperado de consumidores.
- `references/exemplo-DESIGN.md`: exemplo completo para consulta.
- `LICENSE.txt`: licença Apache-2.0 do upstream.
