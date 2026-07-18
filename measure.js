const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const p = await (await browser.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
  await p.goto('http://localhost:8777/', { waitUntil: 'domcontentloaded' }).catch(()=>{});
  await p.waitForTimeout(600);
  const m = await p.evaluate(() => {
    const bar = document.querySelector('#main-menu').getBoundingClientRect();
    const link = document.querySelector('#main-nav > ul > li:nth-child(2) > a').getBoundingClientRect();
    const logo = document.querySelector('#capital-sawmill-logo').getBoundingClientRect();
    return { barTop: bar.top, barH: bar.height, linkCenter: link.top + link.height/2, logoTop: logo.top };
  });
  console.log(JSON.stringify(m));
  await browser.close();
})();
