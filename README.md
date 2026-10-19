# Školní aplikace Gymnázia Příbram

Interaktivní výukové aplikace, které fungují v prohlížeči bez přihlášení a bez instalace.

**Web:** https://aplikace.gympb.cz

## Struktura

```
index.html          katalog aplikací (úvodní stránka)
katalog.json        údaje o aplikacích, ze kterých se skládá katalog
assets/fonty/       písma katalogu (Montserrat, Atkinson Hyperlegible)
CNAME               vlastní doména pro GitHub Pages
caesarova-sifra/    jedna složka = jedna aplikace
  index.html        aplikace
  nahled.png        náhled 1200 × 630 px pro sdílení odkazu
  qr.png            QR kód na adresu aplikace
  fonty/            písma aplikace (pokud používá jiná než katalog)
```

## Přidání aplikace

1. Vytvořte složku s názvem aplikace: malá písmena, bez diakritiky, slova oddělená pomlčkou (např. `vigenerova-sifra`).
2. Aplikaci uložte do složky jako `index.html`. Přidejte `nahled.png` a `qr.png`.
3. Do `katalog.json` připište záznam:

```json
{
  "slug": "vigenerova-sifra",
  "nazev": "Vigenèrova šifra",
  "popis": "Jedna až dvě věty o tom, co aplikace ukazuje.",
  "predmet": ["Informatika"],
  "rocnik": [2],
  "temata": ["kryptografie", "heslo"],
  "motiv": "KLÍČ",
  "autor": "Jméno Příjmení",
  "stav": "nove",
  "aktualizace": "2026-11-02"
}
```

| Pole | Význam |
|---|---|
| `slug` | název složky aplikace |
| `predmet`, `rocnik` | podle nich fungují filtry v katalogu |
| `temata` | slova, podle kterých aplikaci najde hledání |
| `motiv` | krátký text na barevné ploše karty |
| `stav` | `nove`, `overeno` (ověřeno ve výuce), `priprava` (karta bez odkazu), `archiv` (skryto z katalogu, adresa dál funguje) |
| `odkaz` | volitelné: adresa aplikace mimo tento repozitář |

Po uložení se změna do minuty objeví na webu.

## Pravidla

- Aplikace nesbírají osobní údaje, nevyžadují přihlášení a neměří návštěvnost.
- Písma se nenačítají z Google Fonts, ale z repozitáře.
- Složku vyřazené aplikace nemažte, nastavte jí v katalogu stav `archiv`. Staré odkazy a QR kódy tak budou dál fungovat.
- Licence: CC BY 4.0, viz [LICENSE](LICENSE).
