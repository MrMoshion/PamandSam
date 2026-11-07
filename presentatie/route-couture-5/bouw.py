"""Ronde 5: zes letters (alleen de kop) en vijf kleurparen voor de kamers. Zand iets zachter."""
import os
D = os.path.dirname(os.path.abspath(__file__))
# zachter zand: minder verzadigd, iets lichter dan B Zand (#E5D6B3 / #F3EBD8)
Z = dict(wall='#EAE1CC', ceil='#F6F2E8', ink='#2B2419', soft='#5C5140')
DISC = '6 vragen gratis · geen creditcard · anoniem · gesprekken niet opgeslagen op onze servers'
PAMZIN = 'Wat mis je het meest, als je eerlijk bent?'

def L(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]; return .2126*c[0] + .7152*c[1] + .0722*c[2]
def CR(a, b): x, y = L(a), L(b); return (max(x, y) + .05) / (min(x, y) + .05)

# ---------- zes letters ----------
F = {
 '1-literata':  dict(t='1 · Literata', link='Literata:ital,opsz,wght@0,7..72,300..500;1,7..72,300..500', fam='"Literata"', w=400, w2=400, it=True, ls='-.02em',
                     why='Gemaakt om boeken op een scherm te lezen (Google Play Boeken). Past bij zelfhulpboeken.'),
 '2-newsreader':dict(t='2 · Newsreader', link='Newsreader:ital,opsz,wght@0,6..72,300..500;1,6..72,300..500', fam='"Newsreader"', w=400, w2=400, it=True, ls='-.02em',
                     why='Krantenletter met optische maten (de letter past zich aan de grootte aan): verfijnd groot, stevig klein.'),
 '3-source':    dict(t='3 · Source Serif', link='Source+Serif+4:ital,opsz,wght@0,8..60,300..500;1,8..60,300..500', fam='"Source Serif 4"', w=400, w2=300, it=True, ls='-.02em',
                     why='Nuchtere boekletter, weinig contrast tussen dik en dun. Het meest leesbaar, het minst uitgesproken.'),
 '4-fraunces':  dict(t='4 · Fraunces', link='Fraunces:ital,opsz,wght@0,9..144,300..400;1,9..144,300..400', fam='"Fraunces"', w=300, w2=300, it=True, ls='-.02em',
                     why='Zacht en wat eigenzinnig, warm zonder lief te worden. Risico: veel gebruikt bij lifestylemerken.'),
 '5-spectral':  dict(t='5 · Spectral', link='Spectral:ital,wght@0,300;0,400;1,300', fam='"Spectral"', w=300, w2=300, it=True, ls='-.01em',
                     why='Licht en scherp, gemaakt voor schermen. Dichtst bij Bodoni van gevoel, maar veel rustiger te lezen.'),
 '6-jost':      dict(t='6 · Alleen Jost', link='Jost:wght@300;400', fam='"Jost"', w=300, w2=300, it=False, ls='-.035em',
                     why='Ongemakkelijk ver: geen schreefletter meer. Couture zoals een modehuis het doet: groot, licht, schoon. Pam verliest dan haar eigen letter.'),
}
HERO_CSS = '''*{box-sizing:border-box;margin:0;padding:0}a{color:inherit;text-decoration:none}
body{background:var(--wall);color:var(--ink);font-family:Jost,sans-serif;font-weight:300;-webkit-font-smoothing:antialiased}
.pg{min-height:100vh;display:flex;flex-direction:column;background:linear-gradient(var(--ceil) 0 34%,var(--wall) 34%)}
.nav{display:flex;justify-content:space-between;align-items:center;padding:28px max(48px,calc((100vw - 1100px)/2))}
.nav b{font-family:var(--d);font-weight:400;font-size:22px}.nav span{display:flex;gap:28px;align-items:center;font-size:15px;color:var(--soft)}
.nav a.b{border:1px solid var(--ink);color:var(--ink);padding:9px 16px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;border-radius:2px;font-weight:400}
.h{flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;padding:calc(34vh - 40px) 24px 72px}
.k{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--soft)}
h1{font-family:var(--d);font-weight:var(--w);font-size:clamp(46px,7.2vw,104px);line-height:1.02;letter-spacing:var(--ls);margin:22px 0 20px}
h1 span{display:block;font-weight:var(--w2)}
.s{font-size:20px}.s i{display:inline-block;width:2px;height:1.05em;background:var(--ink);vertical-align:-.15em;margin-left:4px;font-style:normal}
.btn{margin-top:36px;background:var(--ink);color:var(--ceil);padding:16px 30px;font-size:13px;letter-spacing:.16em;text-transform:uppercase;border-radius:2px;font-weight:400}
.fine{margin-top:16px;font-size:13px;color:var(--soft)}
@media(max-width:700px){.nav{padding:20px 16px}.nav .l{display:none}.nav b{font-size:20px}.h{padding:calc(34vh - 30px) 16px 40px}.fine{margin-top:auto;padding-top:40px}}
'''
def font(key):
    o = F[key]
    root = f":root{{--wall:{Z['wall']};--ceil:{Z['ceil']};--ink:{Z['ink']};--soft:{Z['soft']};--d:{o['fam']},Georgia,serif;--w:{o['w']};--w2:{o['w2']};--ls:{o['ls']}}}"
    it = 'h1 span{font-style:italic}' if o['it'] else ''
    html = f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pam &amp; Sam · {o['t']}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={o['link']}&family=Jost:wght@300;400&display=swap"><style>{root}{HERO_CSS}{it}</style></head><body>
<div class="pg"><nav class="nav"><b>Pam &amp; Sam</b><span><span class="l">Aanpak &nbsp; Tarieven &nbsp; Contact</span><a class="b">Probeer gratis</a></span></nav>
<section class="h"><p class="k">Iedereen worstelt weleens met zichzelf.</p><h1>Bespreek het <span>met Pam of Sam.</span></h1><p class="s">Jij komt op het antwoord.<i></i></p><a class="btn">Probeer gratis</a><p class="fine">{DISC}</p></section></div>
<div style="display:none" id="leesproef"><p style="font-family:var(--d);font-weight:400;font-size:20px;line-height:1.55">{PAMZIN}</p></div></body></html>'''
    open(os.path.join(D, 'letter-' + key + '.html'), 'w').write(html)

# ---------- vijf kleurparen (Pam warm, maar geen roze; Sam geen blauw) ----------
# w = muur, c = plafond, i = inkt, s = zacht, a = accent (knop, witte tekst)
K = {
 'a-terracotta-salie': dict(t='A · Terracotta en salie',
     p=dict(w='#ECDBC6', c='#F8F1E7', i='#2E1E14', s='#614A3A', a='#9A5536'), q=dict(w='#DDE2D8', c='#F0F3EC', i='#1C2419', s='#4A5545', a='#536651'),
     why='Aarde tegenover blad. Warm en koel zonder gender: een gebakken tegel en een plant in dezelfde kamer.'),
 'b-hout-grafiet': dict(t='B · Hout en grafiet',
     p=dict(w='#E8D6C0', c='#F6EDE2', i='#2C2014', s='#5E4A33', a='#85562C'), q=dict(w='#E2E1DD', c='#F3F2EF', i='#1E1E1C', s='#4C4B47', a='#3D3D3A'),
     why='Pam is de houten bank, Sam de stalen tafel. Sam heeft bijna geen kleur: nuchter als potlood op papier.'),
 'c-middag-ochtend': dict(t='C · Middag en ochtend',
     p=dict(w='#F1DCC6', c='#FBF2E8', i='#2F1F12', s='#644B35', a='#A2582E'), q=dict(w='#DDE5E1', c='#EFF4F1', i='#18231F', s='#46554F', a='#46665D'),
     why='Geleend van film: laat middaglicht tegenover vroeg ochtendlicht. Het verschil is de tijd van de dag, niet een kleur.'),
 'd-abrikoos-papier': dict(t='D · Abrikoos en papier',
     p=dict(w='#F3E0C9', c='#FCF5EC', i='#30200F', s='#67503C', a='#A65A35'), q=dict(w='#ECEBE6', c='#F9F8F5', i='#1A2228', s='#4A5157', a='#1F2A30'),
     why='Sam is een wit vel met inkt: geen sfeer, alleen tekst. Pam krijgt de enige kleur van het huis.'),
 'e-een-kamer': dict(t='E · Eén kamer, twee lampen',
     p=dict(w=Z['wall'], c=Z['ceil'], i=Z['ink'], s=Z['soft'], a='#9C6024'), q=dict(w=Z['wall'], c=Z['ceil'], i=Z['ink'], s=Z['soft'], a='#3F5A4F'),
     why='Ongemakkelijk ver: beide in dezelfde zandkamer. Alleen de lamp (het accent) en de letter verschillen. Je herkent Pam aan hoe ze praat, niet aan de muur.'),
}
KAMER_CSS = '''*{box-sizing:border-box;margin:0;padding:0}body{background:var(--zw);font-family:Jost,sans-serif;font-weight:300;-webkit-font-smoothing:antialiased;padding:40px max(24px,calc((100vw - 1100px)/2))}
.t{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--zs);margin-bottom:20px}
.g{display:grid;grid-template-columns:1fr 1fr;gap:24px}.r{border-radius:4px;overflow:hidden;color:var(--i);background:linear-gradient(var(--c) 0 26%,var(--w) 26%);min-height:520px;display:flex;flex-direction:column;padding:22px 26px 26px}
.r header{display:flex;justify-content:space-between;font-size:14px;color:var(--s)}.r header b{font-weight:400;color:var(--i);font-size:17px}.pam header b{font-family:"Source Serif 4",serif}
.log{flex:1;display:flex;flex-direction:column;justify-content:flex-end;gap:6px;padding-top:150px}.nm{font-size:12px;color:var(--s);display:flex;align-items:center;gap:8px}.nm:before{content:"";width:7px;height:7px;border-radius:50%;background:var(--a)}
.q{font-size:18px;line-height:1.55;color:var(--s)}.pam .q{font-family:"Source Serif 4",serif}.a{font-size:18px;line-height:1.55;font-weight:400;margin-top:10px}
.f{border-bottom:1px solid var(--i);padding:22px 0 10px;color:var(--s);font-size:16px}.acts{display:flex;justify-content:space-between;align-items:center;margin-top:18px;font-size:14px;color:var(--s)}
.acts span{text-decoration:underline;text-underline-offset:4px}.btn{background:var(--a);color:#fff;padding:11px 20px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;border-radius:2px;font-weight:400}
@media(max-width:700px){body{padding:20px 16px}.g{grid-template-columns:1fr}.r{min-height:420px}.log{padding-top:90px}.q,.a{font-size:16px}}
'''
def kamer(key):
    o = K[key]
    def side(v, d, name, other, q, a):
        return (f'<div class="r {v}" style="--w:{d["w"]};--c:{d["c"]};--i:{d["i"]};--s:{d["s"]};--a:{d["a"]}"><header><b>{name}</b><span>Menu &nbsp; ×</span></header>'
                f'<div class="log"><span class="nm">{name}</span><p class="q">{q}</p><p class="a">{a}</p></div><div class="f">Schrijf hier…</div>'
                f'<div class="acts"><span>Wissel naar {other}</span><a class="btn">Verstuur</a></div></div>')
    html = f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pam &amp; Sam · {o['t']}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400&family=Jost:wght@300;400&display=swap">
<style>:root{{--zw:{Z['wall']};--zs:{Z['soft']}}}{KAMER_CSS}</style></head><body><p class="t">{o['t']}</p><div class="g">
{side('pam', o['p'], 'Pam', 'Sam', PAMZIN, 'De buurt. Dat iemand me groette als ik naar buiten liep.')}
{side('sam', o['q'], 'Sam', 'Pam', 'Wat wil jij, los van wat anderen vinden?', 'Tijd. Ik wil mijn dochter van school halen.')}
</div></body></html>'''
    open(os.path.join(D, 'kamer-' + key + '.html'), 'w').write(html)
    worst = min(min(CR(d['s'], d['w']), CR(d['s'], d['c']), CR('#ffffff', d['a'])) for d in (o['p'], o['q']))
    return f'{key}: laagste contrast {worst:.2f}:1'

print('zand zacht: zachte tekst', round(CR(Z['soft'], Z['wall']), 2), 'inkt', round(CR(Z['ink'], Z['wall']), 2))
for k in F: font(k)
for k in K: print(kamer(k))
