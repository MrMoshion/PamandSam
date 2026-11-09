import os
D = os.path.dirname(os.path.abspath(__file__))
B = {
 'a-katern': ('A · Het katern',
   'De site als een opengeslagen tijdschrift. Links één beeld op grijs papier, rechts een gekleurd vlak met een gefluisterde titel en een inhoudsopgave in typemachineletter. Pam en Sam herken je aan de strook aan de rand, zoals een tabblad in een boek.',
   'Op de homepage is de inhoudsopgave de navigatie: elke regel is een deur. De wolk is een plaatshouder voor een echte foto van de lucht.',
   'In de kamer staat de naam van Pam of Sam als gefluisterd woord in het vlak. Jouw tekst staat donker en voorop, hun woorden zacht.'),
 'b-register': ('B · Het register',
   'De ongemakkelijk verre route: geen beeld, geen ceremonie. De hele site is een register, zoals de inhoudsopgave rechtsonder in de spread. Het verloop uit het vlak wordt een markering achter de regel die nu telt.',
   'Pam en Sam staan als eerste regels in het register. De strook aan de rand toont beide stemmen tot je kiest.',
   'Het gesprek wordt een genummerd verslag. Alleen de laatste vraag krijgt het verloop, als een markeerstift; de strook toont nu alleen de gekozen stem.'),
}
CSS = '''*{box-sizing:border-box;margin:0;padding:0}body{background:#fff;color:#262626;font-family:"Hanken Grotesk",sans-serif;font-weight:300;padding:72px 80px 96px}
h1{font-size:44px;font-weight:300;line-height:1.15;margin-bottom:24px}p{font-size:24px;line-height:1.45;max-width:46ch;margin-bottom:56px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:24px}.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:24px;margin-top:24px}
img{display:block;width:100%}.cap{font-size:18px;line-height:1.45;margin:16px 0 64px;max-width:70ch}'''
for k, (t, intro, c1, c2) in B.items():
    d = lambda s: f'<img src="{k}-{s}-d.png">'; m = lambda s: f'<img src="{k}-{s}-m.png">'
    html = f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300;500&display=swap"><style>{CSS}</style></head><body>
<h1>{t}</h1><p>{intro}</p>
<div class="g2">{d('home')}{d('info')}</div><p class="cap">{c1}</p>
<div class="g2">{d('pam')}{d('sam')}</div><p class="cap">{c2}</p>
<div class="g4">{m('home')}{m('info')}{m('pam')}{m('sam')}</div><p class="cap">Op de telefoon worden de twee pagina's één kolom; de strook aan de rand blijft.</p></body></html>'''
    open(os.path.join(D, f'bord-{k}.html'), 'w').write(html)
