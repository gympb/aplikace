# Pravidla pro úpravy webu gymplikace

Platí pro každého, kdo do repozitáře `gympb/aplikace` (web https://aplikace.gympb.cz) zapisuje: lidi i nástroje (Claude, Macaly a další). Před každou úpravou si tato pravidla přečti.

## 1. Jediný zdroj údajů

- Údaje o aplikacích jsou **pouze** v souboru `katalog.json` v kořeni repozitáře. Web čte jen ten.
- Soupis aplikací (např. pro přehled nových aplikací) se čte z `katalog.json`.
- Soubory `metadata.json` ve složkách aplikací nevytvářej a nepoužívej je jako zdroj údajů.
- Před každou úpravou stáhni aktuální verzi repozitáře. Nikdy nepřepisuj soubor starší verzí.

## 2. Úprava katalog.json

- Měň jen záznam aplikace, které se úprava týká, a v něm jen pole, která se mají změnit.
- Ostatní pole zachovej beze změny. Nevyprazdňuj je a nepřepisuj výchozími hodnotami.
- Zachovej formát: kódování UTF-8, odsazení 2 mezery, pořadí záznamů i polí.
- Po úpravě musí být soubor platný JSON.

## 3. Pole záznamu

| Pole | Povinné | Hodnota |
|---|---|---|
| `slug` | ano | název složky aplikace: malá písmena, bez diakritiky, slova oddělená pomlčkou |
| `nazev` | ano | název aplikace |
| `popis` | ano | 1–2 věty o tom, co aplikace ukazuje |
| `predmet` | ano | jeden nebo více předmětů, viz bod 5 |
| `rocnik` | ano | jeden nebo více štítků ročníků, viz bod 4; seznam nesmí být prázdný |
| `temata` | ano | slova, podle kterých aplikaci najde hledání |
| `motiv` | ne | krátký text na kartu, pokud aplikace nemá ilustraci |
| `autor` | ano | jméno autora, jak se zobrazí na kartě a v patičce (např. jméno žáka se souhlasem nebo „žáci 3. ročníku“); nemusí to být ten, kdo aplikaci zveřejnil |
| `zverejneno` | ano* | datum prvního zveřejnění v katalogu `RRRR-MM-DD`; vyplní se jednou a **nikdy se nemění**. *Skrytá aplikace ho do prvního zveřejnění v katalogu nemá, viz bod 6c |
| `aktualizace` | ano | datum poslední úpravy `RRRR-MM-DD` |
| `zarizeni` | ano | `mobil` nebo `pocitac`, viz bod 6b |
| `stav` | ano | `nasazeno`, `skryta`, `priprava` nebo `archiv`, viz bod 6 |
| `obrazek` | ano | `karta.svg`, viz bod 7 |
| `odkaz` | ne | adresa aplikace, pokud není v tomto repozitáři |
| `pripnuto` | ne | datum připnutí na začátek výpisu `RRRR-MM-DD`, viz bod 6a |

Ukázka:

```json
{
  "slug": "vigenerova-sifra",
  "nazev": "Vigenèrova šifra",
  "popis": "Šifrování heslem a jeho prolomení Kasiského metodou.",
  "predmet": ["Informatika"],
  "rocnik": ["TER", "2R"],
  "temata": ["kryptografie", "heslo", "šifra"],
  "autor": "Jméno Příjmení",
  "zverejneno": "2026-11-02",
  "aktualizace": "2026-11-02",
  "zarizeni": "pocitac",
  "stav": "nasazeno",
  "obrazek": "karta.svg"
}
```

## 4. Ročníky: pevný seznam štítků

Používej **jen** tyto štítky. Nové nevytvářej.

| Štítek | Význam |
|---|---|
| `PRI`, `SEK`, `TER`, `KVA` | prima, sekunda, tercie, kvarta |
| `1R`, `2R`, `3R`, `4R` | 1.–4. ročník; zároveň kvinta, sexta, septima, oktáva |
| `NG` | celé nižší gymnázium (PRI, SEK, TER, KVA) |
| `VG` | celé vyšší gymnázium (1R, 2R, 3R, 4R) |
| `All` | všechny ročníky |

- Zapisuj jako text v seznamu, např. `["TER", "1R"]`. Čísla (`1`) ani názvy tříd (`"tercie"`) nepoužívej.
- Pro celou skupinu použij `NG`, `VG` nebo `All` místo výčtu jednotlivých ročníků.
- Na kartě se zobrazují zkratky tak, jak jsou zapsané.
- Filtr na úvodní stránce nabízí ročníky PRI až 4R. Skupiny se při filtrování rozbalí: aplikace se štítkem `NG` se ukáže u PRI, SEK, TER i KVA, aplikace se štítkem `All` u všech ročníků.

## 5. Předměty: otevřený seznam

- Aplikace má jeden nebo více předmětů, např. `["Fyzika", "GymTV"]`.
- Používej existující předměty z `katalog.json` (Biologie, Chemie, Fyzika, GymTV, Informatika …).
- Nový předmět lze založit, když je potřeba:
  - celým českým názvem s velkým počátečním písmenem (`"Dějepis"`, ne `"dějepis"` ani `"D"`),
  - jen pokud už neexistuje v jiném zápisu.
- Pro zkušební aplikace je povolený předmět `Test` (zapisuje se takto, ne `TEST`).

## 6. Stav a štítek „Nové“

| Stav | Význam |
|---|---|
| `nasazeno` | aplikace je zveřejněná (běžný stav) |
| `skryta` | živá aplikace mimo katalog: funguje na své adrese a s QR kódem, v katalogu ani v počtech na úvodní stránce není, viz bod 6c |
| `priprava` | rozpracovaná aplikace: karta bez odkazu, se štítkem „V přípravě“ |
| `archiv` | vyřazená aplikace: skrytá z katalogu, adresa a QR kód dál fungují |

- Štítek **„Nové“** si úvodní stránka spočítá sama z pole `zverejneno`: zobrazuje se 14 dní od zveřejnění a pak sám zmizí.
- Stav se proto kvůli štítku „Nové“ nepřepíná. Stavy `nove` a `bezne` se už nepoužívají.
- Novou aplikaci zveřejni se stavem `nasazeno` a s dnešním datem v `zverejneno` i `aktualizace`.

## 6a. Pořadí a připnutí

- Úvodní stránka řadí aplikace sama, pořadí záznamů v `katalog.json` na výpis nemá vliv:
  1. připnuté aplikace (naposledy připnutá první),
  2. ostatní od nejnovější podle `zverejneno`,
  3. aplikace ve stavu `priprava` na konci.
- Připnutí = pole `pripnuto` s dnešním datem. Připnutá karta má vpravo v řádku štítků bombu, po najetí na ni se rozvine vlaječka „BOMBA!“.
- Připnutí platí 30 dní od data v `pripnuto`, pak se aplikace zařadí mezi ostatní sama. Pole lze smazat i dříve (odepnutí).
- Připnuté smějí být nejvýš 3 aplikace. Při připnutí čtvrté se pole `pripnuto` odstraní u té, která je připnutá nejdéle.
- Připínat a odepínat smí jen správce katalogu. Aplikace ve stavu `priprava` se nepřipínají.

## 6b. Vhodnost pro mobil

| Hodnota `zarizeni` | Význam | Štítek na kartě |
|---|---|---|
| `mobil` | aplikace je optimalizována pro použití na mobilu | ikonka telefonu, „mobil“ |
| `pocitac` | aplikace potřebuje větší obrazovku nebo myš | ikonka monitoru, „na počítač“ |

- Hodnotu `mobil` smí mít jen aplikace, která na šířce displeje 390 px:
  - se vejde bez posouvání stránky do strany,
  - jde celá ovládat prstem, bez najetí myší a bez klávesnice,
  - má tlačítka a ovládací prvky nejméně 40 px velké.
- Ostatní aplikace mají `pocitac`. Když si autor není jistý, zvolí `pocitac`.
- Lišta na úvodní stránce má přepínač „Jen pro mobil“.

## 6c. Skrytá aplikace

- Stav `skryta` použije učitel, když chce aplikaci používat nebo vyzkoušet jen přes odkaz či QR kód, bez karty v katalogu (zkouška naostro, aplikace pro jednu třídu, rozpracovaná verze pro kolegu nebo garanta).
- Skrytá aplikace má normální složku `slug/` se všemi soubory podle bodu 7 a adresu `https://aplikace.gympb.cz/slug/`.
- **Skrytí nic nechrání.** Aplikace je ve veřejném repozitáři i v souboru `katalog.json` a otevře ji každý, kdo zná odkaz. Nesmí proto obsahovat nic, co by nemělo být veřejné.
- Pro skrytou aplikaci platí všechna pravidla jako pro ostatní (soukromí, cizí zdroje, licence, patička s autorem).
- Do hlavičky skryté aplikace se vloží `<meta name="robots" content="noindex">`, aby ji nezobrazovaly vyhledávače. Při přepnutí do stavu `nasazeno` se značka odstraní.
- Skrytá aplikace nemá `zverejneno`, dokud se poprvé neobjeví v katalogu. Při prvním přepnutí do stavu `nasazeno` dostane dnešní datum, a tedy i štítek „Nové“. Aplikace, která už v katalogu byla a znovu se skryje, si původní `zverejneno` ponechá.
- Skrytou aplikaci nelze připnout.

## 7. Složka aplikace

Každá aplikace má vlastní složku `slug/` s těmito soubory:

| Soubor | Obsah |
|---|---|
| `index.html` | aplikace v jednom souboru |
| `karta.svg` | ilustrace na kartu v katalogu, poměr stran 8 : 3 (např. 320 × 120) |
| `nahled.png` | náhled 1200 × 630 px pro sdílení odkazu |
| `qr.png` | QR kód na adresu `https://aplikace.gympb.cz/slug/` |
| `fonty/` | písma aplikace (pokud je používá) |

V aplikaci musí být:
- nahoře odkaz „← Všechny školní aplikace“ s `href="../"`,
- dole patička: `Autor: Jméno Příjmení · Licence CC BY 4.0 · Aktualizace: D. M. RRRR`,
- v hlavičce `<html lang="cs">`, `<meta charset="utf-8">`, `<title>`, `<meta name="description">`, `<meta name="author">`.

### Styl ilustrace karty

Humorná knižní perokresba tenkou, lehce roztřesenou sépiovou linkou s volnými, nedotaženými obrysy. Kolorovaná průsvitnými vodovými barvami s rozpitými okraji, které přesahují linku. Tlumená zemitá paleta (okr, cihlová, olivová, šedomodrá) na teplém krémovém papíře se zrnitou texturou. Stíny se šrafují šikmými čarami. Postavy jsou dobromyslné karikatury s velkou hlavou a drobným tělem. Popisky jsou psané kurzívou patkového písma. Žádné barevné přechody, 3D efekty, fotografie ani loga a značky výrobců.

## 8. Soukromí a cizí zdroje

- Aplikace nesbírají osobní údaje, nevyžadují přihlášení a **neměří návštěvnost**: žádná počítadla, analytika ani identifikátory návštěvníků.
- Nic se nenačítá z cizích serverů: písma jsou ve složce aplikace nebo v `assets/fonty/`, žádné Google Fonts, CDN ani vložené přehrávače.
- Odkazy na cizí stránky (např. video na YouTube) jsou jen obyčejné odkazy, které se otevřou v novém okně.

## 9. Co neměnit bez výslovného pokynu

- `index.html` v kořeni (úvodní stránka katalogu), `README.md`, `PRAVIDLA.md`, `CNAME`, `robots.txt`, `assets/`, `nastroje/`, `.github/`.
- Záznamy v katalogu a složky jiných aplikací.
- Složku aplikace nikdy nemaž. Vyřazená aplikace dostane stav `archiv`.

## 10. Commity

- Jeden commit = jedna změna.
- Zpráva česky ve tvaru „Název aplikace: co se změnilo“.

## 11. Portfolio studentských prací

Portfolio je oddělené od katalogu: nepatří do `katalog.json`, nezobrazuje se v katalogu a na hlavní stránce na něj vede jen odkaz v patičce. Prohlíží se na stránce `portfolio/`, která ukazuje složky jako v průzkumníku. Vyhledávače je nesmějí indexovat (`robots.txt` a značka `noindex`).

**Struktura (přesně pět úrovní):**

```
portfolio/
  2026-27/                      školní rok (tvar 2026-27)
    informatika/                předmět
      4a-bst/                   skupina studentů
        binarni-soustava/       téma
          kocour-tom_prevodnik/ práce: prezdivka_nazev-prace
            index.html
```

- Názvy všech složek jsou malá písmena bez diakritiky a mezer, slova se oddělují pomlčkou. Složka práce má tvar `prezdivka_nazev-prace` (mezi přezdívkou a názvem jedno podtržítko).
- Zobrazované názvy (např. „Binární soustava“, „4A-BST“) se berou z názvu složky. Název s diakritikou lze doplnit v `portfolio/nazvy.json` (klíč je název složky nebo celá cesta, hodnota zobrazovaný název). Žádné další soubory s údaji o práci se nepíšou.
- **Autoři jsou uvedeni jen přezdívkou nebo iniciály.** Celá jména žáků se v portfoliu a v pracích nepoužívají.
- Práce nahrává vyučující, ověří, že splňuje pravidla z bodu 8, a **zodpovídá za její obsah**. Na žádost autora nebo zákonného zástupce se práce stáhne.
- Platí totéž co pro aplikace: žádné cizí zdroje, žádná analytika, žádné odesílání dat. Odkaz zpět do portfolia je žádoucí.
- Jedna práce má nejvýše **5 MB**. Žádná videa ani velké obrázky.
- Práce se do portfolia nepřidávají přes `katalog.json` ani přes administraci v Macaly, jen nahráním složky do repozitáře.

**Kontrola a seznam prací.** Skript `nastroje/portfolio-index.py` (spouští se automaticky po každé změně ve složce `portfolio/`, ručně `python3 nastroje/portfolio-index.py`) ověří strukturu a názvy, velikost, přítomnost `index.html` a cizí zdroje, doplní `noindex` a sestaví `portfolio/index.json`. Práci s chybou ani s varováním (cizí zdroj) neuvede v seznamu. Varování může vyučující potvrdit přidáním cesty práce do `portfolio/povolene.json`. `portfolio/index.json` se nikdy nepíše ručně.

## Kontrolní seznam pro novou aplikaci

1. Složka `slug/` s `index.html`, `karta.svg`, `nahled.png`, `qr.png`.
2. V aplikaci odkaz zpět, patička s autorem a licencí, žádné cizí zdroje ani počítadla.
3. Záznam v `katalog.json` se všemi povinnými poli, ročníky jen ze seznamu v bodě 4, `zarizeni` podle bodu 6b, `stav: "nasazeno"`, `zverejneno` a `aktualizace` s dnešním datem.
4. Soubor `katalog.json` je platný JSON a ostatní záznamy zůstaly beze změny.
