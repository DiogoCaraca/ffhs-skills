#!/usr/bin/env python3
"""Lehrbuch-PDF als Text lesen und dabei die gedruckten Seitenzahlen behalten.

    python3 buchseiten.py text  <buch.pdf> <ziel.txt>
    python3 buchseiten.py suche <ziel.txt> <begriff> [<begriff> ...] [--kontext N]
    python3 buchseiten.py seite <ziel.txt> <buchseite> [<bis-buchseite>]
    python3 buchseiten.py bild  <buch.pdf> <ziel.txt> <buchseite> <zielordner> [--pdf]

text   extrahiert das PDF mit pdftotext (-layout, UTF-8).
suche  zaehlt die Treffer je Begriff und nennt zu jedem Treffer die Buchseite.
seite  gibt den Text einer Buchseite aus, mit den Zeilennummern der Textdatei.
bild   rendert eine Buchseite als PNG (pdftoppm), um Formeln, Tabellen und
       verstuemmelte Stellen am Seitenbild zu pruefen. Mit --pdf ist die Zahl eine
       PDF-Seite, fuer roemisch gezaehlte Seiten wie das Inhaltsverzeichnis.

Die Buchseite wird aus den Kolumnentiteln bestimmt. Wo ein Titel fehlt, wird sie aus
dem Versatz der Nachbarseiten berechnet und mit ~ markiert. Die Suche ignoriert
Gross- und Kleinschreibung, Bindestriche (Hashfunktion findet Hash-Funktion) und
Ligaturen (fi, fl), die pdftotext als ein Zeichen liefert.
"""

import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ZAHL_VORN = re.compile(r"^\s*(\d{1,4})\s+\S")
ZAHL_HINTEN = re.compile(r"\S\s+(\d{1,4})\s*$")
NUR_ZAHL = re.compile(r"^\s*(\d{1,4})\s*$")


def werkzeug(name: str) -> str:
    pfad = shutil.which(name)
    if not pfad:
        sys.exit(f"{name} nicht gefunden. Es gehoert zu Poppler (unter Windows auch in Git enthalten).")
    return pfad


FENSTER = 6  # Seiten nach vorn und hinten, aus denen der Versatz bestimmt wird


SPRUNG = 2   # Seiten, um die eine eigene Seitenzahl vom Versatz der Umgebung abweichen darf


def norm(s: str, trenner: str = "") -> str:
    """Kleinbuchstaben, Ligaturen aufgeloest, Bindestriche entfernt oder durch ein Leerzeichen ersetzt."""
    s = unicodedata.normalize("NFKC", s).lower().replace("\u00ad", "").replace("-", trenner)
    return " ".join(s.split()) if trenner else s


def passt(begriff: str, zeile: str) -> bool:
    """Hashfunktion findet Hash-Funktion, Single Sign On findet Single-Sign-On."""
    return norm(begriff) in norm(zeile) or norm(begriff, " ") in norm(zeile, " ")


def lade(txt: Path):
    """Liefert die PDF-Seiten als Liste von (erste_zeile, zeilen) und den Versatz je Seite."""
    roh = txt.read_text(encoding="utf-8", errors="replace")
    seiten, zeile = [], 1
    for block in roh.split("\f"):
        zeilen = block.split("\n")
        seiten.append((zeile, zeilen))
        zeile += len(zeilen) - 1
    def zahlen(zeilen_):
        return [int(m.group(1)) for z in zeilen_ for muster in (NUR_ZAHL, ZAHL_VORN, ZAHL_HINTEN) if (m := muster.search(z))]

    # Kolumnentitel stehen in den ersten zwei Zeilen oder in der letzten. Auf der ersten
    # Seite eines Kapitels steht die Seitenzahl oft in einer mehrzeiligen Fusszeile.
    kopf, kandidaten = {}, {}
    for i, (_, zeilen) in enumerate(seiten, start=1):
        voll = [z for z in zeilen if z.strip()]
        kopf[i] = zahlen(voll[:2] + voll[-1:])
        kandidaten[i] = kopf[i] + zahlen(voll[-3:-1])
    # Der Versatz ist nicht im ganzen Buch gleich (Vorspann, leere Seiten vor Kapiteln).
    # Deshalb je Seite der haeufigste Versatz in ihrer Umgebung.
    umgebung = {}
    for i in range(1, len(seiten) + 1):
        nah = Counter()
        for j in range(max(1, i - FENSTER), min(len(seiten), i + FENSTER) + 1):
            for n in kopf[j]:
                nah[n - j] += 1
        umgebung[i] = nah.most_common(1)[0][0] if nah else umgebung.get(i - 1, 0)
    # Springt der Versatz (leere Seite vor einem Kapitel), liegt die Umgebung auf den
    # Seiten um den Sprung falsch. Traegt die Seite selbst eine Zahl, die mit der
    # Nachbarseite fortlaeuft und nahe am erwarteten Wert liegt, gilt diese.
    versatz = {}
    for i in range(1, len(seiten) + 1):
        erwartet = i + umgebung[i]
        eigene = [n for n in kandidaten[i]
                  if abs(n - erwartet) <= SPRUNG
                  and (n + 1 in kandidaten.get(i + 1, []) or n - 1 in kandidaten.get(i - 1, []))]
        versatz[i] = min(eigene, key=lambda n: abs(n - erwartet)) - i if eigene else umgebung[i]
    return seiten, kandidaten, versatz


def buchseite(pdf_seite: int, kandidaten: dict, versatz: dict) -> str:
    erwartet = pdf_seite + versatz[pdf_seite]
    if erwartet < 1:
        return "Vorspann"
    return str(erwartet) if erwartet in kandidaten.get(pdf_seite, []) else f"~{erwartet}"


def pdf_seite_von(buch: int, seiten: list, kandidaten: dict, versatz: dict):
    """Sucht die PDF-Seite zu einer Buchseite: erst ueber den Kolumnentitel, dann ueber den Versatz."""
    for i in range(1, len(seiten) + 1):
        if i + versatz[i] == buch and buch in kandidaten.get(i, []):
            return i
    for i in range(1, len(seiten) + 1):
        if i + versatz[i] == buch:
            return i
    return None


def cmd_text(pdf: str, ziel: str) -> None:
    subprocess.run([werkzeug("pdftotext"), "-layout", "-enc", "UTF-8", pdf, ziel], check=True)
    seiten, _, versatz = lade(Path(ziel))
    mitte = versatz[len(seiten) // 2]
    print(f"{ziel}: {len(seiten)} PDF-Seiten, in der Buchmitte gilt Buchseite = PDF-Seite {mitte:+d}")


def cmd_suche(txt: str, begriffe: list[str], kontext: int) -> None:
    seiten, kandidaten, versatz = lade(Path(txt))
    for begriff in begriffe:
        treffer = []
        for i, (start, zeilen) in enumerate(seiten, start=1):
            for k, z in enumerate(zeilen):
                if passt(begriff, z):
                    treffer.append((i, start + k, k, zeilen))
        wo = sorted({buchseite(i, kandidaten, versatz) for i, *_ in treffer}, key=lambda s: int(s.lstrip("~")) if s != "Vorspann" else 0)
        print(f"\n{begriff}: {len(treffer)} Treffer" + (f" (S. {', '.join(wo[:25])}{' ...' if len(wo) > 25 else ''})" if wo else ""))
        for i, nr, k, zeilen in treffer[:40]:
            print(f"  S. {buchseite(i, kandidaten, versatz)}, Zeile {nr}: {zeilen[k].strip()[:150]}")
            for z in zeilen[k + 1:k + 1 + kontext]:
                print(f"      {z.strip()[:150]}")
        if len(treffer) > 40:
            print(f"  ... {len(treffer) - 40} weitere")


def cmd_seite(txt: str, von: int, bis: int) -> None:
    seiten, kandidaten, versatz = lade(Path(txt))
    for b in range(von, bis + 1):
        i = pdf_seite_von(b, seiten, kandidaten, versatz)
        if i is None:
            print(f"Buchseite {b} nicht gefunden.")
            continue
        start, zeilen = seiten[i - 1]
        print(f"\n===== Buchseite {b} (PDF-Seite {i}) =====")
        for k, z in enumerate(zeilen):
            print(f"{start + k:>6}  {z}")


def cmd_bild(pdf: str, txt: str, seite: int, ordner: str, ist_pdf_seite: bool) -> None:
    if ist_pdf_seite:
        i, name = seite, f"pdfseite-{seite}"
    else:
        seiten, kandidaten, versatz = lade(Path(txt))
        i, name = pdf_seite_von(seite, seiten, kandidaten, versatz), f"buchseite-{seite}"
        if i is None:
            sys.exit(f"Buchseite {seite} nicht gefunden.")
    ziel = Path(ordner)
    ziel.mkdir(parents=True, exist_ok=True)
    basis = ziel / name
    subprocess.run([werkzeug("pdftoppm"), "-f", str(i), "-l", str(i), "-r", "110", "-png", "-singlefile", pdf, str(basis)], check=True)
    print(f"{basis}.png")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    a = sys.argv[1:]
    if len(a) >= 3 and a[0] == "text":
        cmd_text(a[1], a[2])
    elif len(a) >= 3 and a[0] == "suche":
        kontext = 0
        if "--kontext" in a:
            k = a.index("--kontext")
            kontext = int(a[k + 1])
            a = a[:k] + a[k + 2:]
        cmd_suche(a[1], a[2:], kontext)
    elif len(a) >= 3 and a[0] == "seite":
        cmd_seite(a[1], int(a[2]), int(a[3]) if len(a) > 3 else int(a[2]))
    elif a and a[0] == "bild" and len([x for x in a if x != "--pdf"]) == 5:
        ist_pdf_seite = "--pdf" in a
        a = [x for x in a if x != "--pdf"]
        cmd_bild(a[1], a[2], int(a[3]), a[4], ist_pdf_seite)
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
