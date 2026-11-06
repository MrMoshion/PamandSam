# UX-oordeel Pam & Sam, testversie (interactief)

Map met alle bewijzen: `/tmp/claude-0/-home-user/22a5d107-f852-5900-b5ed-f06b5ff6d492/scratchpad/ux-judge/`
Bestandsnamen hieronder staan in die map. Voorvoegsel `d-` is desktop (1440×900), `m-` is mobiel (390×844, aanraking), `-rm-` is "minder beweging".

## Eindoordeel: NIET GESLAAGD

Vijf van de negen criteria halen de 4 niet. De basis is sterk: het vlak dat uitgroeit tot het gesprek, de rustige letter op mobiel en de kleuren van Pam en Sam. Op vier punten gaat het mis: toegankelijkheid (de focus ontsnapt uit het chatvenster en de focusrand is bijna onzichtbaar), contrast (de blauwe vergelijkingsbox en de inleiding op de onderwerppagina's), de huisstijl na het wisselen (Pams woorden verliezen hun cursief, Sams woorden krijgen het) en een paar overgangen die toch eerst naar leeg gaan.

## Scores

| # | Criterium | Score | Bewijs | Toelichting |
|---|---|---|---|---|
| 1 | Rust en kalmte | **3** | `d-01-hero-0ms.png`, `d-scroll-05.png`, `d-r-topic-vast-100.png`, `strip-m-switch.png`, `strip-m-rm.png` | De pagina voelt rustig, maar de cursor knippert vijf keer in de kop (`.blink`, 1,1 s, 5 herhalingen). Twee tussenkoppen typen zichzelf en gaan daarna ook knipperen ("Herken je j▌"). Een paginawissel vervaagt eerst naar een lege pagina. Op mobiel licht bij elke tik een cyaan vlak op (de standaard tikmarkering van de browser). |
| 2 | Vloeiende overgangen | **3** | Goed: `d-c01-open-pam-100.png`, `d-c08-topics-150.png`. Fout: `zoom-d-close-300.png`, `d-c04-switch-sam-0.png`, `d-c05-rapid-150.png`, `d-c15-open-sam-btn-150.png`, `d-r-home-back-150.png`, `d-c12-report-150.png` | Het openen vanuit het vlak, de onderwerpen, het menu en de FAQ lopen soepel. Fouten: bij sluiten zie je dubbel beeld (de tekst staat twee keer, iets verschoven). Bij wisselen verdwijnen het bovenmenu en de schrijfregel één beeld lang. Snel wisselen geeft een leeg gesprek. Openen via de knop "Begin bij Sam" toont ongeveer 400 ms een leeg vlak. Een paginawissel gaat eerst naar leeg. |
| 3 | Huisstijl en rangorde | **3** | `d-c04-switch-sam-1400.png`, `d-c05-rapid-1500.png`, `m-c07-fs19.png`, `d-c12-report-700.png` | Zuiver: de neutrale huisstijl (Plex Sans Light met de witte cursor), Menu en Onderwerpen in roman (gemeten: Plex Sans, normal), de vlakke stippen #C9A15F en #4F6F92, blauw alleen als box, en de lichtbaan alleen in de kop en de chat. Fout: de stijl hangt aan het venster in plaats van aan wie spreekt. In Sams venster staan Pams eerdere beurten in blauw roman. In Pams venster staat "Ik ben Sam, ik neem het over" in Pams cursief. Dat geldt ook voor het verslag. |
| 4 | Het gesprek ademt op mobiel | **4** | `m-c03-send2-1500.png`, `m-c07-fs19.png`, meting: chattekst 15 px, schrijfregel 16 px, 24 px marge opzij | Ruim en rustig, met een duidelijke schrijfregel. De tekstgrootte 15, 17 en 19 werkt en blijft bewaard. Minpunt: de vaste regel "Dit is de oefenversie…" beslaat twee regels onder de knoppen. Samen is het onderste deel 210 px, een kwart van het scherm. |
| 5 | Duidelijkheid en vindbaarheid | **3** | `m-c00-kies.png` naast `m-c01-open-pam-200.png`, `d-c12-report-150.png`, `d-c10-topics-list.png`, `m-03-hero-typed.png` | Het vlak op mobiel toont "Vat het samen" linksonder. Het geopende venster toont daar "Wissel naar Sam": het voorproefje belooft iets anders dan er komt. Het verslag opent onderaan, waardoor de titel buiten beeld valt. Het paneel Onderwerpen heeft geen sluitknop. Op mobiel staat in het menu van de homepage alleen "Probeer gratis", dus Aanpak en Tarieven zijn er niet te vinden. Op desktop heet dezelfde functie zowel "Verslag" als "Vat het samen". De ruimte tussen tekst en knoppen is wel in orde (32 px op mobiel). |
| 6 | Leesbaarheid en contrast | **2** | Gemeten op de getekende achtergrond (`d_contrast.js`, `e_contrast2.js`) | Zakt onder AA: in de blauwe vergelijkingsbox de lopende tekst **2,99:1**, het bovenschrift **2,79:1** en "Een gratis chatbot" **3,94:1** (16–17 px). De inleiding op de onderwerppagina's zakt per regel van 3,6 naar **2,1:1** op desktop en van 4,3 naar **1,8:1** op mobiel. Goed: de disclaimer in de kop (6,45:1), de grijze tekst (#625649: 6,5–7,1:1) en de knop van Sam (wit op #4F6F92: 5,2:1, berekend). |
| 7 | Raakvlakken en bediening | **2** | `f_kbd.js`-uitvoer, `d-k-03-focus-room.png`, `d-k-04-focus-chat-3.png` | Escape werkt goed in lagen (hulp, menu, verslag, onderwerpen, venster) en de focus keert na sluiten terug naar het vlak. Fout: het venster heet modaal (`aria-modal`), maar na "Verstuur" springt Tab naar de pagina erachter (logo, Aanpak, Tarieven…). De focusrand #F0C98E haalt op de lichte achtergrond ongeveer 1,4:1 en in Pams venster #C9A15F ongeveer 2:1 (berekend, nodig is 3:1). Een onderwerp in de lijst en de A-knoppen voor tekstgrootte hebben geen focusrand door `all:unset`. Op mobiel zijn de voetlinks 20 px hoog en "Probeer gratis" 42 px. |
| 8 | Passend bij een kwetsbare gebruiker | **3** | `d-03-hero-typed.png`, `d-scroll-08.png`, `d-r-topic-spanning-in-je-relatie-full.png`, `d-scroll-07.png` | Goed: de disclaimer is leesbaar. Hulplijnen (112, 113, 0800-0113, Veilig Thuis) staan op de homepage en de onderwerppagina's. Er zijn geen scores en geen druk in de chat. Fout: in het gesprek zelf staat geen hulplijn. De nummers zijn niet aantikbaar. "Meest gekozen" bij het jaarabonnement is in een testfase niet waar te maken: het werkt als verzonnen sociaal bewijs. De belofte "niets opgeslagen" botst met het opslaan van onderwerpen in de browser, ook voor gratis gebruik, en op een gedeeld apparaat is dat zichtbaar. Je ziet ook nergens hoeveel van de zes gratis vragen er nog over zijn. |
| 9 | Consistentie desktop en mobiel | **4** | Meting: geen horizontaal scrollen (desktop 1425/1440, mobiel 390/390, ook de onderwerppagina's en de chat) | Het voelt als één product. Er zijn kleine breuken: de namen Verslag en "Vat het samen", en het voorproefje op mobiel dat niet klopt met het venster (zie 5). |

## Verbeterpunten per criterium onder de 4

### 1. Rust en kalmte (3)
- **Kop en `[data-type]`-koppen.** Laat de cursor niet knipperen: zet hem stil of laat hem één keer langzaam ademen. Laat de tussenkoppen "Herken je jezelf hierin?" en "Klaar om te beginnen?" niet meer typen. Bewaar het typen voor één regel, "Jij komt op het antwoord.", en zet die regel meteen in beeld, zodat er niet 2,5 s een lege regel staat.
- **`route()`.** Vervaag een paginawissel niet naar `opacity:0` van de hele pagina. Laat de oude en de nieuwe pagina in elkaar overlopen, of houd de kop staan.
- **Mobiel.** Zet `-webkit-tap-highlight-color: transparent` op knoppen en links (`strip-m-switch.png`, eerste beeld).

### 2. Vloeiende overgangen (3)
- **`closeChat`.** De tekst die mee krimpt en de tekst in het vlak overlappen in de laatste 200 ms (`zoom-d-close-300.png`). Laat de tekst in het vlak pas verschijnen als de chat helemaal weg is, of laat de chattekst eerder uitvagen.
- **Wisselen, `snapshot(false)`.** Het bovenmenu en de schrijfregel worden in de momentopname verborgen, dus ze verdwijnen even (`d-c04-switch-sam-0.png`). Houd ze in beeld (`keepChrome = true`) en laat alleen het gesprek overvloeien.
- **Snel wisselen.** De klasse `arrive` start bij elke klik opnieuw en zet het gesprek op leeg (`d-c05-rapid-150.png`). Start de animatie niet opnieuw zolang er al een loopt, of vertraag het wisselen kort.
- **Openen via een knop** ("Begin bij Sam", "Met Pam"). Het vlak groeit leeg op (`d-c15-open-sam-btn-150.png`). Laat de introductietekst meteen zachtjes mee verschijnen.
- **Verslag.** `$('backBtn').focus()` schuift het verslag naar onderen. Gebruik `focus({preventScroll:true})` en zet de focus op de titel.

### 3. Huisstijl en rangorde (3)
- **CSS `.chat.pam .msg.q` en `.msg.q{color:var(--voice)}`.** Geef elke beurt een klasse naar wie spreekt (`.msg.q.v-pam` of `.v-sam`) en kies letter en kleur daarop, niet op het venster. In `render()` en `showReport()` is `voiceOf(m)` al beschikbaar.

### 5. Duidelijkheid en vindbaarheid (3)
- **Vlak op mobiel.** Laat het voorproefje tonen wat er echt komt: "Wissel naar Sam" en Verstuur. Of zet "Vat het samen" in het venster terug waar het vlak het belooft.
- **Verslag.** Open het bovenaan (zie 2). Geef het verslag ook het bovenmenu met de X, zodat je ook sluiten kunt vinden.
- **Onderwerpen.** Zet in het paneel een zichtbare sluitknop ("Terug naar het gesprek").
- **Homepage op mobiel.** Voeg een eenvoudig menu toe, of zet Aanpak en Tarieven als tekstlinks onder de kop.
- **Desktop.** Kies één naam voor één functie: "Verslag" of "Vat het samen", niet allebei.
- **Kleine punten.** In de FAQ staat "Klik rechtsboven op Mijn account", maar die knop bestaat niet. "Privacy · Voorwaarden · Contact" in de voet zijn geen links. Een onderwerptitel eindigt op ".…" ("wisselen.…").

### 6. Leesbaarheid en contrast (2)
- **`.dark-sec .glass`.** Maak de box dekkend en donkerder, bijvoorbeeld #3F5B79 (berekend: wit haalt dan ongeveer 7:1, de tekst met 82% wit ongeveer 5:1). Zet de tekst in `.compare .plain` en `.dark-sec .eyebrow` op minstens 90% wit. Of houd #4F6F92 en gebruik puur wit (5,2:1).
- **`.topic-hero .lead`.** De verlichting van de kop loopt onder de tekst door. Laat de kop langer donker blijven, of zet de inleiding onder de kop op de lichte achtergrond in `--ink`.

### 7. Raakvlakken en bediening (2)
- **`#chat`.** Bouw een echte focusval: Tab blijft in het venster, of maak de pagina erachter `inert` zolang de chat open is. Voor het verslag en het paneel geldt hetzelfde.
- **`:focus-visible`.** Gebruik op lichte vlakken een donkere rand, bijvoorbeeld 2 px `--ink` met de gloed er als extra omheen. In Pams venster haalt #C9A15F de 3:1 niet. Gebruik daar `--pam-ink` of #8A6A3A.
- **`.topic-item` en `.sizes button`.** Zet de focusrand terug na `all:unset`.
- **Mobiel.** Maak de voetlinks en findahelpline.com minstens 44 px hoog (met padding), en "Probeer gratis" 44 px in plaats van 42 px.

### 8. Passend bij een kwetsbare gebruiker (3)
- **Chat.** Zet een vaste, rustige link "Hulp nodig?" in het menu en onder in het venster, met 113 en 112 als aantikbare links (`tel:`).
- **Tarieven.** Haal "Meest gekozen" weg tot het echt gemeten is.
- **Privacy.** Maak de belofte en het gedrag gelijk. Leg in de chat uit dat onderwerpen alleen in deze browser blijven, met een knop "Wis alles". Of sla bij gratis gebruik echt niets op.
- **Gratis vragen.** Laat rustig zien hoeveel er nog over zijn, zonder aftelklok. Zo komt het einde niet als verrassing.
- **Toon** (smaakoordeel, ter overweging). "Zachte heelmeesters maken stinkende wonden" en het Engelse citaat van Covey ("I am a product of my decisions") kunnen bij iemand in nood als verwijt landen.

## De vijf belangrijkste verbeteringen (grootste winst eerst)

1. **Focusval en zichtbare focusrand** in chat, verslag en onderwerpen. Zet de pagina achter de chat op `inert` en geef de focusrand overal minstens 3:1 (criterium 7).
2. **Contrast** van de blauwe vergelijkingsbox (2,8–3,0:1) en de inleiding op de onderwerppagina's (tot 1,8:1) op AA brengen (criterium 6).
3. **Stijl per spreker, niet per venster.** Pams beurten blijven altijd Plex Serif cursief en Sams beurten altijd Plex Sans 400, ook na wisselen en in het verslag (criterium 3).
4. **Overgangen die nooit naar leeg gaan.** Paginawissel, snel wisselen en openen via de knop. Houd het bovenmenu en de schrijfregel staan bij wisselen, haal het dubbele beeld bij sluiten weg en laat het verslag bovenaan openen (criteria 1, 2 en 5).
5. **Hulp en eerlijkheid in de chat zelf.** Aantikbare hulplijnen in het venster, "Meest gekozen" weg, de privacybelofte gelijk aan het gedrag, en geen knipperende of typende koppen buiten de ene regel in de kop (criteria 8 en 1).

## Beperkingen van deze test

- De AI draait lokaal niet. Het gesprek viel terug op de oefenversie met vaste vragen ("Dit is de oefenversie…"). Ik heb geen echte antwoorden gezien en dus ook niet hoe tekst binnenstroomt, hoe lang het duurt of hoe lang de antwoorden zijn. In de oefenversie delen Pam en Sam één teller: na wisselen sloeg Sam zijn eerste vragen over ("Wat houdt je tegen?"). Met "minder beweging" voegde snel wisselen extra overnamezinnen toe.
- Er is geen echte iPhone of Android gebruikt, alleen Chromium-emulatie (390×844, aanraking, schaal 2). Het cyaan tikvlak is de markering van Chromium. Safari op iOS toont een grijs vlak. Het schermtoetsenbord en de aanpassing aan de zichtbare ruimte (`fitVV`) zijn niet echt getest.
- De smalle lichte strook rechts op desktop (x 1425–1440, onder meer `d-c01-open-pam-450.png`) komt door `scrollbar-gutter: stable` in Chromium zonder zwevende schuifbalk. Op macOS met zwevende schuifbalken zie je hem waarschijnlijk niet, op Windows wel. Niet op echte systemen gecontroleerd.
- Schermafbeeldingen kosten zelf ongeveer 100–150 ms. De tijden in de bestandsnamen zijn dus ondergrenzen, en tussenbeelden van overgangen kunnen iets later vallen dan het getal zegt.
- Contrast is gemeten op de getekende achtergrond, met de lichtste of donkerste pixel als slechtste geval. Bij chips en knoppen met afgeronde hoeken telt de gemiddelde waarde, want de hoekpixels vallen buiten het vlak. De focusranden en het voorstel voor #3F5B79 zijn berekend, niet gemeten.
- De lettertypen kwamen via de proxy van Google Fonts en zijn geladen (gecontroleerd met `document.fonts`).
- Er is geen schermlezer gebruikt. Er is ook niet getest met echte gebruikers in een kwetsbare gemoedstoestand: dat blijft nodig.
- De Playwright-scripts (`lib.js`, `a_home.js`, `b_chat.js`, `c_rest.js`, `d_contrast.js`, `e_contrast2.js`, `f_kbd.js`, `g_rm.js`, `h_topiccards.js`) staan nog in de map, omdat `rm` niet gebruikt mocht worden.
