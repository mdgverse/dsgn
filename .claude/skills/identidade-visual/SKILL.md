---
name: identidade-visual
description: Use para criar ou revisar uma identidade visual completa para um cliente. Cobre briefing, conceito, logotipo e variações, paleta com contraste WCAG, tipografia, elementos gráficos, iconografia, direção de fotografia, aplicações, manual, tokens no formato DESIGN.md e o escopo do projeto em ESCOPO.md. Acione quando o usuário falar em identidade visual, marca, logotipo, manual de marca, paleta, sistema visual ou escopo de branding.
---

# Identidade visual

Skill de processo. Ela organiza o trabalho de identidade visual do briefing à entrega e aponta para as outras skills do repositório quando a tarefa exige ferramenta específica.

## Quando usar

- Criar uma identidade nova para um cliente, do zero.
- Revisar uma identidade existente e completar o que falta (manual, tokens, aplicações).
- Montar o escopo de um projeto de branding com fases, entregas e critérios de aceite.

Não use para uma peça isolada sem sistema (um cartaz avulso, por exemplo). Nesse caso, use `frontend-design` para a direção visual da peça.

## Fluxo

### 1. Briefing (`briefing.md`)

Registre cliente, negócio, público, concorrência, objetivos, restrições e materiais recebidos. Liste as perguntas que ainda estão em aberto. Não avance para o conceito com perguntas críticas sem resposta, como o nome da marca, o público principal e o canal prioritário.

### 2. Conceito

Escolha uma ideia central e explique em uma frase por que ela serve ao negócio. O conceito deve gerar elementos visuais concretos. Se ele não se traduz em forma, cor ou comportamento, reescreva.

Antes de fechar o conceito, revise contra a seção de processo de `frontend-design`. Ela lista os padrões de template que a marca deve evitar.

### 3. Logotipo

Entregue, no mínimo:

- principal, horizontal, símbolo, vertical;
- monocromático (uma cor só);
- negativo para fundos escuros;
- área de proteção, tamanho mínimo (em px para tela e em mm para impresso) e usos incorretos.

A área de proteção deve ser definida por um elemento do próprio logotipo, por exemplo o diâmetro do ponto do símbolo. Não use medidas arbitrárias.

**Notas técnicas para gerar logotipos em SVG:**

- Converta o texto em curvas. Assim o SVG não depende de fontes instaladas.
- Ao carregar um WOFF2 com fontTools e salvar uma cópia, defina `font.flavor = None` antes de salvar. Sem isso, o HarfBuzz não encontra os glifos.
- Desative `calt` quando o shaping trocar letras por alternativas (o Fraunces troca "n" por "n.alt").
- Para um elemento que se funde com outro na mesma cor (um ponto sobre um arco, por exemplo), faça um recorte por máscara ao redor dele.

### 4. Sistema visual

**Paleta.** Para cada cor, defina o papel: texto, fundo, destaque, apoio. Entregue HEX, RGB e CMYK aproximado. Informe que o CMYK é uma conversão simples, sem perfil ICC, e que precisa de prova de cor na gráfica.

**Contraste.** Calcule a razão WCAG 2.x para cada par de texto e fundo que o sistema usa:

- texto normal: mínimo 4,5:1 (AA), e 7:1 quando possível (AAA);
- texto grande e elementos gráficos: mínimo 3:1.

Liste os pares proibidos, como os que reprovam, no manual.

```python
def luminancia(hex_cor):
    r, g, b = (int(hex_cor[i:i+2], 16) / 255 for i in (1, 3, 5))
    canal = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * canal(r) + 0.7152 * canal(g) + 0.0722 * canal(b)

def contraste(a, b):
    la, lb = sorted((luminancia(a), luminancia(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)
```

**Tipografia.** Defina uma família para títulos e outra para textos. Escreva a escala com razão definida (por exemplo 1,25), com tamanho e entrelinha de cada nível. Indique pesos, tracking, caixa e fallbacks.

**Elementos gráficos.** Escolha de um a três elementos, cada um derivado do conceito. Para cada um, diga quando usar e quando não usar.

**Iconografia.** Use uma grade fixa, traço fixo e cantos padronizados. Mantenha um conjunto pequeno e coerente, com metáforas do mesmo universo.

**Fotografia e ilustração.** Descreva luz, cena, cor e enquadramento. Inclua uma lista do que evitar (banco de imagem genérico, produto sobre fundo branco, sorrisos forçados).

### 5. Aplicações

Comece pelas peças de maior uso: cartão, embalagem, redes sociais, e-mail, papel timbrado e a primeira dobra do site.

- Peças digitais: exporte em 2x para telas de alta densidade.
- Peças para impressão: use sangria de 3 mm, quando o cliente não informar outro valor.
- Revise cada peça no tamanho real de uso (um cartão de 9 × 5 cm, por exemplo) e não só na tela ampliada.

### 6. Manual de identidade

Use a estrutura padrão, com nove seções: essência, conceito, logotipo, cores, tipografia, sistema gráfico, aplicações, código e tokens, entregáveis. Cada regra precisa de exemplo visual, e cada exemplo precisa de legenda.

### 7. Tokens

Gere o DESIGN.md com a skill `design-md`. Depois exporte as variáveis CSS. O lint do DESIGN.md deve terminar com 0 erros.

### 8. Escopo (`ESCOPO.md`)

Inclua fases com entregas e aprovações, o que fica fora do escopo, o número de revisões por fase, os critérios de aceite e o investimento. Deixe o valor como "a definir" se ele não foi combinado.

## Checagens antes de entregar

- **Contraste.** Todos os pares de texto usados no material passam pela função de contraste acima.
- **Logotipo.** Teste em fundo claro, escuro e na cor de destaque. Confirme que o elemento-chave continua legível no tamanho mínimo.
- **Renderização.** Capture a página em um navegador headless e revise por fatias. Procure cortes, rolagem horizontal indesejada, imagens quebradas e fontes não carregadas.
- **Estrutura.** Tags balanceadas, âncoras de sumário que apontam para seções existentes e imagens que existem no disco.
- **Anti-genérico.** Revise a direção contra a seção de processo de `frontend-design`.
- **Dados.** Em material de demonstração, marque os dados como fictícios. Em material real, troque ou remova os dados de exemplo.

## Armadilhas que já apareceram

- **Creme, serifa e acento terroso.** É um dos padrões que `frontend-design` lista como genéricos. Se o cliente não tiver uma razão de marca para ele, procure outra combinação ou justifique a escolha no briefing.
- **Cor de elemento igual ao fundo.** Um elemento que usa a mesma cor do fundo some sem aviso. Vale para escalas, ícones e marcadores. Use um contorno ou um fundo neutro.
- **Arquivo truncado.** Um HTML gerado em uma só escrita pode sair incompleto, sem fechar tags nem seções. Verifique sempre o fim do arquivo e rode a checagem de estrutura.
- **Grade com colunas demais.** Em uma coluna estreita, uma grade de 6 ou 12 colunas com elementos de largura mínima alta empurra o layout para fora da página. Use a largura disponível, não um valor fixo.
- **Logotipo com efeito.** Sombra, contorno ou gradiente no logotipo quebram as versões aprovadas. Documente esses usos como incorretos.

## Estrutura de pastas do projeto

```
clientes/<cliente>/
  README.md          como abrir, mapa de pastas e comandos de regeneração
  briefing.md        briefing
  ESCOPO.md          escopo, fases e critérios de aceite
  DESIGN.md          tokens e regras (fonte)
  tokens/tokens.css  variáveis CSS geradas
  brand/brand.css    estilos de referência
  logo/              SVG e logo/png/ com PNG
  fontes/            WOFF2 e licenças
  manual/index.html  manual de identidade
  site/index.html    site de demonstração
  aplicacoes/        peças e aplicacoes/png/
  build/             scripts de geração
  index.html         hub com links para tudo
```

## Ferramentas do repositório

- `clientes/<cliente>/build/gerar_logos.py`: gera os SVG dos logotipos.
- `clientes/<cliente>/build/exportar.mjs`: exporta PNG das peças, do site e dos logotipos com um navegador headless.
- `npx @google/design.md`: valida e exporta o DESIGN.md (ver a skill `design-md`).
- Ponteiros de ferramentas externas: `figma-mcp`, `mobbin-mcp`, `higgsfield-mcp` e `transitions-dev`.
