# gymplikace

Interaktivní výukové aplikace, které fungují v prohlížeči bez přihlášení a bez instalace.

**Web:** https://aplikace.gympb.cz

## Struktura

```
index.html          katalog aplikací (úvodní stránka)
katalog.json        údaje o aplikacích, ze kterých se skládá katalog
assets/fonty/       sdílená písma (katalog: Montserrat, Atkinson Hyperlegible; Enigma: Cinzel, Source Sans 3, JetBrains Mono)
CNAME               vlastní doména pro GitHub Pages
caesarova-sifra/    jedna složka = jedna aplikace
  index.html        aplikace
  nahled.png        náhled 1200 × 630 px pro sdílení odkazu
  qr.png            QR kód na adresu aplikace
  karta.svg         ilustrace na kartě v katalogu
  fonty/            písma aplikace (pokud používá jiná než katalog)
```

## Přidání aplikace

**Před každou úpravou si přečtěte [PRAVIDLA.md](PRAVIDLA.md).** Platí pro lidi i pro nástroje (Claude, Macaly).

1. Vytvořte složku s názvem aplikace: malá písmena, bez diakritiky, slova oddělená pomlčkou (např. `vigenerova-sifra`).
2. Aplikaci uložte do složky jako `index.html`. Přidejte `nahled.png` a `qr.png`.
3. Do `katalog.json` připište záznam:

```json
{
  "slug": "vigenerova-sifra",
  "nazev": "Vigenèrova šifra",
  "popis": "Jedna až dvě věty o tom, co aplikace ukazuje.",
  "predmet": ["Informatika"],
  "rocnik": ["2R"],
  "temata": ["kryptografie", "heslo"],
  "motiv": "KLÍČ",
  "autor": "Jméno Příjmení",
  "zverejneno": "2026-11-02",
  "aktualizace": "2026-11-02",
  "stav": "nasazeno"
}
```

| Pole | Význam |
|---|---|
| `slug` | název složky aplikace |
| `predmet` | jeden nebo více předmětů; podle nich funguje filtr. Nový předmět lze založit, ale celým českým názvem s velkým počátečním písmenem (např. `"Dějepis"`) a jen pokud už neexistuje v jiném zápisu. Pro zkušební aplikace je povolený předmět `Test`. |
| `rocnik` | jeden nebo více štítků z pevného seznamu níže, seznam nelze rozšiřovat ani nechat prázdný |
| `temata` | slova, podle kterých aplikaci najde hledání |
| `obrazek` | ilustrace karty ve složce aplikace, např. `karta.svg` (poměr stran 8 : 3) |
| `motiv` | krátký text na kartě, pokud aplikace nemá ilustraci |
| `zverejneno` | datum prvního zveřejnění; vyplní se jednou a nemění se. Štítek „Nové“ se z něj počítá 14 dní. |
| `aktualizace` | datum poslední úpravy |
| `stav` | `nasazeno`, `priprava` (karta bez odkazu), `archiv` (skryto z katalogu, adresa dál funguje) |
| `odkaz` | volitelné: adresa aplikace mimo tento repozitář |

### Štítky ročníků

| Štítek | Význam |
|---|---|
| `PRI`, `SEK`, `TER`, `KVA` | prima, sekunda, tercie, kvarta |
| `1R`, `2R`, `3R`, `4R` | 1.–4. ročník (zároveň kvinta–oktáva) |
| `NG` | nižší gymnázium: PRI, SEK, TER, KVA |
| `VG` | vyšší gymnázium: 1R, 2R, 3R, 4R |
| `All` | všechny ročníky |

Filtr v katalogu nabízí ročníky PRI až 4R. Skupiny se při filtrování rozbalí: aplikace se štítkem `NG` se ukáže u PRI, SEK, TER i KVA, aplikace se štítkem `All` u všech. Na kartě se zobrazují zkratky tak, jak jsou zapsané.

Po uložení se změna do minuty objeví na webu.

## Pravidla

- Aplikace nesbírají osobní údaje, nevyžadují přihlášení a neměří návštěvnost.
- Písma se nenačítají z Google Fonts, ale z repozitáře.
- Složku vyřazené aplikace nemažte, nastavte jí v katalogu stav `archiv`. Staré odkazy a QR kódy tak budou dál fungovat.
- Licence: CC BY 4.0, viz [LICENSE](LICENSE).
