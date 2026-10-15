#!/usr/bin/env python3
"""Prueft einen Spickzettel auf die Muster, die aus einer Formelsammlung eine
Erklaerung machen, auf Luecken im festen Aufbau und auf das, was auf Papier oder in
Obsidian nicht funktioniert.

    python3 pruefe_spickzettel.py <datei> [<datei> ...]
    python3 pruefe_spickzettel.py --max 2000 <datei>

Gegenstueck zu leseauftrag/scripts/pruefe_notizen.py: Was dort ein Fehler ist (Tabellen,
Stichworte, Pfeile), ist hier richtig. Gemeldet wird, was Lesezeit kostet, ohne beim
Loesen zu helfen, und was im Aufbau einer Lerneinheit fehlt. Jeder HINWEIS ist eine Stelle
zum Nachlesen, kein Fehler. Ob ein Thema anwendbar ist, entscheidet das Gegenlesen im Skill.

Abschnitte: Hat die Datei mehrere Ueberschriften der Ebene 1 (# LE1 ...), ist jede davon
eine Lerneinheit. Sonst (aeltere Form) jede Ueberschrift der Ebene 2.

Mit --max N: Eine Lerneinheit wird ab N Woertern (ohne Code) gemeldet statt ab 1200.

Exit 0, auch wenn es Hinweise gibt.
"""

import re
import sys
from pathlib import Path

ABSATZ_LANG = 40       # Woerter in einer Textzeile oder einem Listenpunkt. Darueber wird erklaert.
LANGE_ZELLE = 15       # Woerter in einer Tabellenzelle. Darueber steht ein Satz.
LE_LANG = 1200         # Woerter pro Lerneinheit ohne Code, rund zwei bis drei Bildschirmseiten.
THEORIE_KOEPFE = re.compile(
    r"\b(herleitung|theorie|warum|hintergrund|beweis|erklärung|motivation|einführung|idee)\b",
    re.IGNORECASE)
KAUSAL = re.compile(r"\b(weil|denn|deshalb|deswegen|daher|darum|folglich|nämlich)\b", re.IGNORECASE)
PFLICHT_CALLOUTS = {
    "tip": "keine Übersicht (> [!tip])",
    "example": "kein Anwendungsbeispiel (> [!example])",
    "warning": "keine häufigen Fehler (> [!warning])",
}
PLATZHALTER = re.compile(r"^\*\((füllen|folgt)\)\*$")
TRENNLINIE = re.compile(r"^(-{3,}|\*{3,}|_{3,})$")

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
MATH_INLINE = re.compile(r"\$[^$\n]+\$")
WIKILINK = re.compile(r"\[\[[^\]]+\]\]")
WORT = re.compile(r"[A-Za-zÄÖÜäöüß0-9][\w\-/.]*")
TRENNZEILE = re.compile(r"\|[\s:\-|]+\|?")
LISTE = re.compile(r"^([-*+]|\d+\.)\s")
CALLOUT_KOPF = re.compile(r"^\[!(\w+)\]")


def woerter(text: str) -> int:
    text = WIKILINK.sub(" X ", MATH_INLINE.sub(" X ", text))
    return len(WORT.findall(text))


def zellen(zeile: str) -> list[str]:
    """Tabellenzellen; ein | innerhalb von $...$ trennt hier keine Zelle (wird separat gemeldet)."""
    ohne_mathe = MATH_INLINE.sub(lambda m: m.group(0).replace("|", " "), zeile.strip())
    return ohne_mathe.strip("|").split("|")


def ebene_der_lerneinheiten(text: str) -> int:
    """1, wenn es mehrere Ueberschriften '# ' gibt (Titel + # LE...), sonst 2."""
    im_code = False
    anzahl = 0
    for zeile in text.splitlines():
        if zeile.strip().startswith("```"):
            im_code = not im_code
        elif not im_code and zeile.startswith("# "):
            anzahl += 1
    return 1 if anzahl > 1 else 2


def zeilen_mit_art(text: str):
    """Liefert (nummer, inhalt, art, abschnitt, callout).

    art: text, liste, tabelle, kopf, code, mathe, leer.
    callout: Typ des umgebenden Callouts (tip, example, ...) oder None.
    Bei Callout-Zeilen ist inhalt die Zeile ohne fuehrendes '>'.
    """
    ebene = ebene_der_lerneinheiten(text)
    praefix = "#" * ebene + " "
    titel = _erste_h1(text) if ebene == 1 else -1
    abschnitt = "(vor der ersten Lerneinheit)"
    im_code = im_mathe = False
    callout = None
    treffer = FRONTMATTER.match(text)
    start = len(treffer.group(0).splitlines()) if treffer else 0
    for nr, zeile in enumerate(text.splitlines()[start:], start=start + 1):
        s = zeile.strip()
        if not im_code and s.startswith(">"):
            s = s.lstrip(">").strip()
            if (m := CALLOUT_KOPF.match(s)):
                callout = m.group(1).lower()
                yield nr, s, "kopf", abschnitt, callout
                continue
        elif not im_code:
            callout = None
        if s.startswith("```"):
            im_code = not im_code
            yield nr, s, "code", abschnitt, callout
        elif im_code:
            yield nr, zeile, "code", abschnitt, callout
        elif s.startswith("$$"):
            if not (len(s) > 4 and s.endswith("$$")):
                im_mathe = not im_mathe
            yield nr, s, "mathe", abschnitt, callout
        elif im_mathe:
            yield nr, s, "mathe", abschnitt, callout
        elif not s:
            yield nr, s, "leer", abschnitt, callout
        elif s.startswith("#"):
            if s.startswith(praefix) and nr != titel:
                abschnitt = s[len(praefix):].strip()
            yield nr, s, "kopf", abschnitt, callout
        elif s.startswith("|"):
            yield nr, s, "tabelle", abschnitt, callout
        elif LISTE.match(s):
            yield nr, s, "liste", abschnitt, callout
        else:
            yield nr, s, "text", abschnitt, callout


def _erste_h1(text: str) -> int:
    """Zeilennummer des Dateititels (erste '# '-Ueberschrift), der keine Lerneinheit ist."""
    for nr, zeile in enumerate(text.splitlines(), start=1):
        if zeile.startswith("# "):
            return nr
    return -1


def pruefe(pfad: Path) -> list[str]:
    text = pfad.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    zeilen = list(zeilen_mit_art(text))
    hinweise = []

    # 1 - Absaetze und Listenpunkte, die erklaeren
    for nr, zeile, art, _, _ in zeilen:
        if art in ("text", "liste") and (n := woerter(zeile)) > ABSATZ_LANG:
            hinweise.append(
                f"Zeile {nr}: {n} Wörter am Stück. Kurzeinstieg höchstens zwei Sätze, "
                f"sonst auf Formel, Schritt, Tabelle oder Stichwort kürzen."
            )

    # 2 - Begruendungen (in Anwendungsbeispielen erlaubt)
    for nr, zeile, art, _, callout in zeilen:
        if callout == "example":
            continue
        if art in ("text", "liste", "tabelle") and (m := KAUSAL.search(MATH_INLINE.sub(" ", zeile))):
            hinweise.append(
                f"Zeile {nr}: „{m.group(1)}\" leitet eine Begründung ein. Die gehört in die "
                f"Konzeptnotiz, ausser sie ist selbst die Falle."
            )

    # 3 - Theorie-Ueberschriften
    for nr, zeile, art, _, callout in zeilen:
        if art == "kopf" and callout is None and zeile.startswith("#") and (m := THEORIE_KOEPFE.search(zeile)):
            hinweise.append(
                f"Zeile {nr}: Überschrift „{zeile.lstrip('#').strip()}\". "
                f"Theorie steht im Kurzeinstieg, nicht in einem eigenen Abschnitt."
            )

    # 4 - Tabellen: Saetze in Zellen, nacktes | in Formeln
    for nr, zeile, art, _, _ in zeilen:
        if art != "tabelle" or TRENNZEILE.fullmatch(zeile):
            continue
        if any("|" in m.group(0) for m in MATH_INLINE.finditer(zeile)):
            hinweise.append(
                f"Zeile {nr}: „|\" in einer Formel in der Tabelle. Obsidian trennt dort die Zelle. "
                f"Betrag als \\lvert x\\rvert, Norm als \\lVert x\\rVert schreiben."
            )
        for zelle in zellen(zeile):
            if (n := woerter(zelle)) > LANGE_ZELLE:
                hinweise.append(f"Zeile {nr}: Tabellenzelle mit {n} Wörtern. Auf Angabe kürzen.")

    # 5 - Was auf Papier fehlt
    for nr, zeile, art, _, _ in zeilen:
        if art == "code" and zeile.startswith("```") and zeile[3:].strip().lower() == "dataview":
            hinweise.append(f"Zeile {nr}: Dataview-Abfrage. Im Ausdruck bleibt davon nichts.")
        if art != "code" and "![[" in zeile:
            hinweise.append(f"Zeile {nr}: Einbettung ![[...]]. Im Ausdruck nicht verlässlich, Inhalt direkt hinschreiben.")

    # 6 - Umfang je Lerneinheit (ohne Code)
    umfang: dict[str, int] = {}
    for _, zeile, art, abschnitt, _ in zeilen:
        umfang.setdefault(abschnitt, 0)
        if art in ("text", "liste", "tabelle") and not TRENNZEILE.fullmatch(zeile):
            umfang[abschnitt] += woerter(zeile)
    for abschnitt, n in umfang.items():
        if n > LE_LANG:
            hinweise.append(
                f"Lerneinheit „{abschnitt}\" hat {n} Wörter ohne Code, mehr als der Richtwert "
                f"{LE_LANG}. Gesammelt statt verdichtet?"
            )

    # 7 - Fester Aufbau: Uebersicht, Beispiel, haeufige Fehler je Lerneinheit
    if ebene_der_lerneinheiten(text) == 1:
        gefunden: dict[str, set[str]] = {}
        nur_platzhalter: dict[str, bool] = {}
        for _, zeile, art, abschnitt, callout in zeilen:
            if not re.match(r"LE\s*\d", abschnitt):
                continue
            gefunden.setdefault(abschnitt, set())
            nur_platzhalter.setdefault(abschnitt, True)
            if art == "kopf" and callout and zeile.startswith("[!"):
                gefunden[abschnitt].add(callout)
            if art in ("text", "liste", "tabelle", "code", "mathe") and not (
                    PLATZHALTER.match(zeile) or TRENNLINIE.match(zeile)):
                nur_platzhalter[abschnitt] = False
        for abschnitt, typen in gefunden.items():
            if nur_platzhalter[abschnitt]:
                continue
            for typ, meldung in PFLICHT_CALLOUTS.items():
                if typ not in typen:
                    hinweise.append(f"Lerneinheit „{abschnitt}\": {meldung}.")

    print(f"{pfad.name}")
    for abschnitt, n in umfang.items():
        if n:
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
