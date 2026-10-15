#!/usr/bin/env python3
"""Prueft einen Spickzettel auf die Muster, die aus einer Anwendungshilfe eine
Erklaerung machen, und auf das, was auf Papier nicht funktioniert.

    python3 pruefe_spickzettel.py <datei> [<datei> ...]
    python3 pruefe_spickzettel.py --max 800 <datei>

Gegenstueck zu leseauftrag/scripts/pruefe_notizen.py: Was dort ein Fehler ist (Tabellen,
Stichworte, Pfeile), ist hier richtig. Gemeldet wird, was Lesezeit kostet, ohne beim
Loesen zu helfen. Jeder HINWEIS ist eine Stelle zum Nachlesen, kein Fehler. Ob ein Block
anwendbar ist, entscheidet das Gegenlesen im Skill.

Mit --max N: Eine Lerneinheit (Abschnitt ##) wird ab N Woertern gemeldet statt ab 600.

Exit 0, auch wenn es Hinweise gibt.
"""

import re
import sys
from pathlib import Path

ABSATZ_LANG = 30       # Woerter in einer Textzeile oder einem Listenpunkt. Darueber wird erklaert.
LANGE_ZELLE = 12       # Woerter in einer Tabellenzelle. Darueber steht ein Satz.
LE_LANG = 600          # Woerter pro Abschnitt ##, rund eine A4-Seite mit Formeln.
THEORIE_KOEPFE = re.compile(
    r"\b(herleitung|theorie|warum|hintergrund|beweis|erklärung|motivation|einführung|idee)\b",
    re.IGNORECASE)
KAUSAL = re.compile(r"\b(weil|denn|deshalb|deswegen|daher|darum|folglich|nämlich)\b", re.IGNORECASE)

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
MATH_INLINE = re.compile(r"\$[^$\n]+\$")
WIKILINK = re.compile(r"\[\[[^\]]+\]\]")
WORT = re.compile(r"[A-Za-zÄÖÜäöüß0-9][\w\-/.]*")
TRENNZEILE = re.compile(r"\|[\s:\-|]+\|?")
LISTE = re.compile(r"^([-*+]|\d+\.)\s")


def woerter(text: str) -> int:
    text = WIKILINK.sub(" X ", MATH_INLINE.sub(" X ", text))
    return len(WORT.findall(text))


def zellen(zeile: str) -> list[str]:
    """Tabellenzellen; ein | innerhalb von $...$ trennt keine Zelle."""
    ohne_mathe = MATH_INLINE.sub(lambda m: m.group(0).replace("|", " "), zeile.strip())
    return ohne_mathe.strip("|").split("|")


def zeilen_mit_art(text: str):
    """Liefert (nummer, zeile, art, abschnitt). art: text, liste, tabelle, kopf, code, mathe, leer."""
    abschnitt = "(vor dem ersten Abschnitt)"
    im_code = im_mathe = False
    treffer = FRONTMATTER.match(text)
    start = len(treffer.group(0).splitlines()) if treffer else 0
    for nr, zeile in enumerate(text.splitlines()[start:], start=start + 1):
        s = zeile.strip()
        if s.startswith("```"):
            im_code = not im_code
            yield nr, zeile, "code", abschnitt
        elif im_code:
            yield nr, zeile, "code", abschnitt
        elif s.startswith("$$"):
            if not (len(s) > 4 and s.endswith("$$")):
                im_mathe = not im_mathe
            yield nr, zeile, "mathe", abschnitt
        elif im_mathe:
            yield nr, zeile, "mathe", abschnitt
        elif not s:
            yield nr, zeile, "leer", abschnitt
        elif s.startswith("#"):
            if s.startswith("## "):
                abschnitt = s[3:].strip()
            yield nr, zeile, "kopf", abschnitt
        elif s.startswith("|"):
            yield nr, zeile, "tabelle", abschnitt
        elif LISTE.match(s):
            yield nr, zeile, "liste", abschnitt
        else:
            yield nr, zeile, "text", abschnitt


def pruefe(pfad: Path) -> list[str]:
    text = pfad.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    zeilen = list(zeilen_mit_art(text))
    hinweise = []

    # 1 - Absaetze und Listenpunkte, die erklaeren
    for nr, zeile, art, _ in zeilen:
        if art in ("text", "liste") and (n := woerter(zeile)) > ABSATZ_LANG:
            hinweise.append(
                f"Zeile {nr}: {n} Wörter am Stück. Wer den Stoff kennt, braucht den "
                f"Handgriff, nicht den Absatz. Auf Formel, Schritt oder Stichwort kürzen."
            )

    # 2 - Begruendungen
    for nr, zeile, art, _ in zeilen:
        if art in ("text", "liste", "tabelle") and (m := KAUSAL.search(MATH_INLINE.sub(" ", zeile))):
            hinweise.append(
                f"Zeile {nr}: „{m.group(1)}\" leitet eine Begründung ein. Die gehört in die "
                f"Konzeptnotiz, ausser sie ist selbst die Falle."
            )

    # 3 - Theorie-Ueberschriften
    for nr, zeile, art, _ in zeilen:
        if art == "kopf" and (m := THEORIE_KOEPFE.search(zeile)):
            hinweise.append(
                f"Zeile {nr}: Überschrift „{zeile.strip().lstrip('#').strip()}\". "
                f"Der Spickzettel gliedert nach Aufgaben, nicht nach Theorie."
            )

    # 4 - Tabellenzellen mit einem Satz
    for nr, zeile, art, _ in zeilen:
        if art != "tabelle" or TRENNZEILE.fullmatch(zeile.strip()):
            continue
        for zelle in zellen(zeile):
            if (n := woerter(zelle)) > LANGE_ZELLE:
                hinweise.append(f"Zeile {nr}: Tabellenzelle mit {n} Wörtern. Auf Angabe kürzen.")

    # 5 - Was auf Papier fehlt oder woanders hingehoert
    for nr, zeile, art, _ in zeilen:
        s = zeile.strip()
        if art == "code" and s.startswith("```") and s != "```":
            sprache = s[3:].strip().lower()
            if sprache == "dataview":
                hinweise.append(f"Zeile {nr}: Dataview-Abfrage. Im Ausdruck bleibt davon nichts.")
            else:
                hinweise.append(f"Zeile {nr}: Codeblock. Code gehört ins Code-Cheatsheet des Moduls.")
        if art != "code" and "![[" in zeile:
            hinweise.append(f"Zeile {nr}: Einbettung ![[...]]. Im Ausdruck nicht verlässlich, Inhalt direkt hinschreiben.")

    # 6 - Umfang je Lerneinheit
    umfang: dict[str, int] = {}
    for _, zeile, art, abschnitt in zeilen:
        if art in ("text", "liste", "tabelle") and not TRENNZEILE.fullmatch(zeile.strip()):
            umfang[abschnitt] = umfang.get(abschnitt, 0) + woerter(zeile)
    for abschnitt, n in umfang.items():
        if n > LE_LANG:
            hinweise.append(
                f"Abschnitt „{abschnitt}\" hat {n} Wörter, mehr als rund eine A4-Seite. "
                f"Gesammelt statt verdichtet?"
            )

    print(f"{pfad.name}")
    for abschnitt, n in umfang.items():
        print(f"   {n:5d} Wörter  {abschnitt}")
    return hinweise


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    global LE_LANG
    argumente = sys.argv[1:]
    if "--max" in argumente:
        i = argumente.index("--max")
        LE_LANG = int(argumente[i + 1])
        argumente = argumente[:i] + argumente[i + 2:]
    if not argumente:
        print(__doc__)
        return 2

    gesamt = 0
    for a in argumente:
        pfad = Path(a)
        if not pfad.is_file():
            print(f"Nicht gefunden: {pfad}")
            continue
        hinweise = pruefe(pfad)
        for h in hinweise:
            print(f"   HINWEIS  {h}")
        if not hinweise:
            print("   OK")
        gesamt += len(hinweise)
    print(f"\n{gesamt} Hinweise.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
