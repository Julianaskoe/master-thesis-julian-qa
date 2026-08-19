"""
Eksplorative subgruppeanalyser: diuretika og SGLT2-hæmmere.
Data indtastet fra skærmbillede (n=32).

Kolonner:
  diuretics : 1 = ja, 0 = nej
  sglt2     : 1 = ja, 0 = nej
  urin_p    : U-fosfat, mmol/døgn
  plasma_p  : P-fosfat, mmol/L
  u_na      : U-natrium, mmol/døgn
  gfr       : kreatininclearance, ml/min
  fe_p      : fraktionel fosfatudskillelse, %

Alle analyser er eksplorative, ikke prædefinerede i protokollen og
IKKE korrigeret for multiple sammenligninger. Hypotesegenererende.
"""

import sys

import numpy as np
import pandas as pd
from scipy import stats

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ---------------------------------------------------------------- data
raw = """
1 0 14.40 1.18  57.60 19.63000 43.17237
1 1 16.20 1.39  73.80 17.68000 45.77028
1 1 24.80 1.76 201.50 27.64000 35.39945
1 1 26.00 1.29  92.30 31.23000 44.80620
1 0  6.60 0.86  61.05 15.70000 33.93384
1 1 15.20 1.05  98.80 27.98000 35.91837
1 1 36.00 1.37 151.20 25.28000 72.18167
1 1 11.00 1.42  55.00 13.41000 40.09326
1 0 16.00 1.10 123.20 30.58000 33.02412
1 0 20.00 1.87 132.50 13.03000 56.99500
1 1 25.50 1.08 135.00 31.30000 52.37867
1 1 18.20 1.41  71.40 22.30000 41.34065
1 1 15.40 1.39  86.80 25.76000 41.80806
1 0 13.50 1.32  94.50 24.75000 28.69318
1 1 22.50 1.57  99.00 23.88000 41.66232
1 1 10.00 0.98 110.00 27.37000 25.88921
1 0 30.80 1.73 129.80 23.12000 53.46347
1 0 12.95 1.04 183.15 27.00000 32.00855
1 0 17.15 0.98 164.15 53.51000 20.76923
0 1  9.00 1.31  46.00 20.59000 23.17018
1 1 10.40 1.28  61.10 21.10000 26.73611
1 1 30.00 1.37  96.00 26.32784 57.75944
1 0 15.00 1.51 111.00  9.49000 72.65847
0 1 15.00 1.08  72.00 28.75000 33.53909
0 0  6.75 1.06  60.00 25.21055 17.54095
0 0  8.80 1.72  11.60 18.06685 19.66570
1 1 12.60 0.99  96.60 25.72016 34.36364
1 0 15.60 1.08  92.40 17.56272 43.97203
1 0 25.30 1.23 212.50 41.48629 31.67642
1 1  8.00 1.60  72.00 24.32517 14.27419
1 1 11.25 0.85  27.50 24.71547 37.18795
1 1 27.50 1.35 235.00 29.03304 48.72260
"""

cols = ["diuretics", "sglt2", "urin_p", "plasma_p", "u_na", "gfr", "fe_p"]
df = pd.DataFrame(
    [[float(x) for x in line.split()] for line in raw.strip().splitlines()],
    columns=cols,
)
df["diuretics"] = df["diuretics"].astype(int)
df["sglt2"] = df["sglt2"].astype(int)
# afledte variable
df["inv_gfr"] = 1 / df["gfr"]
df["u_na_per_gfr"] = df["u_na"] / df["gfr"]   # natriumudskillelse pr. nyrefunktion
df["urin_p_per_gfr"] = df["urin_p"] / df["gfr"]

OUTCOMES = {
    "fe_p": "FE-fosfat (%)",
    "plasma_p": "P-fosfat (mmol/L)",
    "urin_p": "U-fosfat (mmol/døgn)",
    "u_na": "U-natrium (mmol/døgn)",
    "u_na_per_gfr": "U-Na / CrCl",
    "urin_p_per_gfr": "U-P / CrCl",
    "gfr": "Kreatininclearance (ml/min)",
}


# ------------------------------------------------------- hjælpefunktioner
def desc(v):
    v = np.asarray(v, float)
    q1, med, q3 = np.percentile(v, [25, 50, 75])
    return f"{med:.2f} ({q1:.2f}–{q3:.2f})"


def rank_biserial(a, b):
    """Effektstørrelse til Mann-Whitney. -1..+1. Positiv = a > b."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    gt = sum((x > y) for x in a for y in b)
    lt = sum((x < y) for x in a for y in b)
    return (gt - lt) / (len(a) * len(b))


def hodges_lehmann(a, b, alpha=0.05):
    """Median af alle parvise differencer + fordelingsfrit 95 % CI."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = np.sort(np.array([x - y for x in a for y in b]))
    n1, n2 = len(a), len(b)
    N = n1 * n2
    est = float(np.median(d))
    # Normalapproksimation til U-fordelingen (Bauer 1972)
    z = stats.norm.ppf(1 - alpha / 2)
    se = np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12.0)
    k = int(np.floor(N / 2 - z * se))
    if k < 0:
        k = 0
    lo = d[k]
    hi = d[N - 1 - k]
    return est, float(lo), float(hi)


def mw(a, b):
    """Mann-Whitney U, eksakt hvis muligt."""
    method = "exact" if (len(a) + len(b)) <= 40 and len(set(list(a) + list(b))) == len(a) + len(b) else "asymptotic"
    try:
        res = stats.mannwhitneyu(a, b, alternative="two-sided", method=method)
    except ValueError:
        res = stats.mannwhitneyu(a, b, alternative="two-sided")
        method = "asymptotic"
    return res.statistic, res.pvalue, method


def spearman_ci(x, y, alpha=0.05):
    x, y = np.asarray(x, float), np.asarray(y, float)
    rho, p = stats.spearmanr(x, y)
    n = len(x)
    z = np.arctanh(rho)
    se = 1.0 / np.sqrt(n - 3)
    crit = stats.norm.ppf(1 - alpha / 2)
    lo, hi = np.tanh(z - crit * se), np.tanh(z + crit * se)
    return rho, p, lo, hi


def partial_spearman(x, y, z):
    """Partiel Spearman: korrelation mellem x og y justeret for z (på ranks)."""
    rx, ry, rz = (stats.rankdata(v) for v in (x, y, z))
    rxy = np.corrcoef(rx, ry)[0, 1]
    rxz = np.corrcoef(rx, rz)[0, 1]
    ryz = np.corrcoef(ry, rz)[0, 1]
    num = rxy - rxz * ryz
    den = np.sqrt((1 - rxz**2) * (1 - ryz**2))
    r = num / den
    n = len(x)
    dfree = n - 3
    t = r * np.sqrt(dfree / (1 - r**2))
    p = 2 * stats.t.sf(abs(t), dfree)
    return r, p


def rule(txt=""):
    print("\n" + "=" * 78)
    if txt:
        print(txt)
        print("=" * 78)


# ============================================================ 0. Kohorte
rule("0. GRUPPESTØRRELSER — tæl først, test bagefter")
n = len(df)
print(f"n = {n}")
print(f"  Diuretika:  ja = {df.diuretics.sum():2d} ({df.diuretics.mean()*100:.0f} %)   "
      f"nej = {(1-df.diuretics).sum():2d}")
print(f"  SGLT2i:     ja = {df.sglt2.sum():2d} ({df.sglt2.mean()*100:.0f} %)   "
      f"nej = {(1-df.sglt2).sum():2d}")
ct = pd.crosstab(df.diuretics, df.sglt2)
ct.index = ["Diuretika nej", "Diuretika ja"]
ct.columns = ["SGLT2i nej", "SGLT2i ja"]
print("\nKrydstabel:")
print(ct.to_string())
# Overlap-test
tab = ct.values
try:
    orr, pf = stats.fisher_exact(tab)
    print(f"\nFisher's exact (samvariation mellem de to præparatgrupper): p = {pf:.3f}")
except Exception as e:  # pragma: no cover
    print(e)


# ============================================ 1. SGLT2i — Mann-Whitney
rule("1. SGLT2i (ja n=%d vs. nej n=%d) — Mann-Whitney U, tosidet"
     % (df.sglt2.sum(), (1 - df.sglt2).sum()))
print(f"{'Udfald':<28}{'SGLT2i ja':>20}{'SGLT2i nej':>20}{'p':>9}{'r_rb':>8}")
print("-" * 85)
rows_sglt2 = []
for key, label in OUTCOMES.items():
    a = df.loc[df.sglt2 == 1, key].values
    b = df.loc[df.sglt2 == 0, key].values
    U, p, meth = mw(a, b)
    rb = rank_biserial(a, b)
    hl, lo, hi = hodges_lehmann(a, b)
    rows_sglt2.append((label, desc(a), desc(b), U, p, rb, hl, lo, hi, meth))
    star = " *" if p < 0.05 else ""
    print(f"{label:<28}{desc(a):>20}{desc(b):>20}{p:>9.3f}{rb:>8.2f}{star}")

print("\nMediandifferencer (Hodges-Lehmann) med fordelingsfrit 95 % CI:")
print(f"{'Udfald':<28}{'HL-diff':>10}{'95 % CI':>24}{'metode':>13}")
print("-" * 76)
for (label, _, _, U, p, rb, hl, lo, hi, meth) in rows_sglt2:
    print(f"{label:<28}{hl:>10.2f}   [{lo:>8.2f}; {hi:>8.2f}]{meth:>13}")


# =================================== 2. Diuretika — Mann-Whitney (svag)
rule("2. Diuretika (ja n=%d vs. nej n=%d) — Mann-Whitney U"
     % (df.diuretics.sum(), (1 - df.diuretics).sum()))
from math import comb
n1, n2 = int(df.diuretics.sum()), int((1 - df.diuretics).sum())
p_min = 2 / comb(n1 + n2, n2)   # mindst mulige tosidede eksakte p-værdi
print(f"!! ADVARSEL: referencegruppen er n = {n2}. Testen er stærkt underpowered.")
print(f"   Ved n1={n1}, n2={n2} er den mindst mulige tosidede eksakte p-værdi "
      f"{p_min:.4f}")
print("   (opnås kun ved FULDSTÆNDIG separation af grupperne).")
print("   Rapportér primært DESKRIPTIVT.\n")
print(f"{'Udfald':<28}{'Diuretika ja':>20}{'Diuretika nej':>20}{'p':>9}{'r_rb':>8}")
print("-" * 85)
for key, label in OUTCOMES.items():
    a = df.loc[df.diuretics == 1, key].values
    b = df.loc[df.diuretics == 0, key].values
    U, p, meth = mw(a, b)
    rb = rank_biserial(a, b)
    print(f"{label:<28}{desc(a):>20}{desc(b):>20}{p:>9.3f}{rb:>8.2f}")

print("\nDe 4 deltagere UDEN diuretika — individuelle værdier (deskriptivt):")
print(df.loc[df.diuretics == 0, ["sglt2", "urin_p", "plasma_p", "u_na", "gfr", "fe_p"]]
      .to_string(index=True, float_format=lambda v: f"{v:.2f}"))
print("\nKohortemedianer til sammenligning:")
print(df[["urin_p", "plasma_p", "u_na", "gfr", "fe_p"]].median()
      .to_string(float_format=lambda v: f"{v:.2f}"))


# ================================= 3. Kruskal-Wallis over 4 kombinationer
rule("3. Kruskal-Wallis — fire behandlingskombinationer")
df["combo"] = np.select(
    [(df.diuretics == 1) & (df.sglt2 == 1),
     (df.diuretics == 1) & (df.sglt2 == 0),
     (df.diuretics == 0) & (df.sglt2 == 1),
     (df.diuretics == 0) & (df.sglt2 == 0)],
    ["Diu+SGLT2i", "Diu alene", "SGLT2i alene", "Ingen"],
    default="",
)
order = ["Diu+SGLT2i", "Diu alene", "SGLT2i alene", "Ingen"]
sizes = df.combo.value_counts().reindex(order)
print("Gruppestørrelser: " + ", ".join(f"{k} n={int(v)}" for k, v in sizes.items()))
print("!! To grupper har n=2. Kruskal-Wallis rapporteres for fuldstændighed,")
print("   men fortolkes med forbehold; Dunn's post hoc er ikke meningsfuld her.\n")

print(f"{'Udfald':<28}{'H':>8}{'df':>4}{'p':>9}{'eps^2':>8}")
print("-" * 57)
for key, label in OUTCOMES.items():
    groups = [df.loc[df.combo == g, key].values for g in order]
    H, p = stats.kruskal(*groups)
    k, N = len(groups), len(df)
    eps2 = (H - k + 1) / (N - k)          # epsilon-squared effektstørrelse
    star = " *" if p < 0.05 else ""
    print(f"{label:<28}{H:>8.3f}{k-1:>4}{p:>9.3f}{eps2:>8.3f}{star}")

print("\nMedian (IQR) pr. gruppe:")
med = (df.groupby("combo")[list(OUTCOMES)]
         .agg(lambda s: desc(s.values)).reindex(order))
med.insert(0, "n", sizes.astype(int).values)
print(med.to_string())


# ============ 4. Stratificeret: SGLT2i inden for diuretikabrugere alene
rule("4. SGLT2i-effekt INDEN FOR diuretikabrugerne (fjerner diuretika som confounder)")
sub = df[df.diuretics == 1]
na, nb = int((sub.sglt2 == 1).sum()), int((sub.sglt2 == 0).sum())
print(f"Delkohorte: alle på diuretika, n = {len(sub)}  (SGLT2i ja n={na}, nej n={nb})\n")
print(f"{'Udfald':<28}{'SGLT2i ja':>20}{'SGLT2i nej':>20}{'p':>9}{'r_rb':>8}")
print("-" * 85)
for key, label in OUTCOMES.items():
    a = sub.loc[sub.sglt2 == 1, key].values
    b = sub.loc[sub.sglt2 == 0, key].values
    U, p, meth = mw(a, b)
    rb = rank_biserial(a, b)
    star = " *" if p < 0.05 else ""
    print(f"{label:<28}{desc(a):>20}{desc(b):>20}{p:>9.3f}{rb:>8.2f}{star}")


# ==================== 5. Korrelationer + partiel korrelation for GFR
rule("5. Korrelationer (Spearman, 95 % CI via Fishers z) og partielle korrelationer")
pairs = [
    ("gfr", "fe_p", "FE-fosfat vs. CrCl"),
    ("inv_gfr", "fe_p", "FE-fosfat vs. 1/CrCl (linearisering)"),
    ("plasma_p", "fe_p", "FE-fosfat vs. P-fosfat"),
    ("gfr", "plasma_p", "P-fosfat vs. CrCl"),
    ("gfr", "u_na", "U-natrium vs. CrCl"),
    ("gfr", "urin_p", "U-fosfat vs. CrCl"),
]
print(f"{'Sammenhæng':<40}{'rho':>7}{'95 % CI':>20}{'p':>9}")
print("-" * 76)
for x, y, label in pairs:
    rho, p, lo, hi = spearman_ci(df[x], df[y])
    star = " *" if p < 0.05 else ""
    print(f"{label:<40}{rho:>7.2f}   [{lo:>5.2f}; {hi:>5.2f}]{p:>9.3f}{star}")

print("\nPearson til sammenligning (sensitivitetsanalyse):")
for x, y, label in pairs:
    r, p = stats.pearsonr(df[x], df[y])
    print(f"{label:<40}{r:>7.2f}{'':>20}{p:>9.3f}")

print("\nPartiel Spearman — SGLT2i-status vs. udfald, justeret for CrCl:")
print(f"{'Udfald':<28}{'r_partiel':>11}{'p':>9}")
print("-" * 48)
for key, label in OUTCOMES.items():
    if key == "gfr":
        continue
    r, p = partial_spearman(df.sglt2.values, df[key].values, df.gfr.values)
    star = " *" if p < 0.05 else ""
    print(f"{label:<28}{r:>11.2f}{p:>9.3f}{star}")


# ======================================= 6. Indflydelsesanalyse (leave-one-out)
rule("6. Leave-one-out: hvor robust er FE-fosfat vs. CrCl?")
rho_full, _ = stats.spearmanr(df.gfr, df.fe_p)
r_full, _ = stats.pearsonr(df.gfr, df.fe_p)
loo_s, loo_p = [], []
for i in range(len(df)):
    d = df.drop(index=df.index[i])
    loo_s.append(stats.spearmanr(d.gfr, d.fe_p)[0])
    loo_p.append(stats.pearsonr(d.gfr, d.fe_p)[0])
loo_s, loo_p = np.array(loo_s), np.array(loo_p)
print(f"Fuld kohorte:  Spearman rho = {rho_full:+.3f}   Pearson r = {r_full:+.3f}")
print(f"Leave-one-out: Spearman  {loo_s.min():+.3f} til {loo_s.max():+.3f}"
      f"   (spændvidde {loo_s.max()-loo_s.min():.3f})")
print(f"               Pearson   {loo_p.min():+.3f} til {loo_p.max():+.3f}"
      f"   (spændvidde {loo_p.max()-loo_p.min():.3f})")
worst = int(np.argmax(np.abs(loo_p - r_full)))
print(f"\nMest indflydelsesrige observation for Pearson: række {worst+1} "
      f"(CrCl {df.gfr.iloc[worst]:.2f}, FE {df.fe_p.iloc[worst]:.2f} %) "
      f"→ r ændres til {loo_p[worst]:+.3f}")
print("Spearman er markant mere robust — brug den som primær analyse.")


# ============================================ 7. Post hoc power / MDE
rule("7. Hvor stor en forskel KUNNE du have opdaget? (post hoc, Mann-Whitney)")
n1, n2 = int(df.sglt2.sum()), int((1 - df.sglt2).sum())
za, zb = stats.norm.ppf(0.975), stats.norm.ppf(0.80)
# Normalapproksimation til Wilcoxon rank-sum, ARE 0.955 ift. t-test
d_min = (za + zb) * np.sqrt(1 / n1 + 1 / n2) / np.sqrt(0.955)
print(f"SGLT2i-analysen: n1 = {n1}, n2 = {n2}")
print(f"Mindste detekterbare effektstørrelse ved 80 % power, alfa = 0,05:")
print(f"  Cohens d ≈ {d_min:.2f}  (dvs. en STOR effekt)\n")
print(f"{'Udfald':<28}{'SD (pooled)':>13}{'MDE i enheder':>16}{'observeret diff':>18}")
print("-" * 76)
for key, label in OUTCOMES.items():
    a = df.loc[df.sglt2 == 1, key].values
    b = df.loc[df.sglt2 == 0, key].values
    sd = np.sqrt(((n1 - 1) * a.var(ddof=1) + (n2 - 1) * b.var(ddof=1)) / (n1 + n2 - 2))
    hl, _, _ = hodges_lehmann(a, b)
    print(f"{label:<28}{sd:>13.2f}{d_min*sd:>16.2f}{hl:>18.2f}")
print("\nTolkning: alt mindre end MDE-kolonnen ville du med >20 % sandsynlighed")
print("overse. Dine observerede differencer er systematisk MINDRE end MDE —")
print("nulfundene er derfor uinformative, ikke bevis for fravær af effekt.")

# ============================================ 8. Klinisk fænotype-optælling
rule("8. Kompensationsfænotyper (FE-fosfat vs. P-fosfat)")
hyper = df.plasma_p > 1.45          # øvre referencegrænse ca. 1,45 mmol/L
lowfe = df.fe_p < df.fe_p.median()
print(f"Hyperfosfatæmi (P-fosfat > 1,45 mmol/L): n = {int(hyper.sum())} "
      f"({hyper.mean()*100:.0f} %)")
print(f"Median FE-fosfat = {df.fe_p.median():.1f} %\n")
tab2 = pd.crosstab(
    pd.Series(np.where(hyper, "P-fosfat høj", "P-fosfat normal"), name=""),
    pd.Series(np.where(lowfe, "FE under median", "FE over median"), name=""),
)
print(tab2.to_string())
print("\nSvigtende kompensation = høj P-fosfat TRODS lav FE:")
fail = df[hyper & lowfe]
print(fail[["gfr", "plasma_p", "fe_p", "sglt2", "diuretics"]]
      .to_string(float_format=lambda v: f"{v:.2f}"))
try:
    orr2, pf2 = stats.fisher_exact(tab2.values)
    print(f"\nFisher's exact: p = {pf2:.3f}  (OR = {orr2:.2f})")
except Exception:
    pass


rule("SAMLET FORMULERING TIL METODEAFSNIT")
print("""
"Subgruppeanalyser efter medicinsk behandling blev udført post hoc.
Kontinuerte udfald blev sammenlignet med Mann-Whitney U-test (to grupper)
og Kruskal-Wallis-test (>2 grupper); effektstørrelser er angivet som
rank-biserial korrelation, henholdsvis epsilon-kvadreret, og
mediandifferencer som Hodges-Lehmann-estimater med fordelingsfrit 95 %
konfidensinterval. Diuretika kunne ikke klassificeres efter stofgruppe
(loop/thiazid/MRA), og analysen af diuretika er derfor begrænset til
eksponering ja/nej med kun N deltagere i referencegruppen; den rapporteres
deskriptivt. Alle analyser var eksplorative, ikke prædefinerede i
protokollen og ikke korrigeret for multiple sammenligninger, og betragtes
som hypotesegenererende."
""")
