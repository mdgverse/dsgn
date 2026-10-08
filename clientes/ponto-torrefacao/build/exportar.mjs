// Exporta os PNGs da identidade Ponto Torrefação.
//
//   1. aplicacoes/index.html: cada elemento com data-export vira aplicacoes/png/<nome>.png
//   2. site/index.html: primeira dobra da home vira aplicacoes/png/site-home.png
//   3. logo/*.svg: vira logo/png/<nome>.png (fundo transparente, 2000 px de largura)
//
// Uso (dentro da pasta build/):
//   npm install
//   npm run exportar
//
// Navegador: usa CHROME_PATH se definido; senão, Chromium do sistema; senão, o binário
// empacotado em @sparticuz/chromium (Linux x64).

import { execSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join, resolve, basename } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { brotliDecompressSync } from 'node:zlib';

const aqui = dirname(fileURLToPath(import.meta.url));
const raiz = resolve(aqui, '..');

function prepararBibliotecasEmpacotadas() {
  // O binário de @sparticuz/chromium depende de bibliotecas NSS que vêm compactadas no pacote.
  const pacote = join(aqui, 'node_modules', '@sparticuz', 'chromium', 'bin', 'al2023.tar.br');
  if (!existsSync(pacote)) return;
  const destino = join(tmpdir(), 'ponto-al2023');
  const lib = join(destino, 'lib');
  if (!existsSync(lib)) {
    mkdirSync(destino, { recursive: true });
    const tar = join(destino, 'al2023.tar');
    writeFileSync(tar, brotliDecompressSync(readFileSync(pacote)));
    execSync(`tar -xf "${tar}" -C "${destino}"`);
  }
  process.env.LD_LIBRARY_PATH = [lib, process.env.LD_LIBRARY_PATH].filter(Boolean).join(':');
}

async function resolverNavegador() {
  if (process.env.CHROME_PATH) return { caminho: process.env.CHROME_PATH, argumentos: [] };
  for (const bin of ['chromium', 'chromium-browser', 'google-chrome', 'google-chrome-stable']) {
    try {
      const caminho = execSync(`command -v ${bin}`, { encoding: 'utf8' }).trim();
      if (caminho) return { caminho, argumentos: [] };
    } catch {
      /* tenta o próximo */
    }
  }
  prepararBibliotecasEmpacotadas();
  const { default: chromium } = await import('@sparticuz/chromium');
  return { caminho: await chromium.executablePath(), argumentos: chromium.args };
}

async function exportarLogos() {
  const { Resvg } = await import('@resvg/resvg-js');
  const origem = join(raiz, 'logo');
  const destino = join(origem, 'png');
  mkdirSync(destino, { recursive: true });
  for (const arquivo of readdirSync(origem).filter((f) => f.endsWith('.svg'))) {
    const svg = readFileSync(join(origem, arquivo), 'utf8');
    const png = new Resvg(svg, { fitTo: { mode: 'width', value: 2000 }, background: 'rgba(0,0,0,0)' })
      .render()
      .asPng();
    const nome = basename(arquivo, '.svg') + '.png';
    writeFileSync(join(destino, nome), png);
    console.log('logo  ', join('logo', 'png', nome));
  }
}

async function main() {
  await exportarLogos();

  const puppeteer = (await import('puppeteer-core')).default;
  const navegador = await resolverNavegador();
  const browser = await puppeteer.launch({
    executablePath: navegador.caminho,
    args: [...navegador.argumentos, '--no-sandbox', '--disable-dev-shm-usage'],
    headless: true,
  });

  try {
    const saida = join(raiz, 'aplicacoes', 'png');
    mkdirSync(saida, { recursive: true });

    // 1) Aplicações
    const pagina = await browser.newPage();
    await pagina.setViewport({ width: 1400, height: 1000, deviceScaleFactor: 1 });
    await pagina.goto(pathToFileURL(join(raiz, 'aplicacoes', 'index.html')).href, { waitUntil: 'networkidle0' });
    await pagina.evaluate(() => document.fonts.ready);
    const pecas = await pagina.$$('[data-export]');
    for (const peca of pecas) {
      const nome = await peca.evaluate((n) => n.dataset.export);
      const escala = Number(await peca.evaluate((n) => n.dataset.escala || 1));
      await pagina.setViewport({ width: 1400, height: 1000, deviceScaleFactor: escala });
      await peca.screenshot({ path: join(saida, `${nome}.png`), omitBackground: false });
      console.log('peca  ', join('aplicacoes', 'png', `${nome}.png`), `(${escala}x)`);
    }

    // 2) Home do site (primeira dobra)
    const site = await browser.newPage();
    await site.setViewport({ width: 1440, height: 1000, deviceScaleFactor: 1 });
    await site.goto(pathToFileURL(join(raiz, 'site', 'index.html')).href, { waitUntil: 'networkidle0' });
    await site.evaluate(() => document.fonts.ready);
    await site.screenshot({
      path: join(saida, 'site-home.png'),
      clip: { x: 0, y: 0, width: 1440, height: 760 },
    });
    console.log('site  ', join('aplicacoes', 'png', 'site-home.png'));
  } finally {
    await browser.close();
  }
  console.log('Pronto.');
}

main().catch((erro) => {
  console.error(erro);
  process.exit(1);
});
