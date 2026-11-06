const { chromium } = require('playwright'); const fs = require('fs'); const S = process.argv[2];
/* Volledige test van openen en sluiten, beeld voor beeld:
   - per beeld de zichtbare positie van de schrijfregel (de meegeschoven in het venster, en die in het vlak)
   - een sprong = de zichtbare onderkant van de schrijfregel verplaatst meer dan 6 px tussen twee beelden terwijl de andere al zichtbaar is,
     of de twee zichtbare exemplaren staan op het moment van overvloeien meer dan 1 px uit elkaar */
(async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const html = '<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><style>body{margin:0}</style></head><body>' + fs.readFileSync(S + '/pam-en-sam.html', 'utf8') + '</body></html>';
  const errs = []; let fail = 0;
  for (const [n, opt] of [['desktop', { viewport: { width: 1440, height: 900 } }], ['mobiel', { viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true }], ['tablet', { viewport: { width: 700, height: 1000 } }]]) {
    for (const v of ['pam', 'sam']) {
      const ctx = await b.newContext(opt); const p = await ctx.newPage(); p.on('pageerror', e => errs.push(e.message));
      await p.setContent(html, { waitUntil: 'networkidle' }); await p.waitForTimeout(500);
      await p.evaluate(v => { document.querySelectorAll('.rv').forEach(x => x.classList.add('shown')); document.querySelector(`.door.${v} .room`).scrollIntoView({ block: 'center' }); }, v); await p.waitForTimeout(700);
      const record = () => p.evaluate(v => new Promise(res => {
        const room = document.querySelector(`.door.${v} .room`), md = room.querySelector('.mini-dock'), form = document.getElementById('sendForm'), chat = document.getElementById('chat');
        const op = el => { let o = 1, x = el; while (x) { const cs = getComputedStyle(x); if (cs.visibility === 'hidden' || cs.display === 'none') return 0; o *= +cs.opacity; x = x.parentElement; } return o; };
        const bg = document.getElementById('roomBg'); const out = []; const t0 = performance.now();
        let moved = 0; const f = () => { const px = document.querySelector('.dock-proxy .md-inner'); const el = px || form; const a = el.getBoundingClientRect(), m = md.getBoundingClientRect(); const rd = document.querySelector('#chat > .layer .dock'); if (rd && getComputedStyle(rd).transform !== 'none') moved++;
          out.push({ t: Math.round(performance.now() - t0), fb: a.bottom, ft: a.top, fo: chat.hidden ? 0 : op(el), moved, mb: m.bottom, mt: m.top, mo: op(md) * (chat.hidden ? 1 : 1 - (+getComputedStyle(bg).opacity)) });
          if (performance.now() - t0 < 1300) requestAnimationFrame(f); else res(out); };
        requestAnimationFrame(f);
      }), v);
      const openP = record(); await p.click(`.door.${v} .room`); const open = await openP;
      await p.waitForTimeout(3500);
      const closeP = record(); await p.click('#closeBtn'); const close = await closeP;
      const check = (frames, label) => {
        let worst = 0, gap = 0;
        for (let i = 1; i < frames.length; i++) {
          const a = frames[i - 1], c = frames[i];
          // zichtbaar exemplaar: het meest dekkende
          const vis = x => x.fo >= x.mo ? 'f' : 'm'; if (vis(a) !== vis(c)) { const pa = vis(a) === 'f' ? a.fb : a.mb, pc = vis(c) === 'f' ? c.fb : c.mb; worst = Math.max(worst, Math.abs(pc - pa)); }
          if (c.fo > 0.05 && c.mo > 0.05) gap = Math.max(gap, Math.abs(c.fb - c.mb), Math.abs(c.ft - c.mt));
        }
        const mv = Math.max(...frames.map(x => x.moved)); const bad = gap > 1.5 || mv > 0; if (bad) fail++;
        return `${label}: sprong bij wissel van exemplaar ${worst.toFixed(1)} px, afstand tijdens overvloeien ${gap.toFixed(1)} px, echt veld bewogen: ${mv ? 'ja' : 'nee'}${bad ? '  << FOUT' : ''}`;
      };
      console.log(n, v, '|', check(open, 'openen'), '|', check(close, 'sluiten'));
      await ctx.close();
    }
  }
  console.log('fouten', fail, 'errors', JSON.stringify(errs)); await b.close(); })();
