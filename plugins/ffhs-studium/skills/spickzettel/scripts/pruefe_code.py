#!/usr/bin/env python3
"""Fuehrt die Python-Bloecke eines Spickzettels aus und stellt jedes Ergebnis neben den
'# ->'-Kommentar, damit falsche Ausgaben im Spickzettel auffallen.

    python3 pruefe_code.py <datei>

Alle ```python-Bloecke der Datei laufen der Reihe nach in einem gemeinsamen Namensraum,
so wie man sie in einer Sitzung abtippen wuerde: Imports und Definitionen aus einem
frueheren Block gelten in den spaeteren. Fuer jede Anweisung, die nur aus einem Ausdruck
besteht (z. B. 'np.linalg.det(M)'), wird das Ergebnis ausgegeben:

    Zeile 412  np.linalg.det(M)
       ist:  5.000000000000001
       soll: -> 5.0

Verglichen wird nicht automatisch - Rundung und Darstellung ('5.0' gegen
'5.000000000000001', Zeilenumbrueche in Arrays) beurteilt das Gegenlesen. Mit '!' markiert
werden nur Ausdruecke, deren Ergebnis keine einzige Zahl aus dem Kommentar enthaelt.

Ein Fehler beim Ausfuehren bricht ab und nennt die Zeile in der Datei.
Exit 0, wenn alles lief, sonst 1.
"""

import ast
import re
import sys
from pathlib import Path

BLOCK = re.compile(r"^```python[^\n]*\n(.*?)^```", re.DOTALL | re.MULTILINE)
ZAHL = re.compile(r"-?\d+(?:\.\d+)?")


def bloecke(text: str):
    """(startzeile_in_datei, code) je Python-Block."""
    for m in BLOCK.finditer(text):
        start = text.count("\n", 0, m.start(1)) + 1
        yield start, m.group(1)


def kommentar(zeile: str) -> str:
    return zeile.split("#", 1)[1].strip() if "#" in zeile else ""


def passt(ergebnis: str, soll: str) -> bool:
    """Grob: Enthaelt das Ergebnis wenigstens eine Zahl aus dem Kommentar (auf 3 Stellen)?"""
    soll_zahlen = [float(z) for z in ZAHL.findall(soll.split("->", 1)[-1])]
    if not soll_zahlen or "->" not in soll:
        return True
    ist_zahlen = [float(z) for z in ZAHL.findall(ergebnis)]
    return any(abs(i - s) < 5e-3 for s in soll_zahlen for i in ist_zahlen) or \
        soll.split("->", 1)[-1].strip().split()[0] in ergebnis


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    pfad = Path(sys.argv[1])
    text = pfad.read_text(encoding="utf-8").replace("\r\n", "\n")

    try:
        import numpy as np
        np.set_printoptions(precision=4, suppress=True)
    except ImportError:
        pass

    ns: dict = {}
    auffaellig = 0
    for start, code in bloecke(text):
        zeilen = code.splitlines()
        try:
            baum = ast.parse(code)
        except SyntaxError as e:
            print(f"Zeile {start + (e.lineno or 1) - 1}: Syntaxfehler: {e.msg}")
            return 1
        for knoten in baum.body:
            nr = start + knoten.lineno - 1
            try:
                if isinstance(knoten, ast.Expr):
                    wert = eval(compile(ast.Expression(knoten.value), str(pfad), "eval"), ns)
                    quelle = zeilen[knoten.lineno - 1]
                    soll = kommentar(quelle)
                    ist = repr(wert)
                    marke = " " if passt(ist, soll) else "!"
                    auffaellig += marke == "!"
                    print(f"{marke} Zeile {nr}  {quelle.split('#')[0].strip()}")
                    print(f"     ist:  {ist}")
                    if soll:
                        print(f"     soll: {soll}")
                else:
                    exec(compile(ast.Module([knoten], []), str(pfad), "exec"), ns)
            except Exception as e:
                print(f"Zeile {nr}: {type(e).__name__}: {e}")
                return 1

    print(f"\n{auffaellig} auffällige Ausgaben (!). Alle Ausgaben gegen die Kommentare lesen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
