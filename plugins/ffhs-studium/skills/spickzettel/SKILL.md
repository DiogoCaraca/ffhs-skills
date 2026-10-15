---
name: spickzettel
description: Füllt den Spickzettel eines Obsidian-Modul-Vaults nach. Verdichtet die Konzeptnotizen einer Lerneinheit zu einer druckfertigen Anwendungshilfe für Kurztests und Open-Book-Prüfungen - Formeln, Verfahren als nummerierte Schritte, Voraussetzungen, ein Miniaturbeispiel, Fallen, Seitenzahlen. Erklärt nichts, denn wer den Spickzettel braucht, kennt den Stoff schon. Nutze diesen Skill, wenn jemand den Spickzettel, die Formelsammlung oder das Cheat Sheet ergänzen, nachfüllen oder für den nächsten Kurztest oder die Prüfung vorbereiten will, auch bei "füg das zum Spickzettel hinzu" oder "mach mir eine Formelsammlung für LE3". Die Skills pva-vorbereitung und leseauftrag rufen ihn auf, wenn der Vault einen Spickzettel-Ordner hat. Nicht für Notizen zum Lernen - dafür ist leseauftrag da.
---

# Spickzettel nachfüllen

## Worum es geht

Der Spickzettel ist das, was in der Prüfung neben dem Aufgabenblatt liegt. Er wird
während des Semesters Lerneinheit für Lerneinheit nachgefüllt, damit er vor jedem
Kurztest bereitliegt und nicht in der letzten Woche aus 30 Notizen zusammengesucht werden
muss.

**Grundprinzip: anwenden, nicht erklären.** Wer den Spickzettel braucht, kennt das Thema
mindestens halbwegs. Gesucht ist in der Prüfung nicht das Verständnis, sondern der
Handgriff: Welche Formel, in welcher Reihenfolge, unter welcher Bedingung, und wo lauert
der Vorzeichenfehler? Erklärt wird an genau einer Stelle, in den Konzeptnotizen. Der
Spickzettel ist ihr Gegenstück und hat die umgekehrten Regeln: Was in einer Konzeptnotiz
ein Fehler wäre (Tabellen, Halbsätze, Pfeile, Stichworte), ist hier richtig.

**Suchzeit ist der Engpass, nicht Wissen.** In 20 Minuten Kurztest bleibt keine Zeit, einen
Absatz zu lesen. Ein Eintrag ist gut, wenn man mit ihm eine typische Aufgabe lösen kann,
ohne die Konzeptnotiz zu öffnen, und ihn in Sekunden findet.

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
erfindet keine Formeln. Quelle sind die Konzeptnotizen und die LE-Übersicht, die der Skill
`leseauftrag` geschrieben hat.

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

**Fertig, wenn** feststeht, ob nachgefüllt wird, und wenn ja, in welche Datei und nach
welchen Regeln des Vaults.

### 2 - Stoff bestimmen

Welche Lerneinheit, welche Notizen? Aus dem Auftrag ablesen: Nach `pva-vorbereitung` oder
`leseauftrag` sind es die Notizen, die gerade neu entstanden oder ergänzt wurden. Nennt
die Person selbst einen Umfang („vorerst nur die Transformationen"), gilt genau dieser.

Dann die Quellen lesen: die Konzeptnotizen, die LE-Übersicht (Lernziele, Vergleichstabellen,
Merksatz) und, falls vorhanden, Aufgaben oder Selbsttests aus der Vorbereitungsnotiz. Die
**Verben der Lernziele** sagen, was auf den Zettel gehört:

| Verb im Lernziel | Auf den Spickzettel |
|---|---|
| berechnen, anwenden, bestimmen, lösen | Formel, Verfahren in Schritten, Miniaturbeispiel |
| unterscheiden, vergleichen, einordnen, auswählen | Abgrenzungstabelle oder Entscheidungsregel „wenn ..., dann ..." |
| nennen, kennen, aufzählen | die Liste selbst, ein Merkmal pro Eintrag |
| erklären, begründen | nur das Stichwort, an dem die Begründung hängt. Die Begründung steht in der Notiz. |

**Fertig, wenn** feststeht, welche Notizen ausgewertet werden und welche Aufgabentypen
daraus folgen.

### 3 - Verdichten

Für jeden Aufgabentyp ein Block. Die Überschrift ist die Aufgabe, nicht das Thema:
„Transformationsmatrix aufstellen" statt „Geometrische Transformationen". Ein Block
enthält, was davon gebraucht wird, in dieser Reihenfolge:

1. **Voraussetzung** in einer Zeile: *Gilt nur, wenn ...* Fehlt sie, rechnet man mit der
   richtigen Formel am falschen Fall.
2. **Formel oder Tabelle.** Kataloge (Matrizen, Regeln, Kennzahlen) als Tabelle mit einer
   Zeile pro Eintrag.
3. **Schritte**, nummeriert, wenn es ein Verfahren ist. Ein Schritt ist eine Handlung,
   kein Satz über die Handlung.
4. **Miniaturbeispiel**: die kleinste Aufgabe, an der man das Verfahren nachrechnen kann.
   Ein 2×2-Beispiel reicht, eines pro Verfahren.
5. **Falle**: Vorzeichen, Reihenfolge, Konvention, Druckfehler im Lehrmittel. Offene Punkte
   aus der Notiz, die das Ergebnis ändern („Drehsinn im Buch umgekehrt"), gehören hierher.
6. **Seitenzahlen** in einer Zeile am Blockende, aus dem Abschnitt `## Quelle` der Notiz
   oder der Kapitellandkarte. Nie raten.

Was **nicht** hineingehört: Herleitungen, Begründungen, Beweise, Geschichte, Einleitungssätze,
„warum das so ist", Didaktik („das kommt oft"). Ebenso kein Code: Der steht im
Code-Cheatsheet des Moduls (`04_Python` oder ähnlich). Und keine Wikilinks als
Inhaltsträger: Auf Papier führen sie nirgendwohin.

In einem Textfach (ohne Formeln) gilt dasselbe in anderer Form: Entscheidungsregeln,
Abgrenzungstabellen über dieselben Kriterien, Listen mit Erkennungsmerkmal, Fachbegriffe
mit Ein-Zeilen-Definition.

Notation und Bezeichner aus den Notizen übernehmen. Steht im Spickzettel $Sp(\varphi)$ und in
der Notiz $S_\varphi$, sucht man in der Prüfung an der falschen Stelle.

Richtwert: **eine A4-Seite pro Lerneinheit.** Wird es mehr, wurde gesammelt statt
verdichtet.

**Fertig, wenn** jeder Block mit dem Spickzettel allein eine typische Aufgabe lösbar
macht und kein Satz darin nur dem Verständnis dient.

### 4 - Eintragen

In den Abschnitt der passenden Lerneinheit schreiben. Platzhalter wie `*(füllen)*`
ersetzen. Was schon dasteht, bleibt: ergänzen, nicht umbauen. Steht ein Eintrag schon in
einem anderen Abschnitt, nicht verdoppeln, sondern dort ergänzen.

Hat der Vault für den Spickzettel eine eigene Form (Tabellenspalten, Überschriftenebenen),
folgt der neue Block ihr. Gibt es zusätzlich ein gedrucktes PDF ohne Quelldatei im Vault,
wird es nicht verändert. Im Bericht erwähnen, dass es veraltet ist.

Lange Markdown-Dateien mit dem Write- oder Edit-Tool schreiben, nicht mit
Bash-Heredocs: LaTeX, Backticks und Anführungszeichen lassen Heredocs regelmässig
scheitern.

### 5 - Prüfen und berichten

```bash
python <skill-pfad>/scripts/pruefe_spickzettel.py "<vault>/06_Pruefung/Spickzettel-Print/<Datei>.md"
```

Das Skript meldet Erklär-Absätze, Begründungsketten, Theorie-Überschriften, lange
Tabellenzellen, Code, Einbettungen, die auf Papier fehlen, und Lerneinheiten über dem
Richtwert. Jeden Hinweis beheben oder im Bericht begründen.

Steht kein `python`/`python3` im PATH, liegt oft eine Anaconda-Installation daneben:

```bash
for p in ~/anaconda3/python.exe ~/miniconda3/python.exe /c/ProgramData/anaconda3/python.exe; do [ -x "$p" ] && echo "$p"; done
```

Dann zweimal gegenlesen:

1. **Abschreibfehler.** Jede Formel, jedes Vorzeichen und jeden Index mit der Konzeptnotiz
   vergleichen. Ein Fehler auf dem Spickzettel kostet mehr als ein fehlender Eintrag, weil
   man ihm in der Prüfung vertraut.
2. **Anwendbarkeit.** Für jeden Block eine typische Aufgabe denken und sie nur mit dem
   Spickzettel lösen. Fehlt ein Schritt, eine Voraussetzung oder ein Vorzeichen, ergänzen.
   Steht etwas da, das beim Lösen nicht gebraucht wurde, streichen.

Läuft der Skill aus `pva-vorbereitung` oder `leseauftrag`, gehört sein Ergebnis als eine
Zeile in deren Bericht. Für sich allein im Chat berichten: was neu ist (eine Zeile), was
bewusst weggelassen wurde und ob ein gedrucktes PDF nachgezogen werden muss.

---

## Häufige Fehler

**Erklären.** Der Reflex aus den Konzeptnotizen. Ein Absatz, der sagt, warum eine Formel
gilt, kostet in der Prüfung Lesezeit und bringt keinen Punkt. Die Erklärung steht in der
Notiz.

**Sammeln statt verdichten.** Jede Formel der Notiz übernehmen, auch die Zwischenschritte
der Herleitung. Auf den Zettel kommt das Ergebnis, das man anwendet.

**Nach Thema statt nach Aufgabe gliedern.** In der Prüfung sucht man „wie bestimme ich ...",
nicht „was steht zu Kapitel 11".

**Formel ohne Voraussetzung.** Die Abstandsformel für Punkt und Ebene gilt mit
Einheitsnormale oder mit Division durch die Norm. Ohne diese Zeile ist sie halb falsch.

**Abschreibfehler.** Ein vertauschtes Vorzeichen in einer Drehmatrix fällt beim
Verdichten nicht auf, in der Prüfung auch nicht.

**Ungefragt anlegen oder befüllen.** Ohne Spickzettel-Ordner oder mit `nachfuellen: nein`
hat sich die Person gegen einen Spickzettel entschieden. Aus einem anderen Skill heraus wird
dann nichts angelegt. Ein leerer Ordner ohne `nachfuellen:` stammt oft aus einer älteren
Version des Gerüstbaus und ist noch keine Entscheidung.

**Die Antwort nicht festhalten.** Wer fragt, ohne `nachfuellen:` einzutragen, fragt bei
der nächsten PVA wieder.

---

## Referenzdateien

- `scripts/pruefe_spickzettel.py` - Prüfskript für Schritt 5.
- `assets/_Ueber Spickzettel-Print.md` - Regeln für den Spickzettel-Ordner, Vorlage beim Anlegen.
- `assets/Spickzettel.md` - Vorlage für die Sammlung.
- `leseauftrag/references/konzeptnotiz.md` (Nachbarskill) - wie die Notizen aufgebaut
  sind, aus denen der Spickzettel schöpft.
