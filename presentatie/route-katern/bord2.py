CSS = open('bord.py').read().split("CSS = '''")[1].split("'''")[0]
html = f'''<!doctype html><html lang="nl"><head><meta charset="utf-8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300;500&display=swap"><style>{CSS}</style></head><body>
<h1>Het register, tweede ronde</h1><p>Markeren wordt de huisstijl. Elke markering is een eigen, net iets andere versie van het verloop, zoals een markeerstift nooit twee keer hetzelfde trekt. Pam en Sam staan even sterk bovenaan, elk met hun eigen markering.</p>
<div class="g2"><img src="b-register-home-d.png"><img src="b-register-lijn-home-d.png"></div><p class="cap">Links de knop gevuld met het verloop, rechts een dunne lijn met een markeerstreep door de tekst. Pam markeert van lavendel naar ijs, Sam van ijs naar mint.</p>
<div class="g2"><img src="b-register-pam-d.png"><img src="b-register-lijn-sam-d.png"></div><p class="cap">In het gesprek krijgt alleen de laatste vraag een markering, in de kleur van de stem. De verstuurknop volgt dezelfde stem.</p>
<img src="markeringen.png"><p class="cap">Een staal: zes knoppen in beide stijlen en markeringen in lopende tekst, elk net anders. De knoppen zijn een tint dieper dan de markeringen, zodat ze opvallen zonder hard te worden.</p>
<div class="g4"><img src="b-register-home-m.png"><img src="b-register-lijn-home-m.png"><img src="b-register-pam-m.png"><img src="b-register-lijn-sam-m.png"></div><p class="cap">Op de telefoon staan Pam en Sam als eerste twee regels, direct onder de kop.</p></body></html>'''
open('bord-register-2.html', 'w').write(html)
