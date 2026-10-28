#!/usr/bin/env python3
"""Sestaví portfolio/index.json a zkontroluje studentské práce.

Spuštění z kořene repozitáře:
    python3 nastroje/portfolio-index.py            # zkontroluje, doplní noindex a zapíše index
    python3 nastroje/portfolio-index.py --jen-kontrola   # nic nemění, jen vypíše výsledek

Struktura (přesně pět úrovní):
    portfolio/<rok>/<predmet>/<skupina>/<tema>/<prezdivka>_<nazev-prace>/index.html
    např. portfolio/2026-27/informatika/4a-bst/binarni-soustava/kocour-tom_prevodnik/index.html

Práce se zveřejní (zapíše do indexu), jen když nemá chybu ani varování.
Práci s varováním může učitel potvrdit přidáním její cesty do portfolio/povolene.json.
Návratový kód je 1, když je nějaká chyba (CI ji tak označí).
"""
import json, re, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PF = ROOT / "portfolio"
LIMIT = 5 * 1024 * 1024
SEG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ROK = re.compile(r"^\d{4}-\d{2}$")
PRACE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*_[a-z0-9]+(?:-[a-z0-9]+)*$")
POVOLENE_SOUBORY = {"index.html", "index.json", "nazvy.json", "povolene.json"}
NOINDEX = '<meta name="robots" content="noindex, nofollow">'
EXT = [
    (re.compile(r"""<(?:script|img|iframe|source|video|audio|embed|link)\b[^>]*\b(?:src|href)\s*=\s*["']?(?:https?:)?//""", re.I), "načítá soubor z cizího serveru (src/href na http)"),
    (re.compile(r"""@import\s+(?:url\()?["']?(?:https?:)?//""", re.I), "CSS @import z cizího serveru"),
    (re.compile(r"""url\(\s*["']?(?:https?:)?//""", re.I), "CSS url() z cizího serveru"),
    (re.compile(r"""\b(?:fetch|XMLHttpRequest|sendBeacon|WebSocket|EventSource)\b[^;\n]{0,80}["']https?://""", re.I), "dotaz na cizí server z kódu"),
    (re.compile(r"""<form\b[^>]*\baction\s*=\s*["']?https?://""", re.I), "formulář odesílaný na cizí server"),
]
jen_kontrola = "--jen-kontrola" in sys.argv
chyby, varovani_vse, prace = [], [], []

def e(msg): chyby.append(msg)

def velikost(p):
    return sum(f.stat().st_size for f in p.rglob("*") if f.is_file())

def uroven(p, parts):
    """vrací seznam podsložek; soubory na jiné úrovni než povolené jsou chyba"""
    out = []
    for c in sorted(p.iterdir()):
        if c.name.startswith("."): continue
        if c.is_file():
            e(f"{'/'.join(parts) or 'portfolio'}: soubor „{c.name}“ je na špatném místě. Soubory patří jen do složky práce.")
        else:
            out.append(c)
    return out

if not PF.is_dir():
    print("Složka portfolio/ neexistuje."); sys.exit(0)

for f in PF.iterdir():
    if f.is_file() and f.name not in POVOLENE_SOUBORY and not f.name.startswith("."):
        e(f"portfolio/{f.name}: neznámý soubor v kořeni portfolia.")

try:
    povolene = set(json.loads((PF / "povolene.json").read_text("utf-8")))
except Exception:
    povolene = set()

dirs = [d for d in sorted(PF.iterdir()) if d.is_dir() and not d.name.startswith(".")]
for rok in dirs:
    if not ROK.match(rok.name): e(f"{rok.name}: školní rok má mít tvar 2026-27."); continue
    for pred in uroven(rok, [rok.name]):
        if not SEG.match(pred.name): e(f"{rok.name}/{pred.name}: název předmětu jen malá písmena bez diakritiky, číslice a pomlčky."); continue
        for sk in uroven(pred, [rok.name, pred.name]):
            if not SEG.match(sk.name): e(f"{rok.name}/{pred.name}/{sk.name}: název skupiny jen malá písmena bez diakritiky, číslice a pomlčky."); continue
            for tema in uroven(sk, [rok.name, pred.name, sk.name]):
                cesta_t = f"{rok.name}/{pred.name}/{sk.name}/{tema.name}"
                if not SEG.match(tema.name): e(f"{cesta_t}: název tématu jen malá písmena bez diakritiky, číslice a pomlčky."); continue
                for pr in uroven(tema, [rok.name, pred.name, sk.name, tema.name]):
                    cesta = f"{cesta_t}/{pr.name}"
                    if not PRACE.match(pr.name):
                        e(f"{cesta}: složka práce má mít tvar prezdivka_nazev-prace (malá písmena bez diakritiky, mezi přezdívkou a názvem podtržítko)."); continue
                    idx = pr / "index.html"
                    if not idx.is_file(): e(f"{cesta}: chybí index.html."); continue
                    var = []
                    vel = velikost(pr)
                    if vel > LIMIT: e(f"{cesta}: práce má {vel/1048576:.1f} MB, limit je {LIMIT//1048576} MB.")
                    html = idx.read_text("utf-8", errors="replace")
                    for rx, popis in EXT:
                        if rx.search(html): var.append(popis)
                    for f in pr.rglob("*"):
                        if f.is_file() and f.suffix.lower() in (".html", ".htm", ".css", ".js") and f != idx:
                            t = f.read_text("utf-8", errors="replace")
                            for rx, popis in EXT:
                                if rx.search(t): var.append(f"{f.relative_to(pr)}: {popis}")
                    if "noindex" not in html.lower():
                        if jen_kontrola: var.append("chybí značka noindex (skript ji běžně doplní)")
                        else:
                            m = re.search(r"<head[^>]*>", html, re.I)
                            if m:
                                idx.write_text(html[:m.end()] + "\n" + NOINDEX + html[m.end():], "utf-8")
                            else: var.append("chybí <head>, nelze doplnit noindex")
                    var = sorted(set(var))
                    ok_chyba = vel > LIMIT
                    schvaleno = cesta in povolene
                    zverejnit = not ok_chyba and (not var or schvaleno)
                    for v in var: varovani_vse.append(f"{cesta}: {v}" + (" (potvrzeno učitelem)" if schvaleno else ""))
                    autor, nazev = pr.name.split("_", 1)
                    prace.append(dict(rok=rok.name, predmet=pred.name, skupina=sk.name, tema=tema.name, slozka=pr.name,
                                      autor=autor, nazev=nazev, velikost=vel, zverejnit=zverejnit))

try: nazvy = json.loads((PF / "nazvy.json").read_text("utf-8"))
except Exception: nazvy = {}

vystup = dict(vygenerovano=datetime.date.today().isoformat(), nazvy=nazvy,
              prace=[{k: v for k, v in p.items() if k != "zverejnit"} for p in prace if p["zverejnit"]])
nesporne = [p for p in prace if not p["zverejnit"]]

if not jen_kontrola:
    (PF / "index.json").write_text(json.dumps(vystup, ensure_ascii=False, indent=1) + "\n", "utf-8")

print(f"Prací ve složce: {len(prace)}, zveřejněno v indexu: {len(vystup['prace'])}")
for v in varovani_vse: print("VAROVÁNÍ:", v)
for c in chyby: print("CHYBA:", c)
for p in nesporne: print(f"NEZVEŘEJNĚNO: {p['rok']}/{p['predmet']}/{p['skupina']}/{p['tema']}/{p['slozka']}")
if varovani_vse and not chyby:
    print("Práci s varováním zveřejníte přidáním její cesty do portfolio/povolene.json po kontrole učitelem.")
sys.exit(1 if chyby else 0)
