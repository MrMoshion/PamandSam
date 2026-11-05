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

## Ronde 3

- De kop volgt de rangorde van de originele site. De grote kop is "Bespreek het met Pam of Sam." Daarboven staat de kleine aanloopzin "Iedereen worstelt weleens met zichzelf.", en daaronder de getypte regel "Jij komt op het antwoord."
- De regel naast de knop is: 6 vragen gratis · geen creditcard · anoniem · gesprekken niet opgeslagen op onze servers.
- "Begin bij Pam" en "Begin bij Sam" staan op dezelfde hoogte, onderaan hun kolom.
- Les: een fout die de ontwerper al heeft benoemd, controleer ik op het beeld vóór ik iets oplever. In dit geval was dat de kleur van Sam in het voorproefje.

## Ronde 4

- De regel met de disclaimers staat op een rustig, donker vlak in wit, zodat hij goed leesbaar is. Hij mag niet lijken op kleine lettertjes.
- Op de onderwerppagina's staat "Begin gratis over …" met daaronder twee gelijkwaardige knoppen: "Met Pam" in Pams kleur en "Met Sam" in Sams kleur. Beide vlak, zonder verloop, zodat Pam niet meer wordt aangeprezen.
- Wisselen vloeit nu over. Het oude venster vervaagt in 0,8 seconde boven het nieuwe, zonder eerst naar leeg te gaan. De voorstelronde van de nieuwe stem komt pas daarna.
- De lichtbundel van Pam liep tijdens het groeien buiten het venster. Hij wordt nu afgesneden op de rand van het venster.
- Regel in CLAUDE.md: alles beweegt rustig en comfortabel.

## Ronde 5

- **Accent:** licht als accent, gekozen na vergelijking met greige, salie, oudroze en stormgrijs (beelden 26 tot en met 29).
  - In de schemering is de hoofdknop warm wit met een gloed. Op licht is hij donker met een warme gloed eronder.
  - De focusrand en de streep onder "Lees meer" zijn warm licht. Pams goud komt niet meer voor buiten het gesprek.
- **Kies je gesprekspartner:** het label, zoals "Pam · Warm & empathisch", staat boven het vlak. Er zit 28 px tussen de lijst en de knop.
- **Kop:** de disclaimer lijnt rechts uit met de knop "Probeer gratis" bovenin.
- **Mobiel, het gesprek ademt:**
  - De tekst is 17 px met regelafstand 1,6, met meer ruimte tussen de beurten.
  - Bovenin staan alleen het logo, "Menu" (Onderwerpen, Wissel, Verslag) en "Sluiten".
  - "Vat het samen" is een tekstlink. Verstuur is de enige knop.
  - Het venster volgt de ruimte boven het toetsenbord. Het inklappen van het toetsenbord doet iOS zelf, in Safari.
  - Desktop blijft zoals het was.
- **Markeren en doorstrepen:** voorlopig verborgen. De ontwerper kijkt hier later naar.
- **Overgangen:**
  - Onderwerpen schuift in en uit. Het verslag en het menu vervagen in en uit.
  - Wisselen van onderwerp vloeit over, net als wisselen tussen Pam en Sam.
  - Nieuwe berichten verschijnen zacht.
  - Onderwerppagina's vloeien over.
- **Ruimte rond knoppen (desktop):** bij alle knoppen en links is de afstand tot de tekst erboven nagemeten. Waar het krap was, is het minstens 24 px geworden: "Lees meer" op de kaarten, de knoppen bij de tarieven en de knoppen onder de formulieren. Knoppen naast elkaar staan op één lijn.
- **Les:** meet na elke ronde zelf de ruimte rond alle knoppen. Wacht daar niet mee tot de ontwerper het opmerkt.

## Ronde 6

- **Mobiel menu:** Onderwerpen, Wissel naar Pam of Sam, en Vat het samen. "Sluiten" is een X. "Verstuur" staat rechts.
- **Onderwerpen:** het paneel heeft geen vervaging van de achtergrond meer. Die zorgde voor haperingen tijdens het inschuiven. Het schuift nu strak in.
- **Sluiten na een wissel:** het venster gaat altijd terug naar het vlak van de stem waarbij je eindigt. Staat dat vlak buiten beeld, dan schuift de pagina er eerst onzichtbaar naartoe.
- **Probeer gratis:** gloeit, net als de hoofdknoppen.
- **Accenten (besluit ontwerper):** de gloed is het algemene accent. Pam is vlak geel (#C9A15F), Sam vlak blauw (#4F6F92), allebei zonder verloop. Ze komen terug als sporen van hun identiteit:
  - de knoppen "Begin bij Pam" en "Begin bij Sam";
  - de knoppen "Met Pam" en "Met Sam" op de onderwerppagina's;
  - een stip voor elk label.
- **Afwisseling in de secties:** warm linnen (een spoor van Pam), koel daglicht (een spoor van Sam) en lichtval (een zachte, schuine bundel licht). Daarnaast de schemering bij de vergelijking. Elke sectie loopt zacht in en uit, zonder harde randen.

## Ronde 7

- **Vast menu:** zodra je voorbij de kop scrolt, komt het menu rustig bovenaan in beeld, op een licht vlak. "Probeer gratis" gloeit erin.
- **"Waarom niet een gratis chatbot?"** staat nu in avondblauw, opgebouwd uit Sams blauw. Pam & Sam blijft het verlichte raam in wit licht.
- **Rustig binnenkomen:** koppen, tekst en vlakken vervagen één keer zacht in (0,9 s). Vlakken naast elkaar komen één voor één, met 0,12 s ertussen. "Herken je jezelf hierin?" en "Klaar om te beginnen?" worden getypt, met dezelfde cursor als in de kop. Wie in het systeem minder beweging heeft ingesteld, ziet alles direct.
- **De lichtbaan** is weg uit de secties en de koppen van de onderwerppagina's. In de kop van de homepage blijft ze, als opener (besluit ontwerper). Ze hoort alleen in de chatvensters, want daarbuiten oogde ze als een gimmick (besluit ontwerper).
- **Favicon en app-icoon:** de witte cursor met de gloed van de lamp, op de schemering. Bestanden in `assets/icon/`: favicon.svg, en app-icon in svg, 180 en 512 pixels.

## Ronde 8

- **"Waarom niet een gratis chatbot?":** gekozen is optie A uit beeld 30, een glazen box in Sams blauw op de gewone lichte achtergrond, zonder verloop. Pam & Sam blijft het verlichte raam erin. De box komt als geheel rustig binnen.
- **Onderwerpen en het menu op mobiel** staan nu in de stijl van het venster waarin je zit. Bij Pam warm licht, cursief en haar kleuren. Bij Sam daglicht en zijn blauw.

## Ronde 9

- De warme linnen secties lopen langer en zachter uit.
- De blauwe secties (Caren en "Belangrijk om te weten") zijn nu een vlakke, lichtblauwe box (#E9EEF2), zonder verloop. Regel: blauw staat nooit als verloop, alleen als box.
- De FAQ klapt zacht open en dicht. Er staat steeds maar één vraag open: opent er een nieuwe, dan klapt de vorige rustig dicht.
- Lichtblauwe boxen staan nu bij Caren, bij "Belangrijk om te weten" en bij "Stel een vraag" (vertrouwen, delen en contact).
- Cursief bij Pam staat alleen nog bij wat zij zegt en bij haar logo. Het menu, Onderwerpen en de titel van het verslag zijn roman.
- "Sluiten" is ook op desktop een X.

## Ronde 10

- **Mobiel:** "Wissel naar Pam" of "Wissel naar Sam" staat onder het gesprek, naast Verstuur. In het menu staan Onderwerpen en "Vat het samen". Desktop blijft zoals het was.
- **Mobiel:** de tekst in het gesprek is 15 px, de schrijfregel 16 px. Onder de 16 px zoomt de iPhone bij het typen vanzelf in.
- **Oorzaak van het eerdere probleem:** de regels voor mobiel stonden in het stijlblad vóór de gewone regels en werden daardoor overschreven. De tekst bleef dus 20 px, ook nadat ik meldde dat hij kleiner was. Het mobiele blok staat nu achteraan.
- **Les:** meet na elke wijziging de werkelijke waarde in de browser (lettergrootte, afstand), en lees die niet alleen af uit de code. En lees een opdracht van de ontwerper zin voor zin terug voordat ik bouw.

## Ronde 11

- **Wisselen op mobiel:** de oude knoppen en de balk zitten niet meer in de laag die wegvloeit, dus je ziet geen dubbele knoppen meer. Het oude gesprek vervaagt eerst (0,45 s), daarna komt het nieuwe (0,6 s). Ze lopen niet meer door elkaar.
- **Tekstgrootte in het menu op mobiel:** 15 px als standaard (door de ontwerper goedgekeurd), en twee stappen groter: 17 en 19 px. De keuze blijft bewaard, en het voorproefje schaalt mee.
- **Toetsenbord sluiten:** in de Claude-app ontbreekt de knop die Safari zelf laat zien. Daarom staat er een eigen icoon in de schrijfregel, een toetsenbord met een pijltje omlaag. Het verschijnt alleen op een touchscreen en alleen tijdens het typen. De Enter-toets van het toetsenbord heet "verstuur".
- Het toetsenbord-icoon verschijnt alleen als het toetsenbord echt open is of als je typt, niet al bij het openen van het venster.
- Wisselen kan altijd direct heen en weer. Een voorstelronde of beurt die nog bezig is, wordt afgebroken en weggehaald. Getest: zes keer snel wisselen, zonder hangende beurten.
