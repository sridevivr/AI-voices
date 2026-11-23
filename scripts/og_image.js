// Screenshot docs/og.html (written by `python -m src.insights site`) to docs/og.png, the 1200x630 link-preview
// image for LinkedIn/X. Needs Node + Playwright with Chromium. Run from the repo root: node scripts/og_image.js
const path = require('path');
const { chromium } = require('playwright');
(async () => {
  const docs = path.join(__dirname, '..', 'docs');
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1200, height: 630 } });
  await pg.goto('file://' + path.join(docs, 'og.html'));
  await pg.waitForTimeout(1200);
  await pg.screenshot({ path: path.join(docs, 'og.png') });
  await b.close();
  console.log('wrote docs/og.png');
})();
