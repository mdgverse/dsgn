# Ponto Torrefação: demonstração de identidade visual

Projeto fictício que mostra um sistema de identidade visual completo, do conceito às aplicações. Marca, nome, pessoas, contatos, endereços, produtos e preços são inventados.

Comece pelo `index.html`, que é o hub com links para todas as peças.

## Como visualizar

Na pasta `clientes/ponto-torrefacao/`, rode um servidor estático:

```bash
python3 -m http.server 8000 --bind 0.0.0.0
```

Depois abra `http://localhost:8000` no navegador. Todos os caminhos são relativos, então a pasta pode ser copiada para qualquer servidor estático.

## Mapa de pastas

| Caminho | Conteúdo |
| --- | --- |
| `index.html` | Hub com links para o manual, o site, as aplicações, os logotipos e os documentos |
| `identidade-completa.html` | Documento único com toda a identidade, para abrir sem as outras pastas. Gerado, não versionado |
| `briefing.md` | Briefing fictício: cliente, público, posicionamento, objetivos e perguntas em aberto |
| `ESCOPO.md` | Fases, entregas, fora do escopo, revisões, critérios de aceite e investimento |
| `DESIGN.md` | Tokens e regras de uso no formato DESIGN.md. É a fonte dos tokens |
| `tokens/tokens.css` | Variáveis CSS geradas a partir do DESIGN.md, com prefixo `ponto` |
| `brand/brand.css` | Estilos de referência: tokens, escala tipográfica e componentes |
| `logo/` | 10 logotipos em SVG, com texto convertido em curvas |
| `logo/png/` | Os mesmos 10 logotipos em PNG de 2000 px, com fundo transparente |
| `fontes/` | Fraunces e Instrument Sans em WOFF2, com as licenças SIL OFL 1.1 |
| `manual/index.html` | Manual de identidade com nove seções |
| `site/index.html` | Site de demonstração, com a home completa |
| `aplicacoes/index.html` | Peças de aplicação. Cada peça com `data-export` vira um PNG |
| `aplicacoes/png/` | PNG exportados das peças e da primeira dobra do site |
| `build/` | Scripts de geração: `gerar_logos.py`, `exportar.mjs`, `gerar_documento_unico.py` e `package.json` |

## Como regenerar

### Logotipos (SVG)

Requer Python 3 com fonttools, brotli e uharfbuzz:

```bash
pip3 install fonttools brotli uharfbuzz
python3 build/gerar_logos.py
```

O script grava os SVG em `logo/`. Os PNG são gerados pelo passo seguinte.

### PNG das aplicações, do site e dos logotipos

```bash
cd build
npm install
npm run exportar
```

O script usa o navegador indicado em `CHROME_PATH`, se a variável existir. Se não existir, procura o Chromium instalado no sistema. Se nenhum for encontrado, usa o Chromium incluído no pacote `@sparticuz/chromium`.

### Tokens (CSS)

Valide o DESIGN.md e gere as variáveis CSS:

```bash
npx @google/design.md lint DESIGN.md
npx @google/design.md export --format css-vars --prefix ponto DESIGN.md > tokens/tokens.css
```

O lint deve terminar com 0 erros.

### Documento único (HTML)

```bash
pip3 install --user --break-system-packages markdown
python3 build/gerar_documento_unico.py
```

O script grava `identidade-completa.html` na raiz do cliente. O arquivo junta briefing, escopo, manual, peças, site de demonstração, arquivos e skills, com fontes, logotipos e imagens embutidos. Ele abre sem as outras pastas. Se as peças mudarem, rode antes `npm run exportar`. O HTML não é versionado: gere de novo sempre que um texto ou uma peça mudar.

## Limites desta demonstração

- **Dados fictícios.** Nomes, pessoas, contatos (domínio `.example`), endereços, produtos e preços não são reais.
- **CMYK aproximado.** Os valores são conversões matemáticas simples. Não há perfil de cor ICC. Faça prova de cor com a gráfica antes de imprimir.
- **Pantone não verificado.** Nenhum equivalente Pantone foi conferido nesta versão.
- **Contraste calculado.** As razões de contraste seguem a fórmula WCAG 2.x. Conferir os pares escolhidos com ferramenta de acessibilidade antes do uso final.
- **Fontes.** Fraunces e Instrument Sans são distribuídas sob SIL OFL 1.1, e as licenças estão em `fontes/`.
- **Site.** É uma demonstração estática. Não há carrinho, cadastro nem pagamento.

## Adaptar para um cliente real

1. Substitua o briefing, o nome, os textos e os contatos.
2. Revise a paleta e os pares de contraste no DESIGN.md.
3. Regenere os logotipos, os PNG e os tokens.
4. Troque as fotos e as ilustrações de demonstração, se houver.
5. Remova os dados fictícios de todos os arquivos antes da entrega.
