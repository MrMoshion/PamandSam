# 51 · Zachter: Pams letter, de kleuren en de knoppen (previews)

Vraag van de ontwerper (7 november 2026):
- Pams letter (Literata) is niet zacht genoeg.
- De kleuren mogen zachter en subtieler.
- De verstuurknop is te hard, bij Pam, bij Sam en in de huisstijl.
- Eerst previews, dan pas bouwen.

Previews staan in `presentatie/route-couture-6/`. De site zelf is nog niet aangepast.

## Vijf letters voor Pam (naast de huidige Literata)
**Het cliché:** een ronde, "vriendelijke" letter die kinderlijk wordt, zoals Quicksand. Dat is uitgesloten. Nunito laat zien waar die grens ligt.

| # | Letter | Waarom zacht | Risico |
|---|---|---|---|
| 1 | Fraunces, zacht | afgeronde schreven en uiteinden (de "SOFT"-instelling): geen scherpe hoeken | veel gebruikt door lifestylemerken |
| 2 | Alegreya | geschreven met een pen: levendig, literair | iets onrustiger in de kop |
| 3 | Lora | penseelachtige rondingen, vertrouwd | weinig eigen |
| 4 | Crimson Pro | klassieke boekletter (Garamond-traditie), ingetogen | klein op het scherm wat fijn |
| 5 | Nunito | ongemakkelijk ver: geen schreef, ronde uiteinden | kan kinderlijk worden; Pam lijkt dan meer op Sam |

**Advies:** 1 · Fraunces zacht. Die blijft het meest een boekletter, maar zonder een enkele scherpe punt. Lora is het rustige alternatief.

## Zachtere kleuren (voorstel)
| Rol | Was | Nu | Zachte tekst |
|---|---|---|---|
| Huisstijl muur / plafond | #EFE8D8 / #F8F5EE | #F0EADD / #F9F6F0 | 6,0:1 |
| Pam muur / plafond | #E8D6C0 / #F6EDE2 | #EEE3D5 / #F9F4EE | 5,9:1 |
| Sam muur / plafond | #ECEBE6 / #F9F8F5 | #EEEDEA / #FAF9F7 | 6,3:1 |

## Vier knopstijlen (voor huisstijl, Pam en Sam)
| Stijl | Wat | Contrast van de tekst |
|---|---|---|
| Nu | bijna zwart vlak | 13:1, hard |
| A · Zacht gevuld | gedempte middentoon (#7A6D58 / #8A6849 / #5F676D), witte tekst | 5,1–5,8:1 |
| B · Licht gevuld | iets donkerder vlak van de eigen muur, donkere tekst | 9,3–9,9:1 |
| C · Omlijnd | dunne lijn, donkere tekst | 11–12:1 |
| D · Alleen tekst | "Verstuur →" zonder vlak | 11–12:1; minder snel te vinden |

**Advies:** combineer twee stijlen met elk hun eigen taak.
- **A voor de uitnodiging naar binnen** ("Probeer gratis", "Begin bij Pam/Sam"). Het blijft de duidelijkste stap op de pagina, maar zonder zwart.
- **C voor "Verstuur" in het gesprek.** Daar hoort jouw tekst voorop te staan (de rangorde van de eerste kamer), dus de knop mag terugtreden.

D is het zachtst, maar voor iemand in onrust is een knop die je moet zoeken een drempel.

**Niet getest:** hoe het zachtere geheel werkt bij echte mensen, en of A op een oud of dimmend scherm nog goed opvalt.

## Keuze en uitvoering (ontwerper, 7 november 2026)
- **Letter:** Crimson Pro *alleen voor Pam*: wat zij zegt, haar logo en haar naam in de kamer.
  - De huisstijl houdt Literata voor koppen en logo. Jost blijft voor de rest en voor Sam.
  - Crimson Pro heeft een kleinere x-hoogte (de hoogte van een kleine letter zoals de x). Die is gelijkgetrokken met `font-size-adjust`, zodat Pams tekst even groot leest.
- **Kleuren:** de zachtere set uit deze notitie (huisstijl #F0EADD, Pam #EEE3D5, Sam #EEEDEA).
- **Knoppen in de huisstijl:** zacht gevuld (#7A6D58, witte tekst 5,1:1). Dat geldt voor "Probeer gratis", de formulieren en de balk bovenin.
- **"Begin bij Pam / Sam":** ook zacht gevuld, in hun eigen middentoon (#8A6849 en #5F676D).
- **Knoppen bij Pam en Sam:** licht gevuld, in hun eigen muur iets donkerder (#D9CFC2 en #D9D8D6, donkere tekst 9,3 en 9,9:1). Dat geldt voor de chat, de voorbeeldkamers en de menu's.

Gevonden en hersteld tijdens het testen:
- Tijdens het openen van de kamer staat er even een kopie van de invoerbalk (nodig voor Safari).
- Die kopie toonde de verstuurknop nog donker, waardoor het beeld kort versprong.
- Na het herstel komt de pixeltest weer rustig tot 0 (grootste afwijking 5,9).

Overige tests:
- openen en sluiten frame voor frame: 0 fouten;
- toetsenbord en focus werken;
- nergens horizontaal scrollen;
- de disclaimer overlapt nergens.

Artifact versie 3.
