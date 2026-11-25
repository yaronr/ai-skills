#!/usr/bin/env node
// Render a deck to PDF and one PNG per slide, and fail on overflow.
// Usage: node render_deck.js deck.html deck.pdf [png-dir]   (default png-dir: _work/slides next to the PDF)
// Needs Playwright with Chromium: require('playwright'). Rules: references/deck-standard.md §8.
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const [src, out, dir] = process.argv.slice(2);
  if (!src || !out) {
    console.error('usage: node render_deck.js deck.html deck.pdf [png-dir]');
    process.exit(2);
  }
  const pngDir = dir || path.join(path.dirname(path.resolve(out)), '_work', 'slides');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto('file://' + path.resolve(src), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const font = await page.evaluate(() =>
    getComputedStyle(document.body).fontFamily.split(',')[0].replace(/["']/g, '').trim());
  if (!(await page.evaluate(f => document.fonts.check(`16px "${f}"`), font)))
    console.log(`WARN  font "${font}" did not load; the render falls back to a system font`);

  await page.emulateMedia({ media: 'print' });
  const problems = await page.evaluate(() => [...document.querySelectorAll('.slide')].flatMap((s, i) => {
    const found = [];
    const S = s.getBoundingClientRect();
    const body = s.querySelector('.body');
    const limit = (body || s).getBoundingClientRect();
    (body || s).querySelectorAll('*').forEach(e => {
      const r = e.getBoundingClientRect();
      if (!r.width && !r.height) return;
      if (r.bottom > limit.bottom + 1)
        found.push(`slide ${i + 1}: content overflows its area by ${Math.round(r.bottom - limit.bottom)}px`);
      if (r.right > S.right + 1)
        found.push(`slide ${i + 1}: content runs ${Math.round(r.right - S.right)}px past the right edge`);
    });
    const foot = s.querySelector('.foot');
    if (foot && foot.getBoundingClientRect().bottom > S.bottom + 1) found.push(`slide ${i + 1}: footnote is cut off`);
    return [...new Set(found)].slice(0, 2);
  }));
  await page.pdf({ path: out, width: '1280px', height: '720px', printBackground: true,
                   margin: { top: 0, right: 0, bottom: 0, left: 0 } });

  fs.mkdirSync(pngDir, { recursive: true });
  await page.emulateMedia({ media: 'screen' });
  const slides = await page.$$('.slide');
  for (let i = 0; i < slides.length; i++)
    await slides[i].screenshot({ path: path.join(pngDir, `slide-${String(i + 1).padStart(2, '0')}.png`) });
  await browser.close();

  console.log(`PDF: ${out} · ${slides.length} slide PNGs in ${pngDir}`);
  if (problems.length) {
    console.log('FAIL  overflow\n  ' + problems.join('\n  '));
    process.exit(1);
  }
  console.log('PASS  no overflow');
})();
