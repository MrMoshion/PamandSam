# 41 · Van de tweede UX-test naar een 4 op elk criterium

Datum: 6 november 2026
Bron: de tweede UX-test met `arn-spark-ux-judge` (volledig rapport in `40-ux-test-ronde-2.md`)
Oordeel: **niet geslaagd**. Vijf van de negen criteria scoren onder de 4.

| # | Criterium | Ronde 1 | Ronde 2 |
|---|---|---|---|
| 1 | Rust en kalmte | 3 | 3 |
| 2 | Vloeiende overgangen | 3 | **2** |
| 3 | Huisstijl en rangorde | 3 | **4** |
| 4 | Gesprek ademt op mobiel | 4 | 4 |
| 5 | Duidelijkheid en vindbaarheid | 3 | 3 |
| 6 | Leesbaarheid en contrast | 2 | **3** |
| 7 | Raakvlakken en toetsenbord | 2 | 2 |
| 8 | Passend bij een kwetsbare gebruiker | 3 | 3 |
| 9 | Samenhang desktop en mobiel | 4 | 4 |

## Eerst eerlijk: wat ik zelf fout deed

Overgangen zakte van 3 naar 2, en dat komt door mijn eigen oplossingen uit de vorige ronde:

- **Openen.** Het groeiende vlak begint half doorzichtig. Daardoor zie je de tekst van het vlak eronder én de tekst die meeschuift: dubbel beeld. Die doorzichtigheid voegde ik toe om het vlak zacht te laten beginnen. Dat was een vergissing.
- **Sluiten.** Ik verborg de tekst in het vlak om dubbel beeld te voorkomen. Als er geen tekst meeschuift, bijvoorbeeld bij een gesprek met geschiedenis, krimpt er nu een leeg vlak terug. Ik loste het ene probleem op door een ander te maken.
- **Wisselen.** Het oude gesprek vervaagt in 0,45 s, en het nieuwe begint al na 0,2 s. Ze overlappen dus toch nog.
- **Bug.** Sluiten op een onderwerppagina na een wissel gaat terug naar de verkeerde knop.

Dit zijn geen keuzes van jou. Het zijn fouten van mij.

## Per criterium: wat is ideaal, waar botst het met jouw keuzes, en wat is de beste oplossing

### 1. Rust en kalmte (3, doel 4)

**Ideaal volgens de test**
- Niets knippert.
- Niets gaat via leeg.
- Een sprong naar een anker scrolt niet langs lege secties.

**Botsing met je keuze**
De knipperende cursor in de kop. De test rekent dat −0,5, omdat hij hard aan en uit springt en al knippert tijdens het typen.

**Beste oplossing (jouw keuze blijft staan)**
- De cursor blijft, maar knippert niet tijdens het typen. Daarna "ademt" hij twee à drie keer zacht (vervagen in plaats van springen) en blijft dan rustig staan. Dat dient nog steeds het doel, typen als opener, maar zonder hard aan en uit.
- Sluiten gaat nooit via een leeg vlak. De tekst van het vlak vloeit in terwijl het venster krimpt.
- Bij een sprong via het menu (bijvoorbeeld naar Aanpak) zijn alle secties onderweg al zichtbaar. Het zachte binnenkomen geldt alleen voor gewoon scrollen.
- Bij terug naar home blijft de tekst in de kop staan.

**Verwachting: 4.**

### 2. Vloeiende overgangen (2, doel 4)

**Ideaal volgens de test**
Overal eerst het oude weg en dan het nieuwe erin, nooit allebei tegelijk leesbaar.

**Botsing met je keuze**
Alles staat in de stijl van het venster. Bij wisselen verandert daardoor ook het lettertype (Pam serif, Sam sans) en de regelafbreking. Overlappende tekst is dan extra onrustig. De test rekent dat −0,5.

**Beste oplossing (jouw keuze blijft staan)**
- Wisselen gaat in twee stappen, na elkaar en niet over elkaar:
  1. De oude tekst vervaagt in 0,3 s.
  2. De nieuwe tekst vloeit in 0,4 s in.

  Alleen de achtergrond loopt doorlopend over. Dan doet het wisselen van lettertype er niet meer toe, en is de botsing weg.
- Openen: het groeiende vlak is direct dekkend, en de tekst in het vlak verdwijnt vanaf het eerste beeld.
- Verslag: eerst vervaagt het gesprek, daarna komt het verslag in beeld.
- Paginawissel: de oude pagina vervaagt boven de nieuwe, en het vaste menu verdwijnt direct.
- De bug bij het sluiten op een onderwerppagina wordt hersteld.

**Verwachting: 4.**

### 3. Huisstijl en rangorde (4)

Gehaald. Pam in roman en de stijl per venster worden geaccepteerd.

**Voor een 5:** aan Pams naam boven haar beurten mag haar kleur meer zichtbaar zijn.

### 4. Gesprek ademt op mobiel (4)

Gehaald.

### 5. Duidelijkheid en vindbaarheid (3, doel 4)

**Ideaal volgens de test**
Elke functie heeft één naam, er zijn weinig verschillende ingangen, en de teksten kloppen met wat er is.

**Botsingen met je keuzes**
- **"Vat het samen" opent een "Verslag" met het hele gesprek.** Jouw keuze is dat het verslag het hele gesprek is, zonder de doorgestreepte woorden. Dat is prima, maar "samenvatten" belooft iets anders.
- **De opslagbelofte die pas bij de livegang wordt aangepast.** De test rekent dat −0,5.

**Beste oplossing**
- **Eén naam voor het verslag.** Mijn voorstel: **"Je gesprek op een rij"**, op de knop en als titel. Het belooft geen samenvatting, en het verslag is precies dat: je gesprek, geordend. Alternatieven:
  - "Verslag": helder, maar wat zakelijk;
  - "Terugblik": warm, maar vager.
- **Twee namen voor beginnen in plaats van zeven.** "Begin bij Pam" en "Begin bij Sam" bij de keuze, en "Probeer gratis" overal elders. "Nu starten" bij de betaalde abonnementen verwijst nu naar het gratis gesprek. Dat wordt "Begin gratis" of verwijst naar de uitleg over de abonnementen.
- **FAQ:**
  - de "wisknop" die niet bestaat verdwijnt uit de tekst;
  - Sam wordt "direct en nuchter" genoemd, zoals overal.

  Deze teksten komen van de oude site.
- **Dubbele onderwerpen.** "Met Pam" op dezelfde onderwerppagina opent het bestaande onderwerp opnieuw in plaats van een nieuw te maken.
- **De titel van het verslag** wordt niet meer midden in een woord afgekapt, maar na een heel woord.
- **De opslagbelofte.** Een kleine, eerlijke regel "Testversie: je gesprekken blijven in deze browser" bij de chat lost de tegenspraak nu al op, zonder de livegang voor te zijn. Zie ook 8.

**Verwachting: 4.**

### 6. Leesbaarheid en contrast (3, doel 4)

Alleen de aanloopzin "Iedereen worstelt weleens met zichzelf." haalt de norm niet: 4,12:1, en de norm is 4,5:1.

**Oplossing:** een iets lichtere kleur, zodat de zin rond de 5:1 uitkomt. Er is geen botsing met een keuze.

**Verwachting: 4 tot 5.**

### 7. Raakvlakken en toetsenbord (2, doel 4)

**Ideaal volgens de test**
- Alles is minstens 44 px groot.
- Elke knop heeft een zichtbare focusrand.
- De focus blijft in het venster en keert na sluiten terug naar de knop waar je vandaan kwam.

**Botsing met je keuze**
Jij hebt de focus in het venster houden en de sterkere focusrand geparkeerd. De test rekent dat −1. **Zonder die twee punten komt dit criterium niet boven de 3.**

**Beste oplossing**
Eerst wat zonder discussie kan:
- De hulpnummers in de chat, "Probeer gratis" en de menulinks worden minstens 44 px.
- Elke knop krijgt een zichtbare focusrand.
- Na het sluiten van Onderwerpen gaat de focus terug naar de knop "Onderwerpen".
- Het verborgen menu is niet meer bereikbaar met Tab.

Daarna de twee geparkeerde punten, als jij ze vrijgeeft. Kort uitgelegd, omdat ze eerder onduidelijk waren:
- **Focus in het venster.** Wie met het toetsenbord werkt (Tab-toets), of met een schermlezer voor blinden en slechtzienden, springt nu van het chatvenster naar de pagina erachter, die hij niet ziet. Hij raakt dan de weg kwijt. De oplossing is onzichtbaar voor iedereen die met muis of vinger werkt.
- **De focusrand.** Dat is de rand om de knop waar je met Tab op staat. Op de lichte vlakken is hij nu bijna niet te zien. Een donkerdere rand is ook alleen zichtbaar voor wie met Tab werkt.

**Verwachting: 3 zonder de geparkeerde punten, 4 met.** Mijn advies: geef ze vrij. Ze veranderen niets aan het beeld voor de meeste mensen, en ze zijn de grootste winst op dit criterium.

### 8. Passend bij een kwetsbare gebruiker (3, doel 4)

**Ideaal volgens de test**
- Hulpnummers zijn overal één tik.
- Er staat geen tegenstrijdige belofte over privacy op de site.
- Er wordt geen sociale druk gesuggereerd die je niet kunt waarmaken.

**Botsingen met je keuzes**
"Meest gekozen" en de opslagbelofte. De test rekent dat samen −0,75.

**Beste oplossing**
- 112, 113 en Veilig Thuis worden overal aantikbaar (op de homepage en de onderwerppagina's), met minstens 44 px. Er is geen botsing; dit alleen al is de grootste stap.
- De opslagbelofte: de eerlijke regel "Testversie" uit punt 5. Je keuze om het pas bij de livegang echt op te lossen blijft staan, maar de tegenspraak is dan niet meer verborgen.
- "Meest gekozen" blijft (jouw keuze). Het kost ongeveer een kwart punt.

**Verwachting: 4.**

### 9. Samenhang desktop en mobiel (4)

Gehaald.

## Samengevat

| Criterium | Wat nodig is | Botst met je keuze? | Verwachting |
|---|---|---|---|
| 1 Rust | Cursor ademt zacht na het typen, sluiten niet via leeg, ankersprong zonder lege secties | Ja, de knipperende cursor; opgelost door zacht te ademen | 4 |
| 2 Overgangen | Eerst het oude weg, dan het nieuwe; vlak direct dekkend; bug sluiten | Ja, de stijl per venster; opgelost door wisselen in twee stappen | 4 |
| 5 Duidelijkheid | Eén naam voor het verslag, twee voor beginnen, FAQ en titels | Licht: de naam "Vat het samen" | 4 |
| 6 Contrast | Aanloopzin lichter | Nee | 4–5 |
| 7 Bediening | 44 px, focusrand op alle knoppen, focus terug | Ja, de geparkeerde punten | 3, met de geparkeerde punten 4 |
| 8 Kwetsbare gebruiker | Hulpnummers overal aantikbaar, regel "Testversie" | Licht: "Meest gekozen" blijft | 4 |

**Conclusie:** zeven van de negen zijn zonder jouw keuzes los te laten naar een 4 te brengen, of zijn dat al. Criterium 7 heeft de twee geparkeerde toegankelijkheidspunten nodig. Criterium 2 en criterium 1 vragen dat ik mijn eigen fouten van de vorige ronde herstel.

**Wat jij moet kiezen**
1. Mag de cursor in de kop zacht ademen in plaats van hard knipperen?
2. Welke naam krijgt het verslag: "Je gesprek op een rij", "Verslag" of "Terugblik"?
3. Mogen de twee geparkeerde toegankelijkheidspunten nu mee?
4. Mag er een kleine regel "Testversie: je gesprekken blijven in deze browser" bij de chat?
