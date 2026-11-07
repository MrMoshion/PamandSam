"""Vijf richtingen vanaf nul. Elk bestand: ?s=home|info|pam|sam."""
import os
D = os.path.dirname(os.path.abspath(__file__))
DISC = '6 vragen gratis · geen creditcard · anoniem · gesprekken niet opgeslagen op onze servers'
PAM = [('Fijn dat je er bent. Vertel me rustig wat er speelt.', 'Ik slaap slecht sinds de verhuizing. Het voelt alsof ik nergens thuis ben.'),
       ('Wat mis je het meest?', 'De buurt. Dat iemand me groette als ik naar buiten liep.'),
       ('Wanneer voelde je je hier wél even gezien?', 'Bij de bakker, vorige week. Ze wist mijn naam nog.')]
SAM = [('Vertel me wat er speelt.', 'Ik moet kiezen tussen een promotie en minder uren werken.'),
       ('Wat wil jij, los van anderen?', 'Tijd. Ik wil mijn dochter van school halen.'),
       ('Wat is je conclusie, in één zin?', 'Ik kies voor minder uren, en ik zeg het maandag.')]
NEXT = {'pam': 'Wat zou je morgen kunnen doen om dat vaker te voelen?', 'sam': 'Wat is je eerste stap?'}
STEPS = [('Vertel wat er speelt', 'Schrijf het op zoals het in je hoofd zit. Niemand oordeelt.'),
         ('Beantwoord één vraag', 'Pam of Sam stelt telkens één vraag. Geen advies, geen lijstjes.'),
         ('Kies je eigen stap', 'Je eindigt met één ding dat je zelf kiest, in je eigen woorden.')]
QUOTE = '“Wat je overkomt hoeft je leven niet te bepalen, je kunt kiezen hoe je erop reageert.”'
NOTE = 'Pam en Sam zijn AI-gesprekspartners. Geen therapie of vervanging van professionele hulp. Gaat het niet goed? Bel 113 of 0800-0113, bij direct gevaar 112.'
turns = lambda v: PAM if v == 'pam' else SAM
name = lambda v: 'Pam' if v == 'pam' else 'Sam'
other = lambda v: 'Sam' if v == 'pam' else 'Pam'

def page(key, fonts, css, home, info, chat):
    return f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pam &amp; Sam · {key}</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<style>*{{box-sizing:border-box;margin:0;padding:0}}a{{color:inherit;text-decoration:none}}ul,ol{{list-style:none}}
.screen{{display:none;min-height:100vh}}body[data-s=home] #home,body[data-s=info] #info,body[data-s=pam] #pam,body[data-s=sam] #sam{{display:block}}{css}</style></head>
<body data-s="home"><div class="screen" id="home">{home}</div><div class="screen" id="info">{info}</div>
<div class="screen" id="pam">{chat('pam')}</div><div class="screen" id="sam">{chat('sam')}</div>
<script>const s=new URLSearchParams(location.search).get('s');if(s)document.body.dataset.s=s;</script></body></html>'''

# ============ 1. SIGNAAL — Vercel/Geist, Dieter Rams, Experimental Jetset: zwart, wit, één signaal ============
def sig_nav(): return '<nav class="nav"><b>Pam &amp; Sam</b><span>Hoe het werkt</span><span>Caren</span><span>Tarieven</span><a class="cta">Probeer gratis →</a></nav>'
sig_css = '''
:root{--o:#FF4D00}body{background:#fff;color:#000;font-family:Geist,sans-serif;font-weight:400;-webkit-font-smoothing:antialiased}
.nav{display:grid;grid-template-columns:2fr 1fr 1fr 1fr auto;align-items:center;gap:24px;padding:20px 32px;border-bottom:1px solid #000;font-size:14px}.nav b{font-weight:600}
.cta{background:#000;color:#fff;padding:12px 18px;font-size:14px;font-weight:500}
.h{display:grid;grid-template-columns:repeat(12,1fr);gap:0 24px;padding:0 32px;min-height:calc(100vh - 59px);align-content:end;padding-bottom:32px}
.h .k{grid-column:1/7;font-size:14px;margin-bottom:24px}.h h1{grid-column:1/-1;font-size:clamp(56px,10.5vw,168px);font-weight:600;letter-spacing:-.055em;line-height:.88}
.h h1 em{font-style:normal;color:var(--o)}.h .b{grid-column:1/-1;display:grid;grid-template-columns:repeat(12,1fr);gap:24px;border-top:1px solid #000;margin-top:32px;padding-top:16px;font-size:14px}
.h .b p:nth-child(1){grid-column:1/5;font-size:22px;font-weight:500}.h .b p:nth-child(2){grid-column:7/10;color:#555}.h .b a{grid-column:10/13;justify-self:end;align-self:start}
.i{padding:32px}.i h2{font-size:72px;font-weight:600;letter-spacing:-.045em;line-height:.95;margin:56px 0}.i ol{display:grid;grid-template-columns:repeat(3,1fr);border-top:1px solid #000}
.i li{padding:20px 24px 48px 0;border-right:1px solid #ddd;margin-right:24px}.i li:last-child{border:0}.i li b{display:block;font-size:14px;color:var(--o);margin-bottom:56px}.i li h3{font-size:24px;font-weight:500;letter-spacing:-.02em}.i li p{margin-top:10px;color:#555;line-height:1.5}
.i .q{display:grid;grid-template-columns:4fr 8fr;gap:24px;border-top:1px solid #000;margin-top:72px;padding-top:20px}.i .q p:first-child{font-size:14px}.i .q blockquote{font-size:34px;font-weight:500;letter-spacing:-.03em;line-height:1.15}
.i .n{margin-top:48px;font-size:13px;color:#555;max-width:72ch}
.c{min-height:100vh;display:grid;grid-template-rows:auto 1fr auto;background:#fff}.c.sam{background:#000;color:#fff}
.c header{display:flex;justify-content:space-between;padding:20px 32px;border-bottom:1px solid currentColor;font-size:14px}.c header b{font-weight:600}.c header span{display:flex;gap:28px}
.c .past{padding:32px;display:grid;grid-template-columns:repeat(12,1fr);gap:24px;align-content:start;font-size:14px}
.c .past div{grid-column:span 4;border-top:1px solid #ccc;padding-top:12px}.c.sam .past div{border-color:#333}.c .past i{font-style:normal;color:#888;display:block;margin-bottom:8px}
.c .now{padding:0 32px 24px}.c .now .w{font-size:14px;color:var(--o);margin-bottom:12px}.c .now h2{font-size:clamp(38px,5.4vw,84px);font-weight:600;letter-spacing:-.045em;line-height:.95;max-width:16ch}
.c .in{display:grid;grid-template-columns:1fr auto auto;gap:24px;align-items:center;border-top:1px solid currentColor;padding:18px 32px;font-size:15px}.c .in .f{color:#888;font-size:18px}
.c .send{background:var(--o);color:#000;padding:12px 18px;font-weight:500}.c .alt{text-decoration:underline;text-underline-offset:3px}
@media(max-width:700px){.nav{grid-template-columns:1fr auto;padding:16px 20px}.nav span{display:none}.h{padding:0 20px 24px;grid-template-columns:1fr}.h .k{grid-column:1}.h h1{font-size:60px}
.h .b{grid-template-columns:1fr}.h .b p,.h .b a{grid-column:1!important;justify-self:start!important}.i{padding:20px}.i h2{font-size:44px;margin:32px 0}.i ol{grid-template-columns:1fr}.i li{border:0;border-bottom:1px solid #ddd;margin:0;padding-bottom:28px}.i li b{margin-bottom:16px}
.i .q{grid-template-columns:1fr}.i .q blockquote{font-size:24px}.c header{padding:16px 20px}.c header span span:not(:last-child){display:none}.c .past{padding:20px;grid-template-columns:1fr}.c .past div{grid-column:1}.c .now{padding:0 20px 20px}.c .now h2{font-size:34px}
.c .in{grid-template-columns:1fr auto;padding:16px 20px}.c .in .f{grid-column:1/-1;font-size:16px}}
'''
sig_home = sig_nav() + f'''<section class="h"><p class="k">Iedereen worstelt weleens met zichzelf.</p><h1>Bespreek het met Pam of Sam<em>.</em></h1>
<div class="b"><p>Jij komt op het antwoord.</p><p>{DISC}</p><a class="cta">Probeer gratis →</a></div></section>'''
sig_info = sig_nav() + '<section class="i"><h2>Drie stappen.<br>Niet meer.</h2><ol>' + ''.join(f'<li><b>0{i+1}</b><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS)) + f'</ol><div class="q"><p>Caren Pardovitch, de bron</p><blockquote>{QUOTE}</blockquote></div><p class="n">{NOTE}</p></section>'
def sig_chat(v):
    past = ''.join(f'<div><i>{name(v)} — {q}</i>{a}</div>' for q, a in turns(v))
    return f'''<div class="c {v}"><header><b>Pam &amp; Sam · {name(v)}</b><span><span>Onderwerpen</span><span>Terugblik</span><span>×</span></span></header>
<div class="past">{past}</div><div class="now"><p class="w">{name(v)} vraagt</p><h2>{NEXT[v]}</h2></div>
<div class="in"><span class="f">Schrijf hier…</span><a class="alt">Wissel naar {other(v)}</a><a class="send">Verstuur →</a></div></div>'''

# ============ 2. LIMOEN — 21st 'Lime Frost', zachte neo-brutalisme: één felle kleur, zwarte lijn ============
lim_css = '''
:root{--l:#D6F94C;--k:#111}body{background:var(--l);color:var(--k);font-family:"Space Grotesk",sans-serif}
.nav{display:flex;justify-content:space-between;align-items:center;padding:22px 28px}.nav b{font-size:20px;font-weight:700;letter-spacing:-.02em}.nav span{display:flex;gap:10px}
.pill{display:inline-flex;align-items:center;border:2px solid var(--k);border-radius:999px;padding:10px 18px;font-weight:500;font-size:15px;background:transparent}.pill.f{background:var(--k);color:var(--l)}
.h{padding:40px 28px 56px;min-height:calc(100vh - 86px);display:flex;flex-direction:column;justify-content:space-between}
.h .k{font-size:20px}.h h1{font-size:clamp(52px,8vw,124px);font-weight:700;letter-spacing:-.045em;line-height:.92;margin:18px 0}
.h .row{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap}.h .who{display:flex;gap:14px}
.card{border:2px solid var(--k);border-radius:24px;background:#fff;padding:22px 24px;width:280px}.card b{font-size:28px;font-weight:700;display:block}.card p{margin-top:6px;font-size:15px}
.card.d{background:var(--k);color:var(--l)}.fine{font-size:13px;max-width:34ch;line-height:1.5}
.i{padding:32px 28px 64px}.i h2{font-size:64px;font-weight:700;letter-spacing:-.04em;margin-bottom:32px}.i ol{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.i li{border:2px solid var(--k);border-radius:24px;background:#fff;padding:28px}.i li b{display:inline-flex;width:44px;height:44px;border-radius:50%;background:var(--k);color:var(--l);align-items:center;justify-content:center;font-weight:700}
.i li h3{font-size:24px;margin:24px 0 8px}.i li p{line-height:1.5}.i .q{margin-top:16px;border:2px solid var(--k);border-radius:24px;background:var(--k);color:var(--l);padding:36px}.i .q p{font-size:30px;font-weight:500;letter-spacing:-.02em;line-height:1.2}.i .q small{display:block;margin-top:14px;font-size:14px}
.i .n{margin-top:24px;font-size:14px;max-width:70ch;line-height:1.5}
.c{min-height:100vh;display:flex;flex-direction:column;padding:18px}.c.sam{background:var(--k);color:var(--l)}
.c header{display:flex;justify-content:space-between;align-items:center;padding:4px 8px 18px}.c header b{font-size:18px;font-weight:700}.c header span{display:flex;gap:8px}
.c.sam .pill{border-color:var(--l)}.c .log{flex:1;display:flex;flex-direction:column;justify-content:flex-end;gap:14px;width:min(720px,100%);margin:0 auto}
.c .q{align-self:flex-start;max-width:80%;font-size:24px;font-weight:500;letter-spacing:-.02em;line-height:1.25}.c .q small{display:block;font-size:13px;font-weight:700;margin-bottom:4px}
.c .a{align-self:flex-start;border:2px solid var(--k);border-radius:20px;background:#fff;color:var(--k);padding:14px 18px;font-size:17px;line-height:1.5;max-width:80%;margin-bottom:12px}
.c.sam .a{background:var(--l);border-color:var(--l)}
.c .in{width:min(720px,100%);margin:20px auto 8px;display:flex;gap:10px;align-items:center;border:2px solid var(--k);border-radius:999px;background:#fff;color:#777;padding:8px 8px 8px 22px;font-size:17px}
.c.sam .in{border-color:var(--l)}.c .in span{flex:1}.c .in .pill.f{color:var(--l)}.c.sam .in .pill.f{background:var(--l);color:var(--k);border-color:var(--l)}.c .sw{text-align:center;font-size:14px;text-decoration:underline;margin-bottom:6px}
@media(max-width:700px){.nav{padding:16px}.nav span .pill:not(.f){display:none}.h{padding:24px 16px 32px}.h h1{font-size:52px}.h .who{flex-direction:column;width:100%}.card{width:100%}
.i{padding:20px 16px}.i h2{font-size:40px}.i ol{grid-template-columns:1fr}.i .q p{font-size:22px}.c .q{font-size:19px;max-width:100%}.c .a{font-size:15px;max-width:100%}.c .in{font-size:16px}.c header span .pill:not(:last-child){display:none}}
'''
lim_nav = '<nav class="nav"><b>Pam &amp; Sam</b><span><a class="pill">Hoe het werkt</a><a class="pill">Tarieven</a><a class="pill f">Probeer gratis</a></span></nav>'
lim_home = lim_nav + f'''<section class="h"><div><p class="k">Iedereen worstelt weleens met zichzelf.</p><h1>Bespreek het<br>met Pam of Sam.</h1><p class="k">Jij komt op het antwoord.</p></div>
<div class="row"><div class="who"><div class="card"><b>Pam</b><p>Warm. Ze geeft eerst ruimte aan wat je voelt.</p></div><div class="card d"><b>Sam</b><p>Nuchter. Hij gaat zonder omweg naar de kern.</p></div></div>
<div><a class="pill f">Probeer gratis →</a><p class="fine" style="margin-top:12px">{DISC}</p></div></div></section>'''
lim_info = lim_nav + '<section class="i"><h2>Drie stappen. Niet meer.</h2><ol>' + ''.join(f'<li><b>{i+1}</b><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS)) + f'</ol><div class="q"><p>{QUOTE}</p><small>Caren Pardovitch, de bron achter Pam &amp; Sam</small></div><p class="n">{NOTE}</p></section>'
def lim_chat(v):
    log = ''.join(f'<p class="q"><small>{name(v)}</small>{q}</p><p class="a">{a}</p>' for q, a in turns(v)) + f'<p class="q"><small>{name(v)}</small>{NEXT[v]}</p>'
    return f'''<div class="c {v}"><header><b>{name(v)}</b><span><a class="pill">Onderwerpen</a><a class="pill">Terugblik</a><a class="pill">×</a></span></header>
<div class="log">{log}</div><div class="in"><span>Schrijf hier…</span><a class="pill f">Verstuur</a></div><a class="sw">Wissel naar {other(v)}</a></div>'''

# ============ 3. TERMINAL — 21st 'Graphite Mono' + 'Catppuccin', calm tech: een rustige werkplek ============
ter_css = '''
:root{--bg:#141416;--p:#1C1C20;--ln:#2A2A30;--t:#D9D9DE;--m:#7C7C86;--pam:#C6B4FF;--sam:#8FE3C4}
body{background:var(--bg);color:var(--t);font-family:"JetBrains Mono",monospace;font-size:14px;line-height:1.6}
.nav{display:flex;justify-content:space-between;padding:14px 24px;border-bottom:1px solid var(--ln);color:var(--m)}.nav b{color:var(--t);font-weight:500}.nav span{display:flex;gap:24px}.nav .on{color:var(--t)}
.key{display:inline-block;border:1px solid var(--ln);background:var(--p);padding:2px 8px;border-radius:4px;color:var(--t)}
.h{min-height:calc(100vh - 52px);display:grid;place-items:center;padding:40px 24px}.h .box{width:min(720px,100%)}
.h .k{color:var(--m)}.h h1{font-family:"IBM Plex Sans","JetBrains Mono";font-weight:400;font-size:44px;line-height:1.15;letter-spacing:-.02em;margin:14px 0 6px}
.h .s{color:var(--t)}.h .s b{color:var(--sam);font-weight:400}.h .pick{margin-top:36px;border:1px solid var(--ln);border-radius:8px;background:var(--p)}
.h .pick div{display:flex;justify-content:space-between;align-items:center;padding:14px 18px;border-bottom:1px solid var(--ln)}.h .pick div:last-child{border:0}
.h .pick i{font-style:normal;color:var(--m)}.h .pick .p{color:var(--pam)}.h .pick .sm{color:var(--sam)}.h .fine{margin-top:16px;color:var(--m);font-size:12px}
.i{width:min(760px,100%);margin:0 auto;padding:48px 24px}.i h2{font-family:"IBM Plex Sans";font-weight:400;font-size:34px;margin:6px 0 28px}.i .k{color:var(--m)}
.i ol li{display:grid;grid-template-columns:60px 1fr;padding:14px 0;border-top:1px solid var(--ln)}.i ol b{color:var(--sam);font-weight:400}.i ol h3{font-weight:500;font-size:14px}.i ol p{grid-column:2;color:var(--m)}
.i pre{margin-top:36px;padding:20px;border:1px solid var(--ln);border-radius:8px;background:var(--p);white-space:pre-wrap;font:inherit;color:var(--t)}.i pre i{color:var(--m);font-style:normal}
.i .n{margin-top:28px;color:var(--m);font-size:12px}
.c{min-height:100vh;display:grid;grid-template-columns:240px 1fr}.c aside{border-right:1px solid var(--ln);padding:16px;color:var(--m);display:flex;flex-direction:column;gap:6px}
.c aside b{color:var(--t);font-weight:500;margin-bottom:12px}.c aside .on{color:var(--t);background:var(--p);border-radius:4px;padding:6px 8px;margin:0 -8px}.c aside .new{margin-top:auto;color:var(--t)}
.c main{display:flex;flex-direction:column}.c .top{display:flex;justify-content:space-between;padding:14px 28px;border-bottom:1px solid var(--ln);color:var(--m)}.c .top b{font-weight:400;color:var(--v)}
.c.pam{--v:var(--pam)}.c.sam{--v:var(--sam)}.c .log{flex:1;width:min(720px,100%);margin:0 auto;padding:32px 28px;display:flex;flex-direction:column;justify-content:flex-end;gap:18px}
.c .q{color:var(--v)}.c .q::before{content:attr(data-w) "  ";color:var(--m)}.c .a{padding-left:16px;border-left:1px solid var(--ln)}
.c .in{width:min(720px,100%);margin:0 auto 28px;padding:0 28px}.c .in div{border:1px solid var(--ln);border-radius:8px;background:var(--p);padding:14px 16px;color:var(--m)}
.c .in div::before{content:"› ";color:var(--v)}.c .in p{display:flex;justify-content:space-between;margin-top:10px;color:var(--m);font-size:12px}
@media(max-width:700px){.nav{padding:12px 16px}.nav span span:not(.key){display:none}.h h1{font-size:30px}.i h2{font-size:26px}.c{grid-template-columns:1fr}.c aside{display:none}.c .top{padding:12px 16px}.c .log{padding:20px 16px}.c .in{padding:0 16px}}
'''
ter_nav = '<nav class="nav"><b>pam&amp;sam</b><span><span>hoe het werkt</span><span>tarieven</span><span class="key">probeer gratis ↵</span></span></nav>'
ter_home = ter_nav + f'''<section class="h"><div class="box"><p class="k">// iedereen worstelt weleens met zichzelf</p><h1>Bespreek het met Pam of Sam.</h1><p class="s">Zij stellen de vragen. <b>Jij komt op het antwoord.</b></p>
<div class="pick"><div><span class="p">pam</span><i>warm, geduldig, vraagt naar wat je voelt</i><span class="key">1</span></div><div><span class="sm">sam</span><i>nuchter, kort, vraagt naar de kern</i><span class="key">2</span></div></div>
<p class="fine">{DISC}</p></div></section>'''
ter_info = ter_nav + '<section class="i"><p class="k">// hoe het werkt</p><h2>Drie stappen. Niet meer.</h2><ol>' + ''.join(f'<li><b>0{i+1}</b><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS)) + f'</ol><pre><i>// caren pardovitch, de bron</i>\n{QUOTE}</pre><p class="n">{NOTE}</p></section>'
def ter_chat(v):
    log = ''.join(f'<p class="q" data-w="{name(v).lower()}">{q}</p><p class="a">{a}</p>' for q, a in turns(v)) + f'<p class="q" data-w="{name(v).lower()}">{NEXT[v]}</p>'
    return f'''<div class="c {v}"><aside><b>onderwerpen</b><span class="on">verhuizing / slapen</span><span>werk of tijd</span><span>relatie</span><span class="new">+ nieuw onderwerp</span></aside>
<main><div class="top"><b>{name(v).lower()}</b><span>terugblik · wissel naar {other(v).lower()} · esc</span></div><div class="log">{log}</div>
<div class="in"><div>schrijf hier…</div><p><span>enter = verstuur · shift+enter = nieuwe regel</span><span>tekstgrootte A A A</span></p></div></main></div>'''

# ============ 4. COUTURE — 21st 'Elegant Luxury', modehuizen: diep bordeaux, een contrastrijke Didone ============
cou_css = '''
:root{--bx:#2B0A10;--bl:#F3D9D6;--m:#C79A96;--pam:#F3D9D6;--sam:#E7E1D8}
body{background:var(--bx);color:var(--bl);font-family:Jost,sans-serif;font-weight:300}
.nav{display:flex;justify-content:space-between;align-items:center;padding:28px 48px;font-size:12px;letter-spacing:.18em;text-transform:uppercase}.nav b{font-family:"Bodoni Moda";font-weight:400;font-size:22px;letter-spacing:.02em;text-transform:none}
.nav a.cta{border-bottom:1px solid currentColor;padding-bottom:4px}
.h{min-height:calc(100vh - 88px);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:24px 48px 72px}
.h .k{font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:var(--m)}.h h1{font-family:"Bodoni Moda";font-weight:400;font-size:clamp(56px,9vw,148px);line-height:.95;letter-spacing:-.02em;margin:28px 0}
.h h1 span{display:block;font-style:italic}.h .s{font-size:20px}.h .cta{display:inline-block;margin-top:48px;background:var(--bl);color:var(--bx);padding:16px 34px;font-size:13px;letter-spacing:.18em;text-transform:uppercase;font-weight:400}
.h .fine{margin-top:18px;font-size:12px;color:var(--m);letter-spacing:.04em}
.i{padding:40px 48px 80px;max-width:1100px;margin:0 auto;text-align:center}.i .k{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--m)}
.i h2{font-family:"Bodoni Moda";font-weight:400;font-size:72px;margin:20px 0 64px}.i ol{display:grid;grid-template-columns:repeat(3,1fr);gap:48px}.i li b{font-family:"Bodoni Moda";font-weight:400;font-size:56px;font-style:italic}
.i li h3{font-weight:400;font-size:13px;letter-spacing:.18em;text-transform:uppercase;margin:16px 0 10px}.i li p{color:var(--m);line-height:1.6}
.i blockquote{font-family:"Bodoni Moda";font-size:38px;line-height:1.2;margin:96px auto 0;max-width:24ch}.i small{display:block;margin-top:18px;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--m)}
.i .n{margin-top:72px;font-size:13px;color:var(--m)}
.c{min-height:100vh;display:grid;grid-template-rows:auto 1fr auto;text-align:center}.c.sam{background:#14161A;color:var(--sam);--m:#8E939B}
.c header{display:flex;justify-content:space-between;padding:26px 48px;font-size:12px;letter-spacing:.18em;text-transform:uppercase}.c header b{font-family:"Bodoni Moda";font-weight:400;font-size:18px;letter-spacing:0;text-transform:none}
.c.sam header b{font-family:Jost;font-weight:400}.c .log{display:flex;flex-direction:column;justify-content:center;align-items:center;gap:22px;padding:24px;width:min(760px,100%);margin:0 auto}
.c .old{font-size:15px;color:var(--m);line-height:1.6;max-width:52ch}.c .old i{display:block;font-style:normal;font-size:11px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:4px}
.c .now{font-family:"Bodoni Moda";font-size:clamp(34px,4.4vw,60px);line-height:1.1;margin-top:28px;max-width:18ch}.c.sam .now{font-family:Jost;font-weight:300;letter-spacing:-.02em}
.c .in{width:min(560px,100%);margin:0 auto;padding:0 24px 48px}.c .in .f{border-bottom:1px solid currentColor;padding:14px 0;color:var(--m);font-size:18px}
.c .in p{display:flex;justify-content:space-between;margin-top:18px;font-size:12px;letter-spacing:.18em;text-transform:uppercase}
@media(max-width:700px){.nav{padding:20px}.nav span{display:none}.h{padding:20px}.h h1{font-size:54px}.i{padding:28px 20px}.i h2{font-size:44px;margin-bottom:36px}.i ol{grid-template-columns:1fr;gap:32px}.i blockquote{font-size:26px;margin-top:56px}
.c header{padding:18px 20px}.c header span{display:none}.c .now{font-size:32px}.c .old{font-size:15px}.c .in .f{font-size:16px}}
'''
cou_nav = '<nav class="nav"><span>Hoe het werkt &nbsp;&nbsp; Caren</span><b>Pam &amp; Sam</b><a class="cta">Probeer gratis</a></nav>'
cou_home = cou_nav + f'''<section class="h"><p class="k">Iedereen worstelt weleens met zichzelf</p><h1>Bespreek het<span>met Pam of Sam.</span></h1><p class="s">Jij komt op het antwoord.</p><a class="cta">Probeer gratis</a><p class="fine">{DISC}</p></section>'''
cou_info = cou_nav + '<section class="i"><p class="k">Hoe het werkt</p><h2>Drie stappen.</h2><ol>' + ''.join(f'<li><b>{i+1}</b><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS)) + f'</ol><blockquote>{QUOTE}</blockquote><small>Caren Pardovitch</small><p class="n">{NOTE}</p></section>'
def cou_chat(v):
    old = ''.join(f'<p class="old"><i>{name(v)}: {q}</i>{a}</p>' for q, a in turns(v))
    return f'''<div class="c {v}"><header><span>Onderwerpen</span><b>{name(v)}</b><span>Terugblik &nbsp; ×</span></header>
<div class="log">{old}<p class="now">{NEXT[v]}</p></div><div class="in"><div class="f">Schrijf hier…</div><p><a>Wissel naar {other(v)}</a><a>Verstuur</a></p></div></div>'''

# ============ 5. RASTER — Wim Crouwel, Josef Müller-Brockmann: het raster is het merk, kobalt op wit ============
ras_css = '''
:root{--co:#1E3BFF;--w:#F4F4F0;--k:#0A0A0A}
body{background:var(--w);color:var(--k);font-family:Archivo,sans-serif;font-weight:400}
.g{display:grid;grid-template-columns:repeat(6,1fr);border-left:1px solid var(--co)}.g>*{border-right:1px solid var(--co);border-bottom:1px solid var(--co);padding:16px}
.nav{font-size:13px;text-transform:lowercase}.nav b{grid-column:span 2;font-family:"Archivo Black";font-weight:400;font-size:18px;text-transform:none;color:var(--co)}.nav .cta{background:var(--co);color:#fff}
.h{min-height:calc(100vh - 52px);grid-template-rows:1fr auto auto}.h .big{grid-column:1/-1;display:flex;align-items:flex-end;font-family:"Archivo Black";font-size:clamp(60px,11vw,180px);line-height:.85;letter-spacing:-.04em;color:var(--co)}
.h .k{grid-column:span 2;font-size:15px}.h .s{grid-column:span 2;font-size:26px;font-family:"Archivo Black";line-height:1.05}.h .fine{grid-column:span 1;font-size:11px;line-height:1.45}.h .cta{grid-column:span 1;background:var(--co);color:#fff;font-weight:600;display:flex;align-items:flex-end}
.h .p,.h .sm{grid-column:span 3;display:flex;justify-content:space-between;font-size:15px}.h .p b,.h .sm b{font-family:"Archivo Black";font-weight:400;font-size:40px;line-height:1}.h .sm{background:var(--k);color:var(--w)}
.i .t{grid-column:1/-1;font-family:"Archivo Black";font-size:88px;line-height:.9;letter-spacing:-.03em;color:var(--co);padding-top:48px}.i .st{grid-column:span 2;min-height:300px;display:flex;flex-direction:column}
.i .st b{font-family:"Archivo Black";font-weight:400;font-size:64px;color:var(--co);line-height:1}.i .st h3{margin-top:auto;font-size:20px;font-weight:600}.i .st p{margin-top:8px;line-height:1.5}
.i .q{grid-column:span 4;font-family:"Archivo Black";font-size:30px;line-height:1.15}.i .by{grid-column:span 2;font-size:13px}.i .n{grid-column:1/-1;font-size:13px}
.c{min-height:100vh;display:flex;flex-direction:column}.c.sam{--co:#0A0A0A}.c.sam .g{background:#fff}
.c .top b{grid-column:span 2;font-family:"Archivo Black";font-weight:400;font-size:18px;color:var(--co)}.c .top span{font-size:13px}
.c .log{flex:1;align-content:end}.c .log .no{grid-column:span 1;font-family:"Archivo Black";font-size:32px;color:var(--co);line-height:1}
.c .log .q{grid-column:span 2;font-size:18px;font-weight:600;color:var(--co);line-height:1.3}.c .log .a{grid-column:span 3;font-size:18px;line-height:1.5}
.c .log .q.now{grid-column:span 5;font-family:"Archivo Black";font-weight:400;font-size:44px;line-height:1}
.c .in .f{grid-column:span 4;font-size:18px;color:#888;padding-top:22px;padding-bottom:22px}.c .in .alt{grid-column:span 1;font-size:13px;display:flex;align-items:center}.c .in .send{grid-column:span 1;background:var(--co);color:#fff;font-weight:600;display:flex;align-items:center}
@media(max-width:700px){.g{grid-template-columns:repeat(2,1fr)}.g>*{grid-column:span 2!important}.nav span:not(.cta){display:none}.nav b,.nav .cta{grid-column:span 1!important}
.h .big{font-size:58px;min-height:44vh}.h .p,.h .sm{grid-column:span 1!important;flex-direction:column;gap:8px}.h .p b,.h .sm b{font-size:28px}.i .t{font-size:46px}.i .st{min-height:0}.i .st b{font-size:40px}.i .q{font-size:22px}
.c .top span:not(:last-child){display:none}.c .top b,.c .top span:last-child{grid-column:span 1!important}.c .log .no{display:none}.c .log .q.now{font-size:28px}.c .log .q,.c .log .a{font-size:15px}.c .in .f{font-size:16px}.c .in .alt,.c .in .send{grid-column:span 1!important}}
'''
ras_nav = '<nav class="g nav"><b>Pam &amp; Sam</b><span>hoe het werkt</span><span>caren</span><span>tarieven</span><a class="cta">probeer gratis →</a></nav>'
ras_home = ras_nav + f'''<section class="g h"><div class="big">Bespreek het met Pam of Sam.</div><p class="k">Iedereen worstelt weleens met zichzelf.</p><p class="s">Jij komt op het antwoord.</p><p class="fine">{DISC}</p><a class="cta">probeer gratis →</a>
<div class="p"><b>Pam</b><span>warm</span></div><div class="sm"><b>Sam</b><span>nuchter</span></div></section>'''
ras_info = ras_nav + '<section class="g i"><div class="t">Drie stappen. Niet meer.</div>' + ''.join(f'<div class="st"><b>0{i+1}</b><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(STEPS)) + f'<p class="q">{QUOTE}</p><p class="by">Caren Pardovitch, de bron</p><p class="n">{NOTE}</p></section>'
def ras_chat(v):
    log = ''.join(f'<span class="no">0{i+1}</span><p class="q">{q}</p><p class="a">{a}</p>' for i, (q, a) in enumerate(turns(v))) + f'<span class="no">04</span><p class="q now">{NEXT[v]}</p>'
    return f'''<div class="c {v}"><div class="g top"><b>Pam &amp; Sam / {name(v)}</b><span>onderwerpen</span><span>terugblik</span><span>tekstgrootte</span><span>×</span></div>
<div class="g log">{log}</div><div class="g in"><span class="f">Schrijf hier…</span><a class="alt">wissel naar {other(v).lower()}</a><a class="send">verstuur →</a></div></div>'''

SETS = [('signaal', 'family=Geist:wght@400;500;600', sig_css, sig_home, sig_info, sig_chat),
        ('limoen', 'family=Space+Grotesk:wght@400;500;700', lim_css, lim_home, lim_info, lim_chat),
        ('terminal', 'family=JetBrains+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400', ter_css, ter_home, ter_info, ter_chat),
        ('couture', 'family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;1,6..96,400&family=Jost:wght@300;400', cou_css, cou_home, cou_info, cou_chat),
        ('raster', 'family=Archivo:wght@400;600&family=Archivo+Black', ras_css, ras_home, ras_info, ras_chat)]
for key, f, css, h, i, c in SETS:
    open(os.path.join(D, f'{key}.html'), 'w').write(page(key, f, css, h, i, c))
print('ok')
