# FFHS-Skills für Claude Code

Zwei Skills, die das Selbststudium in Obsidian organisieren: Der eine baut aus einem
Modulplan ein Notizengerüst, der andere füllt es vor jeder Präsenzveranstaltung mit dem
Stoff aus dem Lehrmittel.

Gedacht für Mitstudierende, die mit Claude Code und Obsidian arbeiten.

---

## Was die beiden Skills machen

### `obsidian-modul-vault`

Du lädst den Modulplan hoch (Semesterplan, Kursbeschreibung, Syllabus). Der Skill baut
daraus ein Obsidian-Gerüst für das ganze Semester:

- Ordnerstruktur für Lerneinheiten, PVAs und Prüfungsvorbereitung
- Startseite (MOC) als Einstiegspunkt
- kompakter Modulplan mit allen Terminen
- Kapitellandkarte des Lehrmittels
- Vorlagen für Konzeptnotizen, LE-Notizen, Präsenz- und Nachbereitungsnotizen

Läuft auch, wenn du nur sagst „ich brauch eine sinnvolle Notizenstruktur für das Modul" —
den Skill-Namen musst du nicht kennen.

### `pva-vorbereitung`

Du gibst den Vorbereitungsauftrag aus Moodle rein (Lernziele, Leseauftrag, Kapitelangaben)
und hast das Lehrmittel-PDF lokal liegen. Der Skill arbeitet die Kapitel auf und schreibt
in den Vault:

- Konzeptnotizen mit Theorie und Beispielen
- die ausgefüllte Vorbereitungsnotiz zur PVA
- aktualisierte LE-Übersicht und Kapitellandkarte
- ein fortlaufendes Python-Cheatsheet

Setzt einen Vault voraus, wie ihn der erste Skill baut.

---

## Installation

**Voraussetzung:** [Claude Code](https://code.claude.com/docs) ist installiert und du bist
eingeloggt.

Marketplace registrieren:

```bash
claude plugin marketplace add DiogoCaraca/ffhs-skills
```

Plugin installieren:

```bash
claude plugin install ffhs-studium@ffhs-skills
```

Prüfen, ob es geklappt hat:

```bash
claude plugin details ffhs-studium
```

Unter `Component inventory` muss `Skills (2)` stehen.

Das war's. Beide Skills greifen ab jetzt automatisch, sobald du in einer Session einen
Modulplan hochlädst oder einen PVA-Auftrag reinkopierst. Du kannst sie auch direkt
aufrufen:

- `/ffhs-studium:obsidian-modul-vault`
- `/ffhs-studium:pva-vorbereitung`

---

## Updates holen

Wenn es eine neue Version gibt:

```bash
claude plugin marketplace update ffhs-skills
```

---

## Deinstallieren

```bash
claude plugin uninstall ffhs-studium@ffhs-skills
```

---

## Ohne Git: manuelle Installation

Falls du Git nicht eingerichtet hast, geht es auch von Hand:

1. Oben auf **Code → Download ZIP** klicken und entpacken.
2. Aus dem entpackten Ordner die beiden Ordner
   `plugins/ffhs-studium/skills/obsidian-modul-vault` und
   `plugins/ffhs-studium/skills/pva-vorbereitung`
   kopieren.
3. Beide einfügen in `~/.claude/skills/` (Windows: `C:\Users\DEIN-NAME\.claude\skills\`).
   Den Ordner `skills` notfalls anlegen.
4. Claude Code neu starten.

Die Skills heissen dann ohne Präfix `obsidian-modul-vault` und `pva-vorbereitung`.

Nachteil: Updates musst du jedes Mal selbst nachziehen. Der Weg über den Marketplace
oben ist der bessere.

> **Nicht beides gleichzeitig.** Wenn du die Skills schon von Hand unter
> `~/.claude/skills/` liegen hast und zusätzlich das Plugin installierst, sind sie doppelt
> da. Dann die Ordner aus `~/.claude/skills/` löschen.

---

## Was hier *nicht* drin ist

**Keine Lehrmittel, keine Skripte, keine Folien, keine Moodle-Inhalte.** Das ist
urheberrechtlich geschütztes Material und bleibt draussen — die `.gitignore` blockt
PDFs und Office-Dateien bewusst.

Die Skills arbeiten mit *deiner* eigenen Kopie des Lehrmittels, die du lokal liegen hast.
Hier drin steckt nur die Methodik: wie die Notizen aufgebaut werden und wie Claude die
Kapitel aufarbeiten soll.

---

## Lizenz

[MIT](LICENSE) — nimm die Skills, ändere sie, bau sie für dein eigenes Modul um.

## Mitmachen

Wenn dir was fehlt oder etwas nicht sauber läuft: Issue aufmachen oder Pull Request
schicken. Die Skills sind reine Markdown-Dateien (`SKILL.md` plus `references/`,
`assets/`, `scripts/`), da kann man gefahrlos reinschreiben.
