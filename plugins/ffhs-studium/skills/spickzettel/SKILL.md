---
name: spickzettel
description: Füllt den Spickzettel eines Obsidian-Modul-Vaults nach. Verdichtet die Konzeptnotizen einer Lerneinheit zu einer druckfertigen Formelsammlung für Kurztests und Open-Book-Prüfungen - pro Thema ein Kurzeinstieg in 1-2 Sätzen, Definition und Formeln, Tabellen, Rezept in Schritten, Anwendungsbeispiel, pro Lerneinheit ein geprüftes Code-Cheatsheet und die häufigen Fehler. Erklärt nicht ausführlich, denn wer den Spickzettel braucht, kennt den Stoff schon. Nutze diesen Skill, wenn jemand den Spickzettel, die Formelsammlung oder das Cheat Sheet ergänzen, nachfüllen, überarbeiten oder für den nächsten Kurztest oder die Prüfung vorbereiten will, auch bei "füg das zum Spickzettel hinzu" oder "mach mir eine Formelsammlung für LE3". Die Skills pva-vorbereitung und leseauftrag rufen ihn auf, wenn der Vault einen Spickzettel-Ordner hat. Nicht für Notizen zum Lernen - dafür ist leseauftrag da.
---

# Spickzettel nachfüllen

## Worum es geht

Der Spickzettel ist das, was in der Prüfung neben dem Aufgabenblatt liegt. Er wird
während des Semesters Lerneinheit für Lerneinheit nachgefüllt, damit er vor jedem
Kurztest bereitliegt und nicht in der letzten Woche aus 30 Notizen zusammengesucht werden
muss.

**Vorbild ist eine Formelsammlung, kein Notizzettel.** Knappe Theorie, Tabellen, Formeln,
Anwendungsbeispiele und Code, jedes Thema gleich aufgebaut. Wer eine Aufgabe vor sich
hat, findet über die Übersicht das passende Thema, liest in zwei Sätzen, worum es geht,
und rechnet mit Formel, Rezept und Beispiel los.

**Grundprinzip: anwenden, nicht erklären.** Wer den Spickzettel braucht, kennt das Thema
mindestens halbwegs. Gesucht ist in der Prüfung nicht das Verständnis, sondern der
Handgriff: Welche Formel, in welcher Reihenfolge, unter welcher Bedingung, und wo lauert
der Vorzeichenfehler? Theorie gibt es nur als Kurzeinstieg von ein bis zwei Sätzen.
Herleitungen und Begründungen stehen an genau einer Stelle, in den Konzeptnotizen.

**Suchzeit ist der Engpass, nicht Wissen.** In 20 Minuten Kurztest bleibt keine Zeit, einen
Absatz zu lesen. Ein Eintrag ist gut, wenn man mit ihm eine typische Aufgabe lösen kann,
ohne die Konzeptnotiz zu öffnen, und ihn in Sekunden findet. Deshalb: Tabellen statt
Fliesstext, Callouts als feste Orientierungspunkte, jedes Thema in derselben Reihenfolge.

**Der Spickzettel ist optional.** Nicht jedes Modul braucht einen, und nicht jede Person
will einen. Ob er nachgefüllt wird, steht im Vault: im Ordner mit `Spickzettel` im Namen,
normalerweise `06_Pruefung/Spickzettel-Print`, und dort in der Zeile `nachfuellen: ja`
oder `nachfuellen: nein` im Frontmatter von `_Ueber Spickzettel-Print.md`. Angelegt wird
der Ordner beim Gerüstbau (`obsidian-modul-vault` fragt danach) oder auf ausdrücklichen
Wunsch. Steht `nachfuellen: ja`, wird er bei jeder neuen Lerneinheit nachgeführt.

Ältere Versionen von `obsidian-modul-vault` haben den Ordner bei Open-Book-Modulen ohne
Nachfrage angelegt. Ein solcher Ordner ohne `nachfuellen:` ist deshalb noch kein Wunsch:
Ist er leer, wird einmal gefragt (Schritt 1).

**Was dieser Skill nicht tut:** Er liest kein Lehrmittel neu, löst keine Aufgaben und
erfindet keine Formeln. Quelle sind die Konzeptnotizen, die LE-Übersicht und das
Code-Cheatsheet des Moduls, die `leseauftrag` und `pva-vorbereitung` geschrieben haben.

---

## Ablauf

Fünf Schritte. Schritt 1 entscheidet, ob überhaupt etwas geschieht.

### 1 - Spickzettel finden

Im Vault nach einem Ordner mit `Spickzettel` im Namen suchen (Gross- und Kleinschreibung
egal). Darin liegen meist zwei Dateien: `_Ueber <Ordner>.md` mit den Regeln und die
eigentliche Sammlung (`<Modulcode> - Spickzettel.md`, in älteren Vaults auch
`Formelsammlung ...` oder ähnlich). Beide lesen.

Dann entscheidet die Zeile `nachfuellen:` im Frontmatter von `_Ueber ...`:

| Lage | Was tun |
|---|---|
| kein Ordner, Aufruf aus `pva-vorbereitung` oder `leseauftrag` | **nichts tun und nichts melden.** Die Person hat keinen Spickzettel gewollt. |
| kein Ordner, die Person verlangt selbst einen Spickzettel | kurz fragen, ob der Bereich angelegt werden soll. Bei Ja: `06_Pruefung/Spickzettel-Print/` mit `_Ueber Spickzettel-Print.md` (`nachfuellen: ja`) und der Sammlung aus `assets/` anlegen und in `_Ueber 06_Pruefung.md` verlinken. |
| `nachfuellen: ja` | weiter mit Schritt 2. Fehlt die Sammlung, aus `assets/Spickzettel.md` anlegen, je Lerneinheit des Moduls eine Überschrift. |
| `nachfuellen: nein`, Aufruf aus einem anderen Skill | **nichts tun und nichts melden.** |
| `nachfuellen: nein`, die Person verlangt selbst einen Eintrag | den Auftrag ausführen und einmal fragen, ob der Spickzettel ab jetzt automatisch nachgefüllt werden soll. Die Antwort eintragen. |
| keine Zeile `nachfuellen:`, Sammlung mit echten Einträgen | Der Spickzettel wird benutzt: `nachfuellen: ja` eintragen und weiter mit Schritt 2. |
| keine Zeile `nachfuellen:`, Sammlung fehlt oder enthält nur Platzhalter wie `*(füllen)*` | **einmal fragen:** „Dein Vault hat einen Spickzettel-Ordner aus dem Gerüstbau. Soll ich ihn ab jetzt nach jeder Lerneinheit nachfüllen?" Die Antwort als `nachfuellen: ja` oder `nein` eintragen, bei Ja weiter mit Schritt 2. |

Die Zeile kommt ins Frontmatter von `_Ueber ...`, die übrigen Zeilen dort bleiben. Fehlt
`_Ueber ...` ganz, wird es aus `assets/` angelegt. Bei Nein bleibt der Ordner, wie er ist:
nichts löschen, was die Person angelegt hat. Gefragt wird nur so, dass die Antwort im
Vault landet. Sonst kommt dieselbe Frage bei jeder PVA wieder.

Die Regeln in `_Ueber ...` gelten vor denen dieses Skills: Hat die Person dort eine eigene
Form festgelegt, wird sie befolgt.

**Fertig, wenn** feststeht, ob nachgefüllt wird, und wenn ja, in welche Datei und nach
welchen Regeln des Vaults.

### 2 - Stoff bestimmen

Welche Lerneinheit, welche Notizen? Aus dem Auftrag ablesen: Nach `pva-vorbereitung` oder
`leseauftrag` sind es die Notizen, die gerade neu entstanden oder ergänzt wurden. Nennt
die Person selbst einen Umfang („vorerst nur die Transformationen"), gilt genau dieser.

Dann die Quellen lesen: die Konzeptnotizen, die LE-Übersicht (Lernziele, Vergleichstabellen,
Merksatz), das Code-Cheatsheet des Moduls (`04_Python` oder ähnlich) und, falls vorhanden,
Aufgaben oder Selbsttests aus der Vorbereitungsnotiz. Die **Verben der Lernziele** sagen,
was auf den Zettel gehört:

| Verb im Lernziel | Auf den Spickzettel |
|---|---|
| berechnen, anwenden, bestimmen, lösen | Formel, Rezept in Schritten, Anwendungsbeispiel, Code |
| unterscheiden, vergleichen, einordnen, auswählen | Abgrenzungstabelle oder Entscheidungstabelle „wenn ..., dann ..." |
| nennen, kennen, aufzählen | die Liste selbst, ein Merkmal pro Eintrag |
| erklären, begründen | nur der Kurzeinstieg und das Stichwort, an dem die Begründung hängt |

**Fertig, wenn** feststeht, welche Notizen ausgewertet werden und welche Themen und
Aufgabentypen daraus folgen.

### 3 - Verdichten

Jede Lerneinheit hat denselben Aufbau. `references/format.md` zeigt ihn an einem
vollständigen Beispiel und nennt die Callout-Syntax. **Vor dem ersten Eintrag lesen.**

```
# LE<n> - <Thema der LE>
> [!tip] Übersicht           - welches Werkzeug / Verfahren für welche Frage
## <Thema>                   - je Thema, so viele wie nötig
   Kurzeinstieg               - 1-2 Sätze: was es ist, wozu
   > [!important] Definition  - Definition, Formeln, Kernregel
   Tabellen                   - Fälle, Varianten, Beispiele mit ✓ / ✗
   Rezept                     - nummerierte Schritte, wenn es ein Verfahren ist
   > [!example] Beispiel      - kursive Aufgabe, kurze Rechnung, Probe
## <Sprache>-Cheatsheet LE<n> - ein Codeblock, nur wenn das Modul eine Sprache verwendet
> [!warning] Häufige Fehler LE<n>
Quellenzeile mit Seitenzahlen
```

Die Teile im Einzelnen:

1. **Übersicht.** Eine Tabelle, die von der Frage zum Werkzeug führt („Winkel? →
   Skalarprodukt"). Sie ist der Einstieg beim Suchen. In einem Textfach führt sie von der
   Situation zum Begriff oder zur Methode.
2. **Kurzeinstieg.** Höchstens zwei Sätze, ohne Herleitung. Er sagt, was das Ding ist und
   wofür man es braucht. Wer mehr braucht, liest die Konzeptnotiz.
3. **Definition / Formeln** im Callout `[!important]`. Notation und Bezeichner aus den
   Notizen übernehmen: Steht im Spickzettel $Sp(\varphi)$ und in der Notiz $S_\varphi$, sucht
   man in der Prüfung an der falschen Stelle.
4. **Tabellen** für alles, was Fälle, Varianten oder Kataloge hat: eine Zeile pro Fall.
   Ja/Nein-Fragen mit ✓ / ✗ und dem Grund in einer Spalte.
5. **Rezept** als nummerierte Schritte, wenn es ein Verfahren ist. Ein Schritt ist eine
   Handlung. Die Voraussetzung gehört davor: *Gilt nur, wenn ...*
6. **Anwendungsbeispiel** im Callout `[!example]`: die Aufgabe kursiv, dann die kürzeste
   Rechnung, die das Verfahren zeigt, und wo möglich eine Probe. Eines pro Thema reicht,
   bei mehreren Fällen eines pro Fall.
7. **Code-Cheatsheet**, nur wenn das Modul Python, R oder eine andere Sprache verwendet.
   Ein Block pro Lerneinheit, gegliedert mit `# (1)`, `# (2)` ..., hinter jeder Zeile mit
   Ergebnis die Ausgabe als `# -> ...`. Das Code-Cheatsheet des Moduls bleibt die
   vollständige Sammlung, hier steht der Auszug zu den Aufgaben dieser LE. **Jede Ausgabe
   wird in Schritt 5 ausgeführt und verglichen.**
8. **Häufige Fehler** im Callout `[!warning]`: nummeriert, der Fehler fett, dahinter in
   einem Halbsatz die Korrektur. Vorzeichen, Reihenfolge, Konvention, Druckfehler im
   Lehrmittel, Code-Fallen.
9. **Quellenzeile** am LE-Ende: Kapitel und Seiten aus dem Abschnitt `## Quelle` der Notizen
   oder der Kapitellandkarte. Nie raten.

Was **nicht** hineingehört: Herleitungen, Beweise, Geschichte, „warum das so ist" über den
Kurzeinstieg hinaus, Didaktik („das kommt oft"). Keine Wikilinks als Inhaltsträger und keine
Einbettungen `![[...]]`: Auf Papier führen sie nirgendwohin.

**Textfach (ohne Formeln):** derselbe Aufbau. An die Stelle der Formeln treten
Definitionen in einer Zeile, an die Stelle der Rezepte Entscheidungsregeln und Prüfschemata,
an die Stelle der Rechnung ein kurzer Fall mit Lösung. Das Code-Cheatsheet entfällt.

**Umfang:** Richtwert rund 1200 Wörter pro Lerneinheit ohne Code, zwei bis drei
Bildschirmseiten. Wird es mehr, wurde gesammelt statt verdichtet: Fliesstext in Tabellen
überführen, doppelte Beispiele streichen.

**Fertig, wenn** jedes Thema mit dem Spickzettel allein eine typische Aufgabe lösbar macht,
jedes Thema gleich aufgebaut ist und kein Satz darin nur dem Verständnis dient.

### 4 - Eintragen

In den Abschnitt der passenden Lerneinheit schreiben. Platzhalter wie `*(füllen)*`
ersetzen. Steht ein Eintrag schon in einem anderen Abschnitt, nicht verdoppeln, sondern
dort ergänzen.

**Bestehende Form:** Hat der Vault einen Spickzettel in einer älteren oder eigenen Form
(etwa nur Tabellen, `## LE` statt `# LE`), folgt ein **Nachtrag** dieser Form. Umgebaut
auf das Format oben wird nur, wenn die Person es verlangt („überarbeite den Spickzettel").
Dann die ganze Datei umbauen, nicht nur die neue LE, damit der Zettel einheitlich bleibt.

Gibt es zusätzlich ein gedrucktes PDF ohne Quelldatei im Vault, wird es nicht verändert.
Im Bericht erwähnen, dass es veraltet ist.

Lange Markdown-Dateien mit dem Write- oder Edit-Tool schreiben, nicht mit
Bash-Heredocs: LaTeX, Backticks und Anführungszeichen lassen Heredocs regelmässig
scheitern.

**In Tabellen kein nacktes `|`**, auch nicht in Formeln: Obsidian trennt daran die Zelle.
Betrag und Norm als `\lvert x\rvert` und `\lVert x\rVert` schreiben. In Callouts beginnt
jede Zeile mit `> `, auch Tabellenzeilen und Leerzeilen (`>`).

### 5 - Prüfen und berichten

Zwei Skripte:

```bash
python <skill-pfad>/scripts/pruefe_spickzettel.py "<vault>/06_Pruefung/Spickzettel-Print/<Datei>.md"
python <skill-pfad>/scripts/pruefe_code.py "<vault>/06_Pruefung/Spickzettel-Print/<Datei>.md"
```

`pruefe_spickzettel.py` meldet lange Absätze, Begründungsketten, Theorie-Überschriften,
lange Tabellenzellen, nackte `|` in Tabellenformeln, Einbettungen, Lerneinheiten über dem
Richtwert und Lerneinheiten ohne Übersicht, Beispiel oder häufige Fehler. Jeden Hinweis
beheben oder im Bericht begründen.

`pruefe_code.py` führt alle Python-Blöcke der Datei der Reihe nach aus und stellt jedes
Ergebnis neben den `# ->`-Kommentar. Jede Abweichung korrigieren - im Kommentar, nicht im
Code, ausser der Code ist falsch. Für R oder andere Sprachen die Blöcke selbst ausführen
und genauso vergleichen.

Steht kein `python`/`python3` im PATH, liegt oft eine Anaconda-Installation daneben:

```bash
for p in ~/anaconda3/python.exe ~/miniconda3/python.exe /c/ProgramData/anaconda3/python.exe; do [ -x "$p" ] && echo "$p"; done
```

Dann zweimal gegenlesen:

1. **Abschreibfehler.** Jede Formel, jedes Vorzeichen und jeden Index mit der Konzeptnotiz
   vergleichen, jede Zahl in den Beispielen nachrechnen. Ein Fehler auf dem Spickzettel
   kostet mehr als ein fehlender Eintrag, weil man ihm in der Prüfung vertraut.
2. **Anwendbarkeit.** Für jedes Thema eine typische Aufgabe denken und sie nur mit dem
   Spickzettel lösen. Fehlt ein Schritt, eine Voraussetzung oder ein Vorzeichen, ergänzen.
   Steht etwas da, das beim Lösen nicht gebraucht wurde, streichen.

Läuft der Skill aus `pva-vorbereitung` oder `leseauftrag`, gehört sein Ergebnis als eine
Zeile in deren Bericht. Für sich allein im Chat berichten: was neu ist (eine Zeile), was
bewusst weggelassen wurde und ob ein gedrucktes PDF nachgezogen werden muss.

---

## Häufige Fehler

**Erklären.** Der Reflex aus den Konzeptnotizen. Ein dritter und vierter Satz im
Kurzeinstieg, der sagt, warum eine Formel gilt, kostet in der Prüfung Lesezeit und bringt
keinen Punkt. Die Erklärung steht in der Notiz.

**Sammeln statt verdichten.** Jede Formel der Notiz übernehmen, auch die Zwischenschritte
der Herleitung. Auf den Zettel kommt das Ergebnis, das man anwendet.

**Uneinheitlicher Aufbau.** Ein Thema mit Beispiel-Callout, das nächste ohne, eines mit
Tabelle, eines als Fliesstext. Die feste Reihenfolge ist es, die das Suchen schnell macht.

**Formel ohne Voraussetzung.** Die Abstandsformel für Punkt und Ebene gilt mit
Einheitsnormale oder mit Division durch die Norm. Ohne diese Zeile ist sie halb falsch.

**Ungeprüfte Code-Ausgaben.** Ein `# -> 5.0`, das in Wahrheit `-14.0` ist, fällt erst in der
Prüfung auf. `pruefe_code.py` läuft vor jedem Bericht.

**Abschreibfehler.** Ein vertauschtes Vorzeichen in einer Drehmatrix fällt beim
Verdichten nicht auf, in der Prüfung auch nicht.

**Ungefragt anlegen, befüllen oder umbauen.** Ohne Spickzettel-Ordner oder mit
`nachfuellen: nein` hat sich die Person gegen einen Spickzettel entschieden. Ein bestehender
Spickzettel in eigener Form wird ergänzt, nicht ungefragt umgebaut.

**Die Antwort nicht festhalten.** Wer fragt, ohne `nachfuellen:` einzutragen, fragt bei
der nächsten PVA wieder.

---

## Referenzdateien

- `references/format.md` - der Aufbau an einem vollständigen Beispiel, Callout-Syntax,
  Variante für Textfächer. Vor dem ersten Eintrag lesen.
- `scripts/pruefe_spickzettel.py` - Prüfskript für Form und Umfang (Schritt 5).
- `scripts/pruefe_code.py` - führt die Python-Blöcke aus und vergleicht mit `# ->` (Schritt 5).
- `assets/_Ueber Spickzettel-Print.md` - Regeln für den Spickzettel-Ordner, Vorlage beim Anlegen.
- `assets/Spickzettel.md` - Vorlage für die Sammlung.
- `leseauftrag/references/konzeptnotiz.md` (Nachbarskill) - wie die Notizen aufgebaut
  sind, aus denen der Spickzettel schöpft.
