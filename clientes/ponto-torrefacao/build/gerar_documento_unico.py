#!/usr/bin/env python3
"""Gera identidade-completa.html: um único arquivo com toda a identidade do projeto.

Tudo fica embutido no arquivo: CSS, fontes, logotipos, imagens, o site de
demonstração (em iframe) e os textos (briefing, escopo, DESIGN.md e tokens).
O arquivo abre offline e não depende de outras pastas.

Uso, a partir de clientes/ponto-torrefacao/:
    pip3 install --user --break-system-packages markdown
    python3 build/gerar_documento_unico.py

A saída fica na raiz do cliente. Ela não é versionada: este script a reconstrói.
"""

import base64
import html
from datetime import date
import pathlib
import re
import sys

import markdown

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "identidade-completa.html"
MIME = {".svg": "image/svg+xml", ".png": "image/png", ".woff2": "font/woff2"}

PECAS = [
    ("cartao-frente", "Cartão de visita, frente"),
    ("cartao-verso", "Cartão de visita, verso"),
    ("saco-250g", "Saco de café de 250 g"),
    ("copo-luva", "Copo com luva"),
    ("papel-timbrado", "Papel timbrado"),
    ("assinatura-email", "Assinatura de e-mail"),
    ("post-1", "Post para redes, 1"),
    ("post-2", "Post para redes, 2"),
    ("story", "Story"),
]

CAPITULOS = [
    ("doc-briefing", "01", "Briefing"),
    ("doc-escopo", "02", "Escopo"),
    ("doc-manual", "03", "Manual de identidade"),
    ("doc-pecas", "04", "Peças de aplicação"),
    ("doc-site", "05", "Site de demonstração"),
    ("doc-arquivos", "06", "Arquivos e código"),
    ("doc-skills", "07", "Skills e licenças"),
]

ARQUIVOS = [
    ("briefing.md", "Briefing do cliente fictício, com perguntas em aberto."),
    ("ESCOPO.md", "Fases, entregas, critérios de aceite e o que fica fora."),
    ("manual/index.html", "Manual de identidade, com 9 seções."),
    ("site/index.html", "Site de demonstração, com seletor de torra."),
    ("aplicacoes/index.html", "Peças de aplicação em HTML e CSS, exportadas para PNG."),
    ("aplicacoes/png/", "Exportação em PNG das peças de aplicação."),
    ("logo/", "Dez variações do logotipo, em SVG."),
    ("logo/png/", "As mesmas dez variações, em PNG de 2000 px."),
    ("brand/brand.css", "Tokens e estilos compartilhados pelas páginas."),
    ("tokens/tokens.css", "Variáveis CSS geradas a partir do DESIGN.md."),
    ("DESIGN.md", "Tokens e componentes no formato DESIGN.md."),
    ("fontes/", "Fraunces e Instrument Sans, com licenças SIL OFL 1.1."),
    ("../../.claude/skills/", "Skills de design e avisos de licença, no repositório e fora desta pasta."),
]

CSS_DOC = """
html { scroll-behavior: smooth; }
.doc-capa { box-sizing: border-box; min-height: 100vh; padding: 56px 64px 48px; background: var(--torra); color: var(--pergaminho); display: flex; flex-direction: column; justify-content: space-between; gap: 56px; }
.doc-capa-logo { display: block; width: min(440px, 70vw); height: auto; }
.doc-capa h1 { font-family: var(--fonte-titulo); font-weight: 600; font-size: 72px; line-height: 76px; letter-spacing: -0.012em; margin: 16px 0 24px; color: var(--pergaminho); max-width: 14ch; }
.doc-capa .doc-kicker { color: var(--mel); }
.doc-capa-lead { font-size: 20px; line-height: 30px; max-width: 56ch; margin: 0 0 24px; color: var(--pergaminho); }
.doc-meta { font-size: 14px; line-height: 20px; margin: 0; color: var(--pergaminho); opacity: 0.7; }
.doc-indice { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 12px 24px; }
.doc-indice a { display: block; color: var(--pergaminho); text-decoration: none; border-top: 1px solid rgba(243, 237, 226, 0.28); padding-top: 12px; font-size: 16px; line-height: 24px; }
.doc-indice a:hover { color: var(--mel); }
.doc-indice span { color: var(--mel); margin-right: 10px; font-variant-numeric: tabular-nums; }
.doc-secao { box-sizing: border-box; max-width: 1200px; margin: 0 auto; padding: 96px 64px; border-top: 1px solid rgba(43, 29, 22, 0.16); color: var(--torra); }
.doc-kicker { font-size: 14px; line-height: 20px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: var(--cacau); margin: 0 0 16px; }
.doc-titulo { font-family: var(--fonte-titulo); font-weight: 600; font-size: 49px; line-height: 54px; letter-spacing: -0.012em; color: var(--torra); margin: 0 0 24px; }
.doc-lead { font-size: 20px; line-height: 30px; color: var(--cacau); margin: 0 0 32px; max-width: 60ch; }
.doc-texto { font-size: 16px; line-height: 26px; color: var(--torra); }
.doc-texto h2 { font-family: var(--fonte-titulo); font-weight: 600; font-size: 49px; line-height: 54px; letter-spacing: -0.012em; margin: 0 0 24px; }
.doc-texto h3 { font-family: var(--fonte-titulo); font-weight: 600; font-size: 31px; line-height: 36px; margin: 48px 0 16px; }
.doc-texto h4 { font-family: var(--fonte-titulo); font-weight: 600; font-size: 25px; line-height: 30px; margin: 40px 0 12px; }
.doc-texto h5, .doc-texto h6 { font-size: 16px; line-height: 26px; font-weight: 600; margin: 24px 0 8px; }
.doc-texto p { margin: 0 0 16px; max-width: 70ch; }
.doc-texto ul, .doc-texto ol { margin: 0 0 16px; padding-left: 24px; max-width: 70ch; }
.doc-texto li { margin: 4px 0; }
.doc-texto a { color: var(--cereja); text-underline-offset: 4px; }
.doc-texto code { font-family: ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace; font-size: 0.9em; background: rgba(43, 29, 22, 0.07); padding: 1px 5px; border-radius: 4px; }
.doc-texto table { width: 100%; border-collapse: collapse; margin: 24px 0 32px; font-size: 15px; line-height: 22px; }
.doc-texto th, .doc-texto td { text-align: left; vertical-align: top; padding: 10px 12px; border-bottom: 1px solid rgba(43, 29, 22, 0.16); }
.doc-texto th { font-weight: 600; background: #fbf8f2; }
.doc-texto hr { border: 0; border-top: 1px solid rgba(43, 29, 22, 0.16); margin: 40px 0; }
.doc-texto pre, .doc-arquivos pre { margin: 0 0 32px; white-space: pre-wrap; overflow-wrap: anywhere; }
.doc-texto pre code { background: none; padding: 0; font-size: 14px; }
.doc-galeria { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 40px 32px; }
.doc-peca { margin: 0; }
.doc-peca img { display: block; width: 100%; height: auto; border-radius: var(--raio-md); }
.doc-peca figcaption { margin-top: 12px; font-size: 14px; line-height: 20px; color: var(--cacau); }
.doc-site { display: block; width: 100%; height: 900px; border: 1px solid rgba(43, 29, 22, 0.16); border-radius: var(--raio-md); background: var(--pergaminho); }
.doc-arquivos code { font-family: ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace; font-size: 14px; }
@media (max-width: 760px) {
  .doc-capa { padding: 40px 24px; }
  .doc-capa h1 { font-size: 48px; line-height: 52px; }
  .doc-secao { padding: 64px 24px; }
  .doc-titulo, .doc-texto h2 { font-size: 36px; line-height: 42px; }
}
"""

JS_DOC = """
document.querySelectorAll('iframe.doc-site').forEach(function (quadro) {
  function ajustar() {
    try {
      var doc = quadro.contentDocument;
      if (doc && doc.readyState !== 'loading') {
        quadro.style.height = doc.documentElement.scrollHeight + 'px';
      }
    } catch (e) { /* sem acesso ao conteúdo: mantém a altura padrão */ }
  }
  quadro.addEventListener('load', ajustar);
  window.addEventListener('resize', ajustar);
  ajustar();
});
"""


def ler(caminho):
    return (RAIZ / caminho).read_text(encoding="utf-8")


def uri(caminho):
    """Devolve o arquivo como data URI. O caminho é relativo à raiz do cliente."""
    arq = RAIZ / caminho
    if not arq.is_file():
        sys.exit(f"Arquivo ausente: {caminho}")
    dados = base64.b64encode(arq.read_bytes()).decode("ascii")
    return f"data:{MIME[arq.suffix]};base64,{dados}"


def embutir(texto):
    """Troca referências relativas a logo/, aplicacoes/png/ e fontes/ por data URIs."""
    padrao = re.compile(r"\.\./((?:logo|aplicacoes/png|fontes)/[^\"')\s]+)")
    return padrao.sub(lambda m: uri(m.group(1)), texto)


def subir_titulos(texto):
    """Desce um nível os títulos do Markdown convertido: h1 vira h2, e assim por diante."""
    return re.sub(
        r"<(/?)h(\d)>",
        lambda m: f"<{m.group(1)}h{min(int(m.group(2)) + 1, 6)}>",
        texto,
    )


def markdown_html(caminho):
    texto = ler(caminho)
    # Links para arquivos locais não abrem dentro do documento único: fica só o texto.
    texto = re.sub(r"\[([^\]]+)\]\((?!https?://|#|mailto:)[^)]*\)", r"\1", texto)
    corpo = markdown.markdown(texto, extensions=["tables", "fenced_code", "sane_lists"])
    return subir_titulos(corpo)


def bloco_codigo(caminho):
    return f"<pre><code>{html.escape(ler(caminho))}</code></pre>"


def figura(arquivo, nome):
    return (
        f'<figure class="doc-peca"><img src="{uri(f"aplicacoes/png/{arquivo}.png")}" '
        f'alt="{html.escape(nome)}"><figcaption>{html.escape(nome)}</figcaption></figure>'
    )


def tabela_arquivos():
    linhas = "".join(
        f"<tr><td><code>{html.escape(c)}</code></td><td>{html.escape(d)}</td></tr>"
        for c, d in ARQUIVOS
    )
    return (
        "<table><thead><tr><th>Caminho</th><th>Conteúdo</th></tr></thead>"
        f"<tbody>{linhas}</tbody></table>"
    )


def data_extensa():
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
             "agosto", "setembro", "outubro", "novembro", "dezembro"]
    hoje = date.today()
    return f"{hoje.day} de {meses[hoje.month - 1]} de {hoje.year}"


def main():
    brand = embutir(ler("brand/brand.css"))

    manual = ler("manual/index.html")
    css_manual = re.search(r"<style>(.*?)</style>", manual, re.S).group(1)
    pagina = embutir(re.search(r'<main class="pagina">(.*?)</main>', manual, re.S).group(1))
    rodape = embutir(re.search(r'<footer class="rodape-manual">(.*?)</footer>', manual, re.S).group(1))

    site = ler("site/index.html")
    site = re.sub(
        r'<link[^>]*href="\.\./brand/brand\.css"[^>]*>',
        lambda m: f"<style>{brand}</style>",
        site,
    )
    site = embutir(site)

    indice = "".join(
        f'<a href="#{ancora}"><span>{num}</span>{titulo}</a>' for ancora, num, titulo in CAPITULOS
    )
    capa = f"""<header class="doc-capa">
  <img class="doc-capa-logo" src="{uri('logo/logo-principal-negativo.svg')}" alt="Ponto Torrefação">
  <div>
    <p class="doc-kicker">Projeto de demonstração · dados fictícios</p>
    <h1>Identidade visual completa</h1>
    <p class="doc-capa-lead">Briefing, escopo, manual, peças de aplicação, site de demonstração e arquivos, em um único documento.</p>
    <p class="doc-meta">Gerado em {data_extensa()}</p>
  </div>
  <nav class="doc-indice" aria-label="Sumário">{indice}</nav>
</header>"""

    figuras = "".join(figura(arq, nome) for arq, nome in PECAS)

    corpo = f"""<main class="doc">
<section id="doc-briefing" class="doc-secao">
  <p class="doc-kicker">01 · Ponto de partida</p>
  <div class="doc-texto">{markdown_html('briefing.md')}</div>
</section>
<section id="doc-escopo" class="doc-secao">
  <p class="doc-kicker">02 · Contrato de trabalho</p>
  <div class="doc-texto">{markdown_html('ESCOPO.md')}</div>
</section>
<section id="doc-manual" class="doc-secao">
  <p class="doc-kicker">03 · Manual de identidade</p>
  <div class="pagina">{pagina}</div>
  <div class="rodape-manual">{rodape}</div>
</section>
<section id="doc-pecas" class="doc-secao">
  <p class="doc-kicker">04 · Peças de aplicação</p>
  <h2 class="doc-titulo">Peças de aplicação</h2>
  <div class="doc-galeria">{figuras}</div>
</section>
<section id="doc-site" class="doc-secao">
  <p class="doc-kicker">05 · Site de demonstração</p>
  <h2 class="doc-titulo">Site de demonstração</h2>
  <p class="doc-lead">Página interativa. O seletor de torra funciona dentro do quadro.</p>
  <iframe class="doc-site" title="Site de demonstração da Ponto Torrefação" srcdoc="{html.escape(site, quote=True)}"></iframe>
</section>
<section id="doc-arquivos" class="doc-secao doc-arquivos">
  <p class="doc-kicker">06 · Arquivos e código</p>
  <h2 class="doc-titulo">Arquivos do projeto</h2>
  <div class="doc-texto">{tabela_arquivos()}</div>
  <h2 class="doc-titulo">DESIGN.md</h2>
  <p class="doc-lead">Tokens e componentes no formato DESIGN.md. É a fonte dos tokens do sistema.</p>
  {bloco_codigo('DESIGN.md')}
  <h2 class="doc-titulo">tokens/tokens.css</h2>
  {bloco_codigo('tokens/tokens.css')}
</section>
<section id="doc-skills" class="doc-secao">
  <p class="doc-kicker">07 · Skills e licenças</p>
  <div class="doc-texto">{markdown_html('../../.claude/skills/README.md')}</div>
  <div class="doc-texto">{markdown_html('../../.claude/skills/THIRD_PARTY_NOTICES.md')}</div>
</section>
</main>"""

    documento = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Identidade visual completa, Ponto Torrefação</title>
<meta name="description" content="Documento único com briefing, escopo, manual, peças, site de demonstração e arquivos da identidade visual fictícia da Ponto Torrefação.">
<style>
{brand}
</style>
<style>
{css_manual}
</style>
<style>
{CSS_DOC}
</style>
</head>
<body>
{capa}
{corpo}
<script>
{JS_DOC}
</script>
</body>
</html>
"""

    # Verificações antes de gravar: nada de referências relativas quebradas, nada de
    # endereços locais, ids únicos e âncoras internas existentes.
    if re.search(r'(?:src|href)="\.\./', documento):
        sys.exit("Erro: ainda há referência relativa (../) no documento.")
    if "localhost" in documento or "127.0.0.1" in documento:
        sys.exit("Erro: endereço local encontrado no documento.")
    ids = re.findall(r' id="([^"]+)"', documento)
    duplicados = sorted({i for i in ids if ids.count(i) > 1})
    if duplicados:
        sys.exit(f"Erro: ids duplicados: {duplicados}")
    ancoras = set(re.findall(r'href="#([^"]+)"', documento))
    faltando = sorted(a for a in ancoras if a not in set(ids))
    if faltando:
        sys.exit(f"Erro: âncoras sem destino: {faltando}")

    SAIDA.write_text(documento, encoding="utf-8")
    print(f"{SAIDA.name}: {SAIDA.stat().st_size / 1024 / 1024:.2f} MB, {len(ids)} ids, {len(ancoras)} âncoras internas")


if __name__ == "__main__":
    main()
