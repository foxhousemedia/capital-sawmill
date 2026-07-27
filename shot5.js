const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const d = await browser.newPage({ viewport: { width: 1400, height: 900 } });
  await d.goto('http://localhost:8777/', { waitUntil: 'domcontentloaded' });
  await d.waitForTimeout(1500);
  await d.evaluate(() => window.scrollTo(0, 260));
  await d.waitForTimeout(800);
  await d.screenshot({ path: '/home/claude/overlap-desktop.png' });
  const m = await browser.newPage({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
  await m.goto('http://localhost:8777/', { waitUntil: 'domcontentloaded' });
  await m.waitForTimeout(1500);
  await m.evaluate(() => window.scrollTo(0, 500));
  await m.waitForTimeout(800);
  await m.screenshot({ path: '/home/claude/overlap-mobile.png' });
  await browser.close();
})();
