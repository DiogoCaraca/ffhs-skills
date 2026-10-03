# Konzeptnotiz

Aufbau und Schreibregeln der Konzeptnotiz. Mit ihr wird gelernt: Sie erklärt den Stoff
jemandem, der ihn noch nicht kennt. Vor der Prüfung liest man die Notizen, nicht mehr das
Buch.

## Inhalt

1. Aufbau
2. Die Form folgt dem Inhalt
3. Klartext schreiben
4. Beim Buch bleiben
5. Tabellen, Listen, Skizzen
6. Rechenfächer
7. Tiefe und Umfang
8. Vorher und nachher
9. Muster

---

## 1. Aufbau

Jede Konzeptnotiz hat dieselben vier Teile in derselben Reihenfolge. Wer eine kennt,
findet sich in allen zurecht.

```markdown
---
LE: 3
tags: [isich/konzept, isich/le3]
---

# Paketfilter

Kopf: was es ist, wozu es dient, wo eine Grenze liegt.

## Theorie

### <kurze Überschrift>

## Beispiel

## Quelle

Eckert Kap. 14.1.2, S. 719-728 (Filterregeln S. 721, zustandsbehaftet S. 723, Grenzen S. 726)
```

| Teil | Inhalt |
|---|---|
| Kopf | Zwei bis vier Sätze direkt unter der H1, höchstens rund 60 Wörter, ohne eigene Überschrift. Bei Rechenthemen mit der Formel. |
| `## Theorie` | Die Erklärung, gegliedert mit `###`. |
| `### Achtung` | Optional, am Ende der Theorie: ein bis drei Fehler, die man beim Anwenden macht. |
| `## Beispiel` | Ein konkreter Fall mit seinen Zahlen. Mehrere Beispiele mit fettem Vorspann. |
| `## Offen` | Nur wenn die Person selbst etwas klären muss, mit Checkbox, vor `## Quelle`. |
| `## Quelle` | Kapitel und Seitenbereich, eine Zeile je Kapitelabschnitt, in Klammern die Seiten der Kernaussagen. |

**Der Kopf ist das Urteil.** Er sagt, was es ist, welches Problem es löst und wo eine
Grenze liegt. Wer nur den Kopf liest, kennt die Kernaussage: „Ein Paketfilter ist eine
Firewall, die Pakete nach Adressen und Ports filtert. Er ist preiswert und relativ einfach
zu realisieren, kontrolliert aber nur grob und verlässt sich auf Angaben, die sich fälschen
lassen." Auch der Kopf bleibt beim Buch: keine Rangfolge („die wichtigste Grenze"), die
dort nicht steht.

**Überschriften kommen aus den Leitfragen.** Jeder Abschnitt beantwortet eine Frage, die
die Person nach dem Lernen beantworten können muss, und die Überschrift nennt sie: als
knappe Frage („Warum reicht ein zustandsloser Filter nicht?") oder als Sachbegriff
(„Grenzen", „Rechentest"). Höchstens eine Zeile, denn über die Überschriften findet man
die Stelle in der Open-Book-Prüfung wieder.

**Kein festes Raster.** Ein Abschnitt entsteht, wenn er einen eigenen Gedankenschritt
trägt. Ein Schema wie Problem, Idee, Funktionsweise, Stärken, Grenzen für jede Notiz
erzeugt bei einfachen Begriffen Füllabschnitte.

**Was das Lernziel direkt beantwortet, steht früh und bekommt den meisten Raum.** Verlangt
das Lernziel, drei Verfahren zu unterscheiden, ist die Unterscheidung nicht der letzte und
kürzeste Abschnitt.

**Das Beispiel übt das Lernziel ein.** Es nimmt einen Fall mit Zahlen, Adressen oder
Regeln, bevorzugt den aus dem Lehrmittel, spielt ihn durch und endet mit einem Satz, der
sagt, was der Fall zeigt. Prüffrage: Kann ich nach dem Beispiel, was das Lernziel
verlangt? Einen Ablauf, den die Theorie schon durcherzählt hat, wiederholt das Beispiel
nicht.

**Achtung ist für Anwendungsfehler.** Was der Begriff nicht kann, sind Grenzen und gehört
als eigener Abschnitt in die Theorie. Unter Achtung stehen die Fehler, die man beim
Anwenden macht, je in einer Zeile: eine Verwechslung zweier Begriffe, ein übersehener
Gültigkeitsbereich, eine Vorzeichenfalle. Was die Theorie schon erklärt, wiederholt der
Block nicht. Gibt es keinen solchen Fehler, entfällt er.

Weitere `##`-Abschnitte gibt es nicht. Dateinamen rein ASCII (`Verschluesselung`), im Text
korrektes Deutsch. Frontmatter nur `LE:` und `tags:`.

---

## 2. Die Form folgt dem Inhalt

Welche Form ein Stück Inhalt bekommt, hängt davon ab, was es ist:

| Der Inhalt ist | Form |
|---|---|
| ein Konzept, ein Mechanismus, eine Begründung, ein Zusammenhang | Klartext in Absätzen |
| mehrere Dinge, verglichen über dieselben Kriterien | Tabelle |
| gleichartige Fälle, Regeln oder Tests zum Nachschlagen | Tabelle oder Liste |
| ein Ablauf, ein Verfahren | nummerierte Schritte |
| eine Rechenregel, ein Gesetz | Formel, dazu ein Satz, was sie aussagt |
| ein Aufbau, eine Anordnung | Skizze im Codeblock |

Eine Tabelle kann vergleichen, aber nicht erklären. Erklären heisst, einen Grund an eine
Aussage zu binden: „weil", „deshalb", „dadurch". In einer Tabellenzelle hat das keinen
Platz, also fällt der Grund weg und es bleibt die Behauptung. Genau das macht aus einer
Lernunterlage einen Spickzettel.

Das ist kein Verbot von Tabellen. Eine Übersicht der Schnelltests, ein Regelsatz, eine
Gegenüberstellung dreier Verfahren sind genau das, was man in der Prüfung sucht. Sie
stehen nach der Erklärung und fassen zusammen.

---

## 3. Klartext schreiben

Der Leser studiert das Fach und sieht diesen Stoff zum ersten Mal. Er ist nicht langsam,
aber er kennt weder die Begriffe noch den Gedankengang des Buchs, und er hat das Kapitel
nicht gelesen.

**Mit dem Problem beginnen.** Ein Begriff wird verständlich, wenn man weiss, wofür es ihn
gibt. Am besten trägt ein konkreter Fall, an dem der Vorgänger scheitert: Die Strategie
„FTP ja, aber nur lesend" kann ein Paketfilter nicht umsetzen, also braucht es einen
Filter, der die Befehle des Dienstes versteht. Danach folgt die Idee fast von selbst.

**Vom Anschaulichen zum Abstrakten.** Zuerst der Fall mit Zahlen oder das Bild, dann die
allgemeine Aussage. Auf eine Formel mit Buchstaben folgt eine Zeile mit eingesetzten
Zahlen.

**Eigenschaften auf ihre Ursache zurückführen.** Fünf Schwächen nebeneinander muss man
auswendig lernen. Eine Ursache mit ihren Folgen versteht man: „Die Grenzen haben eine
gemeinsame Ursache: Der Filter vertraut Header-Angaben, die niemand beglaubigt hat." In
Rechenfächern entspricht das der Frage, aus welcher Definition oder Voraussetzung ein
Satz folgt und was bricht, wenn sie fehlt.

**Die Kette bis zur Folgerung schliessen.** Was es sieht, was es deshalb kann, was es
deshalb nicht kann, was daraus für den Einsatz folgt. Die Folgerungen und Empfehlungen des
Autors („von aussen nur wenige Ports öffnen") fallen beim Zusammenfassen als Erstes weg
und zählen in Szenariofragen am meisten.

**Das Verb des Lernziels bedienen.** Für jedes Verb gibt es eine Stelle, die genau das
vormacht. Verlangt das Lernziel „erklären", steht dort die Erklärung. Verlangt es
„begründen", „auswählen" oder „anwenden", spielt die Notiz eine Entscheidung in Sätzen
durch: wenn dies verlangt ist, dann jenes, weil, und warum die Alternative ausscheidet.
Verlangt es „unterscheiden" oder „vergleichen", steht das Ergebnis des Vergleichs in der
Notiz selbst, ein bis zwei Sätze je Nachbarbegriff: Ein Link ersetzt die Kernaussage
nicht, erklärt wird der Nachbar aber in seiner eigenen Notiz. Die Vergleichstabelle über
alle Begriffe steht einmal, in der LE-Übersicht.

**Ein Absatz, ein Gedanke.** Zwei bis fünf Sätze. Der erste sagt, worum es geht, die
folgenden begründen oder führen aus.

**Das Warum steht im Satz.** „Zustandslose Filter können UDP nicht gezielt filtern" ist
eine Behauptung. „UDP baut keine Verbindung auf, jedes Paket steht für sich, deshalb kann
ein zustandsloser Filter eine Antwort nicht von einem unverlangten Paket unterscheiden"
ist eine Erklärung. Pfeile, Gleichheitszeichen und Pluszeichen ersetzen keine Verben: Sie
sagen, dass etwas zusammenhängt, aber nicht wie.

**Alles erklären, was man zum Nachvollziehen braucht.** Jeden Fachbegriff beim ersten
Auftreten in einem Halbsatz klären, in jeder Notiz, auch wenn er eine eigene Notiz hat:
„ein Screening Router (ein Router mit Paketfilter)". Das ist keine Wiederholung. Der
Halbsatz sagt, was das Wort bedeutet, erklärt wird es in der Nachbarnotiz. Dasselbe gilt
für Rechenregeln aus früheren Kapiteln, ohne die sich ein Beispiel nicht nachrechnen
lässt, und für Begründungen: Setzt die Begründung des Buchs ein anderes Verfahren voraus,
das Nötige in einem Satz dazusagen oder eine Begründung nehmen, die ohne es auskommt.

**Den Stoff schreiben, nicht den Buchbericht.** „Ein Paketfilter entscheidet nach
Adressen und Ports", nicht „Eckert beschreibt, dass ein Paketfilter". Der Autor wird
genannt, wo es auf sein Urteil ankommt („Eckert nennt die Architektur kaum noch üblich").

**Ganze Sätze, kurze Sätze.** Subjekt, Verb, Aussage. Keine Halbsätze, keine Ketten aus
Substantiven, kein Lehrbuchdeutsch nacherzählen.

**Fettdruck sparsam.** Fett ist der Begriff, der an dieser Stelle definiert wird. Wenn in
jedem Satz etwas fett ist, ist nichts hervorgehoben.

**Ein Absatz ist eine Zeile.** Keine Zeilenumbrüche innerhalb eines Absatzes: Obsidian
zeigt jeden Umbruch an, und der Text zerfällt.

**Keine Didaktik.** Lerntipps, Hinweise auf Prüfungsrelevanz, Kontroll- und
Verständnisfragen gehören nicht in die Notiz.

---

## 4. Beim Buch bleiben

Wer in Klartext erklärt, schreibt mehr eigene Sätze als jemand, der Stichworte abschreibt.
Dabei entstehen Fehler einer bestimmten Sorte. Sie sind klein, klingen plausibel und
werden gelernt.

**Das Warum kommt aus dem Buch.** Ein „deshalb" behauptet einen Zusammenhang. Nennt das
Buch den Grund, steht er in der Notiz. Nennt es keinen, wird keiner erfunden.

**Nicht verschärfen.** „Im Wesentlichen nach Header-Angaben" ist nicht „nur nach
Header-Angaben". „Keine sehr hohen Anforderungen" ist nicht „geringer Schutzbedarf". Die
Einschränkungen des Autors (kann, meist, in der Regel, könnte) bleiben stehen. Wörter wie
nur, immer, nie stehen in der Notiz, wenn sie im Buch stehen. Dasselbe gilt für
Superlative und Rangfolgen (die wichtigste, die einfachste, der höchste). Ein Beispiel des
Buchs bleibt ein Beispiel: Aus „zum Beispiel" wird kein „also".

**Eigenes kennzeichnen, knapp.** Eine fachliche Aussage, die über das Buch hinausgeht,
bekommt zwei Wörter in Klammern: „(eigene Folgerung)", „(nicht bei Eckert)". Eine eigene
Zusammenstellung, etwa Entscheidungsfragen für ein Szenario, wird einmal am Anfang
gekennzeichnet und danach gegen das Buch geprüft: Jede abgeleitete Regel muss zu allem
passen, was das Kapitel sagt. Nicht gekennzeichnet werden Gliederung, Überschriften und
Wortwahl.

**Belege stehen unter Quelle.** Kapitel und Seitenbereich, dahinter in Klammern die Seiten
der Kernaussagen, so genau, dass man jede im Buch findet. Im Fliesstext stehen keine
Seitenzahlen, nur die Nummer eines Beispiels, einer Abbildung oder einer Definition des
Buchs, wenn man sie dort nachschlagen will („Bsp. 14.1", „Def. 14.1"). Eine Seitenangabe
hinter jedem Satz macht aus der Lernunterlage einen Apparat.

**Arbeitsnotizen gehören nicht in die Notiz.** Was eine Volltextsuche ergab, wie eine
Stelle rekonstruiert wurde, was das Buch nicht behandelt: Das steht im Bericht, in der
LE-Übersicht unter Lücken oder in der Kapitellandkarte. Ist eine Formel oder Regel im Buch
verdruckt, steht in der Notiz die berichtigte Form und der Vermerk dazu in der Quellenzeile
(„Bsp. 14.2, im Buch verdruckt, hier berichtigt"). `## Offen` ist für das, was die Person
selbst klären muss.

**Nachbarkapitel nur, wenn ein Lernziel es verlangt.** Stoff, der bloss thematisch passt,
bleibt draussen, ein Link auf die Notiz, die ihn behandelt, genügt. Braucht eine Leitfrage
eine Aussage, die im genannten Kapitel fehlt und in einem anderen Kapitel oder im zweiten
Lehrmittel des Moduls steht, kommt sie von dort, mit eigener Quellenzeile.

**Datierte Urteile datieren.** „Sicher", „unsicher", „empfohlen", „üblich" gelten zum
Stand des Buchs. Wo es darauf ankommt, steht das Jahr dabei. Widersprechen sich zwei
übernommene Aussagen scheinbar, löst ein Satz den Widerspruch auf.

---

## 5. Tabellen, Listen, Skizzen

**Die Tabelle fasst zusammen, was der Text erklärt hat.** Sie steht nach der Erklärung,
nicht an ihrer Stelle. In den Zellen stehen Angaben: ein Wort, eine Zahl, ein Stichwort.
Probe: Löscht man die Tabelle, muss das Konzept immer noch verständlich sein.

Eine Tabelle ist richtig, wenn

- mindestens zwei Dinge über dieselben Kriterien nebeneinanderstehen (drei
  Firewall-Klassen nach Schicht, Filterkriterium, Authentifikation), oder
- gleichartige Fälle oder Daten aufgelistet werden, die man nachschlägt (Schnelltests,
  Filterregeln, Wertetabellen, Fallunterscheidungen).

**Der Zellentest.** Enthält eine Zelle ein Verb, einen Pfeil, ein Semikolon oder ein
„weil", gehört ihr Inhalt in einen Satz. Spaltenköpfe wie „Grund", „Warum", „Aussage",
„Was es leistet" zeigen eine Erklärung an, die sich als Tabelle verkleidet hat. Zwei
Listen nebeneinander („Vorteile" neben „Grenzen") sind kein Vergleich, weil die Zeilen
nichts miteinander zu tun haben.

Eine Tabelle, die nur wiederholt, was zwei Absätze davor steht, ohne dass man sie zum
Nachschlagen braucht, entfällt.

Eine Liste ist richtig für gleichartige Dinge, die jeweils in eine Zeile passen. Brauchen
die Punkte je eine Begründung, sind es Absätze.

Nummerierte Schritte sind richtig für Verfahren und Abläufe, bei denen die Reihenfolge
zählt.

Eine Skizze im Codeblock ersetzt eine Abbildung, die im Text fehlt: eine Kette von Zonen,
ein Protokollablauf, ein Schichtenstapel. Eine Zeile genügt oft.

Vergleiche über mehrere Notizen hinweg (alle Verfahren einer Lerneinheit nebeneinander)
gehören einmal in die LE-Übersicht, nicht in jede Notiz.

---

## 6. Rechenfächer

In Rechenfächern trägt die Formel die Aussage. Die Erklärung darum herum macht sie
verständlich, sie ersetzt sie nicht. Eine Notiz zu einem Rechenthema enthält:

- die **Definition in Worten**, danach als abgesetzte Formel. Jedes Symbol ist beim
  ersten Auftreten benannt, und nach der formalen Fassung sagt ein Satz dasselbe in
  Alltagssprache.
- den **Test oder das Verfahren** als abgesetzte Formel oder nummerierte Schritte, mit
  einem Satz, wann es gilt
- eine **Übersicht der Schnelltests** als Tabelle, wenn es mehrere gibt (Fall, Test).
  Jeder Test steht mit seinem Kriterium da, auch wenn eine Nachbarnotiz ihn herleitet: Ein
  Link ersetzt das Kriterium nicht.
- mindestens ein **vollständig durchgerechnetes Beispiel** mit konkreten Zahlen, mit
  Zwischenschritten und einem Satz zur Deutung des Ergebnisses. Wo es einen Test gibt, ein
  Fall, der ihn besteht, und einer, der ihn nicht besteht.
- die **anschauliche Deutung**, wo es eine gibt (geometrisch, als Bild)

Beweise kommen nur hinein, wenn sie in höchstens zwei Sätzen ein Warum liefern oder als
Rechenregel dienen. Der Wortlaut eines Satzes aus dem Buch steht nur da, wenn er gebraucht
wird.

Formeln und Rechenbeispiele vor dem Übernehmen nachrechnen und am Seitenbild prüfen
(`lehrmittel-pruefen.md`). Rechnet das Buch nur den allgemeinen Fall oder nur einen der
beiden Fälle vor, sind eigene Zahlen erlaubt: nachgerechnet und mit „(eigene Rechnung)"
gekennzeichnet. Code gehört ins Cheatsheet des Moduls, nicht in die Notiz.

---

## 7. Tiefe und Umfang

Die Tiefe kommt aus dem Lernziel, nicht aus dem Buch. Die Gewichtung aus dem
Lernziel-Abgleich entscheidet:

| Gewicht | In der Notiz |
|---|---|
| Kern | in der Tiefe erklärt, die das Verb des Lernziels verlangt |
| Überblick | ein bis zwei Sätze |
| überspringen | nicht in der Notiz |

Was fast immer wegfällt: Produktnamen, Syntax, Begriffsgeschichte, Aufzählungen von
Einzelfunktionen, Querverweise auf andere Kapitel, allgemeine Einordnungen des Autors. Von
einer Detailliste bleibt das Prinzip in einem Satz, höchstens mit einem Detail als Beleg.

**Jede Aussage hat eine Heimat.** Ein Mechanismus oder ein Argument, das mehr als einen
Satz braucht, wird in genau einer Notiz ausgeführt, die anderen verweisen mit einem Satz
und einem Link. Dasselbe gilt für Beispiele. Der Halbsatz, der ein Fachwort klärt, darf in
jeder Notiz stehen. Zwei Notizen dürfen dieselbe Sache aus verschiedenen Blickwinkeln
zeigen (den Aufbau in der einen, den Zweck in der anderen), aber nicht denselben Absatz
zweimal.

**Das Budget gilt für den Block.** Wie es sich berechnet, steht in Schritt 3 des Skills.
Die einzelne Notiz liegt meist zwischen 400 und 800 Wörtern, gezählt ohne den Abschnitt
Quelle. Was darüber liegt, meldet das Prüfskript. Verlangt das Lernziel nur „nennen" oder
„grob beschreiben", sind es 300 bis 500. Keine Notiz ist länger als die halbe Buchstelle,
aus der sie schöpft: Gibt das Buch eine halbe Seite her, wird es ein Absatz in einer
Nachbarnotiz, keine eigene Notiz.

Ist der Text länger, hat das meist einen von vier Gründen: Überblick-Stoff wird in
Kern-Tiefe erklärt, eine Nachbarnotiz wird wiederholt statt verlinkt, ein Absatz dient
keiner Leitfrage, oder ein Unterthema hat eine eigene Notiz bekommen, obwohl ein Abschnitt
gereicht hätte.

Gekürzt werden Details, nie Begründungen. Das Budget ist der Normalfall, überschritten
wird es nur, wenn sonst ein Warum fehlt: Ein TL;DR ist erst eines, wenn es ohne Buch
verständlich ist.

---

## 8. Vorher und nachher

**Spickzettel.** Korrekt, aber nur für den lesbar, der es schon weiss:

```markdown
| | zustandslos | zustandsbehaftet |
|---|---|---|
| Antworten erkennen | über ACK-Flag (fälschbar), bei UDP gar nicht | merkt sich ausgehende Anfragen kurz (Timeout) |
| UDP, DNS, aktives FTP | nicht gezielt filterbar (Callback-Problem) | lösbar |
```

**Lernunterlage.** Derselbe Inhalt, erklärt:

```markdown
### Warum reicht ein zustandsloser Filter nicht?

Ein zustandsloser Filter entscheidet allein anhand des Pakets, das gerade vor ihm liegt. Er merkt sich nichts. Daran scheitert er in zwei Fällen.

Erstens erkennt er Antworten nur bei TCP. Dort ist das ACK-Flag bei einer neuen Anfrage nicht gesetzt, bei Antwortpaketen schon. UDP baut keine Verbindung auf, jedes Paket steht für sich. Der Filter kann deshalb eine UDP-Antwort nicht von einem unverlangten Paket unterscheiden.

Zweitens braucht er feste, im Voraus bekannte Ports. Beim aktiven FTP nennt die ausgehende Verbindung einen Port, über den der Server dann von aussen zurückruft (Callback-Problem). Eine statische Regel kann diesen Port nicht kennen.

### Was macht ein zustandsbehafteter Filter besser?

Er merkt sich ausgehende Anfragen für einige Sekunden in einer Tabelle. Ein eingehendes Paket gilt als Antwort, wenn es zu einer gemerkten Anfrage passt. Beim aktiven FTP liest er den vereinbarten Port aus der ausgehenden Verbindung mit und lässt den Rückruf auf diesem Port zu.
```

Die Überschriften sind Leitfragen, jeder Absatz trägt einen Gedanken mit seinem Grund, und
die Tabelle ist weggefallen, weil sie nach dieser Erklärung nichts mehr zum Nachschlagen
bietet.

**Nacherzählung.** Der Gegenfehler: alles erklärt, nichts gefiltert. Das Lernziel hiess
„den Einsatz von Firewalls erklären und Schutzoptionen begründen":

```markdown
### Schutz der Firewall selbst

Eine Firewall ist selbst eine sicherheitskritische Komponente und muss vor Angriffen besonders geschützt werden. Firewall-Rechner erhalten deshalb meist erheblich weniger Software als ein gewöhnlicher PC (S. 719). Für die Rechner, auf denen Proxy-Server laufen, nennt Eckert konkrete Regeln (S. 732):

- Programme und Bibliotheken entfernen, die für die Firewall-Funktion nicht nötig sind
- den Rechner nicht gleichzeitig als Datei- oder Webserver verwenden
- keine normalen Benutzerkonten zulassen
- keinen Compiler installieren
```

Verständlich, belegt und für keine Leitfrage nötig. Im TL;DR bleibt ein Satz:
„Firewall-Rechner tragen möglichst wenig Software, damit es weniger Angriffspunkte gibt."

---

## 9. Muster

Drei Muster: ein Rechenthema, eine kurze Notiz für ein Lernziel der untersten Stufe, ein
Konzeptthema in voller Tiefe. Sie zeigen Form und Tiefe. Tags und Schreibweisen folgen dem
Vault, und fällt ein Leseauftrag auf dasselbe Kapitel, entsteht die Notiz trotzdem aus dem
Buch.

### Rechenthema

Die Formel trägt die Aussage. Der Kopf sagt in Worten, was sie tut.

```markdown
---
LE: 1
tags: [linalg/konzept, linalg/le1]
---

# Kreuzprodukt (Vektorprodukt)

Das Kreuzprodukt macht aus zwei Vektoren des Raums einen dritten, der auf beiden senkrecht steht:

$$v \times w = \begin{pmatrix} v_y w_z - v_z w_y \\ v_z w_x - v_x w_z \\ v_x w_y - v_y w_x \end{pmatrix}$$

In jeder Zeile fehlt der eigene Index, die beiden anderen kommen über Kreuz. Man braucht es, wenn eine Richtung gesucht ist, die auf einer Ebene senkrecht steht, und für Flächen.

## Theorie

### Eigenschaften

Zwei Eigenschaften braucht man ständig. Das Ergebnis steht senkrecht auf beiden Faktoren, deshalb liefert das Kreuzprodukt zweier Richtungsvektoren einer Ebene deren [[Normalenvektor]]. Und die Reihenfolge zählt: Vertauscht man die Faktoren, dreht sich das Vorzeichen.

| Eigenschaft | Formel |
|---|---|
| senkrecht auf beiden Faktoren | $(v \times w) \cdot v = 0$ und $(v \times w) \cdot w = 0$ |
| Vorzeichen beim Vertauschen | $v \times w = -(w \times v)$ |

### Flächen

Die Länge des Kreuzprodukts ist die Fläche des Parallelogramms, das $v$ und $w$ aufspannen. Das Dreieck mit denselben Seiten hat die halbe Fläche.

$$A_{\text{Parallelogramm}} = \|v \times w\| \qquad A_{\text{Dreieck}} = \tfrac{1}{2}\|v \times w\|$$

### Achtung

- Nur im $\mathbb{R}^3$ definiert: Für Vektoren der Ebene gibt es kein Kreuzprodukt.
- Nicht mit dem Skalarprodukt verwechseln: Dort ist das Ergebnis eine Zahl, hier ein Vektor.

## Beispiel

$(-1\ 0\ 1)^T \times (1\ -1\ 0)^T$:

$$\begin{aligned}
\text{1. Komponente} &= 0\cdot0 - 1\cdot(-1) = 1\\
\text{2. Komponente} &= 1\cdot1 - (-1)\cdot0 = 1\\
\text{3. Komponente} &= (-1)(-1) - 0\cdot1 = 1
\end{aligned}$$

Ergebnis $(1\ 1\ 1)^T$. Die Probe zeigt, dass es auf beiden Vektoren senkrecht steht: $(1\ 1\ 1)\cdot(-1\ 0\ 1) = 0$ und $(1\ 1\ 1)\cdot(1\ -1\ 0) = 0$ ✓

## Quelle

Socher Kap. 10.1, S. 219-220 (Definition und Eigenschaften S. 219, Aufgaben S. 220-221)
```

### Kurze Notiz

Das Lernziel hiess „den Nutzen von IPsec grob beschreiben". Das Buch widmet dem Protokoll
26 Seiten, die Notiz bleibt bei rund 300 Wörtern: Problem, Nutzen, Bausteine in je einem
Satz, eine Grenze, ein Fall.

```markdown
---
LE: 3
tags: [isich/konzept, isich/le3]
---

# IPsec

IPsec ist eine Familie von Protokollen, die IP-Pakete auf der Netzwerkschicht schützt: Der Empfänger kann prüfen, woher ein Paket stammt und dass es nicht verändert wurde, und der Inhalt lässt sich verschlüsseln. Weil der Schutz unterhalb der Anwendungen sitzt, müssen diese dafür nicht angepasst werden.

## Theorie

### Welches Problem löst IPsec?

Das Internet-Protokoll IP schützt seine Pakete nicht: Die Angaben im Kopf eines Pakets sind weder verschlüsselt noch gegen gezielte Veränderung gesichert. Eine [[Firewall]] versucht, die Folgen zu begrenzen, die Ursache behebt sie nicht. IPsec setzt beim Paket selbst an und sichert es zwischen zwei Rechnern, zwischen einem Rechner und einem Gateway (zum Beispiel einem Router oder einer Firewall) oder zwischen zwei Gateways.

### Woraus besteht es?

Zwei Protokolle leisten den Schutz. AH (Authentication Header) sichert Herkunft und Unverändertheit eines Pakets, verschlüsselt aber nicht. ESP (Encapsulating Security Payload) verschlüsselt zusätzlich. Die Schlüssel und Verfahren handelt das Protokoll IKE zwischen den Partnern aus.

### Wo liegt die Grenze?

IPsec sichert Herkunft, Unverändertheit und Vertraulichkeit der Pakete. Zur Zugriffskontrolle, also zur Frage, wer worauf zugreifen darf, trägt es nichts bei, und auf jedem beteiligten Rechner muss ein Regelwerk vollständig und widerspruchsfrei formuliert sein, was die Konfiguration anspruchsvoll macht.

## Beispiel

Zwei Standorte einer Firma sind über das Internet verbunden, an jedem steht ein Gateway (eigenes Szenario). Schickt ein Rechner am ersten Standort ein Paket an einen Rechner am zweiten, verpackt das erste Gateway das ganze Paket verschlüsselt in ein neues, das nur die Adressen der beiden Gateways trägt (Tunnelmodus). Das zweite Gateway packt es aus und stellt es zu. Der Fall zeigt den Nutzen: Die Standorte kommunizieren geschützt über ein unsicheres Netz, ohne dass an Rechnern und Anwendungen etwas geändert wird. So entsteht ein [[VPN]].

## Quelle

Eckert Kap. 14.3 und 14.3.1, S. 751-755 (Einsatzgebiete S. 752, AH und ESP S. 753, Tunnelmodus S. 754)
Eckert Kap. 14.3.4, S. 764 (ESP im Tunnelmodus)
Eckert Kap. 14.3.6, S. 772-773 (Grenzen)
```

### Konzeptthema

Der Text trägt die Aussage. Skizze und Tabelle fassen zusammen. Das Lernziel hiess
„erklären und für ein Szenario begründen", deshalb führt das Beispiel eine Entscheidung
durch.

```markdown
---
LE: 3
tags: [isich/konzept, isich/le3]
---

# Firewall-Architekturen

Eine Firewall-Architektur legt fest, wie [[Paketfilter]] und [[Applikationsfilter]] im Netz angeordnet werden. Eckert stellt drei Anordnungen vor: Dual-Homed, Screened Host und Screened Subnet. Sie unterscheiden sich vor allem darin, ob zwischen externem und internem Netz noch direkter IP-Verkehr möglich ist.

## Theorie

### Dual-Homed

Der Applikationsfilter läuft auf einem Bastionsrechner, einem bewusst abgespeckten und besonders geschützten Rechner. Bei der Dual-Homed Firewall hat er zwei Netzwerkschnittstellen, eine ins interne und eine ins externe Netz, und leitet selbst keine IP-Pakete weiter. Die Netze sind damit getrennt, alles muss durch den Applikationsfilter. Davor und dahinter sitzt je ein Paketfilter.

Der Preis: Wer einen Dienst im Internet nutzen will, muss sich auf dem Bastionsrechner einloggen. Das bringt Benutzerkonten auf den Rechner, der geschützt sein soll. Eckert nennt die Architektur kaum noch üblich.

### Screened Host

Der Bastionsrechner hat nur eine Schnittstelle und steht im internen Netz. Am Übergang zum Internet sitzt ein Screening Router (ein Router mit Paketfilter), der den Verkehr von aussen filtert und an den Bastionsrechner weiterleitet. Der Router kann ausgewählte Pakete auch direkt an einen internen Rechner leiten und den Applikationsfilter umgehen. Das macht die Architektur flexibel und, falsch eingesetzt, riskant. Eckert empfiehlt sie nur, wenn das interne Netz keine sehr hohen Sicherheitsanforderungen stellt.

### Screened Subnet

Zwischen externem und internem Netz liegt ein eigenes Netzsegment, begrenzt durch je einen Screening Router. Dieses Segment heisst demilitarisierte Zone (DMZ). Darin stehen der Bastionsrechner und die Server, die von aussen erreichbar sein müssen.

    Internet -- Paketfilter -- DMZ (Bastion, WWW, DNS) -- Paketfilter -- internes Netz

IP-Pakete lassen sich so nicht mehr direkt zwischen externem und internem Netz austauschen. Wer einen Server in der DMZ übernimmt, muss für den Zugriff aufs interne Netz noch den zweiten Paketfilter überwinden.

| | Dual-Homed | Screened Host | Screened Subnet |
|---|---|---|---|
| Bastionsrechner steht | zwischen den Netzen | im internen Netz | in der DMZ |
| Paketfilter | zwei | einer | zwei |
| direkter IP-Verkehr extern zu intern | nein | möglich | nein |

## Beispiel

Eine Firma betreibt einen Webserver, der aus dem Internet erreichbar sein muss, und ein internes Netz mit hohen Sicherheitsanforderungen (eigenes Szenario). Die Wahl fällt auf das Screened Subnet: Der Webserver steht in der DMZ, und wer ihn übernimmt, steht noch nicht im internen Netz. Der Screened Host scheidet aus, weil dort ausgewählte Pakete direkt ins interne Netz gelangen und Eckert ihn nur ohne sehr hohe Anforderungen empfiehlt. Der Fall zeigt, wie die Wahl begründet wird: von der Anforderung (Server erreichbar, internes Netz geschützt) zur Architektur, die genau das trennt.

## Quelle

Eckert Kap. 14.1.5, S. 734-738 (Dual-Homed S. 735-736, Screened Host S. 736-737, Screened Subnet und DMZ S. 737-738)
```
