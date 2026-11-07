"""Zes opties: Plafond (opbouw) + Nis (kleur) + Tegenover (gesprek). Optie 6 is vrij. ?s=home|info|pam|sam"""
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

# muur, plafond, inkt, zacht (gemeten ≥ 4.5:1 op de muur), knop; per stem: muur, plafond, inkt, zacht
O = {
 'a-linnen':      dict(t='A · Linnen', wall='#E8DFCC', ceil='#F5F0E4', ink='#2A2218', soft='#5C503F', hist='folded',
                      pw='#EADDD9', pc='#F7F1EF', pi='#2C1A15', ps='#5E4840', sw='#DCE0E4', sc='#F0F2F4', si='#15202B', ss='#45525F', hc='38vh', cc='30vh'),
 'b-zand':      dict(t='B · Zand', wall='#E5D6B3', ceil='#F3EBD8', ink='#2B2214', soft='#5B4C31', hist='folded',
                      pw='#EADDD9', pc='#F7F1EF', pi='#2C1A15', ps='#5E4840', sw='#DCE0E4', sc='#F0F2F4', si='#15202B', ss='#45525F', hc='38vh', cc='30vh'),
 'c-honing':      dict(t='C · Honing', wall='#ECDDAE', ceil='#F7F0DA', ink='#2A2210', soft='#5A4D2C', hist='folded',
                      pw='#EADDD9', pc='#F7F1EF', pi='#2C1A15', ps='#5E4840', sw='#DCE0E4', sc='#F0F2F4', si='#15202B', ss='#45525F', hc='38vh', cc='30vh'),
}

def L(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]; return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]
def CR(a, b): x, y = L(a), L(b); return (max(x, y) + .05) / (min(x, y) + .05)

BASE = '''
*{box-sizing:border-box;margin:0;padding:0}a{color:inherit;text-decoration:none}ol{list-style:none}
.screen{display:none;min-height:100vh}body[data-s=home] #home,body[data-s=info] #info,body[data-s=pam] #pam,body[data-s=sam] #sam{display:block}
body{color:var(--ink);font-family:Jost,sans-serif;font-weight:300;-webkit-font-smoothing:antialiased}
.cap{font-size:12px;letter-spacing:.18em;text-transform:uppercase}.didone{font-family:"Bodoni Moda";font-weight:400;letter-spacing:-.015em}
.pg{min-height:100vh;background:linear-gradient(var(--ceil) 0 var(--hc),var(--wall) var(--hc))}
.nav{display:flex;justify-content:space-between;align-items:center;padding:28px 48px}.nav b{font-family:"Bodoni Moda";font-weight:400;font-size:22px;letter-spacing:0;text-transform:none}.nav .cta{border-bottom:1px solid currentColor;padding-bottom:3px}
.h{min-height:calc(100vh - 88px);display:flex;flex-direction:column;align-items:center;justify-content:flex-end;text-align:center;padding:0 48px 64px}
.h .k{color:var(--soft)}.h h1{font-size:clamp(54px,8vw,124px);line-height:.96;margin:24px 0}.h h1 span{display:block;font-style:italic}.h .s{font-size:20px}
.btn{display:inline-block;background:var(--ink);color:var(--wall);padding:16px 34px;margin-top:40px}.fine{margin-top:16px;font-size:12px;color:var(--soft)}
.i{text-align:center;padding:calc(var(--hc) - 40px) 48px 72px}.i .k{color:var(--soft)}.i h2{font-size:64px;margin:18px 0 56px}.i ol{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;max-width:980px;margin:0 auto}
.i li b{font-family:"Bodoni Moda";font-weight:400;font-style:italic;font-size:48px}.i li h3{font-weight:400;margin:14px 0 8px}.i li p{color:var(--soft);line-height:1.6}
.i blockquote{font-family:"Bodoni Moda";font-size:34px;line-height:1.2;max-width:24ch;margin:80px auto 0}.i .by{margin-top:16px;color:var(--soft)}
.c{min-height:100vh;display:flex;flex-direction:column;text-align:center;background:linear-gradient(var(--c-ceil) 0 var(--cc),var(--c-wall) var(--cc));color:var(--c-ink)}
.c.pam{--c-wall:var(--pw);--c-ceil:var(--pc);--c-ink:var(--pi);--c-soft:var(--ps)}.c.sam{--c-wall:var(--sw);--c-ceil:var(--sc);--c-ink:var(--si);--c-soft:var(--ss)}
.c header{display:flex;justify-content:space-between;padding:26px 48px}.c header b{font-family:"Bodoni Moda";font-weight:400;font-size:18px;letter-spacing:0;text-transform:none}.c.sam header b{font-family:Jost;font-weight:400}
.c .hist{height:calc(var(--cc) - 76px);display:flex;flex-direction:column;justify-content:center;align-items:center;gap:10px;padding:0 24px}
.old{font-size:15px;line-height:1.55;max-width:52ch;color:var(--c-soft)}.old i{font-style:normal;font-size:11px;letter-spacing:.16em;text-transform:uppercase;margin-right:8px}
.c .room{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px}
.who{color:var(--c-soft)}.room .old{margin-bottom:8px}.room .old + .who{margin-top:28px}.now{font-family:"Bodoni Moda";font-size:clamp(32px,4.2vw,58px);line-height:1.1;max-width:18ch;margin-top:12px}.c.sam .now{font-family:Jost;font-weight:300;letter-spacing:-.02em}
.table{width:min(560px,100%);border-top:1px solid color-mix(in srgb, var(--c-ink) 30%, transparent);margin:6vh auto 3vh}
.mine{font-size:17px;line-height:1.6;max-width:44ch}.mine .who{display:block;margin-bottom:6px}
.in{width:min(560px,100%);margin:0 auto;padding:0 24px 44px}.in .f{border-bottom:1px solid currentColor;padding:14px 0;font-size:18px;color:var(--c-soft)}
.in p{display:flex;justify-content:space-between;margin-top:18px}
.fold{color:var(--c-soft);border-bottom:1px solid currentColor;padding-bottom:2px}
@media(max-width:700px){.nav{padding:20px}.nav .l{display:none}.h{padding:0 20px 40px}.h h1{font-size:50px}.i{padding:calc(var(--hc) - 30px) 20px 40px}.i h2{font-size:42px;margin-bottom:32px}.i ol{grid-template-columns:1fr;gap:28px}.i blockquote{font-size:24px;margin-top:48px}
.c header{padding:18px 20px}.c header .l{display:none}.now{font-size:30px}.old,.mine{font-size:15px}.in .f{font-size:16px}.c .hist{height:auto;min-height:calc(var(--cc) - 60px);padding:8px 20px}}
'''

CHAT = """
.c.k{text-align:left}.c.k .log{flex:1;width:min(640px,calc(100% - 48px));margin:0 auto;display:flex;flex-direction:column;justify-content:flex-end;padding:calc(var(--cc) - 40px) 0 8px}
.c.k .turn{margin-top:36px}.c.k .turn:first-child{margin-top:0}.c.k .nm{display:block;font-size:11px;color:var(--c-soft);margin-bottom:4px}
.c.k .q{font-size:20px;line-height:1.55;color:var(--c-soft)}.c.k .a{margin-top:10px;font-size:20px;line-height:1.55;color:var(--c-ink);font-weight:400}
.c.k .dock{width:min(640px,calc(100% - 48px));margin:0 auto;padding:24px 0 56px}.c.k .f{border-bottom:1px solid var(--c-ink);padding:12px 0 10px;font-size:20px;color:var(--c-soft)}
.c.k .acts{display:flex;justify-content:space-between;align-items:center;margin-top:24px}.c.k .lnk{font-size:15px;color:var(--c-soft);text-decoration:underline;text-underline-offset:5px}
.c.k .send{background:var(--c-ink);color:var(--c-wall);padding:12px 24px;border-radius:30px;font-size:15px}
@media(max-width:700px){.c.k .q,.c.k .a{font-size:15px;line-height:1.6}.c.k .turn{margin-top:28px}.c.k .f{font-size:16px}.c.k .dock{padding-bottom:28px}}
"""
def build(key):
    o = O[key]; nm = lambda v: 'Pam' if v == 'pam' else 'Sam'; ot = lambda v: 'Sam' if v == 'pam' else 'Pam'
    tv = lambda v: PAM if v == 'pam' else SAM
    nav = '<nav class="nav cap"><span class="l">Hoe het werkt &nbsp;·&nbsp; Caren</span><b>Pam &amp; Sam</b><a class="cta">Probeer gratis</a></nav>'
    hero = f'<p class="cap k">Iedereen worstelt weleens met zichzelf</p><h1 class="didone">Bespreek het<span>met Pam of Sam.</span></h1><p class="s">Jij komt op het antwoord.</p><a class="btn cap">Probeer gratis</a><p class="fine">{DISC}</p>'
    extra = ''
    if key == '5-twee-kamers':
        extra = ('<style>.rooms{display:grid;grid-template-columns:1fr 1fr;gap:0;width:100%;margin-top:48px}.rooms div{padding:28px;text-align:left}.rooms .p{background:var(--pw);color:var(--pi)}.rooms .s2{background:var(--sw);color:var(--si)}'
                 '.rooms b{font-family:"Bodoni Moda";font-weight:400;font-size:44px;display:block}.rooms .s2 b{font-family:Jost;font-weight:300}.rooms p{margin-top:6px}.h{justify-content:flex-end;padding-bottom:0}.h .fine{margin-bottom:28px}'
                 '@media(max-width:700px){.rooms{grid-template-columns:1fr}}</style>')
        hero += '<div class="rooms"><div class="p"><b>Pam</b><p>Warm. Ze geeft eerst ruimte aan wat je voelt.</p></div><div class="s2"><b>Sam</b><p>Nuchter. Hij gaat zonder omweg naar de kern.</p></div></div>'
    home = f'<div class="pg">{nav}<section class="h">{hero}</section></div>'
    info = f'<div class="pg">{nav}<section class="i"><p class="cap k">Hoe het werkt</p><h2 class="didone">Drie stappen.</h2><ol>' + ''.join(f'<li><b>{i+1}</b><h3 class="cap">{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS)) + f'</ol><blockquote>{QUOTE}</blockquote><p class="cap by">Caren Pardovitch</p></section></div>'
    def chat(v):
        turns = tv(v)
        head = f'<header class="cap"><span class="l">Onderwerpen</span><b>{nm(v)}</b><span>Terugblik &nbsp; ×</span></header>'
        log = ''.join(f'<div class="turn"><span class="nm cap">{nm(v)}</span><p class="q">{q}</p></div><p class="a">{a}</p>' for q, a in turns)
        log += f'<div class="turn"><span class="nm cap">{nm(v)}</span><p class="q">{NEXT[v]}</p></div>'
        inp = f'<div class="dock"><div class="f">Schrijf hier…</div><div class="acts"><a class="lnk">Wissel naar {ot(v)}</a><a class="send">Verstuur</a></div></div>'
        return f'<div class="c k {v}">{head}<div class="log">{log}</div>{inp}</div>'
    keys = ['wall', 'ceil', 'ink', 'soft', 'pw', 'pc', 'pi', 'ps', 'sw', 'sc', 'si', 'ss', 'hc', 'cc']
    root = ':root{' + ';'.join(f'--{k}:{o[k]}' for k in keys) + '}'
    html = f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pam &amp; Sam · {o['t']}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;1,6..96,400&family=Jost:wght@300;400&display=swap">
<style>{root}{BASE}</style>{extra}<style>{CHAT}</style></head><body data-s="home"><div class="screen" id="home">{home}</div><div class="screen" id="info">{info}</div>
<div class="screen" id="pam">{chat('pam')}</div><div class="screen" id="sam">{chat('sam')}</div><script>const s=new URLSearchParams(location.search).get('s');if(s)document.body.dataset.s=s;</script></body></html>'''
    open(os.path.join(D, key + '.html'), 'w').write(html)
    # contrast: zachte tekst en inkt, op muur en plafond
    worst = min(CR(o['soft'], o['wall']), CR(o['ps'], o['pw']), CR(o['ss'], o['sw']), CR(o['ps'], o['pc']), CR(o['ss'], o['sc']), CR(o['soft'], o['ceil']))
    return f"{key}: laagste contrast zachte tekst {worst:.2f}:1, inkt {min(CR(o['ink'], o['wall']), CR(o['pi'], o['pw']), CR(o['si'], o['sw'])):.2f}:1"

for k in O: print(build(k))
