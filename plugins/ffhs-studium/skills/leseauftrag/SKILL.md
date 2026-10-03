---
name: leseauftrag
description: Arbeitet einen Leseauftrag auf. Liest die genannten Lehrmittel-Kapitel vollständig aus dem PDF, filtert sie nach den Lernzielen und schreibt daraus Konzeptnotizen, mit denen man den Stoff lernen kann. Die Notizen sind das TL;DR des Lehrmittels, in Klartext erklärt für jemanden ohne Vorwissen, statt als Spickzettel verdichtet. Nutze diesen Skill immer, wenn ein Lehrbuchkapitel gelesen, zusammengefasst oder aufgearbeitet werden soll, etwa bei einem Leseauftrag aus Moodle, bei "fass mir Kapitel X zusammen", "was muss ich aus dem Kapitel wissen" oder "ich muss das bis nächste Woche lesen". Ebenso nutzen, wenn eine bestehende Konzeptnotiz unverständlich, zu komprimiert oder zu tabellenlastig ist und neu geschrieben werden soll, und wenn Kapitelnummern eines Lehrmittels geprüft oder Lernziele gegen ein Lehrbuch abgeglichen werden sollen. Der Skill pva-vorbereitung ruft diesen Skill für jeden Leseauftrag eines Vorbereitungsauftrags auf.
---

# Leseauftrag aufarbeiten

## Worum es geht

Ein Leseauftrag nennt Kapitel und Lernziele. Wer ihn bekommt, kennt den Stoff noch nicht
und will ihn verstehen, ohne ganze Kapitel zu durchforsten und selbst abzugleichen, was
davon zählt. Dieser Skill übernimmt beides: Er liest die Kapitel vollständig, filtert sie
nach den Lernzielen und schreibt das Ergebnis als Konzeptnotizen in den Vault. Die Notizen
sind das **TL;DR des Lehrmittels**, und mit ihnen wird gelernt.

**Der Massstab ist der Leser ohne Vorwissen.** Das ist die Person, für die geschrieben
wird: Sie studiert das Fach, hat das Kapitel nicht gelesen und kennt weder die Begriffe
noch den Gedankengang des Buchs. Eine Notiz ist gut, wenn diese Person damit das Lernziel
erfüllen kann. Zwei Sorten Notizen scheitern daran, in entgegengesetzter Richtung:

- Der **Spickzettel**: Tabellen, Pfeile und Halbsätze, die nur versteht, wer den Stoff
  schon kann. Er entsteht, wenn man verdichtet statt erklärt. Für den, der ihn schreibt,
  ist er vollständig, weil er das Kapitel gerade gelesen hat.
- Die **Nacherzählung**: alles aus dem Kapitel, sauber erklärt, ungefiltert. Sie entsteht,
  wenn man erklärt, was im Buch steht, statt was das Lernziel braucht. Sie ist
  verständlich und trotzdem unbrauchbar, weil die Person wieder selbst herausfinden muss,
  was zählt.

Dazwischen liegt das Ziel: so ausführlich, dass man es ohne Buch versteht, und so knapp,
dass nur drinsteht, was ein Lernziel braucht.

Ein Spickzettel hat seinen Platz, etwa als druckfertige Verdichtung für eine
Open-Book-Prüfung. Er ist dann ein eigenes Dokument im Prüfungsordner und entsteht aus
Notizen, die man verstanden hat. Die Konzeptnotiz ist die Lernunterlage.

**Lernziele und Lehrmittel sind die einzigen Quellen.** Die Lernziele bestimmen, was in
die Notiz kommt und wie tief. Der Inhalt stammt aus den Lehrmitteln des Moduls, jede Notiz
nennt Kapitel und Seite. Allgemeines Fachwissen ersetzt das Buch nicht: Eine Notiz, die
beim Nachschlagen im Buch ins Leere führt, kostet in einer Open-Book-Prüfung Zeit, und
eine erfundene Fachaussage wird gelernt.

**Was dieser Skill nicht tut:** Er löst keine Aufgaben und rät keine Kapitelnummern. Wo
das Lehrmittel ein Lernziel nicht abdeckt, benennt er die Lücke, statt sie zu füllen.

Kommt der Leseauftrag als Teil eines ganzen Vorbereitungsauftrags für eine PVA (mit
weiteren Aufträgen, Abgaben, Terminen), führt der Skill `pva-vorbereitung` und ruft diesen
hier für den Leseauftrag auf.

---

## Ablauf

Sechs Schritte. Jeder endet mit einem Kriterium, an dem sich ablesen lässt, ob er fertig
ist. Umfasst der Auftrag mehrere Themenblöcke (Richtwert: mehr als 25 Buchseiten), die
Schritte 2 bis 5 **Block für Block** durchlaufen: Wer erst alles liest und dann alles
schreibt, schreibt die letzten Notizen aus der Erinnerung. Der Lückenabgleich in Schritt 3
(„Was fehlt?") und Schritt 6 laufen einmal für den ganzen Auftrag.

### 1 - Auftrag erfassen

| Was | Wofür |
|---|---|
| **Lernziele wörtlich** | Filter und Tiefenmass für alles Weitere |
| Aufgaben des Leseauftrags (Begriffsliste, Szenarien, Fragen) | zeigen, welcher Stoff gebraucht wird. Gelöst werden sie nicht. |
| Buch, Kapitel, Kapiteltitel | Fundstellen, Quellenangaben |
| Lerneinheit, Vault-Pfad | Ablageort, Frontmatter, Verlinkung |
| vorhandene Konzeptnotizen | werden ergänzt, nicht dupliziert |

**Welche Lernziele filtern?** Die, die der Auftrag dem Leseauftrag zuordnet. Nennt er
keine eigenen, gelten die Lernziele der Lerneinheit, soweit das Kapitel sie berührt. Die
übrigen Lernziele der Lerneinheit dienen nur dem Lückenabgleich in Schritt 3. Nennt die
Person selbst Stoff, den sie erklärt haben will, zählt das wie ein Lernziel. Fehlt dabei
ein Verb, gilt die Stufe des Lernziels, zu dem der Stoff gehört.

Die Lerneinheit ergibt sich aus dem Auftrag oder aus dem Vault (Thema und Frontmatter der
LE-Übersichten). Fehlen Lernziele oder Lehrmittel, danach fragen. Ohne Lernziele gibt es
keinen Filter, und das Ergebnis wird eine Nacherzählung.

**Fertig, wenn** die Lernziele wörtlich vorliegen, Buch und Kapitel benannt sind und klar
ist, wohin die Notizen gehören.

### 2 - Lehrmittel prüfen und lesen

Vorgehen in `references/lehrmittel-pruefen.md`: Text aus dem PDF ziehen, die Kapitel im
Inhaltsverzeichnis suchen, Nummer und Titel gegen den Auftrag prüfen, dann **vollständig
lesen**. Auftrag und Buch weichen häufig ab, weil eine neuere Auflage ein Kapitel
eingeschoben hat. In diesem Fall den Versatz benennen und die Buchnummern verwenden.

Gelesen wird, was der Auftrag nennt. Will die Person nur einen Abschnitt eines Kapitels,
wird dieser vollständig gelesen und der Rest überflogen. Ein zweites Lehrmittel des Moduls
kommt nur dazu, wenn das genannte eine Lücke lässt.

**Fertig, wenn** jedes Kapitel des Auftrags mit echter Nummer und Seitenbereich gefunden
und jeder Abschnitt darin gelesen ist.

### 3 - Lernziele abgleichen

Der Schritt, der dem Leser die Arbeit abnimmt. Er entscheidet, was in die Notizen kommt,
bevor ein Satz geschrieben ist.

**Was verlangt jedes Lernziel?** Das Verb sagt, wie tief die Notiz gehen muss:

| Verb im Lernziel | Die Notiz muss liefern |
|---|---|
| nennen, kennen, grob beschreiben | was es ist, wozu es dient, woran man es erkennt. Im Rechenfach: Definition, ihre Bedeutung in Worten, der Test dazu, ein Beispiel und ein Gegenbeispiel. Mechanismen im Detail und Beweise entfallen. |
| erklären, erläutern, begründen | wie es funktioniert und **warum**, mit Folgen und Grenzen |
| vergleichen, abgrenzen, unterscheiden, einordnen | jedes Ding erklärt, dann die Unterschiede über dieselben Kriterien |
| anwenden, berechnen, auswählen, analysieren | das Verfahren oder die Entscheidung in Schritten und ein durchgeführtes Beispiel |

Zusätze im Lernziel verschieben die Tiefe. „Grob", „im Überblick" und „auf Prinzipebene"
senken sie um eine Stufe: Aus „erklären" wird „beschreiben". „Konzeptionell" heisst
Prinzip und Begründung, ohne Syntax, Produktdetails und Feldlisten.

**Leitfragen ableiten.** Aus den Lernzielen die Fragen ableiten, die die Person nach dem
Lernen beantworten können muss: acht bis zwölf für einen Block von 20 bis 30 Kern-Seiten,
für kürzere Abschnitte entsprechend weniger, für Stoff der untersten Stufe drei bis vier
je Notiz. Die Mischung folgt den Verben: Was ist es und wozu dient es? Wie funktioniert
es, und warum reicht der Vorgänger nicht? Worin unterscheiden sich die Varianten? Was
wählt man in welcher Lage, und warum scheidet die Alternative aus? Die Leitfragen leisten
dreierlei: Sie filtern (was keiner Frage dient, fällt weg), sie gliedern (aus ihnen werden
die Überschriften), und sie prüfen am Schluss (jede muss sich aus den Notizen beantworten
lassen). Als Fragenliste stehen sie nicht im Vault.

**Was im Kapitel dient welcher Leitfrage?** Das Kapitel in thematische Blöcke mit
Seitenbereich teilen, so fein, wie das Gewicht wechselt. Ein nummerierter Abschnitt kann
mehrere Blöcke haben.

| Gewicht | Bedeutung | In den Notizen | Für die Lektüre |
|---|---|---|---|
| **Kern** | eine Leitfrage hängt direkt daran | in der vom Verb verlangten Tiefe erklärt | lesen lohnt sich |
| **Überblick** | Hintergrund, den man zum Verständnis des Kerns braucht | ein bis zwei Sätze | überfliegen genügt |
| **überspringen** | dient keiner Leitfrage (Produktdetails, Geschichte, Spezialfälle) | nicht enthalten | nicht nötig |

**Umfang planen.** Aus dem Kern folgt das Budget für alle Notizen des Blocks zusammen:

- **Textlehrbuch**: rund 100 bis 150 Wörter Notiz je Kern-Seite. Gezählt werden die
  Seiten mit Gewicht Kern, auf halbe Seiten geschätzt, auch die ausserhalb der genannten
  Kapitel. Überblick-Seiten zählen nicht.
- **Rechenfach**: 400 bis 700 Wörter je Begriff. Die Seitenzahl taugt hier nicht als
  Mass, weil eine Seite ohne ihre Beweise sehr dicht ist.
- **Unterste Stufe** (nennen, grob beschreiben): je Notiz 300 bis 500 Wörter, auch wenn
  das Buch zwanzig Seiten darüber schreibt. Für diesen Stoff ersetzt das die Seitenregel.
- **Eine einzelne Notiz neu schreiben**: 400 bis 800 Wörter.

Gemessen wird mit dem Prüfskript. Es zählt jede Notiz ohne ihren Abschnitt Quelle und
meldet mit `--max 500` jede Notiz über dieser Grenze. Bei diesem Umfang waren Notizen im
Test ohne Buch verständlich. Bei doppeltem Umfang wurden dieselben Fragen nicht besser
beantwortet, es stieg nur die Lesezeit.

**Was setzt das Kapitel voraus?** Begriffe aus früheren Kapiteln, ohne die der Kern nicht
zu verstehen ist (ein Schichtenmodell, eine Rechenregel, ein Protokoll), mit Fundstelle
notieren. Sie kommen je in einem Satz in die LE-Übersicht. Das ist kein Stoff von
ausserhalb des Auftrags, sondern die Voraussetzung, ihn zu verstehen.

**Was fehlt?** Für jedes Lernziel prüfen, ob das Kapitel es abdeckt (gezielt suchen, nicht
dem Leseeindruck trauen). Drei Fälle:

- **Der Leseauftrag selbst verlangt etwas** (ein eigenes Lernziel, eine Aufgabe), dessen
  Stoff in einem anderen Kapitel desselben Buchs steht: diese Seiten mitlesen und
  aufarbeiten. Der Auftrag geht vor der Kapitelangabe. In Notiz und Bericht steht, dass
  die Stelle ausserhalb der genannten Kapitel liegt.
- **Ein Lernziel der Lerneinheit**, das der Leseauftrag nicht nennt, hat eine Fundstelle
  anderswo im Buch: Fundstelle in die LE-Übersicht und in den Bericht. Die Person
  entscheidet, ob es dazugelesen wird.
- **Das Buch behandelt es nicht**: eine Lücke im Lehrmittel. Sie wird benannt, mit
  Suchrichtung, und nicht aus Allgemeinwissen gefüllt.

**Fertig, wenn** die Leitfragen stehen, jeder Block des Kapitels ein Gewicht trägt, das
Budget feststeht und jedes Lernziel eine Fundstelle hat oder als Lücke vermerkt ist.

### 4 - Notizen schneiden

Ein Begriff pro Datei. Eine eigene Notiz bekommt, was ein Lernziel nennt oder was für sich
allein erklärbar ist und von anderen Notizen verlinkt wird. Eine Variante oder Erweiterung,
die nur zusammen mit dem Hauptbegriff Sinn ergibt, ist ein Abschnitt in dessen Notiz. Was
im Buch eine halbe Seite einnimmt, wird keine Notiz. Mehrere kleine Begriffe, die der
Auftrag zusammen nennt und die im Buch je nur wenige Absätze haben (vier Angriffsarten,
drei Betriebsarten), teilen sich eine Sammelnotiz mit einem Abschnitt je Begriff. Sie
darf länger sein als eine Einzelnotiz: rund 250 Wörter je Begriff.

Zwei Sonderfälle bleiben kurz. Nennt das Lernziel einen Begriff, den das Buch nicht als
eigenen Abschnitt führt, entsteht eine Brückennotiz von 200 bis 350 Wörtern: Sie definiert
den Begriff, sagt, unter welchen Namen die Sache im Buch steht, und verlinkt die Notizen,
die sie ausführen, statt sie neu zu erzählen. Und gibt das Buch zu einem Begriff nur
wenige Absätze her, ist die Notiz entsprechend kurz. Keine Notiz ist länger als die halbe
Buchstelle, aus der sie schöpft.

Die Notizen folgen der Reihenfolge, in der man sie liest. Greift eine auf eine spätere
vor, sagt sie das Nötige in einem Halbsatz und verlinkt. Braucht ein Abschnitt mehr als
das, etwa das Fazit eines Kapitels, das alle Bausteine voraussetzt, gehört er in die
zuletzt gelesene Notiz.

Vor dem Schreiben festlegen, welche Notiz welche Leitfrage beantwortet und welches
Beispiel bekommt. Auch jeder Überblick-Block bekommt seinen Platz: ein bis zwei Sätze in
genau einer Notiz. In einer Notiz der untersten Stufe dürfen sich mehrere Überblick-Blöcke
einen Satz teilen. Jede Aussage, jede Worterklärung über einen Halbsatz hinaus und jedes
Beispiel hat genau eine Heimat, die anderen Notizen verweisen mit einem Satz und einem
Wikilink. Das Budget aus Schritt 3 auf die Notizen verteilen. Eine Notiz zu teilen, um sie
kürzer zu machen, spart nichts: Das Budget gilt für den Block.

Existiert zu einem Begriff schon eine Notiz, gibt es drei Fälle:

- **Neuer Stoff aus einer weiteren Lerneinheit**: Abschnitt ergänzen, Quelle nachtragen,
  `LE:` im Frontmatter erweitern (es nennt die Lerneinheiten, in denen der Begriff
  vorkommt). Was die Person selbst geschrieben hat, bleibt stehen.
- **Die Notiz soll verständlicher werden**: neu aus Lernziel und Buch aufbauen, nicht die
  alte Notiz Satz für Satz ausformulieren, sonst erbt die neue Auswahl, Ballast und Lücken
  der alten. Dateiname und Frontmatter bleiben, Quellenzeilen nur, soweit die Stelle
  nachgelesen wurde. Am Ende alt gegen neu abgleichen: Formeln, Schnelltests,
  Zahlenbeispiele und Merksätze der alten Notiz, die stimmen und einer Leitfrage dienen,
  gehen nicht verloren. Eigene Einträge der Person (Mitschrift, `## Offen`) bleiben.
- **Eine Nachbarnotiz enthält schon einen Abschnitt zum neuen Begriff**: stehen lassen und
  im Bericht nennen. Verschieben oder löschen entscheidet die Person.

**Fertig, wenn** jede Leitfrage genau einer Notiz zugeordnet ist (eine Frage, die über
zwei Notizen spannt, wird geteilt) und die geplanten Umfänge zusammen im Budget liegen.

### 5 - Schreiben und gegenlesen

Format und Schreibregeln stehen in `references/konzeptnotiz.md`. **Vor der ersten Notiz
lesen.** Die Regel dahinter in einem Satz: Die Form folgt dem Inhalt. Was erklärt wird,
steht in Klartext. Was verglichen oder aufgezählt wird, steht in einer Tabelle oder Liste.
Was gerechnet wird, steht als Formel mit durchgerechnetem Beispiel.

Sind die Notizen eines Blocks geschrieben, zuerst mit dem Prüfskript messen: Wer die
Wortzahl schätzt, liegt daneben. Dann viermal gegenlesen, jedes Mal mit einer anderen
Frage:

1. **Leitfragen.** Jede Leitfrage durchgehen und die Stelle suchen, die sie beantwortet.
   Steht die Antwort nur in einer Tabellenzelle, einem Stichwort oder verteilt über drei
   Notizen, den Abschnitt in Sätzen nachschreiben. Dabei so lesen, als sehe man den Stoff
   zum ersten Mal: Ist jeder Fachbegriff beim ersten Auftreten erklärt?
2. **Streichprobe.** Jeden Absatz fragen: Welche Leitfrage würde ohne ihn schlechter
   beantwortet? Wenn keine, streichen oder auf einen Satz kürzen. Gestrichen werden
   Details, nie Begründungen. Fehlt danach ein Warum, war es zu viel.
3. **Quellentreue.** Zu jeder Fachaussage die Stelle im Buch wiederfinden. Drei Sorten
   Wörter verdienen einen zweiten Blick, weil sie beim Ausformulieren von selbst
   entstehen: Kausalwörter (weil, deshalb), die einen Grund behaupten, den das Buch nicht
   nennt. Absolute Wörter (nur, immer, nie), wo das Buch einschränkt. Eigene Folgerungen,
   die nicht als solche gekennzeichnet sind. Das Prüfskript listet diese Sätze auf:
   `pruefe_notizen.py --quellentreue <Notiz>`.
4. **Muster.** Das Prüfskript über alle Notizen des Blocks zusammen laufen lassen. Es
   meldet Spickzettel-Muster, Überlänge, Seitenangaben im Text und Sätze, die fast gleich
   in zwei Notizen stehen. Jeden Hinweis beheben oder im Bericht begründen:

```bash
python <skill-pfad>/scripts/pruefe_notizen.py "<vault>/02_Konzepte/A.md" "<vault>/02_Konzepte/B.md"
```

Wer die Notiz geschrieben hat, liest über die eigenen Verschärfungen hinweg. Stehen
Subagenten zur Verfügung, die Quellentreue deshalb von einem frischen Subagenten prüfen
lassen: Er bekommt nur den Buchtext und die Notizen, soll jede Fachaussage im Buch suchen
und meldet, was dem Buch widerspricht, nicht darin steht oder es verschärft. Ein zweiter
frischer Subagent liest als Leser ohne Vorwissen: Er bekommt die Notizen in
Lesereihenfolge, aber nicht das Buch, und meldet jedes Fachwort, das ohne Erklärung
benutzt wird, und jeden Gedankensprung. Die Befunde beider danach selbst am Buch prüfen
und einarbeiten.

Bis zu einem Fünftel über der Obergrenze des Budgets ist im Rahmen. Liegt der Block
darüber, wurde meist falsch gefiltert und nicht zu ausführlich erklärt: die vier Gründe in
`references/konzeptnotiz.md` (Abschnitt 7) durchgehen und einmal kürzen. Was dann noch
darüber liegt, bleibt, wenn sonst ein Warum fehlen würde, und steht mit Begründung im
Bericht. Nicht in mehreren Runden kürzen: Verständlichkeit geht vor Kürze.

Lange Markdown-Dateien mit dem Write-Tool schreiben, nicht mit Bash-Heredocs: LaTeX,
Backticks und Anführungszeichen lassen Heredocs regelmässig scheitern.

**Fertig, wenn** jede Leitfrage sich allein aus den Notizen in zusammenhängenden Sätzen
beantworten lässt, jeder Absatz einer Leitfrage dient, jede Fachaussage sich am Buch
belegen lässt und jeder Hinweis des Prüfskripts behoben oder begründet ist.

### 6 - Eintragen und berichten

Im Vault nachtragen (Formate in `pva-vorbereitung/references/dateiformate.md`):

- **LE-Übersicht**: unter `## Überblick` den roten Faden in ein bis zwei Absätzen (worum
  es geht, wie die Konzepte aufeinander aufbauen, Notizen in Lesereihenfolge verlinkt) und
  die Zeile „Vorausgesetzt". Neue Notizen unter `## Konzepte`, Vergleiche über mehrere
  Notizen als Tabelle dort, Lernziele ohne Notiz unter „Noch ohne Notiz". Fundstellen in
  die Tabelle `## Lehrmittel`, Lücken unter `### Lücken im Lehrmittel`. Der Überblick
  deckt ab, was gelesen wurde, und nimmt die Notizen der Lerneinheit auf, die schon da
  sind. Zeilen, die schon dastehen, bleiben.
- **Kapitellandkarte** des Lehrmittels in `07_Quellen`: Auflage des PDF, echte
  Kapitelnummern und Seiten, Befunde der Volltextsuche, Druckfehler und verstümmelte
  Stellen
- **Lesetabelle** der Vorbereitungsnotiz, falls es eine gibt: Spalte `Gewicht` aus Schritt 3
- **Präsenznotiz**, falls es eine gibt: Lücken, die weder Buch noch Auftrag schliessen,
  als Fragen für die Präsenz
- Führt der Vault ein Log zur KI-Nutzung, eine Zeile ergänzen.

Wurde nur eine einzelne Notiz überarbeitet, beschränkt sich das Nachtragen auf
Verlinkung, Fundstellen und die Zeile im Log.

Im Chat berichten:

- der **Kapitelabgleich**: stimmten die Nummern, gab es einen Versatz?
- die **Gewichtung**: was ist Kern, was Überblick, was wurde übersprungen und warum
- die **Lücken**: welche Lernziele deckt das Lehrmittel nicht ab, wo ist stattdessen zu
  suchen, was wurde von ausserhalb der genannten Kapitel dazugelesen
- welche Notizen neu sind oder ergänzt wurden (eine Zeile, keine Dateiliste)

**Fertig, wenn** jede neue Notiz von der LE-Übersicht aus erreichbar ist (prüfbar mit
`pva-vorbereitung/scripts/pruefe_vault.py <vault-pfad>`) und der Bericht Gewichtung und
Lücken nennt.

---

## Häufige Fehler

**Verdichten statt erklären.** Eine Tabellenzelle wie „über ACK-Flag (fälschbar), bei UDP
gar nicht" ist für den, der sie schreibt, eine vollständige Aussage, weil er das Kapitel
gerade gelesen hat. Für den Leser ohne Vorwissen ist sie ein Rätsel.

**Alles erklären statt filtern.** Der Gegenfehler, und er liegt näher, sobald man in
Klartext schreibt: Jeder Abschnitt des Kapitels wird sauber erklärt, auch der, den kein
Lernziel braucht. Die Leitfragen entscheiden, nicht die Vollständigkeit des Kapitels.

**Tiefe am Buch statt am Lernziel ausrichten.** Widmet das Buch einem Protokoll zwanzig
Seiten und das Lernziel verlangt „den Nutzen grob beschreiben", wird die Notiz kurz.

**Begründungen erfinden.** Die Regel „das Warum steht im Satz" verleitet dazu, ein
„deshalb" zu setzen, wo das Buch keinen Grund nennt, und aus „kann" ein „ist" zu machen.
Das Ergebnis liest sich flüssig und ist falsch. Das Warum kommt aus dem Buch.

**Lücken glattbügeln.** Fehlt ein Lernziel im Lehrmittel, ist die Versuchung gross, es aus
allgemeinem Wissen zu füllen. Lücke benennen, Suchrichtung angeben.

---

## Referenzdateien

- `references/konzeptnotiz.md` - Aufbau der Konzeptnotiz, Schreibregeln (Klartext, beim
  Buch bleiben, Tabellen, Rechenfächer, Umfang), Vorher und Nachher, drei Muster.
  **Vor dem Schreiben der ersten Notiz lesen.**
- `references/lehrmittel-pruefen.md` - PDF-Text extrahieren, Kapitelnummern verifizieren,
  Seiten am Bild prüfen, Lernziele gegen das Lehrmittel abgleichen.
- `scripts/buchseiten.py` - Text extrahieren, Begriffe mit Buchseite suchen, Seiten
  ausgeben oder als Bild rendern.
- `scripts/pruefe_notizen.py` - zählt die Wörter und findet Sätze in Tabellenzellen,
  erklärende Spaltenköpfe, Theorie aus Tabellen oder Stichpunkten, Pfeilnotation, harte
  Zeilenumbrüche, Überlänge, Seitenangaben im Text und Sätze, die fast gleich in zwei
  Notizen stehen. Mit `--quellentreue` die Prüfliste der Kausal- und Absolutwörter.
- `assets/Template - Konzeptnotiz.md` - Vorlage.
- `pva-vorbereitung/references/dateiformate.md` - LE-Übersicht, Kapitellandkarte,
  Vorbereitungsnotiz (Nachbarskill).
