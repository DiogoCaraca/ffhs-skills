# Format des Spickzettels

Der Aufbau einer Lerneinheit an einem vollständigen Beispiel, dazu die Callout-Syntax und
die Variante für Textfächer. Das Beispiel stammt aus einer Linearen Algebra und ist
gekürzt: eine echte Lerneinheit hat mehrere Themen.

## Datei

```markdown
---
tags: [<modulcode>/pruefung]
---

# <Modulcode> - Spickzettel

Pro Thema: kurze Theorie, Formeln, Tabellen, Anwendungsbeispiel, Code.

**Inhalt**

- **LE1 <Thema>** - <Thema A> · <Thema B> · ...
- **LE2 <Thema>** - ...

---

# LE1 - <Thema>
...

---

# <Sprache>-Fallen
```

- `# LE<n>` (Ebene 1) pro Lerneinheit, `## <Thema>` (Ebene 2) pro Thema. Die Ebenen
  entsprechen Kapitel und Abschnitt einer gedruckten Formelsammlung.
- `---` zwischen den Lerneinheiten, damit sie im Ausdruck und beim Scrollen trennen.
- Das **Inhaltsverzeichnis** oben listet pro LE die Themen in einer Zeile. Es wird bei
  jedem Nachtrag ergänzt.
- Ein Abschnitt **`<Sprache>-Fallen`** am Dateiende sammelt Code-Fallen, die in allen
  Lerneinheiten vorkommen (`*` statt `@`, `== 0` bei Gleitkomma). LE-spezifische Fallen
  stehen in der LE.

## Callouts

Obsidian-Callouts, jede Zeile mit `> `, auch Leerzeilen (`>`) und Tabellen:

| Callout | Wofür | Wo |
|---|---|---|
| `> [!tip] Übersicht` | Frage → Werkzeug, Begriffskette | Anfang jeder LE, sonst sparsam für Merkregeln |
| `> [!important] Definition` | Definition, Formeln, Kernregel | einmal pro Thema |
| `> [!example] Beispiel` | Anwendungsaufgabe mit Rechnung | mindestens einmal pro Thema |
| `> [!warning] Häufige Fehler LE<n>` | nummerierte Fehler | Ende jeder LE, sonst für einzelne Fallen |

Mehr Callout-Arten braucht es nicht. Vier feste Farben sind schneller gefunden als zehn.

## Beispiel einer Lerneinheit (gekürzt auf ein Thema)

````markdown
# LE2 - Lineare und affine Abbildungen

> [!tip] Welche Matrix für welche Aufgabe?
> | Situation | Vorgehen |
> |---|---|
> | Ursprung bleibt fest | 2×2 bzw. 3×3 aus dem Katalog |
> | Mehrere Abbildungen nacheinander | Matrizenprodukt, **rechts zuerst** |
> | Abbildung rückgängig machen | Inverse |

## Inverse

Die Inverse macht eine Abbildung rückgängig. Sie existiert genau dann, wenn $\det \neq 0$.

> [!important] Formel 2×2
> $$\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$
> Diagonale tauschen, Nebendiagonale negieren, durch $\det$ teilen.

| Abbildung | Inverse |
|---|---|
| Drehung $R(\varphi)$ | $R(-\varphi)$ |
| Skalierung $S(\lambda,\mu)$ | $S(\tfrac1\lambda, \tfrac1\mu)$ |
| Produkt $AB$ | $B^{-1}A^{-1}$ (umgekehrte Reihenfolge) |

> [!example] Beispiel
> *Inverse von $\begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$?*
> $\det = 6 - 1 = 5$ → $\tfrac15\begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}$. Probe: Produkt ergibt $I$ ✓

## Python-Cheatsheet LE2

```python
# (1) Determinante und Inverse
M = np.array([[2, 1], [1, 3]])
np.linalg.det(M)                           # -> 5.0
np.linalg.inv(M)                           # -> [[ 0.6 -0.2] [-0.2  0.4]]

# (2) exakt mit sympy
sp.Matrix([[2, 1], [1, 3]]).inv()          # -> Matrix([[3/5, -1/5], [-1/5, 2/5]])
```

> [!warning] Häufige Fehler LE2
> 1. **Reihenfolge verkehrt** - im Produkt steht rechts, was zuerst passiert.
> 2. **Inverse bei $\det = 0$** - existiert nicht, die Abbildung ist nicht umkehrbar.

Socher 11.5, S. 255-257 · Teschl 10.2, S. 284
````

Was das Beispiel zeigt:

- **Kurzeinstieg** sind zwei Sätze. Der zweite nennt die Voraussetzung.
- Die **Tabelle** ist ein Katalog, eine Zeile pro Fall.
- Das **Beispiel** hat eine kursive Aufgabe, die kürzeste Rechnung und eine Probe.
- Im **Code** hat jede Zeile mit Ergebnis ein `# ->`, Abschnitte sind nummeriert. Die
  Imports stehen einmal am Dateianfang, nicht in jeder LE.
- Die **häufigen Fehler** nennen den Fehler fett und die Korrektur in einem Halbsatz.

## Ja/Nein-Tabellen

Für „Ist X ein Y?"-Aufgaben eine Tabelle mit Grund, der Grund ist das Gegenbeispiel:

```markdown
| Menge | Unterraum? | Grund |
|---|---|---|
| $\{x + y - z = 0\}$ | ✓ | homogene lineare Gleichung |
| $\{x + y = 1\}$ | ✗ | $\mathbf{0} \notin U$ |
| $\{xy = 0\}$ | ✗ | $(1\ 0) + (0\ 1) = (1\ 1)$ |
```

## Textfach

Derselbe Aufbau, andere Füllung:

| Formelfach | Textfach |
|---|---|
| Übersicht Frage → Werkzeug | Übersicht Situation → Begriff, Methode oder Paragraf |
| Definition und Formeln | Definition in einer Zeile, Merkmale als Liste |
| Tabelle der Fälle | Abgrenzungstabelle über dieselben Kriterien |
| Rezept in Schritten | Prüfschema in Schritten |
| Beispiel mit Rechnung | kurzer Fall mit Lösung nach dem Prüfschema |
| Code-Cheatsheet | entfällt |
| Häufige Fehler | Verwechslungen und typische Fehlargumente |

## Obsidian und Ausdruck

- In Tabellen kein nacktes `|`, auch nicht in `$...$`: Betrag `\lvert x\rvert`, Norm
  `\lVert x\rVert`.
- Interne Sprünge im Inhaltsverzeichnis als `[[#Thema]]` sind erlaubt, sie sind nur
  Navigation. Inhalt nie hinter einen Link stellen.
- Keine Einbettungen `![[...]]`, kein Dataview: Im Ausdruck bleibt davon nichts.
