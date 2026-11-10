# 59 · "Pam of Sam?" en het logo (previews)

Ontwerper (10 november 2026):
- Punt 1 uit het oordeel van 58 was niet duidelijk: graag een preview, zonder de site aan te passen.
- Punt 2 (lengte en ritme van de homepage): niet mee eens. Het is de opzet van Pardo; de hiërarchie zit in de markeringen, boxen en beelden. Blijft zo.
- Punt 3: het logo mag beter, misschien met een cursor in het verloop. Gevraagd: vijf voorstellen, drie met een cursor en twee vrij maar gewaagd.
- Punt 4: "risico" was te groot uitgedrukt.

## "Pam of Sam?": nu en voorstel
Preview: `presentatie/route-register-kies/overzicht.png`. De site is niet aangepast.

- **Blijft:** de kleine kamers, omdat die laten zien hoe een gesprek eruitziet.
- **Weg:**
  - de stip met "Pam · Warm & empathisch" in typemachineletter;
  - de opsommingstekens;
  - de losse knop.
- **Nieuw:**
  - de naam als kopje in de eigen letter, met eronder één regel;
  - de lijst "Kies Pam als" zonder bolletjes, tussen dunne lijnen;
  - eronder de regel "Begin bij Pam" in het verloop, zoals in de kop.
  - De kolommen van Pam en Sam staan exact op dezelfde hoogte.
  - Het logo in de kleine kamer is bij Pam en Sam gelijk; dat verschilde.

## Het logo, vijf voorstellen
Preview: `presentatie/route-register-logo/overzicht.png`. Elk voorstel is getoond in de menubalk, op mobiel en groot. Geen enkele cursor knippert.

1. **Cursor achter de naam.** Schreefletter, met een staande cursor in het verloop. Het rustigst. Een cursor in een logo zie je vaker bij techbedrijven.
2. **Blokcursor, kleine letters.** Het herkenbaarst, ook als icoon, maar het voelt het meest als software.
3. **Cursor als onderstreep.** Typemachineletter, zoals een schrijfmachine die wacht. Die letter staat elders op de site bijna niet meer.
4. **De markering (vrij).** Eén streep van lavendel naar mint onder het hele woord. Het gebaar van de site wordt het merk. Klein wordt de streep een vlekje.
5. **Het &-teken als vorm (vrij).** Pam in schreef, Sam in schreefloos, en een groot &-teken in het verloop ertussen. Het &-teken kan los het icoon zijn. Het meest gewaagd; klein kan het druk worden.

**Advies:** 1 voor de site, omdat het het rustigst is en de cursor de essentie draagt: jij schrijft verder. 5 als je het merk meer eigen wilt maken; het &-teken is dan ook het app-icoon.

## Besluit (ontwerper, 10 november 2026)
- **"Pam of Sam?" blijft zoals het is.** Het huidige onderscheid, met alleen de stippen, is binnen de huisstijl juist subtiel en goed. Het voorstel vervalt.
- **Les voor Claude:** je hoeft niet alles te benoemen of te herontwerpen. Vertrouw op eigen eerdere ontwerpkeuzes. De vrije interpretaties werken het best.
- **Logo: 4, de markering.**
  - Alleen in de menubalk: "Pam & Sam" in Newsreader, met één streep van lavendel naar mint onder het hele woord.
  - Het gesprek en de kleine kamers blijven zoals ze waren; daar staat de markering al.
  - Het aantikbare vlak van het logo is 44 px hoog, zonder dat de streep verschuift.
  - Gebouwd in artifact versie 9. Alle tests zijn gedraaid: openen en sluiten 0 fouten, pixeltests 2,3 en 6,7, toetsenbord en focus, geen horizontaal scrollen.

## Rustig scrollen naar secties (10 november 2026; artifact versie 10)
- **Wat de ontwerper vroeg:** scrollen naar een sectie, vanuit het menu en vanuit alle knoppen die dat doen, met easing. Het ging net iets te snel.
- **Oorzaak:** de browser sprong zelf naar de sectie bij een klik op de link, met zijn eigen korte beweging.
- **Oplossing:**
  - Klikken op links naar een sectie vangt de site nu zelf op, en scrolt met dezelfde rustige beweging als naar de kleine kamers.
  - De duur is 0,9 tot 1,4 seconde, afhankelijk van de afstand, met zacht aanzetten en zacht uitlopen.
  - Scroll je zelf tijdens de beweging, dan stopt die meteen.
  - Bij de instelling voor minder beweging springt de pagina direct.
  - Het adres en de terugknop van de browser blijven werken.
- **Nagemeten:** menu naar Tarieven ongeveer 1,35 seconde; kop naar de uitleg over Sam en via "Probeer gratis" ongeveer 1 seconde. Vanaf een onderwerppagina terug naar een sectie werkt.
- **Getest:**
  - openen en sluiten: 0 fouten;
  - de pixeltests: 2,3 en 6,7;
  - toetsenbord en focus werken;
  - nergens horizontaal scrollen;
  - de kleine kamers blijven gevuld na navigeren.
