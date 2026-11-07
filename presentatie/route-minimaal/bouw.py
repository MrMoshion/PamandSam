"""Bouwt vijf minimalistische richtingen van 'de kamer'. Elk bestand heeft vier schermen: ?s=home|info|pam|sam."""
import os
D = os.path.dirname(os.path.abspath(__file__))

FONTS = {
 'drempel': 'family=Instrument+Serif&family=Inter+Tight:wght@300;400;500',
 'kalk': 'family=Inter:wght@300;400;500&family=EB+Garamond:wght@400',
 'vlakken': 'family=Manrope:wght@300;400;600&family=Young+Serif',
 'avond': 'family=Fraunces:opsz,wght@9..144,300;9..144,400&family=Work+Sans:wght@300;400',
 'toneel': 'family=Courier+Prime:wght@400;700&family=Libre+Franklin:wght@300;400;600',
}

PAM = [('Fijn dat je er bent. Vertel me rustig wat er speelt.', 'Ik slaap slecht sinds de verhuizing. Het voelt alsof ik nergens thuis ben.'),
       ('Wat mis je het meest?', 'De buurt. Dat iemand me groette als ik naar buiten liep.'),
       ('Wanneer voelde je je hier wél even gezien?', 'Bij de bakker, vorige week. Ze wist mijn naam nog.')]
PAM_NEXT = 'Wat zou je morgen kunnen doen om dat vaker te voelen?'
SAM = [('Vertel me wat er speelt.', 'Ik moet kiezen tussen een promotie en minder uren werken.'),
       ('Wat wil jij, los van anderen?', 'Tijd. Ik wil mijn dochter van school halen.'),
       ('Wat is je conclusie, in één zin?', 'Ik kies voor minder uren, en ik zeg het maandag.')]
SAM_NEXT = 'Wat is je eerste stap?'
DISC = '6 vragen gratis · geen creditcard · anoniem · gesprekken niet opgeslagen op onze servers'
STEPS = [('Vertel wat er speelt', 'Schrijf het op zoals het in je hoofd zit. Niemand oordeelt.'),
         ('Beantwoord één vraag', 'Pam of Sam stelt telkens één vraag. Geen advies, geen lijstjes.'),
         ('Kies je eigen stap', 'Je eindigt met één ding dat je zelf kiest, in je eigen woorden.')]

def nav(extra=''):
    return f'<nav class="nav"><a class="logo">Pam &amp; Sam</a><ul><li>Hoe het werkt</li><li>Caren</li><li>Tarieven</li><li class="k"><a class="btn">Probeer gratis</a></li></ul>{extra}</nav>'

def info_body():
    st = ''.join(f'<li><span class="n">0{i+1}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS))
    return f'''<section class="info">
  <p class="eyebrow">Hoe het werkt</p>
  <h2>Drie stappen. Niet meer.</h2>
  <ol class="steps">{st}</ol>
  <div class="caren"><p class="eyebrow">Waar het vandaan komt</p>
    <p class="quote">“Wat je overkomt hoeft je leven niet te bepalen, je kunt kiezen hoe je erop reageert.”</p>
    <p class="by">Caren Pardovitch, adviseur bij Pam &amp; Sam</p></div>
  <p class="note">Pam en Sam zijn AI-gesprekspartners. Geen therapie of vervanging van professionele hulp. Gaat het niet goed? Bel 113 of 0800-0113, bij direct gevaar 112.</p>
</section>'''

def chat(v):
    turns, nxt, other = (PAM, PAM_NEXT, 'Sam') if v == 'pam' else (SAM, SAM_NEXT, 'Pam')
    name = 'Pam' if v == 'pam' else 'Sam'
    lines = ''.join(f'<div class="turn"><p class="q"><span class="who">{name}</span>{q}</p><p class="a">{a}</p></div>' for q, a in turns)
    return f'''<div class="chat {v}">
  <header class="ch"><span class="logo">Pam &amp; Sam</span><ul><li>Onderwerpen</li><li>Terugblik</li><li class="k">×</li></ul></header>
  <main class="log">{lines}<div class="turn"><p class="q"><span class="who">{name}</span>{nxt}</p></div></main>
  <footer class="dock"><div class="field">Schrijf hier…</div><div class="acts"><a class="alt">Wissel naar {other}</a><a class="send">Verstuur</a></div></footer>
</div>'''

def page(key, css, hero):
    return f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Pam &amp; Sam · {key}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{FONTS[key]}&display=swap">
<style>*{{box-sizing:border-box;margin:0;padding:0}}a{{color:inherit;text-decoration:none;cursor:pointer}}ul,ol{{list-style:none}}
.s{{display:none;min-height:100vh}}body[data-s=home] #home,body[data-s=info] #info,body[data-s=pam] #pam,body[data-s=sam] #sam{{display:block}}
.chat{{min-height:100vh;display:flex;flex-direction:column}}.chat .log{{flex:1;display:flex;flex-direction:column;justify-content:flex-end}}
{css}</style></head><body data-s="home">
<div class="s" id="home">{hero}</div>
<div class="s" id="info">{nav()}{info_body()}</div>
<div class="s" id="pam">{chat('pam')}</div>
<div class="s" id="sam">{chat('sam')}</div>
<script>const s=new URLSearchParams(location.search).get('s');if(s)document.body.dataset.s=s;</script></body></html>'''

# ---------------------------------------------------------------- 1. DREMPEL
drempel_css = '''
:root{--bg:#EEE7DC;--ink:#2B231C;--soft:#6E6255;--pam:#B5643A;--pamw:#F4E9DC;--sam:#41607E;--samw:#E6EBEF}
body{background:var(--bg);color:var(--ink);font-family:"Inter Tight",sans-serif;font-weight:300}
.nav{display:flex;justify-content:space-between;align-items:center;padding:32px 64px}.nav .logo{font-family:"Instrument Serif";font-size:26px}
.nav ul{display:flex;gap:36px;align-items:center;font-size:15px;color:var(--soft)}
.btn{display:inline-block;font-size:15px;font-weight:400;color:var(--bg);background:var(--ink);padding:14px 26px;border-radius:999px}
.hero{display:grid;grid-template-columns:1fr 1fr;align-items:end;gap:64px;padding:40px 64px 72px;min-height:calc(100vh - 100px)}
.hero .door{height:72vh;max-height:640px;border-radius:999px 999px 0 0;background:var(--pamw);position:relative;overflow:hidden}
.hero .door::after{content:"";position:absolute;right:0;top:0;bottom:0;width:50%;background:var(--samw)}
.hero .door span{position:absolute;bottom:28px;font-family:"Instrument Serif";font-size:30px;z-index:1}
.hero .door .p{left:32px;color:var(--pam)}.hero .door .sm{right:32px;color:var(--sam);font-family:"Inter Tight";font-weight:400;font-size:24px}
.hero .kick{font-size:18px;color:var(--soft)}.hero h1{font-family:"Instrument Serif";font-weight:400;font-size:84px;line-height:1;letter-spacing:-.01em;margin:20px 0}
.hero .sub{font-size:22px}.hero .row{margin-top:40px;display:flex;flex-direction:column;gap:16px;align-items:flex-start}.fine{font-size:13px;color:var(--soft);max-width:36ch;line-height:1.5}
.info{padding:56px 64px 80px;max-width:1100px}.eyebrow{font-size:13px;color:var(--soft);margin-bottom:14px}
.info h2{font-family:"Instrument Serif";font-weight:400;font-size:56px;margin-bottom:56px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}.steps li{background:#F6F1EA;border-radius:180px 180px 16px 16px;padding:72px 32px 36px;text-align:center}
.steps .n{font-family:"Instrument Serif";font-size:44px;color:var(--pam)}.steps h3{font-weight:400;font-size:20px;margin:14px 0 10px}.steps p{color:var(--soft);line-height:1.55}
.caren{margin:72px 0 0;max-width:42ch}.quote{font-family:"Instrument Serif";font-size:34px;line-height:1.2}.by{margin-top:14px;color:var(--soft)}
.note{margin-top:56px;font-size:14px;color:var(--soft);max-width:60ch;line-height:1.6}
.chat.pam{background:var(--pamw);--v:var(--pam)}.chat.sam{background:var(--samw);--v:var(--sam)}
.ch{display:flex;justify-content:space-between;padding:28px 56px;font-size:14px}.ch .logo{font-family:"Instrument Serif";font-size:22px;color:var(--v)}.ch ul{display:flex;gap:28px;color:var(--soft)}
.log{width:min(640px,100%);margin:0 auto;padding:32px 24px}
.chat .log{position:relative}
.turn{padding:18px 0}.q{color:var(--v);font-size:19px;line-height:1.5}.chat.pam .q{font-family:"Instrument Serif";font-size:24px;line-height:1.35}
.who{display:block;font-family:"Inter Tight";font-size:12px;letter-spacing:.04em;color:var(--soft);margin-bottom:4px}
.a{margin-top:12px;font-size:19px;line-height:1.6}
.dock{width:min(640px,100%);margin:0 auto;padding:12px 24px 48px}.field{font-size:19px;color:var(--soft);padding:16px 24px;border-radius:999px;background:rgba(255,255,255,.7)}
.acts{display:flex;justify-content:space-between;align-items:center;margin-top:18px;font-size:14px}.alt{color:var(--soft);text-decoration:underline;text-underline-offset:4px}
.send{background:var(--v);color:#fff;padding:12px 24px;border-radius:999px}
@media(max-width:700px){.nav{padding:20px}.nav ul li:not(.k){display:none}.hero{grid-template-columns:1fr;padding:12px 20px 40px;gap:28px}.hero .door{height:280px;order:-1}
.hero h1{font-size:50px}.info{padding:32px 20px}.info h2{font-size:38px;margin-bottom:28px}.steps{grid-template-columns:1fr}.steps li{padding:48px 24px 28px}
.ch{padding:18px 20px}.ch ul li:not(.k){display:none}.q,.a{font-size:15px}.chat.pam .q{font-size:19px}.field{font-size:16px}.dock{padding-bottom:28px}}
'''
drempel_hero = nav() + f'''<section class="hero"><div><p class="kick">Iedereen worstelt weleens met zichzelf.</p><h1>Bespreek het met Pam of Sam.</h1>
<p class="sub">Jij komt op het antwoord.</p><div class="row"><a class="btn">Probeer gratis</a><p class="fine">{DISC}</p></div></div>
<div class="door"><span class="p">Pam</span><span class="sm">Sam</span></div></section>'''

# ---------------------------------------------------------------- 2. KALK
kalk_css = '''
:root{--bg:#F5F2EB;--ink:#1F1D1A;--soft:#6B665E;--rule:#D8D2C6;--pam:#9A5B3C;--sam:#3E5568}
body{background:var(--bg);color:var(--ink);font-family:Inter,sans-serif;font-weight:300;font-size:14px}
.nav{display:flex;justify-content:space-between;align-items:center;padding:22px 40px;border-bottom:1px solid var(--rule)}.nav .logo{font-family:"EB Garamond";font-size:20px}
.nav ul{display:flex;gap:28px;align-items:center;font-size:13px}.btn{display:inline-block;border:1px solid var(--ink);padding:10px 18px;font-size:13px;font-weight:400}
.hero{min-height:calc(100vh - 70px);display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:40px;padding:40px}
.hero .t{grid-column:2/4;align-self:center}.hero .kick{font-size:13px;color:var(--soft)}.hero h1{font-family:"EB Garamond";font-weight:400;font-size:44px;line-height:1.15;margin:18px 0 12px}
.hero .sub{font-size:15px}.hero .row{margin-top:36px;display:flex;gap:24px;align-items:center}.fine{font-size:12px;color:var(--soft);max-width:34ch;line-height:1.55}
.hero .keys{grid-column:4;align-self:end;display:flex;flex-direction:column;gap:8px;font-size:13px}.hero .keys span{display:flex;justify-content:space-between;border-top:1px solid var(--rule);padding-top:8px}
.hero .keys i{font-style:normal;color:var(--soft)}
.info{display:grid;grid-template-columns:1fr 3fr;gap:40px;padding:56px 40px}.eyebrow{font-size:12px;color:var(--soft)}
.info h2{font-family:"EB Garamond";font-weight:400;font-size:34px;grid-column:2;margin:-6px 0 24px}.info>.eyebrow{grid-column:1;grid-row:1}
.steps{grid-column:2;border-top:1px solid var(--ink)}.steps li{display:grid;grid-template-columns:60px 220px 1fr;gap:20px;padding:18px 0;border-bottom:1px solid var(--rule)}
.steps .n{color:var(--soft)}.steps h3{font-weight:400;font-size:14px}.steps p{color:var(--soft);line-height:1.6}
.caren{grid-column:2;margin-top:48px;max-width:46ch}.caren .eyebrow{margin-bottom:12px}.quote{font-family:"EB Garamond";font-size:24px;line-height:1.35}.by{margin-top:10px;color:var(--soft)}
.note{grid-column:2;margin-top:48px;color:var(--soft);max-width:70ch;line-height:1.6}
.chat{background:var(--bg)}.chat.pam{--v:var(--pam)}.chat.sam{--v:var(--sam)}
.ch{display:flex;justify-content:space-between;padding:22px 40px;border-bottom:1px solid var(--rule);font-size:13px}.ch .logo{font-family:"EB Garamond";font-size:18px}
.chat.sam .ch .logo{font-family:Inter;font-weight:400;font-size:15px}.ch ul{display:flex;gap:24px;color:var(--soft)}
.ch .logo::after{content:"";display:inline-block;width:7px;height:7px;background:var(--v);margin-left:10px;vertical-align:2px}
.log{width:min(560px,100%);margin:0 auto;padding:40px 24px}.turn{padding:16px 0;border-bottom:1px solid var(--rule)}
.who{display:block;font-size:11px;color:var(--v);margin-bottom:6px;font-weight:400}.q{font-size:15px;line-height:1.55;color:var(--v)}
.chat.pam .q{font-family:"EB Garamond";font-size:18px;line-height:1.4}.chat.pam .who{font-family:Inter}.a{margin-top:10px;font-size:15px;line-height:1.65}
.dock{width:min(560px,100%);margin:0 auto;padding:16px 24px 40px}.field{border:1px solid var(--ink);padding:14px 16px;font-size:15px;color:var(--soft)}
.acts{display:flex;justify-content:space-between;align-items:center;margin-top:14px;font-size:13px}.alt{color:var(--soft)}.send{background:var(--ink);color:var(--bg);padding:10px 18px}
@media(max-width:700px){.nav{padding:18px 20px}.nav ul li:not(.k){display:none}.hero{grid-template-columns:1fr;padding:32px 20px}.hero .t,.hero .keys{grid-column:1}
.hero h1{font-size:34px}.hero .row{flex-direction:column;align-items:flex-start}.info{grid-template-columns:1fr;padding:32px 20px}.info>*{grid-column:1!important}
.steps li{grid-template-columns:30px 1fr;}.steps li p{grid-column:2}.ch{padding:18px 20px}.ch ul li:not(.k){display:none}}
'''
kalk_hero = nav() + f'''<section class="hero"><div class="t"><p class="kick">Iedereen worstelt weleens met zichzelf.</p><h1>Bespreek het met Pam of Sam.</h1>
<p class="sub">Jij komt op het antwoord.</p><div class="row"><a class="btn">Probeer gratis</a><p class="fine">{DISC}</p></div></div>
<div class="keys"><span>Pam <i>warm en empathisch</i></span><span>Sam <i>direct en nuchter</i></span><span>Caren <i>de bron</i></span></div></section>'''

# ---------------------------------------------------------------- 3. VLAKKEN (Albers)
vlakken_css = '''
:root{--bg:#F2EEE6;--ink:#211E1A;--soft:#5F584F;--p1:#E9D3B4;--p2:#D9A66F;--p3:#B86A3A;--s1:#CCD6DD;--s2:#8FA3B4;--s3:#3F5A73}
body{background:var(--bg);color:var(--ink);font-family:Manrope,sans-serif;font-weight:300}
.nav{display:flex;justify-content:space-between;align-items:center;padding:28px 56px}.nav .logo{font-family:"Young Serif";font-size:22px}
.nav ul{display:flex;gap:32px;align-items:center;font-size:15px}.btn{display:inline-block;background:var(--ink);color:var(--bg);padding:15px 26px;font-weight:600;font-size:15px}
.hero{display:grid;grid-template-columns:1.1fr 1fr;gap:56px;align-items:center;padding:24px 56px 56px;min-height:calc(100vh - 100px)}
.sq{display:grid;grid-template-columns:1fr 1fr;gap:16px}.sq div{aspect-ratio:1;display:flex;align-items:center;justify-content:center}
.sq .a1{background:var(--p1)}.sq .a1 i{width:72%;height:72%;background:var(--p2);display:flex;align-items:center;justify-content:center}.sq .a1 i b{width:55%;height:55%;background:var(--p3)}
.sq .b1{background:var(--s1)}.sq .b1 i{width:72%;height:72%;background:var(--s2);display:flex;align-items:center;justify-content:center}.sq .b1 i b{width:55%;height:55%;background:var(--s3)}
.sq i{display:block}.sq b{display:block}.sq small{grid-column:span 1;font-size:14px;display:flex;justify-content:space-between}
.hero .kick{font-size:17px;color:var(--soft)}.hero h1{font-family:"Young Serif";font-weight:400;font-size:64px;line-height:1.05;margin:18px 0}.hero .sub{font-size:21px}
.hero .row{margin-top:36px;display:flex;flex-direction:column;gap:14px;align-items:flex-start}.fine{font-size:13px;color:var(--soft);max-width:36ch;line-height:1.5}
.info{padding:48px 56px 80px}.eyebrow{font-size:14px;color:var(--soft);margin-bottom:12px}.info h2{font-family:"Young Serif";font-weight:400;font-size:48px;margin-bottom:40px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:0}.steps li{padding:40px 32px;min-height:300px}.steps li:nth-child(1){background:var(--p1)}.steps li:nth-child(2){background:#E4DCCF}.steps li:nth-child(3){background:var(--s1)}
.steps .n{font-family:"Young Serif";font-size:52px}.steps h3{font-weight:600;font-size:19px;margin:22px 0 10px}.steps p{line-height:1.55;color:var(--soft)}
.caren{margin-top:56px;display:grid;grid-template-columns:1fr 2fr;gap:56px}.quote{font-family:"Young Serif";font-size:30px;line-height:1.25}.by{color:var(--soft);margin-top:12px}
.note{margin-top:48px;font-size:14px;color:var(--soft);max-width:64ch;line-height:1.6}
.chat.pam{background:var(--p1);--v:var(--p3);--d:var(--p2)}.chat.sam{background:var(--s1);--v:var(--s3);--d:var(--s2)}
.chat .log,.chat .dock{background:#FBF8F3;width:min(760px,calc(100% - 112px));margin:0 auto}.chat.sam .log,.chat.sam .dock{background:#F6F8F9}
.ch{display:flex;justify-content:space-between;padding:28px 56px;font-size:14px}.ch .logo{font-family:"Young Serif";font-size:20px}.chat.sam .ch .logo{font-family:Manrope;font-weight:600}.ch ul{display:flex;gap:26px}
.log{padding:48px 56px 16px}.turn{padding:16px 0}.who{display:block;font-size:12px;font-weight:600;letter-spacing:.04em;margin-bottom:4px;color:var(--v)}
.q{font-size:19px;line-height:1.5;color:var(--v)}.chat.pam .q{font-family:"Young Serif";font-size:21px}.a{margin-top:10px;font-size:19px;line-height:1.6;padding-left:16px;border-left:4px solid var(--d)}
.dock{padding:16px 56px 40px;margin-bottom:56px!important}.field{background:var(--d);color:#fff;padding:18px 20px;font-size:18px}.chat.pam .field{color:var(--ink)}
.acts{display:flex;justify-content:space-between;align-items:center;margin-top:16px;font-size:14px}.alt{text-decoration:underline;text-underline-offset:4px}.send{background:var(--v);color:#fff;padding:13px 24px;font-weight:600}
@media(max-width:700px){.nav{padding:20px}.nav ul li:not(.k){display:none}.hero{grid-template-columns:1fr;padding:12px 20px 40px;gap:28px}.hero h1{font-size:42px}
.info{padding:28px 20px}.info h2{font-size:34px}.steps{grid-template-columns:1fr}.steps li{min-height:0;padding:28px 22px}.caren{grid-template-columns:1fr;gap:12px}
.ch{padding:18px 20px}.ch ul li:not(.k){display:none}.chat .log,.chat .dock{width:calc(100% - 24px)}.log{padding:28px 20px 8px}.dock{padding:12px 20px 24px;margin-bottom:12px!important}
.q,.a{font-size:15px}.chat.pam .q{font-size:17px}.field{font-size:16px}}
'''
vlakken_hero = nav() + f'''<section class="hero"><div><p class="kick">Iedereen worstelt weleens met zichzelf.</p><h1>Bespreek het met Pam of Sam.</h1>
<p class="sub">Jij komt op het antwoord.</p><div class="row"><a class="btn">Probeer gratis</a><p class="fine">{DISC}</p></div></div>
<div class="sq"><div class="a1"><i><b></b></i></div><div class="b1"><i><b></b></i></div><small><span>Pam</span><span>warm</span></small><small><span>Sam</span><span>nuchter</span></small></div></section>'''

# ---------------------------------------------------------------- 4. AVOND
avond_css = '''
:root{--bg:#26211D;--ink:#EFE6DA;--soft:#A99C8C;--rule:#3B342E;--lamp:#F2C88A;--pam:#E3B27A;--pamr:#2E2620;--sam:#9DB4C8;--samr:#1F2429}
body{background:var(--bg);color:var(--ink);font-family:"Work Sans",sans-serif;font-weight:300}
.nav{display:flex;justify-content:space-between;align-items:center;padding:30px 60px}.nav .logo{font-family:Fraunces;font-size:24px;font-weight:300}
.nav ul{display:flex;gap:34px;align-items:center;font-size:15px;color:var(--soft)}.btn{display:inline-block;background:var(--ink);color:var(--bg);padding:14px 26px;border-radius:6px;font-size:15px;font-weight:400}
.hero{min-height:calc(100vh - 104px);display:flex;flex-direction:column;justify-content:center;padding:0 60px 80px;position:relative}
.hero .lampje{width:14px;height:14px;border-radius:50%;background:var(--lamp);margin-bottom:48px}
.hero .kick{font-size:19px;color:var(--soft)}.hero h1{font-family:Fraunces;font-weight:300;font-size:92px;line-height:1;letter-spacing:-.02em;margin:22px 0;max-width:12ch}
.hero .sub{font-size:24px;color:var(--lamp)}.hero .row{margin-top:48px;display:flex;align-items:center;gap:28px}.fine{font-size:13px;color:var(--soft);max-width:38ch;line-height:1.5}
.info{padding:56px 60px 90px;max-width:1200px}.eyebrow{font-size:14px;color:var(--soft);margin-bottom:14px}.info h2{font-family:Fraunces;font-weight:300;font-size:58px;margin-bottom:56px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:56px}.steps li{border-top:1px solid var(--rule);padding-top:24px}.steps .n{color:var(--lamp);font-size:14px}
.steps h3{font-family:Fraunces;font-weight:300;font-size:28px;margin:14px 0 12px}.steps p{color:var(--soft);line-height:1.6}
.caren{margin-top:80px;max-width:48ch}.quote{font-family:Fraunces;font-weight:300;font-size:34px;line-height:1.25}.by{margin-top:14px;color:var(--soft)}
.note{margin-top:64px;font-size:14px;color:var(--soft);max-width:62ch;line-height:1.6}
.chat.pam{background:var(--pamr);--v:var(--pam)}.chat.sam{background:var(--samr);--v:var(--sam)}
.ch{display:flex;justify-content:space-between;align-items:center;padding:28px 56px;font-size:14px}.ch .logo{font-family:Fraunces;font-size:22px;color:var(--v)}.chat.sam .ch .logo{font-family:"Work Sans";font-weight:400;font-size:19px}
.ch .logo::before{content:"";display:inline-block;width:9px;height:9px;border-radius:50%;background:var(--v);margin-right:12px;vertical-align:2px}.ch ul{display:flex;gap:28px;color:var(--soft)}
.log{width:min(620px,100%);margin:0 auto;padding:40px 24px}.turn{padding:18px 0}.who{display:block;font-size:12px;color:var(--soft);margin-bottom:6px;font-family:"Work Sans"}
.q{color:var(--v);font-size:20px;line-height:1.5}.chat.pam .q{font-family:Fraunces;font-weight:300;font-size:23px;line-height:1.4}.a{margin-top:12px;font-size:19px;line-height:1.65;color:var(--ink)}
.dock{width:min(620px,100%);margin:0 auto;padding:12px 24px 48px}.field{border-bottom:1px solid var(--soft);padding:14px 0;font-size:19px;color:var(--soft)}
.acts{display:flex;justify-content:space-between;align-items:center;margin-top:20px;font-size:14px;color:var(--soft)}.send{background:var(--v);color:var(--bg);padding:12px 24px;border-radius:6px;font-weight:400}
@media(max-width:700px){.nav{padding:20px}.nav ul li:not(.k){display:none}.hero{padding:40px 20px}.hero h1{font-size:52px}.hero .row{flex-direction:column;align-items:flex-start}
.info{padding:32px 20px}.info h2{font-size:38px}.steps{grid-template-columns:1fr;gap:28px}.ch{padding:18px 20px}.ch ul li:not(.k){display:none}.q,.a,.field{font-size:15px}.chat.pam .q{font-size:18px}.field{font-size:16px}}
'''
avond_hero = nav() + f'''<section class="hero"><span class="lampje"></span><p class="kick">Iedereen worstelt weleens met zichzelf.</p><h1>Bespreek het met Pam of Sam.</h1>
<p class="sub">Jij komt op het antwoord.</p><div class="row"><a class="btn">Probeer gratis</a><p class="fine">{DISC}</p></div></section>'''

# ---------------------------------------------------------------- 5. TONEEL
toneel_css = '''
:root{--bg:#FBFAF7;--ink:#141414;--soft:#6A6A66;--rule:#E3E1DB;--pam:#A3532B;--sam:#2F5274}
body{background:var(--bg);color:var(--ink);font-family:"Libre Franklin",sans-serif;font-weight:300}
.nav{display:flex;justify-content:space-between;align-items:center;padding:26px 56px}.nav .logo{font-family:"Courier Prime";font-weight:700;font-size:18px;letter-spacing:.02em}
.nav ul{display:flex;gap:32px;align-items:center;font-size:14px}.btn{display:inline-block;font-family:"Courier Prime";font-weight:700;border:2px solid var(--ink);padding:12px 22px;font-size:15px}
.hero{min-height:calc(100vh - 96px);display:flex;align-items:center;justify-content:center;padding:40px 24px 80px}
.script{width:min(620px,100%);font-family:"Courier Prime";font-size:18px;line-height:1.55}
.script .scene{font-weight:700;margin-bottom:28px}.script .act{margin:0 0 28px}.script .role{text-align:center;margin-top:18px;font-weight:700}
.script .par{text-align:center;color:var(--soft)}.script .say{width:70%;margin:0 auto 18px}
.script .role.p{color:var(--pam)}.script .role.sr{color:var(--sam)}.script h1{font:inherit;font-weight:700;font-size:42px;line-height:1.15;margin:8px 0 26px;font-family:"Libre Franklin";letter-spacing:-.02em}
.script .row{margin-top:36px;display:flex;flex-direction:column;align-items:center;gap:14px}.fine{font-family:"Libre Franklin";font-size:13px;color:var(--soft);text-align:center;max-width:40ch;line-height:1.5}
.info{width:min(760px,100%);margin:0 auto;padding:48px 24px 90px}.eyebrow{font-family:"Courier Prime";font-weight:700;font-size:14px;margin-bottom:12px}
.info h2{font-weight:600;font-size:44px;letter-spacing:-.02em;margin-bottom:40px}.steps li{display:grid;grid-template-columns:120px 1fr;gap:24px;padding:22px 0;border-top:1px solid var(--rule)}
.steps .n{font-family:"Courier Prime";font-weight:700}.steps h3{font-weight:600;font-size:19px;margin-bottom:8px}.steps p{grid-column:2;color:var(--soft);line-height:1.6}.steps h3{grid-column:2;grid-row:1}
.caren{margin-top:56px;font-family:"Courier Prime";font-size:18px;line-height:1.55}.quote{width:70%;margin:0 auto}.by{text-align:center;font-weight:700;margin-bottom:8px;order:-1}.caren{display:flex;flex-direction:column}
.note{margin-top:56px;font-size:14px;color:var(--soft);line-height:1.6}
.chat{background:var(--bg)}.chat.pam{--v:var(--pam)}.chat.sam{--v:var(--sam)}
.ch{display:flex;justify-content:space-between;padding:24px 56px;font-size:14px;border-bottom:1px solid var(--rule)}.ch .logo{font-family:"Courier Prime";font-weight:700;color:var(--v)}.ch ul{display:flex;gap:28px;color:var(--soft)}
.log{width:min(620px,100%);margin:0 auto;padding:40px 24px;font-family:"Courier Prime";font-size:17px;line-height:1.55}
.turn{padding:8px 0}.q{width:72%;margin:0 auto;color:var(--v)}.who{display:block;text-align:center;font-weight:700;margin-bottom:2px}
.a{width:72%;margin:16px auto 0}.a::before{content:"JIJ";display:block;text-align:center;font-weight:700;margin-bottom:2px}
.dock{width:min(620px,100%);margin:0 auto;padding:12px 24px 44px;font-family:"Courier Prime"}.field{width:72%;margin:0 auto;padding:12px 0;border-bottom:2px solid var(--ink);color:var(--soft);font-size:17px}
.field::before{content:"JIJ";display:block;text-align:center;font-weight:700;color:var(--ink);margin-bottom:6px}
.acts{width:72%;margin:18px auto 0;display:flex;justify-content:space-between;align-items:center;font-size:15px}.alt{color:var(--soft)}.send{font-weight:700;color:#fff;background:var(--v);padding:11px 20px}
@media(max-width:700px){.nav{padding:18px 20px}.nav ul li:not(.k){display:none}.script{font-size:15px}.script h1{font-size:30px}.script .say{width:88%}
.info{padding:28px 20px}.info h2{font-size:32px}.steps li{grid-template-columns:1fr;gap:4px}.steps p,.steps h3{grid-column:1;grid-row:auto}.quote{width:88%}
.ch{padding:18px 20px}.ch ul li:not(.k){display:none}.log{font-size:15px}.q,.a,.field,.acts{width:88%}.field{font-size:16px}}
'''
toneel_hero = nav() + f'''<section class="hero"><div class="script">
<p class="scene">BINNEN. EEN RUSTIGE KAMER. AVOND.</p>
<p class="act">Iedereen worstelt weleens met zichzelf. Jij ook. Je gaat zitten.</p>
<h1>Bespreek het met Pam of Sam.</h1>
<p class="role p">PAM</p><p class="par">(warm)</p><p class="say">Vertel me rustig wat er speelt.</p>
<p class="role sr">SAM</p><p class="par">(nuchter)</p><p class="say">Wat is precies het probleem?</p>
<p class="role">JIJ</p><p class="say">Ik kom zelf op het antwoord.</p>
<div class="row"><a class="btn">Probeer gratis</a><p class="fine">{DISC}</p></div></div></section>'''

for key, css, hero in [('drempel', drempel_css, drempel_hero), ('kalk', kalk_css, kalk_hero), ('vlakken', vlakken_css, vlakken_hero), ('avond', avond_css, avond_hero), ('toneel', toneel_css, toneel_hero)]:
    open(os.path.join(D, f'{key}.html'), 'w').write(page(key, css, hero))
print('ok')
