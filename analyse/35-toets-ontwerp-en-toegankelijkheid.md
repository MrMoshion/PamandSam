# 35 · Toets van de vier schermen: ontwerp en toegankelijkheid

Studio.Edu · 5 november 2026. Skills: `design:design-critique` en `design:accessibility-review` (WCAG 2.1 AA).

**Getoetst:**
- de homepage met de warme schemering, de lichtval en het getypte "Jij komt op het antwoord.";
- kiezen tussen Pam en Sam;
- de chat met Pam;
- de chat met Sam;
- het plan: een voorbeeld van de chat op de homepage waarin je direct kiest, en dat vlak groeit uit tot het hele chatscherm.

## Ontwerp
**Eerste indruk.** Rustig, warm, en geen AI-tool. De kop trekt het eerst de aandacht, en dat klopt. De regel "Zelfhulp, met AI als gesprekspartner" is te klein en te zwak voor wat hij moet doen: eerlijk zijn over de AI.

| Bevinding | Ernst | Voorstel |
|---|---|---|
| In de chat zie je niet waar je typt. Er is alleen een cursor, geen veld en geen manier om te versturen. | 🔴 | Een zichtbaar maar rustig schrijfveld: een dunne lijn met "Schrijf hier…". Versturen met Enter én met een knop "Verstuur". |
| "Ik ben er" is dubbelzinnig: het kan ook betekenen "ik ben aanwezig". | 🟡 | Toetsen met gebruikers. Alternatieven: "Ik heb mijn antwoord" of "Klaar voor nu". |
| Bij het voorbeeld van de chat is niet duidelijk dat je erin kunt klikken of typen. | 🟡 | In elk vlak een schrijfveld of de tekst "Begin bij Pam" of "Begin bij Sam". Bij het uitgroeien: een duidelijke weg terug. |
| In de chat ontbreekt een vangnet. | 🟡 | Bovenin de chat altijd zichtbaar "Hulp nodig?", met een verwijzing naar 113 en de huisarts. Past bij traumabewust ontwerp. |
| De sprong van de warme schemering naar het koele daglicht van Sam is groot. | 🟢 | Beoordelen in de echte site. Eventueel een iets warmere ondertoon in het daglicht. |
| "Je kunt later altijd wisselen" bij het kiezen. | ✅ | Houden: dit stelt gerust. |

**Hiërarchie.** In de chat is de hoofdvraag dominant en vervaagt het eerdere gesprek. Dat is goed bedoeld, maar het eerdere gesprek wordt te zwak om te lezen (zie hieronder).

## Toegankelijkheid
**Contrast** (eis voor gewone tekst 4,5:1, voor grote tekst 3:1, voor randen van knoppen 3:1):

| Element | Gemeten | Eis | Voorstel |
|---|---|---|---|
| Kop op de homepage | 10,5 | 3 | ✅ |
| "Pam en Sam stellen de vragen." | 5,0 | 4,5 | ✅ |
| Kleine regel "Gratis kennismaken · Zelfhulp…" (15 px) | 3,9 | 4,5 | ❌ dekking van 55% naar ±70% |
| Uitleg bij de kernpunten | 3,6 | 4,5 | ❌ dekking van 60% naar ±75% |
| Eerdere tekst in de chat van Pam | 2,7 | 4,5 | ❌ van 45% naar ±65% |
| Eerdere tekst in de chat van Sam | 2,9 | 4,5 | ❌ van 45% naar ±65% |
| "Verslag" in de kop van de chat | 2,8 | 4,5 | ❌ van 45% naar ±65% |
| Randen van de knoppen in de chat | 2,1 en 1,9 | 3 | ❌ van 30–35% naar ±55% |

**Beweging en schermlezers**
- **De knipperende cursor:** beweging die langer duurt dan 5 seconden moet te stoppen zijn (WCAG 2.2.2). Laat de cursor na een paar seconden stoppen met knipperen. Bij *reduced motion* knippert hij helemaal niet.
- **De getypte zin:** voor schermlezers staat de hele zin er meteen. Het typen is alleen beeld.
- **Het uitgroeien van het vlak:** bij *reduced motion* volgt direct de overgang, zonder groeien. De focus gaat naar het schrijfveld, en bij sluiten terug naar het gekozen vlak.
- **Antwoorden die verschijnen terwijl ze geschreven worden:** de schermlezer leest het antwoord pas voor als het af is (*aria-live polite*), niet woord voor woord.

**Bediening**
- De vlakken van Pam en Sam zijn echte knoppen, te kiezen met de toetsenbord. Met Escape sluit je de chat.
- Op de warme achtergrond moet zichtbaar zijn waar de focus staat.
- De knoppen in de chat moeten minstens 44 × 44 px zijn.
- Bij 200% zoom moet de opbouw heel blijven, ook op de telefoon.

## De belangrijkste aanpassingen voor het bouwen
1. **Een zichtbaar schrijfveld en een verstuurknop in de chat.** Zonder dat weet iemand niet wat hij moet doen.
2. **Het contrast van de zachte teksten en de knoppen omhoog.** De rust blijft, maar alles is leesbaar.
3. **Een vangnet in de chat:** "Hulp nodig?", altijd zichtbaar.
4. **Rustige beweging:** de cursor stopt met knipperen, *reduced motion* wordt gerespecteerd, en schermlezers krijgen de hele tekst.
5. **"Ik ben er" toetsen**, met een alternatief achter de hand.

## Besluiten van de ontwerper na de toets
- **Geparkeerd:** het vangnet ("Hulp nodig?") en het toetsen van "Ik ben er".
- **Het gesprek:** de chatbot stuurt aan op een conclusie in de woorden van de gebruiker.
- **Even groot:** de huidige vraag en de eigen tekst. De vraag staat in de stem van Pam of Sam, de eigen tekst in Plex Sans Light in de donkerste kleur. Het eerdere gesprek is kleiner en zachter, maar leesbaar.
- **De hele hoogte, zoals in een gewone chat:**
  - het schrijfveld staat vast onderaan, met *Vat het samen* en *Verstuur*;
  - het gesprek groeit naar boven;
  - geen tekstballonnen.
- **Ruimte:** meer ademruimte rondom en tussen de regels.
- **De plek van de kolom:** op desktop iets links van het midden. Op mobiel staat het schrijfveld onderaan, in het bereik van de duim. Zie beelden 22 en 23.
