# UX-oordeel Pam & Sam, testversie (ronde 3, interactief)

Datum: 6 november 2026. Beoordeeld: `site/pam-en-sam.html`, versie van 09:21 (vastgelegd als `ux-judge-3/snapshot-0921.html`). Ik heb op een schone lei gewerkt en geen scores uit eerdere rondes overgenomen.

## Eindoordeel: NIET GESLAAGD

Vijf van de negen criteria halen de 4 niet. Het kernmoment werkt wel goed: het vlak groeit uit tot het gesprek, het gesprek ademt en het venster krimpt terug naar de juiste stem. De zwakke plekken zitten in de overgangen eromheen. Bij wisselen tussen pagina's, ankers en onderwerpen is het scherm even leeg, staat er dubbel beeld of verschijnt er kort een verkeerde interface. Daarnaast verdwijnt de tekst van de knop in de vaste balk zodra je eroverheen beweegt of erop tikt.

Uitleg van een paar vakbegrippen in dit rapport:
- **Spookbeeld**: een kopie van het oude scherm die over het nieuwe heen vervaagt.
- **Focus**: het element waar je toetsenbord op dat moment op staat.
- **Raakvlak**: het deel van het scherm dat op een tik of klik reageert.
- **Contrastverhouding**: hoe sterk tekst afsteekt tegen de achtergrond. WCAG AA vraagt 4,5:1 voor gewone tekst, 3:1 voor grote tekst en voor randen van bedieningselementen.

## Scores

| # | Criterium | Score | Bewijs (kort) | Toelichting |
|---|---|---|---|---|
| 1 | Rust en kalmte | **2/5** | `strip-m-anker-tarieven.png`, `strip-d-terug-home.png`, `strip-d-kaart-naar-onderwerp.png`, `film/d-wissel-snel-0777ms.jpg` | Er knippert niets en er draait geen eindeloze animatie (gemeten: 0). De cursor ademt 3 keer en blijft dan staan. Maar het scherm gaat wel eerst naar leeg: bij een ankersprong via het menu (ongeveer 0,5 s een lege crèmekleurige pagina), bij terug naar home via het logo (leeg, daarna scrolt de pagina in één ruk van de footer omhoog) en bij overstappen tussen onderwerppagina's (ongeveer 250 ms leeg). |
| 2 | Vloeiende overgangen | **2/5** | `strip-onderwerp-ghost.png`, `film/d-wissel-snel-0777ms.jpg`, `strip-terugblik-dip.png`, sampler-logs in `chat-d.log` | Openen vanuit het vlak en sluiten naar het vlak zijn goed: geen dubbel beeld, de tekst schuift mee. Fout gaat het hier: (a) bij snel wisselen staan Pams schreefletter en Sams schreefloze letter verschoven over elkaar; (b) bij een nieuw of ander onderwerp toont het spookbeeld 100 tot 300 ms knoppen die niet bestaan ("Menu" en "Terugblik" bovenin, een grote pil "Wissel naar Pam" in het midden, op mobiel een dubbele "Verstuur"); (c) bij het sluiten van de Terugblik staan oud en nieuw verschoven over elkaar; (d) bij het openen van de Terugblik en bij een gewone wissel zakt de tekst eerst bijna weg (combinatie onder 30 procent dekking, ongeveer 100 ms) voordat het nieuwe binnenkomt. Dat is na elkaar overvloeien, geen echte kruisovergang. |
| 3 | Huisstijl en rangorde | **3/5** | `d-50-spanning-in-je-relatie.png`, `d-30-bar-hover.png`, `d-14-sam-na-wissel.png` | Goed: de neutrale stijl is Plex Sans 300 (121 tekstelementen), knoppen en labels staan in 400, Pam is vlak #C9A15F en Sam vlak #4F6F92 zonder verloop, en het blauw komt alleen als vlak voor ("Waarom niet gewoon een gratis chatbot?"). Fout: de lichtbaan staat ook in de kop van alle drie de onderwerppagina's (`.beam-1/2/3`), en de regel is "alleen homepagekop en chatvensters". De primaire knop in de vaste balk wordt bij hover inkt-op-inkt (rgb 46,40,34 op 46,40,34), dus een lege donkere pil. De versie van 09:21 heeft ook geen cursor meer bij het logo ("Pam & Sam" zonder lichtje), terwijl besluit 18 een wit oplichtende cursor noemt. Als dat bewust is, moet het besluit worden bijgewerkt. |
| 4 | Het gesprek ademt op mobiel | **4/5** | `m-71-rm-chat.png`, `m-51-topic-chat-pam.png`, `m-17-tekst-19.png` | Ruim wit, 15/17/19 px werkt en blijft bewaard, het menu blijft open bij het kiezen van een tekstgrootte, en tussen tekst en schrijfregel zit 32 px. Minpunten: van schrijfregel naar knoppen is maar 18 px, en bij een lang gesprek wordt de eerste regel hard afgesneden onder de kop (`d-15-na-snel-wisselen.png`), zonder zachte overgang. |
| 5 | Duidelijkheid en vindbaarheid | **3/5** | HTML-tekst, `d-03-scroll-*`, `d-15-na-snel-wisselen.png` | Eén naam per functie wordt niet gehaald. "Pam & Sam" is zowel het logo (naar boven) als een menu-item (naar #kies), en "Probeer gratis" gaat naar dezelfde plek als dat menu-item. Het menu van de onderwerppagina's mist "Pam & Sam". De footer zegt "Je onderwerpen blijven alleen in deze browser", het gesprek zegt "je gesprekken blijven…". De teksten kloppen niet met elkaar: de FAQ zegt "voor gratis gebruikers wordt niets opgeslagen, sluit je de browser dan is het weg", de vergelijking zegt "je gesprek blijft in je eigen browser", en de testversie bewaart het wel. "Privacy" en "Voorwaarden" in de footer zien eruit als links maar zijn platte tekst. "6 vragen" en "Zes vragen" staan door elkaar, net als "€60,-" en "€5,99". Na snel wisselen staat "Ik ben Sam, ik neem het over" twee keer achter elkaar. In de chat zit 16 px (desktop) of 18 px (mobiel) tussen schrijfregel en knoppen, dus minder dan 24 px. De knoppen zelf zijn netjes uitgelijnd: de prijsknoppen staan op één lijn (y=5317), de deurknoppen ook. |
| 6 | Leesbaarheid en contrast | **3/5** | `contrast/` + `contrast.py` (1138 teksten gemeten op de getekende achtergrond), `d-30-bar-hover.png` | Alle gemeten teksten in rust halen AA. De laagste waarden: "Jij komt op het antwoord." 3,55:1 (grote tekst, AA gehaald), de kop 4,55:1, wit op Sams blauw 5,22:1. Maar: de knop in de vaste balk zakt bij hover naar 1:1, dus de tekst is weg. Dat is een harde AA-fout in een toestand (en blijft op touch hangen na een tik, `m-24-na-sluiten.png`). De rand van de formuliervelden in de contactbox is 2,92:1 tegen de box en 3,0:1 tegen het veld, dus net onder of precies op de grens. De schrijfregel in de chat haalt 4,4 tot 4,7:1 en de focusrand 13,3:1 (op donker 5,2:1). Dat is goed. |
| 7 | Raakvlakken en bediening | **3/5** | `targets-*.log`, `rest-*.log` | De belangrijkste knoppen zijn 44 px of groter (sluiten, menu, tekstgrootte 44×44, pillen 46 tot 50 px). De telefoonnummers hebben een onzichtbaar raakvlak van 44 px. Te klein: de schrijfregel zelf (24 px hoog op mobiel, 29 px op desktop; het meest gebruikte element), het logo-link (35 px) en de inline link findahelpline.com (22 px). Focus: openen zet de focus in de schrijfregel; sluiten met X of Escape geeft de focus terug aan het vlak van de stem waar je eindigt; bij het paneel Onderwerpen gaat de focus terug naar Onderwerpen of Menu. Dat is goed. Twee afwijkingen: Tab ontsnapt één stap per rondje naar `BODY` buiten het venster (de rest van de pagina is wel onbereikbaar, want die staat op inert), en na het sluiten van de Terugblik gaat de focus naar de schrijfregel in plaats van naar de knop Terugblik. De focusrand is overal goed zichtbaar (`d-74-focus-kop.png`). |
| 8 | Passend bij een kwetsbare gebruiker | **3/5** | HTML-tekst, `d-50-*`, `m-51-topic-chat-pam.png` | Goed: geen meldingen, scores of tellers. In elk gesprek staan 113, 0800-0113 en 112 als aantikbare links, de relatiepagina noemt Veilig Thuis, en "geen therapie" is helder uitgelegd. Zwak: de hulpregel in de chat is 13 px, wat voor veiligheidsinformatie klein is. De onderwerppagina's "Vast in een keuze" en "Werk wordt te veel" hebben geen hulpnummers, dus niet "overal". "Probeer gratis" staat 7 keer op de homepage, met daarbij "Klaar om te beginnen?", "Zachte heelmeesters maken stinkende wonden" en een Engelse Covey-quote ("I am a product of my decisions"). Dat legt de verantwoordelijkheid nadrukkelijk bij iemand die op dat moment misschien vastzit. |
| 9 | Samenhang | **4/5** | `t-80…83`, `overflow`-metingen in `home-*.log` | Nergens horizontaal scrollen (desktop 1425/1440, tablet 685/700, mobiel 390/390). Desktop, tablet en mobiel voelen als hetzelfde product. Minpunten: het menu van de onderwerppagina's verschilt van dat van de homepage, en de wisselknop staat op desktop bovenin en op mobiel onder de schrijfregel. Dat laatste is verdedigbaar, maar het is wel een tweede plek om te onthouden. |

## Wat er per criterium nodig is voor de volgende stap

**1. Rust (2 → 4/5)**
- Bij een ankersprong niet 3000 tot 9000 px vloeiend scrollen door secties die nog moeten binnenkomen. Spring direct en laat alleen de doelsectie zacht binnenkomen, of laat de oude pagina eerst vervagen boven de nieuwe positie.
- Bij terug naar home via het logo eerst naar boven gaan, dan pas de pagina tonen. Geen scrollrit vanaf de footer.
- De lege fase bij overstappen tussen onderwerppagina's oplossen. De oorzaak staat onder 2.
- Voor een 5: geen enkel frame zonder inhoud. Controleer elke overgang met een filmstrip.

**2. Overgangen (2 → 4/5)**
- *Bug 1, oorzaak gevonden:* `route()` maakt een spookbeeld van de onderwerppagina met de klasse `topic`. Direct daarna zet `swap()` `hidden` op álle `.topic` zonder het juiste id, dus ook op het spookbeeld. Geef het spookbeeld een andere klasse of sluit het uit in `swap()`.
- *Bug 2, oorzaak gevonden:* `snapshot()` haalt de id's weg in de kopie. Daardoor gelden regels als `#menuBtn{display:none}`, `#reportBtn{display:none}` en `#switchBtn2{display:none}` niet meer, en verschijnen die knoppen in het spookbeeld. De kopie neemt ook het open paneel Onderwerpen mee. Verberg in de kopie de elementen die nu verborgen zijn, of maak de kopie alleen van het logboek (`keepChrome=false`, zoals bij wisselen).
- Snel wisselen: laat een nieuwe wissel pas toe als de vorige klaar is (de `anim`-vlag ook bij wisselen gebruiken), of breek het lopende spookbeeld af in plaats van er een nieuw bovenop te stapelen.
- Terugblik: laat het gesprek en de terugblik echt kruiselings overvloeien. Nu wacht het nieuwe 180 tot 260 ms terwijl het oude al bijna weg is. Gebruik bij het sluiten geen verschuiving (`translateY 12px`) tijdens de overlap, of verberg het oude eerst volledig, maar nooit beide tegelijk half zichtbaar en verschoven.
- Wissel van stem: laat het nieuwe logboek al binnenkomen terwijl het spookbeeld nog op ongeveer 50 procent staat (vertraging `.2s` naar ongeveer `.08s`), zodat de dekking samen niet onder ongeveer 70 procent zakt.

**3. Huisstijl (3 → 4/5)**
- Haal `.beam` uit de koppen van de onderwerppagina's (laat alleen `.lamp` staan).
- Herstel de hover van `.bar .nav .btn`, bijvoorbeeld met `.bar .nav a.btn:hover{color:var(--light)}`. Controleer daarna alle hovertoestanden op contrast.
- Leg vast of het logo een cursor heeft. Dat verschilt nu tussen het besluit (18) en de site van 09:21.

**4. Mobiel gesprek (4 → 5/5)**
- Minimaal 24 px tussen schrijfregel en knoppen.
- Laat tekst zacht wegvloeien onder de kop (een verloop van 24 px aan de bovenrand van `.scroll`) in plaats van hem hard af te snijden.

**5. Duidelijkheid (3 → 4/5)**
- Kies één naam voor de knop naar #kies ("Probeer gratis" of "Pam & Sam") en maak de menu's van homepage en onderwerppagina's gelijk.
- Kies "gesprekken" of "onderwerpen" en gebruik dat woord overal (de footer, de testversieregel, het paneel).
- Zorg dat FAQ, vergelijking en testversie hetzelfde zeggen over opslaan.
- Maak van Privacy en Voorwaarden links, of haal ze weg.
- Schrijf "6" of "zes" op één manier, en zet de prijzen in één notatie (€ 60 en € 5,99).
- Voorkom een dubbele overdrachtszin na snel wisselen.

**6. Contrast (3 → 4/5)**
- Los de hoverfout van de balkknop op (1:1). Daarmee is 4 haalbaar.
- Voor een 5: de formulierranden in `.daybox` naar ten minste 3,5:1 (bijvoorbeeld `rgba(46,40,34,.6)`), en de getypte kopregel naar ten minste 4,5:1.

**7. Bediening (3 → 4/5)**
- Maak de hele schrijfregel een raakvlak van ten minste 44 px (bijvoorbeeld `min-height:44px` op de textarea, of een klik op `.field` die de textarea focust).
- Maak het logo-link ten minste 44 px hoog.
- Houd Tab binnen het venster: vanaf het laatste element naar het eerste.
- Geef na het sluiten van de Terugblik de focus terug aan de knop Terugblik (op desktop) of aan Menu (op mobiel).

**8. Kwetsbare gebruiker (3 → 4/5)**
- Hulpnummers als aantikbare links op álle onderwerppagina's en in de footer.
- De hulpregel in de chat op ten minste 15 px (de grootte van de chattekst).
- Minder herhaling van "Probeer gratis".
- Heroverweeg de Covey-quote (Engels, en een schuldtoon) en de "stinkende wonden"-zin. Dat valt onder toon, dus eerder een vraag voor merk dan voor UX.

**9. Samenhang (4 → 5/5)**
- Eén gedeeld menu voor homepage en onderwerppagina's.
- Leg vast waarom de wisselknop per formaat op een andere plek staat, of trek dat gelijk.

## Keuzes van de ontwerper en hun effect op de score

| Keuze | Oordeel | Effect op de score |
|---|---|---|
| **Stijl per venster** (na een wissel staat ook wat Pam zei in Sams letter en kleur, met naam en stip erboven; de terugblik volgt dat) | Het is consequent en het naamlabel met stip houdt de spreker herkenbaar. Maar wat Pam zei, verandert met terugwerkende kracht van stem. Dat wringt met "twee stemmen", en het maakt het dubbele beeld bij snel wisselen extra zichtbaar (schreef en schreefloos over elkaar). | Crit. 3: −0,5. Crit. 2: −0,25 (versterkt de bestaande fout, veroorzaakt hem niet). Telt niet mee in de verlaging naar onder de drempel. |
| **Pam in roman** (Plex Serif licht, alleen haar woorden en logo) | Correct toegepast: gemeten alleen op `.msg.q`, het Pam-logo en het mini-vlak. Rustig en leesbaar. | Geen. |
| **Typen in de kop** (alleen de kopregel, dan 3 keer ademen) | Gemeten: precies 3 ademcycli van 2,6 s, daarna dekking 1,00 en stilstand. Geen andere getypte zinnen actief. | Geen. |
| **"Meest voordelig" bij het jaarabonnement** | Een lichte verkoopduw in een product dat belooft niet te jagen. Bescheiden uitgevoerd (alleen een label en een rand). | Crit. 8: −0,25. |
| **Testversie-regel** | Prima als tijdelijke regel. Hij botst wel inhoudelijk met de FAQ ("gratis = niets opgeslagen") en gebruikt een ander woord dan de footer. | Crit. 5: −0,25 (het woordverschil en de tegenspraak, niet het bestaan van de regel). |

Geen van deze keuzes is de reden dat een criterium onder de 4 valt. Die oorzaken zijn bugs en tekstinconsistenties.

## Beperkingen van deze test

- **Het bestand veranderde tijdens de test.** Ik begon op de versie van 09:13 en om 09:21 werd het overschreven. Daarin is onder meer de cursor bij de logo's verdwenen. Ik heb alle hoofdroutes, het gesprek en de onderwerppagina's opnieuw gedraaid op de vastgelegde versie van 09:21 (`snapshot-0921.html`). De beelden van de oude versie staan apart in `film-v0913/`. De contrastmeting (`contrast/`) is gedaan op 09:13. Kleuren en stijlregels zijn daarna niet veranderd (zelfde CSS-regels voor kleur), maar dat heb ik niet volledig opnieuw gemeten.
- **De AI draait lokaal niet.** Het gesprek gebruikt de oefenversie met vaste vragen ("Dit is de oefenversie…"). Streaming, de echte lengte van antwoorden en de reactietijd heb ik niet gezien.
- Headless Chromium met nagebootste touch. Geen echte iPhone of Android, geen Safari, geen virtueel toetsenbord. Daardoor zijn het aanpassen aan het toetsenbord (`visualViewport`) en de knop "toetsenbord sluiten" niet getest.
- Filmstrips zijn opeenvolgende schermafbeeldingen. Elk beeld kost 40 tot 150 ms (mobiel trager), dus tussenliggende frames kunnen ontbreken. Ik heb dat aangevuld met een meting per frame van de dekking van de lagen (logs in `chat-*.log` en `rest-*.log`).
- De contrastmeting werkt op de getekende achtergrond met onzichtbaar gemaakte tekst. Tekst die deels onder de vaste balk of over de rand van het beeld viel, is weggelaten. Teksten in de onderwerpkoppen zijn alleen visueel beoordeeld.
- Geen test met schermlezer. `aria-live` en de dialooglabels heb ik alleen in de code gezien.
- Markeren en doorstrepen staan verborgen (`hidden`) en zijn niet beoordeeld.

## Belangrijkste bewijsbestanden
Alle bestanden staan in `/tmp/claude-0/-home-user/22a5d107-f852-5900-b5ed-f06b5ff6d492/scratchpad/ux-judge-3/`:
- Overgangen: `strip-onderwerp-ghost.png`, `strip-m-wissel-onderwerp.png`, `strip-d-kaart-naar-onderwerp.png`, `strip-d-terug-home.png`, `strip-m-anker-tarieven.png`, `strip-terugblik-dip.png`, `film/d-wissel-snel-0777ms.jpg`, `strip-d-open-pam-vlak.png`, `strip-m-sluiten.png`
- Hoverfout: `d-30-bar-hover.png`, `m-24-na-sluiten.png`
- Schermen: `d-02-kop-rust.png`, `d-03-scroll-*.png`, `m-03-scroll-*.png`, `t-03-scroll-*.png`, `d-50-*.png`, `m-71-rm-chat.png`, `t-81-chat.png`, `d-22-terugblik.png`, `d-18-onderwerpen.png`, `d-74-focus-kop.png`
- Metingen: `contrast/`, `contrast.py`, `chat-d.log`, `chat-m.log`, `rest-*.log`, `targets-*.log`, `home-*.log`
