const { chromium } = require('playwright'); const fs = require('fs'); const S = process.argv[2];
/* Pixeltest van het einde van het sluiten: vanaf het moment dat het venster het vlak bereikt,
   mag het beeld van het vlak niet meer veranderen (geen flits, geen verspringing).
   Per beeld: gemiddeld pixelverschil met het eindbeeld, binnen het vlak (0-255). */
(async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const html = '<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><style>body{margin:0}</style></head><body>' + fs.readFileSync(S + '/pam-en-sam.html', 'utf8') + '</body></html>';
  const calc = await b.newPage();
  let worstAll = 0;
  for (const [n, opt] of [['desktop', { viewport: { width: 1440, height: 900 } }], ['mobiel', { viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true }]]) {
    for (const v of ['pam', 'sam']) {
      for (const hist of [false, true]) {
        const ctx = await b.newContext(opt); const p = await ctx.newPage();
        await p.setContent(html, { waitUntil: 'networkidle' }); await p.waitForTimeout(400);
        await p.evaluate(v => { document.querySelectorAll('.rv').forEach(x => x.classList.add('shown')); document.querySelector(`.door.${v} .room`).scrollIntoView({ block: 'center' }); }, v); await p.waitForTimeout(600);
        if (hist) { await p.click(`.door.${v} .room`); await p.waitForTimeout(3000); await p.fill('#input', 'Ik weet het niet'); await p.press('#input', 'Enter'); await p.waitForTimeout(1500); await p.click('#closeBtn'); await p.waitForTimeout(1500); }
        await p.click(`.door.${v} .room`); await p.waitForTimeout(450);
        const clip = await p.evaluate(() => { const r = document.getElementById('sendForm').getBoundingClientRect(); return { x: Math.round(r.left) - 4, y: Math.round(r.top) - 4, width: Math.round(r.width) + 8, height: Math.round(r.height) + 8 }; });
        const shots = []; for (let i = 0; i < 40; i++) { shots.push((await p.screenshot({ clip })).toString('base64')); }
        await p.waitForTimeout(600); const fin = (await p.screenshot({ clip })).toString('base64');
        const d = await calc.evaluate(async ([shots, fin]) => {
          const load = src => new Promise(r => { const i = new Image(); i.onload = () => r(i); i.src = 'data:image/png;base64,' + src; });
          const px = async s => { const i = await load(s); const c = document.createElement('canvas'); c.width = i.width; c.height = i.height; const x = c.getContext('2d'); x.drawImage(i, 0, 0); return x.getImageData(0, 0, i.width, i.height).data; };
          const F = await px(fin); const out = [];
          for (const s of shots) { const A = await px(s); let sum = 0; for (let k = 0; k < A.length; k += 4) sum += Math.abs(A[k] - F[k]) + Math.abs(A[k + 1] - F[k + 1]) + Math.abs(A[k + 2] - F[k + 2]); out.push(+(sum / (A.length / 4) / 3).toFixed(2)); }
          return out;
        }, [shots, fin]);
        const worst = Math.max(...d); worstAll = Math.max(worstAll, worst);
        console.log(n, v, hist ? 'opnieuw openen' : 'eerste keer  ', 'verschil met eindbeeld per beeld:', d.join(' '));
        await ctx.close();
      }
    }
  }
  console.log('grootste afwijking', worstAll); await b.close(); })();
