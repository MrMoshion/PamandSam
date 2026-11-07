"""Ronde 7: zes contrastkleuren voor de huisstijl, sticky menu in glas (60%), meer lucht rond de bovenregel. Alleen previews."""
import os
D = os.path.dirname(os.path.abspath(__file__))
def L(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]; return .2126*c[0] + .7152*c[1] + .0722*c[2]
def CR(a, b): x, y = L(a), L(b); return (max(x, y) + .05) / (min(x, y) + .05)
N = dict(wall='#F0EADD', ceil='#F9F6F0', ink='#2F2A22', soft='#5E564A', mid='#7A6D58')
# c = contrastkleur (vlak en stip), t = tekst op het vlak, mark = gebruik als markering achter tekst
C = {
 '1-mos':      dict(t='1 · Mos', c='#5E6B45', on='#F9F6F0', why='Gedempt groen als een plant in de kamer. Rustig, levend, botst niet met hout of papier.'),
 '2-petrol':   dict(t='2 · Petrol', c='#2F5A5A', on='#F9F6F0', why='Diep blauwgroen, als geglazuurd aardewerk. Koel tegen het warme zand; het sterkste contrast.'),
 '3-roest':    dict(t='3 · Roest', c='#9A4E30', on='#FFFFFF', why='Gebrande aarde. Warm op warm: veel karakter, maar dicht bij Pams hout. Rood alleen gedempt en klein (zie 48).'),
 '4-pruim':    dict(t='4 · Pruim', c='#5A3B4C', on='#F9F6F0', why='Donker paarsbruin, als een fluwelen stoel. Couture zonder roze; ernstig en warm tegelijk.'),
 '5-oker':     dict(t='5 · Diep oker', c='#8C6420', on='#FFFFFF', why='Toon op toon: de donkerste kleur van het zand zelf. Het minst opvallend, het meest één familie.'),
 '6-marker':   dict(t='6 · Markeerstift', c='#D9DE6A', on='#2F2A22', mark=True, why='Ongemakkelijk ver: een lichte markeerkleur, alleen áchter woorden, zoals je in een zelfhulpboek onderstreept (zie 11). Geen vlakken.'),
}
CSS = '''*{box-sizing:border-box;margin:0;padding:0}a{color:inherit;text-decoration:none}
body{background:%(wall)s;color:%(ink)s;font-family:Jost,sans-serif;font-weight:300;-webkit-font-smoothing:antialiased}
.nav{position:sticky;top:0;z-index:5;display:flex;justify-content:space-between;align-items:center;padding:22px max(48px,calc((100vw - 1100px)/2));transition:background .4s,backdrop-filter .4s}
.nav.glass{background:rgba(249,246,240,.6);-webkit-backdrop-filter:blur(14px) saturate(1.1);backdrop-filter:blur(14px) saturate(1.1);border-bottom:1px solid rgba(47,42,34,.08)}
.nav b{font-family:Literata,serif;font-weight:400;font-size:22px}.nav span{display:flex;gap:28px;align-items:center;font-size:15px;color:%(soft)s}
.nav a.b{background:%(mid)s;color:#fff;padding:10px 16px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;border-radius:2px;font-weight:400}
.top{background:linear-gradient(%(ceil)s 0 34vh,%(wall)s 34vh);margin-top:-80px;padding-top:80px}
.h{min-height:calc(100vh - 80px);display:flex;flex-direction:column;align-items:center;text-align:center;padding:calc(34vh - 80px + 56px) 24px 72px}
.k{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:%(soft)s;max-width:30ch}
.k:before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%%;background:var(--c);margin-right:12px;vertical-align:.15em}
h1{font-family:Literata,serif;font-weight:400;font-size:clamp(46px,7vw,100px);line-height:1.04;letter-spacing:-.025em;margin:44px 0 22px}
.s{font-size:20px}.s i{display:inline-block;width:2px;height:1.05em;background:var(--c);vertical-align:-.15em;margin-left:4px}
.btn{margin-top:36px;background:%(mid)s;color:#fff;padding:16px 30px;font-size:13px;letter-spacing:.16em;text-transform:uppercase;border-radius:2px;font-weight:400}
.fine{margin-top:16px;font-size:13px;color:%(soft)s}
.sec{padding:96px max(48px,calc((100vw - 1100px)/2))}.sec .e{font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:%(soft)s}
.sec h2{font-family:Literata,serif;font-weight:400;font-size:52px;letter-spacing:-.02em;margin:16px 0 18px;max-width:18ch}
.sec p{font-size:19px;line-height:1.65;max-width:56ch;color:%(soft)s}.sec p a{color:%(ink)s;text-decoration:underline;text-decoration-color:var(--c);text-decoration-thickness:2px;text-underline-offset:5px}
.band{background:var(--c);color:var(--on)}.band .e,.band p{color:var(--on);opacity:.85}
.mk{background:linear-gradient(transparent 55%%,var(--c) 55%%);padding:0 2px;color:%(ink)s}
@media(max-width:700px){.nav{padding:16px}.nav .l{display:none}.h{padding:calc(34vh - 80px + 40px) 16px 40px}h1{margin:32px 0 18px}.sec{padding:64px 16px}.sec h2{font-size:34px}}
'''
def page(k):
    o = C[k]; css = CSS % N
    mark = o.get('mark')
    band = ('<section class="sec"><p class="e">De eerlijke vraag</p><h2>Waarom niet gewoon een <span class="mk">gratis chatbot</span>?</h2><p>Een chatbot geeft je snel een antwoord. Pam en Sam stellen de vraag <span class="mk">die je zelf verder helpt</span>. <a>Lees hoe het werkt</a></p></section>'
            if mark else
            '<section class="sec band"><p class="e">De eerlijke vraag</p><h2>Waarom niet gewoon een gratis chatbot?</h2><p>Een chatbot geeft je snel een antwoord. Pam en Sam stellen de vraag die je zelf verder helpt.</p></section>'
            '<section class="sec"><p class="e">Hoe het werkt</p><h2>Drie stappen. Niet meer.</h2><p>Je vertelt wat er speelt, je beantwoordt één vraag, je kiest je eigen stap. <a>Lees hoe het werkt</a></p></section>')
    html = f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pam &amp; Sam · {o['t']}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,300..500&family=Jost:wght@300;400&display=swap"><style>:root{{--c:{o['c']};--on:{o['on']}}}{css}</style></head><body>
<nav class="nav" id="nav"><b>Pam &amp; Sam</b><span><span class="l">Aanpak &nbsp; Tarieven &nbsp; Contact</span><a class="b">Probeer gratis</a></span></nav>
<div class="top"><section class="h"><p class="k">Iedereen worstelt weleens met zichzelf.</p><h1>Bespreek het<br>met Pam of Sam.</h1><p class="s">Jij komt op het antwoord.<i></i></p><a class="btn">Probeer gratis</a><p class="fine">6 vragen gratis · geen creditcard · anoniem · gesprekken niet opgeslagen op onze servers</p></section></div>
{band}<section class="sec" style="height:60vh"></section>
<script>addEventListener('scroll',()=>document.getElementById('nav').classList.toggle('glass',scrollY>8),{{passive:true}})</script></body></html>'''
    open(os.path.join(D, 'contrast-' + k + '.html'), 'w').write(html)
    if mark: return f"{k}: inkt op markering {CR(N['ink'], o['c']):.1f}:1 (markering naast zand {CR(o['c'], N['wall']):.1f}:1)"
    return f"{k}: tekst op vlak {CR(o['on'], o['c']):.1f}:1, kleur als lijn/stip op zand {CR(o['c'], N['wall']):.1f}:1"
for k in C: print(page(k))
