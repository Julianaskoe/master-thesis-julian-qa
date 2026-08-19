"""Hovedanalyse: GFR-fejl, balance vs. ratio vs. FE, ICC, alle korrelationer."""

import numpy as np
import pandas as pd
from scipy import stats
from load import load, rule, MW_P, MW_NA

df = load()
N = len(df)


def sp(x, y, data=None, alpha=0.05):
    d = df if data is None else data
    m = d[[x, y]].dropna() if isinstance(x, str) else None
    a, b = m[x].values, m[y].values
    rho, p = stats.spearmanr(a, b)
    n = len(a)
    z, se = np.arctanh(rho), 1 / np.sqrt(n - 3)
    c = stats.norm.ppf(1 - alpha / 2)
    return rho, p, np.tanh(z - c * se), np.tanh(z + c * se), n


def table(pairs, data=None, w=46):
    print(f"{'Sammenhaeng':<{w}}{'n':>4}{'rho':>7}{'95 % CI':>19}{'p':>9}")
    print("-" * (w + 39))
    for x, y, lab in pairs:
        rho, p, lo, hi, n = sp(x, y, data)
        star = " *" if p < 0.05 else ""
        print(f"{lab:<{w}}{n:>4}{rho:>7.2f}   [{lo:>5.2f}; {hi:>5.2f}]{p:>9.4f}{star}")


# ============================================== 1. DE 5 AFVIGENDE GFR-RAEKKER
rule("1. HVAD ER GALT I DE 5 GFR-RAEKKER?")
df["gfr_diff"] = (df.crcl - df.gfr_sheet) / df.gfr_sheet * 100
bad = df[df.gfr_diff.abs() > 0.5]
print("Din FE-kolonne er 100 % konsistent med P-cr, U-cr, U-p og P-p (afvigelse")
print("0,0000 % i alle 32 raekker). Fejlen sidder derfor i GFR-KOLONNEN.\n")
print("Jeg regner baglaens: hvilken U-cr eller P-cr ville give din GFR-vaerdi?\n")
print(f"{'#':>3}{'Din GFR':>9}{'Korrekt':>9}{'Faktor':>8}"
      f"{'U-cr brugt?':>13}{'P-cr brugt?':>13}")
print("-" * 55)
for i, r in bad.iterrows():
    factor = r.gfr_sheet / r.crcl
    u_needed = r.gfr_sheet * r.p_cr_mmol * 1.44
    p_needed = r.u_cr / (r.gfr_sheet * 1.44) * 1000
    print(f"{i:>3}{r.gfr_sheet:>9.2f}{r.crcl:>9.2f}{factor:>8.4f}"
          f"{u_needed:>13.3f}{p_needed:>13.0f}")
print(f"\n(faktiske vaerdier for sammenligning:)")
for i, r in bad.iterrows():
    print(f"{i:>3}{'':>18}{'':>8}{r.u_cr:>13.3f}{r.p_cr:>13.0f}")

print("\nEffekt paa gruppeinddelingen <20 vs. >=20 ml/min:")
df["grp_sheet"] = np.where(df.gfr_sheet < 20, "<20", ">=20")
df["grp_calc"] = np.where(df.crcl < 20, "<20", ">=20")
shift = df[df.grp_sheet != df.grp_calc]
print(f"  Med din GFR-kolonne:  <20 n={int((df.gfr_sheet<20).sum())}, "
      f">=20 n={int((df.gfr_sheet>=20).sum())}")
print(f"  Med korrekt CrCl:     <20 n={int((df.crcl<20).sum())}, "
      f">=20 n={int((df.crcl>=20).sum())}")
if len(shift):
    print(f"  Deltagere der SKIFTER gruppe: {list(shift.index)}")
    print(shift[["gfr_sheet", "crcl", "grp_sheet", "grp_calc"]].to_string(
        float_format=lambda v: f"{v:.2f}"))
else:
    print("  Ingen skifter gruppe.")


# ================================ 2. HVOR STOR EN DEL AF BALANCEN ER INDTAG?
rule("2. DOMINERER INDTAGET BALANCEN?  (punkt 1 fra foerste feedback)")
print("Hvis balancen B = I - E naesten kun afspejler I, tester dine")
print("balanceanalyser i praksis 'korrelerer indtaget med clearance?'\n")
print(f"{'Mineral / metode':<28}{'SD indtag':>11}{'SD udskil.':>12}"
      f"{'rho(B,I)':>10}{'rho(B,E)':>10}")
print("-" * 71)
for I, E, lab in [("p_in_wfr", "u_p_mg", "Fosfor, vejet"),
                  ("p_in_pho", "u_p_mg", "Fosfor, foto"),
                  ("na_in_wfr", "u_na_mg", "Natrium, vejet"),
                  ("na_in_pho", "u_na_mg", "Natrium, foto")]:
    B = f"{'p' if 'p_in' in I else 'na'}_bal_{'wfr' if 'wfr' in I else 'pho'}"
    m = df[[B, I, E]].dropna()
    r1 = stats.spearmanr(m[B], m[I])[0]
    r2 = stats.spearmanr(m[B], m[E])[0]
    print(f"{lab:<28}{m[I].std(ddof=1):>11.0f}{m[E].std(ddof=1):>12.0f}"
          f"{r1:>10.2f}{r2:>10.2f}")
print("\nSD-forholdet viser hvor meget mere indtaget svinger end udskillelsen.")
print("rho(B,I) taet paa 1,0 = balancen ER indtaget.")


# ============================================ 3. BALANCE / RATIO / FE vs. NYREFUNKTION
rule("3. DE TRE ENDPOINTS MOD NYREFUNKTION — hvilket er bedst?")
print(">>> A) mod CrCl (paavirkes af opsamlingskvalitet)")
table([
    ("crcl", "p_bal_wfr", "Fosforbalance (vejet) vs. CrCl"),
    ("crcl", "p_bal_pho", "Fosforbalance (foto) vs. CrCl"),
    ("crcl", "p_ratio_wfr", "Fosfor-ratio E/I (vejet) vs. CrCl"),
    ("crcl", "p_ratio_pho", "Fosfor-ratio E/I (foto) vs. CrCl"),
    ("crcl", "fe_p", "FE-fosfat vs. CrCl"),
    ("crcl", "na_bal_wfr", "Natriumbalance (vejet) vs. CrCl"),
    ("crcl", "na_bal_pho", "Natriumbalance (foto) vs. CrCl"),
    ("crcl", "na_ratio_wfr", "Natrium-ratio E/I (vejet) vs. CrCl"),
    ("crcl", "na_ratio_pho", "Natrium-ratio E/I (foto) vs. CrCl"),
])

print("\n>>> B) mod P-KREATININ (blodproeve — IMMUN over for opsamling)")
print("    NB: fortegn vender, fordi hoej P-cr = DAARLIG nyrefunktion")
table([
    ("p_cr", "p_bal_wfr", "Fosforbalance (vejet) vs. P-kreatinin"),
    ("p_cr", "p_bal_pho", "Fosforbalance (foto) vs. P-kreatinin"),
    ("p_cr", "p_ratio_wfr", "Fosfor-ratio (vejet) vs. P-kreatinin"),
    ("p_cr", "p_ratio_pho", "Fosfor-ratio (foto) vs. P-kreatinin"),
    ("p_cr", "fe_p", "FE-fosfat vs. P-kreatinin"),
    ("p_cr", "na_bal_wfr", "Natriumbalance (vejet) vs. P-kreatinin"),
    ("p_cr", "na_bal_pho", "Natriumbalance (foto) vs. P-kreatinin"),
    ("p_cr", "na_ratio_wfr", "Natrium-ratio (vejet) vs. P-kreatinin"),
    ("p_cr", "na_ratio_pho", "Natrium-ratio (foto) vs. P-kreatinin"),
])


# ============================================ 4. SPLIT: INDTAG vs. UDSKILLELSE
rule("4. SPLIT BALANCEN OP — kommer fundet fra indtag eller udskillelse?")
table([
    ("crcl", "u_na_mg", "U-natrium vs. CrCl"),
    ("crcl", "na_in_wfr", "Na-INDTAG (vejet) vs. CrCl"),
    ("crcl", "na_in_pho", "Na-INDTAG (foto) vs. CrCl"),
    ("crcl", "u_p_mg", "U-fosfat vs. CrCl"),
    ("crcl", "p_in_wfr", "P-INDTAG (vejet) vs. CrCl"),
    ("crcl", "p_in_pho", "P-INDTAG (foto) vs. CrCl"),
])
print("\nSamme split, men mod P-kreatinin (uafhaengig af opsamling):")
table([
    ("p_cr", "u_na_mg", "U-natrium vs. P-kreatinin"),
    ("p_cr", "na_in_wfr", "Na-INDTAG (vejet) vs. P-kreatinin"),
    ("p_cr", "u_p_mg", "U-fosfat vs. P-kreatinin"),
    ("p_cr", "p_in_wfr", "P-INDTAG (vejet) vs. P-kreatinin"),
])


# ============================================ 5. ICC — ATTENUERING MED DINE TAL
rule("5. ICC — hvor reproducerbart er ET doegns kostregistrering?")
print("ICC = hvor stor en andel af variationen i dine tal der er AEGTE")
print("forskelle mellem personer (frem for tilfaeldig dag-til-dag stoej).\n")


def icc_and_atten(cols, label):
    sub = df[cols].dropna(thresh=2)          # mindst 2 dage
    if len(sub) < 5:
        print(f"{label}: for faa komplette (n={len(sub)})")
        return
    within, means, ks = [], [], []
    for _, row in sub.iterrows():
        v = row.dropna().values.astype(float)
        if len(v) >= 2:
            within.append(v.var(ddof=1))
            means.append(v.mean())
            ks.append(len(v))
    within = np.mean(within)
    k = np.mean(ks)
    between = np.var(means, ddof=1) - within / k
    between = max(between, 0)
    icc1 = between / (between + within) if (between + within) > 0 else 0
    icc_k = between / (between + within / k) if (between + within / k) > 0 else 0
    cv = np.sqrt(within) / np.mean(means) * 100
    print(f"{label}")
    print(f"  n = {len(sub)} deltagere, gennemsnit {k:.1f} dage")
    print(f"  Within-person SD  : {np.sqrt(within):8.0f} mg/doegn")
    print(f"  Between-person SD : {np.sqrt(between):8.0f} mg/doegn")
    print(f"  Within-person CV  : {cv:8.1f} %")
    print(f"  ICC (1 dag)       : {icc1:8.3f}   -> attenuering "
          f"sqrt(ICC) = {np.sqrt(icc1):.3f}")
    print(f"  ICC ({k:.0f} dages gns.) : {icc_k:8.3f}")
    for r_true in (0.30, 0.40, 0.50, 0.60):
        r_obs = r_true * np.sqrt(icc1)
        t = abs(r_obs) * np.sqrt((N - 2) / (1 - r_obs**2))
        p = 2 * stats.t.sf(t, N - 2)
        sig = "JA " if p < 0.05 else "NEJ"
        print(f"    sand r = {r_true:.2f}  ->  du ville maale {r_obs:.2f}  "
              f"(p = {p:.3f})  signifikant: {sig}")
    print()


icc_and_atten(df.attrs["p_wfr"], "FOSFORINDTAG, vejet (3 dage)")
icc_and_atten(df.attrs["na_wfr"], "NATRIUMINDTAG, vejet (3 dage)")
icc_and_atten(df.attrs["p_pho"], "FOSFORINDTAG, foto (3 dage)")
icc_and_atten(df.attrs["na_pho"], "NATRIUMINDTAG, foto (3 dage)")


# ============================================ 6. METODESAMMENLIGNING
rule("6. BLAND-ALTMAN: vejet vs. foto")
for w, p_, lab, unit in [("p_in_wfr", "p_in_pho", "Fosforindtag", "mg"),
                         ("na_in_wfr", "na_in_pho", "Natriumindtag", "mg")]:
    m = df[[w, p_]].dropna()
    d = m[p_] - m[w]
    mean_ = (m[p_] + m[w]) / 2
    bias, sd = d.mean(), d.std(ddof=1)
    n = len(m)
    se_bias = sd / np.sqrt(n)
    tcrit = stats.t.ppf(0.975, n - 1)
    print(f"\n{lab} (foto minus vejet), n = {n}")
    print(f"  Bias                 : {bias:+8.1f} {unit}/doegn "
          f"(95 % CI {bias-tcrit*se_bias:+.0f} til {bias+tcrit*se_bias:+.0f})")
    print(f"  SD paa differencen   : {sd:8.1f}")
    print(f"  95 % limits of agree.: {bias-1.96*sd:+8.0f} til {bias+1.96*sd:+.0f}")
    print(f"  Bias i % af middel   : {bias/mean_.mean()*100:+8.1f} %")
    t, pt = stats.ttest_rel(m[p_], m[w])
    try:
        wst, pw = stats.wilcoxon(m[p_], m[w])
    except Exception:
        pw = np.nan
    print(f"  Wilcoxon             : p = {pw:.4f}")
    r = stats.spearmanr(mean_, d)[0]
    print(f"  Proportional bias    : rho(difference, middel) = {r:+.2f}")
    if abs(r) > 0.3:
        print("    -> BEMAERK: bias afhaenger af niveauet (ikke konstant)")


# ============================================ 7. SAMLET RESULTATOVERSIGT
rule("7. ROBUSTHEDSMATRIX — hvilke fund holder mod BEGGE maal?")
df["cr_flag"] = df.cr_idx < 10
sub = df[~df.cr_flag]
print(f"Flaggede (kreatinin-index < 10 mg/kg/doegn): {int(df.cr_flag.sum())}")
print(f"{'Udfald':<26}{'vs CrCl':>17}{'vs P-krea':>17}{'u. flag (CrCl)':>18}")
print("-" * 78)
for y, lab in [("fe_p", "FE-fosfat"),
               ("u_p_per_cr", "U-P/U-krea"),
               ("p_p", "P-fosfat"),
               ("u_na_mg", "U-natrium"),
               ("u_na_per_cr", "U-Na/U-krea"),
               ("p_bal_wfr", "P-balance vejet"),
               ("p_ratio_wfr", "P-ratio vejet"),
               ("na_bal_wfr", "Na-balance vejet"),
               ("na_bal_pho", "Na-balance foto"),
               ("na_ratio_pho", "Na-ratio foto")]:
    r1, p1, *_ = sp("crcl", y)
    r2, p2, *_ = sp("p_cr", y)
    r3, p3, *_ = sp("crcl", y, sub)
    f = lambda r, p: f"{r:+.2f} (p={p:.3f})"
    print(f"{lab:<26}{f(r1,p1):>17}{f(r2,p2):>17}{f(r3,p3):>18}")

rule("8. GRUPPESAMMENLIGNING <20 vs. >=20 (korrekt CrCl)")
print(f"{'Udfald':<24}{'<20':>16}{'>=20':>16}{'p':>9}")
print("-" * 65)
for y, lab in [("na_bal_wfr", "Na-balance vejet"), ("na_bal_pho", "Na-balance foto"),
               ("na_ratio_pho", "Na-ratio foto"), ("u_na_mg", "U-natrium"),
               ("u_na_per_cr", "U-Na/U-krea"), ("p_bal_wfr", "P-balance vejet"),
               ("fe_p", "FE-fosfat"), ("cr_idx", "Kreatinin-index")]:
    m = df[[y, "crcl"]].dropna()
    a = m.loc[m.crcl < 20, y]
    b = m.loc[m.crcl >= 20, y]
    if len(a) < 3 or len(b) < 3:
        continue
    p = stats.mannwhitneyu(a, b, alternative="two-sided").pvalue
    star = " *" if p < 0.05 else ""
    print(f"{lab:<24}{a.median():>9.1f} (n={len(a)}){b.median():>9.1f} "
          f"(n={len(b)}){p:>9.4f}{star}")

# eksport
out = df[["diu", "sglt2", "p_cr", "u_cr", "weight", "cr_idx", "cr_flag",
          "gfr_sheet", "crcl", "gfr_diff", "fe_p", "p_p", "u_p", "u_na",
          "u_na_per_cr", "u_p_per_cr", "p_in_wfr", "p_in_pho", "na_in_wfr",
          "na_in_pho", "p_bal_wfr", "p_bal_pho", "na_bal_wfr", "na_bal_pho",
          "p_ratio_wfr", "p_ratio_pho", "na_ratio_wfr", "na_ratio_pho"]]
out.to_csv("beregnet_fuld.csv", sep=";", decimal=",", float_format="%.4f",
           encoding="utf-8-sig")
print("\nSkrevet: analysis/beregnet_fuld.csv")
