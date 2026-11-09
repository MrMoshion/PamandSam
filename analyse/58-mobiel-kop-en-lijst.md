# 58 · Mobiel: de kop en een lijst aanpassingen

Feedback van de ontwerper (9 november 2026):
- Het voorstel "Pam of Sam?" als spread werkt slecht en vervalt (zie 56).
- De kop is te druk. "Probeer gratis" staat al in het menu en mag uit de kop, op mobiel en ook op desktop.
- Pam en Sam als iets kleinere blokken in de kop: eerst drie previews.

## Drie opties voor de kop op mobiel
Preview: `presentatie/route-register-mobiel/overzicht-kop-mobiel.png`.

De zin staat bovenaan; de keuze voor Pam of Sam onderaan het eerste scherm. Daar bereikt je duim hem het makkelijkst; dat is een bekend principe uit het ontwerpen voor telefoons. Alle drie passen op 375×667 en 390×844, zonder horizontaal scrollen.

- **A · Twee tegels:** Pam en Sam als twee gelijke, vierkante tegels naast elkaar, met de naam groot in de eigen letter. Het duidelijkst als keuze.
- **B · Twee smalle regels:** twee lage regels onder elkaar. Het rustigst en het dichtst bij het register.
- **C · De namen zijn de knoppen (ongemakkelijk ver):** geen blokken. "Pam" en "Sam" in de kop zelf zijn gemarkeerd en aan te tikken. Het minst druk, maar je moet zien dat het knoppen zijn.

**Advies:** B. Het neemt het minst ruimte en past het best bij "het moet het doel dienen, geen effect zijn".

**Kritische lezing:**
- A is duidelijker, maar zwaarder.
- C is het mooist, maar bij C weet een kwetsbare gebruiker misschien niet dat hij op een woord moet tikken.

## Wat daarna gebouwd wordt (na akkoord)
1. "Probeer gratis" uit de kop, op mobiel en desktop. In het menu blijft hij staan.
2. De foto bij "Drie stappen" zo uitsnijden dat de bladschaduwen goed zichtbaar zijn.
3. "Waarom niet gewoon een gratis chatbot?": bij scrollen schuiven twee kaarten over elkaar, eerst de chatbot, dan Pam & Sam eroverheen.
4. De tariefkaarten bij "Transparant" stapelen op dezelfde manier.
5. "Jouw vertrouwen staat voorop" en "Ken je iemand die hier iets aan heeft?" worden echte kopjes in plaats van labels tussen haakjes, op desktop en mobiel. "Jouw vertrouwen staat voorop" krijgt de gele markering.

## Gebouwd (ontwerper koos B, 9 november 2026; artifact versie 5)
- **De kop.**
  - Op mobiel: optie B. De zin staat bovenaan; onderaan het eerste scherm staan twee smalle regels voor Pam en Sam, met alleen een pijl, en de kleine regel.
  - Op desktop staan de regels naast de zin, zoals eerst.
  - "Probeer gratis" is weg uit de kop, op beide; hij staat alleen in het menu.
- **Pam en Sam in de kop openen niet meer het gesprek.** Ze brengen je naar de uitleg over Pam of Sam bij "Pam of Sam?" verderop op de pagina, op desktop en mobiel. Op desktop staat er "lees meer →".
- **"Drie stappen":** de foto is uitgesneden vanaf de linkerbovenkant, zodat de bladschaduwen goed te zien zijn.
- **"Waarom niet gewoon een gratis chatbot?":** twee kaarten die bij scrollen over elkaar schuiven. Eerst de chatbot, dan schuift Pam & Sam eroverheen.
- **Tarieven:** de drie kaarten schuiven op dezelfde manier over elkaar. Het jaarabonnement komt als laatste bovenop.
- **Contact:** "Jouw vertrouwen staat voorop" (geel gemarkeerd) en "Ken je iemand die hier iets aan heeft?" zijn echte kopjes, op desktop en mobiel.

Getest:
- openen en sluiten: 0 fouten;
- de pixeltests komen rustig tot 0;
- toetsenbord en focus werken;
- nergens horizontaal scrollen;
- op 375×667 tot 760×1024 overlapt niets in de kop, en de kleine regel staat op het eerste scherm;
- een klik op Sam in de kop gaat naar de uitleg over Sam, zonder dat het gesprek opent.

**Kritische lezing:** schuivende kaarten zijn een bekend effect. Het blijft rustig zolang het alleen bij deze twee secties staat; niet verder uitbreiden.

## Ronde 61: geen schuivende kaarten, naadloos openen en sluiten (ontwerper, 9 november 2026)
- **De schuivende kaarten zijn weg** (eerlijke vraag en tarieven). De gewone opstelling is terug, met de verlooplijnen links.
- **Openen en sluiten naadloos**, zoals in de eerdere versies. Frame voor frame gevonden:
  1. Bij sluiten verdween eerst alle inhoud en stond er ongeveer 0,25 seconde een leeg vlak, voordat het venster ging krimpen. Omdat het vel bijna de kleur van de pagina heeft, leek de pagina even weg.
  2. Bij sluiten naar een regel landde een wit blok op de gekleurde regel van Pam of Sam en vervaagde pas daarna.
- **Hersteld:**
  - het krimpen begint na 0,09 seconde in plaats van 0,24, terwijl de inhoud nog vervaagt;
  - bij een regel lost het vlak tijdens het krimpen op in die regel;
  - bij een kleine kamer blijft de overvloeiing zoals die was, alleen iets eerder.
- **Getest:**
  - openen en sluiten: 0 fouten;
  - de pixeltest aan het eind van sluiten is nog rustiger (grootste afwijking 2,3, was 3,1);
  - openen: 6,7;
  - frame voor frame bekeken vanuit de kleine kamer en vanuit een onderwerppagina, op desktop en mobiel.
