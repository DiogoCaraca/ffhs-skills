# FFHS-Skills für Claude Code

Drei Skills, die das Selbststudium in Obsidian organisieren: Der erste baut aus einem
Modulplan ein Notizengerüst, der zweite trägt vor jeder Präsenzveranstaltung die Aufträge
und Lernziele ein, der dritte liest die Lehrmittel-Kapitel und schreibt daraus
verständliche Zusammenfassungen.

Gedacht für Mitstudierende, die mit Claude Code und Obsidian arbeiten.

---

## Was die drei Skills machen

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

Du gibst den Vorbereitungsauftrag aus Moodle rein (Lernziele, Aufträge, Leseauftrag).
Der Skill trägt ihn in den Vault ein:

- die Lernziele wörtlich als Checkliste in die LE-Übersicht
- die Vorbereitungsnotiz zur PVA mit allen Aufträgen und der Lesetabelle
- Präsenz- und Nachbereitungsnotiz
- ein fortlaufendes Python-Cheatsheet

Für jeden Leseauftrag ruft er den Skill `leseauftrag` auf. Setzt einen Vault voraus, wie
ihn der erste Skill baut.

### `leseauftrag`

Du nennst Kapitel und Lernziele und hast das Lehrmittel-PDF lokal liegen. Der Skill liest
die Kapitel vollständig, filtert sie nach den Lernzielen und schreibt Konzeptnotizen als
TL;DR des Lehrmittels:

- Konzepte in Klartext erklärt, Tabellen nur für Vergleiche und Listen
- so tief, wie das Lernziel es verlangt: was Kern ist, was Überblick, was du überspringen
  kannst
- mit Beispiel und mit Kapitel und Seite zu jeder Notiz
- Lernziele, die das Lehrmittel nicht abdeckt, als Lücke benannt statt erfunden

Läuft auch für sich allein: „fass mir Kapitel 14.1 zusammen" oder „die Firewall-Notiz ist
zu komprimiert, schreib sie verständlich" genügt.

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

Falls das Klonen an SSH scheitert (kein SSH-Key hinterlegt), stattdessen die HTTPS-URL
angeben:

```bash
claude plugin marketplace add https://github.com/DiogoCaraca/ffhs-skills.git
```

Prüfen, ob es geklappt hat:

```bash
claude plugin details ffhs-studium
```

Unter `Component inventory` muss `Skills (3)` stehen.

Das war's. Die Skills greifen ab jetzt automatisch, sobald du in einer Session einen
Modulplan hochlädst, einen PVA-Auftrag reinkopierst oder ein Kapitel zusammenfassen lässt.
Du kannst sie auch direkt aufrufen:

- `/ffhs-studium:obsidian-modul-vault`
- `/ffhs-studium:pva-vorbereitung`
- `/ffhs-studium:leseauftrag`

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
2. Aus dem entpackten Ordner die drei Ordner
   `plugins/ffhs-studium/skills/obsidian-modul-vault`,
   `plugins/ffhs-studium/skills/pva-vorbereitung` und
   `plugins/ffhs-studium/skills/leseauftrag`
   kopieren. Alle drei, sie verweisen aufeinander.
3. Einfügen in `~/.claude/skills/` (Windows: `C:\Users\DEIN-NAME\.claude\skills\`).
   Den Ordner `skills` notfalls anlegen.
4. Claude Code neu starten.

Die Skills heissen dann ohne Präfix `obsidian-modul-vault`, `pva-vorbereitung` und
`leseauftrag`.

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
