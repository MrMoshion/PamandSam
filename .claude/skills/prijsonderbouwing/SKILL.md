---
name: prijsonderbouwing
description: Prijzen van Studio.Edu bepalen en onderbouwen per stap van een opdracht, met marktprijzen uit bronnen, en toetsen hoe ze gepresenteerd worden. Gebruik dit altijd als de ontwerper vraagt wat iets moet kosten, of een bedrag klopt, hoe een prijs uit te splitsen of te onderbouwen, of als er prijzen in een voorstel, offerte of presentatie voor een klant komen. Ook bij twijfel over een bedrag ("schrikt dit niet af?", "is dit niet te veel?").
---

# Prijsonderbouwing (Studio.Edu)

Studio.Edu wil prijzen die eerlijk, te verdedigen en goed gepresenteerd zijn. Deze skill helpt de ontwerper kiezen. Claude onderzoekt en rekent; **de ontwerper kiest het bedrag.**

## Volgorde

### 1. Eerst begrijpen
- Lees de werkafspraken van het project (`CLAUDE.md`) en de prijsafspraak met de ontwerper, als die er is (dagtarief, ondergrens, minimale projectprijs).
- Vat samen welke stappen er geprijsd moeten worden en wat de klant wil (bijvoorbeeld: het moet zich terugbetalen). Vraag om bevestiging voor je rekent.
- Beantwoord vragen van de ontwerper eerst. Pas niets aan in een presentatie zonder akkoord.

### 2. Het werk uitsplitsen in soorten werk
- Per stap: een paar koppen met kort wat erin zit. Tastbaar, geen lange lijst.
- **Niet in dagen of uren naar de klant.** Uren nodigen uit tot afdingen; soorten werk laten zien wat hij krijgt. Dagen mag je intern gebruiken om te rekenen.
- Maak zichtbaar waar het denkwerk zit (bijvoorbeeld "het systeem uitdenken", "een huisstijl binnen een huisstijl", UX), zodat het niet leest als "een kleurtje kiezen".
- Benoem wat inbegrepen is (eerder werk, het aantal feedbackrondes) en wat niet (kosten van derden).
- Werkt de klant zelf mee, leg dan de werkverdeling vast (bijvoorbeeld 50/50) en zet "in overleg" bij die stap, met een voetnoot dat het om de werkverdeling gaat.

### 3. Marktprijzen opzoeken
- Zoek per onderdeel wat Nederlandse studio's, bureaus en freelancers vragen. Gebruik de zoekfunctie uitgebreid, want dit bepaalt het oordeel.
- Noem bij elk getal de bron als link.
- Zeg eerlijk:
  - dat de meeste bronnen bureaus zijn die zichzelf aanprijzen;
  - dat wat er precies in zit per bureau verschilt;
  - wat je niet hebt kunnen vinden.

  Verzin geen marktprijzen.
- Zoek ook vergelijkingen die de klant helpen rekenen. Een voorbeeld: wat werkgevers betalen voor een vergelijkbare dienst. Alleen echte getallen met een bron.

### 4. Een prijs kiezen en onderbouwen
Leg per stap naast elkaar:
1. **De markt:** de bandbreedte uit stap 3.
2. **Het werk:** de interne inschatting tegen het dagtarief.
3. **De afspraak:** het dagtarief, de ondergrens en de minimale projectprijs.
4. **De waarde:** wat het de klant oplevert. Prijs naar waarde, niet naar uren. Dat de ontwerper snel werkt, is vakmanschap en geen reden om goedkoper te zijn.

Kies dan een bedrag of bandbreedte en zeg waarom:
- Een vaste prijs voor de eerste stap, en bandbreedtes voor wat later komt.
- Zet per stap een beslismoment, zodat de klant na elke stap kan stoppen.
- Let op verhoudingen. Is één stap een uitschieter, kijk dan eerst of de andere stappen te laag zijn, voordat je het met een uitleg oplost.

Zeg eerlijk wat een aanname is, wat je niet hebt gecontroleerd, en waar de ervaring van de ontwerper beslist.

### 5. De presentatie toetsen
Laad `marketing-psychology:price-framing` en toets:
- **Het anker:** welk getal ziet de klant vlak voor de prijs? Een klein getal (zoals de opbrengst per gebruiker) vlak voor een groot bedrag laat het bedrag groter lijken. Zet een groot, eerlijk getal met een bron vóór de prijs, en de kleine getallen erna, gekoppeld aan een doel.
- **Inhoud vóór prijs:** eerst wat hij krijgt, daarna de tabel.
- **Namen:** noem een stap naar wat hij werkelijk is, niet naar het kleinste onderdeel.
- **Geen trucjes:** geen opgeblazen eerste bedrag om het echte te laten meevallen, en geen verzonnen "normale" prijzen. Marktprijzen gebruik je in het gesprek, niet op een pagina.
- **Een rekensom op de pagina:** de som staat erbij, en het woord "indicatie" als er aannames in zitten.

### 6. Opleveren
1. Een korte tabel per stap: wat hij krijgt, de prijs, het beslismoment. Prijzen exclusief btw.
2. De bronnen als links.
3. De aannames.
4. Hooguit drie vragen voor de ontwerper.
5. Leg de uitkomst vast in `analyse/` (genummerd), en commit en push na akkoord.

## Toon
Schrijf in het Nederlands, helder en zonder jargon. Wees eerlijk als een bedrag te hoog of te laag lijkt. "Dit is gemiddeld" is stuurinformatie, geen kritiek.
