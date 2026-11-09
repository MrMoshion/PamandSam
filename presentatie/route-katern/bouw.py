"""Twee voorstellen op basis van de spread 'Requiem' (Emergence Magazine Vol. 6, Studio Airport).
A · Het katern: de site als een opengeslagen spread. B · Het register: de site als inhoudsopgave.
Elke pagina: ?s=home|info|pam|sam"""
import os
D = os.path.dirname(os.path.abspath(__file__))
def L(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in c]; return .2126*c[0] + .7152*c[1] + .0722*c[2]
def CR(a, b): x, y = L(a), L(b); return (max(x, y) + .05) / (min(x, y) + .05)

# kleuren uit de spread
PAPER = '#E7E7E4'   # grijs ongecoat papier (linkerpagina)
SHEET = '#F1F1EE'   # lichter vel
INK = '#222321'; SOFT = '#55574F'
MINT = '#CFE3DE'; MINT2 = '#BFD9D3'; LAV = '#CACBE6'; ICE = '#DCEAE7'
GREEN = '#17A07C'   # de verzadigde strook: Sam (één kleur, recht)
GRAD = 'linear-gradient(180deg,#9AA7E0 0%,#5B6FD6 38%,#3EA6A0 70%,#17A07C 100%)'  # de verloopstrook: Pam (gelaagd)
CLOUD = '''<svg class="cloud" viewBox="0 0 300 400" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><filter id="f%(i)s" x="0" y="0" width="100%%" height="100%%"><feTurbulence type="fractalNoise" baseFrequency=".0055 .009" numOctaves="6" seed="%(seed)s"/><feColorMatrix type="matrix" values="1 0 0 0 0  1 0 0 0 0  1 0 0 0 0  0 0 0 0 1"/><feComponentTransfer><feFuncR type="linear" slope="2.1" intercept="-.38"/><feFuncG type="linear" slope="2.1" intercept="-.38"/><feFuncB type="linear" slope="2.1" intercept="-.36"/></feComponentTransfer></filter><rect width="300" height="400" filter="url(#f%(i)s)"/></svg>'''
TOPICS = [('Vast in een keuze', 'Je hebt alle voor- en nadelen op een rij, en je komt nog steeds geen stap verder.'),
          ('Spanning in je relatie', 'Steeds dezelfde discussie, of juist een stilte die blijft hangen.'),
          ('Werk wordt te veel', 'Je lijst wordt langer, je energie korter.'),
          ('Iets is voorbij', 'Een baan, een huis, een gewoonte. Je weet nog niet wat ervoor in de plaats komt.')]
PAMLOG = [('Pam', 'Fijn dat je er bent. Vertel me rustig wat er speelt.'), ('Jij', 'Ik slaap slecht sinds de verhuizing. Het voelt alsof ik nergens thuis ben.'),
          ('Pam', 'Wat mis je het meest, als je eerlijk bent?'), ('Jij', 'De buurt. Dat iemand me groette als ik naar buiten liep.'), ('Pam', 'Wanneer voelde je je hier wél even gezien?')]
SAMLOG = [('Sam', 'Vertel me wat er speelt.'), ('Jij', 'Ik moet kiezen tussen een promotie en minder uren werken.'),
          ('Sam', 'Wat wil jij, los van wat anderen vinden?'), ('Jij', 'Tijd. Ik wil mijn dochter van school halen.'), ('Sam', 'Wat is dan je eerste stap?')]
DISC = '6 vragen gratis · geen creditcard · anoniem · gesprekken niet opgeslagen op onze servers'
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,300..500&family=Courier+Prime&family=Hanken+Grotesk:wght@300;400&display=swap">'
SWITCH = "<script>const s=new URLSearchParams(location.search).get('s')||'home';document.body.dataset.s=s;</script>"
COMMON = f'''*{{box-sizing:border-box;margin:0;padding:0}}a{{color:inherit;text-decoration:none}}ol,ul{{list-style:none}}
.scr{{display:none}}body[data-s=home] #home,body[data-s=info] #info,body[data-s=pam] #pam,body[data-s=sam] #sam{{display:block}}
body{{background:{PAPER};color:{INK};-webkit-font-smoothing:antialiased;font-family:"Hanken Grotesk",sans-serif;font-weight:300}}
.mono{{font-family:"Courier Prime",ui-monospace,monospace;font-weight:400}}.serif{{font-family:Newsreader,Georgia,serif}}
.cloud{{display:block;width:100%;height:100%}}
'''

# ================= A · HET KATERN =================
A_CSS = COMMON + f'''
.spread{{display:grid;grid-template-columns:1fr 1fr;min-height:100vh}}
.pL{{background:{PAPER};position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:6vh 6vw}}
.pL .img{{width:min(26vw,44vh);aspect-ratio:3/4;box-shadow:none}}
.pL .cred{{position:absolute;bottom:4.5vh;left:0;right:0;text-align:center;font-family:Newsreader,serif;font-weight:500;font-size:15px}}
.pL .logo{{position:absolute;top:3.6vh;left:3.4vw;font-family:Newsreader,serif;font-size:19px}}
.pR{{background:{SHEET};position:relative;padding:3.4vh 3.4vw 3.4vh 1.6vw;display:flex;flex-direction:column;gap:6px}}
.field{{position:relative;flex:1;display:flex;align-items:center;justify-content:center}}
.field.ft{{background:linear-gradient(180deg,{ICE},{MINT} 70%,{MINT2})}}
.field.fb{{background:linear-gradient(160deg,{LAV} 0%,#D3DDEA 35%,{MINT} 75%,{ICE});align-items:flex-start;justify-content:flex-start;padding:5.5vh 3vw}}
.whisper{{font-family:Newsreader,serif;font-weight:300;color:#fff;font-size:clamp(56px,6.4vw,104px);letter-spacing:-.01em;line-height:1}}
.strip{{position:absolute;right:1.3vw;width:12px}}.strip.g{{top:3.4vh;height:calc(50% - 3.4vh - 3px);background:{GREEN}}}.strip.p{{bottom:3.4vh;height:calc(50% - 3.4vh - 3px);background:{GRAD}}}
.toc{{font-family:"Courier Prime",monospace;font-size:14px;line-height:1.35;color:{INK};display:grid;grid-template-columns:7.5ch 1fr;row-gap:14px;column-gap:2ch;max-width:46ch}}
.toc .n{{color:{SOFT}}}.toc a{{display:block}}.toc a b{{font-weight:400;display:block}}
.lead{{font-family:Newsreader,serif;font-size:clamp(22px,1.9vw,28px);line-height:1.25;margin-bottom:4.5vh;max-width:26ch;font-weight:400}}
.lead span{{display:block;color:{SOFT};font-weight:300}}
.go{{grid-column:2;margin-top:6px;display:inline-block;background:{INK};color:{SHEET};padding:12px 18px;font-family:"Courier Prime",monospace;font-size:14px;width:max-content}}
.fine{{grid-column:2;font-size:12px;color:{SOFT}}}
/* info */
.pL.txt{{align-items:flex-start;justify-content:flex-start;padding:16vh 6vw 8vh 6vw}}
.pL.txt h2{{font-family:Newsreader,serif;font-weight:400;font-size:40px;line-height:1.1;margin-bottom:28px;max-width:16ch}}
.pL.txt p{{font-family:Newsreader,serif;font-size:19px;line-height:1.6;max-width:36ch;margin-bottom:16px;color:#33342f}}
.pL.txt .q{{font-size:26px;line-height:1.3;margin-top:24px;color:{INK}}}.pL.txt .by{{font-family:"Courier Prime",monospace;font-size:13px;color:{SOFT}}}
/* kamer */
.room{{min-height:100vh;display:grid;grid-template-columns:1fr minmax(0,720px) 1fr;background:{SHEET};position:relative}}
.room .col{{grid-column:2;display:flex;flex-direction:column;min-height:100vh;padding:3.4vh 0}}
.room .top{{height:30vh;display:flex;align-items:center;justify-content:center;position:relative}}
.room.pam .top{{background:linear-gradient(160deg,{LAV},#D3DDEA 45%,{MINT})}}.room.sam .top{{background:linear-gradient(180deg,{ICE},{MINT} 70%,{MINT2})}}
.room .bar{{position:fixed;top:0;bottom:0;right:0;width:12px}}.room.pam .bar{{background:{GRAD}}}.room.sam .bar{{background:{GREEN}}}
.room .nav{{position:absolute;top:3.4vh;left:3.4vw;right:3.4vw;display:flex;justify-content:space-between;font-family:"Courier Prime",monospace;font-size:13px;color:{SOFT}}}
.log{{flex:1;display:flex;flex-direction:column;justify-content:flex-end;gap:22px;padding:6vh 0 3vh}}
.t{{display:grid;grid-template-columns:6ch 1fr;column-gap:2ch}}.t .who{{font-family:"Courier Prime",monospace;font-size:13px;color:{SOFT};padding-top:5px}}
.t .v{{font-family:Newsreader,serif;font-size:19px;line-height:1.55;color:{SOFT}}}.t.me .v{{font-family:"Hanken Grotesk",sans-serif;font-size:19px;font-weight:400;color:{INK}}}
.room.sam .t .v{{font-family:"Hanken Grotesk",sans-serif;font-weight:300}}.room.sam .t.me .v{{font-weight:400}}
.inp{{display:grid;grid-template-columns:6ch 1fr;column-gap:2ch;padding-top:2vh}}.inp .f{{border-bottom:1px solid {INK};padding:10px 0;font-size:18px;color:{SOFT}}}
.inp .acts{{grid-column:2;display:flex;justify-content:space-between;align-items:center;margin-top:16px;font-family:"Courier Prime",monospace;font-size:13px;color:{SOFT}}}
.inp .acts a.s{{background:{INK};color:{SHEET};padding:10px 16px}}
@media(max-width:760px){{
 .spread{{grid-template-columns:1fr}}.pL{{min-height:auto;padding:76px 16px 56px}}.pL .img{{width:min(62vw,300px)}}.pL .logo{{top:20px;left:16px}}.pL .cred{{bottom:20px}}
 .pR{{padding:6px 16px 16px 16px;min-height:100vh}}.field.ft{{min-height:34vh;flex:none}}.field.fb{{padding:36px 22px 40px}}.strip{{right:4px;width:6px}}
 .whisper{{font-size:58px}}.toc{{grid-template-columns:6ch 1fr;font-size:13px}}
 .pL.txt{{padding:84px 16px 40px}}.pL.txt h2{{font-size:32px}}.pL.txt p{{font-size:17px}}
 .room .col{{padding:0 16px}}.room .top{{margin:0 -16px;height:26vh}}.room .nav{{left:16px;right:20px;top:18px}}.t,.inp{{grid-template-columns:1fr}}.t .who{{padding:0 0 2px}}.t .v,.t.me .v{{font-size:16px}}.room .bar{{width:6px}}.inp>span:first-child{{display:none}}.inp .acts{{grid-column:1}}}}
'''
def a_build():
    cloud = lambda i, seed: CLOUD % {'i': i, 'seed': seed}
    toc = ''.join(f'<span class="n">(P. {i*12+8:02d})</span><a><b>{t}</b></a>' for i, (t, d) in enumerate(TOPICS))
    home = f'''<div class="spread"><section class="pL"><a class="logo">Pam &amp; Sam</a><div class="img">{cloud('h', 7)}</div><p class="cred">Iedereen worstelt weleens met zichzelf.</p></section>
<section class="pR"><div class="field ft"><span class="whisper" aria-hidden="true">Pam &amp; Sam</span></div><div class="field fb"><div>
<h1 class="lead">Bespreek het met Pam of Sam.<span>Jij komt op het antwoord.</span></h1>
<div class="toc"><span class="n">(Pam)</span><a><b>Warm en empathisch</b>Ze geeft eerst ruimte aan wat je voelt.</a><span class="n">(Sam)</span><a><b>Direct en nuchter</b>Hij gaat zonder omweg naar de kern.</a>
{toc}<a class="go">Probeer gratis →</a><span class="fine">{DISC}</span></div></div></div>
<span class="strip g"></span><span class="strip p"></span></section></div>'''
    info = f'''<div class="spread"><section class="pL txt"><a class="logo">Pam &amp; Sam</a><h2>Waar het idee vandaan komt.</h2>
<p>Pam en Sam geven je geen kant-en-klaar antwoord. Ze stellen de vragen die je naar het antwoord leiden dat al in jezelf zit.</p>
<p>Ze zijn geïnspireerd door gesprekken met Caren, die mensen begeleidt bij stress rond werk, privéleven en ingrijpende veranderingen.</p>
<p class="q">“Wat je overkomt hoeft je leven niet te bepalen, je kunt kiezen hoe je erop reageert.”</p><p class="by">(Caren, adviseur bij Pam &amp; Sam)</p></section>
<section class="pR"><div class="field ft"><span class="whisper" aria-hidden="true">Aanpak</span></div><div class="field fb"><div class="toc">
<span class="n">(01)</span><a><b>Vertel wat er speelt</b>Schrijf het op zoals het in je hoofd zit.</a><span class="n">(02)</span><a><b>Beantwoord één vraag</b>Telkens één vraag. Geen advies.</a>
<span class="n">(03)</span><a><b>Kies je eigen stap</b>In je eigen woorden.</a><span class="n">(→)</span><a><b>Tarieven</b>Gratis kennismaking, daarna €5,99 per maand.</a></div></div>
<span class="strip g"></span><span class="strip p"></span></section></div>'''
    def room(v, log):
        nm = 'Pam' if v == 'pam' else 'Sam'; ot = 'Sam' if v == 'pam' else 'Pam'
        turns = ''.join(f'<div class="t{" me" if w == "Jij" else ""}"><span class="who">({w})</span><p class="v">{x}</p></div>' for w, x in log)
        return f'''<div class="room {v}"><span class="bar"></span><div class="col"><div class="top"><span class="nav"><span>(Onderwerpen)</span><span>(Terugblik) &nbsp; (×)</span></span><span class="whisper" aria-hidden="true">{nm}</span></div>
<div class="log">{turns}</div><div class="inp"><span></span><div class="f">Schrijf hier…</div><div class="acts"><a>(Wissel naar {ot})</a><a class="s">Verstuur →</a></div></div></div></div>'''
    html = f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pam &amp; Sam · Het katern</title>{FONTS}<style>{A_CSS}</style></head>
<body data-s="home"><div class="scr" id="home">{home}</div><div class="scr" id="info">{info}</div><div class="scr" id="pam">{room('pam', PAMLOG)}</div><div class="scr" id="sam">{room('sam', SAMLOG)}</div>{SWITCH}</body></html>'''
    open(os.path.join(D, 'a-katern.html'), 'w').write(html)

# ================= B · HET REGISTER =================
B_CSS = COMMON + f'''
body{{background:{SHEET}}}
.pg{{min-height:100vh;position:relative;padding:4vh 5vw 6vh 5vw}}
.edge{{position:fixed;top:0;bottom:0;right:0;width:10px;display:flex;flex-direction:column;gap:4px}}.edge i{{flex:1}}.edge .g{{background:{GREEN}}}.edge .p{{background:{GRAD}}}
.pam .edge .g,.sam .edge .p{{opacity:.18}}
.hd{{display:flex;justify-content:space-between;font-family:"Courier Prime",monospace;font-size:13px;color:{SOFT}}}.hd b{{font-weight:400;color:{INK}}}
.reg{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);column-gap:6vw;margin-top:14vh}}
h1.t{{font-family:Newsreader,serif;font-weight:300;font-size:clamp(40px,4.6vw,72px);line-height:1.04;letter-spacing:-.015em}}
h1.t span{{display:block;color:{SOFT}}}
.intro{{font-family:"Courier Prime",monospace;font-size:14px;line-height:1.5;color:{SOFT};margin-top:4vh;max-width:40ch}}
.rows{{font-family:"Courier Prime",monospace;font-size:15px;line-height:1.4}}
.row{{display:grid;grid-template-columns:8ch 1fr 9ch;column-gap:2ch;padding:16px 14px;margin:0 -14px}}
.row .n,.row .r{{color:{SOFT}}}.row .r{{text-align:right}}.row b{{font-weight:400;display:block}}.row span.d{{color:{SOFT};display:block;margin-top:2px}}
.row.mark{{background:linear-gradient(100deg,{LAV},#D3DDEA 45%,{MINT})}}
.row.go{{margin-top:18px}}.row.go b{{background:{INK};color:{SHEET};display:inline-block;padding:10px 16px}}
.foot{{position:absolute;left:5vw;bottom:4vh;font-family:"Courier Prime",monospace;font-size:12px;color:{SOFT}}}
/* info */
.cols{{display:grid;grid-template-columns:1fr 1fr 1fr;column-gap:3vw;margin-top:6vh}}.cols p{{font-family:Newsreader,serif;font-size:18px;line-height:1.6;color:#33342f}}
.cols .n{{font-family:"Courier Prime",monospace;font-size:13px;color:{SOFT};display:block;margin-bottom:10px}}
.q{{font-family:Newsreader,serif;font-size:clamp(26px,2.6vw,38px);line-height:1.25;max-width:30ch;margin-top:10vh}}.q + .by{{font-family:"Courier Prime",monospace;font-size:13px;color:{SOFT};margin-top:14px}}
/* kamer */
.chat{{max-width:760px;margin:0 auto;min-height:calc(100vh - 10vh);display:flex;flex-direction:column}}
.chat .log{{flex:1;display:flex;flex-direction:column;justify-content:flex-end;padding-top:8vh}}
.e{{display:grid;grid-template-columns:8ch 1fr;column-gap:2ch;padding:14px 14px;margin:0 -14px}}.e .n{{font-family:"Courier Prime",monospace;font-size:13px;color:{SOFT};padding-top:5px}}
.e .v{{font-size:19px;line-height:1.55}}.e.v-ai .v{{font-family:Newsreader,serif;color:{SOFT}}}.sam .e.v-ai .v{{font-family:"Hanken Grotesk",sans-serif;font-weight:300}}
.e.me .v{{font-family:"Hanken Grotesk",sans-serif;font-weight:400;color:{INK}}}
.e.now{{background:linear-gradient(100deg,{LAV},#D3DDEA 45%,{MINT})}}.sam .e.now{{background:linear-gradient(100deg,{ICE},{MINT})}}
.e.now .v{{color:{INK}}}
.ip{{display:grid;grid-template-columns:8ch 1fr;column-gap:2ch;padding:22px 0 0}}.ip .n{{font-family:"Courier Prime",monospace;font-size:13px;color:{SOFT};padding-top:12px}}.ip .f{{border-bottom:1px solid {INK};padding:10px 0;font-size:18px;color:{SOFT}}}
.ip .acts{{grid-column:2;display:flex;justify-content:space-between;align-items:center;margin-top:16px;font-family:"Courier Prime",monospace;font-size:13px;color:{SOFT}}}.ip .acts a.s{{background:{INK};color:{SHEET};padding:10px 16px}}
@media(max-width:760px){{.pg{{padding:20px 22px 40px 16px}}.reg{{grid-template-columns:1fr;margin-top:8vh}}.rows{{margin-top:6vh;font-size:14px}}.row{{grid-template-columns:8ch 1fr;column-gap:1ch}}.row .r{{display:none}}
 .cols{{grid-template-columns:1fr;row-gap:24px}}.edge{{width:6px}}.e,.ip{{grid-template-columns:1fr}}.e .n,.ip .n{{padding:0 0 2px}}.e .v{{font-size:16px}}.foot{{position:static;margin-top:6vh}}.ip .acts{{grid-column:1}}}}
'''
def b_build():
    edge = '<span class="edge"><i class="g"></i><i class="p"></i></span>'
    hd = '<header class="hd"><b>Pam &amp; Sam</b><span>(Aanpak) &nbsp; (Tarieven) &nbsp; (Contact)</span></header>'
    rows = (f'<div class="row mark"><span class="n">(Pam)</span><a><b>Warm en empathisch</b><span class="d">Ze geeft eerst ruimte aan wat je voelt.</span></a><span class="r">begin →</span></div>'
            f'<div class="row"><span class="n">(Sam)</span><a><b>Direct en nuchter</b><span class="d">Hij gaat zonder omweg naar de kern.</span></a><span class="r">begin →</span></div>'
            + ''.join(f'<div class="row"><span class="n">(P. {i*12+8:02d})</span><a><b>{t}</b><span class="d">{d}</span></a><span class="r">lees</span></div>' for i, (t, d) in enumerate(TOPICS))
            + '<div class="row go"><span class="n">(→)</span><a><b>Probeer gratis</b></a><span class="r"></span></div>')
    home = f'''<div class="pg">{hd}<div class="reg"><div><h1 class="t">Bespreek het met Pam of Sam.<span>Jij komt op het antwoord.</span></h1><p class="intro">Iedereen worstelt weleens met zichzelf. Kies een stem, of begin bij wat er speelt.</p></div>
<div class="rows">{rows}</div></div><p class="foot">{DISC}</p>{edge}</div>'''
    info = f'''<div class="pg">{hd}<div style="margin-top:14vh"><h1 class="t">Hoe het werkt.<span>Drie stappen. Niet meer.</span></h1></div>
<div class="cols"><p><span class="n">(01) Vertel wat er speelt</span>Schrijf het op zoals het in je hoofd zit. Pam of Sam luistert en vraagt door.</p><p><span class="n">(02) Beantwoord één vraag</span>Telkens één vraag. Geen advies, geen lijstjes. De vraag helpt je zelf verder.</p><p><span class="n">(03) Kies je eigen stap</span>Je gaat weg met één ding dat je vandaag nog kunt doen, in je eigen woorden.</p></div>
<p class="q">“Wat je overkomt hoeft je leven niet te bepalen, je kunt kiezen hoe je erop reageert.”</p><p class="by">(Caren, adviseur bij Pam &amp; Sam)</p>{edge}</div>'''
    def room(v, log):
        nm = 'Pam' if v == 'pam' else 'Sam'; ot = 'Sam' if v == 'pam' else 'Pam'
        ents = ''.join(f'<div class="e {"me" if w == "Jij" else "v-ai"}{" now" if i == len(log)-1 else ""}"><span class="n">({i+1:02d}) {w}</span><p class="v">{x}</p></div>' for i, (w, x) in enumerate(log))
        return f'''<div class="pg {v}"><header class="hd"><b>{nm}</b><span>(Onderwerpen) &nbsp; (Terugblik) &nbsp; (×)</span></header><div class="chat"><div class="log">{ents}</div>
<div class="ip"><span class="n">({len(log)+1:02d}) Jij</span><div class="f">Schrijf hier…</div><div class="acts"><a>(Wissel naar {ot})</a><a class="s">Verstuur →</a></div></div></div>{edge}</div>'''
    html = f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pam &amp; Sam · Het register</title>{FONTS}<style>{B_CSS}</style></head>
<body data-s="home"><div class="scr" id="home">{home}</div><div class="scr" id="info">{info}</div><div class="scr" id="pam">{room('pam', PAMLOG)}</div><div class="scr" id="sam">{room('sam', SAMLOG)}</div>{SWITCH}</body></html>'''
    open(os.path.join(D, 'b-register.html'), 'w').write(html)

a_build(); b_build()
for nm, a, b in [('zachte tekst op vel', SOFT, SHEET), ('zachte tekst op mint', SOFT, MINT), ('zachte tekst op lavendel', SOFT, LAV), ('inkt op lavendel', INK, LAV),
                 ('wit op mint (alleen woordmerk)', '#FFFFFF', MINT), ('groene strook naast vel', GREEN, SHEET)]:
    print(f'{nm}: {CR(a, b):.2f}:1')
