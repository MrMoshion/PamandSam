# 49 · Couture als klikbare site (zand)

**Gekozen (ontwerper, 7 november 2026):** neutraal B "Zand" voor de landingspagina. De kamers van Pam en Sam komen uit optie 2 van 48. Live te bekijken als artifact: https://claude.ai/artifact/X18b7gD4h9jELpjFuiY2CK

## Wat het is
Dezelfde site als de kamer (v31): dezelfde pagina's, chat, onderwerpen, terugblik en help. Alle geteste werking is behouden. Alleen de huid is nieuw: `site/couture/couture.css`, gebouwd met `site/couture/bouw.py`.

- **Plafond en muur:** elke kop is een licht plafond boven een warmere muur, vlak zonder verloop, gloed of korrel. De kamer zit in de verhouding, niet in effecten.
- **Letters:** Bodoni Moda voor koppen en Pams stem, Jost voor tekst en Sams stem.
- **Knoppen:** klein gezet als een label, in hoofdletters met ruime spatiëring en een hoek van 2px.

## Kleuren en accenten
| Rol | Muur | Plafond | Tekst | Accent |
|---|---|---|---|---|
| Neutraal (Zand) | #E5D6B3 | #F3EBD8 | #2B2214 | #7A5C2A (alleen onderstreping) |
| Pam | #EADDD9 | #F7F1EF | #2C1A15 | klei #8C5A44 |
| Sam | #DCE0E4 | #F0F2F4 | #15202B | leisteen #44596E |

De accenten van Pam en Sam zijn gedempter dan het oude geel en blauw, zodat ze bij zand passen. Ze verschijnen alleen als spoor: de knop per stem, de stip voor de naam en de cursor in de chat. Contrast (WCAG AA, de toegankelijkheidsnorm):
- witte knoptekst op klei: 5,7:1;
- witte knoptekst op leisteen: 7,2:1;
- zachte tekst op zand: 5,8:1;
- zachte tekst in Pams kamer: 6,4:1;
- zachte tekst in Sams kamer: 6,0:1.

## Overgangen (uit de voorbeeldsites, ingetogen)
- **Binnenkomen in de kop:** regel voor regel één keer uit een lichte waas, naar het voorbeeld van "Blur In Text" op 21st.dev. Alleen de getypte regel wordt nog getypt. Daarna beweegt er niets meer.
- **Van kaart naar kamer:** de bestaande overvloeiing van de kamer (de deur groeit uit tot de kamer, het oude vervaagt boven het nieuwe) blijft, met de hoek teruggebracht naar 4px.
- **Bij weinig-beweging-instelling:** geen animaties.

Bewust niet overgenomen: scroll-gekoppelde effecten, magnetische knoppen en lichtbanen. Die zijn opsmuk en botsen met "rustig, niets knippert".

## Getest
- Openen en sluiten frame voor frame: 0 fouten.
- Pixelvergelijking aan het eind van het sluiten: komt rustig tot 0.
- Intro typen, help, wisselen en sluiten werken zonder fouten.
- Toetsenbord, focus en Escape werken.
- Geen horizontaal scrollen op 375 tot 1440.
- Kop op 5 maten: de disclaimer overlapt nergens meer.
- Hersteld in deze ronde:
  - de disclaimer op mobiel;
  - de knop in het menu die afbrak;
  - "Wissel naar …" stond in hoofdletters;
  - de rand om de secties;
  - ronde velden.

**Niet getest:** echte antwoorden van Pam en Sam in de artifact (die lopen via Claude, alleen in de browser van de gebruiker), en een echte iPhone.

## Kritische lezing
- Bodoni met Jost is een bekend luxe-paar. Het risico is "boetiekhotel" in plaats van "eigen kamer". Toets: herken je het zonder logo? Het plafond-muurbeeld helpt daar meer bij dan de letter.
- Zand kan bij lange teksten vermoeiend warm worden. Lange teksten staan daarom op het lichtere plafond.
