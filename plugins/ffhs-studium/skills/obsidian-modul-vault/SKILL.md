---
name: obsidian-modul-vault
description: Baut aus einem hochgeladenen Modulplan (Semesterplan, Kursbeschreibung, Syllabus) ein schlankes Obsidian-Notizen-Gerüst - mit Ordnerstruktur, Startseite (MOC), kompaktem Modulplan samt Terminen, Lehrmittel-Kapitellandkarte, Prüfungsordner und Vorlagen. Nutze diesen Skill immer, wenn jemand ein Studienmodul, einen Kurs oder ein Semester in Obsidian vorbereiten, strukturieren oder organisieren will - auch dann, wenn nur nach einer "sinnvollen Notizenstruktur", einem "Vault-Aufbau", einer "Ordnerstruktur für meine Unterlagen" oder nach "Lernnotizen anlegen" gefragt wird und das Wort Skill oder Obsidian gar nicht fällt. Ebenfalls nutzen, wenn ein bestehender Modul-Vault erweitert, aufgeräumt oder ein zweites Modul nach demselben Muster angelegt werden soll.
---

# Obsidian-Vault aus Modulplan

## Worum es geht

Studierende laden einen Modulplan hoch und wollen daraus ein Notizen-Gerüst, mit dem sie
das ganze Semester arbeiten können. Dieser Skill erzeugt dieses Gerüst.

**Grundprinzip: Der Modulplan ist die einzige Quelle der Wahrheit.** Ordnernamen,
Reihenfolge der Lerneinheiten, Lernziele, Lehrmittel und Prüfungslogik werden daraus
abgeleitet - nicht aus allgemeinem Wissen über das Fachgebiet. Ein generisches
"IT-Sicherheit"-Gerüst ist wertlos; ein Gerüst, das exakt der Kapitelreihenfolge *dieses*
Moduls folgt, ist es nicht.

**Zweites Grundprinzip: schlank.** Ein Gerüst, in dem man suchen muss, wird nach zwei
Wochen nicht mehr geöffnet. Jede Datei hat wenige, immer gleiche Abschnitte. Gebrauchsanleitungen,
Lerntipps, Prüfungsdidaktik und Fortschritts-Tracker gehören nicht hinein - sie erzeugen
Pflegeaufwand ohne Nutzen. Richtwert für das fertige Gerüst: **20-30 Dateien, Median unter
50 Zeilen pro Datei.** Erklärt wird an genau einer Stelle, in den Konzeptnotizen, und die
entstehen erst im Lauf des Semesters.

**Wer das Gerüst benutzt, kennt den Stoff noch nicht.** Die Person studiert das Fach und
will mit den Notizen lernen. Das Gerüst ist deshalb schlank, die Konzeptnotizen, die später
hineinkommen, sind es nicht: Sie erklären in Klartext, sie sind kein Spickzettel.

**Die Notizen werden auf Deutsch verfasst**, auch wenn Teile des Modulplans englische
Fachbegriffe enthalten. Fachbegriffe bleiben im Original (Least Privilege, Shared
Responsibility), der Fliesstext ist deutsch.

**Was dieser Skill nicht tut:** Er unterrichtet nicht und füllt keine Fachinhalte ein. Er
baut das Gerüst - gefüllt wird es im Lauf des Semesters, Block für Block, mit den Skills
`pva-vorbereitung` und `leseauftrag`.

---

## Ablauf

Fünf Phasen. Phase 2 ist ein Pflicht-Halt: erst nach Freigabe wird gebaut.

### Phase 1 - Modulplan auslesen

| Was | Wofür |
|---|---|
| Modulname, Modulcode, ECTS, Studiengang | Frontmatter, MOC, Eckdaten |
| Vorkenntnisse, Anschlussmodule | Eckdaten, Tiefenkalibrierung |
| Kompetenzziele (wörtlich, nummeriert) | Modulplan kompakt |
| Lerninhalte **inkl. Reihenfolge** und Unterpunkte | `01_Lerneinheiten`, je LE eine Übersicht |
| **Präsenzveranstaltungen**: Anzahl, Termine, zugehörige LE | `03_PVA` |
| Lehrmittel (Autor, Titel, ISBN, Beschaffung) | `07_Quellen` |
| Prüfungsform, Dauer, Hilfsmittel, Gewichtung | `06_Pruefung` und dessen Zuschnitt |
| Erfahrungsnote: Gewicht, Nachprüfbarkeit | Warnhinweis im Prüfungsordner |
| Praxisanteil: Labor, Programmierung, Werkzeuge | ob es einen `04_`-Ordner gibt |
| Besondere Auflagen (z. B. KI-Policy) | Abschnitt im Modulplan kompakt |

Fehlt der Modulplan, frage danach, bevor du irgendetwas baust. Ein geratenes Gerüst
verursacht mehr Aufräumarbeit, als es spart.

Sind Lehrmittel als PDF vorhanden: Inhaltsverzeichnisse durchsuchen und **echte
Kapitelnummern** ermitteln. Vorgehen in `leseauftrag/references/lehrmittel-pruefen.md`.
Kapitelnummern niemals raten - eine falsche Nummer ist in einer Open-Book-Prüfung schlimmer
als gar keine.

### Phase 2 - Struktur vorschlagen und Freigabe einholen

Zeige im Chat:

- den Ordnerbaum als Codeblock
- pro Ordner einen Satz, **warum** er existiert (abgeleitet aus dem Modulplan)
- die **PVA-Aufteilung**: wie viele Präsenzen, welche LE je PVA
- die Konsequenz aus der Prüfungsform (siehe unten)
- die Liste der Dateien, die du anlegen wirst

Dann warte auf Freigabe.

**Konsequenzen aus der Prüfungsform:**

| Prüfungsform | Was daraus folgt |
|---|---|
| Open Book (Papier / offline PDF) | Ordner `06_Pruefung/Spickzettel-Print` für verdichtete, druckfertige Notizen. Festhalten: Plugin-Ansichten (Dataview, Graph) existieren am Prüfungstag nicht. Suchzeit ist der Engpass, nicht Wissen. |
| Closed Book | Fokus auf Wiederholung, kein Print-Layer |
| Mündlich | Ordner für Argumentationsketten statt Spickzettel |
| Projekt-/Transferarbeit | Ordner für Artefakte, Zwischenstände, Abgabekriterien |
| Erfahrungsnote ohne Nachprüfung | Auffälliger Warnhinweis, Termine zuoberst |
| Besondere Auflage (z. B. KI-Policy) | Eigener Abschnitt, der die Auflage operationalisiert |

### Phase 3 - Vault bauen

```
<Modulcode>/
├── LIESMICH - Einrichtung.md
├── 00_Meta/          MOC + Modulplan kompakt (mit Terminen)
├── 01_Lerneinheiten/ flach: je eine "LEx - Uebersicht.md", KEINE Unterordner pro LE
├── 02_Konzepte/      atomare Notizen, ein Begriff pro Datei
├── 03_PVA/           Workflow je Praesenzveranstaltung
├── 04_<Praxis>/      nur wenn der Modulplan es hergibt: 04_Labor, 04_Python, ...
├── 06_Pruefung/      zugeschnitten auf die Pruefungsform
├── 07_Quellen/       je Lehrmittel eine Kapitellandkarte
└── 99_Templates/     Vorlagen
```

Die Lücke bei `05` ist Absicht: Dort lag früher ein Übungsordner. Übungsaufgaben gehören in
die PVA-Phase, in der sie gestellt werden, nicht in einen eigenen Bereich.

`00_Meta` enthält **genau zwei Dateien**: die MOC und `Modulplan kompakt.md`. Letztere
trägt Eckdaten, **Termine**, Kompetenzziele, Lerninhalte, Lehrmittel und Leistungsnachweis.
Keine getrennten Dateien für Lernplan, Stundenbudget oder einen Kompetenzziele-Tracker -
solche Tracker werden nach zwei Wochen nicht mehr gepflegt und stehen dann falsch da.
Fortschritt wird über die Checkboxen der Lernziele in den LE-Übersichten sichtbar.

Der PVA-Bereich ist nach Präsenzveranstaltungen und deren drei Phasen gegliedert:

```
03_PVA/
├── _Ueber 03_PVA.md
└── PVA1/
    ├── 01_Vorbereitung/   Auftrag vor der PVA: Leseauftrag, Aufgaben
    ├── 02_PVA/            Termin, Fragen fuer die Praesenz, Mitschrift
    └── 03_Nachbereitung/  Auftrag nach der PVA
```

Drei Dateien, eine pro Phase. **Keine `PVAx - Uebersicht.md`** - ein Hub, der nur Termin und
drei Links auf die Nachbarordner trägt, ist ein Klick ohne Inhalt. Termin und Fragen stehen
in den Präsenznotizen, die zugehörige Lerneinheit im Frontmatter (`LE:`).

**Die PVA-Ordner sind Arbeitsablagen, keine Inhaltsablagen.** Sie tragen, was
**abzuarbeiten** ist. Lernziele, Theorie und Lehrmittel-Lücken gehören in die LE-Übersicht
und die Konzeptnotizen - dort sucht man sie im Semester und vor der Prüfung. Lernziele
stehen genau einmal, nämlich in der LE-Übersicht; die Vorbereitungsnotiz verlinkt sie nur.

**PVA und LE sind zwei getrennte Achsen - nicht 1:1.** `01_Lerneinheiten` + `02_Konzepte`
tragen den **Inhalt**, `03_PVA` den **Ablauf**. Eine PVA kann mehrere LEs abdecken und
umgekehrt eine LE über mehrere PVAs laufen. Verknüpft wird **ausschliesslich per Wikilink** -
**nie** durch Schachteln der Ordner.

**Lege nur die erste PVA an**, und auch die nur, wenn ihr Auftrag schon vorliegt. Ordner für
PVA 2 bis 5 auf Vorrat sind Attrappen: Ein PVA-Ordner entsteht, wenn sein Auftrag kommt -
dafür ist der Skill `pva-vorbereitung` da. Ist noch gar kein Auftrag da, genügt
`_Ueber 03_PVA.md`, das die Struktur erklärt.

Ordner weglassen, die der Modulplan nicht hergibt. Ein leerer `04_Labor` in einem
Theoriemodul ist Ballast.

Beim Schreiben gelten die Inhaltsregeln unten und **zwingend**:

- `references/dateinamen-und-encoding.md` - Dateinamen-Regeln. Vor der ersten Datei lesen.
- `pva-vorbereitung/references/dateiformate.md` - der genaue Aufbau jedes Dateityps.
  Dieser Skill legt die Hüllen an, jener füllt sie; die Formate müssen dieselben sein.

Lange Markdown-Dateien mit dem Write-Tool schreiben, nicht mit Bash-Heredocs: LaTeX,
Backticks und Anführungszeichen lassen Heredocs regelmässig scheitern.

Vorlagen liegen in `assets/templates/`.

### Phase 4 - Technisch prüfen

```bash
python <skill-pfad>/scripts/pruefe_vault.py <vault-pfad>
```

Prüft Nicht-ASCII in Dateinamen, doppelte Dateinamen, Wikilinks ins Leere und den Umfang.
Alle FEHLER beheben. HINWEISE zu noch nicht existierenden Konzeptnotizen sind erwartet - das
ist die Arbeitsliste.

Steht kein `python`/`python3` im PATH, liegt oft eine Anaconda-Installation daneben:

```bash
for p in ~/anaconda3/python.exe ~/miniconda3/python.exe /c/ProgramData/anaconda3/python.exe; do [ -x "$p" ] && echo "$p"; done
```

### Phase 5 - Übergeben

Der Vault wird direkt im Zielordner angelegt - standardmässig als Unterordner
`<Modulcode>/` im aktuellen Arbeitsverzeichnis. Nennt die Person einen Pfad zu ihrem
bestehenden Vault, dort hinein bauen. Vorher prüfen, ob der Ordner schon existiert, und
nicht ungefragt überschreiben.

Nur wenn ausdrücklich ein Archiv gewünscht ist:

```bash
cd <übergeordneter-ordner> && zip -qr -UN=UTF8 <Modulcode>-Obsidian-Vault.zip <Modulcode>
```

Danach kurz berichten: was drin ist (eine Zeile, keine Dateiliste), zwei bis drei
**fachliche** Entscheidungen mit Begründung aus dem Modulplan, was bewusst fehlt (z. B.
echte Termine), und dass ausgegraute Links keine Fehler sind, sondern die Arbeitsliste.

---

## Inhaltsregeln

**Lernziele wörtlich als Checkliste.** Die Unterpunkte des Modulplans werden zu
`- [ ]`-Einträgen in der LE-Übersicht. Liegen feinkörnigere Lernziele aus dem LMS vor, haben
diese Vorrang - sie sind prüfungsnäher formuliert. So sieht die Person jederzeit, was offen
ist.

**Die LE-Übersicht ist der Einstieg in die Lerneinheit.** Vier Abschnitte: *Lernziele*,
*Überblick* (der rote Faden in ein bis zwei Absätzen, mit den Notizen in Lesereihenfolge
verlinkt), *Konzepte* (Wikilinks, gern als Tabelle gruppiert), *Lehrmittel* (Kapitel und
Seite). Optional ein `## Merksatz`, wenn das Kapitel wirklich eine tragende Idee hat -
höchstens einer pro Lerneinheit. Der Überblick entsteht erst mit dem Leseauftrag (Skill
`leseauftrag`), beim Gerüstbau bleibt er leer. Kein "Warum diese LE hier steht", kein
"Vorwissen aus vorheriger LE", kein Selbstcheck.

**Konzeptnotizen haben genau vier Abschnitte:** Kopf (was es ist, wozu es dient),
`## Theorie`, `## Beispiel`, `## Quelle`. Schreibregeln und Muster in
`leseauftrag/references/konzeptnotiz.md`. Die Musternotizen des Gerüsts folgen ihnen: in
Klartext erklärt, kein Spickzettel. Beim Gerüstbau werden nur zwei bis drei
Musternotizen angelegt; der Rest bleibt als `[[Wikilink]]` ohne Datei - Obsidian zeigt sie
ausgegraut, ein Klick legt sie an. Das ergibt eine automatische Arbeitsliste.

**PVA-Dateien bleiben minimal.** Die Vorbereitungsnotiz trägt die Auftragsschritte als
Checkliste und die Lesetabelle, sonst nichts. Die Präsenznotiz ist fast leer, weil
währenddessen hineingeschrieben wird. Keine Lernziele (die stehen in der LE-Übersicht),
keine Hinweise auf Kurztests, Notengewichte oder Aufwand - das steht im Modulplan kompakt
und im Prüfungsordner.

**Sprachliche Signale des Modulplans ernst nehmen.** Steht dort "Nutzen und Grenzen",
"einordnen", "abgrenzen" oder "begründen", ist das die Aufgabenform der Prüfung. Baue die
passende Struktur ein - eine Abgrenzungstabelle in der LE-Übersicht, wo alle verwandten
Begriffe nebeneinanderstehen, nicht in jeder einzelnen Konzeptnotiz.

**Platzhalter als Platzhalter kennzeichnen.** Wo Fachinhalt fehlt, schreibe `*(offen)*` oder
einen `## Offen`-Abschnitt mit Checkbox statt erfundenen Inhalt. Erfundene Fachaussagen in
einem Lernvault sind aktiv schädlich: Sie werden gelernt.

**Stundenbudget kurz halten.** ECTS × 30 h ergibt den Gesamtaufwand; das gehört als Zeile in
die Eckdaten, nicht in eine eigene Datei mit Wochenlast-Tabellen.

**Frontmatter knapp.** Was nicht gefiltert oder sortiert wird, gehört nicht hinein:

```yaml
---
LE: 3
thema: Netzwerk- und Systemsicherheit
tags: [<modulcode>/le3]
---
```

PVA-Notizen zusätzlich `pva:` und `phase:` (`Vorbereitung`/`PVA`/`Nachbereitung`).
**Weglassen:** `status:`, `kompetenzziel:`, `typ:`, `quelle:`.

---

## Häufige Fehler

**Fachgebietswissen statt Modulplan.** Der Reflex, ein bekanntes Themengebiet nach
Lehrbuchlogik zu gliedern, führt an der Prüfung vorbei. Wenn der Modulplan IAM vor
Netzwerksicherheit stellt, wird IAM zu LE2 - unabhängig davon, wie Lehrbücher es machen.

**Zu viele Dateien.** Ein Gerüst mit 50 leeren Dateien wird nicht gepflegt. Ziel sind
**20-30**: MOC, Modulplan kompakt, je LE eine Übersicht, die drei Phasennotizen der ersten PVA, zwei bis drei Musterkonzepte, Prüfung, Quellen, Vorlagen.

**Tracker und Lernpläne anlegen.** Kompetenzziele-Tracker mit Nachweisspalten,
Wochenrhythmus-Vorschläge und Fortschrittstabellen wirken hilfreich und werden nie
ausgefüllt. Die Lernziel-Checkboxen in den LE-Übersichten leisten dasselbe ohne Zusatzdatei.

**Didaktik in die Notizen schreiben.** "Das ist prüfungsrelevant", "hier hängen die
meisten", "erst selbst rechnen, dann vergleichen" ist Rauschen. Die Person kennt ihre
Lernstrategie.

**PVA in die LE schachteln.** Weil PVA und LE nicht 1:1 sind, dürfen die PVA-Phasen nicht
als Unterordner einer LE liegen.

**Einen Übungsordner anlegen.** Aufträge gehören unter die PVA, die sie stellt.

**Plugin-Abhängigkeit.** Dataview-Abfragen sind ein Bonus, nie die Grundlage. Der Vault muss
mit Obsidian-Bordmitteln funktionieren - besonders bei Open-Book-Prüfungen, wo am Ende
Papier oder ein PDF zählt.

**Kapitelnummern raten.** Nur eintragen, was im Inhaltsverzeichnis gefunden wurde.

---

## Danach

Das Gerüst ist leer, wo Fachinhalt fehlt. Gefüllt wird es Block für Block mit zwei Skills:
**`pva-vorbereitung`** nimmt den Vorbereitungsauftrag einer PVA, trägt Lernziele und
Aufträge ein und ruft für jeden Leseauftrag **`leseauftrag`** auf. Der prüft die
Kapitelnummern im Lehrmittel, liest die Kapitel und schreibt die Konzeptnotizen.

---

## Referenzdateien

- `references/dateinamen-und-encoding.md` - Dateinamen-Regeln, Mojibake-Problem, doppelte
  Dateinamen. **Vor dem Anlegen der ersten Datei lesen.**
- `pva-vorbereitung/references/dateiformate.md` - genauer Aufbau jedes Dateityps.
- `leseauftrag/references/konzeptnotiz.md` - Aufbau und Schreibregeln der Konzeptnotiz.
- `leseauftrag/references/lehrmittel-pruefen.md` - Kapitelnummern aus dem PDF gewinnen.
- `scripts/pruefe_vault.py` - Prüfskript für Phase 4.
- `assets/templates/` - Vorlagen zum Kopieren nach `99_Templates`.
