"""Een staal van de markering als huisstijl: telkens een andere, vaste variant."""
import importlib.util, io, contextlib, os
spec = importlib.util.spec_from_file_location('b', 'bouw.py')
with contextlib.redirect_stdout(io.StringIO()):
    b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
g = ''.join(b.btn(t, i * 7 + 3, 'grad', f) for i, (t, f) in enumerate([('Probeer gratis', 'mix'), ('Begin bij Pam', 'pam'), ('Begin bij Sam', 'sam'), ('Verstuur →', 'pam'), ('Verstuur →', 'sam'), ('Versturen', 'mix')]))
l = ''.join(b.btn(t, i * 7 + 3, 'lijn', f) for i, (t, f) in enumerate([('Probeer gratis', 'mix'), ('Begin bij Pam', 'pam'), ('Begin bij Sam', 'sam'), ('Verstuur →', 'pam'), ('Verstuur →', 'sam'), ('Versturen', 'mix')]))
w = lambda txt, seed, fam: f'<span style="background-image:{b.mark(seed, fam)};background-size:100% 48%;background-position:0 92%;background-repeat:no-repeat;padding:0 2px">{txt}</span>'
zin = f'Pam en Sam geven je geen {w("kant-en-klaar antwoord", 61, "mix")}. Ze stellen de vraag {w("die je zelf verder helpt", 73, "pam")}, en je gaat weg met {w("één stap in je eigen woorden", 89, "sam")}.'
html = f'''<!doctype html><html lang="nl"><head><meta charset="utf-8">{b.FONTS}<style>{b.COMMON}
body{{background:{b.SHEET};padding:56px 64px}}.r{{display:flex;flex-wrap:wrap;gap:18px;margin-bottom:40px}}
.bt{{display:inline-block;font-family:"Courier Prime",monospace;font-size:15px;color:{b.INK};padding:11px 18px}}.bt-s{{border:1px solid {b.INK};padding:10px 17px}}.bt-s span{{padding:0 3px}}
p.z{{font-family:Newsreader,serif;font-size:30px;line-height:1.5;max-width:40ch}}</style></head><body><div class="r">{g}</div><div class="r">{l}</div><p class="z">{zin}</p></body></html>'''
open('markeringen.html', 'w').write(html)
