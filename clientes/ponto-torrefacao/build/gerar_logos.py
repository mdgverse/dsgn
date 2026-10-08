#!/usr/bin/env python3
"""
Gera o pacote de logotipos da marca Ponto Torrefação.

- Símbolo: arco de 270° (a escala de torra) + ponto marcado sobre o arco (o "ponto" da torra).
  O arco recebe um recorte circular ao redor do ponto, para que o ponto se leia em qualquer cor.
- Logotipo: "ponto" em Fraunces (instância estática wght 600, SOFT 100, WONK 0, opsz 144),
  com kerning do HarfBuzz e texto convertido em curvas (o SVG não depende de fontes instaladas).

Uso:
    pip install fonttools brotli uharfbuzz
    python3 build/gerar_logos.py

Saída: logo/*.svg  (os PNG são gerados por build/exportar.mjs)
"""
from __future__ import annotations

import math
from io import BytesIO
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = Path(__file__).resolve().parent.parent
FONT_SRC = ROOT / "fontes" / "fraunces-latin-full-normal.woff2"
OUT = ROOT / "logo"

# Paleta (ver DESIGN.md)
TORRA = "#2B1D16"
PERGAMINHO = "#F3EDE2"
CEREJA = "#B8372C"
MEL = "#D9A441"

# Geometria do símbolo (viewBox 120 x 120)
S = 120.0
CX = CY = 60.0
R_ARC = 44.0          # raio da linha central do arco
STROKE = 14.0         # espessura do arco
ANG_START = 135.0     # graus (sistema SVG: y para baixo)
ANG_END = 45.0        # sentido horário, varre 270°
ANG_DOT = 297.0       # posição do ponto (~60% da escala)
R_DOT = 13.0
GAP_KNOCK = 4.5       # folga entre o ponto e o arco (recorte)

# Logotipo
WORD = "ponto"
WEIGHT, SOFT, WONK, OPSZ = 600, 100, 0, 144
XH_TARGET = 0.46 * S  # altura de x do logotipo em relação ao símbolo
TRACKING_EM = -0.012  # ajuste fino de espaçamento
GAP = 0.18 * S        # espaço entre símbolo e logotipo (versão horizontal)
GAP_V = 0.22 * S      # espaço entre símbolo e logotipo (versão vertical)

# Recursos OpenType: kerning ligado; alternativas contextuais (calt) desligadas
# para manter o desenho padrão do "n" e evitar substituições automáticas.
FEATURES = {"kern": True, "liga": False, "calt": False}


def fmt(v: float) -> str:
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def load_static_font() -> TTFont:
    """Lê a Fraunces variável e cria uma instância estática para o logotipo."""
    font = TTFont(str(FONT_SRC))
    static = instancer.instantiateVariableFont(
        font, {"wght": WEIGHT, "SOFT": SOFT, "WONK": WONK, "opsz": OPSZ}
    )
    # A fonte veio de WOFF2; salvar como TTF puro (o HarfBuzz não lê WOFF2 aqui).
    static.flavor = None
    return static


def shape(font: TTFont, text: str):
    """Shaping com HarfBuzz (kerning incluído). Devolve (nome do glifo, avanço, dx, dy)."""
    buf = BytesIO()
    font.save(buf)
    face = hb.Face(buf.getvalue())
    hfont = hb.Font(face)
    b = hb.Buffer()
    b.add_str(text)
    b.guess_segment_properties()
    hb.shape(hfont, b, FEATURES)
    out = []
    for info, pos in zip(b.glyph_infos, b.glyph_positions):
        out.append((font.getGlyphName(info.codepoint), pos.x_advance, pos.x_offset, pos.y_offset))
    return out


def wordmark(font: TTFont, text: str, x0: float, baseline_y: float, size: float):
    """Retorna (path_d, bbox) do texto em curvas, em coordenadas do documento (y para baixo)."""
    upm = font["head"].unitsPerEm
    scale = size / upm
    gs = font.getGlyphSet()
    d_pen = SVGPathPen(gs, ntos=fmt)
    bounds_pen = BoundsPen(gs)
    cursor = 0.0
    for name, adv, xoff, yoff in shape(font, text):
        gx = x0 + (cursor + xoff) * scale
        gy = baseline_y - yoff * scale
        t = (scale, 0, 0, -scale, gx, gy)
        gs[name].draw(TransformPen(d_pen, t))
        gs[name].draw(TransformPen(bounds_pen, t))
        cursor += adv + TRACKING_EM * upm
    xmin, ymin, xmax, ymax = bounds_pen.bounds
    return d_pen.getCommands(), (xmin, ymin, xmax, ymax)


def xheight_em(font: TTFont) -> float:
    gs = font.getGlyphSet()
    bp = BoundsPen(gs)
    gs["x"].draw(bp)
    return bp.bounds[3] / font["head"].unitsPerEm


def arc_path(cx, cy, r, a0, a1):
    """Arco no sentido horário (SVG) de a0 até a1 (graus), varrendo 270°."""
    def pt(a):
        rad = math.radians(a)
        return cx + r * math.cos(rad), cy + r * math.sin(rad)
    x0, y0 = pt(a0)
    x1, y1 = pt(a1)
    sweep = (a1 - a0) % 360
    large = 1 if sweep > 180 else 0
    return f"M{fmt(x0)} {fmt(y0)}A{fmt(r)} {fmt(r)} 0 {large} 1 {fmt(x1)} {fmt(y1)}"


def dot_xy():
    rad = math.radians(ANG_DOT)
    return CX + R_ARC * math.cos(rad), CY + R_ARC * math.sin(rad)


def symbol_group(arc_color: str, dot_color: str, dx: float = 0.0, dy: float = 0.0, uid: str = "s") -> str:
    """Símbolo: arco com recorte circular ao redor do ponto + ponto."""
    dxp, dyp = dot_xy()
    mid = f"recorte-{uid}"
    return (
        f'<defs><mask id="{mid}" maskUnits="userSpaceOnUse" x="-20" y="-20" width="160" height="160">'
        f'<rect x="-20" y="-20" width="160" height="160" fill="#fff"/>'
        f'<circle cx="{fmt(dxp)}" cy="{fmt(dyp)}" r="{fmt(R_DOT + GAP_KNOCK)}" fill="#000"/>'
        f"</mask></defs>"
        f'<g transform="translate({fmt(dx)} {fmt(dy)})">'
        f'<path d="{arc_path(CX, CY, R_ARC, ANG_START, ANG_END)}" fill="none" stroke="{arc_color}" '
        f'stroke-width="{fmt(STROKE)}" stroke-linecap="round" mask="url(#{mid})"/>'
        f'<circle cx="{fmt(dxp)}" cy="{fmt(dyp)}" r="{fmt(R_DOT)}" fill="{dot_color}"/>'
        f"</g>"
    )


def svg_doc(view, body: str, title: str) -> str:
    x, y, w, h = view
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{fmt(x)} {fmt(y)} {fmt(w)} {fmt(h)}" '
        f'width="{fmt(w)}" height="{fmt(h)}" role="img" aria-labelledby="t">'
        f'<title id="t">{title}</title>{body}</svg>\n'
    )


def build_principal(font, color_arc, color_dot, color_word, title, uid):
    """Símbolo + logotipo na horizontal. Símbolo ocupa 0..120; logotipo fica à direita."""
    size = XH_TARGET / xheight_em(font)
    baseline = CY + XH_TARGET / 2          # altura de x centralizada no símbolo
    x0 = S + GAP
    d, (xmin, ymin, xmax, ymax) = wordmark(font, WORD, x0, baseline, size)
    minx, miny = 0.0, min(0.0, ymin)
    maxx, maxy = max(S, xmax), max(S, ymax)
    view = (minx, miny, maxx - minx, maxy - miny)
    body = symbol_group(color_arc, color_dot, uid=uid) + f'<path fill="{color_word}" d="{d}"/>'
    return svg_doc(view, body, title)


def build_logotipo(font, color_word, title):
    size = XH_TARGET / xheight_em(font)
    d, (xmin, ymin, xmax, ymax) = wordmark(font, WORD, 0.0, 0.0, size)
    view = (xmin, ymin, xmax - xmin, ymax - ymin)
    body = f'<path fill="{color_word}" d="{d}"/>'
    return svg_doc(view, body, title)


def build_vertical(font, color_arc, color_dot, color_word, title, uid):
    """Símbolo em cima, logotipo centralizado embaixo. O canvas tem a largura do texto."""
    size = XH_TARGET / xheight_em(font) * 1.05
    _, (xmin, ymin, xmax, ymax) = wordmark(font, WORD, 0.0, 0.0, size)
    text_w = xmax - xmin
    text_h = ymax - ymin
    W = max(S, text_w)
    x0 = (W - text_w) / 2 - xmin           # margem esquerda do texto = centro do canvas
    top_word_y = S + GAP_V
    baseline = top_word_y - ymin           # topo das ascendentes = top_word_y
    d, _ = wordmark(font, WORD, x0, baseline, size)
    H = top_word_y + text_h
    sym_dx = (W - S) / 2                   # símbolo centralizado
    body = symbol_group(color_arc, color_dot, dx=sym_dx, uid=uid) + f'<path fill="{color_word}" d="{d}"/>'
    return svg_doc((0.0, 0.0, W, H), body, title)


def build_simbolo(color_arc, color_dot, title, uid):
    return svg_doc((0.0, 0.0, S, S), symbol_group(color_arc, color_dot, uid=uid), title)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    font = load_static_font()

    files = {
        # Versão principal (positiva, para fundos claros)
        "logo-principal.svg": build_principal(font, TORRA, CEREJA, TORRA,
                                              "Ponto Torrefação — logotipo principal", "p"),
        # Versão negativa (para fundos Torra). Ponto em Mel: contraste 7,2:1 sobre Torra.
        "logo-principal-negativo.svg": build_principal(font, PERGAMINHO, MEL, PERGAMINHO,
                                                       "Ponto Torrefação — logotipo negativo", "n"),
        # Monocromáticas (uma cor só: carimbo, gravação, bordado)
        "logo-monocromatico-torra.svg": build_principal(font, TORRA, TORRA, TORRA,
                                                        "Ponto Torrefação — monocromático Torra", "m1"),
        "logo-monocromatico-pergaminho.svg": build_principal(font, PERGAMINHO, PERGAMINHO, PERGAMINHO,
                                                             "Ponto Torrefação — monocromático Pergaminho", "m2"),
        # Logotipo sem símbolo
        "logotipo.svg": build_logotipo(font, TORRA, "Ponto Torrefação — logotipo (texto)"),
        # Símbolo isolado
        "simbolo.svg": build_simbolo(TORRA, CEREJA, "Ponto Torrefação — símbolo", "s1"),
        "simbolo-negativo.svg": build_simbolo(PERGAMINHO, MEL, "Ponto Torrefação — símbolo negativo", "s2"),
        "simbolo-monocromatico-torra.svg": build_simbolo(TORRA, TORRA, "Ponto Torrefação — símbolo monocromático Torra", "s3"),
        "simbolo-monocromatico-pergaminho.svg": build_simbolo(PERGAMINHO, PERGAMINHO, "Ponto Torrefação — símbolo monocromático Pergaminho", "s4"),
        # Versão vertical (empilhada)
        "logo-vertical.svg": build_vertical(font, TORRA, CEREJA, TORRA,
                                            "Ponto Torrefação — logotipo vertical", "v"),
    }
    for name, svg in files.items():
        (OUT / name).write_text(svg, encoding="utf-8")
        print(f"ok  logo/{name}  ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
