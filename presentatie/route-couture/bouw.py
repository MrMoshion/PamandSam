"""Vijf schetsen: Couture met het gevoel van de kamer. Elk bestand: ?s=home|info|pam|sam."""
import os
D = os.path.dirname(os.path.abspath(__file__))
DISC = '6 vragen gratis · geen creditcard · anoniem · gesprekken niet opgeslagen op onze servers'
PAM = [('Fijn dat je er bent. Vertel me rustig wat er speelt.', 'Ik slaap slecht sinds de verhuizing. Het voelt alsof ik nergens thuis ben.'),
       ('Wat mis je het meest?', 'De buurt. Dat iemand me groette als ik naar buiten liep.')]
SAM = [('Vertel me wat er speelt.', 'Ik moet kiezen tussen een promotie en minder uren werken.'),
       ('Wat wil jij, los van anderen?', 'Tijd. Ik wil mijn dochter van school halen.')]
NEXT = {'pam': 'Wanneer voelde je je hier wél even gezien?', 'sam': 'Wat is je eerste stap?'}
STEPS = [('Vertel wat er speelt', 'Schrijf het op zoals het in je hoofd zit.'), ('Beantwoord één vraag', 'Telkens één vraag. Geen advies.'), ('Kies je eigen stap', 'In je eigen woorden.')]
QUOTE = '“Wat je overkomt hoeft je leven niet te bepalen, je kunt kiezen hoe je erop reageert.”'

# palet per schets: achtergrond, kamer, inkt, zacht; en per stem de kamer-tinten
P = {
 'a-binnen':   dict(bg='#E6DCD8', room='#F2EBE7', ink='#2A1A22', soft='#6E5A62', pam='#F4E9E3', pamI='#3A1F25', sam='#E9ECEC', samI='#1E2A2E'),
 'b-nis':      dict(bg='#B9A4A6', room='#C8B5B6', ink='#241619', soft='#4B373B', pam='#C9B0AB', pamI='#2A1714', sam='#A9AEB4', samI='#161C22'),
 'c-vloer':    dict(bg='#1F2620', room='#1F2620', ink='#E8E2D6', soft='#A9A596', pam='#2A2620', pamI='#EADFCF', sam='#1C2328', samI='#DCE3E6'),
 'd-tegenover':dict(bg='#5E2B32', room='#5E2B32', ink='#F6E9E2', soft='#D6B6AF', pam='#6A3036', pamI='#F8EBE4', sam='#2E3036', samI='#EDEAE6'),
 'e-plafond':  dict(bg='#ECEEEC', room='#F7F7F4', ink='#16202C', soft='#5B6672', pam='#F3EEE7', pamI='#2B211B', sam='#ECF0F2', samI='#16202C'),
}
TITLE = {'a-binnen': 'A · Binnen', 'b-nis': 'B · Nis', 'c-vloer': 'C · Vloer', 'd-tegenover': 'D · Tegenover', 'e-plafond': 'E · Plafond'}

BASE = '''
*{box-sizing:border-box;margin:0;padding:0}a{color:inherit;text-decoration:none}ol{list-style:none}
.screen{display:none;min-height:100vh}body[data-s=home] #home,body[data-s=info] #info,body[data-s=pam] #pam,body[data-s=sam] #sam{display:block}
body{background:var(--bg);color:var(--ink);font-family:Jost,sans-serif;font-weight:300;-webkit-font-smoothing:antialiased}
.cap{font-size:12px;letter-spacing:.18em;text-transform:uppercase}
.nav{display:flex;justify-content:space-between;align-items:center;padding:28px 48px}.nav b{font-family:"Bodoni Moda";font-weight:400;font-size:22px}
.nav .cta{border-bottom:1px solid currentColor;padding-bottom:3px}
.didone{font-family:"Bodoni Moda";font-weight:400;letter-spacing:-.015em}
.btn{display:inline-block;background:var(--ink);color:var(--bg);padding:16px 34px}
.h{display:flex;flex-direction:column;align-items:center;text-align:center;justify-content:center}
.h .k{color:var(--soft)}.h h1{font-size:clamp(54px,8vw,128px);line-height:.96;margin:26px 0}.h h1 span{display:block;font-style:italic}.h .s{font-size:20px}
.h .btn{margin-top:44px}.h .fine{margin-top:16px;font-size:12px;color:var(--soft)}
.i{text-align:center;padding:40px 48px 72px}.i h2{font-size:64px;margin:18px 0 56px}.i ol{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;max-width:980px;margin:0 auto}
.i li b{font-family:"Bodoni Moda";font-weight:400;font-style:italic;font-size:48px}.i li h3{font-weight:400;margin:14px 0 8px}.i li p{color:var(--soft);line-height:1.6}
.i blockquote{font-family:"Bodoni Moda";font-size:34px;line-height:1.2;max-width:24ch;margin:80px auto 0}.i .by{margin-top:16px;color:var(--soft)}
.c{min-height:100vh;display:flex;flex-direction:column;text-align:center}.c.pam{--cbg:var(--pam);--cink:var(--pamI)}.c.sam{--cbg:var(--sam);--cink:var(--samI)}
.c{background:var(--cbg);color:var(--cink)}.c header{display:flex;justify-content:space-between;padding:26px 48px}.c header b{font-family:"Bodoni Moda";font-weight:400;font-size:18px;letter-spacing:0;text-transform:none}
.c.sam header b{font-family:Jost;font-weight:400}.c .room{flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:20px;padding:24px}
.old{font-size:15px;line-height:1.6;max-width:50ch;opacity:.72}.old i{display:block;font-style:normal;font-size:11px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:4px}
.now{font-family:"Bodoni Moda";font-size:clamp(32px,4.2vw,58px);line-height:1.1;max-width:18ch;margin-top:20px}.c.sam .now{font-family:Jost;font-weight:300;letter-spacing:-.02em}
.in{width:min(560px,100%);margin:0 auto;padding:0 24px 44px}.in .f{border-bottom:1px solid currentColor;padding:14px 0;font-size:18px;opacity:.65}
.in p{display:flex;justify-content:space-between;margin-top:18px}
@media(max-width:700px){.nav{padding:20px}.nav .l{display:none}.h h1{font-size:50px}.i{padding:28px 20px}.i h2{font-size:42px;margin-bottom:32px}.i ol{grid-template-columns:1fr;gap:28px}.i blockquote{font-size:24px;margin-top:48px}
.c header{padding:18px 20px}.c header .l{display:none}.now{font-size:30px}.old{font-size:15px}.in .f{font-size:16px}}
'''

# per schets: extra CSS die het gevoel van de kamer maakt
VAR = {
'a-binnen': '''
.h{min-height:calc(100vh - 88px);padding:0 48px 48px}.frame{background:var(--room);width:100%;min-height:calc(100vh - 136px);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:48px}
.i .frame{min-height:0;padding:56px 48px}.c .room{margin:0}
@media(max-width:700px){.h{padding:0 12px 12px}.frame{padding:40px 20px;min-height:calc(100vh - 90px)}.i{padding:0 12px 12px}.i .frame{padding:32px 16px}}''',
'b-nis': '''
.h{min-height:calc(100vh - 88px);padding:0 48px 56px}.niche{background:var(--room);width:min(880px,100%);border-radius:420px 420px 0 0;padding:96px 48px 64px;display:flex;flex-direction:column;align-items:center}
.c .niche{background:color-mix(in srgb, var(--cbg) 86%, #fff 14%);width:min(820px,calc(100% - 48px));margin:0 auto;flex:1;border-radius:420px 420px 0 0;display:flex;flex-direction:column;justify-content:flex-end;padding:72px 40px 0}
.c.sam .niche{background:color-mix(in srgb, var(--cbg) 82%, #fff 18%)}
@media(max-width:700px){.h{padding:0 12px 20px}.niche{padding:64px 20px 40px;border-radius:200px 200px 0 0}.c .niche{width:calc(100% - 20px);padding:48px 16px 0;border-radius:200px 200px 0 0}}''',
'c-vloer': '''
.h{min-height:calc(100vh - 88px);position:relative;padding:0 48px 30vh}.h::after,.c::after{content:"";position:absolute;left:0;right:0;bottom:0;height:30vh;background:color-mix(in srgb, var(--bg) 88%, #000 12%);border-top:1px solid color-mix(in srgb, var(--ink) 30%, transparent)}
.h > *{position:relative;z-index:1}.h .btn{position:relative;z-index:1}.c{position:relative}.c > *{position:relative;z-index:1}.c::after{z-index:0;background:color-mix(in srgb, var(--cbg) 85%, #000 15%);border-top-color:color-mix(in srgb, var(--cink) 25%, transparent)}
.c .room{padding-bottom:12vh}.in{padding-bottom:9vh}
@media(max-width:700px){.h{padding:0 20px 24vh}.h::after{height:24vh}}''',
'd-tegenover': '''
.h{min-height:calc(100vh - 88px);padding:0 48px 56px}.h .s{margin-top:8vh}
.c .room{justify-content:space-between;padding:40px 24px 0}.c .their{display:flex;flex-direction:column;align-items:center;gap:18px}.c .now{margin-top:8px}
.c .table{width:min(560px,100%);border-top:1px solid color-mix(in srgb, var(--cink) 35%, transparent);margin:6vh auto 0}
.c .mine{display:flex;flex-direction:column;align-items:center;gap:14px;margin:4vh 0 24px}.c .mine .old{opacity:.9}''',
'e-plafond': '''
body{background:linear-gradient(var(--room) 0 34vh,var(--bg) 34vh)}.h{min-height:calc(100vh - 88px);justify-content:flex-end;padding:0 48px 64px}
.c{background:linear-gradient(color-mix(in srgb, var(--cbg) 55%, #fff 45%) 0 30vh,var(--cbg) 30vh)}.c .room{justify-content:flex-end}
@media(max-width:700px){.h{padding:0 20px 40px}}''',
}

def nav(): return '<nav class="nav cap"><span class="l">Hoe het werkt &nbsp;·&nbsp; Caren</span><b>Pam &amp; Sam</b><a class="cta">Probeer gratis</a></nav>'
def hero_inner(): return f'<p class="cap k">Iedereen worstelt weleens met zichzelf</p><h1 class="didone">Bespreek het<span>met Pam of Sam.</span></h1><p class="s">Jij komt op het antwoord.</p><a class="btn cap">Probeer gratis</a><p class="fine">{DISC}</p>'
def info_inner(): return '<p class="cap k" style="color:var(--soft)">Hoe het werkt</p><h2 class="didone">Drie stappen.</h2><ol>' + ''.join(f'<li><b>{i+1}</b><h3 class="cap">{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS)) + f'</ol><blockquote>{QUOTE}</blockquote><p class="cap by">Caren Pardovitch</p>'

def build(key):
    p = P[key]; nm = lambda v: 'Pam' if v == 'pam' else 'Sam'; ot = lambda v: 'Sam' if v == 'pam' else 'Pam'
    tv = lambda v: PAM if v == 'pam' else SAM
    if key == 'a-binnen':
        home = nav() + f'<section class="h"><div class="frame">{hero_inner()}</div></section>'; info = nav() + f'<section class="i"><div class="frame">{info_inner()}</div></section>'
    elif key == 'b-nis':
        home = nav() + f'<section class="h"><div class="niche">{hero_inner()}</div></section>'; info = nav() + f'<section class="i">{info_inner()}</section>'
    else:
        home = nav() + f'<section class="h">{hero_inner()}</section>'; info = nav() + f'<section class="i">{info_inner()}</section>'
    def chat(v):
        old = ''.join(f'<p class="old"><i>{nm(v)}: {q}</i>{a}</p>' for q, a in tv(v))
        head = f'<header class="cap"><span class="l">Onderwerpen</span><b>{nm(v)}</b><span>Terugblik &nbsp; ×</span></header>'
        inp = f'<div class="in"><div class="f">Schrijf hier…</div><p class="cap"><a>Wissel naar {ot(v)}</a><a>Verstuur</a></p></div>'
        if key == 'd-tegenover':
            q, a = tv(v)[-1]
            return f'<div class="c {v}">{head}<div class="room"><div class="their"><p class="old"><i>{nm(v)}</i>{q}</p><p class="now">{NEXT[v]}</p></div><div class="table"></div><div class="mine"><p class="old"><i>Jij</i>{a}</p></div></div>{inp}</div>'
        if key == 'b-nis':
            return f'<div class="c {v}">{head}<div class="niche"><div class="room">{old}<p class="now">{NEXT[v]}</p></div>{inp}</div></div>'
        return f'<div class="c {v}">{head}<div class="room">{old}<p class="now">{NEXT[v]}</p></div>{inp}</div>'
    root = ':root{' + ';'.join(f'--{k}:{v}' for k, v in p.items()) + '}'
    html = f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pam &amp; Sam · {TITLE[key]}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;1,6..96,400&family=Jost:wght@300;400&display=swap">
<style>{root}{BASE}{VAR[key]}</style></head><body data-s="home"><div class="screen" id="home">{home}</div><div class="screen" id="info">{info}</div>
<div class="screen" id="pam">{chat('pam')}</div><div class="screen" id="sam">{chat('sam')}</div><script>const s=new URLSearchParams(location.search).get('s');if(s)document.body.dataset.s=s;</script></body></html>'''
    open(os.path.join(D, key + '.html'), 'w').write(html)

for k in P: build(k)
print('ok')
