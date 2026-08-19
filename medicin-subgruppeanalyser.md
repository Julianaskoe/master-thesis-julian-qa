# Subgruppeanalyser: diuretika og SGLT2-hæmmere

*Kørt på de 32 rækker fra dit skærmbillede. Script: `analysis/medication_tests.py`, rå output: `analysis/output.txt`.*

---

## ⚠️ Først: to ting du skal afklare, før tallene bruges

### 1. Dine n stemmer ikke med specialet

| Kilde | Diuretika | SGLT2i |
|---|---|---|
| Specialet / tidligere tråd | 26 (81 %) | 23 (72 %) |
| **Dette skærmbillede** | **28 (88 %)** | **19 (59 %)** |

SGLT2i-tallet afviger med 4 deltagere. Find ud af hvilket der er rigtigt, **før** noget kommer på et slide. Hvis skærmbilledet er en delmængde (fx kun dem med komplet FE-beregning), skal det fremgå.

### 2. Række 31 er stadig ikke rettet

`urin_p = 11,25` med `fe_p = 37,19` — i den tidligere tråd stod der 3,72 %, hvilket var faktor 10 forkert. Nu står 37,19 %, så **du har rettet den**. Godt. Men verificér, at `GFR`-kolonnen og `FE`-kolonnen bruger samme U-kreatinin hele vejen ned.

---

## Svaret på dit spørgsmål: er der nok information på billedet?

**Til SGLT2i: ja.** Du har eksponering (ja/nej) og alle relevante udfald.

**Til diuretika: nej — men på en anden måde end du frygtede.**

Problemet er ikke, at du mangler stofgruppe. Problemet er, at **kun 4 af 32 ikke får diuretika.** Selv med perfekt klassificering i loop/thiazid/MRA kunne du ikke lave en meningsfuld sammenligning, fordi referencegruppen er tom. Så det du ikke kan få adgang til, er ikke det, der begrænser dig.

Det ændrer, hvad du skal sige til forsvaret — se afsnittet nederst.

---

## Analyse 1 — SGLT2i (n=19 vs. n=13), Mann-Whitney U

| Udfald | SGLT2i ja | SGLT2i nej | HL-diff | 95 % CI | p | r<sub>rb</sub> |
|---|---|---|---|---|---|---|
| FE-fosfat (%) | 40,1 (34,0–45,3) | 33,0 (28,7–44,0) | +3,72 | [−7,8; +13,8] | 0,45 | 0,17 |
| P-fosfat (mmol/L) | 1,35 (1,08–1,40) | 1,18 (1,06–1,51) | +0,05 | [−0,20; +0,27] | 0,69 | 0,09 |
| U-fosfat (mmol/døgn) | 15,4 (11,1–25,2) | 15,0 (13,0–17,2) | +1,80 | [−3,5; +8,7] | 0,48 | 0,15 |
| U-natrium (mmol/døgn) | 92,3 (71,7–104,5) | 111,0 (61,1–132,5) | −15,1 | [−51,8; +24,0] | 0,51 | −0,14 |
| U-Na / CrCl | 3,65 (2,96–4,16) | 4,03 (3,07–5,61) | −0,83 | [−2,24; +0,52] | 0,34 | −0,21 |
| Kreatininclearance | 25,7 (23,1–27,8) | 23,1 (17,6–27,0) | +2,64 | [−2,7; +8,1] | 0,27 | 0,24 |

**Ingen signifikante forskelle.** Retningerne er dog konsistente med litteraturen: SGLT2i-gruppen har numerisk højere FE-fosfat og højere P-fosfat.

> ⚠️ **Fælden:** litteraturen forudsiger *nedsat* fraktionel fosfatudskillelse ved SGLT2i. Du finder numerisk det modsatte (+3,7 procentpoint). Med p=0,45 og CI [−7,8; +13,8] kan du ikke sige noget om retningen — men **sig ikke, at fundet understøtter litteraturen.** Det gør det ikke.

### Vigtigt: SGLT2i-gruppen har bedre nyrefunktion

CrCl er 2,6 ml/min højere i SGLT2i-gruppen. Det er ikke signifikant, men det er **confounding by indication** — SGLT2i ordineres til dem med bedre bevaret funktion. Derfor kørte jeg også partiel korrelation justeret for CrCl:

| Udfald | Partiel Spearman (justeret for CrCl) | p |
|---|---|---|
| FE-fosfat | 0,18 | 0,32 |
| P-fosfat | 0,17 | 0,36 |
| U-natrium | −0,28 | 0,13 |

Konklusionen ændrer sig ikke. Det er et godt kort at kunne spille: *"jeg justerede for clearance, og billedet var uændret."*

---

## Analyse 2 — Diuretika (n=28 vs. n=4)

Her sker der noget, som **ser** stærkt ud, og som du skal håndtere meget forsigtigt:

| Udfald | Diuretika ja (n=28) | Diuretika nej (n=4) | p | r<sub>rb</sub> |
|---|---|---|---|---|
| FE-fosfat (%) | 40,7 (32,8–46,5) | 21,4 (19,1–25,8) | **0,009** | 0,79 |
| U-fosfat (mmol/døgn) | 15,8 (12,9–24,9) | 8,9 (8,3–10,5) | **0,023** | 0,72 |
| U-natrium (mmol/døgn) | 97,7 (73,4–133,1) | 53,0 (37,4–63,0) | **0,010** | 0,81 |
| **U-Na / CrCl** | 4,02 (3,33–5,35) | 2,31 (1,84–2,41) | **<0,001** | **0,95** |
| U-P / CrCl | 0,77 (0,49–0,92) | 0,46 (0,39–0,50) | **0,029** | 0,68 |
| P-fosfat (mmol/L) | 1,31 (1,07–1,41) | 1,20 (1,08–1,41) | 0,93 | 0,04 |
| Kreatininclearance | 25,0 (20,7–27,7) | 22,9 (20,0–26,1) | 0,72 | 0,12 |

Alle fire deltagere uden diuretika ligger under kohortemedianen på **alle** udskillelsesmål. Rank-biserial på 0,95 for U-Na/CrCl betyder næsten fuldstændig separation.

### Hvorfor du ikke må præsentere dette som et fund

**De fire deltagere uden diuretika (deskriptivt — brug denne tabel, ikke p-værdierne):**

| # | U-P | P-fosfat | U-Na | CrCl | FE-P | SGLT2i |
|---|---|---|---|---|---|---|
| 19 | 9,00 | 1,31 | 46,0 | 20,6 | 23,2 % | ja |
| 23 | 15,00 | 1,08 | 72,0 | 28,8 | 33,5 % | ja |
| 24 | 6,75 | 1,06 | 60,0 | 25,2 | 17,5 % | nej |
| 25 | 8,80 | 1,72 | 11,6 | 18,1 | 19,7 % | nej |
| | | | | | | |
| **Kohortemedian** | **15,3** | **1,30** | **95,3** | **25,0** | **36,6 %** | |

Tre selvstændige grunde til forsigtighed:

1. **n=4.** Én deltagers værdi flytter medianen med 25 %. Deltager 25 har U-Na på 11,6 mmol/døgn — det er ekstremt lavt og i sig selv mistænkeligt for ufuldstændig opsamling.
2. **Alternativ forklaring der er mindst lige så plausibel:** de fire lave U-Na-værdier kan skyldes *dårligere opsamling* eller *lavere saltindtag*, ikke fravær af diuretikaeffekt. Du kan ikke skelne.
3. **Kausaliteten kan gå begge veje.** Diuretika gives til dem med væskeretention — som ofte har højere saltindtag. Så er det diuretikaen der øger udskillelsen, eller er det saltindtaget der udløste både diuretikaen og udskillelsen?

**Formuleringen til forsvaret:**

> *"Kun fire deltagere fik ikke diuretika. Alle fire havde natrium- og fosfatudskillelse under kohortemedianen, hvilket er retningsmæssigt foreneligt med en diuretikaeffekt, men med n=4 er en formel test ikke meningsfuld, og forskellen kan lige så vel skyldes lavere saltindtag eller ufuldstændig opsamling i denne lille gruppe. Jeg rapporterer det deskriptivt."*

---

## Analyse 3 — Kruskal-Wallis, fire behandlingskombinationer

Jeg lavede den kombinationsvariabel du efterspurgte:

| Gruppe | n | FE-fosfat | U-Na | **U-Na/CrCl** | CrCl |
|---|---|---|---|---|---|
| Diuretika + SGLT2i | 17 | 41,3 (35,4–45,8) | 96,0 (72–110) | 3,76 (3,20–4,17) | 25,7 |
| Diuretika alene | 11 | 33,9 (31,8–48,7) | 123,2 (93–148) | 5,12 (3,85–6,20) | 23,1 |
| SGLT2i alene | 2 | 28,4 | 59,0 | 2,37 | 24,7 |
| Ingen | 2 | 18,6 | 35,8 | 1,51 | 21,6 |

**Kruskal-Wallis (df=3):**

| Udfald | H | p | ε² |
|---|---|---|---|
| **U-Na / CrCl** | 10,96 | **0,012** | 0,284 |
| **U-natrium** | 7,96 | **0,047** | 0,177 |
| FE-fosfat | 6,86 | 0,077 | 0,138 |
| U-fosfat | 5,95 | 0,114 | 0,105 |
| U-P / CrCl | 4,89 | 0,180 | 0,068 |
| P-fosfat | 0,72 | 0,87 | — |
| Kreatininclearance | 1,42 | 0,70 | — |

**To grupper har n=2.** Jeg har ikke kørt Dunn's post hoc — det er ikke meningsfuldt her, og en censor vil se det. Kruskal-Wallis er signifikant, fordi den drives fuldstændigt af de fire deltagere uden diuretika. Det er samme fund som analyse 2, ikke et nyt.

**Brug denne tabel til at vise en dosis-respons-gradient deskriptivt** (U-Na/CrCl: 1,5 → 2,4 → 3,8 → 5,1 fra ingen behandling til diuretika alene) — men uden p-værdi.

---

## Analyse 4 — SGLT2i inden for diuretikabrugerne (n=17 vs. n=11)

Dette er den **metodisk reneste** analyse du har: alle er på diuretika, så diuretika er elimineret som confounder.

| Udfald | SGLT2i ja | SGLT2i nej | p | r<sub>rb</sub> |
|---|---|---|---|---|
| FE-fosfat (%) | 41,3 | 33,9 | 0,71 | 0,09 |
| P-fosfat | 1,37 | 1,18 | 0,51 | 0,16 |
| U-natrium | 96,0 | 123,2 | 0,26 | −0,26 |
| U-Na / CrCl | 3,76 | 5,12 | 0,15 | −0,34 |

Ingen signifikans, men **U-Na/CrCl er den mest interessante**: r<sub>rb</sub> = −0,34 og p=0,15 i retning af *lavere* natriumudskillelse pr. nyrefunktion hos SGLT2i-brugere. Det er modsat den forventede natriurese — men SGLT2i's natriuretiske effekt er kendt for at være **forbigående** (nogle uger), hvorefter der etableres en ny steady state. Hvis dine deltagere har været i behandling længe, er det præcis hvad man ville forvente. **Det er et godt svar at have klar.**

---

## Analyse 5 — Korrelationer med 95 % CI

| Sammenhæng | Spearman ρ | 95 % CI | p | Pearson r | p |
|---|---|---|---|---|---|
| FE-fosfat vs. CrCl | −0,17 | [−0,49; +0,19] | 0,34 | −0,32 | 0,076 |
| FE-fosfat vs. **1/CrCl** | +0,17 | [−0,19; +0,49] | 0,34 | **+0,41** | **0,021** |
| FE-fosfat vs. P-fosfat | +0,33 | [−0,02; +0,61] | 0,061 | +0,28 | 0,124 |
| **P-fosfat vs. CrCl** | **−0,38** | [−0,65; −0,04] | **0,031** | −0,36 | 0,044 |
| **U-natrium vs. CrCl** | **+0,54** | [+0,23; +0,75] | **0,001** | +0,50 | 0,003 |
| **U-fosfat vs. CrCl** | **+0,39** | [+0,05; +0,65] | **0,026** | +0,29 | 0,104 |

### Tre ting du skal vide her

**a) 1/CrCl-lineariseringen virker — men kun for Pearson.** Pearson går fra −0,32 til +0,41 (p=0,021). Spearman er uændret ±0,17, fordi rangordenen er identisk (1/x er monoton). **Det betyder, at forbedringen udelukkende er en lineariseringseffekt, ikke ny information.** Hvis du rapporterer Pearson på 1/CrCl som "signifikant", mens Spearman på samme data er 0,17 (p=0,34), skal du kunne forklare hvorfor. Det ærlige svar: forholdet er ikke-lineært, og Pearson på den lineariserede skala er derfor det mest passende mål — men rapportér begge.

**b) Din FE vs. CrCl er svagere end den tidligere tråd angav.** Der stod ρ = −0,29; jeg får −0,17 på Spearman og −0,32 på Pearson. Sandsynligvis fordi række 31 nu er rettet. Brug de nye tal.

**c) De tre signifikante korrelationer er dine bedste fysiologiske fund:**
- **P-fosfat stiger når CrCl falder** (ρ=−0,38): forventeligt, validerer datasættet.
- **U-natrium falder når CrCl falder** (ρ=+0,54): dette er stærkt — og relevant for din opsamlingsdiskussion, se nedenfor.
- **U-fosfat falder når CrCl falder** (ρ=+0,39).

> ⚠️ **Kritisk for dit natriumfund:** ρ = +0,54 mellem U-Na og CrCl kan læses på to måder. Antaget lige saltindtag betyder det, at de sygeste udskiller mindre natrium — altså **natriumretention**, som du konkluderer. Men det er også *præcis* det mønster man ville se, hvis **de sygeste opsamlede dårligst.** Du kan ikke skelne de to med disse data. Rejs det selv.

---

## Analyse 6 — Robusthed (leave-one-out) på FE vs. CrCl

| | Fuld kohorte | Leave-one-out spændvidde |
|---|---|---|
| Spearman ρ | −0,174 | −0,233 til −0,092 |
| Pearson r | −0,318 | −0,370 til −0,201 |

Mest indflydelsesrige observation: **række 23** (CrCl 9,49, FE 72,7 %) → Pearson falder til −0,201.

Efter rettelsen af række 31 er analysen **markant mere robust** end da vi diskuterede den sidst. Ingen enkelt observation vælter resultatet. Det er værd at nævne — det er stærk metodedisciplin.

---

## Analyse 7 — Hvor stor en forskel kunne du overhovedet have fundet?

Dette er dit vigtigste forsvar for nulfundene. Post hoc MDE (80 % power, α=0,05, n=19 vs. 13) → **Cohens d ≈ 1,08**, altså en stor effekt.

| Udfald | Pooled SD | Mindste detekterbare forskel | Observeret forskel |
|---|---|---|---|
| FE-fosfat (%) | 14,4 | **14,8** | 3,7 |
| P-fosfat (mmol/L) | 0,27 | **0,28** | 0,05 |
| U-fosfat (mmol/døgn) | 7,7 | **7,9** | 1,8 |
| U-natrium (mmol/døgn) | 53,3 | **55,0** | −15,1 |

**Formuleringen:**

> *"Med 19 mod 13 deltagere havde jeg 80 % power til at detektere en forskel svarende til Cohens d = 1,1 — for FE-fosfat ca. 15 procentpoint. Enhver realistisk SGLT2i-effekt er mindre end det. Fraværet af signifikante forskelle skal derfor tolkes som manglende styrke, ikke som evidens for fravær af effekt."*

Det er den samme signal/støj-pointe som i punkt 8 sidst — men nu med **dine egne tal**, og det gør den meget lettere at forsvare mundtligt.

---

## Analyse 8 — Kompensationsfænotyper (den kliniske analyse)

Hyperfosfatæmi (P-fosfat > 1,45 mmol/L): **7 af 32 (22 %)**. Median FE-fosfat: 36,6 %.

| | FE over median | FE under median |
|---|---|---|
| P-fosfat høj | 4 | 3 |
| P-fosfat normal | 12 | 13 |

Fisher's exact p = 1,00. **Ingen association** — så den analyse jeg foreslog sidst gav ikke det, jeg håbede.

**Men de tre deltagere med svigtende kompensation er stadig værd at vise:**

| # | CrCl | P-fosfat | FE-fosfat | Diuretika | SGLT2i |
|---|---|---|---|---|---|
| 2 | 27,6 | 1,76 | 35,4 % | ja | ja |
| 25 | 18,1 | 1,72 | 19,7 % | nej | nej |
| 29 | 24,3 | 1,60 | 14,3 % | ja | ja |

Hyperfosfatæmi trods FE under median = kompensationen har svigtet. Det er den fænotype dit speciale handler om, og du kan pege på tre konkrete patienter. Bemærk at deltager 25 er en af de fire uden diuretika — og har U-Na på 11,6. Den deltager driver flere af dine fund og fortjener et selvstændigt blik.

---

## Hvad du konkret siger til forsvaret

**Hvis du bliver spurgt om diuretika:**

> *"Jeg havde ikke adgang til klassificering efter stofgruppe, og det er en reel begrænsning, fordi thiazider og loop-diuretika har modsatrettede effekter på urin-calcium. Men den bindende begrænsning var en anden: 28 af 32 fik diuretika, så referencegruppen var kun fire deltagere. Selv med perfekt klassificering ville en formel test ikke være meningsfuld. Jeg har derfor rapporteret de fire deltagere uden diuretika deskriptivt — de lå alle under kohortemedianen på natrium- og fosfatudskillelse, hvilket er retningsmæssigt foreneligt med en diuretikaeffekt, men også med lavere saltindtag eller ufuldstændig opsamling."*

**Hvis du bliver spurgt om SGLT2i:**

> *"Jeg testede eksplorativt med Mann-Whitney på FE-fosfat, P-fosfat, U-fosfat og U-natrium, både i hele kohorten og stratificeret til kun diuretikabrugere for at fjerne diuretika som confounder, samt med partiel korrelation justeret for creatininclearance. Ingen forskelle var signifikante. Med 19 mod 13 deltagere havde jeg kun power til at detektere en effektstørrelse på d ≈ 1,1, så det er et uinformativt nulfund, ikke evidens for fravær af effekt. Retningen for FE-fosfat var faktisk modsat litteraturens forudsigelse, men konfidensintervallet [−7,8; +13,8 procentpoint] tillader ingen konklusion om retning."*

**Prioritering til dit oplæg:**

| Prioritet | Hvad | Hvorfor |
|---|---|---|
| **1** | U-natrium vs. CrCl (ρ=+0,54) med den dobbelte fortolkning | Dit stærkeste fund — og du foregriber det stærkeste angreb |
| **2** | Power/MDE-tabellen | Forvandler alle dine nulfund fra svaghed til metodeindsigt |
| **3** | De fire uden diuretika, deskriptivt | Viser du kan lade være med at teste |
| 4 | Leave-one-out på FE vs. CrCl | Robusthed, kort nævnt |
| 5 | De tre svigtende kompensationer | Klinisk konkret |
| — | **Ikke** Kruskal-Wallis med n=2-grupper som hovedfund | Inviterer til kritik du ikke kan forsvare |

---

## Hvad der ville have gjort en forskel

Du spurgte, om der er nok information. Til de test jeg har lavet: ja. Men følgende ville have flyttet mest, i prioriteret rækkefølge:

1. **Kropsvægt pr. deltager** → kreatinin-index pr. person, så du kan flagge de mistænkelige opsamlinger. Det er den analyse, der ville styrke natriumfundet mest.
2. **U-kreatinin og P-kreatinin som separate kolonner** → jeg kunne verificere FE og CrCl mod hinanden i alle 32 rækker i stedet for at stole på GFR-kolonnen.
3. **Natriumindtag** → uden det er U-Na vs. CrCl-korrelationen ikke fortolkelig som retention.
4. Diuretikaklasse — reelt mindst vigtig, af de grunde ovenfor.

Send vægt og U-kreatinin, hvis du kan, så laver jeg kreatinin-index og sensitivitetsanalysen uden de flaggede.
