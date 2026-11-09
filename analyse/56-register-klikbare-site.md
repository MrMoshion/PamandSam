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

## Ronde 57: secties, foto's en gesprek (ontwerper, 9 november 2026)
Keuze: optie A (achtergrond), maar niet voor de eerlijke vraag. De ontwerper leverde twee nieuwe foto's: een groene muur met bladschaduw, en een bloemknop.

Doorgevoerd (artifact versie 2):
- **"Eerlijk, ook als het ongemakkelijk is.":** de hele kop is geel gemarkeerd.
- **"Waarom niet gewoon een gratis chatbot?":**
  - alleen de titel "Pam & Sam" boven die kolom is geel gemarkeerd;
  - rechts langs de kolom loopt een verlooplijn van Pam (lavendel) naar Sam (mint);
  - geen foto.
- **"Drie stappen. Niet meer.":** de groene muurfoto als achtergrond (optie A), met de stappen als lichte vellen erop.
- **"Pam & Sam is geen therapie.":** dezelfde verlooplijn rechts langs de box, en de titel geel gemarkeerd.
- **"Klaar om te beginnen?":** de bloemfoto links, zonder bijschrift (optie B). Op mobiel staat de foto boven de tekst.
- **In het gesprek:**
  - bij de laatste vraag is alleen het label gemarkeerd, zoals "(03) Sam", in de effen kleur van de stem;
  - jouw antwoorden staan in gewone letter (300), niet vet.
- **Lettergrootte:** op desktop weer in het menu van het gesprek (drie maten A, A, A; de gekozen maat geel). Op desktop is dat 20, 22 of 24 px; op mobiel 15, 17 of 19 px.
- **Hover hersteld:**
  - "Probeer gratis" kreeg bij hover lichte tekst op geel en viel daardoor weg;
  - "Begin bij Pam/Sam" verloor bij hover zijn verloop.
  - Beide blijven nu staan, met donkere tekst.
- **Gevonden tijdens het testen:** de bloemfoto werd 1120 px hoog, omdat de hoogte in de afbeelding zelf won van de verhouding. Hersteld.

Getest:
- openen en sluiten: 0 fouten;
- de pixeltests komen rustig tot 0;
- toetsenbord, focus en Escape werken;
- nergens horizontaal scrollen;
- de lettergrootte op desktop gaat van 20 naar 24 px;
- de antwoorden hebben gewicht 300;
- de hover-kleur blijft donker op geel.

## Ronde 58: onderwerppagina's als spread en het lijstje (ontwerper, 9 november 2026)
Gekozen: opmaak A · De spread (zie 57), met alles links uitgelijnd, ook de tweede alinea, en zonder inspringing.

Doorgevoerd (artifact versie 3):
- **Onderwerppagina's als spread.** Links de foto op een eigen vlak; die blijft staan terwijl je de tekst leest. Rechts staan:
  - een kopregel in typemachineletter met paginanummer;
  - de titel;
  - de eerste alinea iets groter, daarna gewone alinea's met witregels;
  - Pam en Sam als twee regels in hun verloop;
  - de kleine regel over hulp.
  - Per onderwerp een eigen foto: de twijg (keuze), de lathyrussen (relatie) en de pioen (werk).
- **"Drie stappen":** de muurfoto op 70%. Het kleine label "(Hoe het werkt)" haalt nu 4,9:1 (was 4,3); de kop haalt 10,3:1.
- **Knoppen met een lijn** (Terugblik, WhatsApp, LinkedIn, de kaartknoppen): de lijn is weg; bij hover verschijnt een dunne onderstreping.
- **Tarieven:**
  - het jaarabonnement heeft de verlooplijn links in plaats van een omlijning;
  - "Probeer gratis" in de gratis kaart heeft een gele markeerstreep, zonder vlak, en is daarmee ondergeschikt aan het jaarabonnement.
- **"Waarom niet gewoon een gratis chatbot?":** de verlooplijn staat links van de kolom Pam & Sam.
- **Menu:** geen lijn en geen schaduw meer onderaan.

Getest:
- openen en sluiten: 0 fouten;
- de pixeltests komen rustig tot 0;
- toetsenbord, focus en Escape werken;
- nergens horizontaal scrollen;
- de drie onderwerppagina's op desktop en mobiel bekeken.
