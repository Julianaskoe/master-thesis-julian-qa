"""Aendrer P-kreatinin noget ved GFR-beregningen? Direkte validering."""

import numpy as np
from scipy import stats
from load import load, rule

df = load()

rule("A. VALIDERING AF DIN GFR-KOLONNE")
print("Din formel (rekonstrueret):  CrCl = U_cr[mmol/d] / (P_cr[mmol/L] * 1.44)")
print("Det svarer til              CrCl = U_cr*1000 / (P_cr[µmol/L] * 1.44)\n")
print(f"{'#':>3}{'P-cr':>7}{'U-cr':>8}{'Din GFR':>10}{'Genberegnet':>13}"
      f"{'Afvig %':>9}{'':>4}")
print("-" * 54)
df["gfr_diff"] = (df.crcl - df.gfr_sheet) / df.gfr_sheet * 100
bad = []
for i, r in df.iterrows():
    f = ""
    if abs(r.gfr_diff) > 0.5:
        f = " <--"
        bad.append(i)
    print(f"{i:>3}{r.p_cr:>7.0f}{r.u_cr:>8.3f}{r.gfr_sheet:>10.2f}"
          f"{r.crcl:>13.2f}{r.gfr_diff:>9.2f}{f}")
print(f"\nAfvigende raekker: {bad if bad else 'INGEN'}")
print(f"Maks absolut afvigelse: {df.gfr_diff.abs().max():.3f} %")
if df.gfr_diff.abs().max() < 0.5:
    print("=> DIN GFR-KOLONNE ER KORREKT. Ingen aendringer noedvendige.")

rule("B. VALIDERING AF DIN FE-KOLONNE")
df["fe_diff"] = (df.fe_p - df.fe_sheet) / df.fe_sheet * 100
print(f"{'#':>3}{'Din FE':>10}{'Genberegnet':>13}{'Afvig %':>9}{'':>4}")
print("-" * 39)
badfe = []
for i, r in df.iterrows():
    f = ""
    if abs(r.fe_diff) > 0.5:
        f = " <--"
        badfe.append(i)
    print(f"{i:>3}{r.fe_sheet:>10.3f}{r.fe_p:>13.3f}{r.fe_diff:>9.3f}{f}")
print(f"\nAfvigende raekker: {badfe if badfe else 'INGEN'}")
print(f"Maks absolut afvigelse: {df.fe_diff.abs().max():.4f} %")
if df.fe_diff.abs().max() < 0.5:
    print("=> DIN FE-KOLONNE ER OGSAA KORREKT.")

rule("C. ER GFR OG FE INTERNT KONSISTENTE?")
print("Tidligere (uden P-kreatinin) maatte jeg regne P-cr BAGLAENS ud af FE og")
print("fandt 5 'afvigende' raekker. Nu har jeg den faktiske P-kreatinin.\n")
print("Bagudregnet P-cr fra din FE-kolonne vs. den faktiske P-cr:")
df["p_cr_back"] = df.fe_sheet * df.p_p * df.u_cr / (100 * df.u_p) * 1000
print(f"{'#':>3}{'Faktisk P-cr':>14}{'Bagudregnet':>13}{'Afvig %':>9}")
print("-" * 39)
for i, r in df.iterrows():
    d = (r.p_cr_back - r.p_cr) / r.p_cr * 100
    print(f"{i:>3}{r.p_cr:>14.0f}{r.p_cr_back:>13.1f}{d:>9.2f}")
print("\n=> Hvis alle ligger paa 0 %, var mine tidligere '5 afvigende raekker'")
print("   en artefakt af MIN skaermbillede-transskribering, ikke en fejl hos dig.")

rule("D. FYSIOLOGISK PLAUSIBILITET")
print(f"P-kreatinin: median {df.p_cr.median():.0f} µmol/L, "
      f"range {df.p_cr.min():.0f}–{df.p_cr.max():.0f}")
print(f"CrCl:        median {df.crcl.median():.2f} ml/min, "
      f"range {df.crcl.min():.2f}–{df.crcl.max():.2f}")
print(f"U-kreatinin: median {df.u_cr.median():.2f} mmol/doegn, "
      f"range {df.u_cr.min():.2f}–{df.u_cr.max():.2f}")
print("\nSanity check: CrCl og P-kreatinin skal korrelere STAERKT negativt")
rho, p = stats.spearmanr(df.p_cr, df.crcl)
print(f"  Spearman rho = {rho:.3f}, p = {p:.2e}")
r, pp = stats.pearsonr(1 / df.p_cr, df.crcl)
print(f"  1/P-cr vs. CrCl (Pearson) r = {r:.3f}, p = {pp:.2e}")
print("\nHvor stor en del af variationen i CrCl kommer fra hhv. P-cr og U-cr?")
for v, lab in [("p_cr_mmol", "P-kreatinin (blod)"), ("u_cr", "U-kreatinin (urin)")]:
    rho2, p2 = stats.spearmanr(df[v], df.crcl)
    print(f"  CrCl vs. {lab:<22} rho = {rho2:+.3f}  (p = {p2:.4f})")
print("\n=> Fortolkning: hvis U-kreatinin bidrager svagt, er CrCl i praksis")
print("   drevet af blodproeven, og opsamlingsartefaktet er MINDRE alvorligt.")

rule("E. VOLUMEN-UAFHAENGIGE MAAL — findes de?")
print("BEMAERK: din CrCl bruger U_cr (mmol/doegn), ikke koncentration x volumen.")
print("Urinvolumen indgaar derfor ikke eksplicit. MEN: hvis en portion mangler,")
print("mangler den i doegnmaengden, saa problemet er det samme.\n")
print("Vaerdier hvis ALLE doegnmaengder skaleres med k = 0.8 (20 % tab):")
for lab, formel in [
    ("CrCl", "k * CrCl          -> paavirket"),
    ("FE-fosfat", "uaendret          -> IMMUN (U_p og U_cr skaleres begge)"),
    ("U-Na/U-cr", "uaendret          -> IMMUN"),
    ("U-natrium", "k * U_na          -> paavirket"),
    ("Kreatinin-index", "k * index         -> paavirket"),
    ("P-kreatinin", "uaendret          -> IMMUN (blodproeve)"),
    ("P-fosfat", "uaendret          -> IMMUN (blodproeve)"),
]:
    print(f"  {lab:<18}{formel}")
