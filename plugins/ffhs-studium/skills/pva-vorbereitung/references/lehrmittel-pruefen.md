# Lehrmittel prüfen

Wie man aus einem Lehrbuch-PDF echte Kapitelnummern gewinnt und die Lernziele dagegen
abgleicht. Dieser Schritt entscheidet über den Wert der ganzen Arbeit: Eine falsche
Kapitelnummer kostet die Person Zeit, eine übersehene Lücke kostet sie eine Stunde.

## Text aus dem PDF holen

`pdftotext` ist meist vorhanden, auch wenn andere Poppler-Werkzeuge fehlen. Erst prüfen:

```bash
for c in pdftotext pdftoppm mutool qpdf; do printf "%-10s " "$c"; command -v $c >/dev/null && echo ok || echo "-"; done
```

Dann extrahieren. `-layout` erhält die Spaltenstruktur, `-enc UTF-8` verhindert kaputte
Umlaute:

```bash
pdftotext -layout -enc UTF-8 "Lehrbuch.pdf" /tmp/buch.txt
wc -l /tmp/buch.txt
```

Ohne `-enc UTF-8` erscheint `Einf�hrung` statt `Einführung` - dann neu extrahieren, nicht
raten.

Der Read-Tool kann PDFs nur rendern, wenn `pdftoppm` installiert ist. Bei einem
Textlehrbuch ist `pdftotext` ohnehin die bessere Wahl: durchsuchbar, zitierfähig,
sparsam im Kontext.

## Inhaltsverzeichnis finden

```bash
grep -n "Analytische Geometrie" /tmp/buch.txt | head -20
```

Die ersten Treffer mit Punktführung (`. . . . 193`) sind das Inhaltsverzeichnis, spätere
sind Kolumnentitel im Fliesstext. Das komplette Verzeichnis dann als Block lesen:

```bash
sed -n '130,240p' /tmp/buch.txt | grep -v '^\s*$'
```

Daraus die Kapitelnummern **und** Seitenzahlen für alle Lerneinheiten des Moduls
übernehmen, nicht nur für den aktuellen Block. Das kostet fünf Minuten und füllt die
Kapitellandkarte für das ganze Semester.

## Kapitelversatz erkennen

**Immer prüfen, ob Kapitelnummer und Kapiteltitel des Auftrags zusammenpassen.**

Typischer Fall: Der Auftrag nennt „Kapitel 8: Analytische Geometrie in der Ebene", im Buch
trägt Kapitel 8 den Titel „Wahrscheinlichkeitsrechnung" und die analytische Geometrie steht
in Kapitel 9. Ursache steht meist im Vorwort:

```bash
grep -n -A3 "Vorwort zur" /tmp/buch.txt | head -20
```

> „In der zweiten Auflage wurde das Buch erweitert um Kapitel 8 zur Wahrscheinlichkeitsrechnung."

Alles danach rutscht um eine Nummer. In diesem Fall:

- die **Buchnummern** verwenden, sie sind die überprüfbaren
- den Versatz in der Vorbereitungsnotiz und in der Kapitellandkarte als Callout benennen
- die Ursache nennen, damit die Person es einordnen kann

Stimmen Nummer und Titel überein, ist nichts zu tun - aber geprüft haben muss man es.

## Kapitel lesen

Die Kapitelgrenzen im Fliesstext bestimmen und den Block lesen:

```bash
grep -n "Analytische Geometrie in der Ebene\|Lineare und affine Abbildungen" /tmp/buch.txt | awk -F: '$1>9000'
sed -n '9389,9800p' /tmp/buch.txt
```

In Abschnitten von 400 bis 500 Zeilen lesen. Formeln kommen aus `-layout` zerpflückt heraus
(`---vv--- = 1-- 3`); der Zusammenhang bleibt trotzdem erkennbar. Beim Übertragen in LaTeX
die Formel aus der Struktur rekonstruieren, nicht aus dem Zeichensalat abtippen - und im
Zweifel die Stelle nochmals gezielt anschauen.

Mitschreiben: Definitionen, Sätze mit Voraussetzung, Rechenregeln, die durchgerechneten
Beispiele **mit ihren Zahlen**, und das Anwendungsproblem, das das Kapitel motiviert.

## Lernziele abgleichen

Für jedes Lernziel des Auftrags: Steht das Verfahren im gelesenen Kapitel?

Gezielt gegenprüfen, statt sich auf den Leseeindruck zu verlassen:

```bash
for t in "Eigenwert" "Orthogonalbasis" "Gram-Schmidt" "QR-Zerlegung" "Hamming"; do
  printf "%-20s %s\n" "$t" "$(grep -ci "$t" /tmp/buch.txt)"
done
```

Null Treffer im **ganzen** Buch ist eine belastbare Aussage - deutlich stärker als „habe ich
im Kapitel nicht gesehen". Solche Befunde gehören in die Kapitellandkarte, weil sie für das
ganze Semester gelten:

> Volltextsuche ergibt **0 Treffer** für Eigenwert, Orthogonalbasis, QR-Zerlegung.
> Für LE5 und LE6 ist Teschl das einzige Lehrmittel.

Ein Treffer sagt umgekehrt noch nicht, dass das Thema behandelt wird - die Fundstelle
ansehen. Ein Begriff kann in einer Aufgabe vorkommen, ohne im Text hergeleitet zu sein. Das
ist ein Unterschied, der in der Notiz benannt gehört:

> Schnittgerade zweier Ebenen: nur als Aufgabe 10.3/3 im Spezialfall, kein Verfahren im Text.

## Sachwortverzeichnis nutzen

Der zuverlässigste Beleg für eine Seitenzahl. Es steht am Buchende und liefert Nummern, die
man nicht rekonstruieren muss:

```bash
grep -n "Hamming" /tmp/buch.txt | tail -10
```

```
Hamming-Abstand 308
Hamming-Code 316
Hamming-Matrix 316
```

Wenn Inhaltsverzeichnis und Sachwortverzeichnis übereinstimmen, ist die Angabe sicher.

## Was in die Notizen darf

| Befund | Notiz |
|---|---|
| Im Inhaltsverzeichnis gefunden | Kapitelnummer und Seite eintragen |
| Im Sachwortverzeichnis gefunden | Seite eintragen, Kapitel dazu |
| Im Fliesstext gelesen | Theorie übernehmen, Kapitel als Quelle |
| Nur in einer Aufgabe erwähnt | eintragen **mit** dem Hinweis, dass kein Verfahren im Text steht |
| Null Treffer | `## Offen` mit Checkbox und Suchrichtung |
| Nicht nachgeschlagen | Feld leer lassen und im Chat sagen |

Die letzte Zeile ist die wichtigste: **Eine leere Zelle ist besser als eine geratene
Nummer.** In einer Open-Book-Prüfung kostet eine falsche Seitenzahl mehr Zeit als eine
fehlende.

## Aufräumen

Die extrahierte Textdatei gehört ins Scratchpad-Verzeichnis, nicht in den Vault. Sie ist
ein Arbeitsmittel, kein Ergebnis.
