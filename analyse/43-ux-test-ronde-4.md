# Oordeel UX-jury: Pam & Sam, testversie (vaste kopie `vast.html`)

**Eindoordeel: NIET GESLAAGD**
**Werkwijze:** interactief. Ik heb het prototype zelf bediend met Playwright (Chromium) op desktop (1440×900), mobiel (390×844, aanraken) en tablet (700×1000). Ik heb filmstrips opgenomen via de schermopname van de browser, per beeld gemeten hoe zichtbaar elke laag is, en het contrast gemeten op de achtergrond zoals die echt getekend wordt (met verloop, lichtbaan en korrel). Ik ben zonder scores begonnen en heb niets uit eerdere rondes overgenomen.

Norm: score 1 tot 5, minimaal 4 per criterium. Zes van de negen criteria halen de 4 niet.

---

## Scores

| # | Criterium | Score | Status | Bewijs (gemeten of gezien) | Toelichting |
|---|---|---|---|---|---|
| 1 | Rust en kalmte | **3** | NIET GESLAAGD | Bij elke wissel verdwijnt het hele gesprek en komt het terug (strip `strip-desktop-wissel.jpg`, beeld 2 tot 6). De statusregel verdwijnt ongeveer 500 ms en komt daarna terug, waardoor de hulpregels 28 px op en neer springen. Bij het sluiten blijft één afgesneden regel staan, waarna de alinea in één keer verschijnt (`pair-sluit.jpg`). Met minder beweging schuift de vaste balk nog steeds binnen (`transform` en `opacity` op `.bar` lopen). | De basis is rustig: de kop typt één keer, de cursor ademt precies 3 keer (gemeten: dekking 1 → 0,3 → 1) en er knippert niets eindeloos in beeld. Maar woorden die niet veranderen, knipperen wel bij elke wissel. |
| 2 | Vloeiende overgangen | **3** | NIET GESLAAGD | Openen vanuit het vlak verloopt goed: de tekst schuift mee, de rest komt binnen tussen 560 en 810 ms, zonder dubbel beeld. Bij **wisselen** zakt de zichtbaarheid van de tekst samen tot ongeveer 0,15 (rond 280 ms: oud 0,08 en nieuw 0,10). Bij de **paginawissel** home → onderwerp zakt die tot ongeveer 0,07 (rond 346 ms: oud 0,07 en nieuw 0). Bij **sluiten** springt de beginalinea van de bovenrand naar het krimpende vlak. | De achtergrond blijft wel staan, maar de inhoud gaat bijna naar leeg. Dat is precies wat de regel uitsluit. |
| 3 | Huisstijl en rangorde | **4** | GESLAAGD | De neutrale delen staan in Plex Sans 300. Het venster van Pam heeft een serif-logo, dat van Sam Sans 400. De accenten zijn vlak: #C9A15F voor Pam en #4F6F92 voor Sam (knoppen en stippen). Er zitten geen lichtbanen buiten de koppen en vensters (`.tone-beam` heeft geen eigen lichtbaan). Blauw komt in neutrale delen alleen als box voor (`.daybox` #E9EEF2 en de glazen box #4F6F92). | Klopt met de regels. Wat de score drukt: het venster van Pam loopt van #FFFDF7 naar #ECDCB8 en is daardoor duidelijk gelder en donkerder dan dat van Sam (#EEF3F8 en #F8FBFE). "Dicht bij wit, net als Sams daglicht" wordt dus niet gehaald. De lichtbanen op de onderwerppagina's zijn nauwelijks te zien. |
| 4 | Het gesprek ademt op mobiel | **3** | NIET GESLAAGD | Op 390×844 is de schrijfzone onderin 302 tot 330 px hoog (36 tot 39 % van het scherm) en het gesprek 446 px. Met een nagebootst toetsenbord (zichtbare hoogte 508 px) blijft er **110 px** voor het gesprek over: alleen de laatste vraag (`c-mobile-toetsenbord-sim.png`). De gesprekstekst is 15 px, de eigen invoer 16 px. Bovenaan wordt de tekst hard afgesneden, zonder zachte overgang. | De ruimte tussen de beurten is goed (32 px) en de regelhoogte ook (24 px). Maar de vaste meldingen nemen meer ruimte in dan het gesprek zelf, juist op het moment dat je schrijft. |
| 5 | Duidelijkheid en vindbaarheid | **3** | NIET GESLAAGD | Het menu in het venster verschilt per formaat: op desktop en tablet staan Onderwerpen en Wissel boven en Terugblik onder, op mobiel staan Onderwerpen en Terugblik in Menu en Wissel onder. Tekstgrootte bestaat alleen onder 600 px. Op de onderwerppagina's zit **18 px** tussen "Begin gratis over …" en de knoppen (norm 24). De sectie "Wat mensen zeggen / Geen marketing. Gewoon ervaringen." bevat geen ervaringen. "jij wist het wanneer je wilt" belooft een wisfunctie die het venster niet heeft. In de tarieven staat de knop van de eerste kaart niet op één lijn met de slotregels van de andere twee kaarten. | Elke functie heeft wel één naam (Terugblik, Onderwerpen, Wissel naar …), en de ankers landen netjes 72 px onder de vaste balk. |
| 6 | Leesbaarheid en contrast | **3** | NIET GESLAAGD | **AA niet gehaald:** het logo "Pam & Sam" (22 px, licht) in de kop van "Vast in een keuze" haalt 3,97:1 op desktop (hoogste waarde 4,6) en 4,05:1 op mobiel, waar 4,5 nodig is. Krap maar voldoende: de koptekst op de lichtbaan 3,72 (grote tekst, norm 3), witte tekst in de glazen box 5,22, menu in de kop 5,2. De randen van invoervelden halen 5,05 (formulieren) en 4,4 tot 4,7 (schrijfregel in het venster). De focusrand haalt 13:1 of meer. | Al het andere haalt AA, ook de chatvensters (laagste 5,9). Eén echte fout plus veel lichte tekst net boven de norm: geen 4. |
| 7 | Raakvlakken en bediening | **3** | NIET GESLAAGD | Alle raakvlakken zijn **44×44 px of groter**, ook de belnummers (vergroot met `::after`). Mis gaat het volgende. (a) Na het kiezen van een onderwerp in het paneel valt de focus naar `BODY`, op desktop en mobiel. (b) Bij elke Tab-ronde in het venster valt de focus één keer buiten het venster (`BODY`). (c) Open je met "Begin bij Sam" op de homepage, dan gaat de focus na sluiten naar het vlak, niet naar de knop. (d) Het menu op mobiel neemt de focus niet over: Tab na "Menu" gaat naar "Probeer gratis" en niet naar de menupunten. (e) De schrijfregel heeft geen focusrand; alleen de lijn eronder wordt donkerder. | Escape werkt goed in lagen (menu → Terugblik → paneel → venster). De focus keert terug na het paneel (naar Onderwerpen of Menu) en na Terugblik (X → Terugblik of Menu). |
| 8 | Passend bij een kwetsbare gebruiker | **4** | GESLAAGD | Het venster toont altijd 113, 0800-0113 en 112, aantikbaar. Elk onderwerp heeft een eigen hulpregel (bij relaties Veilig Thuis 0800-2000). De disclaimers halen 5,9:1 of meer. Wat schuurt: op mobiel breekt "0800-0113" over twee regels in "Belangrijk om te weten". "Gratis" en "6 vragen" staan acht keer op de homepage. In Terugblik en in het paneel Onderwerpen staan geen hulpnummers. | Geen meldingen, geen scores en geen teller. De verkooptoon zit vooral in herhaling. |
| 9 | Samenhang | **4** | GESLAAGD | Er is op geen van de drie formaten horizontaal scrollen (scrollbreedte gelijk aan schermbreedte, op desktop alleen de vaste schuifbalkruimte). Kleur, letter en vensters zijn overal gelijk. Op tablet (700 px) zie je de mobiele kop (Menu) samen met het desktopvenster: twee bedieningswijzen in één apparaat. | Het is hetzelfde product. De bediening van het venster verschilt per formaat (zie 5). |

---

## Per criterium onder de 5: wat nodig is, en de oorzaak in de code

### 1. Rust en kalmte (3 → 4)
- **Herteken bij wisselen alleen wat verandert.** `switchBtn.onclick` roept `render()` aan. Dat bouwt alle beurten opnieuw op, en `applyVoice()` zet ze in de letter van de nieuwe stem. Daarna faden ze opnieuw in via `.log.arrive`. Laat de bestaande beurten staan en laat alleen de achtergrond en de bedieningsdelen overvloeien. Of: laat de oude en de nieuwe tekst tegelijk en lineair overvloeien, zodat ze samen steeds ongeveer volledig zichtbaar zijn.
- **De statusregel springt.** In de wisselhandler staat `status.textContent = ''`, en de oefenversie zet de regel ongeveer 500 ms later terug (`handTimer`). Wis de status niet bij wisselen, of reserveer er vaste ruimte voor.
- **Minder beweging.** Voeg `.bar,.site-menu{transition:none}` en `.btn:hover,.card:hover{transform:none}` toe binnen `@media (prefers-reduced-motion: reduce)`.
- Overweeg om knoppen en kaarten bij hover niet op te tillen (`translateY(-1px/-2px)`). Klein, maar het is beweging zonder reden.

### 2. Vloeiende overgangen (3 → 4)
- **Paginawissel.** In `route()` vervaagt het spookbeeld in 320 ms, terwijl de nieuwe pagina pas na 220 ms begint (`pg.animate(... delay: 220)`). Het spookbeeld ligt al bovenop. Laat de nieuwe pagina daarom direct op volle sterkte staan en vervaag alleen het spookbeeld.
- **Wisselen.** `.log.arrive{animation:arrive .45s .2s}` begint pas als het spookbeeld (`dissolve`, 300 ms) bijna weg is. Zet de vertraging op 0, of laat het spookbeeld langer duren dan het binnenkomen.
- **Sluiten.** `inView()` meet tegen `chat.clientHeight` en niet tegen het scrollvak `#scroll`. Daardoor wordt een half afgesneden beginalinea gekozen om mee te bewegen. Daarna blijft er één regel staan (de rest vervaagt), en vervolgens springt de hele alinea in beeld. Meet tegen `scroll.getBoundingClientRect()`, of scroll eerst naar boven.
- Openen vanuit het vlak en de overgangen van paneel en Terugblik zijn in orde.

### 3. Huisstijl en rangorde (4 → 5)
- Breng het licht van Pam dichter bij wit. Laat de rand van `.bg-pam` eindigen rond #F6EEDC in plaats van #ECDCB8, zodat de vensters van Pam en Sam even licht aanvoelen.
- Maak de lichtval op de onderwerppagina's zichtbaar (nu zijn ze bijna zwart op zwart), of houd hem zwak maar zorg dat het logo erbuiten valt (zie 6).

### 4. Het gesprek ademt op mobiel (3 → 4)
- **Laat de schrijfzone krimpen zodra je schrijft.** Verberg de statusregel en de testregel als het toetsenbord open is (de klasse `.field.typing` bestaat al). Zet de hulpregel op één regel (bijvoorbeeld "Hulp nodig? 113 · 112") of verplaats hem naar het menu, met één tikbare regel die blijft staan. Doel: met een open toetsenbord minstens ongeveer 40 % gesprek in beeld.
- Zet de gesprekstekst standaard op 16 tot 17 px (`--chat-fs`), niet kleiner dan wat je zelf typt.
- Geef `#scroll` bovenaan een zachte vervaging (`mask-image`), zodat de tekst niet hard onder de kop wordt afgesneden.

### 5. Duidelijkheid en vindbaarheid (3 → 4)
- **Eén menu.** Kies op alle formaten dezelfde indeling: Menu met Onderwerpen, Terugblik en Tekstgrootte, en Wissel naar … bij de schrijfregel. Maak Tekstgrootte ook beschikbaar boven 600 px.
- `.topic-body{gap:18px}` met `.cta-row{margin-top:0}` geeft 18 px. Zet het op minstens 24 px.
- Haal de kop "Wat mensen zeggen / Geen marketing. Gewoon ervaringen." weg zolang er geen ervaringen zijn, of noem hem "Deel jouw ervaring".
- Bied de beloofde wisfunctie ("jij wist het wanneer je wilt"), bijvoorbeeld in Onderwerpen, of pas de tekst aan.
- Tarieven: zet in alle drie de kaarten onderaan hetzelfde element (knop of regel), zodat ze op één lijn staan.

### 6. Leesbaarheid en contrast (3 → 4)
- Logo in de kop van de onderwerppagina's: `.nav a{color:var(--dusk-soft)}` (dekking 0,88) staat op de lichtbaan `.beam-1` (die begint op 6 tot 30 % van links). Geef het logo daar de volle kleur `--dusk-text`, of schuif de lichtbaan van het logo weg. Doel: minstens 4,5:1, liefst 7:1.
- Voor een 5: maak de lichte tekst (300) op de glazen box en het menu in de kop zwaarder (400) of verhoog het contrast tot 7:1 of meer.

### 7. Raakvlakken en bediening (3 → 4)
- **Kiezen van een onderwerp:** `b.onclick = () => { closeDrawer(); … }` zet de focus nergens neer. Voeg `input.focus()` toe.
- **Focus in het venster vasthouden:** `inert` op de rest van de pagina is niet genoeg, want de browser zet de focus na het laatste element op het document. Laat de focus van het laatste naar het eerste element doorlopen, met een `keydown`-afhandeling voor Tab of een `<dialog>` met `showModal()`.
- **Terugkeer van de focus:** in `closeChat()` krijgt `back = room || o` voorrang voor het vlak. Laat de focus terugkeren naar de knop waarmee je opende (`origin`), ook als het venster visueel naar het vlak krimpt.
- **Menu op mobiel:** zet bij openen de focus op het eerste menupunt, sluit het menu als de focus eruit gaat, en zet de focus na Escape terug op de knop "Menu".
- **Schrijfregel:** geef `.field:focus-within` een duidelijke focusrand van minstens 2 px (bijvoorbeeld een dikkere lijn of een gloed in de stemkleur).
- Kleine ongelijkheid: Escape in Terugblik zet de focus op de schrijfregel, de X zet hem op "Terugblik". Kies één van de twee.

### 8. Passend bij een kwetsbare gebruiker (4 → 5)
- `a.tel{white-space:nowrap}`, zodat "0800-0113" nooit breekt.
- Zet onderaan Terugblik dezelfde hulpregel. Dat is het moment waarop iemand alles terugleest.
- Noem "gratis", "6 vragen" en "geen creditcard" één keer duidelijk in de kop en één keer bij Tarieven, niet acht keer.

### 9. Samenhang (4 → 5)
- Eén bedieningsmodel voor het venster op alle formaten (zie 5).
- Op tablet: laat de kop en het venster hetzelfde breekpunt gebruiken (nu 760 px voor de kop en 600 px voor het venster).

---

## Keuzes van de ontwerper: wat ze aan de score kosten

| Keuze | Raakt criterium | Kost | Waarom |
|---|---|---|---|
| Stijl per venster (ook de beurten van Pam in het venster van Sam in Sans en in Sams kleur) | 1, 2, 3 | ongeveer −0,5 op 1 en 2; 0 op 3 | Hierdoor moet bij elke wissel het hele gesprek opnieuw getekend worden in een andere letter. Dat is de oorzaak van het "knipperen" van tekst die niet verandert. Het botst ook met "Pam alleen in serif bij wat zij zegt": in het venster van Sam verliest zij haar letter. Consequent uitgevoerd, maar het kost rust. |
| Pam in Plex Serif licht roman | 6 | 0 | Contrast in het venster 6,8:1 of meer; goed leesbaar. |
| Typen in de kop en 3 keer ademen | 1 | 0 | Gemeten: precies 3 ademhalingen, daarna stil. Bij minder beweging staat de regel direct vast. Rustig uitgevoerd. |
| Logo alleen tekst, cursor als beeldmerk | 3 | 0 | Klopt. Het favicon bevat de cursor met gloed. |
| Lichtbanen in koppen en vensters | 6, 3 | ongeveer −0,5 op 6 | De lichtbaan van "Vast in een keuze" valt over het logo en zorgt voor de enige AA-fout. Op de andere onderwerppagina's is de lichtbaan bijna onzichtbaar. |
| Blauwe boxen; vergelijking in een blauwe glazen box (#4F6F92) | 3, 6 | ongeveer −0,5 op 3 | Dit is precies de kleur van Sam. De vergelijking "chatbot tegenover Pam & Sam" krijgt daardoor de kleur van één stem en verwatert de kleurcode. Witte tekst 5,22:1: voldoende, niet ruim. |
| "Meest voordelig" bij het jaarabonnement | 8 | ongeveer −0,25 | Een klassiek verkoopsignaal, samen met "2 maanden gratis". Klein, maar het telt op bij de herhaling van "gratis". |
| De testregel | 4, 8 | ongeveer −0,5 op 4 | Op mobiel kost de testregel 2 regels in de schrijfzone, ook met het toetsenbord open. Voor 8 is hij juist eerlijk (0). |
| Twee citaten ("Zachte heelmeesters…" en Covey) | 8, 5 | ongeveer −0,25 op 8 | "Stinkende wonden" is hard voor iemand die kwetsbaar binnenkomt. Covey ("product of my decisions") kan schuld oproepen bij iemand die iets is overkomen, en staat als enige tekst in het Engels. |

Zonder deze keuzes zouden 1 en 2 waarschijnlijk op 3,5 tot 4 uitkomen. De overige fouten (bijna leeg bij de paginawissel, de afgesneden regel bij sluiten, de springende statusregel) zijn uitvoeringsfouten en geen keuzes.

---

## Interactieve observaties
- **Openen vanuit het vlak** is het sterkste moment van de site. Het vlak groeit in ongeveer 540 ms uit tot het venster, de beginalinea schuift mee op zijn plek, en pas daarna komen de kop en de schrijfregel binnen. Dat voelt als binnenlopen in een kamer.
- **Snel heen en weer wisselen** (5 keer binnen 450 ms) loopt niet vast. Er blijft geen spookbeeld hangen, de eindstem klopt, en er komt één overnamezin bij. Wel verschijnt de denkcursor korter dan een seconde in de stem die je net verlaat.
- Op mobiel zijn **Menu** en **Tekstgrootte** prettig: het menu blijft open na het kiezen van een grootte, zodat je kunt vergelijken.
- In het paneel **Onderwerpen** schijnt de X van het venster rechts door de schaduw. Dat zijn twee kruisjes tegelijk in beeld.
- Het woord "onderwerp" betekent op de homepage een soort probleem (onderwerppagina's), en in het venster een eigen gesprek. Het verwart niet direct, omdat de homepage "Waar gaat het over?" gebruikt, maar het is een risico.
- De sectie "Pam & Sam is geen therapie." gebruikt het woord therapie. Het is een ontkenning, maar de werkafspraak zegt "nooit naar buiten therapie noemen". Dat moet de ontwerper beslissen.

## Overall
Een rustig en herkenbaar product, met één echt sterk idee: het vlak dat het gesprek wordt. De zwakke plekken zitten in de overgangen die volgen (wisselen, sluiten, van pagina wisselen), in de ruimte voor het gesprek op mobiel, en in de toetsenbordbediening. Allemaal zijn ze aan te wijzen in de code en te verhelpen zonder het idee aan te tasten.

---

## Beperkingen van deze test
- **Geen echte AI.** Lokaal draait de oefenversie met vaste vragen ("Dit is de oefenversie…"). Hoe lang, hoe snel en hoe zacht echte antwoorden binnenkomen, heb ik niet kunnen testen. Echte antwoorden komen in stukken binnen (`onText` → `render()` per stuk), en dat kan extra onrust geven. Niet getest.
- **Toetsenbord op mobiel nagebootst.** Ik heb het scherm verkleind tot 390×508. `visualViewport` gedraagt zich op een echte iPhone of Android anders (onder meer `offsetTop` en de veilige zones). Het getal van 110 px is een schatting.
- **Eén browser.** Alleen Chromium. Safari (iOS) en Firefox zijn niet getest; denk aan `backdrop-filter`, `inert` en `scrollbar-gutter`.
- **Contrast** heb ik gemeten per pixel op de getekende achtergrond, met de slechtste waarde onder de tekst. De korrel (`.grain`, dekking 0,10) maakt die waarde iets strenger dan de gemiddelde indruk. De fout bij het logo staat wel vast: ook de beste pixel haalt op desktop maar 4,6:1.
- **Geen schermlezer** gebruikt. De labels (`aria-label`, `aria-live`) heb ik alleen in de code gelezen.
- De beweging heb ik beoordeeld met schermopnames (ongeveer 30 tot 60 beelden per seconde) en metingen per animatiebeeld. Echte haperingen op trage telefoons zijn niet gemeten.

## Bewijs (alle bestanden in `/tmp/claude-0/-home-user/22a5d107-f852-5900-b5ed-f06b5ff6d492/scratchpad/ux-judge-4/`)
- Filmstrips: `strip-desktop-open-pam.jpg`, `strip-desktop-wissel.jpg`, `pair-wissel.jpg`, `strip-desktop-sluit.jpg`, `pair-sluit.jpg`, `strip-*-route-naar-onderwerp.jpg`, `strip-*-route-naar-home.jpg`, `strip-*-drawer.jpg`, `strip-*-terugblik.jpg`, `strip-*-snel.jpg`, `strip-desktop-faq.jpg` (losse beelden in `f-*/`)
- Schermen: `h-*-top.png`, `s-desktop-*.png`, `s-mobile-*.png`, `c-desktop-*.png`, `c-mobile-*.png`, `sheet-mobile-chat.png`, `c-mobile-toetsenbord-sim.png`, `o-*-*.png`, `o-desktop-drie.png`, `tb-*.png`, `sheet-tablet.png`, `k-*.png`, `r-*-chat.png`
- Contrastmetingen homepage: `c-home.txt`
- Scripts: `lib.js`, `cast.js`, `contrast.js`, `t1.js` tot en met `t11.js`
