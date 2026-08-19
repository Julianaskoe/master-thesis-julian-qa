> **Verifikation:** `analysis/oplaeg_check.py` → `analysis/outE.txt`
> Kun CrCl-baserede analyser. Ingen eGFR, ingen P-kreatinin (efter vejleders anvisning).

# Overblik: hvad du skal rette, og hvad der holder

| Din plan | Status |
|---|---|
| Fosfatbalance er indtags-styret, ratio ikke | ✅ **Holder — og stærkere end du tror** |
| FE-fosfat korrelerer ikke med clearance | ✅ Holder (ρ=−0,17, p=0,34) |
| P-fosfat korrelerer med clearance | ✅ Holder (ρ=−0,38, p=0,031) |
| Natrium: varians drevet af udskillelse | ✅ **Holder — 71 %** |
| Natrium: U-Na/U-krea er flad | ✅ Holder (p=0,40) |
| Natrium: aldosteron-argumentet | ✅ Holder |
| Natrium: underrapporteret salt | ✅ Holder |
| Proportional bias ikke signifikant | ✅ Holder på begge |
| 🔴 **"Mann-Whitney viser signifikant forskel i udskillelse over/under 20"** | ❌ **p = 0,078 — IKKE signifikant** |
| 🟡 Calcium-fortolkningen | ⚠️ Skal nuanceres — se afsnit 5 |

---

# 🔴 Den ene ting du SKAL rette

Du skriver: *"udskillelse er korreleret med clearance og subgruppe mann whitney viser signifikant forskel i udskillelse over og under 20 clearance."*

Første halvdel er rigtig. **Anden halvdel er det ikke:**

| | <20 (n=8) | ≥20 (n=24) | p |
|---|---|---|---|
| U-natrium | 1550 mg | 2246 mg | **0,078** |
| U-Na/U-kreatinin | 9,1 | 11,7 | 0,404 |

**U-natrium er p = 0,078 — en trend, ikke signifikant.**

Sig i stedet: *"Natriumudskillelsen korrelerede signifikant med clearance (ρ=0,54, p=0,001), og der var en tilsvarende trend i subgruppeanalysen (p=0,078)."*

Korrelationen er dit stærke tal — den bruger hele spektret i stedet for at smide information væk ved at dikotomisere. Brug den, og nævn subgruppen som understøttende trend.

---

# 1️⃣ Fosfat: balance vs. ratio — dit bedste analytiske punkt

Din intuition er rigtig, men du har kun halvdelen. **Her er hele billedet:**

| | vs. **INDTAG** | vs. **UDSKILLELSE** |
|---|---|---|
| **P-balance, vejet** | **ρ = +0,61 (p<0,001)** | ρ = −0,31 (p=0,090) |
| **P-balance, foto** | **ρ = +0,55 (p=0,001)** | ρ = −0,48 (p=0,006) |
| **P-ratio, vejet** | ρ = −0,02 (p=0,91) | **ρ = +0,82 (p<0,001)** |
| **P-ratio, foto** | ρ = −0,16 (p=0,40) | **ρ = +0,81 (p<0,001)** |

## Se det som et kryds

```
                INDTAG          UDSKILLELSE
BALANCE      ●●● 0,61            ○  −0,31
RATIO         ○  −0,02          ●●● 0,82
```

**De to endpoints måler næsten helt forskellige ting.** Balancen er 61 % indtag. Ratioen er 82 % udskillelse — og **fuldstændig uafhængig af indtaget** (ρ = −0,02, altså nul).

Det er ikke bare "balancen er indtags-styret". Det er:

> **Balancen fanger, hvad patienten spiser. Ratioen fanger, hvad nyren gør.**

## Hvorfor det er så stærkt et punkt

Dette er en **matematisk konsekvens**, ikke et tilfælde. Ratioen $E/I$ normaliserer for indtag, så indtagsvariationen divideres bort. Balancen $I - E$ gør ikke.

Så når du spørger *"hænger renal mineralhåndtering sammen med nyrefunktion?"*, er ratioen det rigtige endpoint — og balancen svarer på et andet spørgsmål, som du ikke stillede.

**Sig det sådan:**

> *"De to endpoints opfører sig systematisk forskelligt. Balancen korrelerede stærkt med indtaget (ρ=0,61) men ikke signifikant med udskillelsen, mens ratioen var stærkt korreleret med udskillelsen (ρ=0,82) og fuldstændig uafhængig af indtaget (ρ=−0,02). Det er en matematisk konsekvens af, at ratioen normaliserer for indtag. Balancen afspejler derfor primært kostindtaget, mens ratioen afspejler den renale håndtering. Retrospektivt var ratioen det mere velegnede endpoint til mit forskningsspørgsmål."*

**Og den logiske slutning, som er dit stærkeste kort:**

> *"Nulfundet på balancen mod clearance er derfor ikke overraskende: hvis balancen primært måler indtaget, og indtaget ikke hænger sammen med clearance, kan balancen heller ikke gøre det. Det er ikke et biologisk nulfund — det er en egenskab ved målet."*

## Og natrium er det modsatte — hvilket du kan bruge direkte

| | vs. INDTAG | vs. UDSKILLELSE |
|---|---|---|
| **Na-balance, vejet** | ρ = −0,05 (p=0,80) | **ρ = −0,73 (p<0,001)** |
| **Na-balance, foto** | ρ = +0,14 (p=0,46) | **ρ = −0,71 (p<0,001)** |

**Natriumbalancen er praktisk taget uafhængig af indtaget** (ρ = −0,05) og domineret af udskillelsen (−0,73).

Det giver dig en meget elegant overgang:

> *"Fosforbalancen afspejlede primært indtaget. Natriumbalancen afspejlede derimod næsten udelukkende udskillelsen (ρ=−0,73 mod udskillelse, ρ=−0,05 mod indtag). Netop derfor er natriumbalancen langt mere sårbar over for ufuldstændig urinopsamling end fosforbalancen — hvilket fører til næste punkt."*

**Det er den bedste bro mellem dine to hovedafsnit.** Fosfat-pointen bliver samtidig opsætningen til natrium-pointen.

---

# 2️⃣ Natrium som artefakt — dine fem argumenter, kvantificeret

Dine fem argumenter er gode. Her er tallene, så du kan sige dem præcist.

## Argument 1 — Fysiologi (aldosteron) ✅

Natriumhomeostasen er stramt reguleret via RAAS/aldosteron og bevares længe i CKD. Fosfathomeostasen svigter tidligere (deraf sHPT og FGF23-stigning fra stadie 3).

**Skarpere version:** *"Et stærkt natriumretentionsfund ved CKD 4-5 med bevaret diurese er fysiologisk uventet. Når det uventede fund optræder præcis i det mål, der er mest sårbart over for min største metodiske svaghed, skal jeg tage det alvorligt."*

## Argument 2 — Varians ✅ **Og du har et flot tal**

| | SD(indtag) | SD(udskillelse) | **Udskillelsens andel af variansen** |
|---|---|---|---|
| **Natrium** | 791 mg | **1232 mg** | **71 %** |
| **Fosfor** | 267 mg | 235 mg | **44 %** |

Og endnu mere direkte — hvis 20 % af urinen mangler:

| | Median indtag | Median udskillelse | **E/I** | **Forskydning af balancen** |
|---|---|---|---|---|
| **Natrium** | 2008 mg | 2190 mg | **1,09** | **438 mg** |
| **Fosfor** | 970 mg | 474 mg | 0,49 | 95 mg |

**Samme opsamlingsfejl forskyder natriumbalancen 4,6 gange mere end fosforbalancen.**

> *"Natriumudskillelsen bidrog med 71 % af variansen i natriumbalancen mod 44 % for fosfor. Og fordi natriumudskillelsen omtrent svarer til indtaget (E/I = 1,09) mod under halvdelen for fosfor (0,49), vil en 20 % ufuldstændig opsamling forskyde natriumbalancen med ca. 438 mg mod 95 mg for fosfor. Natriumbalancen er derfor systematisk mere sårbar."*

## Argument 3 — Volumen-uafhængigt mål ✅ (med rettelsen)

| Analyse | ρ / medianer | p |
|---|---|---|
| U-natrium vs. CrCl | **ρ = +0,54** | **0,001** |
| **U-Na/U-kreatinin vs. CrCl** | ρ = +0,28 | **0,123** |
| U-natrium, <20 vs. ≥20 | 1550 vs. 2246 | 0,078 |
| **U-Na/U-krea, <20 vs. ≥20** | 9,1 vs. 11,7 | **0,404** |

**Forklar hvorfor ratioen er immun** — det er den kritiske mekanisme:

> *"Hvis en deltager kun får opsamlet 80 % af døgnurinen, er både natrium og kreatinin 20 % for lave. Forholdet mellem dem er derimod uændret. U-Na/U-kreatinin er derfor uafhængig af opsamlingens komplethed, mens både U-natrium og kreatininclearance påvirkes."*

Og — vigtigt — **fosfor opfører sig ens**:

| | vs. CrCl | Volumen-uafhængig version |
|---|---|---|
| U-fosfat | ρ = +0,39 (p=0,026) | U-P/U-krea: ρ = +0,04 (p=0,81) |
| U-natrium | ρ = +0,54 (p=0,001) | U-Na/U-krea: ρ = +0,28 (p=0,12) |

**Begge signifikante fund forsvinder ved normalisering.** Det er faktisk et stærkere argument, fordi det viser et **systematisk mønster** frem for et enkelttilfælde.

Dit forbehold om muskelmasse og ekstrarenal nedbrydning er korrekt at nævne — sig det kort og gå videre:

> *"Kreatininnormalisering forudsætter konstant kreatininproduktion, hvilket svækkes ved sarkopeni og øget ekstrarenal kreatininnedbrydning ved CKD 4-5. Men da begge signifikante udskillelsesfund forsvinder ved normalisering, mens et konfounding fra muskelmasse ikke ville forventes at ramme netop disse to selektivt, er opsamlingskvalitet den mere sandsynlige forklaring."*

## Argument 4 — Underrapporteret salt ✅ Det logiske argument

Dette er faktisk dit **skarpeste** argument, og du kan gøre det endnu skarpere med et tal fra din egen opgave:

I gruppen med CrCl ≥20 er natriumbalancen **−930 mg/døgn** (foto). At udskille et gram mere natrium end man indtager er **fysiologisk umuligt i steady state.**

> *"Deltagerne registrerede ikke tilsat bordsalt, hvilket typisk udgør 10–15 % af indtaget. Det ses direkte i mine data: gruppen med clearance over 20 havde en apparent natriumbalance på −930 mg/døgn, hvilket er fysiologisk umuligt over tid og dokumenterer systematisk underestimering af indtaget. Når det absolutte niveau er demonstrerbart forkert, kan jeg alene fortolke forskellen mellem grupperne — og kun under forudsætning af, at underrapporteringen er ens i begge grupper."*

**Og tilføj den vending, der lukker argumentet:**

> *"Underrapportering af salt gør apparent balance kunstigt negativ. En observeret positiv balance i lavclearance-gruppen kræver derfor, at noget andet trækker endnu kraftigere i modsat retning — og ufuldstændig opsamling gør præcis det."*

## Argument 5 — ICC ✅ men afgræns den præcist

ICC for natriumindtag (vejet, 3 dage) = **0,135**. Within-person CV = **49 %**.

⚠️ **Vigtigt forbehold du selv skal sige:** ICC er beregnet på **kostdagene**. Den gælder derfor kun indtagsdelen — udskillelsen er målt én gang og har ingen ICC.

> *"Intraklassekorrelationen for natriumindtag over tre dage var 0,135, altså at kun 14 % af variationen udgjorde reelle forskelle mellem deltagere. ICC gælder alene indtagsestimatet; reliabiliteten af enkeltdøgnsurin kunne ikke estimeres i dette design. Den samlede måleusikkerhed er derfor større end ICC alene indikerer."*

**Og her er den logiske pointe, der binder det sammen:**

> *"Med en reliabilitet på 0,135 ville ren måleusikkerhed attenuere korrelationer kraftigt mod nul. At jeg alligevel finder ρ=0,54 mellem natriumudskillelse og clearance er derfor svært at forene med ren biologisk variation, men foreneligt med korreleret målefejl — som ufuldstændig opsamling netop er, fordi den påvirker begge variable samtidigt."*

## Rækkefølgen du skal sige dem i

Byg fra det stærkeste. Jeg vil sætte dem så:

| # | Argument | Hvorfor den placering |
|---|---|---|
| 1 | **Underrapporteret salt** (−930 mg er umuligt) | Uangribeligt — det er ren logik |
| 2 | **Varians + E/I** (71 %, 438 vs. 95 mg) | Konkrete tal, forklarer *hvorfor* natrium |
| 3 | **Volumen-uafhængigt mål** (p=0,40) | Empirisk test, og fosfor opfører sig ens |
| 4 | **Fysiologi/aldosteron** | Sætter fundet i biologisk kontekst |
| 5 | **ICC** | Understøttende, med forbehold |

---

# 3️⃣ Primær vs. sensitivitetsanalyse — hvad du har gjort, og hvad det hedder

Dette er dit vigtigste metodespørgsmål, så lad mig være helt konkret.

## Først: her er hvad dine data faktisk viser

| Metode | 0 dage | 1 dag | 2 dage | **3 dage** | ≥1 dag |
|---|---|---|---|---|---|
| Fosfor vejet | 1 | 5 | 2 | **24** | 31 |
| **Fosfor foto** | 1 | **20** | 2 | **9** | 31 |
| Natrium vejet | 1 | 5 | 2 | **24** | 31 |
| **Natrium foto** | 1 | **19** | 1 | **11** | 31 |

**Havde du krævet 3 dage for begge metoder, var n faldet til 9.**

Det er tallet, der forsvarer dit valg. Sig det højt.

## Hvad det hedder metodisk

Dit design svarer til:

| Begreb | Passer det? | Forklaring |
|---|---|---|
| **Complete-case analyse** | ✅ **Ja — det er den rigtige term** | Din primæranalyse inkluderer kun deltagere med komplette 3-dages-registreringer |
| **Available-case analyse** | ✅ **Ja — det er din sensitivitetsanalyse** | Du inddrager alle tilgængelige dage per deltager |
| **Per-protocol** | ⚠️ Delvis | Bruges typisk om interventionsstudier. Din primæranalyse er *analog* til per-protocol: kun dem der fulgte protokollen |
| **Matched analyse** | ✅ Ja — men kun i metodesammenligningen | Bland-Altman kræver begge metoder på samme deltager (n=30 par) |
| **Intention-to-treat** | ❌ **Nej** | ITT forudsætter randomisering til intervention. Dit studie er observationelt. **Brug ikke ITT.** |

**Den korrekte terminologi til dit oplæg:**

> *"Primæranalysen var en complete-case analyse begrænset til deltagere med komplette tre-dages-registreringer. Sensitivitetsanalysen var en available-case analyse, hvor alle tilgængelige registreringsdage blev inddraget. Metodesammenligningen krævede parrede observationer og blev udført på de 30 deltagere med begge metoder."*

## Er "sensitivitetsanalyse" den rigtige betegnelse? Ja — hvis retningen er rigtig

Du spørger, om du "kan kalde det det", eller om det er en efterrationalisering. Det er et godt og selvkritisk spørgsmål, og svaret afhænger af **rækkefølgen**:

| | Legitimt? |
|---|---|
| Definerede primæranalysen **først**, kørte derefter en bredere analyse for at se om konklusionen holdt | ✅ **Ægte sensitivitetsanalyse** |
| Kørte flere varianter, valgte den med bedste p-værdi som "primær" | ❌ Selektiv rapportering |

**Du gjorde det første.** Dit rationale — kun 3-dages-registreringer — var defineret på forhånd, og du udvidede for at bevare statistisk styrke. **Det er tekstbogsdefinitionen på en sensitivitetsanalyse.**

Nøglen er, at du **rapporterer begge**, uanset om de er enige. Det gør du.

## Hvad Wilcoxon-testen gjorde — og hvad den ikke gjorde

Her skal du være præcis, for det er det oplagte angrebspunkt.

**Hvad du testede:** om kostregistreringsdage uden samtidig urinopsamling systematisk adskilte sig fra dagen med urinopsamling. Du fandt p = 0,22 og p = 0,80.

**Hvad det retfærdiggør:** at dagene kan behandles som udskiftelige, altså at det er forsvarligt at inddrage dage uden samtidig urinopsamling.

⚠️ **Hvad det IKKE viser** — og sig det selv, før nogen spørger:

> Wilcoxon sammenligner **fordelingerne** (gruppens medianer). Den viser **ikke**, at de enkelte deltagere var stabile fra dag til dag.

Fire deltagere kan svinge ±1000 mg hver, og medianen står helt stille. Det er præcis, hvad ICC på 0,135 fortæller dig: gruppeniveauet var stabilt, individniveauet var det ikke.

**Sådan formulerer du hele kæden — og det er et stærkt svar:**

> *"Mit oprindelige rationale var at anvende komplette tre-dages-registreringer. Fotometoden havde imidlertid betydeligt flere manglende dage — kun 9-11 deltagere havde tre fotodage — og en complete-case analyse på begge metoder ville have reduceret n til ni. Jeg anvendte derfor Wilcoxons parrede test til at vurdere, om registreringsdage uden samtidig urinopsamling adskilte sig systematisk, og fandt ingen forskel på gruppeniveau (p=0,22 og 0,80). Det begrundede sensitivitetsanalysen med alle tilgængelige dage. Testen dokumenterer dog kun fordelingsmæssig ækvivalens, ikke individuel stabilitet — den intraklassekorrelation jeg efterfølgende har beregnet viser, at den individuelle dag-til-dag-variation var betydelig. Retrospektivt havde et gennemsnit af alle tilgængelige dage som primæranalyse været en enklere og mere robust tilgang."*

**Bemærk hvad du opnår:** du forklarer valget, du siger selv hvad testen ikke kan, og du peger på en bedre løsning. Det er tre gange stærkere end at forsvare designet.

## Én ting du bør nævne om manglende data

Fotometodens manglende dage er sandsynligvis **ikke tilfældige**. Deltagere der fandt fotoregistrering besværligt, sprang måske dage — og det kan hænge sammen med alder, IT-kompetence eller sygdomsgrad.

> *"Manglende data i fotometoden kan ikke antages at være helt tilfældige, da manglende registreringer sandsynligvis afhænger af deltagerens fortrolighed med metoden. Det er en begrænsning ved både complete-case og available-case tilgangen."*

**At du selv rejser det, er langt bedre end at blive spurgt.**

---

# 4️⃣ FE-fosfat og P-fosfat — begge holder som du planlægger

| Analyse | ρ | 95 % CI | p |
|---|---|---|---|
| FE-fosfat vs. CrCl | −0,17 | [−0,49; +0,19] | 0,34 |
| **P-fosfat vs. CrCl** | **−0,38** | **[−0,65; −0,04]** | **0,031** |
| FE-fosfat vs. P-fosfat | +0,33 | [−0,02; +0,61] | 0,061 |

## P-fosfat: brug den som positiv kontrol

> *"P-fosfat korrelerede signifikant negativt med kreatininclearance (ρ=−0,38, 95 % CI −0,65 til −0,04, p=0,031), i overensstemmelse med litteraturen. Da dette er en veletableret sammenhæng ved CKD, fungerer den som positiv kontrol og understøtter, at datasættet kan detektere reelle fysiologiske sammenhænge."*

**Det er et vigtigt argument:** det viser, at dine nulfund ikke skyldes, at datasættet er ubrugeligt.

## FE-fosfat: attenuering — og et vigtigt begrebsmæssigt hul

Dit argument er, at lav clearance-spredning attenuerer korrelationen. **Det holder, og her er tallene:**

| | Antal |
|---|---|
| CrCl < 15 ml/min | **3** |
| CrCl 15–32 ml/min | **27** (84 %) |
| CrCl > 32 ml/min | **2** |

SD = 8,21 ml/min. **84 % af kohorten i et bånd på 17 ml/min.**

Korrigeret for range restriction (Pearson r = −0,32):

| Hvis SD havde været | Korrigeret r | p |
|---|---|---|
| 8,2 (faktisk) | −0,32 | 0,076 |
| 10 | −0,38 | **0,033** |
| **12** | **−0,44** | **0,012** |
| 14 | −0,50 | 0,004 |

⚠️ **Men vær præcis om terminologien** — her er der en vigtig skelnen, som en censor kan udfordre dig på:

| Fænomen | Hvad det er | Effekt |
|---|---|---|
| **Range restriction** | For lille spredning i x | Attenuerer |
| **Måleusikkerhed** | Støj i x eller y | Attenuerer |

**Du skriver "lav clearance kan attenuere korrelationen" — det er upræcist.** Det er ikke *lav* clearance, det er *lille spredning* i clearance. Sig:

> *"Kreatininclearance havde begrænset spredning: 84 % af kohorten lå mellem 15 og 32 ml/min (SD 8,2). Range restriction attenuerer korrelationer, og korrigeret for dette ville en spredning på 12 ml/min svare til r ≈ −0,44 (p≈0,01). Konfidensintervallet [−0,49; +0,19] er desuden bredt og foreneligt med både en moderat negativ sammenhæng og ingen sammenhæng — fundet er uinformativt snarere end negativt."*

Og tilføj **rekrutteringsargumentet**, som er reelt og godt:

> *"Prædialytisk stadie 5 er et smalt rekrutteringsvindue, da patienterne påbegynder dialyse. Det er en strukturel designbegrænsning."*

## ⚠️ Vær forsigtig med FE-fosfat på en anden måde

FE-fosfat bruger $U_{fosfat} \times P_{krea} / (P_{fosfat} \times U_{krea})$ — og CrCl bruger $U_{krea}/P_{krea}$. **De deler både U-kreatinin og P-kreatinin**, men i modsatte positioner. Hvis nogen spørger, om det er problematisk: nej, FE er volumen-uafhængig (samme argument som U-Na/U-krea), men **nævn ikke** at den skulle være "immun over for alt" — det er den ikke, fordi CrCl-aksen stadig påvirkes af opsamlingen.

Hold det simpelt: *"FE er beregnet af forhold inden for samme prøve og er derfor uafhængig af opsamlingens komplethed på udfaldssiden."*

---

# 5️⃣ Calcium — din fortolkning skal justeres

**Dine tal:** ingen korrelation mellem balance/ratio og clearance. Mann-Whitney viser trend mod lavere balance ved lavere clearance, ingen forskel i ratio.

**Din fortolkning:** *"når nyrerne er ødelagt nok er det indtaget der styrer balancen og ikke udskillelsen."*

## ⚠️ Her er problemet

Din urin-calcium er **median 35 mg/døgn** mod et indtag på ~753 mg. **Udskillelsen er kun ~5 % af indtaget.**

Det betyder, at calciumbalancen $I - E$ **matematisk er næsten identisk med indtaget** — uanset nyrefunktion. Der er ikke plads til, at udskillelsen kan styre noget.

**Så din fortolkning er rigtig i konklusionen, men forkert i begrundelsen.** Det er ikke, at nyrerne er "ødelagt nok" — det er, at renal udskillelse **aldrig** er den dominerende regulator for calcium. Calciumhomeostase styres primært af **intestinal absorption** (via kalcitriol) og **knogleomsætning**, ikke af urinudskillelse.

Og fordi urin-calcium er så lille, kan din balance **ikke** detektere ændringer i renal håndtering. Målet har ikke opløsningsevne til spørgsmålet.

**Den korrekte formulering:**

> *"Der var ingen sammenhæng mellem apparent calciumbalance eller -ratio og kreatininclearance. Urinudskillelsen af calcium udgjorde kun omkring 5 % af indtaget, hvorfor den apparente balance matematisk domineres af indtagsestimatet og har begrænset følsomhed over for ændringer i renal calciumhåndtering. Calciumhomeostasen reguleres desuden primært via intestinal absorption og knogleomsætning frem for renal udskillelse. Uden fæcesopsamling og uden markører for knogleomsætning kan studiet derfor ikke vurdere calciumbalancen meningsfuldt, og nulfundet afspejler snarere metodens begrænsning end fravær af forstyrret calciumhomeostase."*

**Det er et bedre svar, fordi du forklarer hvorfor målet ikke kunne virke** — i stedet for at fortolke et nulfund fysiologisk.

## Og husk vand-fundet — det er dit pæneste metodearbejde

Du observerede en konsistent bias (−138 mg), opstillede en hypotese (drikkevandets calciumindhold), testede den, og bekræftede den. **Det er god videnskabelig praksis, og du skal fremhæve det.** Men se punktet nedenfor om korrektionsfaktoren.

---

# 6️⃣ Bland-Altman: proportional bias — ✅ og du har helt ret

Jeg har testet det på to måder (Spearman og regression):

| | Fosforindtag | Natriumindtag |
|---|---|---|
| n | 30 | 30 |
| Bias (foto − vejet) | −39,1 mg | −194,1 mg |
| 95 % CI for bias | −135 til +57 | −471 til +83 |
| Wilcoxon (bias=0?) | p = 0,33 | p = 0,12 |
| 95 % limits of agreement | −543 til +465 | −1646 til +1258 |
| **Proportional bias, Spearman** | ρ = −0,05 (p=0,78) | ρ = +0,08 (p=0,67) |
| **Proportional bias, regression** | hældning +0,09 (p=0,66) | hældning +0,23 (p=0,19) |

**Proportional bias er ikke signifikant på nogen af dem — bekræftet med to metoder.**

## At du selv modsiger dig er en styrke, ikke en svaghed

Du skriver, at det modsiger dine argumenter i opgaven. **Sig det højt — det er præcis den slags selvkorrektion der belønnes:**

> *"I specialet argumenterede jeg for en niveauafhængig bias. Ved efterfølgende formel testning var den proportionale bias ikke signifikant for hverken fosfor (hældning +0,09, p=0,66) eller natrium (+0,23, p=0,19). Biasen er altså tilnærmelsesvis konstant på tværs af indtagsniveauer, og den formulering i specialet var upræcis."*

## Og det har en konkret positiv konsekvens

En **konstant** bias kan korrigeres med et simpelt fradrag. En **proportional** bias kan ikke. Så dette fund understøtter faktisk din egen korrektionsfaktor-idé fra calciumafsnittet:

> *"At biasen er konstant snarere end proportional betyder, at en simpel additiv korrektion i princippet er anvendelig — hvilket understøtter den korrektionsfaktor jeg foreslog for calcium fra drikkevand."*

⚠️ **Men to forbehold du skal nævne selv:**

1. Med n=30 har testen **begrænset styrke** til at udelukke en moderat proportional bias. Konfidensintervallet for natriums hældning [−0,12; +0,57] rummer stadig en betydelig positiv hældning. Sig: *"ikke-signifikant er ikke det samme som fraværende."*

2. For natrium er der en **antydning af heteroskedasticitet** (ρ mellem |difference| og middelværdi = 0,353, p = 0,056) — altså at uenigheden mellem metoderne bliver større ved højere indtag, selvom retningen er konstant. Det er værd at nævne, hvis nogen spørger.

## Hovedbudskabet fra Bland-Altman

| | Fortolkning |
|---|---|
| Bias −39 mg for fosfor (−3,8 %) | **Lille og ikke signifikant** — metoden er brugbar på gruppeniveau |
| Limits of agreement ±500 mg | **Brede** — ikke brugbar på individniveau |

> *"Fotometoden viste lille og ikke-signifikant bias for fosforindtag, men brede limits of agreement. Metoden er derfor anvendelig til gruppeniveau-estimater, men kan ikke erstatte vejet registrering til individuel kostvurdering."*

Og du kan tilføje en nuance, som løfter det:

> *"En del af uenigheden mellem metoderne afspejler formentlig reel dag-til-dag-variation i kosten snarere end metodefejl — den intra-individuelle variation var af samme størrelsesorden som limits of agreement."*

⚠️ Kun hvis metoderne dækkede **forskellige** dage. Hvis de dækkede samme dage, gælder argumentet ikke — tjek det.

---

# 🎤 Struktur: 10 minutter arbejde + 10 minutter highlights

Din vejleders opdeling er klog: første del er redegørende, anden del er analytisk. Det er også den rækkefølge, en bedømmelse følger.

## Del 1 — Arbejdet (10 min)

| Min | Indhold | Vigtigt |
|---|---|---|
| **0–1,5** | **Baggrund og formål** | CKD-MBD, hvorfor mineralbalance betyder noget, hvorfor stadie 4-5 er uudforsket |
| **1,5–2,5** | **Forskningsspørgsmål og hypoteser** | Formuler dem **helt** — sætningen på s. 10 er ufuldstændig i specialet |
| **2,5–6** | **Metode** | Design, population, de to kostmetoder, døgnurin, clearance. **Definér "apparent balance" eksplicit** |
| **6–8** | **Statistik** | Spearman, Mann-Whitney, Bland-Altman. **Primær = complete-case, sensitivitet = available-case, Wilcoxon som begrundelse** |
| **8–10** | **Hovedresultater** | Baseline, de tre mineraler, metodesammenligning. Tal og CI, ikke fortolkning endnu |

### Det ene slide du ikke må springe over

**"Hvad apparent balance er — og ikke er"**

> *"Uden fæcesopsamling måler jeg ikke balance, men differencen mellem estimeret indtag og renal udskillelse. Fækal udskillelse udgør en betydelig og ukendt del af mineralomsætningen, og den er aldrig undersøgt ved CKD stadie 4-5. 'Apparent balance' er derfor et estimat af renal håndtering relativt til indtag, ikke af nettoretention."*

**Sig det tidligt og eksplicit.** Det er den mest oplagte kritik af hele designet, og hvis du definerer begrebet præcist fra starten, er den afværget. Hvis du venter, virker det som en indrømmelse.

## Del 2 — Highlights (10 min)

Dette er hvor karakteren afgøres. Byg det som en **argumentation**, ikke en liste.

| Min | Indhold | Kernetal |
|---|---|---|
| **0–2,5** | **1. Balance og ratio måler forskellige ting** | Balance–indtag ρ=0,61 · Ratio–udskillelse ρ=0,82 · Ratio–indtag ρ=−0,02 |
| **2,5–6** | **2. Natriumfundet er sandsynligvis artefakt** | Fem argumenter, i den rækkefølge fra afsnit 2 |
| **6–7,5** | **3. Fosfat: hvad der holder og hvad der ikke gør** | P-fosfat ρ=−0,38 (positiv kontrol) · FE-fosfat CI [−0,49; +0,19] · range restriction |
| **7,5–8,5** | **4. Metodesammenligning revideret** | Bias −39 mg ns · proportional bias ns · brede LoA |
| **8,5–10** | **5. Reviderede konklusioner + klinisk relevans** | Gammel vs. ny formulering side om side |

### Slide-idé til punkt 1 — kryds-tabellen

Vis kun de fire tal:

|  | vs. INDTAG | vs. UDSKILLELSE |
|---|---|---|
| **Balance** | **0,61** | −0,31 |
| **Ratio** | −0,02 | **0,82** |

Ét slide, fire tal, én pointe. Det er det mest overbevisende slide du kan lave, fordi publikum ser mønstret selv.

### Slide-idé til punkt 5 — gammel vs. ny

| Skrev jeg | Bør stå |
|---|---|
| "sodium retention occurred below 20 ml/min" | "apparent sodium balance was significantly higher below 20 ml/min, consistent with — but not proof of — relative sodium retention" |
| "no real trend towards increasing retention" | "the study could neither confirm nor exclude clinically relevant phosphorus retention" |
| "forskellen skyldes alfacalcidol" | "kan ikke adskilles fra effekten af nyrefunktion (confounding by indication)" |
| "high but consistent bias" | "konstant, ikke-signifikant bias; proportional bias kunne ikke påvises" |

**Dette slide er guld.** Det demonstrerer, at du kan vurdere dit eget arbejde kritisk — hvilket er en eksplicit læringsmålsformulering på kandidatniveau.

---

# Styrker, svagheder, relevans — dine bedste punkter

## Styrker (nævn 4, ikke flere)

1. **Første studie af apparent mineralbalance ved prædialytisk CKD stadie 4-5** — reelt uudforsket område
2. **To parallelle kostmetoder** på samme deltagere — muliggør formel metodevalidering
3. **VEK-godkendt tillægsprotokol**, 50 rekrutterede, systematisk dataindsamling
4. **Kreatininclearance frem for eGFR** — direkte måling frem for estimat

## Svagheder (nævn 4, og sig dem selv)

1. **Ingen fæcesopsamling** → apparent, ikke reel balance
2. **Én døgnurin per deltager** → kan ikke estimere reliabilitet af udfaldsmålet
3. **Tilsat bordsalt ikke registreret** → natriumindtag systematisk underestimeret
4. **Begrænset clearance-spredning** (84 % inden for 17 ml/min) → range restriction

## Klinisk relevans — vær konkret

Du blev spurgt, hvad en diætist skal gøre anderledes. "Kan bruges på gruppeniveau" er ikke en anbefaling — diætister arbejder på individniveau. Her er tre konkrete:

1. **Fotometoden kan supplere, ikke erstatte.** Brugbar til gruppeniveau og som supplement ved restaurantbesøg eller dage hvor vejning er upraktisk. Ikke til individuel kostvurdering, fordi limits of agreement er ±500 mg for fosfor.

2. **Drikkevandets calciumindhold skal med i kostberegningen.** Det bidrog systematisk (−138 mg bias) og forsvandt når vand blev inkluderet. Og — vigtigere end en korrektionsfaktor — **spørg til væskeindtag som et separat spørgsmål.** Det er enklere og mere validt end at korrigere.

3. **Natriumindtag kan ikke vurderes på 3 dages registrering.** Within-person CV var 49 %. Brug døgnurin til natrium, eller flere dage — og registrér bordsalt separat.

## Hvad du ville gøre anderledes

| # | Ændring | Begrundelse |
|---|---|---|
| 1 | **Ratio (eller FE) som primært endpoint** | Balancen måler primært indtag (ρ=0,61) |
| 2 | **Flere døgnurinopsamlinger** | Muliggør reliabilitetsestimering af udfaldsmålet |
| 3 | **Registrere tilsat bordsalt** | De absolutte natriumtal er ikke fortolkelige uden |
| 4 | **Bredere rekruttering i clearance-spektret** | Undgå range restriction — men erkend at prædialytisk stadie 5 er et smalt vindue |
| 5 | **Fæcesopsamling i en delkohorte** | Ville gøre "balance" reel frem for apparent |

---

# Forventede spørgsmål — og dine svar

| Spørgsmål | Kernesvar |
|---|---|
| *"Hvorfor kalder du det balance uden fæces?"* | Jeg gør ikke — jeg definerer det som apparent balance. Fækal udskillelse er en ukendt størrelse ved CKD 4-5 og aldrig undersøgt. |
| *"Er sensitivitetsanalysen en efterrationalisering?"* | Nej. Primæranalysen var defineret på forhånd som complete-case. Fotometoden havde flere manglende dage, og et krav om 3 dage for begge metoder ville reducere n til 9. Jeg rapporterer begge analyser uanset resultat. |
| *"Din Wilcoxon viser ikke stabilitet"* | Korrekt — den viser fordelingsmæssig ækvivalens på gruppeniveau, ikke individuel stabilitet. ICC på 0,135 for natriumindtag viser, at den individuelle variation var betydelig. |
| *"Hvorfor tror du ikke på dit eget natriumfund?"* | Fem uafhængige argumenter, hvoraf det stærkeste er, at balancen i højclearance-gruppen var −930 mg/døgn, hvilket er fysiologisk umuligt. Og det volumen-uafhængige mål viser ingen forskel (p=0,40). |
| *"Kunne du ikke bare have brugt eGFR?"* | Kreatininclearance er en direkte måling frem for et estimat, og det var det metodiske valg i protokollen. Sammenligningen mellem målene er relevant for videre arbejde. |
| *"Hvad er dit vigtigste fund?"* | Metodologisk: at valg af endpoint afgør, hvad man måler — balance afspejler indtag, ratio afspejler renal håndtering. Klinisk: at fotometoden er anvendelig på gruppeniveau men ikke individuelt. |

---

# Til sidst

Din plan var god, og du har selv fundet det centrale analytiske punkt (balance vs. ratio) — det er stærkere end du selv formulerede det, fordi ratioen er **fuldstændig** uafhængig af indtaget (ρ = −0,02), ikke bare mindre afhængig.

**De to ting du skal huske:**

1. **Ret "signifikant forskel i udskillelse" til "trend (p=0,078)"** — brug korrelationen ρ=0,54 som dit stærke tal
2. **Calcium-fortolkningen** skal handle om, at udskillelsen kun er 5 % af indtaget, ikke om at nyrerne er "ødelagt nok"

Og den vending, der bærer hele dit oplæg:

> *"Mit vigtigste fund er ikke et enkelt resultat, men en erkendelse af, at valget af endpoint afgør, hvad man i realiteten måler. Balancen afspejler primært kostindtaget, ratioen afspejler den renale håndtering. Det er en forudsætning for at designe det næste studie korrekt."*

Held og lykke — du er godt forberedt.
