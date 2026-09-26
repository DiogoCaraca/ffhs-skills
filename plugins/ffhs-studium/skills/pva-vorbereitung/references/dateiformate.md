# Dateiformate

Verbindlicher Aufbau je Dateityp. Diese Formate sind das Ergebnis einer Aufräumaktion, bei
der ein Vault von 3400 auf 2100 Zeilen geschrumpft wurde, weil er unbenutzbar geworden war.
Die weggelassenen Rubriken fehlen mit Absicht.

## Grundsatz

> Beim Öffnen einer Datei muss in zwei Sekunden klar sein, wo was steht.

Das erreicht man durch **immer gleiche Abschnitte in immer gleicher Reihenfolge**, nicht
durch gute Überschriften. Wenn jede Konzeptnotiz denselben Aufbau hat, muss man sie nicht
lesen, um sich zurechtzufinden.

---

## Konzeptnotiz

Der wichtigste Dateityp. **Genau vier Abschnitte.**

```markdown
---
LE: 1
tags: [linalg/konzept, linalg/le1]
---

# Kreuzprodukt (Vektorprodukt)

Zwei Vektoren des **Raums** rein, ein **Vektor** raus:

$$v \times w = \begin{pmatrix} v_y w_z - v_z w_y \\ v_z w_x - v_x w_z \\ v_x w_y - v_y w_x \end{pmatrix}$$

Merkstruktur: In jeder Zeile fehlt der eigene Index, die anderen kommen über Kreuz.

## Theorie

### Eigenschaften

| | Eigenschaft | Bedeutung |
|---|---|---|
| a | $v \times w = -(w \times v)$ | nicht kommutativ |
| d | orthogonal zu $v$ und $w$ | daraus der [[Normalenvektor]] |

### Flächen

$$A_{\text{Parallelogramm}} = \|v \times w\| \qquad A_{\text{Dreieck}} = \tfrac{1}{2}\|v \times w\|$$

### Achtung

- Existiert **nur im $\mathbb{R}^3$**
- Nicht kommutativ, nicht assoziativ

## Beispiel

$(-1\ 0\ 1)^T \times (1\ -1\ 0)^T$:

$$\begin{aligned}
\text{1. Komponente} &= 0\cdot0 - 1\cdot(-1) = 1\\
\text{2. Komponente} &= 1\cdot1 - (-1)\cdot0 = 1\\
\text{3. Komponente} &= (-1)(-1) - 0\cdot1 = 1
\end{aligned}$$

Ergebnis $(1\ 1\ 1)^T$.

**Probe:** $(1\ 1\ 1)\cdot(-1\ 0\ 1) = 0$ und $(1\ 1\ 1)\cdot(1\ -1\ 0) = 0$ ✓

## Quelle

Socher Kap. 10.1, S. 219-220
Teschl Bd. 1, Definition 13.17
```

**Regeln**

| | |
|---|---|
| Kopf | Ein bis zwei Sätze plus die Formel. Kein eigener Abschnitt, direkt unter der H1. |
| `## Theorie` | Formeln, Tabellen, nummerierte Verfahren. `###`-Unterabschnitte erlaubt. |
| `## Beispiel` | Echte Zahlen, gerechnet. Mehrere Beispiele erlaubt, mit fettem Vorspann. |
| `## Quelle` | Kapitel und Seite, eine Zeile pro Buch. Keine Aufzählungspunkte nötig. |
| `## Offen` | **Nur** wenn etwas ungeklärt ist. Mit Checkbox. Steht vor `## Quelle`. |
| Umfang | 50-85 Zeilen |

**Erlaubt innerhalb von `## Theorie`:** ein kurzer `### Achtung`-Block mit zwei bis drei
Stichpunkten für echte Fallstricke (Definitionslücken, Vorzeichenfallen, Gültigkeitsbereich).
Das ist Theorie, keine Didaktik.

**Nicht erlaubt:** `## Warum gibt es das?`, `## Grenzen / Was es NICHT löst`,
`## Abgrenzung zu ähnlichen Begriffen`, `## In numpy`, `## Prüfungsfrage in eigenen Worten`,
`## Selbstcheck`, Callout-Blöcke mit Lerntipps.

Braucht ein Begriff eine Abgrenzung zu Nachbarbegriffen, gehört die als **eine Tabelle in
die LE-Übersicht**, wo alle verwandten Begriffe nebeneinanderstehen - nicht in jede
einzelne Notiz.

---

## LE-Übersicht

Der Inhalts-Hub einer Lerneinheit. Beantwortet: Was muss ich können, welche Notizen gehören
dazu, wo steht es im Buch.

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
- [ ] Schnittpunkte zweier Geraden, Durchstosspunkt einer Geraden durch eine Ebene

## Konzepte

**Grundlagen**
[[Vektor]] · [[Norm eines Vektors]]

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

Nicht im Socher: Schnittgerade zweier Ebenen, Abstand zweier Geraden im Raum.
```

`## Merksatz` ist optional und nur dann sinnvoll, wenn das Kapitel wirklich eine tragende
Idee hat. Höchstens ein Merksatz pro Lerneinheit - sonst ist es keiner.

Umfang 35-70 Zeilen. Für noch nicht bearbeitete Lerneinheiten reichen Lernziele aus dem
Modulplan, Konzeptliste und Lehrmitteltabelle: rund 35 Zeilen.

---

## PVA-Dateien

**Drei** Dateien pro Präsenzveranstaltung, in drei Phasenordnern. Zusammen unter 90 Zeilen.

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

### PVAx - Vorbereitung (30-40 Zeilen)

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

| Kapitel | Titel | Seiten | |
|---|---|---|---|
| 9.2 | Vektoren | 194-201 | [ ] |
| 9.3 | Winkel, Skalarprodukt und Determinante | 202-205 | [ ] |

## Bearbeitung
```

| Abschnitt | Inhalt |
|---|---|
| Kopfzeile | ein Link auf die LE-Übersicht - dort stehen die Lernziele |
| `## Aufträge` | die Handlungsschritte des Auftrags als Checkliste, Erledigtes abgehakt |
| `## Lektüre <Buch>` | Kapiteltabelle mit Häkchenspalte, darüber der Kapitelversatz falls vorhanden |
| `## Bearbeitung` | leer - Platz für Notizen beim Abarbeiten |

**Nicht enthalten:** Lernziele (stehen in der LE-Übersicht), Lehrmittel-Lücken (ebenfalls
dort), Aufwandsangaben, Hinweise auf Kurztests oder Notengewichte, organisatorische
Fragenlisten.

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
braucht. Die Leerzeilen unter den Überschriften sind Absicht: Der Cursor landet direkt an
der richtigen Stelle.

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
2. **Kapitelversatz** als Callout, falls Auftrag und Buch abweichen
3. **Abdeckung**: welche Lerneinheiten das Buch behandelt und welche nicht, mit der
   Suchmethode belegt (0 Treffer für Begriff X)
4. Tabelle LE / Thema / Kapitel / Seite
5. **Nicht im Buch**: Liste der Lernziele ohne Fundstelle
6. Eigenheiten (Programmiersprache des Buchs, wo die Lösungen liegen)

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
