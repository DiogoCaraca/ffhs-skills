# Dateiformate

Verbindlicher Aufbau je Dateityp. Diese Formate sind das Ergebnis einer Aufräumaktion, bei
der ein Vault von 3400 auf 2100 Zeilen geschrumpft wurde, weil er unbenutzbar geworden war.
Die weggelassenen Rubriken fehlen mit Absicht.

## Grundsatz

> Beim Öffnen einer Datei muss in zwei Sekunden klar sein, wo was steht.

Das erreicht man durch **immer gleiche Abschnitte in immer gleicher Reihenfolge**, nicht
durch gute Überschriften. Wenn jede Konzeptnotiz denselben Aufbau hat, muss man sie nicht
lesen, um sich zurechtzufinden.

## Bestehender Vault

Die Formate gelten für neue Vaults und für alles, was ein Vault offen lässt. Hat ein Vault
schon eine eigene Schreibweise für Tags, Überschriften, Tabellenspalten oder Zeitangaben,
folgen neue Dateien dem Vault: Einheitlichkeit im Vault zählt mehr als Übereinstimmung mit
diesem Dokument. Bestehende Tabellen (Lesetabelle, Kapitellandkarte, Vergleichstabellen)
werden ergänzt, nicht umgebaut. Eine Spalte oder ein Abschnitt, den dieses Dokument
vorsieht und der noch fehlt, darf angefügt werden, etwa die Spalte `Gewicht`. Was am Format
abweicht und stört, gehört in den Bericht, nicht in einen stillen Umbau. Ein sachlicher
Fehler in einer bestehenden Datei (eine falsche Kapitelangabe) wird berichtigt und im
Bericht genannt.

---

## Konzeptnotiz

Der wichtigste Dateityp, und der einzige, in dem erklärt wird. Aufbau, Schreibregeln und
Muster stehen beim Skill, der sie schreibt: `leseauftrag/references/konzeptnotiz.md`.

Kurzfassung des Aufbaus, damit die Hüllen stimmen: Kopf direkt unter der H1 (was es ist,
wozu es dient), dann `## Theorie`, `## Beispiel`, `## Quelle`. `## Offen` nur, wenn die
Person selbst etwas klären muss, vor `## Quelle`.

Braucht ein Begriff eine Abgrenzung zu Nachbarbegriffen, gehört die als **eine Tabelle in
die LE-Übersicht**, wo alle verwandten Begriffe nebeneinanderstehen - nicht in jede
einzelne Notiz.

---

## LE-Übersicht

Der Einstieg in eine Lerneinheit. Beantwortet: Was muss ich können, worum geht es und wie
hängt es zusammen, welche Notizen lese ich in welcher Reihenfolge, wo steht es im Buch.

```markdown
---
LE: 1
thema: Vektorgeometrie in der Ebene und im Raum
tags: [linalg/le1]
---

# LE1 - Vektorgeometrie in der Ebene und im Raum

Vorbereitung: [[PVA1 - Vorbereitung]]

## Lernziele

- [ ] Geradengleichungen in Parameterform, in der Ebene und im Raum
  Notizen: [[Parameterform einer Geraden]], [[Parameterform einer Ebene]]
- [ ] Schnittpunkte zweier Geraden, Durchstosspunkt einer Geraden durch eine Ebene
  Noch offen.

## Überblick

Die Lerneinheit beschreibt Geometrie mit Zahlen. Ein [[Vektor]] ist ein Pfeil mit Richtung und Länge, seine Länge misst die [[Norm eines Vektors]]. Zwei Produkte machen aus zwei Vektoren eine Aussage über ihre Lage zueinander: Das [[Skalarprodukt]] liefert eine Zahl und damit den Winkel, das [[Kreuzprodukt]] liefert einen Vektor, der auf beiden senkrecht steht.

Mit diesen Werkzeugen lassen sich Geraden und Ebenen als Gleichungen schreiben ([[Parameterform einer Geraden]], [[Parameterform einer Ebene]]). Daraus folgen die Aufgaben der Lernziele: Schnittpunkte berechnen und [[Abstandsprobleme]] lösen.

Vorausgesetzt: Sinus und Kosinus am rechtwinkligen Dreieck (Schulstoff, nicht im Socher).

## Konzepte

**Grundlagen**
[[Vektor]] · [[Norm eines Vektors]]

**Noch ohne Notiz**
[[Lagebeziehungen]]

**Die vier Produkte**

| | Eingabe | Ergebnis | Wo | Misst |
|---|---|---|---|---|
| [[Skalarprodukt]] | 2 Vektoren | Zahl | jedes $\mathbb{R}^n$ | Winkel, Projektion |
| [[Kreuzprodukt]] | 2 Vektoren | **Vektor** | nur $\mathbb{R}^3$ | Fläche, Normalenrichtung |

## Merksatz

$$\cos\varphi = \frac{v \cdot w}{\|v\|\,\|w\|} \qquad \sin\varphi = \frac{\det(v,w)}{\|v\|\,\|w\|}$$

> **Kosinus liefert den Wert des Winkels, Sinus die Orientierung.**

## Lehrmittel

**Socher ist hier das primäre Buch.** Der Auftrag nennt Kapitel 8 und 9, im Buch sind es **9 und 10**.

| Thema | Socher | Seite |
|---|---|---|
| Vektoren in der Ebene | 9.2 | 194 |
| Winkel, Skalarprodukt, Determinante | 9.3 | 202 |

### Lücken im Lehrmittel

- Schnittgerade zweier Ebenen: im Socher nur als Aufgabe 10.3/3, kein Verfahren im Text. Suchrichtung: Teschl Bd. 1, Kap. 9.
- Abstand zweier Geraden im Raum: 0 Treffer im Socher.
```

| Abschnitt | Inhalt |
|---|---|
| `## Lernziele` | wörtlich aus dem Auftrag, als Checkliste. Ein Lernziel, das nur ein Leseauftrag nennt, steht mit Vermerk in derselben Liste. Sobald Notizen da sind, steht unter jedem Lernziel eingerückt, welche Notizen es abdecken oder dass es noch offen ist. |
| `## Überblick` | Der rote Faden in ein bis zwei Absätzen Klartext, für jemanden, der den Stoff noch nicht kennt: worum es geht, welches Problem die Lerneinheit löst, wie die Konzepte aufeinander aufbauen. Jede Konzeptnotiz ist an der Stelle verlinkt, an der sie im Gedankengang vorkommt. Das ergibt die Lesereihenfolge. Greift der Gedankengang auf eine spätere Notiz vor, steht sie als eigene Zeile „Lesereihenfolge" darunter. Dann die Zeile „Vorausgesetzt": was das Kapitel aus früheren Kapiteln als bekannt annimmt, in wenigen Sätzen mit Fundstelle. |
| `## Konzepte` | die Notizen gruppiert, dazu die Tabellen, die mehrere Begriffe nebeneinanderstellen: Vergleiche (drei Verfahren nach denselben Kriterien) und Zuordnungen (welche Lage verlangt welches Verfahren). Unter „Noch ohne Notiz" die Begriffe, die ein Lernziel verlangt und die noch keine Notiz haben. |
| `## Merksatz` | optional, nur wenn das Kapitel wirklich eine tragende Idee hat: eine Aussage des Buchs aus dem Kern-Stoff, mit Seite, ohne eigene Übertragung. Höchstens einer pro Lerneinheit, sonst ist es keiner. |
| `## Lehrmittel` | Fundstellen mit Kapitel und Seite. Stoff, den ein Lernziel braucht und der ausserhalb der genannten Kapitel steht, als Zeile mit dem Vermerk *(ausserhalb Auftrag)*. Darunter `### Lücken im Lehrmittel`, wenn es welche gibt: je Lernziel ohne Fundstelle ein Satz mit Suchrichtung. Trefferzahlen und Suchbelege stehen in der Kapitellandkarte. |

Der Überblick erklärt nichts im Detail, das tun die Konzeptnotizen. Er sagt, wie die Teile
zusammengehören, damit man weiss, womit man anfängt und warum das Nächste folgt. Ein
Absatz ist eine Zeile.

Umfang rund 40 bis 100 Zeilen. Für noch nicht bearbeitete Lerneinheiten reichen Lernziele
aus dem Modulplan, Konzeptliste und Lehrmitteltabelle, der Überblick entsteht mit dem
ersten Leseauftrag und deckt ab, was gelesen wurde.

---

## PVA-Dateien

**Drei** Dateien pro Präsenzveranstaltung, in drei Phasenordnern. Sie sind so lang, wie
Aufträge und Lesetabelle es verlangen, und enthalten sonst nichts.

```
03_PVA/PVA1/
├── 01_Vorbereitung/PVA1 - Vorbereitung.md
├── 02_PVA/PVA1 - Praesenznotizen.md
└── 03_Nachbereitung/PVA1 - Nachbereitung.md
```

**Keine `PVAx - Uebersicht.md`.** Ein Hub, der nur Termin und drei Links auf die
Nachbarordner trägt, ist ein Klick ohne Inhalt - die Struktur einer PVA ist
selbsterklärend. Termin und Fragen stehen in den Präsenznotizen, die Lerneinheit im
Frontmatter.

**Diese Ordner sind Arbeitsablagen.** Sie tragen, was **abzuarbeiten** ist. Lernziele,
Theorie und Lehrmittel-Lücken stehen in der LE-Übersicht und den Konzeptnotizen - dort
sucht man sie im Semester und vor der Prüfung. Eine PVA-Datei, die man nach der Präsenz
noch braucht, ist falsch geschnitten.

### PVAx - Vorbereitung

```markdown
---
pva: 1
phase: Vorbereitung
LE: 1
tags: [<modulcode>/pva, <modulcode>/pva1]
---

# PVA1 - Vorbereitung

Lernziele und Theorie: [[LE1 - Uebersicht]]

## Aufträge

- [x] Python installieren (Anaconda mit Jupyter Notebook)
- [x] Einführungsvideos anschauen
- [ ] Theorielektüre Socher, siehe unten
- [ ] Kontrollfragen lösen
- [ ] Offene Fragen im Forum diskutieren

## Lektüre Socher

Der Auftrag nennt Kapitel 8 und 9. **Im Buch sind es 9 und 10** - die 2. Auflage hat ein
Kapitel zur Wahrscheinlichkeitsrechnung eingeschoben.

Die Konzeptnotizen fassen zusammen, was als Kern oder Überblick markiert ist.

| Kapitel | Titel | Seiten | Gewicht | |
|---|---|---|---|---|
| 9.1 | Einführung | 193 | überspringen | [ ] |
| 9.2 | Vektoren | 194-201 | Kern | [ ] |
| 9.3 | Winkel, Skalarprodukt und Determinante | 202-205 | Kern | [ ] |
| 9.3 | darin: Herleitung der Additionstheoreme | 204 | überspringen | [ ] |

## Bearbeitung
```

| Abschnitt | Inhalt |
|---|---|
| Kopfzeile | ein Link auf die LE-Übersicht - dort stehen die Lernziele |
| `## Aufträge` | die Handlungsschritte des Auftrags als Checkliste, Erledigtes abgehakt |
| `## Lektüre <Buch>` | Kapiteltabelle mit Häkchenspalte, darüber der Kapitelversatz falls vorhanden und der Satz, dass die Notizen Kern und Überblick zusammenfassen. Spalte `Gewicht` aus dem Lernziel-Abgleich des Skills `leseauftrag`: **Kern** (lesen lohnt sich, die Notizen erklären es), **Überblick** (überfliegen genügt), **überspringen** (dient keinem Lernziel). Wechselt das Gewicht innerhalb eines Kapitels, bekommt der abweichende Teil eine eigene Zeile „darin: ...". Kapitel, die nicht abgeglichen wurden, bleiben in der Spalte leer. Stellen ausserhalb der genannten Kapitel, die ein Auftrag verlangt, stehen als eigene Zeilen am Ende, mit dem Vermerk *(ausserhalb Auftrag)*. |
| `## Bearbeitung` | Platz für Notizen beim Abarbeiten. Verlangt ein Auftrag ein schriftliches Ergebnis (Begriffsliste, Szenarien), bekommt es hier eine leere `###`-Überschrift, auf die der Auftrag verlinkt. |

**Nicht enthalten:** Lernziele (stehen in der LE-Übersicht), Lehrmittel-Lücken (ebenfalls
dort), Aufwandsangaben (ausser die bisherigen Vorbereitungsnotizen des Vaults führen sie),
Hinweise auf Kurztests oder Notengewichte, organisatorische Fragenlisten.

Eine Ausnahme: Verlangt ein Auftrag Stoff, der nicht in der Lektüre steht, bekommt er
einen Hinweis, wo der Stoff zu finden ist („Stoff dazu: [[Netzwerkbedrohungen]]" oder
„Stoff dazu: Kap. 3.3.1, siehe LE-Übersicht").

### PVAx - Praesenznotizen

Fast leer - hier wird während der Präsenz getippt. `datum:` im Frontmatter trägt den Termin.

```markdown
---
pva: 1
phase: PVA
LE: 1
datum: 
tags: [<modulcode>/pva, <modulcode>/pva1]
---

# PVA1 - Präsenznotizen

## Fragen für die Präsenz

- [ ] 

## Mitschrift



## Beispiele von der Tafel



## Für die Nachbereitung

- [ ] 
```

*Fragen für die Präsenz* steht zuoberst, weil man sie vor dem Termin sammelt und zu Beginn
braucht. Der Skill `leseauftrag` trägt dort die Lücken ein, die weder Buch noch Auftrag
schliessen (etwa „Gegenmassnahme gegen Portscans: steht nicht im Lehrmittel"). Die
Leerzeilen unter den Überschriften sind Absicht: Der Cursor landet direkt an der richtigen
Stelle.

### PVAx - Nachbereitung

Zwei Abschnitte: `## Aufträge` mit leerer Checkbox, `## Bearbeitung` leer. Nennt der Auftrag
nach der Präsenz konkrete Schritte (Abgabe, Aufgabenserie), kommen die als Checkliste hinein.

---

## Python-Cheatsheet

Eine Datei für das ganze Modul, nach Lerneinheit gegliedert. Echter, lauffähiger Code -
keine Funktionsnamen-Tabelle, keine Platzhalter.

```markdown
## LE1 - Vektorgeometrie

```python
v @ w                             # Skalarprodukt
np.linalg.det(np.array([v, w]))   # Determinante 2x2
np.cross(v, w)                    # Kreuzprodukt (nur 3D)
```

**Winkel** - `np.clip` ist Pflicht, sonst bricht `arccos` bei Rundung ab:

```python
cos = v @ w / (np.linalg.norm(v) * np.linalg.norm(w))
phi = np.degrees(np.arccos(np.clip(cos, -1, 1)))
```
```

Fallen als Kommentar hinter der Zeile oder als kurzer Fettsatz über dem Block. Am Ende ein
Abschnitt `## Die drei Fallen` mit den teuersten Fehlern des Moduls.

---

## Kapitellandkarte

Pro Lehrmittel eine Datei in `07_Quellen`. Enthält:

1. Bibliografische Zeile
2. **Kapitelversatz** als Callout, nur falls Auftrag und Buch abweichen
3. **Abdeckung**: welche Lerneinheiten das Buch behandelt und welche nicht, mit der
   Suchmethode belegt (0 Treffer für Begriff X). „Nicht im Buch" und „im Buch, aber
   ausserhalb der Leseaufträge" sind zwei verschiedene Befunde.
4. Tabelle LE / Thema / Kapitel / Seite
5. **Nicht im Buch**: Liste der Lernziele ohne Fundstelle
6. Eigenheiten (Programmiersprache des Buchs, wo die Lösungen liegen, Druckfehler und im PDF
   verstümmelte Stellen mit Seite)

Nur eintragen, was tatsächlich im Inhalts- oder Sachwortverzeichnis gefunden wurde.

---

## Frontmatter

Knapp halten. Was nicht gefiltert oder sortiert wird, gehört nicht hinein.

```yaml
---
LE: 1
tags: [linalg/konzept, linalg/le1]
---
```

Bei PVA-Dateien zusätzlich `pva:` und `phase:` (`Vorbereitung` / `PVA` / `Nachbereitung`).

**Weglassen:** `status:`, `kompetenzziel:`, `typ:`, `quelle:` - das erzeugt Pflegeaufwand
ohne Nutzen. Fortschritt wird über die Checkboxen der Lernziele sichtbar.

---

## Dateinamen

Reines ASCII: `A-Z a-z 0-9 Leerzeichen - _ .`

| Verboten | Ersetzen durch |
|---|---|
| `ä ö ü` | `ae oe ue` |
| `ß` | `ss` |
| `–` `—` | `-` |
| Emoji, `→`, `…` | ausschreiben |

**Im Dateiinhalt gilt das nicht** - Überschriften und Text tragen korrektes Deutsch. Die
Datei heisst `LE1 - Uebersicht.md`, die H1 darin lautet `# LE1 - Übersicht`.

Jeder Dateiname im Vault muss **eindeutig** sein, weil Obsidian Wikilinks über den
Dateinamen auflöst, nicht über den Pfad. Deshalb `_Ueber 02_Konzepte.md` statt
`_Ueber diesen Ordner.md`.
