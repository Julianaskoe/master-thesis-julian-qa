"""
Kreatinin-index, intern datavalidering og sensitivitetsanalyser.
Data fra det fulde skaermbillede (n=32), de tætte kolonner.

Kolonner:
  diu       : diuretika ja/nej
  sglt2     : SGLT2-haemmer ja/nej
  u_p       : U-fosfat, mmol/doegn
  p_p       : P-fosfat, mmol/L
  u_na      : U-natrium, mmol/doegn
  gfr       : kreatininclearance fra Excel-kolonnen "GFR", ml/min
  fe_p      : FE-fosfat fra Excel-kolonnen "FE p", %
  weight    : kropsvaegt, kg
  u_cr      : U-kreatinin, mmol/doegn
"""

import sys

import numpy as np
import pandas as pd
from scipy import stats

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

raw = """
1 0 14.40 1.18  57.60 19.63000 43.17237 81.0  8.4800
1 1 16.20 1.39  73.80 17.68000 45.77028 65.1  5.2200
1 1 24.80 1.76 201.50 27.64000 35.39945 71.2 10.2300
1 1 26.00 1.29  92.30 31.23000 44.80620 79.5 13.0000
1 0  6.60 0.86  61.05 15.70000 33.93384 88.9  5.8575
1 1 15.20 1.05  98.80 27.98000 35.91837 74.7  6.6500
1 1 36.00 1.37 151.20 25.28000 72.18167 99.0  9.7200
1 1 11.00 1.42  55.00 13.41000 40.09326 90.5  7.4000
1 1 16.00 1.10 123.20 30.58000 33.02412 89.0  7.8400
1 1 20.00 1.87 132.50 13.03000 56.99500 80.0  7.7500
1 1 25.50 1.08 135.00 31.30000 52.37867 72.3  8.7000
1 1 18.20 1.41  71.40 22.30000 41.34065 83.0  8.6800
1 1 15.40 1.39  86.80 25.76000 41.80806 69.3  7.4200
1 1 13.50 1.32  94.50 24.75000 28.69318 69.3  7.2000
1 1 22.50 1.57  99.00 23.88000 41.66232 77.0  9.1500
1 1 10.00 0.98 110.00 27.37000 25.88921 73.2  8.7500
1 1 30.80 1.73 129.80 23.12000 53.46347 76.0 13.4200
1 1 12.95 1.04 183.15 27.00000 32.00855 67.1  8.3250
1 1 17.15 0.98 164.15 53.51000 20.76923 88.5 15.9250
0 1  9.00 1.31  46.00 20.59000 23.17018 55.7  5.1000
1 1 10.40 1.28  61.10 21.10000 26.73611 74.0  7.0200
1 1 30.00 1.37  96.00 26.32784 57.75944 85.0 13.8000
1 1 15.00 1.51 111.00  9.49000 72.65847 90.4  5.2500
0 1 15.00 1.08  72.00 28.75000 33.53909 75.0  6.7500
0 0  6.75 1.06  60.00 25.21055 17.54095 56.6  6.8250
0 0  8.80 1.72  11.60 18.06685 19.66570 61.0  9.6000
1 1 12.60 0.99  96.60 25.72016 34.36364 70.0  7.0000
1 1 15.60 1.08  92.40 17.56272 43.97203 90.9 11.7600
1 1 25.30 1.23 212.50 41.48629 31.67642 99.0 15.0000
1 1  8.00 1.60  72.00 24.32517 14.27419 87.2  6.2000
1 1 11.25 0.85  27.50 24.71547 37.18795 77.0  5.1250
1 1 27.50 1.35 235.00 29.03304 48.72260 96.2 12.2500
"""

cols = ["diu", "sglt2", "u_p", "p_p", "u_na", "gfr", "fe_p", "weight", "u_cr"]
df = pd.DataFrame(
    [[float(x) for x in line.split()] for line in raw.strip().splitlines()],
    columns=cols,
)
df.index = np.arange(1, len(df) + 1)          # deltagernummer = raekkenummer
df["diu"] = df["diu"].astype(int)
df["sglt2"] = df["sglt2"].astype(int)

MW_CREA = 113.12          # g/mol

# ---------------------------------------------------------------- afledte
# Kreatinin-index
df["cr_idx_mg"] = df.u_cr * MW_CREA / df.weight        # mg/kg/doegn
df["cr_idx_mmol"] = df.u_cr / df.weight                # mmol/kg/doegn

# Bagudregnet P-kreatinin fra FE-formlen:
#   FE% = U_p * P_cr / (P_p * U_cr) * 100   =>   P_cr = FE * P_p * U_cr / (100 * U_p)
df["p_cr_back"] = df.fe_p * df.p_p * df.u_cr / (100 * df.u_p)      # mmol/L
df["p_cr_umol"] = df.p_cr_back * 1000
# Uafhaengig CrCl af de bagudregnede tal:  U_cr / (P_cr * 1.44)  -> ml/min
df["crcl_check"] = df.u_cr / (df.p_cr_back * 1.44)
df["gfr_diff_pct"] = (df.crcl_check - df.gfr) / df.gfr * 100

# Normaliseringer
df["inv_gfr"] = 1 / df.gfr
df["u_na_per_kg"] = df.u_na / df.weight
df["u_p_per_kg"] = df.u_p / df.weight
df["u_na_per_cr"] = df.u_na / df.u_cr        # natrium/kreatinin-ratio (volumenfri!)
df["u_p_per_cr"] = df.u_p / df.u_cr


def rule(t=""):
    print("\n" + "=" * 78)
    if t:
        print(t)
        print("=" * 78)


def spearman_ci(x, y, alpha=0.05):
    x, y = np.asarray(x, float), np.asarray(y, float)
    rho, p = stats.spearmanr(x, y)
    z, se = np.arctanh(rho), 1 / np.sqrt(len(x) - 3)
    c = stats.norm.ppf(1 - alpha / 2)
    return rho, p, np.tanh(z - c * se), np.tanh(z + c * se)


def show_corr(pairs, data, label_w=44):
    print(f"{'Sammenhaeng':<{label_w}}{'rho':>7}{'95 % CI':>20}{'p':>9}")
    print("-" * (label_w + 36))
    for x, y, lab in pairs:
        rho, p, lo, hi = spearman_ci(data[x], data[y])
        star = " *" if p < 0.05 else ""
        print(f"{lab:<{label_w}}{rho:>7.2f}   [{lo:>5.2f}; {hi:>5.2f}]{p:>9.3f}{star}")


# ================================================ 1. INTERN DATAVALIDERING
rule("1. INTERN DATAVALIDERING — stemmer GFR-kolonnen med FE-kolonnen?")
print("Metode: jeg regner P-kreatinin baglaens ud af din FE-formel og bruger den")
print("til at genberegne clearance. Hvis begge kolonner bruger samme raadata,")
print("skal de to clearance-tal vaere identiske.\n")
print(f"{'#':>3}{'P-krea (µmol/L)':>17}{'GFR-kolonne':>13}{'Genberegnet':>13}{'Afvigelse':>11}")
print("-" * 58)
bad = []
for i, r in df.iterrows():
    flag = ""
    if abs(r.gfr_diff_pct) > 1.0:
        flag = "  <-- AFVIGER"
        bad.append(i)
    print(f"{i:>3}{r.p_cr_umol:>17.1f}{r.gfr:>13.2f}{r.crcl_check:>13.2f}"
          f"{r.gfr_diff_pct:>10.2f}%{flag}")
print(f"\nRaekker med afvigelse > 1 %: {bad if bad else 'INGEN'}")
if not bad:
    print("=> Hele datasaettet er internt konsistent. FE og GFR bygger paa samme tal.")

# Plausibilitetstjek af P-kreatinin
print(f"\nP-kreatinin (bagudregnet): median {df.p_cr_umol.median():.0f} µmol/L, "
      f"range {df.p_cr_umol.min():.0f}–{df.p_cr_umol.max():.0f}")
print("Forventet ved CKD 4-5: ca. 150–500 µmol/L. Vaerdier udenfor = tjek raadata.")
odd = df[(df.p_cr_umol < 120) | (df.p_cr_umol > 600)]
if len(odd):
    print("Uplausible:")
    print(odd[["gfr", "fe_p", "p_cr_umol", "u_cr"]].to_string(
        float_format=lambda v: f"{v:.2f}"))
else:
    print("Alle P-kreatininvaerdier er fysiologisk plausible.")


# ================================================ 2. KREATININ-INDEX
rule("2. KREATININ-INDEX — er urinopsamlingerne komplette?")
ci = df.cr_idx_mg
print(f"n = {len(df)}")
print(f"  Median      {ci.median():6.2f} mg/kg/doegn   "
      f"({df.cr_idx_mmol.median():.3f} mmol/kg)")
print(f"  IQR         {ci.quantile(.25):6.2f} – {ci.quantile(.75):.2f}")
print(f"  Range       {ci.min():6.2f} – {ci.max():.2f}")
print(f"  Middel±SD   {ci.mean():6.2f} ± {ci.std(ddof=1):.2f}")

print("\nForventet doegnudskillelse (Walser, alder 75 aar):")
exp_m = 28.2 - 0.172 * 75
exp_f = 21.9 - 0.115 * 75
print(f"  Maend   {exp_m:.1f} mg/kg/doegn   (-30 % = {exp_m*0.7:.1f})")
print(f"  Kvinder {exp_f:.1f} mg/kg/doegn   (-30 % = {exp_f*0.7:.1f})")

print("\nAntal under forskellige graenser:")
for t in (12, 11, 10.7, 10, 9.3, 9, 8):
    n_ = int((ci < t).sum())
    print(f"  < {t:>4} mg/kg/doegn : {n_:>2} deltagere ({n_/len(df)*100:>4.0f} %)")

df["flag"] = ci < 10
print(f"\nPRIMAERT FLAGKRITERIUM valgt: < 10 mg/kg/doegn  ->  "
      f"{int(df.flag.sum())} flaggede\n")

print("De flaggede deltagere, sorteret efter index:")
print(df.loc[df.flag, ["cr_idx_mg", "u_cr", "weight", "gfr", "u_na", "fe_p"]]
      .sort_values("cr_idx_mg")
      .to_string(float_format=lambda v: f"{v:.2f}"))

print("\nEr flagningen skaev over clearance-spektret?")
lowgfr = df.gfr < 20
tab = pd.crosstab(
    pd.Series(np.where(lowgfr, "CrCl < 20", "CrCl >= 20"), index=df.index, name=""),
    pd.Series(np.where(df.flag, "Flagget", "OK"), index=df.index, name=""),
)
print(tab.to_string())
orr, pf = stats.fisher_exact(tab.values)
print(f"Fisher's exact: p = {pf:.3f}   OR = {orr:.2f}")

print("\nHaenger index sammen med kropsvaegt? (hvis ja, er 'lavt index' delvis")
print("bare 'stor krop', ikke daarlig opsamling)")
show_corr([("weight", "cr_idx_mg", "Kreatinin-index vs. kropsvaegt"),
           ("weight", "u_cr", "U-kreatinin (total) vs. kropsvaegt")], df)


# ============================== 3. ER INDEX KOBLET TIL CLEARANCE? (tautologi)
rule("3. KORRELERER KREATININ-INDEX MED NYREFUNKTIONEN?")
print("OBS: U-kreatinin staar i taelleren i BAADE index og CrCl. En positiv")
print("korrelation er derfor delvis regneteknisk (tautologisk).\n")
show_corr([
    ("gfr", "cr_idx_mg", "Kreatinin-index vs. CrCl  (deler U-krea!)"),
    ("p_cr_umol", "cr_idx_mg", "Kreatinin-index vs. P-kreatinin  (UAFHAENGIG)"),
    ("cr_idx_mg", "u_na", "Kreatinin-index vs. U-natrium"),
    ("cr_idx_mg", "u_p", "Kreatinin-index vs. U-fosfat"),
    ("cr_idx_mg", "fe_p", "Kreatinin-index vs. FE-fosfat"),
], df)
print("\nP-kreatinin er maalt i BLOD og er helt uafhaengig af urinopsamlingen.")
print("Hvis index ikke haenger sammen med P-kreatinin, er der ikke evidens for,")
print("at de sygeste opsamlede systematisk daarligere.")


# ================================================ 4. FE-FOSFAT
rule("4. FE-FOSFAT — kompenserer de resterende nefroner?")
show_corr([
    ("gfr", "fe_p", "FE-fosfat vs. CrCl"),
    ("inv_gfr", "fe_p", "FE-fosfat vs. 1/CrCl"),
    ("p_cr_umol", "fe_p", "FE-fosfat vs. P-kreatinin (uafh. af opsamling)"),
    ("p_p", "fe_p", "FE-fosfat vs. P-fosfat"),
    ("u_p_per_cr", "p_p", "U-fosfat/U-krea vs. P-fosfat"),
], df)

print("\nPearson til sammenligning:")
for x, y, lab in [("gfr", "fe_p", "FE-fosfat vs. CrCl"),
                  ("inv_gfr", "fe_p", "FE-fosfat vs. 1/CrCl"),
                  ("p_cr_umol", "fe_p", "FE-fosfat vs. P-kreatinin"),
                  ("p_p", "fe_p", "FE-fosfat vs. P-fosfat")]:
    r, p = stats.pearsonr(df[x], df[y])
    print(f"  {lab:<48}{r:>7.2f}{p:>9.3f}")

print("\nLeave-one-out paa FE-fosfat vs. 1/CrCl (Pearson) — hvor skroebelig er den?")
r_full = stats.pearsonr(df.inv_gfr, df.fe_p)[0]
loo = []
for i in df.index:
    d = df.drop(index=i)
    loo.append((i, stats.pearsonr(d.inv_gfr, d.fe_p)[0]))
loo_v = np.array([v for _, v in loo])
print(f"  Fuld kohorte: r = {r_full:+.3f}")
print(f"  Spaendvidde:  {loo_v.min():+.3f} til {loo_v.max():+.3f}")
worst = min(loo, key=lambda t: t[1])
print(f"  Mest indflydelsesrig: deltager {worst[0]} "
      f"(CrCl {df.gfr[worst[0]]:.2f}, FE {df.fe_p[worst[0]]:.1f} %) "
      f"-> r falder til {worst[1]:+.3f}")

print("\nRange restriction i CrCl:")
print(f"  SD(CrCl) = {df.gfr.std(ddof=1):.2f} ml/min")
print(f"  Antal under 15 ml/min: {int((df.gfr < 15).sum())}")
print(f"  Antal 15-32 ml/min:    {int(((df.gfr >= 15) & (df.gfr <= 32)).sum())}")
print(f"  Antal over 32 ml/min:  {int((df.gfr > 32).sum())}")
sd_r = df.gfr.std(ddof=1)
for sd_u in (10, 12, 14):
    r = stats.pearsonr(df.gfr, df.fe_p)[0]
    k = sd_u / sd_r
    r_corr = r * k / np.sqrt(1 - r**2 + r**2 * k**2)
    n = len(df)
    t = abs(r_corr) * np.sqrt((n - 2) / (1 - r_corr**2))
    p = 2 * stats.t.sf(t, n - 2)
    print(f"  Hvis SD havde vaeret {sd_u} ml/min -> korrigeret r = {r_corr:+.2f} "
          f"(p ≈ {p:.3f})")


# ================================================ 5. NATRIUM
rule("5. NATRIUM — udskillelse mod nyrefunktion, med og uden normalisering")
show_corr([
    ("gfr", "u_na", "U-natrium vs. CrCl"),
    ("p_cr_umol", "u_na", "U-natrium vs. P-kreatinin (uafh. af opsamling)"),
    ("gfr", "u_na_per_kg", "U-natrium/kg vs. CrCl"),
    ("gfr", "u_na_per_cr", "U-Na/U-krea vs. CrCl  (VOLUMENFRI)"),
    ("p_cr_umol", "u_na_per_cr", "U-Na/U-krea vs. P-kreatinin (dobbelt uafh.)"),
    ("gfr", "u_p", "U-fosfat vs. CrCl"),
    ("gfr", "u_p_per_cr", "U-fosfat/U-krea vs. CrCl  (VOLUMENFRI)"),
    ("gfr", "p_p", "P-fosfat vs. CrCl"),
], df)

print("\nDen volumenfri ratio U-Na/U-kreatinin er immun over for ufuldstaendig")
print("opsamling, praecis som FE. Hvis den viser samme moenster som U-Na alene,")
print("er moensteret ikke et opsamlingsartefakt.")

print("\nGruppesammenligning CrCl < 20 vs. >= 20 ml/min (Mann-Whitney):")
print(f"{'Udfald':<26}{'< 20':>18}{'>= 20':>18}{'p':>9}")
print("-" * 71)
for key, lab in [("u_na", "U-natrium"), ("u_na_per_kg", "U-natrium/kg"),
                 ("u_na_per_cr", "U-Na/U-krea"), ("u_p", "U-fosfat"),
                 ("u_p_per_cr", "U-fosfat/U-krea"), ("fe_p", "FE-fosfat"),
                 ("p_p", "P-fosfat"), ("cr_idx_mg", "Kreatinin-index")]:
    a = df.loc[df.gfr < 20, key]
    b = df.loc[df.gfr >= 20, key]
    p = stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
    star = " *" if p < 0.05 else ""
    print(f"{lab:<26}{a.median():>10.2f} (n={len(a)}){b.median():>10.2f} "
          f"(n={len(b)}){p:>9.3f}{star}")


# ================================================ 6. SENSITIVITETSANALYSE
rule("6. SENSITIVITETSANALYSE — hvad sker der uden de flaggede?")
sub = df[~df.flag]
print(f"Alle: n = {len(df)}    Uden flaggede: n = {len(sub)}")
print(f"Clearance-range: alle {df.gfr.min():.1f}–{df.gfr.max():.1f}, "
      f"uden flaggede {sub.gfr.min():.1f}–{sub.gfr.max():.1f}")
print(f"Antal med CrCl < 20:  alle {int((df.gfr<20).sum())}, "
      f"uden flaggede {int((sub.gfr<20).sum())}\n")

print(f"{'Sammenhaeng':<40}{'alle (n=32)':>22}{'uden flag (n=%d)' % len(sub):>22}")
print("-" * 84)
for x, y, lab in [
    ("gfr", "fe_p", "FE-fosfat vs. CrCl"),
    ("inv_gfr", "fe_p", "FE-fosfat vs. 1/CrCl"),
    ("p_p", "fe_p", "FE-fosfat vs. P-fosfat"),
    ("gfr", "u_na", "U-natrium vs. CrCl"),
    ("gfr", "u_na_per_cr", "U-Na/U-krea vs. CrCl"),
    ("gfr", "u_p", "U-fosfat vs. CrCl"),
    ("gfr", "p_p", "P-fosfat vs. CrCl"),
]:
    r1, p1 = stats.spearmanr(df[x], df[y])
    r2, p2 = stats.spearmanr(sub[x], sub[y])
    print(f"{lab:<40}{f'{r1:+.2f} (p={p1:.3f})':>22}{f'{r2:+.2f} (p={p2:.3f})':>22}")

print("\nVIGTIGT: tjek om eksklusionen ogsaa fjerner den nederste ende af")
print("clearance-spektret. Hvis ja, er tabet af signifikans tvetydigt.")
print("Flaggede deltageres clearance: "
      + ", ".join(f"{v:.1f}" for v in sorted(df.loc[df.flag, 'gfr'])))


# ================================================ 7. FAENOTYPER
rule("7. KOMPENSATIONSFAENOTYPER")
med_fe = df.fe_p.median()
hyper = df.p_p > 1.45
print(f"Median FE-fosfat = {med_fe:.1f} %   |   "
      f"Hyperfosfataemi (>1,45): n = {int(hyper.sum())} ({hyper.mean()*100:.0f} %)\n")

def phen(r):
    if r.p_p > 1.45 and r.fe_p < med_fe:
        return "A: svigtet (hoej P, lav FE)"
    if r.p_p > 1.45 and r.fe_p >= med_fe:
        return "B: utilstraekkelig (hoej P, hoej FE)"
    if r.p_p <= 1.45 and r.fe_p >= med_fe:
        return "C: velfungerende (normal P, hoej FE)"
    return "D: ubelastet (normal P, lav FE)"

df["faenotype"] = df.apply(phen, axis=1)
for name, g in df.groupby("faenotype"):
    print(f"{name}  — n = {len(g)}")
    print(g[["gfr", "p_p", "fe_p", "cr_idx_mg", "diu", "sglt2"]]
          .to_string(float_format=lambda v: f"{v:.2f}"))
    print()


# ================================================ 8. MEDICIN (opdateret)
rule("8. MEDICINGRUPPER I DENNE FIL")
print(f"Diuretika ja: {int(df.diu.sum())}   nej: {int((1-df.diu).sum())}")
print(f"SGLT2i    ja: {int(df.sglt2.sum())}   nej: {int((1-df.sglt2).sum())}")
print("\n!! Kontrollér disse to tal mod dit speciale (der stod 26 og 23).")
print("   Jeg kan ikke laese ja/nej-kolonnerne 100 % sikkert fra et skaermbillede.\n")
print(f"{'Udfald':<22}{'SGLT2i ja':>16}{'SGLT2i nej':>16}{'p':>9}")
print("-" * 63)
for key, lab in [("fe_p", "FE-fosfat"), ("p_p", "P-fosfat"),
                 ("u_p", "U-fosfat"), ("u_na", "U-natrium"),
                 ("u_na_per_cr", "U-Na/U-krea"), ("gfr", "CrCl"),
                 ("cr_idx_mg", "Kreatinin-index")]:
    a = df.loc[df.sglt2 == 1, key]
    b = df.loc[df.sglt2 == 0, key]
    p = stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
    star = " *" if p < 0.05 else ""
    print(f"{lab:<22}{a.median():>16.2f}{b.median():>16.2f}{p:>9.3f}{star}")


# ================================================ 9. EKSPORT
rule("9. EKSPORT")
out = df[["diu", "sglt2", "weight", "u_cr", "cr_idx_mg", "cr_idx_mmol", "flag",
          "p_cr_umol", "gfr", "crcl_check", "gfr_diff_pct", "fe_p", "p_p",
          "u_p", "u_na", "u_na_per_cr", "u_p_per_cr", "faenotype"]]
out.to_csv("analysis/beregnede_variable.csv", sep=";", decimal=",",
           float_format="%.4f", encoding="utf-8-sig")
print("Skrevet: analysis/beregnede_variable.csv")
print("(semikolon-separeret med komma som decimaltegn -> aabner direkte i dansk Excel)")
