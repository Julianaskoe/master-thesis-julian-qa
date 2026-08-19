"""Verifikation af de paastande brugeren vil fremsaette i oplaegget.
Kun med CrCl — ingen eGFR, ingen P-kreatinin (vejlederens oenske)."""

import numpy as np
import pandas as pd
from scipy import stats
from load import load, rule

df = load()

for tag, cols in [("p_wfr", df.attrs["p_wfr"]), ("p_pho", df.attrs["p_pho"]),
                  ("na_wfr", df.attrs["na_wfr"]), ("na_pho", df.attrs["na_pho"])]:
    df[f"{tag}_mean"] = df[cols].mean(axis=1)
    df[f"{tag}_n"] = df[cols].notna().sum(axis=1)

df["p_bal_wfr"] = df.p_wfr_mean - df.u_p_mg
df["p_bal_pho"] = df.p_pho_mean - df.u_p_mg
df["na_bal_wfr"] = df.na_wfr_mean - df.u_na_mg
df["na_bal_pho"] = df.na_pho_mean - df.u_na_mg
df["p_rat_wfr"] = df.u_p_mg / df.p_wfr_mean * 100
df["p_rat_pho"] = df.u_p_mg / df.p_pho_mean * 100
df["na_rat_wfr"] = df.u_na_mg / df.na_wfr_mean * 100
df["na_rat_pho"] = df.u_na_mg / df.na_pho_mean * 100


def sp(x, y, data=None):
    d = df if data is None else data
    m = d[[x, y]].dropna()
    rho, p = stats.spearmanr(m[x], m[y])
    n = len(m)
    z, se = np.arctanh(rho), 1 / np.sqrt(n - 3)
    c = stats.norm.ppf(0.975)
    return rho, p, np.tanh(z - c * se), np.tanh(z + c * se), n


def row(lab, x, y, w=44):
    rho, p, lo, hi, n = sp(x, y)
    star = " *" if p < 0.05 else ""
    print(f"{lab:<{w}}{n:>4}{rho:>7.2f}   [{lo:>5.2f}; {hi:>5.2f}]{p:>8.3f}{star}")


def head(w=44):
    print(f"{'Analyse':<{w}}{'n':>4}{'rho':>7}{'95 % CI':>19}{'p':>8}")
    print("-" * (w + 38))


# ============================================================ 1
rule("1. DIN PAASTAND: fosforbalancen er INDTAGS-styret, ikke udskillelses-styret")
head()
row("P-balance vejet vs. P-INDTAG vejet", "p_wfr_mean", "p_bal_wfr")
row("P-balance vejet vs. U-FOSFAT", "u_p_mg", "p_bal_wfr")
row("P-balance foto vs. P-INDTAG foto", "p_pho_mean", "p_bal_pho")
row("P-balance foto vs. U-FOSFAT", "u_p_mg", "p_bal_pho")
print()
row("P-ratio vejet vs. P-INDTAG vejet", "p_wfr_mean", "p_rat_wfr")
row("P-ratio vejet vs. U-FOSFAT", "u_p_mg", "p_rat_wfr")
row("P-ratio foto vs. P-INDTAG foto", "p_pho_mean", "p_rat_pho")
row("P-ratio foto vs. U-FOSFAT", "u_p_mg", "p_rat_pho")
print("\n>>> Til sammenligning: NATRIUM")
row("Na-balance vejet vs. Na-INDTAG vejet", "na_wfr_mean", "na_bal_wfr")
row("Na-balance vejet vs. U-NATRIUM", "u_na_mg", "na_bal_wfr")
row("Na-balance foto vs. Na-INDTAG foto", "na_pho_mean", "na_bal_pho")
row("Na-balance foto vs. U-NATRIUM", "u_na_mg", "na_bal_pho")

# ============================================================ 2
rule("2. VARIANSDEKOMPOSITION — hvor stor en del kommer fra udskillelsen?")
print("Var(B) = Var(I) + Var(E) - 2Cov(I,E)\n")
print(f"{'':<14}{'SD(indtag)':>12}{'SD(udskil)':>12}{'SD(balance)':>13}"
      f"{'andel E':>10}{'CV_E/CV_I':>11}")
print("-" * 72)
for I, E, B, lab in [("p_wfr_mean", "u_p_mg", "p_bal_wfr", "Fosfor vejet"),
                     ("p_pho_mean", "u_p_mg", "p_bal_pho", "Fosfor foto"),
                     ("na_wfr_mean", "u_na_mg", "na_bal_wfr", "Natrium vejet"),
                     ("na_pho_mean", "u_na_mg", "na_bal_pho", "Natrium foto")]:
    m = df[[I, E, B]].dropna()
    si, se_, sb = m[I].std(ddof=1), m[E].std(ddof=1), m[B].std(ddof=1)
    andel = se_**2 / (si**2 + se_**2) * 100
    cvi, cve = si / m[I].mean(), se_ / m[E].mean()
    print(f"{lab:<14}{si:>12.0f}{se_:>12.0f}{sb:>13.0f}{andel:>9.0f}%"
          f"{cve/cvi:>11.2f}")
print("\n>>> Kernetal til dit argument 2 om natrium:")
m = df[["na_wfr_mean", "u_na_mg"]].dropna()
si, se_ = m.na_wfr_mean.std(ddof=1), m.u_na_mg.std(ddof=1)
print(f"  Natrium: SD(udskillelse) = {se_:.0f} mg  vs. SD(indtag) = {si:.0f} mg")
print(f"           -> udskillelsen bidrager {se_**2/(si**2+se_**2)*100:.0f} % af"
      f" den samlede varians")
m = df[["p_wfr_mean", "u_p_mg"]].dropna()
si, se_ = m.p_wfr_mean.std(ddof=1), m.u_p_mg.std(ddof=1)
print(f"  Fosfor:  SD(udskillelse) = {se_:.0f} mg  vs. SD(indtag) = {si:.0f} mg")
print(f"           -> udskillelsen bidrager {se_**2/(si**2+se_**2)*100:.0f} % af"
      f" den samlede varians")

# ============================================================ 3
rule("3. E/I-FORHOLDET — hvorfor natrium er mere saarbart")
print("Hvis kun andelen k af urinen opsamles, forskydes balancen med (1-k)*E.")
print("Hvor meget det betyder afhaenger af E's stoerrelse ift. I.\n")
print(f"{'':<16}{'median I':>11}{'median E':>11}{'E/I':>8}"
      f"{'forskydn. v. k=0,8':>20}")
print("-" * 66)
for I, E, lab in [("na_wfr_mean", "u_na_mg", "Natrium vejet"),
                  ("na_pho_mean", "u_na_mg", "Natrium foto"),
                  ("p_wfr_mean", "u_p_mg", "Fosfor vejet"),
                  ("p_pho_mean", "u_p_mg", "Fosfor foto")]:
    mi, me = df[I].median(), df[E].median()
    print(f"{lab:<16}{mi:>11.0f}{me:>11.0f}{me/mi:>8.2f}{0.2*me:>19.0f} mg")

# ============================================================ 4
rule("4. NATRIUM: udskillelse og volumen-uafhaengigt maal mod clearance")
head()
row("U-natrium vs. CrCl", "gfr_sheet", "u_na_mg")
row("U-Na/U-kreatinin vs. CrCl (volumen-uafh.)", "gfr_sheet", "u_na_per_cr")
row("U-fosfat vs. CrCl", "gfr_sheet", "u_p_mg")
row("U-P/U-kreatinin vs. CrCl (volumen-uafh.)", "gfr_sheet", "u_p_per_cr")
print()


def mw(lab, y, cut=20, w=30):
    m = df[[y, "gfr_sheet"]].dropna()
    a, b = m.loc[m.gfr_sheet < cut, y], m.loc[m.gfr_sheet >= cut, y]
    p = stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
    dd = np.sort([x - y2 for x in a for y2 in b])
    hl = float(np.median(dd))
    star = " *" if p < 0.05 else ""
    print(f"{lab:<{w}}{a.median():>10.1f} ({len(a):>2}){b.median():>10.1f} "
          f"({len(b):>2}){hl:>9.1f}{p:>8.3f}{star}")


print(f"{'Mann-Whitney <20 vs >=20':<30}{'<20 (n)':>14}{'>=20 (n)':>14}"
      f"{'HL-diff':>9}{'p':>8}")
print("-" * 75)
mw("U-natrium (mg)", "u_na_mg")
mw("U-Na/U-krea (volumen-uafh.)", "u_na_per_cr")
mw("Na-balance vejet", "na_bal_wfr")
mw("Na-balance foto", "na_bal_pho")
mw("Na-ratio vejet", "na_rat_wfr")
mw("Na-ratio foto", "na_rat_pho")
mw("U-fosfat (mg)", "u_p_mg")
mw("P-balance vejet", "p_bal_wfr")
mw("P-ratio vejet", "p_rat_wfr")
mw("FE-fosfat", "fe_p")
mw("P-fosfat", "p_p")

# ============================================================ 5
rule("5. FE-FOSFAT OG P-FOSFAT mod CrCl (dine specialetal)")
head()
row("FE-fosfat vs. CrCl", "gfr_sheet", "fe_p")
row("P-fosfat vs. CrCl", "gfr_sheet", "p_p")
row("FE-fosfat vs. P-fosfat", "p_p", "fe_p")
print("\nRange restriction i CrCl:")
print(f"  SD = {df.gfr_sheet.std(ddof=1):.2f} ml/min")
q = df.gfr_sheet
print(f"  <15: {int((q<15).sum())}   15-32: {int(((q>=15)&(q<=32)).sum())}"
      f"   >32: {int((q>32).sum())}   -> "
      f"{int(((q>=15)&(q<=32)).sum())/len(q)*100:.0f} % i et baand paa 17 ml/min")
r = stats.pearsonr(df.gfr_sheet, df.fe_p)[0]
sd_r = df.gfr_sheet.std(ddof=1)
print(f"\n  Pearson r = {r:+.3f}. Korrigeret for range restriction:")
for sd_u in (10, 12, 14):
    k = sd_u / sd_r
    rc = r * k / np.sqrt(1 - r**2 + r**2 * k**2)
    t = abs(rc) * np.sqrt((len(df) - 2) / (1 - rc**2))
    p = 2 * stats.t.sf(t, len(df) - 2)
    print(f"    hvis SD var {sd_u} ml/min -> r = {rc:+.2f} (p ~ {p:.3f})")

# ============================================================ 6
rule("6. BLAND-ALTMAN: er proportional bias signifikant?")
for w_, p_, lab, unit in [("p_wfr_mean", "p_pho_mean", "Fosforindtag", "mg"),
                          ("na_wfr_mean", "na_pho_mean", "Natriumindtag", "mg")]:
    m = df[[w_, p_]].dropna()
    d = m[p_] - m[w_]
    mean_ = (m[p_] + m[w_]) / 2
    n = len(m)
    bias, sd = d.mean(), d.std(ddof=1)
    tcrit = stats.t.ppf(0.975, n - 1)
    print(f"\n{lab} (foto minus vejet), n = {n}")
    print(f"  Bias                  : {bias:+8.1f} {unit}/doegn"
          f"  (95 % CI {bias-tcrit*sd/np.sqrt(n):+.0f} til "
          f"{bias+tcrit*sd/np.sqrt(n):+.0f})")
    print(f"  SD paa differencen    : {sd:8.1f}")
    print(f"  95 % limits of agree. : {bias-1.96*sd:+8.0f} til {bias+1.96*sd:+.0f}")
    try:
        pw = stats.wilcoxon(m[p_], m[w_]).pvalue
    except Exception:
        pw = np.nan
    print(f"  Wilcoxon (bias = 0?)  : p = {pw:.3f}")
    # proportional bias: BAADE Spearman OG regression
    rho, pr = stats.spearmanr(mean_, d)
    sl, ic, rr, pp, sef = stats.linregress(mean_, d)
    print(f"  PROPORTIONAL BIAS:")
    print(f"    Spearman rho(diff, middel) = {rho:+.3f}   p = {pr:.3f}")
    print(f"    Regression: haeldning = {sl:+.4f}  (95 % CI "
          f"{sl-tcrit*sef:+.3f} til {sl+tcrit*sef:+.3f})  p = {pp:.3f}")
    print(f"    => proportional bias er "
          f"{'SIGNIFIKANT' if pp < 0.05 else 'IKKE signifikant'}")
    # er variansen konstant? (heteroskedasticitet)
    rho2, pr2 = stats.spearmanr(mean_, d.abs())
    print(f"    Heteroskedasticitet: rho(|diff|, middel) = {rho2:+.3f}"
          f"  p = {pr2:.3f}")

# ============================================================ 7
rule("7. HVOR MANGE DAGE HAR HVER METODE? (til primaer/sensitivitet)")
print(f"{'Metode':<18}{'0 dage':>8}{'1 dag':>8}{'2 dage':>8}{'3 dage':>8}"
      f"{'>=1 dag':>9}")
print("-" * 59)
for tag, lab in [("p_wfr", "Fosfor vejet"), ("p_pho", "Fosfor foto"),
                 ("na_wfr", "Natrium vejet"), ("na_pho", "Natrium foto")]:
    c = df[f"{tag}_n"].value_counts()
    print(f"{lab:<18}" + "".join(f"{int(c.get(k,0)):>8}" for k in (0, 1, 2, 3))
          + f"{int((df[f'{tag}_n']>=1).sum()):>9}")
print("\nBegge metoder tilgaengelige (matched/komplet par):")
print(f"  Fosfor : n = {int(((df.p_wfr_n>=1)&(df.p_pho_n>=1)).sum())}")
print(f"  Natrium: n = {int(((df.na_wfr_n>=1)&(df.na_pho_n>=1)).sum())}")
print(f"  Begge metoder MED 3 dage: fosfor n = "
      f"{int(((df.p_wfr_n==3)&(df.p_pho_n==3)).sum())}, natrium n = "
      f"{int(((df.na_wfr_n==3)&(df.na_pho_n==3)).sum())}")
print("\n=> Fotometoden er aarsagen: kun 9-11 deltagere har 3 fotodage.")
print("   Havde du krfaevet 3 dage for BEGGE metoder, var n faldet til ~9.")
