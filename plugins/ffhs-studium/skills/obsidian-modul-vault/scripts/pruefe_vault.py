#!/usr/bin/env python3
"""Prueft einen Obsidian-Modul-Vault auf die drei Fehler, die Links zerreissen.

    python3 pruefe_vault.py <vault-pfad>

FEHLER  muessen behoben werden.
HINWEIS ist erwartet - Wikilinks ohne Datei sind die Arbeitsliste fuer das Semester.

Exit 1, wenn FEHLER gefunden wurden.
"""

import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

SKIP_DIRS = {".obsidian", ".git", ".trash", "__pycache__"}
ERLAUBT = re.compile(r"^[A-Za-z0-9 \-_.]+$")

# Wikilinks in Codebloecken und Inline-Code sind keine Links.
FENCE = re.compile(r"```.*?```", re.DOTALL)
INLINE = re.compile(r"`[^`\n]*`")
WIKILINK = re.compile(r"\[\[([^\]\|#\\]+)")  # ohne den Backslash aus [[Name\|Alias]] in Tabellen

MOJIBAKE = {"ÔÇô": "–", "ÔÇö": "—", "Ã¤": "ä", "Ã¶": "ö", "Ã¼": "ü", "ÃŸ": "ß"}


def md_dateien(vault: Path):
    for p in sorted(vault.rglob("*.md")):
        if not SKIP_DIRS & set(p.relative_to(vault).parts):
            yield p


def alle_pfade(vault: Path):
    for p in sorted(vault.rglob("*")):
        if not SKIP_DIRS & set(p.relative_to(vault).parts):
            yield p


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if len(sys.argv) != 2:
        print(__doc__)
        return 2

    vault = Path(sys.argv[1]).resolve()
    if not vault.is_dir():
        print(f"FEHLER  Kein Verzeichnis: {vault}")
        return 2

    fehler = 0
    dateien = list(md_dateien(vault))
    print(f"Vault: {vault}\n{len(dateien)} Markdown-Dateien\n")

    # 1 - Nicht-ASCII in Datei- und Ordnernamen
    print("1. Dateinamen (nur ASCII)")
    treffer = 0
    for p in alle_pfade(vault):
        name = p.name if p.is_file() else p.name
        if not ERLAUBT.match(name.removesuffix(".md") if p.is_file() else name):
            schuldig = "".join(
                f"{c!r}({unicodedata.name(c, '?')}) "
                for c in name
                if not re.match(r"[A-Za-z0-9 \-_.]", c)
            )
            print(f"   FEHLER  {p.relative_to(vault)}")
            print(f"           verbotene Zeichen: {schuldig}")
            for kaputt, echt in MOJIBAKE.items():
                if kaputt in name:
                    print(f"           Mojibake erkannt: {kaputt} war urspruenglich {echt}")
            treffer += 1
    fehler += treffer
    print("   OK" if not treffer else f"   {treffer} Fehler")

    # 2 - Doppelte Dateinamen (Obsidian loest Wikilinks ueber den Namen auf)
    print("\n2. Eindeutige Dateinamen")
    nach_name = defaultdict(list)
    for p in dateien:
        nach_name[p.stem].append(p.relative_to(vault))
    dubletten = {k: v for k, v in nach_name.items() if len(v) > 1}
    for name, pfade in sorted(dubletten.items()):
        print(f"   FEHLER  '{name}' existiert {len(pfade)}x:")
        for pf in pfade:
            print(f"           {pf}")
    fehler += len(dubletten)
    print("   OK" if not dubletten else f"   {len(dubletten)} Fehler")

    # 3 - Wikilinks ins Leere
    print("\n3. Wikilinks")
    vorhanden = set(nach_name)
    ziele = defaultdict(set)
    for p in dateien:
        text = p.read_text(encoding="utf-8", errors="replace")
        text = INLINE.sub(" ", FENCE.sub(" ", text))
        for roh in WIKILINK.findall(text):
            ziel = roh.strip()
            if ziel:
                ziele[ziel].add(p.relative_to(vault))

    offen = sorted(z for z in ziele if z not in vorhanden)
    if not offen:
        print("   OK  alle Wikilinks lösen auf")
    else:
        print(f"   HINWEIS  {len(offen)} Wikilinks ohne Datei (Arbeitsliste, kein Fehler):")
        for ziel in offen:
            quellen = ", ".join(str(q) for q in sorted(ziele[ziel])[:2])
            mehr = "" if len(ziele[ziel]) <= 2 else f" (+{len(ziele[ziel]) - 2})"
            print(f"            [[{ziel}]]  <- {quellen}{mehr}")

    # Umfang - schlank halten ist Teil der Anforderung
    print("\n4. Umfang")
    zeilen = {p: len(p.read_text(encoding="utf-8", errors="replace").splitlines())
              for p in dateien}
    print(f"   {sum(zeilen.values())} Zeilen gesamt, "
          f"Median {sorted(zeilen.values())[len(zeilen) // 2]} Zeilen pro Datei")
    # Nachschlagewerke duerfen lang sein - sie werden nicht gelesen, sondern durchsucht.
    NACHSCHLAGEN = ("rezeptbuch", "cheatsheet", "formelsammlung", "kapitellandkarte")
    dick = sorted((n, p) for p, n in zeilen.items()
                  if n > 120 and not any(k in p.stem.lower() for k in NACHSCHLAGEN))
    for n, p in dick:
        print(f"   HINWEIS  {p.relative_to(vault)} hat {n} Zeilen - aufteilen?")
    if not dick:
        print("   OK  keine Datei ungewöhnlich lang")

    print(f"\n{'=' * 50}")
    if fehler:
        print(f"{fehler} FEHLER - beheben und erneut pruefen.")
        return 1
    print("Keine Fehler.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
