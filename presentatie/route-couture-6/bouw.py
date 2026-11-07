"""Ronde 6: zachtere letter voor Pam (5 opties + huidige) en zachtere kleuren en knoppen (4 knopstijlen). Alleen previews."""
import os
D = os.path.dirname(os.path.abspath(__file__))
def L(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]; return .2126*c[0] + .7152*c[1] + .0722*c[2]
def CR(a, b): x, y = L(a), L(b); return (max(x, y) + .05) / (min(x, y) + .05)

# zachtere kleuren (voorstel)
N = dict(wall='#F0EADD', ceil='#F9F6F0', ink='#2F2A22', soft='#5E564A')
P = dict(wall='#EEE3D5', ceil='#F9F4EE', ink='#33281D', soft='#63523F', acc='#9A7350')
S = dict(wall='#EEEDEA', ceil='#FAF9F7', ink='#262C30', soft='#51575C', acc='#5A6268')
PAMMSG = 'Hoi, ik ben Pam. Fijn dat je er bent. Ik geef je geen kant-en-klaar advies. Ik stel je vragen die je helpen zelf helder te krijgen wat voor jou klopt. Vertel me rustig wat er speelt.'
PAMQ = 'Wat mis je het meest, als je eerlijk bent?'
JIJ = 'De buurt. Dat iemand me groette als ik naar buiten liep.'

# ---------- letters voor Pam ----------
FL = {
 '0-literata-nu':  dict(t='Nu · Literata', link='Literata:opsz,wght@7..72,300..500', fam='"Literata"', h=400, b=300, extra='',
                        why='De huidige keuze, ter vergelijking.'),
 '1-fraunces-zacht': dict(t='1 · Fraunces, zacht', link='Fraunces:opsz,wght,SOFT@9..144,300..400,0..100', fam='"Fraunces"', h=300, b=300, extra='font-variation-settings:"SOFT" 100;',
                        why='Afgeronde schreven en uiteinden: de letter heeft geen scherpe hoeken. Het zachtst van allemaal.'),
 '2-alegreya':     dict(t='2 · Alegreya', link='Alegreya:wght@400;500', fam='"Alegreya"', h=400, b=400, extra='',
                        why='Geschreven met een pen: levendig en literair, met een ritme als handschrift. Gemaakt voor lange teksten.'),
 '3-lora':         dict(t='3 · Lora', link='Lora:wght@400;500', fam='"Lora"', h=400, b=400, extra='',
                        why='Penseelachtige rondingen met een gewone opbouw: warm en vertrouwd. Ook veel gebruikt, dus minder eigen.'),
 '4-crimson':      dict(t='4 · Crimson Pro', link='Crimson+Pro:wght@300;400', fam='"Crimson Pro"', h=300, b=400, extra='',
                        why='Klassieke boekletter in de traditie van Garamond: rustig en ingetogen, als een bladzijde in een boek.'),
 '5-nunito':       dict(t='5 · Nunito (geen schreef)', link='Nunito:wght@300;400', fam='"Nunito"', h=300, b=400, extra='',
                        why='Ongemakkelijk ver: Pam zonder schreef, met ronde uiteinden. Het zachtst in de hand, maar het kan kinderlijk worden.'),
}
FCSS = '''*{box-sizing:border-box;margin:0;padding:0}body{font-family:Jost,sans-serif;font-weight:300;-webkit-font-smoothing:antialiased;background:%(nw)s;color:%(ni)s}
.b{display:grid;grid-template-columns:1.35fr 1fr;height:100vh}
.hero{background:linear-gradient(%(nc)s 0 34%%,%(nw)s 34%%);display:flex;flex-direction:column}
.nav{display:flex;justify-content:space-between;padding:26px 40px;font-size:14px;color:%(ns)s}.nav b{font-family:var(--f);font-weight:400;font-size:22px;color:%(ni)s;var(--x)}
.h{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;text-align:center;padding:calc(34vh - 60px) 32px 40px}
.k{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:%(ns)s}
h1{font-family:var(--f);font-weight:var(--hw);font-size:74px;line-height:1.04;letter-spacing:-.02em;margin:20px 0 18px}
.s{font-size:19px}
.room{background:linear-gradient(%(pc)s 0 26%%,%(pw)s 26%%);color:%(pi)s;display:flex;flex-direction:column;padding:26px 36px 32px}
.room header{display:flex;justify-content:space-between;font-size:14px;color:%(ps)s}.room header b{font-family:var(--f);font-weight:400;font-size:20px;color:%(pi)s}
.log{flex:1;display:flex;flex-direction:column;justify-content:flex-end;gap:8px}.nm{font-size:12px;color:%(ps)s;display:flex;gap:8px;align-items:center}.nm:before{content:"";width:6px;height:6px;border-radius:50%%;background:%(pa)s}
.pam{font-family:var(--f);font-weight:var(--bw);font-size:19px;line-height:1.6;color:%(ps)s}.q{margin-top:22px}
.jij{font-size:19px;line-height:1.55;font-weight:400;margin-top:10px}
.f{border-bottom:1px solid %(ps)s;padding:24px 0 10px;color:%(ps)s;font-size:17px}
.f2{display:flex;justify-content:space-between;align-items:center;margin-top:16px;font-size:14px;color:%(ps)s}
.f2 a{border:1px solid %(ps)s;color:%(pi)s;padding:10px 18px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;border-radius:2px}
*{font-variation-settings:inherit}h1,.pam,.nav b,.room header b{%(extra)s}
''' 
def fontpage(k):
    o = FL[k]
    css = FCSS % dict(nw=N['wall'], nc=N['ceil'], ni=N['ink'], ns=N['soft'], pw=P['wall'], pc=P['ceil'], pi=P['ink'], ps=P['soft'], pa=P['acc'], extra=o['extra'])
    css = css.replace('var(--x)', '')
    html = f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pam &amp; Sam · {o['t']}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={o['link']}&family=Jost:wght@300;400&display=swap"><style>:root{{--f:{o['fam']},Georgia,serif;--hw:{o['h']};--bw:{o['b']}}}{css}</style></head><body><div class="b">
<section class="hero"><nav class="nav"><b>Pam &amp; Sam</b><span>Aanpak &nbsp; Tarieven &nbsp; Contact</span></nav><div class="h"><p class="k">Iedereen worstelt weleens met zichzelf.</p><h1>Bespreek het<br>met Pam of Sam.</h1><p class="s">Jij komt op het antwoord.</p></div></section>
<section class="room"><header><b>Pam</b><span>Menu &nbsp; ×</span></header><div class="log"><span class="nm">Pam</span><p class="pam">{PAMMSG}</p><p class="jij">{JIJ}</p><span class="nm q">Pam</span><p class="pam">{PAMQ}</p></div>
<div class="f">Schrijf hier…</div><div class="f2"><span>Wissel naar Sam</span><a>Verstuur</a></div></section></div></body></html>'''
    open(os.path.join(D, 'letter-' + k + '.html'), 'w').write(html)
for k in FL: fontpage(k)

# ---------- knopstijlen, toegepast op neutraal, Pam en Sam ----------
def darker(h, f):
    h = h.lstrip('#'); return '#' + ''.join(f'{max(0, int(int(h[i:i+2], 16) * f)):02X}' for i in (0, 2, 4))
BTN = {
 'nu':  dict(t='Nu · donkere inkt', why='Zoals het nu is: bijna zwart. Duidelijk, maar hard.'),
 'a':   dict(t='A · Zacht gevuld', why='Een gedempte middentoon met witte tekst. Nog altijd een echte knop, maar minder hard.'),
 'b':   dict(t='B · Licht gevuld', why='Een iets donkerder vlak van de eigen muurkleur met donkere tekst. De knop hoort bij de kamer.'),
 'c':   dict(t='C · Omlijnd', why='Alleen een dunne lijn en tekst. Het rustigst wat nog als knop leest.'),
 'd':   dict(t='D · Alleen tekst', why='Ongemakkelijk ver: "Verstuur →" zonder vlak. Het zachtst, maar minder snel te vinden voor iemand in onrust.'),
}
def btn(style, room):
    i, w = room['ink'], room['wall']
    if style == 'nu': return f'background:{i};color:{room["ceil"]};border:1px solid {i}'
    if style == 'a':  return f'background:{room["mid"]};color:#fff;border:1px solid {room["mid"]}'
    if style == 'b':  return f'background:{darker(w, .915)};color:{i};border:1px solid {darker(w, .915)}'
    if style == 'c':  return f'background:transparent;color:{i};border:1px solid {room["soft"]}'
    if style == 'd':  return f'background:transparent;color:{i};border:1px solid transparent;padding-left:0!important;padding-right:0!important;text-decoration:underline;text-underline-offset:6px'
ROOMS = [('neutraal', dict(N, mid='#7A6D58'), 'Probeer gratis'), ('pam', dict(P, mid='#8A6849'), 'Verstuur'), ('sam', dict(S, mid='#5F676D'), 'Verstuur')]
BCSS = '''*{box-sizing:border-box;margin:0;padding:0}body{font-family:Jost,sans-serif;font-weight:300;-webkit-font-smoothing:antialiased;background:#FBFAF8;padding:28px 32px}
.row{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
.c{border-radius:4px;overflow:hidden;height:300px;display:flex;flex-direction:column;justify-content:flex-end;padding:24px 26px}
.c .lab{font-size:11px;letter-spacing:.18em;text-transform:uppercase;margin-bottom:auto}
.c h2{font-family:"Literata",serif;font-weight:400;font-size:34px;letter-spacing:-.02em;margin-bottom:22px;text-align:center}
.c .msg{font-family:"Literata",serif;font-weight:300;font-size:17px;line-height:1.55;margin-bottom:6px}.c.sam .msg{font-family:Jost;font-weight:300}
.c .f{border-bottom:1px solid currentColor;padding:12px 0 8px;font-size:15px;opacity:.75}
.acts{display:flex;justify-content:space-between;align-items:center;margin-top:16px;font-size:14px}
.btn{display:inline-block;padding:12px 22px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;border-radius:2px;font-weight:400}
.cen{text-align:center}
'''
def btnpage(style):
    o = BTN[style]; cells = []; rep = []
    for name, r, label in ROOMS:
        b = btn(style, r)
        bg = f'linear-gradient({r["ceil"]} 0 30%,{r["wall"]} 30%)'
        if name == 'neutraal':
            inner = f'<p class="lab" style="color:{r["soft"]}">Huisstijl</p><h2 style="color:{r["ink"]}">Bespreek het met Pam of Sam.</h2><p class="cen"><a class="btn" style="{b}">{label}</a></p>'
        else:
            nm = 'Pam' if name == 'pam' else 'Sam'; other = 'Sam' if name == 'pam' else 'Pam'
            q = PAMQ if name == 'pam' else 'Wat wil jij, los van wat anderen vinden?'
            inner = (f'<p class="lab" style="color:{r["soft"]}">{nm}</p><p class="msg" style="color:{r["soft"]}">{q}</p><div class="f" style="color:{r["soft"]}">Schrijf hier…</div>'
                     f'<div class="acts" style="color:{r["soft"]}"><span style="text-decoration:underline;text-underline-offset:4px">Wissel naar {other}</span><a class="btn" style="{b}">{label}{" →" if style == "d" else ""}</a></div>')
        cells.append(f'<div class="c {name}" style="background:{bg};color:{r["ink"]}">{inner}</div>')
        # contrast van de knoptekst op de knop (of op de muur bij c/d)
        if style == 'nu': cr = CR(r['ceil'], r['ink'])
        elif style == 'a': cr = CR('#ffffff', r['mid'])
        elif style == 'b': cr = CR(r['ink'], darker(r['wall'], .915))
        else: cr = CR(r['ink'], r['wall'])
        rep.append(f'{name} {cr:.1f}:1')
    html = f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><title>Knop {o['t']}</title><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Literata:opsz,wght@7..72,300..500&family=Jost:wght@300;400&display=swap">
<style>{BCSS}</style></head><body><div class="row">{''.join(cells)}</div></body></html>'''
    open(os.path.join(D, 'knop-' + style + '.html'), 'w').write(html)
    return f"knop {style}: " + ', '.join(rep)

print('zacht neutraal: zachte tekst', round(CR(N['soft'], N['wall']), 2), '| pam', round(CR(P['soft'], P['wall']), 2), '| sam', round(CR(S['soft'], S['wall']), 2))
for s in BTN: print(btnpage(s))
