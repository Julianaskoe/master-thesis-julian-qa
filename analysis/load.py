"""Faelles indlaesning af CSV-filen. Importeres af de andre scripts."""

import sys
import numpy as np
import pandas as pd

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

CSV = r"c:\Users\julia\Downloads\Book 1 opdateret(Ark1).csv"

MW_CR = 113.12      # kreatinin, g/mol
MW_P = 30.974       # fosfor, g/mol
MW_NA = 22.990      # natrium, g/mol


def load():
    df = pd.read_csv(CSV, sep=";", decimal=",", encoding="latin-1",
                     skipinitialspace=True)
    df.columns = [c.strip() for c in df.columns]
    df = df.rename(columns={
        "diuretics": "diu",
        "creatinine p": "p_cr",          # µmol/L
        "sglt2": "sglt2",
        "urin p": "u_p",                 # mmol/doegn
        "plasma p": "p_p",               # mmol/L
        "urinary sodium": "u_na",        # mmol/doegn
        "GFR": "gfr_sheet",              # ml/min, din egen kolonne
        "eGFR": "egfr",                  # ml/min/1.73m2
        "FE p": "fe_sheet",              # %, din egen kolonne
        "vægt": "weight",
        "v\ufffdgt": "weight",
        "urin cr": "u_cr",               # mmol/doegn
    })
    # find vaegtkolonnen uanset hvordan aa/ae er kodet
    for c in df.columns:
        if c.lower().startswith("v") and c not in ("weight",) and len(c) <= 5:
            df = df.rename(columns={c: "weight"})

    # rens de numeriske kolonner (nogle celler indeholder linjeskift i anfoerselstegn)
    intake_cols = [c for c in df.columns
                   if "fosfat" in c.lower() or "natrium" in c.lower()]
    for c in intake_cols + ["p_cr", "u_p", "p_p", "u_na", "gfr_sheet", "egfr",
                            "fe_sheet", "weight", "u_cr"]:
        df[c] = pd.to_numeric(
            df[c].astype(str).str.replace("\n", "", regex=False)
                 .str.replace(",", ".", regex=False).str.strip()
                 .replace({"": None, "nan": None}),
            errors="coerce")

    df = df.dropna(subset=["u_cr", "p_cr"]).reset_index(drop=True)
    df.index = np.arange(1, len(df) + 1)
    df["diu"] = (df.diu.astype(str).str.strip().str.lower() == "yes").astype(int)
    df["sglt2"] = (df.sglt2.astype(str).str.strip().str.lower() == "yes").astype(int)

    # kolonnegrupper
    df.attrs["p_wfr"] = ["fosfat dag 1 vejet", "fosfat 2 vejet", "fosfat 3 vejet"]
    df.attrs["p_pho"] = ["billede 1 fosfat", "billede 2 fosfat", "billede 3 fosfat"]
    df.attrs["na_wfr"] = ["Natrium dag 1 vejet", "Natrium 2 vejet", "Natrium 3 vejet"]
    df.attrs["na_pho"] = ["Natrium dag 1 billede", "Natrium 2 billede",
                          "Natrium 3 billede"]

    # ---------- afledte variable ----------
    df["p_cr_mmol"] = df.p_cr / 1000
    # Kreatininclearance af raadata: U_cr[mmol/d] / (P_cr[mmol/L] * 1.44) -> ml/min
    df["crcl"] = df.u_cr / (df.p_cr_mmol * 1.44)
    # FE-fosfat af raadata
    df["fe_p"] = df.u_p * df.p_cr_mmol / (df.p_p * df.u_cr) * 100

    df["cr_idx"] = df.u_cr * MW_CR / df.weight          # mg/kg/doegn
    df["inv_crcl"] = 1 / df.crcl
    df["u_na_mg"] = df.u_na * MW_NA
    df["u_p_mg"] = df.u_p * MW_P
    df["u_na_per_cr"] = df.u_na / df.u_cr
    df["u_p_per_cr"] = df.u_p / df.u_cr

    # indtag = gennemsnit af de dage der findes
    df["p_in_wfr"] = df[df.attrs["p_wfr"]].mean(axis=1)
    df["p_in_pho"] = df[df.attrs["p_pho"]].mean(axis=1)
    df["na_in_wfr"] = df[df.attrs["na_wfr"]].mean(axis=1)
    df["na_in_pho"] = df[df.attrs["na_pho"]].mean(axis=1)
    df["n_p_wfr"] = df[df.attrs["p_wfr"]].notna().sum(axis=1)
    df["n_p_pho"] = df[df.attrs["p_pho"]].notna().sum(axis=1)
    df["n_na_wfr"] = df[df.attrs["na_wfr"]].notna().sum(axis=1)
    df["n_na_pho"] = df[df.attrs["na_pho"]].notna().sum(axis=1)

    # balance (indtag - udskillelse), mg/doegn
    df["p_bal_wfr"] = df.p_in_wfr - df.u_p_mg
    df["p_bal_pho"] = df.p_in_pho - df.u_p_mg
    df["na_bal_wfr"] = df.na_in_wfr - df.u_na_mg
    df["na_bal_pho"] = df.na_in_pho - df.u_na_mg
    # ratio (udskillelse / indtag), %
    df["p_ratio_wfr"] = df.u_p_mg / df.p_in_wfr * 100
    df["p_ratio_pho"] = df.u_p_mg / df.p_in_pho * 100
    df["na_ratio_wfr"] = df.u_na_mg / df.na_in_wfr * 100
    df["na_ratio_pho"] = df.u_na_mg / df.na_in_pho * 100
    return df


def rule(t=""):
    print("\n" + "=" * 78)
    if t:
        print(t)
        print("=" * 78)
