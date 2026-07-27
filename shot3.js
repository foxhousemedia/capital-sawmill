const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const d = await browser.newPage({ viewport: { width: 1400, height: 900 } });
  await d.goto('http://localhost:8777/#service-area-section', { waitUntil: 'networkidle' });
  await d.waitForTimeout(3500);
  await d.evaluate(() => document.getElementById('service-area-section').scrollIntoView());
  await d.waitForTimeout(2500);
  await d.screenshot({ path: '/home/claude/map-desktop.png' });
  const m = await browser.newPage({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
  await m.goto('http://localhost:8777/#service-area-section', { waitUntil: 'networkidle' });
  await m.waitForTimeout(3500);
  await m.evaluate(() => document.getElementById('service-area-section').scrollIntoView());
  await m.waitForTimeout(2500);
  await m.screenshot({ path: '/home/claude/map-mobile.png' });
  await browser.close();
})();
