# 56 · Het register als klikbare site

Feedback van de ontwerper (9 november 2026):
- De kop was te druk. De situaties horen verderop.
- Het hoeft niet letterlijk een register met alle info te zijn: "het moet altijd het doel dienen en geen effect zijn."
- Pam en Sam zijn het verloop.
- Verstuur in de chat is geen verloop, maar effen lavendel (Pam) of mint (Sam).
- De algemene accentkleur wordt geel, als een markeerstift, toegepast zoals in de previews.

Gebouwd in een nieuwe artifact: https://claude.ai/artifact/KRG2p6k7NDBdEWTGvfj7bB (bron in `site/register/`).

## Wat er staat
- **De kop.** Links de bovenregel, de zin, de getypte regel, "Probeer gratis" en de kleine regel. Rechts alleen Pam en Sam, als twee even sterke regels in hun eigen verloop.
  - Een klik op zo'n regel opent direct het gesprek: het venster groeit vanuit de regel.
  - De situaties staan verderop, in "Herken je jezelf hierin?".
- **Pam en Sam als verloop:**
  - Pam van lavendel naar ijs (#C6C8EA → #DCEAE7);
  - Sam van ijs naar mint (#DCEAE7 → #BFE1D3).
  - Aan de rechterrand staat een strook zoals de duimindex in het tijdschrift: boven Pam, onder Sam. In het gesprek alleen de gekozen stem.
- **Verstuur:** effen lavendel #C9CBEB bij Pam, effen mint #BFE0D3 bij Sam, met donkere tekst.
- **Geel als markeerstift** (#F4E86E en vier verwante tinten). Elke markering krijgt een eigen, vaste variant van het verloop. Geel staat op:
  - "Probeer gratis";
  - de knop in het menu;
  - "Versturen" bij de formulieren;
  - als streep onder "Lees meer";
  - op woorden die je zelf markeert in het gesprek.
- **Het gesprek als verslag.** Labels in typemachineletter: (01) Pam, (02) Jij, en zo verder.
  - De vraag die openstaat krijgt het verloop van de stem.
  - De begroeting krijgt dat niet; die is geen vraag die telt.
- **Eén menu**, altijd bovenaan. Bij scrollen wordt het glas met 60% dekking.
- **Letters:**
  - Newsreader voor koppen en Pam;
  - Hanken Grotesk voor tekst, Sam en jouw woorden;
  - Courier Prime voor de labels.

## Getest
- openen en sluiten frame voor frame: 0 fouten;
- pixeltests: openen en sluiten komen rustig tot 0;
- toetsenbord, focus en Escape werken;
- nergens horizontaal scrollen;
- de kop overlapt op 5 maten nergens;
- een gesprek met antwoord en nummering werkt.

**Niet getest:** de echte antwoorden van Pam en Sam buiten de artifact, en een echte iPhone.

## De drie sporen naast elkaar
1. **De kamer:** https://claude.ai/artifact/84bDmMXcAXSoYf1CryUXQx
2. **Couture** (de minimalistische versie): https://claude.ai/artifact/X18b7gD4h9jELpjFuiY2CK
3. **Het register:** https://claude.ai/artifact/KRG2p6k7NDBdEWTGvfj7bB

**Kritische lezing:**
- Het register leunt nu op de werking van de kamer. Dat maakt het volledig, maar sommige onderdelen, zoals de deuren met mini-kamers bij "Pam of Sam?", komen nog uit die wereld. Een eigen vorm voor die sectie zou het spoor zuiverder maken.
- Het geel is de luidste kleur van de site. Dat is goed voor één knop, maar het moet schaars blijven.

## De eerlijke vraag met een lichtbeeld (previews)
De ontwerper leverde een foto: bladschaduw op een warme muur. De vraag was die op drie manieren te plaatsen in de sectie "Waarom niet gewoon een gratis chatbot?". Previews staan in `presentatie/route-register-beeld/`.

- **A · Als achtergrond:** de foto vult de sectie; de vergelijking ligt erop als twee vellen, het vel van Pam & Sam lichter. Het meest sfeervol, maar de foto concurreert met de tekst.
- **B · Als plaat in het grid:** de foto staat naast de vergelijking, zoals de foto op de linkerpagina van de spread, met een bijschrift in typemachineletter. Het rustigst.
- **C · Licht op één kolom (ongemakkelijk ver):** alleen de kolom van Pam & Sam krijgt het licht, met een dun licht waas erover. Het beeld draagt de boodschap: hier valt het licht. Het meest eigen.

**Leesbaarheid:** de donkere tekst haalt op het donkerste deel van de foto ongeveer 8:1 (A en C).

**Advies:** C, omdat de foto daar iets zegt in plaats van alleen sfeer te maken. B als het rustiger moet.
