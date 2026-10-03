# Lehrmittel prüfen

Wie man aus einem Lehrbuch-PDF echte Kapitelnummern und Seitenzahlen gewinnt, das Kapitel
liest und die Lernziele dagegen abgleicht. Dieser Schritt entscheidet über den Wert der
ganzen Arbeit: Eine falsche Kapitelnummer kostet die Person Zeit, eine übersehene Lücke
kostet sie eine Stunde.

Das Skript `scripts/buchseiten.py` nimmt die wiederkehrende Handarbeit ab: Text
extrahieren, Treffer zählen, zu jedem Treffer die gedruckte Seitenzahl nennen, eine Seite
als Bild rendern.

## Text aus dem PDF holen

```bash
python <skill-pfad>/scripts/buchseiten.py text "Lehrbuch.pdf" <scratch>/buch.txt
```

Das ruft `pdftotext -layout -enc UTF-8` auf. `pdftotext` gehört zu Poppler und ist unter
Windows auch in Git enthalten. Unter Windows ist `python` im PATH oft nur ein Platzhalter
des Microsoft Store, dann liegt meist eine Anaconda-Installation daneben
(`~/anaconda3/python.exe`).

Die Textdatei gehört ins Scratchpad-Verzeichnis, nicht in den Vault. Sie ist ein
Arbeitsmittel, kein Ergebnis.

Aus der Titelei Auflage und Erscheinungsjahr notieren und mit der Angabe im Modulplan
vergleichen (Auflage, ISBN). Seitenzahlen gelten nur für die vorliegende Auflage: Weicht
sie ab, steht das in der Kapitellandkarte und im Bericht.

Bei einem Textlehrbuch ist die Textdatei die beste Grundlage: durchsuchbar, zitierfähig,
sparsam im Kontext. Ihre Schwächen muss man kennen:

- Marginalien (Stichworte am Rand) ragen in die Zeilen hinein.
- Abbildungen fehlen, nur ihre Beschriftungen sind da.
- **Zeichen gehen verloren.** Aus „≠ 25" wird „= 25", Minuszeichen und Indizes
  verschwinden, Matrizen und Summenformeln kommen zerpflückt heraus. Eine Regel oder
  Formel kann sich dadurch umkehren.

Deshalb gilt: Formeln, Tabellen mit Zahlen, Regeln und jede Stelle, die verstümmelt
aussieht, am Seitenbild prüfen (siehe unten). Das ist kein Sonderfall für Mathebücher.

## Inhaltsverzeichnis finden

```bash
python <skill-pfad>/scripts/buchseiten.py suche <scratch>/buch.txt "Analytische Geometrie"
```

Die ersten Treffer mit Punktführung (`. . . . 193`) sind das Inhaltsverzeichnis, spätere
sind Kolumnentitel und Überschriften im Fliesstext. Das Verzeichnis dann als Block lesen
(Read-Tool mit Zeilenbereich).

Bei manchen Büchern zerlegt die Extraktion das Verzeichnis in getrennte Spalten: Die
Kapitelnummern stehen in anderen Zeilen als Titel und Seiten. Dann das Verzeichnis am
Seitenbild lesen (`bild` mit `--pdf`, siehe unten) oder die Zuordnung über die
Überschriften im Fliesstext bestätigen, die das Skript mit Buchseite ausgibt.

Ist die Kapitellandkarte des Buchs noch leer, Kapitelnummern und Seiten für alle
Lerneinheiten des Moduls übernehmen, nicht nur für den aktuellen Block. Das kostet fünf
Minuten und füllt sie für das Semester. Ist sie schon gefüllt, nur den aktuellen Block
nachtragen.

## Kapitelversatz erkennen

**Immer prüfen, ob Kapitelnummer und Kapiteltitel des Auftrags zusammenpassen.**

Typischer Fall: Der Auftrag nennt „Kapitel 8: Analytische Geometrie in der Ebene", im Buch
trägt Kapitel 8 den Titel „Wahrscheinlichkeitsrechnung" und die analytische Geometrie steht
in Kapitel 9. Die Ursache steht meist im Vorwort (Suche nach „Vorwort zur"):

> „In der zweiten Auflage wurde das Buch erweitert um Kapitel 8 zur Wahrscheinlichkeitsrechnung."

Alles danach rutscht um eine Nummer. In diesem Fall:

- die **Buchnummern** verwenden, sie sind die überprüfbaren
- den Versatz in der Vorbereitungsnotiz und in der Kapitellandkarte benennen
- die Ursache nennen, damit die Person es einordnen kann

Stimmen Nummer und Titel überein, ist nichts zu tun. Geprüft haben muss man es.

## Kapitel lesen

```bash
python <skill-pfad>/scripts/buchseiten.py seite <scratch>/buch.txt 716 740
```

gibt die Buchseiten 716 bis 740 mit den Zeilennummern der Textdatei aus. Bequemer zum
Lesen ist das Read-Tool mit diesen Zeilennummern, in Abschnitten von 400 bis 500 Zeilen.
Vollständig lesen, nichts überspringen: Was man nicht gelesen hat, kann man nicht
gewichten.

Mitschreiben, je mit Seite: Definitionen, Sätze mit Voraussetzung, Rechenregeln, die
Begründungen des Autors, seine Folgerungen und Empfehlungen, die durchgeführten Beispiele
mit ihren Zahlen und das Problem, das das Kapitel motiviert.

## Am Seitenbild prüfen

```bash
python <skill-pfad>/scripts/buchseiten.py bild "Lehrbuch.pdf" <scratch>/buch.txt 722 <scratch>/seiten
```

rendert Buchseite 722 als `buchseite-722.png`. Das Bild mit dem Read-Tool ansehen. Mit
`--pdf` am Ende ist die Zahl eine PDF-Seite, das braucht es für römisch gezählte Seiten
wie das Inhaltsverzeichnis. Braucht `pdftoppm` (Poppler). Fehlt es, die Stelle in der
Notiz als ungeprüft kennzeichnen.

Am Seitenbild prüfen, bevor etwas in eine Notiz kommt:

- jede Formel und jedes Rechenbeispiel
- Tabellen mit Zahlen, Vergleichszeichen oder Regeln
- Abbildungen, auf die sich die Erklärung stützt
- Stellen, die im Text verstümmelt aussehen

Stellt sich eine Stelle als Druckfehler des Buchs heraus, steht in der Notiz die
berichtigte Form, der Vermerk dazu in ihrer Quellenzeile, und die Kapitellandkarte sammelt
den Fehler unter Eigenheiten.

## Lernziele abgleichen

Für jedes Lernziel des Auftrags: Steht der Stoff im gelesenen Kapitel? Gezielt
gegenprüfen, statt sich auf den Leseeindruck zu verlassen:

```bash
python <skill-pfad>/scripts/buchseiten.py suche <scratch>/buch.txt Eigenwert Orthogonalbasis "QR-Zerlegung" Hamming
```

Das Skript nennt je Begriff die Trefferzahl und die Buchseiten. Es ignoriert Gross- und
Kleinschreibung, Ligaturen und Bindestriche („Hashfunktion" findet „Hash-Funktion", „Single
Sign On" findet „Single-Sign-On").
Wortformen und Synonyme sucht es nicht mit: „Härtung" und „Hardening" sind zwei Suchen.
Vor einem Null-Befund den Wortstamm und den Namen probieren, unter dem das Buch die Sache
führt („Netzwerksegmentierung" steht bei Eckert unter „Partitionierung").

Null Treffer im **ganzen** Buch ist eine belastbare Aussage, deutlich stärker als „habe
ich im Kapitel nicht gesehen". Solche Befunde gehören in die Kapitellandkarte, weil sie
für das ganze Semester gelten:

> Volltextsuche ergibt **0 Treffer** für Eigenwert, Orthogonalbasis, QR-Zerlegung.
> Für LE5 und LE6 ist Teschl das einzige Lehrmittel.

Ein Treffer sagt umgekehrt noch nicht, dass das Thema behandelt wird. Die Fundstelle
ansehen. Ein Begriff kann in einer Aufgabe vorkommen, ohne im Text hergeleitet zu sein:

> Schnittgerade zweier Ebenen: nur als Aufgabe 10.3/3 im Spezialfall, kein Verfahren im Text.

Steht der Stoff zu einem Lernziel in einem anderen Kapitel desselben Buchs, ist das keine
Lücke, sondern eine Fundstelle ausserhalb der genannten Kapitel. Was damit geschieht,
regelt Schritt 3 im Skill.

## Sachwortverzeichnis nutzen

Der zuverlässigste Beleg für eine Seitenzahl. Es steht am Buchende, die Treffer mit den
höchsten Seitenzahlen einer Suche sind meist die Einträge:

```
Hamming-Abstand 308
Hamming-Code 316
```

Wenn Inhaltsverzeichnis und Sachwortverzeichnis übereinstimmen, ist die Angabe sicher.

## Was in die Notizen darf

| Befund | Notiz |
|---|---|
| Im Inhaltsverzeichnis gefunden | Kapitelnummer und Seite eintragen |
| Im Sachwortverzeichnis gefunden | Seite eintragen, Kapitel dazu |
| Im Fliesstext gelesen | Theorie übernehmen, Kapitel und Seite als Quelle |
| Nur in einer Aufgabe erwähnt | eintragen **mit** dem Hinweis, dass kein Verfahren im Text steht |
| Null Treffer | Lücke in der LE-Übersicht, mit Suchrichtung |
| Nicht nachgeschlagen | Feld leer lassen und im Chat sagen |

Die letzte Zeile ist die wichtigste: **Eine leere Zelle ist besser als eine geratene
Nummer.** In einer Open-Book-Prüfung kostet eine falsche Seitenzahl mehr Zeit als eine
fehlende.
