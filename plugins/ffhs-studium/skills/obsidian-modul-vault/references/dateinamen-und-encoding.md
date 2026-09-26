# Dateinamen und Encoding

Diese Regeln existieren, weil ein Vault, dessen Dateinamen beim Entpacken verstümmelt
werden, seine internen Verlinkungen verliert. Der Inhalt der Notizen ist davon nicht
betroffen - dort sind Umlaute und Sonderzeichen problemlos.

## Regel 1 - Dateinamen und Ordnernamen: reines ASCII

Erlaubt in Datei- und Ordnernamen: `A-Z a-z 0-9 Leerzeichen - _ .`

Verboten und wodurch zu ersetzen:

| Verboten | Ersetzen durch | Beispiel |
|---|---|---|
| `–` En Dash, `—` Em Dash | `-` Bindestrich | `LE1 - Uebersicht.md` |
| `ä ö ü` | `ae oe ue` | `Uebersicht`, `Loesungen` |
| `Ä Ö Ü` | `Ae Oe Ue` | `Ueber diesen Ordner` |
| `ß` | `ss` | `Schluessel` statt `Schlüssel` |
| `„ " ' '` typografische Anführungszeichen | weglassen oder `"` | |
| `/ \ : * ? < > \|` | weglassen | von Dateisystemen ohnehin gesperrt |
| Emoji, `→`, `…` | ausschreiben | |

**Im Dateiinhalt gilt das nicht.** Überschriften, Fliesstext und Tabellen dürfen und
sollen korrektes Deutsch mit Umlauten enthalten. Nur der Dateiname ist ASCII.

Das erzeugt gelegentlich einen kleinen Bruch: Die Datei heisst `LE1 - Uebersicht.md`, die
H1-Überschrift darin lautet aber `# LE1 - Übersicht`. Das ist gewollt und stört nicht,
weil Obsidian im Explorer den Dateinamen und im Dokument die Überschrift zeigt.

## Warum das nötig ist - das Mojibake-Problem

Ein Gedankenstrich `–` (U+2013) besteht in UTF-8 aus drei Bytes: `E2 80 93`. Das
ZIP-Format besitzt zwar ein Flag, das Dateinamen als UTF-8 kennzeichnet (Bit 11 der
General Purpose Flags), aber nicht jedes Packprogramm setzt es und nicht jeder Entpacker
beachtet es. Fehlt das Flag, raten viele Entpacker - unter Windows typischerweise die
alte DOS-Codepage CP850/CP437. Dort werden die drei Bytes einzeln zu `Ô`, `Ç` und `ô`.

Aus `LE1 – Uebersicht.md` wird dann auf der Festplatte buchstäblich
`LE1 ÔÇô Uebersicht.md`. Die Wikilinks in den Notizen zeigen weiter auf den korrekten
Namen und laufen ins Leere.

Erkennungsmuster, falls jemand solche Zeichen meldet:

| Anzeige | Ursprünglich |
|---|---|
| `ÔÇô` | `–` En Dash |
| `ÔÇö` | `—` Em Dash |
| `ÔÇ£` / `ÔÇ¥` | typografische Anführungszeichen |
| `Ã¤` `Ã¶` `Ã¼` | `ä` `ö` `ü` |
| `ÃŸ` | `ß` |
| `â‚¬` | `€` |

Alles derselbe Mechanismus: UTF-8-Bytes, die als Single-Byte-Codepage gelesen werden.

## Regel 2 - Jeder Dateiname im Vault ist eindeutig

Obsidian löst `[[Wikilinks]]` primär über den Dateinamen auf, nicht über den Pfad.
Existieren mehrere Dateien gleichen Namens in verschiedenen Ordnern, wird der Link
mehrdeutig und landet unter Umständen im falschen Ordner.

Typische Falle: mehrere Ordner bekommen je eine Datei `_Ueber diesen Ordner.md`.

Richtig ist stattdessen:

```
02_Konzepte/_Ueber 02_Konzepte.md
04_Labor/_Ueber 04_Labor.md
06_Pruefung/Spickzettel-Print/_Ueber Spickzettel-Print.md
```

## Regel 3 - Wikilinks zeigen auf Notizen, nicht auf Ordner

`[[06_Pruefung/Spickzettel-Print]]` ist ein toter Link, weil der Ordner keine Notiz ist.
Verlinke stattdessen die Erklärnotiz darin.

## Regel 4 - Beim Packen das UTF-8-Flag setzen

Auch bei reinen ASCII-Namen kostet es nichts:

```bash
zip -qr -UN=UTF8 <Name>.zip <Ordner>
```

## Nachträgliche Reparatur

Falls bereits Dateien mit verbotenen Zeichen angelegt wurden: erst umbenennen, **dann**
die Wikilinks in allen Dateien nachziehen. Die Reihenfolge ist wichtig, sonst zeigen die
reparierten Links auf noch nicht umbenannte Dateien.

```bash
cd <vault>
# 1. Umbenennen
find . -type f -name '*–*' | while read -r f; do mv "$f" "$(echo "$f" | sed 's/ – / - /g')"; done
# 2. Links nachziehen (gezielt pro Linkziel, nicht global im Fliesstext)
find . -type f -name '*.md' -print0 | xargs -0 sed -i 's/\[\[LE1 – Uebersicht/[[LE1 - Uebersicht/g'
# 3. Kontrolle
python3 <skill-pfad>/scripts/pruefe_vault.py .
```

Wichtig bei Schritt 2: nur innerhalb von `[[...]]` ersetzen. Ein globales Ersetzen aller
Gedankenstriche würde auch den Fliesstext verändern, wo sie typografisch korrekt sind.
