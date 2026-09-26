---
name: pva-vorbereitung
description: Bearbeitet eine Vorbereitungsaufgabe für eine Präsenzveranstaltung (PVA) und füllt damit einen bestehenden Obsidian-Modul-Vault. Aus dem Moodle-Auftrag (Lernziele, Leseauftrag, Kapitelangaben) und den Lehrmittel-PDFs entstehen Konzeptnotizen mit Theorie und Beispielen, eine gefüllte Vorbereitungsnotiz, aktualisierte LE-Übersicht, Kapitellandkarte und Python-Cheatsheet. Nutze diesen Skill, wenn jemand einen Vorbereitungsauftrag, Leseauftrag, Selbsttest oder Lernziele einer PVA hochlädt oder einfügt und daraus Notizen, Zusammenfassungen oder eine Kapitelaufarbeitung will - auch dann, wenn nur "fass mir Kapitel X zusammen", "bereite die PVA vor", "ich muss das bis nächste Woche lesen" oder "trag das in Obsidian ein" gesagt wird. Ebenfalls nutzen, wenn Kapitelnummern eines Lehrmittels geprüft oder Lernziele gegen ein Lehrbuch abgeglichen werden sollen.
---

# PVA-Vorbereitungsaufgabe bearbeiten

## Worum es geht

Vor jeder Präsenzveranstaltung gibt es einen Auftrag: Lernziele lesen, Kapitel im
Lehrmittel durcharbeiten, Kontrollfragen lösen. Dieser Skill verwandelt diesen Auftrag in
Notizen, die man **vor** der Präsenz liest und **in** der Präsenz benutzt.

**Grundprinzip: Der Auftrag und das Lehrmittel sind die einzigen Quellen.** Die Lernziele
werden wörtlich übernommen, die Theorie stammt aus dem Buch, jede Notiz nennt Kapitel und
Seite. Allgemeines Fachwissen ist kein Ersatz - eine Zusammenfassung, die nicht dem
gelesenen Kapitel folgt, hilft beim Lesen nicht.

**Der Zielzustand ist schlank.** Die Person will beim Öffnen einer Datei sofort sehen, wo
was steht. Lange Fliesstexte, Nebenbemerkungen, Lerntipps und Prüfungsdidaktik machen
Notizen unbenutzbar. Die Formatregeln in `references/dateiformate.md` sind deshalb
verbindlich, nicht als Anregung gemeint.

**Was dieser Skill nicht tut:** Er löst die Aufgaben nicht, erfindet keine Fachinhalte und
rät keine Kapitelnummern. Wo das Lehrmittel ein Lernziel nicht abdeckt, wird das als
offener Punkt vermerkt statt gefüllt.

---

## Ablauf

Vier Phasen. Phase 2 entscheidet über die Qualität des Rests.

### Phase 1 - Auftrag und Vault erfassen

Aus dem Auftrag (Screenshot, Text, PDF, Moodle-Export) herausziehen:

| Was | Wofür |
|---|---|
| **Lernziele wörtlich** | Checkliste in Vorbereitungsnotiz und LE-Übersicht |
| Leseauftrag: Buch, Kapitel, Titel | Lesetabelle, Quellenangaben |
| Welche PVA, welche Lerneinheit | Ablageort, Verlinkung |
| Bereits erledigte Schritte | als erledigt markieren, nicht erneut auflisten |
| Abgaben, Fristen | nur wenn genannt |

Dann den Vault ansehen: Wo liegen `02_Konzepte`, `03_PVA`, die LE-Übersichten? Welche
Konzeptnotizen existieren schon? Bestehende Notizen werden **ergänzt, nicht überschrieben**.

Fehlt der Auftrag oder das Lehrmittel, danach fragen, bevor irgendetwas geschrieben wird.

### Phase 2 - Lehrmittel prüfen

Das ist der Schritt, den man nicht überspringen darf. Vorgehen in
`references/lehrmittel-pruefen.md`, kurz:

1. **Inhaltsverzeichnis aus dem PDF ziehen** und die genannten Kapitel suchen
2. **Kapitelnummern verifizieren.** Auftrag und Buch weichen häufig ab, weil eine neuere
   Auflage ein Kapitel eingeschoben hat. Stimmen Nummer und Titel nicht überein, den
   Versatz benennen und die **Buchnummern** verwenden.
3. **Kapitel vollständig lesen** - nicht überfliegen. Definitionen, Sätze, Rechenregeln und
   die durchgerechneten Beispiele mit ihren Zahlen.
4. **Lernziele gegen das Gelesene abgleichen.** Für jedes Lernziel: steht das Verfahren im
   Kapitel, oder nicht?

Der letzte Punkt ist der wertvollste Teil der ganzen Arbeit. Ein Lernziel, das im
angegebenen Lehrmittel fehlt, kostet die Person sonst eine Stunde Suchen. Solche Lücken
werden ausdrücklich als **Offen** vermerkt, mit einem Hinweis, wo stattdessen zu suchen ist.

Kapitelnummern niemals raten. Findest du kein Inhaltsverzeichnis, sag das und lass die
Angabe leer.

### Phase 3 - Schreiben

Reihenfolge:

1. **Konzeptnotizen** in `02_Konzepte` - ein Begriff pro Datei, Aufbau
   **Definition → Theorie → Beispiel → Quelle**
2. **LE-Übersicht** in `01_Lerneinheiten` - Lernziele, Konzeptliste, Lehrmitteltabelle,
   Lücken im Lehrmittel
3. **Vorbereitungsnotiz** in `03_PVA/PVAx/01_Vorbereitung` - **nur die Aufträge** und die
   Lesetabelle
4. **Kapitellandkarte** in `07_Quellen` - echte Nummern nachtragen
5. **Python-Cheatsheet** in `04_Python` - die Rechenschritte des Blocks als Code

> [!important] Die PVA-Ordner sind Arbeitsablagen, keine Inhaltsablagen
> Lernziele, Theorie, Konzeptlinks und Lehrmittel-Lücken gehören in die **LE-Übersicht**
> und die Konzeptnotizen - dort sucht man sie im Semester und vor der Prüfung. In
> `03_PVA/PVAx/` steht nur, was **abzuarbeiten** ist.
>
> Konkret: Die Vorbereitungsnotiz führt die Auftragsschritte als Checkliste und die
> Lesetabelle. Sie wiederholt die Lernziele **nicht** - sie verlinkt in der Kopfzeile auf
> die LE-Übersicht, wo sie stehen. Eine Vorbereitungsnotiz, die man nach der Präsenz noch
> braucht, ist falsch geschnitten.
>
> **Es gibt keine `PVAx - Uebersicht.md`.** Ein Hub, der nur Termin und drei Links trägt,
> ist ein Klick ohne Inhalt. Termin und Fragen für die Präsenz stehen in den
> Präsenznotizen, die Lerneinheit im Frontmatter (`LE:`).

Verbindlich dabei:

- **Die vier Abschnitte und sonst nichts.** Keine Rubriken wie „Warum gibt es das", „Grenzen",
  „Abgrenzung zu ähnlichen Begriffen", „Prüfungsfrage in eigenen Worten", „Selbstcheck".
- **Keine Kontroll- oder Verständnisfragen**, weder erfunden noch aus dem Buch übernommen.
- **Beispiele mit echten Zahlen**, Schritt für Schritt gerechnet, bevorzugt die aus dem
  Lehrmittel. Ein Beispiel ohne Zahlen ist kein Beispiel.
- **Jede Konzeptnotiz nennt Kapitel und Seite.**
- **Keine erfundenen Fachaussagen.** Wo Inhalt fehlt: `*(offen)*` oder ein Abschnitt
  `## Offen` mit Checkbox.
- **Dateinamen rein ASCII** (`Uebersicht`, `Vektorraeume`), Umlaute nur im Text.

Zeilenbudget als Orientierung: Konzeptnotiz 50-85, LE-Übersicht 35-70, Vorbereitungsnotiz
40-50, PVA-Hub unter 25. Wird eine Datei deutlich länger, ist meist ein zweites Konzept
darin versteckt - dann aufteilen.

Beim Schreiben langer Markdown-Dateien den Write-Tool verwenden, keine Bash-Heredocs:
LaTeX, Backticks und Anführungszeichen lassen Heredocs regelmässig scheitern.

Vorlagen zum Kopieren: `assets/`.

### Phase 4 - Prüfen und übergeben

```bash
python <skill-pfad>/scripts/pruefe_vault.py <vault-pfad>
```

Prüft Nicht-ASCII in Dateinamen, doppelte Dateinamen, Wikilinks ins Leere und den Umfang.
Alle FEHLER beheben. HINWEISE zu noch nicht angelegten Konzeptnotizen sind erwartet - das
ist die Arbeitsliste für das Semester.

Steht kein `python`/`python3` im PATH, liegt oft eine Anaconda-Installation daneben:

```bash
for p in ~/anaconda3/python.exe ~/miniconda3/python.exe /c/ProgramData/anaconda3/python.exe; do [ -x "$p" ] && echo "$p"; done
```

Danach im Chat berichten:

- was neu ist (eine Zeile, keine Dateiliste)
- **der Kapitelabgleich**: stimmten die Nummern, gab es einen Versatz?
- **die Lücken**: welche Lernziele deckt das Lehrmittel nicht ab, und wo ist stattdessen zu
  suchen? Das ist die wichtigste Information des ganzen Durchgangs.
- was bewusst offen blieb

---

## Inhaltsregeln

**Lernziele wörtlich und vollständig - in die LE-Übersicht.** Sie sind der Massstab, an dem
die Person ihren Fortschritt misst, und meist prüfungsnäher formuliert als der Modulplan.
Sie stehen genau einmal, nämlich dort, wo auch die Konzepte und das Lehrmittel stehen. Ein
Lernziel ohne zugehörige Konzeptnotiz ist entweder eine Lücke im Lehrmittel oder eine
fehlende Notiz - beides muss sichtbar sein.

**Aufträge in die PVA-Ordner.** Was im Auftrag als Handlung steht - installieren, lesen,
Kontrollfragen lösen, im Forum fragen, abgeben - wird zur Checkliste in der
Vorbereitungsnotiz. Erledigtes als erledigt markieren. Nach der Präsenz wandern die
Folgeaufgaben in die Nachbereitungsnotiz.

**Ein Begriff pro Datei.** Faustregel: Alles, was in mehr als einer Lerneinheit vorkommt,
wird eine eigene Datei. Sammelnotizen sind erlaubt, wenn ein Lernziel mehrere Verfahren
bündelt (etwa „Abstandsprobleme" oder „Lagebeziehungen") - dann aber mit einer
Übersichtstabelle zuoberst.

**Theorie in Formeln und Tabellen, nicht in Fliesstext.** Eine Regel gehört in eine
Tabellenzeile, ein Verfahren in nummerierte Schritte, ein Zusammenhang in eine Formel.
Fliesstext nur, wo er etwas trägt, das eine Tabelle nicht kann - und dann in zwei Sätzen.

**Den roten Faden des Kapitels mitnehmen.** Gute Lehrmittel bauen ein Kapitel um eine Idee
herum. Wenn das Buch zwei Begriffe aus derselben Herleitung gewinnt oder ein
Anwendungsproblem durch das ganze Kapitel zieht, ist genau das die Merkhilfe - ein
`> Merksatz` in der LE-Übersicht, nicht drei Absätze Erklärung.

**Bestehendes ergänzen, nicht ersetzen.** Kommt ein Begriff in einer schon vorhandenen
Notiz vor, wird ein Abschnitt ergänzt und die Quelle nachgetragen. Frontmatter `LE:` um die
neue Lerneinheit erweitern.

**Erledigtes als erledigt markieren.** Was die Person schon gemacht hat (Software
installiert, Videos geschaut), steht als erledigt in der Tabelle - nicht als offene Aufgabe.

**Python nur im Cheatsheet.** Code gehört an eine Stelle, nicht verstreut in
Konzeptnotizen. Im Cheatsheet echter, lauffähiger Code mit den Fallen als Kommentar.

---

## Häufige Fehler

**Kapitelnummern übernehmen statt prüfen.** Der häufigste und teuerste Fehler. Auftrag und
Buchauflage weichen regelmässig ab.

**Lücken glattbügeln.** Wenn ein Lernziel im Lehrmittel fehlt, ist die Versuchung gross, es
aus allgemeinem Wissen zu füllen. Das erzeugt eine Notiz, die beim Nachschlagen im Buch ins
Leere führt. Lücke benennen, Suchrichtung angeben, Checkbox setzen.

**Aus einer Zusammenfassung ein Lehrbuch machen.** Die Notiz begleitet das Lesen, sie
ersetzt es nicht. Wenn eine Konzeptnotiz länger wird als der Buchabschnitt, den sie
zusammenfasst, ist etwas falsch gelaufen.

**Didaktik in die Notizen schreiben.** Hinweise wie „das ist prüfungsrelevant", „hier
hängen die meisten", „erst selbst rechnen, dann vergleichen" sind Rauschen. Die Person
kennt ihre Lernstrategie.

**Lernziele in die Vorbereitungsnotiz kopieren.** Sie stehen dann doppelt und laufen
auseinander, sobald eines nachgetragen wird. Die Vorbereitungsnotiz verlinkt die
LE-Übersicht, mehr nicht.

**Eine PVA-Übersichtsdatei anlegen.** Ein Hub mit Termin und drei Links auf Nachbarordner
ist ein Klick ohne Inhalt. Die Ordnerstruktur einer PVA ist selbsterklärend.

**PVA-Ordner auf Vorrat anlegen.** Leere Ordner für PVA 2 bis 5 sind Attrappen. Ein
PVA-Ordner entsteht, wenn sein Auftrag kommt.

**PVA-Dateien mit Kontext aufblähen.** Die Präsenznotiz ist fast leer, weil während der
Präsenz hineingeschrieben wird. Alles Erklärende gehört in die Konzeptnotizen.

**Beispiele ohne Zahlen.** „Man berechnet zuerst den Normalenvektor und setzt dann ein" ist
kein Beispiel, sondern eine Wiederholung der Theorie.

---

## Referenzdateien

- `references/dateiformate.md` - der genaue Aufbau jedes Dateityps mit Mustern.
  **Vor dem Schreiben der ersten Datei lesen.**
- `references/lehrmittel-pruefen.md` - PDF-Text extrahieren, Kapitelnummern verifizieren,
  Lernziele gegen das Lehrmittel abgleichen.
- `scripts/pruefe_vault.py` - Prüfskript für Phase 4.
- `assets/` - Vorlagen für Konzeptnotiz, LE-Übersicht, PVA-Dateien.
