---
name: pva-vorbereitung
description: Bearbeitet den Vorbereitungsauftrag für eine Präsenzveranstaltung (PVA) und trägt ihn in einen bestehenden Obsidian-Modul-Vault ein. Aus dem Moodle-Auftrag entstehen die Lernziele in der LE-Übersicht, die Vorbereitungsnotiz mit allen Aufträgen als Checkliste und der Lesetabelle, Präsenz- und Nachbereitungsnotiz und das Python-Cheatsheet. Die Leseaufträge darin arbeitet der Skill leseauftrag auf, den dieser Skill dafür aufruft. Nutze diesen Skill, wenn jemand einen Vorbereitungsauftrag, die Aufträge, einen Selbsttest oder die Lernziele einer PVA hochlädt oder einfügt, auch wenn nur "bereite die PVA vor" oder "trag das in Obsidian ein" gesagt wird und auch wenn der Auftrag nur aus einem Leseauftrag besteht.
---

# PVA-Vorbereitungsaufgabe bearbeiten

## Worum es geht

Vor jeder Präsenzveranstaltung gibt es einen Auftrag: Lernziele, Kapitel im Lehrmittel,
Videos, Aufgaben, manchmal eine Abgabe. Dieser Skill verwandelt ihn in zwei Dinge:

- die **Arbeitsliste** der PVA: was abzuarbeiten ist, als Checkliste im PVA-Ordner
- den **Stoff** der Lerneinheit: Lernziele in der LE-Übersicht, die Theorie als
  Konzeptnotizen. Die Konzeptnotizen schreibt der Skill `leseauftrag`, den dieser Skill
  für jeden Leseauftrag aufruft.

**Grundprinzip: Der Auftrag und das Lehrmittel sind die einzigen Quellen.** Die Lernziele
werden wörtlich übernommen, die Theorie stammt aus dem Buch, jede Notiz nennt Kapitel und
Seite.

**Gelernt wird mit den Konzeptnotizen und der LE-Übersicht.** Wer den Auftrag bekommt,
kennt den Stoff noch nicht. Die Konzeptnotizen erklären ihn, die LE-Übersicht zeigt den
roten Faden und führt in Lesereihenfolge durch die Notizen.

**Die Arbeitsablagen sind schlank.** Die PVA-Dateien sind Checklisten und Tabellen: Beim
Öffnen muss sofort klar sein, was zu tun ist. Erklärt wird dort nichts. Die Formate in
`references/dateiformate.md` sind deshalb verbindlich.

**Was dieser Skill nicht tut:** Er löst die Aufgaben nicht, erfindet keine Fachinhalte und
rät keine Kapitelnummern.

---

## Ablauf

Vier Phasen. Die ersten beiden sind Buchhaltung und schnell erledigt. Phase 3 ist die
eigentliche Arbeit und entscheidet über den Wert des Ganzen.

### Phase 1 - Auftrag und Vault erfassen

Aus dem Auftrag (Screenshot, Text, PDF, Moodle-Export) herausziehen:

| Was | Wofür |
|---|---|
| **Lernziele wörtlich** | Checkliste in der LE-Übersicht, Filter für den Leseauftrag |
| alle Aufträge, je mit Art (lesen, Video, Aufgabe, Abgabe) | Checkliste in der Vorbereitungsnotiz |
| Leseauftrag: Buch, Kapitel, Titel, seine eigenen Lernziele und Aufgaben | Übergabe an den Skill `leseauftrag` |
| Welche PVA, welche Lerneinheit | Ablageort, Verlinkung |
| Bereits erledigte Schritte | als erledigt markieren, nicht erneut auflisten |
| Abgaben, Fristen | nur wenn genannt |

Dann den Vault ansehen: Wo liegen `02_Konzepte`, `03_PVA`, die LE-Übersichten? Welche
Konzeptnotizen existieren schon?

Fehlt der Auftrag oder das Lehrmittel, danach fragen, bevor irgendetwas geschrieben wird.

### Phase 2 - Lernziele und Aufträge eintragen

1. **LE-Übersicht** in `01_Lerneinheiten`: Lernziele wörtlich als Checkliste. Stichworte
   aus dem Modulplan, die dort schon stehen, weichen dem Wortlaut des Auftrags, Abgehaktes
   bleibt abgehakt. Überblick, Konzepte und Lehrmittel füllt Phase 3.
2. **PVA-Ordner** `03_PVA/PVAx/` mit Vorbereitungs-, Präsenz- und Nachbereitungsnotiz
3. **Vorbereitungsnotiz**: jeder Auftrag als Checkbox, Erledigtes abgehakt

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

### Phase 3 - Leseaufträge aufarbeiten

Für jeden Leseauftrag den Skill **`leseauftrag`** laden (als Plugin
`ffhs-studium:leseauftrag`; ohne Skill-Tool `leseauftrag/SKILL.md` im Nachbarordner
lesen) und vollständig durcharbeiten. Übergeben werden Buch und Kapitel, der Vault-Pfad,
die Lernziele wörtlich und die Aufgaben, die der Auftrag an die Lektüre knüpft
(Begriffsliste, Szenarien, Fragen). Nennt der Auftrag für den Leseauftrag eigene
Lernziele, sind das die Filter. Sonst gelten die Lernziele der PVA, soweit das Kapitel sie
berührt.

Der Skill `leseauftrag` prüft die Kapitelnummern, liest die Kapitel, gewichtet sie nach
den Lernzielen und schreibt die Konzeptnotizen. Er trägt auch Überblick, Konzeptlinks,
Fundstellen und Lücken in die LE-Übersicht, die Kapitellandkarte und die Lesetabelle ein.

Die Konzeptnotizen nicht nebenbei aus diesem Skill heraus schreiben. Was ohne die
Schreibregeln von `leseauftrag` entsteht, wird ein Spickzettel: korrekt, aber nur für den
verständlich, der den Stoff schon kann. Die Person will mit den Notizen lernen.

Danach jedes Lernziel und jeden Auftrag der PVA durchgehen: Gibt es eine Notiz, mit der
man es lernen oder bearbeiten kann? Wenn nicht, steht der Begriff in der LE-Übersicht
unter „Noch ohne Notiz", mit Fundstelle oder als Lücke, und der Auftrag bekommt in der
Vorbereitungsnotiz den Hinweis, wo sein Stoff zu finden ist.

Enthält der Auftrag keinen Leseauftrag, entfällt diese Phase.

Hat das Modul ein Code-Cheatsheet (`04_Python` oder ähnlich), danach die Rechenschritte
des Blocks als lauffähigen Code nachtragen.

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

Führt der Vault ein Log zur KI-Nutzung oder nennt der Modulplan eine Auflage dazu, eine
Zeile ergänzen. Eine Zeile und ein Bericht genügen für den ganzen Durchgang, auch wenn der
Skill `leseauftrag` mitgelaufen ist.

Danach im Chat berichten:

- was neu ist (eine Zeile, keine Dateiliste)
- **der Kapitelabgleich**: stimmten die Nummern, gab es einen Versatz?
- **die Gewichtung**: was im Leseauftrag Kern ist und was übersprungen werden kann
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

**Den roten Faden des Kapitels mitnehmen.** Gute Lehrmittel bauen ein Kapitel um eine Idee
herum. Wenn das Buch zwei Begriffe aus derselben Herleitung gewinnt oder ein
Anwendungsproblem durch das ganze Kapitel zieht, ist genau das die Merkhilfe - ein
`> Merksatz` in der LE-Übersicht.

**Abgrenzungen in die LE-Übersicht.** Stehen mehrere verwandte Begriffe nebeneinander
(vier Produkte, drei Filterklassen), gehört die Vergleichstabelle einmal in die
LE-Übersicht, nicht in jede einzelne Konzeptnotiz.

**Bestehendes ergänzen, nicht ersetzen.** Kommt ein Begriff in einer schon vorhandenen
Notiz vor, wird ein Abschnitt ergänzt und die Quelle nachgetragen. Frontmatter `LE:` um die
neue Lerneinheit erweitern.

**Keine erfundenen Fachaussagen.** Wo Inhalt fehlt: `*(offen)*` oder ein Abschnitt
`## Offen` mit Checkbox.

**Python nur im Cheatsheet.** Code gehört an eine Stelle, nicht verstreut in
Konzeptnotizen. Im Cheatsheet echter, lauffähiger Code mit den Fallen als Kommentar.

**Dateinamen rein ASCII** (`Uebersicht`, `Vektorraeume`), Umlaute nur im Text.

**Der Vault gewinnt bei Äusserlichkeiten.** Hat der Vault eine eigene Schreibweise für
Tags, Überschriften, Tabellenspalten oder Zeitangaben, folgen neue Dateien dem Vault.
Bestehende Tabellen werden ergänzt, nicht umgebaut (siehe `references/dateiformate.md`).

Beim Schreiben langer Markdown-Dateien den Write-Tool verwenden, keine Bash-Heredocs:
LaTeX, Backticks und Anführungszeichen lassen Heredocs regelmässig scheitern.

---

## Häufige Fehler

**Die Konzeptnotizen nebenbei schreiben.** Der Leseauftrag ist der grösste Teil der Arbeit
und hat eigene Regeln. Wer ihn zwischen Checkliste und Lesetabelle miterledigt, liefert
verdichtete Stichworte statt Erklärungen.

**Lernziele in die Vorbereitungsnotiz kopieren.** Sie stehen dann doppelt und laufen
auseinander, sobald eines nachgetragen wird. Die Vorbereitungsnotiz verlinkt die
LE-Übersicht, mehr nicht.

**Eine PVA-Übersichtsdatei anlegen.** Ein Hub mit Termin und drei Links auf Nachbarordner
ist ein Klick ohne Inhalt. Die Ordnerstruktur einer PVA ist selbsterklärend.

**PVA-Ordner auf Vorrat anlegen.** Leere Ordner für PVA 2 bis 5 sind Attrappen. Ein
PVA-Ordner entsteht, wenn sein Auftrag kommt.

**PVA-Dateien mit Kontext aufblähen.** Die Präsenznotiz ist fast leer, weil während der
Präsenz hineingeschrieben wird. Alles Erklärende gehört in die Konzeptnotizen.

**Didaktik in die Notizen schreiben.** Hinweise wie „das ist prüfungsrelevant", „hier
hängen die meisten", „erst selbst rechnen, dann vergleichen" sind Rauschen. Die Person
kennt ihre Lernstrategie.

---

## Referenzdateien

- `references/dateiformate.md` - der genaue Aufbau von LE-Übersicht, PVA-Dateien,
  Cheatsheet und Kapitellandkarte. **Vor dem Schreiben der ersten Datei lesen.**
- `leseauftrag/SKILL.md` (Nachbarskill) - Leseaufträge aufarbeiten, Konzeptnotizen
  schreiben, Kapitelnummern verifizieren.
- `scripts/pruefe_vault.py` - Prüfskript für Phase 4.
- `assets/` - Vorlagen für LE-Übersicht und PVA-Dateien.
