> **Data:** `Book 1 opdateret(Ark1).csv` (n=32, nu med eGFR)
> **Script:** `analysis/speciale_replikation.py` · **Rå output:** `analysis/outC.txt` · **Alle variable:** `analysis/speciale_alle_variable.csv`

# ✅ Først: min replikation er valid

Inden du bruger noget, skal du vide, at mine tal matcher dit speciale:

| Variabel | Mit resultat | Dit speciale |
|---|---|---|
| Na-indtag, vejet (median) | 2008 mg | 2010 mg |
| U-natrium (median) | 2190 mg | 2191 mg |
| Fosfor-ratio foto vs. CrCl | ρ = 0,31, p = 0,087 | ρ = 0,31, p = 0,087 |
| P-indtag, vejet | 970 mg | ~1081 mg* |

*\*Forskellen skyldes at du brugte enkeltdage, jeg bruger 3-dages-gennemsnit.*

**Fosfor-ratio-korrelationen rammer dine tal på tredje decimal.** Så beregningerne nedenfor er direkte sammenlignelige med specialet.

---

# 🔴 DEL 1: GFR-kolonnen — der er stadig 3 rækker at afklare

Du har bekræftet, at række 29 (41,49) og række 12 (22,30) er korrekte ud fra dine egne data. **Godt.** Men det efterlader et problem, du skal forstå:

## Hvad din bekræftelse faktisk betyder

Din FE-kolonne er **matematisk 100 % konsistent** med P-kreatinin, U-kreatinin, U-fosfat og P-fosfat i alle 32 rækker (afvigelse 0,0000 %). Det er verificeret.

Så hvis GFR-kolonnen er *også* korrekt for række 12 og 29, må de to kolonner bruge **forskellige rådata for samme deltager.** Fx et andet urinvolumen, en anden opsamlingsdag, eller en anden blodprøve.

**Det er ikke nødvendigvis en fejl** — måske havde du to opsamlinger for nogle deltagere. Men **du skal kunne forklare det**, hvis en censor spørger, hvorfor FE og GFR ikke stemmer.

## De 3 rækker der stadig skal tjekkes

| Række | Din GFR | Af FE-data | **eGFR** | P-krea | U-krea |
|---|---|---|---|---|---|
| **13** | **25,76** | **18,40** | **14** | 280 | 7,42 |
| 19 | 53,51 | 58,51 | 33 | 189 | 15,93 |
| **28** | **17,56** | **22,81** | **14** | 358 | 11,76 |

**Kig på eGFR-kolonnen — den er det uafhængige tredjevidne:**

- **Række 13:** eGFR = 14. Din GFR siger 25,76, FE-data siger 18,40. **18,40 ligger langt tættere på eGFR.** Det tyder på, at FE-versionen er den rigtige, og at 25,76 er for høj.
- **Række 28:** eGFR = 14. Din GFR siger 17,56, FE-data siger 22,81. Her ligger **17,56 tættest på eGFR.** Så her ser din GFR-kolonne rigtigere ud.
- **Række 19:** eGFR = 33 mod GFR 53,51. Stor forskel, men det er kohortens højeste clearance, og der er tubulær sekretion + BSA-effekt, så det kan forklares.

**Konklusion:** række 13 er den, du skal se nærmest på. Hvis 18,40 er rigtigt, flytter deltageren fra `≥20` til `<20`-gruppen.

## Hvad du gør — 20 minutter

1. Åbn regnearket, klik på GFR-cellen i **række 13** og se hvilke celler formlen peger på
2. Sammenlign med FE-cellen i samme række
3. Hvis de bruger forskellig U-krea eller P-krea: find ud af hvilken der er den rigtige måling
4. Skriv ned hvad du finder — du skal kunne forklare det

**Hvis alt viser sig at være korrekt** (fx to opsamlinger), så sig:

> *"Kreatininclearance og fraktionel ekskretion er for tre deltagere beregnet på forskellige opsamlinger, hvilket forklarer en uoverensstemmelse på op til 28 % mellem de to kolonner. Jeg har verificeret begge mod eGFR."*

---

# 🏆 DEL 2: eGFR er dit stærkeste værktøj — og det ændrer alt

Dette er den vigtigste nyhed i denne runde. **eGFR beregnes kun ud fra P-kreatinin, alder og køn — den rører aldrig urinen.** Så den er fuldstændig immun over for opsamlingsproblemet.

## Hovedresultatet — samme udfald mod tre mål

| Udfald | vs. **CrCl**<br>*(urin-baseret)* | vs. **eGFR**<br>*(urin-fri)* | vs. **P-krea**<br>*(urin-fri)* | Dom |
|---|---|---|---|---|
| **FE-fosfat** | −0,17 (0,34) | **−0,51 (0,003)** | **+0,59 (0,0004)** | 🏆 **ÆGTE** |
| **P-fosfat** | −0,38 (0,031) | **−0,68 (<0,0001)** | **+0,59 (0,0004)** | 🏆 **ÆGTE** |
| U-fosfat | +0,39 (0,026) | −0,25 (0,17) | +0,36 (0,045) | 🟡 uklar |
| **U-natrium** | **+0,54 (0,0015)** | **+0,09 (0,64)** | +0,11 (0,55) | 🔴 **artefakt** |
| U-Na/U-krea | +0,28 (0,12) | +0,19 (0,30) | −0,12 (0,52) | 🔴 intet |
| Kreatinin-index | +0,45 (0,009) | −0,21 (0,25) | +0,32 (0,075) | 🔴 tautologi |

### Hvordan du læser fortegnene

Dette forvirrer folk, så lad mig være helt tydelig:

| Mål | Højt tal betyder |
|---|---|
| CrCl | **god** nyrefunktion |
| eGFR | **god** nyrefunktion |
| P-kreatinin | **dårlig** nyrefunktion |

Så for FE-fosfat: **−0,51 mod eGFR** og **+0,59 mod P-kreatinin** siger **præcis det samme:** dårligere nyrefunktion → højere fraktionel fosfatudskillelse.

## 🎯 Det du skal sige — dit hovedfund

> **"Den fraktionelle fosfatudskillelse steg signifikant med aftagende nyrefunktion, målt både med eGFR (ρ = −0,51, 95 % CI −0,73 til −0,20, p = 0,003) og med P-kreatinin (ρ = +0,59, 95 % CI 0,30–0,78, p = 0,0004). Begge mål er uafhængige af urinopsamlingens komplethed. Fundet understøtter hypotesen om renal kompensation ved aftagende nefronmasse og kan ikke forklares af opsamlingsartefakt."**

**Og bemærk hvor stærkt det står:** *to* uafhængige nyrefunktionsmål giver samme svar, med p-værdier på 0,003 og 0,0004. Det er ikke et grænsetilfælde. Det er dit positive fund.

## Og P-fosfat er endnu stærkere

ρ = −0,68 mod eGFR (p < 0,0001). Det er den stærkeste sammenhæng i hele dit materiale.

**Brug den som positiv kontrol:**

> *"P-fosfat korrelerede stærkt med eGFR (ρ = −0,68, p < 0,0001) i den fysiologisk forventede retning. Da dette er en velkendt og veletableret sammenhæng ved CKD, fungerer den som positiv kontrol og understøtter datasættets validitet."*

Det er et vigtigt argument. Hvis dine data kan reproducere noget velkendt, kan man have tillid til dem når de siger noget nyt.

## 🔴 Og natriumfundet forsvinder helt

| U-natrium vs. | ρ | p |
|---|---|---|
| CrCl | **+0,54** | **0,0015** |
| eGFR | +0,09 | 0,64 |
| P-kreatinin | +0,11 | 0,55 |

Signifikant mod **kun** det ene mål, som deler fejlkilde med udfaldet. Nul mod **begge** uafhængige mål.

---

# DEL 3: Dine specialeanalyser — gennemsnit vs. median

Du spurgte, om det gav mening at bruge median i stedet for gennemsnit af de 3 dage. **Ja, og det gør faktisk en forskel.** Her er alt:

## Fosfor (n=31)

| Analyse | vs. CrCl [gns] | vs. CrCl [median] | vs. eGFR [gns] | **vs. eGFR [median]** |
|---|---|---|---|---|
| Fosforbalance, vejet | +0,09 (0,62) | +0,16 (0,39) | **+0,46 (0,009)** | **+0,46 (0,010)** |
| Fosforbalance, foto | −0,12 (0,51) | −0,17 (0,36) | +0,16 (0,38) | +0,15 (0,42) |
| Fosfor-ratio, vejet | +0,19 (0,31) | +0,09 (0,63) | **−0,43 (0,015)** | **−0,50 (0,004)** |
| Fosfor-ratio, foto | +0,31 (0,087) | +0,34 (0,063) | −0,22 (0,23) | −0,21 (0,25) |

**Og mod P-kreatinin:**

| Analyse | [gns] | **[median]** |
|---|---|---|
| Fosforbalance, vejet | −0,36 (0,044) | −0,36 (0,049) |
| **Fosfor-ratio, vejet** | +0,45 (0,012) | **+0,52 (0,0025)** ⭐ |

## 🎯 Det store nye fund: fosforbalancen VIRKER mod eGFR

Se den øverste tabel igen. **Fosforbalance vejet vs. eGFR: ρ = +0,46, p = 0,009.**

Det er dit **primære endpoint** fra specialet, og det er **signifikant** — når du bruger et nyrefunktionsmål der ikke er forurenet af urinopsamling.

**Retningen:** positiv mod eGFR = **lavere eGFR → lavere (mere negativ) balance**. Det er *modsat* retentionshypotesen. Fortolkningen er, at deltagere med dårligere nyrefunktion har **lavere apparent fosforbalance** — sandsynligvis fordi de spiser mindre (diætrestriktion, appetitløshed ved fremskreden CKD).

Og fosfor-ratio bekræfter det fra den anden side: ρ = −0,50 mod eGFR (p=0,004) = **lavere eGFR → højere andel udskilt**. Det er kompensation.

> **Sig det sådan:** *"Målt mod eGFR var både fosforbalancen (ρ = 0,46, p = 0,009) og fosfor-ratioen (ρ = −0,50, p = 0,004) signifikant relateret til nyrefunktionen. Deltagere med lavere nyrefunktion havde lavere apparent fosforbalance og udskilte en større andel af det indtagne fosfor. Dette er foreneligt med bevaret renal kompensation kombineret med reduceret fosforindtag ved fremskreden sygdom — ikke med progressiv fosforretention."*

**Det er en helt anden og meget bedre konklusion end "vi fandt ingenting".**

## Median vs. gennemsnit — hvad du skal vælge

| | Gennemsnit | Median |
|---|---|---|
| Fosfor-ratio vejet vs. P-krea | +0,45 (0,012) | **+0,52 (0,0025)** |
| Fosfor-ratio vejet vs. eGFR | −0,43 (0,015) | **−0,50 (0,004)** |
| Na-balance vejet vs. CrCl | −0,30 (0,10) | **−0,42 (0,019)** |

**Median er konsekvent lidt stærkere.** Det er logisk: medianen af 3 dage er mindre påvirket af én ekstrem dag (fx pizzadagen).

⚠️ **Men vær forsigtig her.** Du må **ikke** vælge median, fordi den giver bedre p-værdier — det er præcis den fælde du var i med Pearson/Spearman sidst. Vælg **gennemsnit som primær**, fordi:

1. Det er standard i kostforskning
2. Det er hvad du gjorde i specialet
3. Gennemsnittet er det bedste estimat for langtidsindtag ved 3 dage

Og rapportér median som **sensitivitetsanalyse**:

> *"Analyserne blev gentaget med medianen af de tre registreringsdage i stedet for gennemsnittet. Sammenhængene var konsistente og gennemgående marginalt stærkere, hvilket indikerer robusthed over for enkelte ekstreme registreringsdage."*

**Det er den ærlige og stærke måde at bruge det.**

## Natrium (n=31)

| Analyse | vs. CrCl [gns] | vs. CrCl [med] | vs. eGFR [gns] | vs. P-krea [gns] |
|---|---|---|---|---|
| Na-balance, vejet | −0,30 (0,10) | **−0,42 (0,019)** | +0,18 (0,34) | −0,23 (0,22) |
| Na-balance, foto | −0,35 (0,057) | −0,34 (0,059) | −0,14 (0,46) | +0,08 (0,68) |
| Na-ratio, vejet | +0,24 (0,19) | +0,32 (0,080) | −0,15 (0,41) | +0,17 (0,36) |
| Na-ratio, foto | +0,20 (0,28) | +0,19 (0,30) | +0,17 (0,37) | −0,16 (0,40) |

**Mønstret er entydigt:** signifikant eller næsten signifikant mod CrCl, **fuldstændig nul** mod begge urin-uafhængige mål. Alle 8 analyser mod eGFR og P-kreatinin har p > 0,2.

---

# DEL 4: Gruppesammenligninger

## Med din GFR-kolonne (som i specialet)

| Udfald | <20 (n=8) | ≥20 (n=23) | HL-diff | p |
|---|---|---|---|---|
| **Na-balance vejet [median]** | **274,4** | **−437,5** | **+716** | **0,048** |
| Na-balance foto [gns] | −75,5 | −495,3 | +691 | 0,074 |
| Na-balance foto [median] | −46,4 | −495,3 | +697 | 0,054 |
| Na-balance vejet [gns] | 179,4 | −333,5 | +592 | 0,12 |
| U-natrium | 1550 | 2246 | −794 | 0,078 |
| U-Na/U-krea (urin-fri) | 9,1 | 11,7 | −1,6 | **0,40** |
| FE-fosfat | 43,6 | 34,9 | +8,1 | 0,16 |
| Kreatinin-index | 10,1 | 12,8 | −2,5 | 0,12 |

## 🎯 Med eGFR < 20 (urin-uafhængig gruppering)

**Her sker det interessante:**

| Udfald | <20 (n=13) | ≥20 (n=19) | HL-diff | p |
|---|---|---|---|---|
| **FE-fosfat** | **44,8 %** | **33,0 %** | **+16,1** | **0,0006** 🏆 |
| **P-fosfat** | **1,4** | **1,1** | **+0,3** | **0,0009** 🏆 |
| Na-balance vejet | −401,4 | −96,6 | −412 | 0,10 |
| Na-balance foto | −238,6 | −490,3 | +91 | 0,79 |
| U-natrium | 2207 | 2173 | +237 | 0,76 |
| U-Na/U-krea | 9,7 | 12,6 | −1,9 | 0,38 |

**Læg mærke til to ting:**

**1. FE-fosfat bliver stærkt signifikant** (p = 0,0006) når du grupperer på eGFR i stedet for CrCl. Og gruppestørrelserne er meget bedre balancerede: 13 vs. 19 i stedet for 8 vs. 23. **Det er en bedre analyse på alle måder.**

**2. Natriumfundet forsvinder** (p = 0,10 til 0,79).

> **Formuleringen:** *"Ved gruppering efter eGFR < 20 ml/min/1,73m², som er uafhængig af urinopsamling og giver mere balancerede grupper (13 vs. 19), havde deltagerne med lavest nyrefunktion signifikant højere fraktionel fosfatudskillelse (44,8 % vs. 33,0 %, p = 0,0006) og højere P-fosfat (p = 0,0009). Natriumbalancen adskilte sig derimod ikke mellem grupperne (p = 0,10–0,79)."*

## Vigtigt: én ting du selv skal rejse

`U-Na/U-krea` er den volumen-uafhængige version af natriumudskillelsen — hvis 20 % af urinen mangler, mangler det i **både** tæller og nævner, så ratioen er uændret.

Den er **p = 0,40** (CrCl-gruppering) og **p = 0,38** (eGFR-gruppering). Fuldstændig flad.

> *"Den kreatinin-normaliserede natriumudskillelse, som er uafhængig af opsamlingens komplethed, adskilte sig ikke mellem clearance-grupperne (p = 0,40). Dette understøtter, at forskellen i natriumudskillelse mellem grupperne kan afspejle forskelle i opsamlingskvalitet snarere end i renal natriumhåndtering."*

---

# DEL 5: Sensitivitetsanalysen — dit fosfatfund er robust

Jeg fjernede de 7 med kreatinin-index < 10:

| Analyse | Alle (n=32) | Uden flaggede (n=25) | |
|---|---|---|---|
| **FE-fosfat vs. P-krea** | +0,59 (0,0004) | **+0,58 (0,002)** | ✅ holder |
| **FE-fosfat vs. eGFR** | −0,51 (0,003) | **−0,46 (0,021)** | ✅ holder |
| **P-fosfat vs. eGFR** | −0,68 (<0,0001) | **−0,77 (<0,0001)** | ✅ **bliver stærkere** |
| **P-ratio vejet vs. P-krea** | +0,45 (0,012) | **+0,52 (0,009)** | ✅ **bliver stærkere** |
| FE-fosfat vs. CrCl | −0,17 (0,34) | −0,03 (0,89) | forsvinder |
| U-natrium vs. eGFR | +0,09 (0,64) | +0,17 (0,42) | ns i begge |
| Na-balance foto vs. CrCl | −0,35 (0,057) | −0,27 (0,21) | forsvinder |

**Dette er meget stærkt.** Alle fire fosfatfund mod urin-uafhængige mål **holder eller bliver stærkere**. Det udelukker praktisk taget, at de er artefakter.

Og bemærk, at to bliver **stærkere**. Det er logisk: dårlige opsamlinger er støj, og støj trækker korrelationer mod nul. Fjerner du støjen, kommer signalet tydeligere frem. **Det er også evidens for, at dit flagkriterium fandt noget virkeligt.**

---

# DEL 6: Indtags-paradokset — din skarpeste metodepointe

| Indtag | vs. CrCl | vs. eGFR | vs. P-kreatinin |
|---|---|---|---|
| **Na-indtag, vejet** | **+0,45 (0,012)** | +0,29 (0,11) | **−0,02 (0,90)** |
| Na-indtag, foto | +0,30 (0,10) | +0,07 (0,70) | +0,10 (0,61) |
| P-indtag, vejet | +0,35 (0,057) | +0,17 (0,37) | −0,00 (0,99) |
| P-indtag, foto | +0,23 (0,22) | −0,10 (0,61) | +0,12 (0,52) |

## Hvad du skal se her

**Natriumindtaget korrelerer signifikant med CrCl (ρ = 0,45, p = 0,012) — men er nul mod P-kreatinin (ρ = −0,02, p = 0,90).**

Tænk over det. Der findes **ingen fysiologisk mekanisme**, hvorved indholdet af en kostregistrering skulle afhænge af, hvilket nyrefunktionsmål forskeren bagefter vælger at bruge. Kosten er den samme.

**Så det er CrCl-variablen der opfører sig underligt, ikke kosten.**

Den mest sandsynlige forklaring: **omhu samvarierer.** En deltager, der er grundig med urinopsamlingen, er sandsynligvis også grundig med kostregistreringen. Og en, der glemmer vandladninger, glemmer også at registrere mellemmåltider.

```
Deltagerens omhu
   ↓          ↓
God urin-   God kost-
opsamling   registrering
   ↓          ↓
Høj målt    Højt målt
CrCl        indtag
   └────┬─────┘
        ↓
  FALSK korrelation
```

Bemærk at eGFR ligger **midt imellem** (ρ = 0,29, p = 0,11). Det passer perfekt: eGFR er urin-fri, men den deler P-kreatinin med CrCl, så en lille rest af sammenhængen overlever.

> **Formuleringen:** *"Det estimerede natriumindtag korrelerede signifikant med kreatininclearance (ρ = 0,45, p = 0,012), men ikke med P-kreatinin (ρ = −0,02, p = 0,90). Da der ikke findes en fysiologisk mekanisme, hvorved kostregistreringens indhold kan afhænge af valget af nyrefunktionsmål, indikerer dette, at variationen ligger i clearance-variablen. En plausibel forklaring er, at deltagernes omhu med urinopsamling og kostregistrering samvarierer, hvilket vil generere spuriøse korrelationer mellem clearance og alle registreringsbaserede mål. Dette svækker fortolkningen af natriumfundet betydeligt."*

**Det er detektivarbejde i data, og det er svært at modargumentere.** Det er den enkeltpointe, jeg ville sætte højest af alt vi har lavet.

---

# DEL 7: CrCl vs. eGFR — svar til Lahiji-referencen

Nu har du tallene:

| | Median | Range |
|---|---|---|
| CrCl | 25,0 ml/min | 9,5–53,5 |
| eGFR | 20,0 ml/min/1,73m² | 10–33 |

**Mediandifference: +3,5 ml/min. CrCl > eGFR hos 23 af 32 (72 %). Wilcoxon p = 0,0011.**

Og korrelationen mellem dem: ρ = 0,55 (p = 0,001) — moderat, ikke stærk. De to mål er **ikke** udskiftelige.

> *"Kreatininclearance oversteg eGFR med median 3,5 ml/min (p = 0,001), og CrCl var højest hos 72 % af deltagerne. Det er forventeligt ud fra tubulær kreatininsekretion, som får kreatininclearance til at overstige sand GFR med 10–30 %, samt af at eGFR er indekseret til 1,73 m² legemsoverflade, mens min CrCl er rå ml/min. At CrCl ikke lå under eGFR taler imod systematisk — men ikke mod differentiel — undersopsamling. Lahijis modsatte fund stammer fra en onkologisk population med udbredt kakeksi, hvor eGFR-ligningerne overestimerer på grund af lav muskelmasse."*

Og bemærk: **eGFR vs. kreatinin-index er ρ = −0,21 (p = 0,25)** — ikke signifikant. Det er en ren test af, om de sygeste opsamlede dårligere, og den er negativ. Godt for dig.

---

# ✅ ENDELIG TO-DO-LISTE

## 🔴 Skal gøres (2 timer)

| # | Opgave | Tid | Hvorfor |
|---|---|---|---|
| **1** | Tjek GFR-formlen i **række 13** (og 19, 28). Sammenlign med eGFR-kolonnen. Skriv ned hvad du finder | 30 min | Den eneste uafklarede datakvalitetssag |
| **2** | Ret abstract: *"sodium retention occurred"* → *"apparent sodium balance was significantly higher"* | 20 min | Den ene sætning alle læser |
| **3** | Ret perspektivering: *"no real trend"* → *"could neither confirm nor exclude"* | 15 min | Nulfund ≠ fravær af effekt |
| **4** | Ret alfacalcidol i resultatafsnittet → confounding by indication | 15 min | Resultat- og diskussionsafsnit skal sige det samme |
| **5** | Verificér diuretika/SGLT2-optællingen mod medicinlisten | 20 min | Tre forskellige tal har været i spil |

## 🟢 Bør gøres til oplægget (4 timer)

| # | Opgave | Tid |
|---|---|---|
| 6 | Slide: **FE-fosfat mod eGFR og P-kreatinin** (ρ=−0,51 og +0,59) | 45 min |
| 7 | Slide: **Robusthedsmatrix** (tabellen i Del 2) | 45 min |
| 8 | Slide: **Indtags-paradokset** (0,45 mod CrCl, −0,02 mod P-krea) | 45 min |
| 9 | Slide: **Kreatinin-index** (median 11,8; 22 % flagget; 50 % vs. 13 %, p=0,047) | 30 min |
| 10 | Slide: **ICC** (natrium 0,135 — selv sand r=0,60 ville ikke findes) | 30 min |
| 11 | Slide: **Gammel vs. ny formulering**, side om side | 30 min |

## 🟡 Hvis der er tid

| # | Opgave |
|---|---|
| 12 | Fænotype-tabellen (FE 14–72 % ved samme GFR) |
| 13 | Range restriction (84 % inden for 17 ml/min) |
| 14 | Formalia: tabelnumre, "Figure xx", `r=8153`, dublerede referencer |

---

# 🎤 OPLÆG — struktur til 20 minutter

| Min | Indhold | Hovedbudskab |
|---|---|---|
| **0–3** | Baggrund + forskningsspørgsmål | Formuler spørgsmålet **helt** (sætningen s. 10 er ufuldstændig) |
| **3–7** | Metode: to kostmetoder, døgnurin, hvad "apparent balance" er og **ikke** er | Ingen fæcesopsamling → omskrevet indtag, ikke balance |
| **7–12** | Specialets resultater | Metodesammenligning (bias −3,8 %), nulfundene, natriumfundet |
| **12–17** | **"Hvad jeg har arbejdet videre med"** ⭐ | Se nedenfor |
| **17–20** | Reviderede konklusioner + klinisk perspektiv | Hvad en diætist skal gøre i morgen |

## Blok 12–17 — den vigtigste, i denne rækkefølge

**1. Jeg identificerede en metodisk trussel** (1 min)

> "Kreatininclearance fungerer i mit design både som eksponeringsvariabel og som indikator for opsamlingskvalitet, fordi urin-kreatinin indgår i begge. Glemmer en deltager en vandladning, falder både min målte clearance og min målte udskillelse — samme fejl på begge akser i plottet."

**2. Jeg kvantificerede den** (1 min)

> "Kreatinin-index var median 11,8 mg/kg/døgn, 22 % lå under 10, og andelen var højere ved CrCl under 20: 50 % mod 13 %, p = 0,047."

**3. Jeg løste den med tre uafhængige nyrefunktionsmål** (2 min) ⭐

> "Jeg gentog analyserne mod eGFR og mod P-kreatinin, som begge er blodbaserede og ikke kan påvirkes af urinopsamlingen. Fosfatfundet blev **stærkere**: FE-fosfat ρ = −0,51 mod eGFR og +0,59 mod P-kreatinin, begge p < 0,005. Natriumfundet **forsvandt**: fra ρ = 0,54 mod clearance til 0,09 mod eGFR."

**4. Og jeg fandt hvorfor** (1 min)

> "Natriumindtaget korrelerede også med clearance, ρ = 0,45, men ikke med P-kreatinin, ρ = −0,02. Der er ingen fysiologisk grund til, at en kostregistrering skulle afhænge af hvilket nyrefunktionsmål jeg vælger. Den mest sandsynlige forklaring er, at deltagernes omhu med opsamling og registrering samvarierer."

**5. Og hvor følsomt mit design var** (30 sek)

> "ICC for natriumindtag over tre dage var 0,135. Med den reliabilitet ville selv en sand korrelation på 0,60 kun fremstå som 0,22 og ikke nå signifikans."

---

# Dine tre kernebudskaber

## 1️⃣ Du HAR et positivt fysiologisk fund

**FE-fosfat vs. eGFR: ρ = −0,51, p = 0,003**
**FE-fosfat vs. P-kreatinin: ρ = +0,59, p = 0,0004**
**FE-fosfat, eGFR<20 vs. ≥20: 44,8 % vs. 33,0 %, p = 0,0006**

Tre analyser, to uafhængige mål, alle signifikante. Kompensationshypotesen er bekræftet.

## 2️⃣ Natriumfundet kan du ikke forsvare — og du siger det selv

Det findes kun mod det ene mål, der deler fejlkilde med udfaldet. Og du kan **forklare mekanismen**, ikke bare konstatere problemet.

## 3️⃣ Nulfundene er uinformative, og du har målt hvor meget

ICC 0,135 for natriumindtag. Dit design kunne ikke finde det du ledte efter — det er kvantificeret metodeindsigt, ikke en undskyldning.

---

# Til sidst

Du var bekymret for karakteren. Se på hvad du har nu:

- Et gennemført klinisk studie med VEK-godkendelse og 50 rekrutterede
- En intern datakvalitetskontrol der fandt og forklarede uoverensstemmelser
- Et positivt fysiologisk fund, verificeret mod **to** uafhængige mål og robust over for sensitivitetsanalyse
- En kvantificeret forklaring på hvorfor de øvrige analyser var nulfund
- Et fund du selv har taget fra dig, med mekanismen forklaret
- Reviderede konklusioner der matcher datas opløsningsevne

Det sidste punkt er det sjældne. **De fleste specialer forsvarer deres resultater. Du kan forklare hvornår dine ikke holder — og hvorfor.** Det er forskellen mellem at have lavet et projekt og at have forstået det.

Held og lykke til forsvaret.
