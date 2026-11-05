# 37 · Commentaar op de testversie, ronde 1

Datum: 5 november 2026
Testversie: https://claude.ai/artifact/84bDmMXcAXSoYf1CryUXQx (versie 2, privé)
Bron: `site/pam-en-sam.html`
Skill bij deze laag: `design:design-critique` (de toets van het commentaar), daarna de bouw

## De regel die alles ordent: de hiërarchie van de huisstijl

- **De huisstijl van Pam & Sam** geldt voor alles wat Pam & Sam is: de site, de onderwerppagina's, de vergelijking, de citaten en de knoppen. Hij gebruikt IBM Plex Sans Light en geen cursief.
- **De huisstijl van Pam of Sam** geldt alleen in hun gesprek. Ook het verslag komt uit de stijl van Pam of Sam, niet uit die van Pam & Sam.
- Dat betekent: Pams cursief (Plex Serif licht) staat nergens anders op de site. De vlakken om te kiezen op de homepage zijn een voorproefje van het gesprek en houden daarom de stem.

## Het commentaar en wat er is gedaan

| # | Commentaar | Besluit en uitvoering |
|---|---|---|
| 1 | Het gesprek begint zoals Pardo het ontwierp | Het gesprek opent met Pardo's eigen introductie van Pam of Sam. De vlakken op de homepage gebruiken de korte versie |
| 2 | Markeren gaat niet soepel | Markeren werkt nu zoals selecteren: zet Markeer aan en selecteer tekst met muis, vinger of toetsenbord. Selecteer je hetzelfde nog eens, dan verdwijnt de markering. Geel voor Pam en Sam |
| 3 | Doorstrepen op dezelfde manier | Werkt net zoals markeren |
| 4 | Een mooie, snelle overgang bij het wisselen | Het oude licht vervaagt en de tekst wisselt van letter, samen in ongeveer 0,4 seconde |
| 5 | Geen knipperende cursor in het logo | Het logo knippert niet meer. Alleen de getypte zin in de kop knippert, en maar kort |
| 6 | Het verslag is het hele gesprek, zonder de doorgestreepte woorden | Het verslag toont het hele gesprek, met de markeringen. Wat je doorstreepte valt weg, ook bij kopiëren. De uitleg over "loslaten" is weg |
| 7 | Meerdere onderwerpen, zoals een chatgeschiedenis | De knop "Onderwerpen" opent een lijst met je gesprekken en "Nieuw onderwerp". De titel komt uit je eerste bericht. Alles blijft in je eigen browser. In het echte product is dit voor de betaalde versie, maar het staat in de testversie om te kunnen testen |
| 8 | Groter worden en terugkrimpen gaat soepeler, zonder de harde streep van Sam | Tijdens het groeien is alleen het vlak zichtbaar. De diagonaal en de tekst komen daarna rustig in beeld. Bij sluiten vervaagt eerst de inhoud en krimpt het vlak daarna terug, zonder schokken |
| 9 | De brug met de kernpunten mag weg | Verwijderd |
| 10 | "Hoe het werkt" in drie blokken | Drie losse vlakken, zoals op de echte site |
| 11 | De foto van Caren | Opgenomen |
| 12 | Pam & Sam verlicht in "Waarom niet een gratis chatbot?" | De kolom van Pam & Sam is een verlicht vlak. De gratis chatbot staat er kaal naast. Op mobiel staan ze onder elkaar |
| 13 | De pagina's van "Herken je jezelf hierin?" in de huisstijl | Drie pagina's met de tekst van de echte site: Vast in een keuze, Spanning in je relatie, Werk wordt te veel. Met knoppen naar Pam en Sam. Pam of Sam weet dan via welk onderwerp je binnenkwam |
| 14 | Knoppen mogen meer opvallen | De hoofdknoppen zijn gevuld, en de randen zijn dikker en groter |
| 15 | Geen cursief van Pam buiten het gesprek | De citaten staan in Plex Sans Light. Zie de regel hierboven |

## Kritische lezing

- **Markeren door selecteren** is vertrouwd, maar op een telefoon is selecteren onhandig: je moet eerst lang drukken en dan de grepen verslepen. Dat moet de echte gebruikerstest uitwijzen. Het alternatief is een tik per woord, alleen op mobiel.
- **Het verslag na een wissel** toont het hele gesprek in de stijl van degene met wie je nu praat, ook de beurten van de vorige. Dat volgt de regel, maar het voelt mogelijk vreemd. Het is een open punt voor ronde 2.
- **Onderwerpen in de gratis versie.** In de testversie blijven gesprekken in de browser bewaard. Dat botst met de belofte "gratis wordt niets opgeslagen". Voor de echte site geldt: onderwerpen alleen voor abonnees, lokaal opgeslagen en altijd te wissen.

## Niet getest

- **De echte antwoorden van Pam en Sam** (via Claude) werken alleen op claude.ai. Lokaal is alleen de oefenversie met vaste vragen getest.
- Lokaal is wel nagelopen, op desktop en mobiel: geen fouten en geen horizontale scroll. Markeren, doorstrepen, wisselen, verslag, onderwerpen en de onderwerppagina's werken.

## Ronde 2 (zelfde dag)

| Commentaar | Uitvoering |
|---|---|
| Het voorproefje moet eruitzien zoals het echt is | Het vlak is het gesprek in het klein: het logo in de stijl van Pam of Sam, Pardo's volledige introductie, de schrijfregel en de knoppen. Een fout zette de achtergrond van de vlakken op leeg, waardoor Sam crème leek. Die is hersteld |
| De vergelijking is lelijk en in Pams kleur | Route A: de sectie staat in de schemering. De chatbot staat in het donker, Pam & Sam is een verlicht raam in neutraal wit licht |
| Na een wissel blijft de vraag van de ander staan | Elke beurt houdt zijn eigen stem en heeft een korte naam erboven. Alles staat in de stijl van het venster waarin je zit. Bij een wissel stelt de nieuwe stem zich voor en stelt dan één vraag. Is er nog niets gezegd, dan wisselt alleen de introductie |
| Geen keuzevakken | De suggesties zijn weg. Je begint met een lege regel |
| Markeer en doorstreep als icoon, met een vraagteken | Twee ronde icoonknoppen met een label bij aanwijzen. Het vraagteken opent een kaartje met twee kleine animaties |
| Van het vlak naar het venster en terug | De achtergrond groeit van het vlak naar het scherm. De introductie en het logo schuiven mee naar hun plek. De rest vervaagt daarna in beeld. Sluiten gaat precies omgekeerd |
| De kop kleiner, en "Bespreek het met Pam of Sam" | De kop is kleiner, met daaronder "Bespreek het met Pam of Sam." en dan de getypte regel "Jij komt op het antwoord." |
