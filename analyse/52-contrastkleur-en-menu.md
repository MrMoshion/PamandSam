# 52 · Contrastkleur voor de huisstijl, sticky menu, meer lucht (previews)

Vraag van de ontwerper (7 november 2026):
- De huisstijl krijgt een overkoepelende contrastkleur.
- Het menu is sticky en enkel, niet dubbel. Bij scrollen wordt het glas met 60% dekking.
- Meer lucht rond "Iedereen worstelt weleens met zichzelf."

Previews staan in `presentatie/route-couture-7/`. De site zelf is nog niet aangepast; dat bouw ik samen met de kleurkeuze.

## Wat de contrastkleur doet
De kleur doet twee dingen:
- **Klein:** de stip voor de bovenregel, de cursor achter de getypte regel en de onderstreping van links.
- **Groot:** één vlak per pagina, voor een sectie die eruit mag springen ("Waarom niet gewoon een gratis chatbot?").

De knoppen blijven zacht gevuld (#7A6D58). De contrastkleur is geen knopkleur.

**Het cliché:** een "kalmerende" pastel, zoals mint of lila, of het blauw van elke zorgsite. Dat is uitgesloten.

| # | Kleur | Hex | Tekst op het vlak | Als lijn of stip op zand | Idee |
|---|---|---|---|---|---|
| 1 | Mos | #5E6B45 | 5,3:1 | 4,8:1 | een plant in de kamer |
| 2 | Petrol | #2F5A5A | 7,1:1 | 6,4:1 | geglazuurd aardewerk, koel tegen zand |
| 3 | Roest | #9A4E30 | 6,0:1 | 5,0:1 | gebrande aarde; dicht bij Pams hout, rood alleen gedempt |
| 4 | Pruim | #5A3B4C | 9,0:1 | 8,1:1 | een fluwelen stoel; couture zonder roze |
| 5 | Diep oker | #8C6420 | 5,3:1 | 4,4:1 | toon op toon, het minst opvallend |
| 6 | Markeerstift | #D9DE6A | inkt erop 9,9:1 | — | ongemakkelijk ver: alleen áchter woorden, zoals onderstrepen in een zelfhulpboek (11); geen vlakken |

**Advies:** 4 · Pruim.
- Het is de enige kleur die couture voelt zonder roze.
- Hij is ver genoeg van Pams hout en Sams papier om bij geen van beiden te horen. Dat is precies wat een overkoepelende kleur moet doen.
- Hij heeft het hoogste contrast.

**Alternatief:** 1 · Mos, als het lichter en levendiger mag.

**Kritische lezing:**
- Pruim kan zwaar of ernstig worden als hij te vaak terugkomt. Daarom maximaal één vlak per pagina.
- Roest en oker liggen te dicht bij Pam: dan lijkt de huisstijl een Pam-pagina.
- Markeerstift is het meest eigen en sluit aan op het idee van markeren en doorstrepen (11). Als vlak werkt hij niet, en bij veel gebruik wordt het een gimmick.

## Menu
- Eén balk, sticky bovenaan. Geen tweede balk meer die verschijnt.
- Bovenaan de pagina is hij doorzichtig.
- Zodra je scrolt, wordt hij glas: het plafond met 60% dekking, met een zachte vervaging erachter en een haarlijn eronder.
- De overgang duurt 0,4 seconde; er knippert niets.

## Meer lucht
- Boven de bovenregel staat 56px meer ruimte.
- Tussen de bovenregel en de kop staat nu 44px (was 22px). Op mobiel 32px.
- De bovenregel breekt netjes over twee regels, met de stip ervoor.

**Niet getest:** hoe glas zich gedraagt in oudere browsers. Zonder ondersteuning voor vervaging (`backdrop-filter`) wordt het een gewone balk met 60% dekking.
