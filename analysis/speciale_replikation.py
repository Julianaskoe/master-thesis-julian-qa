"""
Replikation af specialets analyser med de opdaterede data.
Koerer bevidst BEGGE varianter:
  (a) "n=31" — alle deltagere som har MINDST EEN dag med den paagaeldende metode
  (b) "matched n=30" — kun deltagere som har BEGGE metoder (metodesammenligning)
og bruger baade gennemsnit og median af de tilgaengelige dage.
"""

import numpy as np
import pandas as pd
from scipy import stats
from load import load, rule, MW_P, MW_NA

df = load()

# ---- byg indtag paa BEGGE maader: gennemsnit og median af de dage der findes
for tag, cols in [("p_wfr", df.attrs["p_wfr"]), ("p_pho", df.attrs["p_pho"]),
                  ("na_wfr", df.attrs["na_wfr"]), ("na_pho", df.attrs["na_pho"])]:
    df[f"{tag}_mean"] = df[cols].mean(axis=1)
    df[f"{tag}_med"] = df[cols].median(axis=1)
    df[f"{tag}_n"] = df[cols].notna().sum(axis=1)

for agg in ("mean", "med"):
    df[f"p_bal_wfr_{agg}"] = df[f"p_wfr_{agg}"] - df.u_p_mg
    df[f"p_bal_pho_{agg}"] = df[f"p_pho_{agg}"] - df.u_p_mg
    df[f"na_bal_wfr_{agg}"] = df[f"na_wfr_{agg}"] - df.u_na_mg
    df[f"na_bal_pho_{agg}"] = df[f"na_pho_{agg}"] - df.u_na_mg
    df[f"p_rat_wfr_{agg}"] = df.u_p_mg / df[f"p_wfr_{agg}"] * 100
    df[f"p_rat_pho_{agg}"] = df.u_p_mg / df[f"p_pho_{agg}"] * 100
    df[f"na_rat_wfr_{agg}"] = df.u_na_mg / df[f"na_wfr_{agg}"] * 100
    df[f"na_rat_pho_{agg}"] = df.u_na_mg / df[f"na_pho_{agg}"] * 100

df["cr_idx"] = df.u_cr * 113.12 / df.weight
df["cr_flag"] = df.cr_idx < 10


def sp(x, y, data=None, alpha=0.05):
    d = df if data is None else data
    m = d[[x, y]].dropna()
    if len(m) < 5:
        return np.nan, np.nan, np.nan, np.nan, len(m)
    rho, p = stats.spearmanr(m[x], m[y])
    n = len(m)
    z, se = np.arctanh(rho), 1 / np.sqrt(n - 3)
    c = stats.norm.ppf(1 - alpha / 2)
    return rho, p, np.tanh(z - c * se), np.tanh(z + c * se), n


def corr_row(lab, x, y, data=None, w=38):
    rho, p, lo, hi, n = sp(x, y, data)
    if np.isnan(rho):
        print(f"{lab:<{w}}{n:>4}   for faa observationer")
        return
    star = " *" if p < 0.05 else ""
    print(f"{lab:<{w}}{n:>4}{rho:>7.2f}   [{lo:>5.2f}; {hi:>5.2f}]{p:>9.4f}{star}")


def head(w=38):
    print(f"{'Analyse':<{w}}{'n':>4}{'rho':>7}{'95 % CI':>19}{'p':>9}")
    print("-" * (w + 39))


def mw_row(lab, y, cut_var="gfr_sheet", cut=20, data=None, w=30):
    d = df if data is None else data
    m = d[[y, cut_var]].dropna()
    a, b = m.loc[m[cut_var] < cut, y], m.loc[m[cut_var] >= cut, y]
    if len(a) < 3 or len(b) < 3:
        print(f"{lab:<{w}} for faa (n={len(a)}/{len(b)})")
        return
    p = stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
    # Hodges-Lehmann
    dd = np.sort([x - y2 for x in a for y2 in b])
    hl = float(np.median(dd))
    star = " *" if p < 0.05 else ""
    print(f"{lab:<{w}}{a.median():>9.1f} ({len(a):>2}){b.median():>10.1f} "
          f"({len(b):>2}){hl:>9.1f}{p:>9.4f}{star}")


def mw_head(w=30):
    print(f"{'Udfald':<{w}}{'<20 (n)':>13}{'>=20 (n)':>14}{'HL-diff':>9}{'p':>9}")
    print("-" * (w + 45))


# ==================================================== 0. DATASAETTETS N
rule("0. HVOR MANGE DELTAGERE HAR HVILKE DATA?")
print(f"Total i filen:                       n = {len(df)}")
for tag, lab in [("p_wfr", "Fosfor, vejet"), ("p_pho", "Fosfor, foto"),
                 ("na_wfr", "Natrium, vejet"), ("na_pho", "Natrium, foto")]:
    n1 = int((df[f"{tag}_n"] >= 1).sum())
    n3 = int((df[f"{tag}_n"] == 3).sum())
    print(f"  {lab:<22} mindst 1 dag: {n1:>2}   alle 3 dage: {n3:>2}")
both_p = int(((df.p_wfr_n >= 1) & (df.p_pho_n >= 1)).sum())
both_na = int(((df.na_wfr_n >= 1) & (df.na_pho_n >= 1)).sum())
print(f"\n  BEGGE metoder, fosfor:  n = {both_p}")
print(f"  BEGGE metoder, natrium: n = {both_na}")
print("\n=> Specialets 'n=31' svarer til 'mindst een dag med mindst een metode'.")
print("   Metodesammenligningen kraever BEGGE metoder -> lavere n.")

# ==================================================== 1. GFR-VALIDERING (opdateret)
rule("1. GFR-KOLONNEN — status efter din kontrol")
df["gfr_diff"] = (df.crcl - df.gfr_sheet) / df.gfr_sheet * 100
bad = df[df.gfr_diff.abs() > 0.5]
print(f"{'#':>3}{'P-cr':>7}{'U-cr':>8}{'Din GFR':>10}{'Genberegnet':>13}{'Afvig %':>9}")
print("-" * 50)
for i, r in bad.iterrows():
    print(f"{i:>3}{r.p_cr:>7.0f}{r.u_cr:>8.3f}{r.gfr_sheet:>10.2f}"
          f"{r.crcl:>13.2f}{r.gfr_diff:>9.2f}")
print(f"\nAfvigende raekker: {list(bad.index)}")
print("\nDu har bekraeftet at 41,49 (raekke 29) og 22,30 (raekke 12) er korrekte.")
print("Det betyder, at GFR-kolonnen bruger ANDRE raadata end FE-kolonnen for")
print("disse deltagere — fx et andet urinvolumen eller en anden proeve.")
print("\nTilbage at afklare — raekke 13, 19 og 28:")
for i in (13, 19, 28):
    r = df.loc[i]
    print(f"  Raekke {i}: din GFR {r.gfr_sheet:.2f} | af FE-data {r.crcl:.2f} "
          f"| eGFR {r.egfr:.0f} | P-cr {r.p_cr:.0f} | U-cr {r.u_cr:.3f}")

# ==================================================== 2. eGFR SOM TREDJE MAAL
rule("2. eGFR — det tredje, HELT uafhaengige nyrefunktionsmaal")
print(f"eGFR: median {df.egfr.median():.0f} ml/min/1.73m2, "
      f"range {df.egfr.min():.0f}–{df.egfr.max():.0f}")
print(f"CrCl: median {df.gfr_sheet.median():.2f} ml/min, "
      f"range {df.gfr_sheet.min():.2f}–{df.gfr_sheet.max():.2f}")
print(f"\nMediandifference CrCl - eGFR: "
      f"{(df.gfr_sheet - df.egfr).median():+.2f} ml/min")
print(f"Antal hvor CrCl > eGFR: {int((df.gfr_sheet > df.egfr).sum())} af {len(df)}")
try:
    w = stats.wilcoxon(df.gfr_sheet, df.egfr)
    print(f"Wilcoxon CrCl vs. eGFR: p = {w.pvalue:.4f}")
except Exception:
    pass
print()
head()
corr_row("eGFR vs. CrCl (din kolonne)", "egfr", "gfr_sheet")
corr_row("eGFR vs. P-kreatinin", "egfr", "p_cr")
corr_row("eGFR vs. kreatinin-index", "egfr", "cr_idx")
print("\n=> eGFR bygger KUN paa P-kreatinin, alder og koen. Den kan ikke")
print("   paavirkes af urinopsamlingen. Perfekt tredje test.")

# ==================================================== 3. HOVEDKORRELATIONER
rule("3. HOVEDANALYSER — samme udfald mod TRE nyrefunktionsmaal")
for xvar, xlab, note in [
    ("gfr_sheet", "CrCl (din GFR-kolonne)", "paavirkes af opsamling"),
    ("egfr", "eGFR", "UAFHAENGIG af opsamling"),
    ("p_cr", "P-kreatinin", "UAFHAENGIG (NB: fortegn vender)"),
]:
    print(f"\n>>> mod {xlab}  ({note})")
    head()
    corr_row("FE-fosfat", xvar, "fe_p")
    corr_row("P-fosfat", xvar, "p_p")
    corr_row("U-fosfat (mg)", xvar, "u_p_mg")
    corr_row("U-natrium (mg)", xvar, "u_na_mg")
    corr_row("U-Na/U-krea (volumenfri)", xvar, "u_na_per_cr")
    corr_row("U-P/U-krea (volumenfri)", xvar, "u_p_per_cr")
    corr_row("Kreatinin-index", xvar, "cr_idx")

# ==================================================== 4. BALANCE OG RATIO
rule("4. BALANCE OG RATIO — gennemsnit vs. median af de 3 dage")
for xvar, xlab in [("gfr_sheet", "CrCl"), ("egfr", "eGFR"),
                   ("p_cr", "P-kreatinin")]:
    print(f"\n>>> mod {xvar.upper()} ({xlab})")
    head(w=42)
    for base, lab in [("p_bal_wfr", "Fosforbalance, vejet"),
                      ("p_bal_pho", "Fosforbalance, foto"),
                      ("p_rat_wfr", "Fosfor-ratio E/I, vejet"),
                      ("p_rat_pho", "Fosfor-ratio E/I, foto"),
                      ("na_bal_wfr", "Natriumbalance, vejet"),
                      ("na_bal_pho", "Natriumbalance, foto"),
                      ("na_rat_wfr", "Natrium-ratio E/I, vejet"),
                      ("na_rat_pho", "Natrium-ratio E/I, foto")]:
        corr_row(f"{lab} [gns]", xvar, f"{base}_mean", w=42)
        corr_row(f"{lab} [median]", xvar, f"{base}_med", w=42)

# ==================================================== 5. GRUPPESAMMENLIGNINGER
rule("5. GRUPPESAMMENLIGNING <20 vs. >=20 ml/min (Mann-Whitney)")
print(">>> Grænse sat paa DIN GFR-kolonne (som i specialet)\n")
mw_head()
for y, lab in [("na_bal_wfr_mean", "Na-balance vejet [gns]"),
               ("na_bal_wfr_med", "Na-balance vejet [med]"),
               ("na_bal_pho_mean", "Na-balance foto [gns]"),
               ("na_bal_pho_med", "Na-balance foto [med]"),
               ("na_rat_pho_mean", "Na-ratio foto [gns]"),
               ("p_bal_wfr_mean", "P-balance vejet [gns]"),
               ("p_bal_pho_mean", "P-balance foto [gns]"),
               ("p_rat_pho_mean", "P-ratio foto [gns]"),
               ("u_na_mg", "U-natrium (mg)"),
               ("u_na_per_cr", "U-Na/U-krea"),
               ("fe_p", "FE-fosfat"),
               ("p_p", "P-fosfat"),
               ("cr_idx", "Kreatinin-index")]:
    mw_row(lab, y)

print("\n>>> Samme grænse, men paa eGFR < 20 (uafhaengigt af opsamling)\n")
mw_head()
for y, lab in [("na_bal_wfr_mean", "Na-balance vejet [gns]"),
               ("na_bal_pho_mean", "Na-balance foto [gns]"),
               ("u_na_mg", "U-natrium (mg)"),
               ("u_na_per_cr", "U-Na/U-krea"),
               ("fe_p", "FE-fosfat"),
               ("p_p", "P-fosfat")]:
    mw_row(lab, y, cut_var="egfr")

# ==================================================== 6. SENSITIVITET
rule("6. SENSITIVITETSANALYSE — uden de 7 med kreatinin-index < 10")
sub = df[~df.cr_flag]
print(f"n = {len(df)} -> {len(sub)}\n")
print(f"{'Analyse':<34}{'alle':>19}{'uden flaggede':>19}")
print("-" * 72)
for xvar, y, lab in [
    ("egfr", "fe_p", "FE-fosfat vs. eGFR"),
    ("p_cr", "fe_p", "FE-fosfat vs. P-kreatinin"),
    ("gfr_sheet", "fe_p", "FE-fosfat vs. CrCl"),
    ("egfr", "p_p", "P-fosfat vs. eGFR"),
    ("gfr_sheet", "u_na_mg", "U-natrium vs. CrCl"),
    ("egfr", "u_na_mg", "U-natrium vs. eGFR"),
    ("gfr_sheet", "na_bal_pho_mean", "Na-balance foto vs. CrCl"),
    ("egfr", "na_bal_pho_mean", "Na-balance foto vs. eGFR"),
    ("p_cr", "p_rat_wfr_mean", "P-ratio vejet vs. P-kreatinin"),
]:
    r1, p1, *_ = sp(xvar, y)
    r2, p2, *_ = sp(xvar, y, sub)
    print(f"{lab:<34}{f'{r1:+.2f} (p={p1:.3f})':>19}{f'{r2:+.2f} (p={p2:.3f})':>19}")

# ==================================================== 7. INDTAG-PARADOKSET
rule("7. INDTAGS-PARADOKSET — korrelerer kostregistreringen med maalemetoden?")
print("Der er INGEN fysiologisk grund til at kostregistreringens indhold")
print("skulle afhaenge af hvilket nyrefunktionsmaal man bruger.\n")
head(w=42)
for base, lab in [("na_wfr_mean", "Na-indtag vejet"),
                  ("na_pho_mean", "Na-indtag foto"),
                  ("p_wfr_mean", "P-indtag vejet"),
                  ("p_pho_mean", "P-indtag foto")]:
    corr_row(f"{lab} vs. CrCl", "gfr_sheet", base, w=42)
    corr_row(f"{lab} vs. eGFR", "egfr", base, w=42)
    corr_row(f"{lab} vs. P-kreatinin", "p_cr", base, w=42)
    print()

# ==================================================== 8. DESKRIPTIVT
rule("8. DESKRIPTIV TABEL — til dine slides")
def d(v):
    v = pd.Series(v).dropna()
    return f"{v.median():.1f} ({v.quantile(.25):.1f}–{v.quantile(.75):.1f})"

print(f"{'Variabel':<34}{'n':>4}{'Median (IQR)':>26}")
print("-" * 64)
for y, lab in [("gfr_sheet", "Kreatininclearance (ml/min)"),
               ("egfr", "eGFR (ml/min/1.73m2)"),
               ("p_cr", "P-kreatinin (µmol/L)"),
               ("cr_idx", "Kreatinin-index (mg/kg/d)"),
               ("weight", "Kropsvaegt (kg)"),
               ("fe_p", "FE-fosfat (%)"),
               ("p_p", "P-fosfat (mmol/L)"),
               ("u_p_mg", "U-fosfat (mg/d)"),
               ("u_na_mg", "U-natrium (mg/d)"),
               ("p_wfr_mean", "P-indtag vejet (mg/d)"),
               ("p_pho_mean", "P-indtag foto (mg/d)"),
               ("na_wfr_mean", "Na-indtag vejet (mg/d)"),
               ("na_pho_mean", "Na-indtag foto (mg/d)"),
               ("p_bal_wfr_mean", "P-balance vejet (mg/d)"),
               ("p_bal_pho_mean", "P-balance foto (mg/d)"),
               ("na_bal_wfr_mean", "Na-balance vejet (mg/d)"),
               ("na_bal_pho_mean", "Na-balance foto (mg/d)"),
               ("p_rat_wfr_mean", "P-ratio vejet (%)"),
               ("na_rat_wfr_mean", "Na-ratio vejet (%)")]:
    v = df[y].dropna()
    print(f"{lab:<34}{len(v):>4}{d(v):>26}")

df.to_csv("speciale_alle_variable.csv", sep=";", decimal=",",
          float_format="%.4f", encoding="utf-8-sig")
print("\nSkrevet: analysis/speciale_alle_variable.csv")
