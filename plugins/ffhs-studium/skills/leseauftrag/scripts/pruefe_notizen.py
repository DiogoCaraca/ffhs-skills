#!/usr/bin/env python3
"""Prueft Konzeptnotizen auf die Muster, die aus einer Lernunterlage einen Spickzettel
oder eine Nacherzaehlung machen.

    python3 pruefe_notizen.py <datei-oder-ordner> [<datei-oder-ordner> ...]
    python3 pruefe_notizen.py --max 500 <datei-oder-ordner> [...]
    python3 pruefe_notizen.py --quellentreue <datei-oder-ordner> [...]

Ohne Schalter: Hinweise zu Form und Umfang, bei mehreren Notizen auch zu Saetzen, die
fast gleich in zwei Notizen stehen. Jeder HINWEIS ist eine Stelle zum Nachlesen, kein
Fehler. Das Skript erkennt Muster, nicht Verstaendlichkeit: Ob eine Notiz fuer einen
Leser ohne Vorwissen verstaendlich ist, entscheidet das Gegenlesen im Skill.

Mit --max N: Die Laenge wird schon ab N Woertern gemeldet statt ab 800, fuer Notizen mit
kleinerem Budget (Lernziel der untersten Stufe).

Mit --quellentreue: Liste aller Saetze mit Kausalwoertern (weil, deshalb) und absoluten
Woertern (nur, immer, nie). Das sind die Stellen, an denen beim Ausformulieren Gruende
und Verschaerfungen entstehen, die nicht im Buch stehen. Jede Stelle am Buch pruefen.

Gedacht fuer Konzeptnotizen (02_Konzepte), nicht fuer LE-Uebersichten oder PVA-Dateien.

Exit 0, auch wenn es Hinweise gibt.
"""

import re
import sys
from pathlib import Path

LANGE_ZELLE = 12       # Woerter. Ab hier steht in der Zelle ein Satz, keine Angabe.
TABELLENANTEIL = 45    # Prozent von Kopf und Theorie, die in Tabellen stehen.
LISTENANTEIL = 50      # Prozent von Kopf und Theorie, die in Listenpunkten stehen.
MINDESTENS = 50        # Woerter in Kopf und Theorie, ab denen die Anteile zaehlen.
PFEILE = 3             # Pfeile ausserhalb von Tabellen, die keinen Wikilink einleiten.
UMBRUCH_AB = 70        # Zeichen. Laengere Textzeile mit Folgezeile = harter Umbruch.
LANG = 800             # Woerter der Notiz ohne Quelle, ab denen die Laenge einen Blick verdient.
KOPF_LANG = 80         # Woerter. Der Kopf ist das Urteil in zwei bis vier Saetzen.
SEITEN_IM_TEXT = 8     # Seitenklammern im Fliesstext. Belege stehen unter Quelle.
DUBLETTE_AB = 12       # verschiedene Woerter. Kuerzere Saetze gleichen sich zufaellig.
DUBLETTE_NAEHE = 0.6   # Anteil gemeinsamer Woerter, ab dem zwei Saetze als gleich gelten.
ERKLAER_KOEPFE = {"grund", "warum", "aussage", "erklärung", "begründung", "was es leistet"}

KAUSAL = r"weil|denn|deshalb|deswegen|daher|darum|dadurch|somit|folglich"
ABSOLUT = (r"nur|immer|nie|niemals|stets|alle|allen|aller|jede|jeder|jedes|jeden|kein|keine|keinen|keiner"
           r"|ausschliesslich|vollständig|grundsätzlich|zwingend|unmöglich|überflüssig"
           r"|einzig\w*|sämtlich\w*|höchst\w*|dieselbe\w*|derselbe\w*|dasselbe")
SIGNALWORT = re.compile(rf"\b({KAUSAL}|{ABSOLUT})\b", re.IGNORECASE)

FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)
MATH_INLINE = re.compile(r"\$[^$\n]+\$")
WIKILINK = re.compile(r"\[\[[^\]]+\]\]")
WORT = re.compile(r"[A-Za-zÄÖÜäöüß0-9][\w\-/.]*")
TRENNZEILE = re.compile(r"\|[\s:\-|]+\|?")
LISTE = re.compile(r"^([-*+]|\d+\.)\s")
SATZENDE = re.compile(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ\[\"„«(])")
SEITENKLAMMER = re.compile(r"\(S\.\s?\d")


def lies(pfad: Path) -> str:
    return pfad.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")


def woerter(text: str) -> int:
    text = WIKILINK.sub(" X ", MATH_INLINE.sub(" X ", text))
    return len(WORT.findall(text))


def zeilen_mit_art(text: str):
    """Liefert (nummer, zeile, art, abschnitt). art: text, tabelle, liste, leer, sonst."""
    abschnitt = "kopf"
    im_code = im_mathe = False
    start = len(FRONTMATTER.match(text).group(0).splitlines()) if FRONTMATTER.match(text) else 0
    for nr, zeile in enumerate(text.splitlines()[start:], start=start + 1):
        s = zeile.strip()
        if s.startswith("```"):
            im_code = not im_code
            yield nr, zeile, "sonst", abschnitt
            continue
        if s.startswith("$$"):
            if not (len(s) > 4 and s.endswith("$$")):
                im_mathe = not im_mathe
            yield nr, zeile, "sonst", abschnitt
            continue
        if im_code or im_mathe or not s:
            yield nr, zeile, "leer" if not s else "sonst", abschnitt
            continue
        if s.startswith("## "):
            abschnitt = s[3:].strip().lower()
            yield nr, zeile, "sonst", abschnitt
        elif s.startswith("#") or s.startswith(">") or zeile.startswith("    "):
            yield nr, zeile, "sonst", abschnitt
        elif s.startswith("|"):
            yield nr, zeile, "tabelle", abschnitt
        elif LISTE.match(s):
            yield nr, zeile, "liste", abschnitt
        else:
            yield nr, zeile, "text", abschnitt


def umfang(zeilen) -> tuple[int, int, int]:
    """Woerter in Kopf und Theorie: gesamt, in Tabellen, in Listen."""
    theorie = [(z, a) for _, z, a, ab in zeilen if ab in ("kopf", "theorie")]
    tab = sum(woerter(z) for z, a in theorie if a == "tabelle" and not TRENNZEILE.fullmatch(z.strip()))
    liste = sum(woerter(z) for z, a in theorie if a == "liste")
    text = sum(woerter(z) for z, a in theorie if a == "text")
    return tab + liste + text, tab, liste


def pruefe(pfad: Path) -> tuple[list[str], int]:
    zeilen = list(zeilen_mit_art(lies(pfad)))
    hinweise = []

    # 1 - Tabellenzellen, die einen Satz enthalten
    for nr, zeile, art, _ in zeilen:
        if art != "tabelle" or TRENNZEILE.fullmatch(zeile.strip()):
            continue
        for zelle in zeile.strip().strip("|").split("|"):
            n = woerter(zelle)
            if n > LANGE_ZELLE:
                hinweise.append(
                    f"Zeile {nr}: Tabellenzelle mit {n} Wörtern. Eine Zelle, die einen "
                    f"Satz braucht, erklärt etwas. Erklärung in den Text holen."
                )

    # 2 - Spaltenkoepfe, die eine Erklaerung ankuendigen
    vorher = "leer"
    for nr, zeile, art, _ in zeilen:
        if art == "tabelle" and vorher != "tabelle":
            koepfe = [k.strip().strip("*").lower() for k in zeile.strip().strip("|").split("|")]
            treffer = [k for k in koepfe if k in ERKLAER_KOEPFE]
            if treffer:
                hinweise.append(
                    f"Zeile {nr}: Spaltenkopf „{treffer[0]}\". Eine Spalte mit Begründungen "
                    f"ist eine Erklärung in Tabellenform. In den Text holen."
                )
        vorher = art

    # 3 - Kopf und Theorie, die fast nur aus Tabellen oder Listenpunkten bestehen
    gesamt, tab, liste = umfang(zeilen)
    if gesamt >= MINDESTENS and 100 * tab / gesamt > TABELLENANTEIL:
        hinweise.append(
            f"Kopf und Theorie stehen zu {round(100 * tab / gesamt)} % in Tabellen. "
            f"Sind die verglichenen Dinge vorher im Text erklärt?"
        )
    if gesamt >= MINDESTENS and 100 * liste / gesamt > LISTENANTEIL:
        hinweise.append(
            f"Kopf und Theorie stehen zu {round(100 * liste / gesamt)} % in Listenpunkten. "
            f"Brauchen die Punkte je eine Begründung, sind es Absätze."
        )

    # 4 - Pfeile anstelle von Begruendungen. Rechenschritte mit Formeln und der
    #     Abschnitt Beispiel sind ausgenommen: dort ist der Pfeil ein Folgepfeil.
    pfeile = 0
    for _, zeile, art, ab in zeilen:
        if art in ("text", "liste") and ab in ("kopf", "theorie") and "$" not in zeile:
            pfeile += len(re.findall(r"→(?!\s*\[\[)", zeile))
    if pfeile > PFEILE:
        hinweise.append(
            f"{pfeile} Pfeile im Text, die keinen Wikilink einleiten. Ein Pfeil sagt, "
            f"dass etwas folgt, aber nicht warum. Als Satz ausschreiben."
        )

    # 5 - Harte Zeilenumbrueche im Absatz
    umbrueche = []
    for (nr, zeile, art, ab), (_, _, art2, _) in zip(zeilen, zeilen[1:]):
        if ab == "quelle":
            continue
        if art == "text" and art2 == "text" and len(zeile.rstrip()) >= UMBRUCH_AB:
            umbrueche.append(nr)
    if umbrueche:
        stellen = ", ".join(str(n) for n in umbrueche[:5]) + (" ..." if len(umbrueche) > 5 else "")
        hinweise.append(
            f"Absatz über mehrere Zeilen umbrochen (Zeile {stellen}). Obsidian zeigt "
            f"jeden Zeilenumbruch an. Ein Absatz ist eine Zeile."
        )

    # 6 - Laenge. Kein Fehler, aber ein Anlass, den Filter zu pruefen.
    alles = sum(woerter(z) for _, z, a, ab in zeilen if a in ("text", "liste", "tabelle") and ab != "quelle")
    if alles > LANG:
        hinweise.append(
            f"Die Notiz hat {alles} Wörter. Steht Überblick-Stoff in Kern-Tiefe da, wird eine "
            f"Nachbarnotiz wiederholt, dient ein Absatz keiner Leitfrage, oder hätte ein "
            f"Abschnitt in der Nachbarnotiz gereicht?"
        )

    # 7 - Kopf, der mehr ist als das Urteil
    kopf = sum(woerter(z) for _, z, a, ab in zeilen if ab == "kopf" and a == "text")
    if kopf > KOPF_LANG:
        hinweise.append(
            f"Der Kopf hat {kopf} Wörter. Er sagt in zwei bis vier Sätzen, was es ist, "
            f"wozu es dient und wo die Grenze liegt."
        )

    # 8 - Seitenangaben im Fliesstext
    seiten = sum(len(SEITENKLAMMER.findall(z)) for _, z, a, ab in zeilen if a in ("text", "liste") and ab != "quelle")
    if seiten > SEITEN_IM_TEXT:
        hinweise.append(
            f"{seiten} Seitenangaben im Fliesstext. Belege stehen unter Quelle, im Text "
            f"stören sie das Lesen."
        )

    return hinweise, alles


def saetze(pfad: Path):
    """Liefert (zeile, satz, wortmenge) fuer alle laengeren Saetze ausserhalb von Quelle und Offen."""
    for nr, zeile, art, ab in zeilen_mit_art(lies(pfad)):
        if art not in ("text", "liste") or ab in ("quelle", "offen"):
            continue
        for satz in SATZENDE.split(zeile.strip()):
            menge = {w.lower() for w in WORT.findall(WIKILINK.sub(" ", satz))}
            if len(menge) >= DUBLETTE_AB:
                yield nr, satz.strip(), menge


def dubletten(dateien: list[Path]) -> list[str]:
    """Fast gleiche Saetze in zwei verschiedenen Notizen."""
    alle = [(p, nr, s, m) for p in dateien for nr, s, m in saetze(p)]
    funde = []
    for i, (p1, n1, s1, m1) in enumerate(alle):
        for p2, n2, _, m2 in alle[i + 1:]:
            if p1 != p2 and len(m1 & m2) / len(m1 | m2) >= DUBLETTE_NAEHE:
                funde.append(f"{p1.name} Zeile {n1} und {p2.name} Zeile {n2}: {s1[:110]}")
    return funde


def quellentreue(pfad: Path) -> int:
    """Gibt alle Saetze mit Kausal- oder Absolutwoertern aus. Liefert ihre Anzahl."""
    n = 0
    for nr, zeile, art, ab in zeilen_mit_art(lies(pfad)):
        if art not in ("text", "liste") or ab in ("quelle", "offen"):
            continue
        for satz in SATZENDE.split(zeile.strip()):
            treffer = sorted({m.group(1).lower() for m in SIGNALWORT.finditer(satz)})
            if treffer:
                n += 1
                print(f"   Zeile {nr} [{', '.join(treffer)}]: {satz.strip()}")
    return n


def sammle(argumente: list[str]) -> list[Path]:
    dateien = []
    for a in argumente:
        p = Path(a)
        if p.is_dir():
            dateien += sorted(q for q in p.glob("*.md") if not q.name.startswith("_"))
        elif p.is_file():
            dateien.append(p)
        else:
            print(f"Nicht gefunden: {p}")
    return dateien


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    global LANG
    argumente = [a for a in sys.argv[1:] if a != "--quellentreue"]
    if "--max" in argumente:
        i = argumente.index("--max")
        LANG = int(argumente[i + 1])
        argumente = argumente[:i] + argumente[i + 2:]
    if not argumente:
        print(__doc__)
        return 2
    dateien = sammle(argumente)

    if "--quellentreue" in sys.argv:
        for pfad in dateien:
            print(pfad.name)
            n = quellentreue(pfad)
            print(f"   {n} Sätze am Buch prüfen: Nennt das Buch diesen Grund? Schränkt es ein, wo die Notiz es nicht tut?\n")
        return 0

    mit_hinweis = summe = 0
    for pfad in dateien:
        hinweise, alles = pruefe(pfad)
        summe += alles
        print(f"{pfad.name}  ({alles} Wörter)")
        for h in hinweise:
            print(f"   HINWEIS  {h}")
        if not hinweise:
            print("   OK")
        mit_hinweis += bool(hinweise)

    if len(dateien) > 1:
        funde = dubletten(dateien)
        if funde:
            print(f"\nFast gleiche Sätze in zwei Notizen ({len(funde)}). Jede Aussage hat eine Heimat, die andere Notiz verweist:")
            for f in funde[:15]:
                print(f"   HINWEIS  {f}")
            if len(funde) > 15:
                print(f"   ... {len(funde) - 15} weitere")

    print(f"\n{len(dateien)} Notizen geprüft, {mit_hinweis} mit Hinweisen, zusammen {summe} Wörter.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
