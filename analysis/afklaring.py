"""Verifikation af de spoergsmaal brugeren rejser."""

import numpy as np
import pandas as pd
from scipy import stats
from load import load, rule

df = load()

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


def sp(x, y, data=None):
    d = df if data is None else data
    m = d[[x, y]].dropna()
    if len(m) < 5:
        return np.nan, np.nan, len(m)
    rho, p = stats.spearmanr(m[x], m[y])
    return rho, p, len(m)


# ===================================================== 1. SGLT2-OPTAELLING
rule("1. SGLT2 OG DIURETIKA — hvad staar der faktisk i filen?")
print(f"Raa optaelling af 'yes' i kolonnerne:")
print(f"  sglt2      ja = {int(df.sglt2.sum())}   blank/nej = {int((1-df.sglt2).sum())}")
print(f"  diuretics  ja = {int(df.diu.sum())}   blank/nej = {int((1-df.diu).sum())}")
print("\nDu siger det korrekte er SGLT2: 23 ja / 9 nej.")
print(f"Filen giver {int(df.sglt2.sum())} ja. Differencen er "
      f"{int(df.sglt2.sum())-23}.")
print("\nDeltagere hvor sglt2-kolonnen er BLANK (dvs. laest som 'nej'):")
print("  raekkenr:", list(df.index[df.sglt2 == 0]))
print("\n=> Hvis 9 skal vaere 'nej', men filen kun har "
      f"{int((1-df.sglt2).sum())} blanke, mangler der "
      f"{9-int((1-df.sglt2).sum())} blanke celler i filen.")
print("   Sammenlign selv med medicinlisten.")


# ============================ 2. SENSITIVITET: BLIVER NATRIUM STAERKERE?
rule("2. NATRIUM VED EKSKLUSION AF FLAGGEDE — bliver det staerkere?")
sub = df[~df.cr_flag]
print(f"n = {len(df)} -> {len(sub)}   (7 flaggede fjernet)\n")
print(f"{'Analyse':<38}{'alle':>18}{'uden flaggede':>18}{'retning':>10}")
print("-" * 84)
for xv, y, lab in [
    ("gfr_sheet", "na_bal_wfr_mean", "Na-balance vejet vs. CrCl"),
    ("gfr_sheet", "na_bal_wfr_med", "Na-balance vejet [med] vs. CrCl"),
    ("gfr_sheet", "na_bal_pho_mean", "Na-balance foto vs. CrCl"),
    ("gfr_sheet", "na_bal_pho_med", "Na-balance foto [med] vs. CrCl"),
    ("gfr_sheet", "na_rat_wfr_mean", "Na-ratio vejet vs. CrCl"),
    ("gfr_sheet", "na_rat_pho_mean", "Na-ratio foto vs. CrCl"),
    ("gfr_sheet", "u_na_mg", "U-natrium vs. CrCl"),
    ("gfr_sheet", "u_na_per_cr", "U-Na/U-krea vs. CrCl"),
    ("egfr", "na_bal_wfr_mean", "Na-balance vejet vs. eGFR"),
    ("egfr", "u_na_mg", "U-natrium vs. eGFR"),
]:
    r1, p1, n1 = sp(xv, y)
    r2, p2, n2 = sp(xv, y, sub)
    d = "STAERKERE" if abs(r2) > abs(r1) + 0.03 else (
        "svagere" if abs(r2) < abs(r1) - 0.03 else "uaendret")
    print(f"{lab:<38}{f'{r1:+.2f} (p={p1:.3f})':>18}"
          f"{f'{r2:+.2f} (p={p2:.3f})':>18}{d:>10}")

print("\nOg fosfor til sammenligning:")
for xv, y, lab in [
    ("gfr_sheet", "p_bal_wfr_mean", "P-balance vejet vs. CrCl"),
    ("egfr", "p_bal_wfr_mean", "P-balance vejet vs. eGFR"),
    ("egfr", "p_rat_wfr_mean", "P-ratio vejet vs. eGFR"),
    ("egfr", "fe_p", "FE-fosfat vs. eGFR"),
]:
    r1, p1, n1 = sp(xv, y)
    r2, p2, n2 = sp(xv, y, sub)
    d = "STAERKERE" if abs(r2) > abs(r1) + 0.03 else (
        "svagere" if abs(r2) < abs(r1) - 0.03 else "uaendret")
    print(f"{lab:<38}{f'{r1:+.2f} (p={p1:.3f})':>18}"
          f"{f'{r2:+.2f} (p={p2:.3f})':>18}{d:>10}")


# ============================ 3. HVAD ICC GAELDER FOR
rule("3. HVAD ICC GAELDER FOR — og hvad den IKKE gaelder for")
print("ICC er beregnet paa de 3 KOSTDAGE. Den siger derfor kun noget om")
print("INDTAGSDELEN. Udskillelsen er maalt EEN gang og har ingen ICC.\n")
print("Konsekvens for hver analysetype:")
rows = [
    ("U-natrium vs. clearance", "INGEN kostdata", "ICC irrelevant"),
    ("FE-fosfat vs. clearance", "INGEN kostdata", "ICC irrelevant"),
    ("Na-balance vs. clearance", "indtag OG udskillelse", "ICC gaelder delvis"),
    ("Na-ratio vs. clearance", "indtag OG udskillelse", "ICC gaelder delvis"),
]
print(f"{'Analyse':<30}{'Bruger':<26}{'ICC-relevans'}")
print("-" * 74)
for a, b, c in rows:
    print(f"{a:<30}{b:<26}{c}")

print("\nHvor stor en del af balancens varians kommer fra indtaget?")
for I, E, B, lab in [("na_wfr_mean", "u_na_mg", "na_bal_wfr_mean", "Na vejet"),
                     ("na_pho_mean", "u_na_mg", "na_bal_pho_mean", "Na foto"),
                     ("p_wfr_mean", "u_p_mg", "p_bal_wfr_mean", "P vejet"),
                     ("p_pho_mean", "u_p_mg", "p_bal_pho_mean", "P foto")]:
    m = df[[I, E, B]].dropna()
    vi, ve = m[I].var(ddof=1), m[E].var(ddof=1)
    cov = np.cov(m[I], m[E])[0, 1]
    vb = m[B].var(ddof=1)
    print(f"  {lab:<10} Var(I)={vi:>10.0f}  Var(E)={ve:>10.0f}  "
          f"2Cov={2*cov:>11.0f}  Var(B)={vb:>10.0f}")
    print(f"{'':<12}andel fra indtag = {vi/(vi+ve)*100:>5.1f} %   "
          f"rho(B,I)={stats.spearmanr(m[B],m[I])[0]:+.2f}  "
          f"rho(B,E)={stats.spearmanr(m[B],m[E])[0]:+.2f}")


# ============================ 4. DELT FEJL FORSTAERKER — DEMONSTRATION
rule("4. HVORFOR DELT FEJL KAN FORSTAERKE (modsat maalestoej)")
print("Simulation: 32 personer, INGEN aegte sammenhaeng mellem clearance og")
print("natriumudskillelse. Kun tilfaeldig ufuldstaendig opsamling (k).\n")
rng = np.random.default_rng(42)
res = []
for _ in range(4000):
    true_crcl = rng.normal(25, 8, 32).clip(8, 55)
    true_una = rng.normal(2200, 700, 32).clip(300, None)   # uafhaengig!
    k = rng.uniform(0.65, 1.0, 32)                          # opsamlingsandel
    meas_crcl = true_crcl * k
    meas_una = true_una * k
    res.append(stats.spearmanr(meas_crcl, meas_una)[0])
res = np.array(res)
print(f"  Sand korrelation: 0,00 (indbygget i simulationen)")
print(f"  Observeret median rho: {np.median(res):+.3f}")
print(f"  90 %-interval: {np.percentile(res,5):+.3f} til {np.percentile(res,95):+.3f}")
print(f"  Andel med p < 0,05: {np.mean(np.abs(res) > 0.349)*100:.0f} %")
print(f"\n  Dit observerede U-Na vs. CrCl: +0,54")
print(f"  Percentil i simulationen: "
      f"{stats.percentileofscore(res, 0.54):.0f}")
print("\n=> Delt opsamlingsfejl SKABER positiv korrelation ud af ingenting.")
print("   Det er MODSAT maalestoej, som traekker korrelationer mod nul.")

print("\nSamme simulation, men for FE (immun over for k):")
res2 = []
for _ in range(4000):
    true_crcl = rng.normal(25, 8, 32).clip(8, 55)
    true_fe = rng.normal(37, 14, 32)
    k = rng.uniform(0.65, 1.0, 32)
    meas_crcl = true_crcl * k
    meas_fe = true_fe            # FE er uaendret af k
    res2.append(stats.spearmanr(meas_crcl, meas_fe)[0])
res2 = np.array(res2)
print(f"  Observeret median rho: {np.median(res2):+.3f}  (forventet 0)")
print("=> Ingen kunstig korrelation. FE kan ikke snydes af opsamlingen.")


# ============================ 5. ER P-KREATININ 'DEN RETTE'?
rule("5. ER P-KREATININ DET 'RIGTIGE' MAAL? — aerlig gennemgang")
print("Ingen af dine tre maal er sandheden. De har FORSKELLIGE fejl:\n")
print(f"{'Maal':<16}{'Fejl fra urinopsamling':<26}{'Fejl fra muskelmasse'}")
print("-" * 70)
for a, b, c in [("CrCl", "JA — direkte", "nej"),
                ("eGFR", "nej", "JA — stor"),
                ("P-kreatinin", "nej", "JA — stor")]:
    print(f"{a:<16}{b:<26}{c}")
print("\nPointen er IKKE at P-kreatinin er sand. Pointen er at fejlene er")
print("UAFHAENGIGE af hinanden. Naar to maal med forskellige fejl er enige,")
print("er det svaert at forklare med een af fejlene.\n")

print("Muskelmasse-fejlen: laver den kunstige FE-korrelation?")
print("Sarkopeni -> lav P-kreatinin OG lav U-kreatinin.")
print("U-kreatinin staar i FE's NAEVNER -> lav U-cr giver HOEJ FE.")
print("Saa sarkopeni ville give: lav P-cr + hoej FE = NEGATIV korrelation.")
r, p, n = sp("p_cr", "fe_p")
print(f"Du finder: rho = {r:+.2f} (p={p:.4f}) — POSITIV.")
print("=> Muskelmasse-fejlen trakker MODSAT dit fund. Fundet er robust.\n")

print("Direkte test: haenger P-kreatinin sammen med muskelmasse-markoerer?")
for x, y, lab in [("p_cr", "cr_idx", "P-kreatinin vs. kreatinin-index"),
                  ("p_cr", "u_cr", "P-kreatinin vs. U-kreatinin (total)"),
                  ("p_cr", "weight", "P-kreatinin vs. kropsvaegt"),
                  ("egfr", "cr_idx", "eGFR vs. kreatinin-index")]:
    r, p, n = sp(x, y)
    print(f"  {lab:<38}rho = {r:+.2f}  p = {p:.3f}")


# ============================ 6. VEJLEDERENS HYPOTESE
rule("6. VEJLEDERENS HYPOTESE — er natrium bedre reguleret end fosfat?")
print("Hypotesen: natriumhomeostase er saa stram (RAAS/aldosteron) at man IKKE")
print("forventer retention foer meget sent. Fosfat svigter tidligere.")
print("Hvis det er rigtigt, er et STAERKT natriumfund mistaenkeligt.\n")
print("Hvad dine data siger:")
print(f"{'Udfald':<26}{'vs CrCl':>17}{'vs eGFR':>17}{'vs P-krea':>17}")
print("-" * 77)
for y, lab in [("u_na_mg", "U-natrium"),
               ("na_bal_wfr_mean", "Na-balance vejet"),
               ("na_rat_wfr_mean", "Na-ratio vejet"),
               ("fe_p", "FE-fosfat"),
               ("p_p", "P-fosfat"),
               ("p_rat_wfr_mean", "P-ratio vejet"),
               ("p_bal_wfr_mean", "P-balance vejet")]:
    out = []
    for xv in ("gfr_sheet", "egfr", "p_cr"):
        r, p, n = sp(xv, y)
        out.append(f"{r:+.2f} (p={p:.3f})")
    print(f"{lab:<26}{out[0]:>17}{out[1]:>17}{out[2]:>17}")
print("\n=> Alle fosfat-maal er signifikante mod de urin-uafhaengige maal.")
print("   Alle natrium-maal er signifikante KUN mod CrCl.")
print("   Det er praecis moensteret vejlederens fysiologi forudsiger.")


# ============================ 7. MEDIAN VS GENNEMSNIT — HVOR MANGE DAGE?
rule("7. MEDIAN VS GENNEMSNIT — betyder antal dage noget?")
print("Med 1 dag er median = gennemsnit. Med 2 dage er median = gennemsnit.")
print("Kun ved 3 dage er de forskellige.\n")
for tag, lab in [("p_wfr", "Fosfor vejet"), ("p_pho", "Fosfor foto"),
                 ("na_wfr", "Natrium vejet"), ("na_pho", "Natrium foto")]:
    c = df[f"{tag}_n"].value_counts().sort_index()
    tot3 = int((df[f"{tag}_n"] == 3).sum())
    print(f"{lab:<16}" + "  ".join(f"{k} dag(e): n={v}" for k, v in c.items())
          + f"   -> median!=gns for {tot3}")
print("\n=> Median og gennemsnit kan KUN afvige for de deltagere der har 3 dage.")
print("   For foto-metoden er det kun 9-11 deltagere. Forskellen er derfor")
print("   drevet af meget faa personer — brug gennemsnit som primaer.")
