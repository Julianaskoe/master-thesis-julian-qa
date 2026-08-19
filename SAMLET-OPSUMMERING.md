# Samlet opsummering — alt vi har fundet, forklaret let

*Data: `Book 1(Ark1).csv` (n=32) · Scripts: `analysis/` · Alle beregnede tal: `analysis/beregnet_fuld.csv`*

---

# DEL A: Svaret på dit spørgsmål om GFR

## Din GFR-formel er rigtig — jeg har rekonstrueret den

Med P-kreatinin i hånden kan jeg nu regne efter i stedet for at gætte. Din formel er:

$$\mathrm{CrCl}\ (\text{ml/min}) = \frac{U_{kreatinin}\ (\text{mmol/døgn})}{P_{kreatinin}\ (\text{mmol/L}) \times 1{,}44}$$

**Hvor kommer 1,44 fra?** Det er enhedsomregningen: der er 1440 minutter i et døgn, og du vil have svaret i ml/min i stedet for L/døgn:

$$\frac{\text{mmol/døgn}}{\text{mmol/L}} = \text{L/døgn} \quad\Longrightarrow\quad \times \frac{1000\ \text{ml}}{1440\ \text{min}} = \div 1{,}44$$

**Formlen er korrekt.** Det er standard kreatininclearance.

## ✅ Din FE-kolonne er perfekt — alle 32 rækker

Jeg genberegnede FE for hver deltager af rådataene:

| | Resultat |
|---|---|
| Maksimal afvigelse | **0,0000 %** |
| Antal fejl | **0 af 32** |

Det er så tæt på perfekt som det kan blive. Enhedsomregningen (µmol → mmol) er håndteret korrekt hele vejen. **Du kan bruge FE-kolonnen med fuld tillid.**

## 🔴 Men GFR-kolonnen har 5 fejl — og de er reelle

Her er hvad jeg gjorde: FE-formlen indeholder P-kreatinin og U-kreatinin. Da din FE-kolonne er 100 % korrekt, **ved jeg** at FE-kolonnen bruger de rigtige rådata. Så jeg regner clearance med de samme tal og sammenligner med din GFR-kolonne.

| Række | Din GFR | Korrekt CrCl | Afvigelse |
|---|---|---|---|
| 12 | 22,30 | 21,68 | −2,8 % |
| **13** | **25,76** | **18,40** | **−28,6 %** 🔴 |
| **19** | **53,51** | **58,51** | **+9,4 %** |
| **28** | **17,56** | **22,81** | **+29,9 %** 🔴 |
| **29** | **41,49** | **45,09** | **+8,7 %** |

De øvrige 27 rækker afviger under 0,06 % — altså perfekt.

### Jeg har fundet ud af hvad der gik galt

Jeg regnede baglæns: hvilket tal *skulle* der have stået, for at din GFR-værdi var kommet ud?

| Række | Din GFR svarer til U-krea | Faktisk U-krea | Din GFR svarer til P-krea | Faktisk P-krea |
|---|---|---|---|---|
| 12 | 8,927 | 8,680 | 270 | 278 |
| **13** | 10,386 | **7,420** | **200** | **280** |
| 19 | 14,563 | 15,925 | 207 | 189 |
| **28** | 9,054 | 11,760 | **465** | **358** |
| 29 | 13,800 | 15,000 | 251 | 231 |

**Se række 13 og 28.** Din GFR-kolonne har brugt P-kreatinin = 200 og 465, men de faktiske værdier er 280 og 358.

Læg mærke til: **række 29 har U-krea = 15,000 og din GFR-kolonne har brugt 13,800 — hvilket er præcis U-krea fra række 22.** Det ser ud som en celle, der er trukket fra den forkerte række. Det er den klassiske "formel kopieret med forskudt reference"-fejl.

### 🔴 Konsekvensen: to deltagere skifter gruppe

Dette er det vigtige:

| Deltager | Din GFR | Gruppe i specialet | Korrekt CrCl | Korrekt gruppe |
|---|---|---|---|---|
| **13** | 25,76 | ≥20 | **18,40** | **<20** |
| **28** | 17,56 | <20 | **22,81** | **≥20** |

**De to bytter plads.** Gruppestørrelserne er tilfældigvis uændrede (8 vs. 24), men det er **ikke** de samme 8 personer, som du analyserede i specialet.

## Hvad du skal gøre — og hvordan du siger det

**Gør dette:**
1. Åbn regnearket, klik på GFR-cellen i række 12, 13, 19, 28 og 29
2. Se om formlen peger på den rigtige række (den er sandsynligvis forskudt)
3. Ret dem, og genkør din natriumanalyse

**Sig dette til forsvaret** — og sig det *selv*, tidligt:

> *"Efter afleveringen gennemførte jeg en intern konsistenskontrol af mit datasæt ved at genberegne kreatininclearance af rådataene og sammenholde med den beregnede kolonne. Den fraktionelle fosfatudskillelse var korrekt i alle 32 tilfælde, men clearance-kolonnen indeholdt fem regnefejl, hvoraf to var betydelige. To deltagere er derfor placeret i den forkerte clearance-gruppe i specialets subgruppeanalyse. Jeg har genberegnet med de korrigerede værdier, og her er effekten på resultaterne."*

**Vær ikke bange for at sige det.** En studerende der finder og retter fejl i sit eget datasæt viser noget, man ikke kan læse sig til. En studerende der *ikke* har tjekket, og hvor censor finder det, er i en meget dårligere position. Og du har allerede rettet noget lignende (U-kreatinin 51,25), så du har historikken.

## Ændrer det dine konklusioner? Nej

Jeg har kørt alt med de korrigerede tal. Medianen for CrCl bliver 24,73 (mod 24,98) — praktisk taget uændret. Retningerne holder. **Det er en fejl i datakvalitet, ikke en fejl i konklusion.** Det er vigtigt at kunne sige.

---

# DEL B: Svaret på dit andet spørgsmål — skal indtag-udskillelse bruges?

Du spurgte, om balanceberegningen (indtag − udskillelse) skal bruges, eller om de andre analyser er mere relevante. **Nu kan jeg svare med tal.**

## Sammenligning af de tre måltyper

Du har tre måder at måle det samme:

| Mål | Formel | Hvad det er |
|---|---|---|
| **Balance** | $I - E$ | "Hvor meget bliver tilbage i kroppen" (i mg) |
| **Ratio** | $E / I$ | "Hvor stor en andel kommer ud" (i %) |
| **FE** | fosfatclearance / GFR | "Hvor stor en andel af det filtrerede kommer ud" (i %) |

Her er hvad de giver mod nyrefunktion:

| Mål | vs. CrCl | vs. P-kreatinin (opsamlings-immun) |
|---|---|---|
| Fosforbalance (vejet) | +0,14 (p=0,44) | **−0,36 (p=0,044)** ✅ |
| Fosfor-ratio (vejet) | +0,14 (p=0,44) | **+0,45 (p=0,012)** ✅ |
| **FE-fosfat** | −0,18 (p=0,32) | **+0,59 (p=0,0004)** 🏆 |
| Natriumbalance (foto) | −0,38 (p=0,034) | +0,08 (p=0,68) 🔴 |
| Natrium-ratio (foto) | +0,24 (p=0,20) | −0,16 (p=0,40) 🔴 |

**Din prioritering skal være:**

### 1. FE-fosfat — brug den som hovedendpoint 🏆

ρ = 0,59 mod P-kreatinin, p = 0,0004. Klart det stærkeste. Og den kræver **ingen kostregistrering**, så den har kun én støjkilde i stedet for to.

### 2. Ratio — næstbedst

Fosfor-ratio giver ρ = 0,45 (p = 0,012). Ratio normaliserer for indtag, så den er mindre sårbar over for at folk spiser forskelligt.

### 3. Balance — svagest, men brug den ikke *i stedet* for de andre

Fosforbalance giver ρ = −0,36 (p = 0,044). Den virker faktisk — men svagere.

## Hvorfor balancen er svagest — nu med dine egne tal

Jeg testede den påstand jeg fremsatte helt i starten (at balancen bare er indtaget):

| Mineral / metode | SD indtag | SD udskillelse | ρ(balance, indtag) | ρ(balance, udskillelse) |
|---|---|---|---|---|
| Fosfor, vejet | 267 | 235 | **+0,61** | −0,31 |
| Fosfor, foto | 276 | 233 | +0,55 | −0,48 |
| Natrium, vejet | 791 | **1232** | −0,05 | **−0,73** |
| Natrium, foto | 943 | **1218** | +0,14 | **−0,71** |

### 🔄 Jeg tog delvist fejl — og det er godt nyt for dig

Jeg sagde tidligere, at balancen ville korrelere >0,85 med indtaget. **Det gør den ikke.** For fosfor er det 0,61, og for natrium er det praktisk taget nul (−0,05).

**Hvorfor jeg tog fejl:** jeg regnede på IQR fra din baselinetabel, men den var beregnet på tværs af enkeltdage, ikke på 3-dages-gennemsnittene. Når du bruger gennemsnittet af 3 dage, udjævnes indtagsvariationen betydeligt — SD falder fra ~600 til 267.

**Hvad det betyder for dig:** din balance er **ikke** blot en omskrivning af indtaget. Det gør balancemålet mere legitimt end jeg påstod. Men se natriumrækkerne: ρ(balance, udskillelse) = −0,73. **Natriumbalancen er næsten ren udskillelse** — og udskillelsen er præcis det, der rammes af opsamlingsproblemet. Det er derfor natriumfundet er skrøbeligt.

**Sig dette hvis nogen spørger, om balancen bare er indtaget:**

> *"Jeg har testet det. Fosforbalancen korrelerer 0,61 med indtaget og −0,31 med udskillelsen, så begge komponenter bidrager. Natriumbalancen korrelerer derimod −0,73 med udskillelsen og kun −0,05 med indtaget — den er i praksis et udskillelsesmål. Det er relevant, fordi udskillelsen er den komponent, der påvirkes af opsamlingskvalitet."*

---

# DEL C: 🔴 Det vigtigste nye fund — dit natriumindtag er ikke måleligt

Det her er den mest betydningsfulde beregning i hele forløbet. Læs den grundigt.

## Hvad ICC er — helt enkelt

Du registrerede kost i **3 dage**. Så jeg kan spørge: *hvor meget af variationen i dine tal er ægte forskelle mellem personer, og hvor meget er blot at samme person spiser forskelligt fra dag til dag?*

Det tal kaldes **ICC** (intraklassekorrelation):

- **ICC = 1,0** → personerne er helt stabile. Én dag er nok.
- **ICC = 0,5** → halvdelen af dine tal er tilfældig dag-til-dag-støj
- **ICC = 0,1** → dine tal er næsten ren støj

## Dine ICC-værdier

| Variabel | n | Within-person CV | **ICC (1 dag)** | ICC (3-dages gns.) |
|---|---|---|---|---|
| Fosforindtag, vejet | 26 | 24,8 % | **0,451** | 0,706 |
| **Natriumindtag, vejet** | 26 | **48,9 %** | **0,135** 🔴 | **0,313** |
| Fosforindtag, foto | 11 | 20,6 % | 0,600 | 0,809 |
| Natriumindtag, foto | 12 | 32,7 % | 0,540 | 0,774 |

### 🔴 Se natriumindtag, vejet: ICC = 0,135

**Det betyder, at kun 14 % af variationen i dine natriumindtag-tal er ægte forskelle mellem personer. De øvrige 86 % er tilfældig dag-til-dag-variation.**

Within-person SD er **1066 mg/døgn** mod en between-person SD på kun 421. Altså: **samme person svinger 2,5 gange mere fra dag til dag, end personerne indbyrdes er forskellige.**

## Hvad det gør ved dine muligheder for at finde noget

Måleusikkerhed trækker korrelationer mod nul. Formlen:

$$r_{\text{observeret}} = r_{\text{sand}} \times \sqrt{\mathrm{ICC}}$$

**For natriumindtag** ($\sqrt{0{,}135} = 0{,}37$):

| Hvis sandheden er | Du ville måle | Signifikant? |
|---|---|---|
| 0,30 | 0,11 | ❌ nej |
| 0,40 | 0,15 | ❌ nej |
| 0,50 | 0,18 | ❌ nej |
| **0,60** | **0,22** | ❌ **nej** |

**Selv en meget stærk sand sammenhæng på 0,60 ville du ikke kunne finde.** Din måling af natriumindtag er simpelthen for upræcis til nogen som helst korrelationsanalyse.

**For fosforindtag, foto** ($\sqrt{0{,}600} = 0{,}78$):

| Hvis sandheden er | Du ville måle | Signifikant? |
|---|---|---|
| 0,40 | 0,31 | ❌ nej |
| **0,50** | **0,39** | ✅ **ja** |
| 0,60 | 0,46 | ✅ ja |

Her kan du faktisk finde noget, hvis effekten er moderat-stærk.

## Hvorfor natrium er så meget værre end fosfor

Det er faktisk fysiologisk logisk, og det er værd at kunne forklare:

| | Fosfor | Natrium |
|---|---|---|
| Hvor kommer det fra? | Jævnt fordelt i protein, mejeri, korn | Koncentreret i få ting: brød, pålæg, ost, færdigmad |
| Effekt af én ret | Lille | **Enorm** — én pizza kan fordoble dagens salt |
| Within-person CV | 25 % | **49 %** |
| Bordsalt registreret? | irrelevant | **Nej** — det er design-valget |

En dag med hjemmelavet mad og en dag med take-away giver **helt** forskellige natriumtal for samme person. Fosfor følger proteinindtaget, som er meget mere stabilt.

## 🎯 Dette er dit bedste svar på "hvorfor fandt du ingenting?"

Dette er langt stærkere end at citere Stremke, fordi **det er dine egne data der forklarer sin egen begrænsning:**

> **"Jeg har beregnet intraklassekorrelationen for kostregistreringerne. For fosforindtag var ICC for én dag 0,45 (vejet) og 0,60 (foto). For natriumindtag var den 0,135 ved den vejede metode — altså at kun 14 % af variationen udgjorde ægte forskelle mellem deltagere, mens 86 % var dag-til-dag-variation. Within-person variationskoefficienten var 49 %. Med den reliabilitet ville selv en sand korrelation på 0,60 kun fremstå som 0,22 i mine data og dermed ikke nå signifikans ved n=31. Studiets natriumanalyser var derfor metodisk ude af stand til at detektere selv stærke sammenhænge, og nulfundene kan ikke tolkes som evidens for fravær af sammenhæng."**

**Det er ikke en undskyldning — det er en kvantificeret metodeanalyse.** Og det er præcis, hvad der belønnes: du har målt din egen målings begrænsning.

## Og det giver dig en bedre klinisk anbefaling

Du blev spurgt, hvad en diætist skal gøre anderledes. Nu har du et konkret, tal-baseret svar:

> *"Til fosfor er 3 dages registrering rimeligt (ICC 0,71 for 3-dages-gennemsnittet). Til natrium er 3 dage utilstrækkeligt (ICC 0,31) — man kan ikke vurdere en enkelt patients saltindtag på 3 dages registrering. Her bør man bruge døgnurin i stedet, eller registrere flere dage. Og bordsalt skal registreres separat."*

Det er en anbefaling, en klinisk diætist kan bruge i morgen. Og den kommer fra dine egne data.

---

# DEL D: Robusthedsmatrix — hvad holder, og hvad holder ikke

Dette er hele dit materiale samlet i én tabel. Kolonnerne er tre forskellige måder at teste samme sammenhæng:

- **vs. CrCl** — dit oprindelige mål. Påvirkes af opsamlingskvalitet.
- **vs. P-kreatinin** — blodprøve. Kan **ikke** påvirkes af opsamling.
- **uden flaggede** — de 7 med kreatinin-index < 10 fjernet.

| Udfald | vs. CrCl | vs. P-kreatinin | Uden flaggede | Dom |
|---|---|---|---|---|
| **FE-fosfat** | −0,18 (0,32) | **+0,59 (0,0004)** | −0,02 (0,92) | 🏆 **ÆGTE** |
| **P-fosfat** | **−0,43 (0,013)** | **+0,59 (0,0004)** | **−0,50 (0,012)** | 🏆 **ÆGTE** |
| **P-ratio vejet** | +0,14 (0,44) | **+0,45 (0,012)** | +0,06 (0,78) | ✅ ægte |
| **P-balance vejet** | +0,14 (0,44) | **−0,36 (0,044)** | +0,22 (0,30) | ✅ ægte |
| U-fosfat | +0,39 (0,026) | **+0,36 (0,045)** | — | ✅ ægte |
| U-natrium | **+0,56 (0,001)** | +0,11 (0,55) | +0,61 (0,001) | 🔴 **artefakt** |
| U-Na/U-krea | +0,25 (0,17) | −0,12 (0,52) | +0,38 (0,062) | 🔴 intet |
| Na-balance foto | **−0,38 (0,034)** | +0,08 (0,68) | −0,33 (0,11) | 🔴 **artefakt** |
| Na-ratio foto | +0,24 (0,20) | −0,16 (0,40) | +0,15 (0,48) | 🔴 intet |
| Na-balance vejet | −0,27 (0,14) | −0,23 (0,22) | −0,22 (0,30) | 🟡 intet |

## Sådan læser du tabellen

**Reglen:** et fund er ægte, hvis det holder mod **P-kreatinin**, fordi det mål er immunt over for opsamlingsproblemet.

**Læg mærke til at fortegnene vender mellem de to første kolonner.** Det er ikke en fejl — høj CrCl = **god** nyre, høj P-kreatinin = **dårlig** nyre. Så negativ mod CrCl og positiv mod P-kreatinin betyder **det samme fysiologiske udsagn**.

## 🏆 To fund holder helt

**1. FE-fosfat stiger når nyrefunktionen falder** (ρ = 0,59 mod P-kreatinin, p = 0,0004, 95 % CI 0,30–0,78)

Det er kompensationshypotesen — dit speciales kernespørgsmål. **Og det er dit positive fund.**

**2. P-fosfat stiger når nyrefunktionen falder** (ρ = 0,59, p = 0,0004)

Denne er signifikant i **alle tre** kolonner. Det er den mest robuste sammenhæng i hele materialet. Den er ikke overraskende fysiologisk — men det er præcis dét, der gør den værdifuld: **den validerer dit datasæt.** Hvis dine data kan reproducere en velkendt sammenhæng, kan man have tillid til dem.

Sig det: *"P-fosfat korrelerede med nyrefunktionen i den forventede retning uanset hvilket nyrefunktionsmål jeg brugte. Det er en positiv kontrol, der understøtter datakvaliteten."*

## 🔴 Natriumfundet holder ikke

| U-natrium vs. | ρ | p |
|---|---|---|
| CrCl | **+0,56** | **0,001** |
| P-kreatinin | +0,11 | 0,55 |

Sammenhængen findes **kun**, når nyrefunktionen måles med det redskab, der deler fejlkilde med udfaldet.

## Og her er sømmet i kisten — jeg fandt hvorfor

Jeg splittede natriumbalancen op i sine to dele:

| | vs. CrCl | vs. P-kreatinin |
|---|---|---|
| U-natrium (udskillelse) | +0,56 (p=0,001) | +0,11 (p=0,55) |
| **Na-INDTAG, vejet** | **+0,49 (p=0,005)** | **−0,02 (p=0,90)** |
| **P-INDTAG, vejet** | **+0,40 (p=0,026)** | **−0,00 (p=0,99)** |

**Se de to nederste rækker.** Deltagernes *indtag* korrelerer signifikant med CrCl (ρ = 0,49 og 0,40) — men **overhovedet ikke** med P-kreatinin (ρ = −0,02 og −0,00).

Tænk over hvad det betyder. Der er ingen fysiologisk grund til, at kostregistreringen skulle hænge sammen med clearance men ikke med P-kreatinin. **Det peger på, at det er CrCl-variablen der opfører sig underligt, ikke kosten.**

Den mest sandsynlige forklaring: deltagere, der er grundige med **urinopsamlingen**, er også grundige med **kostregistreringen**. Omhu er en personlighedsegenskab, ikke en fysiologisk variabel. Dårlig opsamling → lav målt CrCl. Dårlig kostregistrering → lavt målt indtag. Begge falder sammen → falsk korrelation.

**Formuleringen:**

> *"Både natrium- og fosforindtag korrelerede signifikant med kreatininclearance (ρ = 0,49 og 0,40), men ikke med P-kreatinin (ρ = −0,02 og −0,00). Da der ikke er nogen fysiologisk mekanisme, hvorved kostregistreringens indhold skulle afhænge af, hvilket nyrefunktionsmål der anvendes, indikerer dette, at variationen ligger i clearance-variablen. En sandsynlig forklaring er, at deltagernes omhu med urinopsamling og kostregistrering samvarierer, hvilket ville skabe en spuriøs korrelation mellem clearance og alle registreringsbaserede mål. Dette svækker fortolkningen af natriumfundet betydeligt."*

**Det er den skarpeste metodiske pointe, du kan fremføre.** Den er detektivarbejde i data, og den er svær at modargumentere.

## Gruppesammenligning med de rettede GFR-værdier

| Udfald | <20 (n=8) | ≥20 (n=23-24) | p |
|---|---|---|---|
| **Na-balance foto** | −27,3 | −495,3 | **0,038** |
| **Na-ratio foto** | 100,6 % | 126,2 % | **0,043** |
| U-natrium | 1550 | 2246 | 0,064 |
| Na-balance vejet | 179,4 | −324,3 | 0,19 |
| U-Na/U-krea (opsamlings-immun) | 11,1 | 11,2 | **0,72** |
| FE-fosfat | 42,5 % | 34,9 % | 0,19 |
| Kreatinin-index | 10,1 | 13,5 | 0,064 |

Bemærk mønstret igen: **foto-metoden er signifikant, vejet er ikke, og det volumen-uafhængige mål er fuldstændig flat (p=0,72).**

Og bemærk kreatinin-index: 10,1 vs. 13,5 (p=0,064). <20-gruppen har lavere opsamlingskvalitet. Igen samme historie.

---

# DEL E: Metodesammenligningen (Bland-Altman)

Dette er dit speciales anden halvdel, og her er tallene:

| | Fosforindtag | Natriumindtag |
|---|---|---|
| n | 30 | 30 |
| **Bias** (foto − vejet) | **−39 mg/døgn** | **−194 mg/døgn** |
| 95 % CI for bias | −135 til +57 | −471 til +83 |
| SD på differencen | 257 | 741 |
| **95 % limits of agreement** | **−543 til +465** | **−1646 til +1258** |
| Bias i % af middelværdi | −3,8 % | −9,2 % |
| Wilcoxon | p = 0,33 | p = 0,12 |
| Proportional bias | ρ = −0,05 | ρ = +0,08 |

## Hvad du kan sige — og det er faktisk positivt

**1. Bias er lille og ikke signifikant for begge.** Fotometoden underestimerer med kun 3,8 % for fosfor. **Det er et godt resultat** — det betyder, at metoden er brugbar på gruppeniveau.

**2. Ingen proportional bias** (ρ = −0,05 og +0,08). Det betyder, at bias er **konstant** — den bliver ikke større ved højt indtag. Det er vigtigt, fordi det betyder, at en simpel korrektionsfaktor faktisk *kunne* virke. Sig det, det er et pænt fund.

**3. Men limits of agreement er brede.** ±500 mg for fosfor, ±1450 mg for natrium. **Det betyder: brugbar på gruppeniveau, ikke på individniveau.**

Og nu kan du sætte det i perspektiv med ICC-tallene: **de brede limits skyldes ikke primært, at fotometoden er dårlig — de skyldes, at kosten svinger fra dag til dag.** Within-person SD for natrium var 1066 mg. Limits of agreement er ±1450. De to tal er i samme størrelsesorden.

**Det er en vigtig og nuanceret pointe:**

> *"De brede limits of agreement afspejler ikke udelukkende metodeforskelle, men også reel biologisk dag-til-dag-variation i kosten, som var af samme størrelsesorden (within-person SD 1066 mg/døgn for natrium). En del af uenigheden mellem metoderne er derfor ikke metodefejl, men genuint forskellige måledage."*

⚠️ Men vær opmærksom: hvis dine to metoder dækkede **samme** dage (som du skrev), gælder det argument mindre. Tjek det — hvis metoderne blev brugt på samme dage, er uenigheden ren metodefejl, og så skal du ikke bruge argumentet.

---

# DEL F: OPSUMMERING — hvad du bruger, og hvordan

## Dine tre budskaber

Hvis du kun husker tre ting til forsvaret, så disse:

### 1️⃣ Du HAR et positivt fysiologisk fund

**FE-fosfat stiger med aftagende nyrefunktion: ρ = 0,59, 95 % CI [0,30; 0,78], p = 0,0004.**

Målt mod P-kreatinin, som er immunt over for opsamlingsproblemer. Det bekræfter kompensationshypotesen, og det er dit speciales kernespørgsmål.

### 2️⃣ Natriumfundet kan du ikke forsvare — og du siger det selv

Det findes kun mod CrCl (ρ=0,56), ikke mod P-kreatinin (ρ=0,11). Og du kan **forklare hvorfor**: indtaget korrelerer også med CrCl men ikke med P-kreatinin, hvilket peger på at omhu med opsamling og med kostregistrering samvarierer.

### 3️⃣ Nulfundene er uinformative, og du har målt hvor meget

ICC for natriumindtag = 0,135. Selv en sand korrelation på 0,60 ville fremstå som 0,22 og ikke nå signifikans. **Dit design kunne ikke finde det du ledte efter.** Det er en kvantificeret metodeindsigt, ikke en undskyldning.

## De reviderede formuleringer

| Sted | Erstat | Med |
|---|---|---|
| Abstract | "sodium retention occurred below 20 ml/min" | "apparent sodium balance was significantly higher below 20 ml/min" |
| Perspektivering | "no real trend towards an increasing retention" | "the study could neither confirm nor exclude clinically relevant retention" |
| Resultater | "forskellen skyldes alfacalcidol" | "kan ikke adskilles fra effekten af nyrefunktion (confounding by indication)" |

## Slide-rækkefølge til oplægget (blok 12-17 min)

| # | Slide | Hovedtal |
|---|---|---|
| 1 | **Datakvalitetskontrol** | FE korrekt i 32/32; 5 fejl i GFR-kolonnen; 2 deltagere skiftede gruppe |
| 2 | **Kreatinin-index** | Median 11,8 mg/kg/døgn; 7 flaggede (22 %); 50 % vs. 13 % under/over CrCl 20 (p=0,047) |
| 3 | 🏆 **FE-fosfat mod P-kreatinin** | **ρ = 0,59, p = 0,0004** — kompensationen findes |
| 4 | **Robusthedsmatrix** | Tabellen fra Del D — hvad holder mod begge mål |
| 5 | 🔴 **Hvorfor natriumfundet ikke holder** | Indtaget korrelerer også med CrCl (0,49) men ikke P-krea (−0,02) |
| 6 | **ICC** | Natrium 0,135 — selv sand r=0,60 ville ikke findes |
| 7 | **Reviderede konklusioner** | Gammel vs. ny tekst, side om side |

Slide 3 og 5 er dine to vigtigste. Slide 3 er dit positive fund; slide 5 viser, at du kan tage et resultat fra dig selv.

## To-do i rækkefølge

| # | Opgave | Tid |
|---|---|---|
| **1** | 🔴 Ret GFR række 12, 13, 19, 28, 29 i regnearket | 30 min |
| **2** | Genkør natriumanalysen med de rettede grupper | 30 min |
| 3 | Byg slide 3 (FE mod P-kreatinin) | 45 min |
| 4 | Byg slide 5 og 6 (indtag-paradokset + ICC) | 1 t |
| 5 | Skriv de tre reviderede formuleringer | 45 min |
| 6 | Fænotype-tabellen (14–72 % FE ved samme GFR) | 30 min |

## Det du siger, hvis censor spørger "hvad har du lært?"

> *"Jeg har lært, at valget af nyrefunktionsmål ikke er neutralt. Kreatininclearance og urinudskillelse deler samme fejlkilde — urinopsamlingen — og det kan skabe sammenhænge, der ikke findes. Ved at gentage analyserne mod P-kreatinin, som er uafhængig af opsamlingen, kunne jeg skelne: fosfatfundet blev stærkere og holder, natriumfundet forsvandt. Og ved at beregne intraklassekorrelationen på mine egne kostregistreringer kunne jeg kvantificere, hvor stor en sammenhæng mit design overhovedet var i stand til at opdage. Det væsentligste, jeg tager med, er, at man skal måle sin målings begrænsning, før man fortolker sit resultat."*

---

**Én sidste ting:** du var bekymret for at dumpe. Se på hvad du nu har: et gennemført klinisk studie, en intern datakvalitetskontrol der fandt fejl du selv retter, et positivt fysiologisk fund testet mod to uafhængige mål, en kvantificeret forklaring på dine nulfund, og reviderede konklusioner der matcher dine datas opløsningsevne.

Det er ikke en studerende der dumper. Det er en studerende der har lært at arbejde videnskabeligt. Held og lykke.
