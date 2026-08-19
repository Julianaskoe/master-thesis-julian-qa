> **Verifikation:** `analysis/afklaring.py` → `analysis/outD.txt`

# Kort svar først: hvad du skal rapportere

**Du skal rapportere dit speciale som det er.** Alt det nye hører i oplægget som supplerende analyser. Jeg har lavet mange test, og det er min fejl at det er blevet uoverskueligt — her er den korte version:

| Analyse | Status | Hvor |
|---|---|---|
| Balance + ratio vs. **clearance**, primær + sensitivitet | **Uændret — det er dit speciale** | Specialet |
| Samme mod **eGFR og P-kreatinin** | Supplerende | Oplæg |
| **FE-fosfat** | Supplerende, dit bedste fund | Oplæg |
| Median i stedet for gennemsnit | Sensitivitetsanalyse, ikke primær | Oplæg, kort |

**Intet af det jeg har lavet gør dit speciale forkert.** Det tilføjer en ekstra fortolkningslag.

---

# 1. ⚠️ Jeg tog fejl om natrium og de flaggede — du havde ret

**Du spurgte:** *"hvis balance for natrium samt ratio faktisk bliver stærkere ved at fjerne de flaggede, kan jeg så konkludere det er dårlig opsamling? burde det ikke være modsat?"*

**Din intuition er rigtig, og jeg skrev det forkert.** Jeg har regnet efter:

| Analyse | Alle (n=32) | Uden flaggede (n=25) | Retning |
|---|---|---|---|
| **Na-balance vejet vs. CrCl** | −0,30 (p=0,10) | −0,26 (p=0,21) | **svagere** ✅ |
| **Na-balance vejet [median]** | −0,42 (p=0,019) | −0,40 (p=0,051) | svagere |
| **Na-balance foto vs. CrCl** | −0,35 (p=0,057) | −0,27 (p=0,21) | **svagere** ✅ |
| **Na-ratio vejet vs. CrCl** | +0,24 (p=0,19) | +0,19 (p=0,38) | **svagere** ✅ |
| **Na-ratio foto vs. CrCl** | +0,20 (p=0,28) | +0,08 (p=0,73) | **svagere** ✅ |
| U-natrium vs. CrCl | +0,54 (p=0,001) | +0,57 (p=0,003) | stærkere |
| U-Na/U-krea vs. CrCl | +0,28 (p=0,12) | +0,41 (p=0,042) | stærkere |

**Alle dine natriumbalance- og ratio-analyser bliver SVAGERE når de flaggede fjernes.** Det er præcis hvad opsamlingshypotesen forudsiger. I mit tidligere dokument skrev jeg at U-Na/U-krea blev stærkere og fremstillede det som om balancen også gjorde — det var sjusket af mig. **Undskyld, og godt du fangede det.**

## Men her er hvor din logik skal skærpes — og det er vigtigt

Du siger: *"burde det ikke være modsat?"* Du tænker sandsynligvis: *støj trækker korrelationer mod nul, så fjerner man støj bliver de stærkere.*

**Det gælder kun for uafhængig støj.** Ufuldstændig urinopsamling er ikke uafhængig støj — det er **delt fejl**, og den opfører sig omvendt.

### Jeg har simuleret det for at vise dig hvor stærkt effekten er

Jeg lavede 4000 simulerede datasæt med 32 personer, hvor der er **nul** sammenhæng mellem clearance og natriumudskillelse. Kun tilfældig ufuldstændig opsamling (k mellem 0,65 og 1,0), som rammer både urin-kreatinin og urin-natrium:

| | Resultat |
|---|---|
| Sand korrelation (indbygget) | **0,00** |
| Observeret median ρ | **+0,12** |
| 90 %-interval | −0,19 til +0,41 |
| Andel med p < 0,05 | **10 %** (skulle være 5 %) |

**Ren opsamlingsfejl producerer en positiv korrelation ud af ingenting.** Og til sammenligning: samme simulation for FE-fosfat, som er immun over for k, gav median ρ = **+0,005** — altså præcis nul, som det skal være.

### De to fejltyper, side om side

| | Uafhængig målestøj | Delt opsamlingsfejl |
|---|---|---|
| Eksempel | Dag-til-dag-variation i kosten | Glemt vandladning |
| Rammer | Én variabel ad gangen | **Begge variable samtidigt** |
| Effekt på ρ | Trækker **mod nul** | **Skaber** korrelation |
| Fjerner man den | ρ bliver **stærkere** | ρ bliver **svagere** |

**Så dit spørgsmål har et præcist svar:** ja, forsvinder korrelationen ved eksklusion, peger det mod delt fejl (opsamling). Bliver den stærkere, peger det mod uafhængig støj. **Og dine natriumbalance-analyser gør det første.**

## ⚠️ Men vær ærlig om ét forbehold

Da du fjerner de 7 flaggede, mister du også kohortens laveste clearance (9,49) og halverer <20-gruppen fra 8 til 4. Så en del af svækkelsen kan skyldes tabt spredning, ikke kun tabt artefakt.

**Formuleringen:**

> *"Ved eksklusion af deltagere med kreatinin-index under 10 mg/kg/døgn blev samtlige natriumbalance- og ratio-korrelationer svagere (fx balance vejet fra ρ=−0,30 til −0,26; ratio foto fra +0,20 til +0,08). Da ufuldstændig urinopsamling påvirker både kreatininclearance og natriumudskillelse i samme retning, er en svækkelse ved eksklusion netop hvad opsamlingsartefakt forudsiger. Eksklusionen reducerede dog samtidig spredningen i clearance, hvorfor tabet ikke entydigt kan tilskrives artefakt."*

---

# 2. Ændrer P-kreatinin din fortolkning af fosfatbalance og ratio?

**Ja — og det er faktisk gode nyheder.** Se her:

| Analyse | vs. CrCl (speciale) | vs. eGFR | vs. P-kreatinin |
|---|---|---|---|
| **P-balance vejet** | +0,09 (p=0,62) | **+0,46 (p=0,009)** | **−0,36 (p=0,044)** |
| P-balance foto | −0,12 (p=0,51) | +0,16 (p=0,38) | −0,19 (p=0,30) |
| **P-ratio vejet** | +0,19 (p=0,31) | **−0,43 (p=0,015)** | **+0,45 (p=0,012)** |
| P-ratio foto | +0,31 (p=0,087) | −0,22 (p=0,23) | +0,27 (p=0,14) |
| **FE-fosfat** | −0,17 (p=0,34) | **−0,51 (p=0,003)** | **+0,59 (p=0,0004)** |

## Hvad det betyder — dit nulfund var et måleproblem

Dit speciale konkluderer, at der ikke er sammenhæng mellem fosforbalance og clearance. **Mod eGFR er der en signifikant sammenhæng (ρ = 0,46, p = 0,009).**

Og bemærk at balance og ratio siger **det samme** fra hver sin side:

| | Retning mod eGFR | Fortolkning |
|---|---|---|
| Balance | **+0,46** | Lavere eGFR → lavere (mere negativ) balance |
| Ratio E/I | **−0,43** | Lavere eGFR → **højere** andel udskilt |

Begge peger på: **deltagere med dårligere nyrefunktion udskiller en større andel af det de spiser.** Det er kompensation, ikke retention.

Og FE-fosfat (ρ = −0,51 mod eGFR) bekræfter det med et mål, der ikke bruger kostregistrering overhovedet. **Tre uafhængige endpoints, samme konklusion.**

## Din nye fortolkning

**Gammel** (fra specialet):
> "No correlation was found between apparent phosphorus balance and creatinine clearance."

**Ny** (til oplægget):
> *"Ingen sammenhæng blev fundet mellem apparent fosforbalance og kreatininclearance. Ved supplerende analyse mod eGFR — som er uafhængigt af urinopsamlingens komplethed — var både balancen (ρ=0,46, p=0,009), ratioen (ρ=−0,43, p=0,015) og den fraktionelle fosfatudskillelse (ρ=−0,51, p=0,003) signifikant relateret til nyrefunktionen. Deltagere med lavere nyrefunktion udskilte en større andel af det indtagne fosfor, foreneligt med bevaret renal kompensation. Den manglende sammenhæng mod kreatininclearance skyldes formentlig, at clearance-variablen indeholder målestøj fra urinopsamlingen."*

**Det er en langt bedre konklusion.** Du går fra "vi fandt ingenting" til "vi fandt det, når vi brugte et bedre måleredskab — og her er hvorfor det første ikke virkede."

**Din vejleder bad dig bruge clearance, og det var ikke forkert** — det er standard, og det er det mest direkte mål. Men at du selv kan vise, hvad der sker med et alternativt mål, er netop den slags selvstændighed der belønnes.

---

# 3. Hvordan kan vi konkludere at P-kreatinin er "den rette"?

**Vi kan ikke, og det skal du ikke sige.** Det er et vigtigt spørgsmål, og jeg har været for kategorisk.

## Ingen af dine tre mål er sandheden

| Mål | Fejl fra urinopsamling | Fejl fra muskelmasse |
|---|---|---|
| **CrCl** | **JA — direkte** | nej |
| **eGFR** | nej | **JA — stor** |
| **P-kreatinin** | nej | **JA — stor** |

Sand GFR måles med iohexol eller inulin. Det har du ikke, og det har næsten ingen kliniske studier.

## Pointen er ikke at ét mål er sandt — det er at fejlene er uafhængige

Det er trianguleringsargumentet:

> Hvis to måleredskaber med **forskellige** fejlkilder giver samme svar, er det svært at forklare svaret med én af fejlkilderne. Så er den mest sandsynlige forklaring, at der er noget virkeligt.

**Det er sådan du skal formulere det:**

> *"Ingen af de anvendte nyrefunktionsmål er fri for bias. Kreatininclearance påvirkes af urinopsamlingens komplethed, mens eGFR og P-kreatinin påvirkes af muskelmasse. Fordi fejlkilderne er indbyrdes uafhængige, giver overensstemmelse mellem målene en stærkere fortolkning end noget enkelt mål alene. Fosfatfundene var signifikante mod begge urin-uafhængige mål, mens natriumfundene alene var signifikante mod kreatininclearance."*

## Og jeg har testet, om muskelmasse kan forklare fosfatfundet

Dette er vigtigt, for det er det åbenlyse modargument. Følg logikken:

1. Sarkopeni → mindre kreatininproduktion → **lav P-kreatinin** (ser ud som god nyrefunktion)
2. Sarkopeni → **lav U-kreatinin**
3. U-kreatinin står i FE's **nævner** → lav U-kreatinin giver **høj FE**

Så sarkopeni ville give: lav P-kreatinin **+** høj FE = en **negativ** korrelation.

**Du finder ρ = +0,59.** Muskelmasse-fejlen trækker altså **modsat** dit fund. At fundet alligevel er stærkt, gør det mere robust — ikke mindre.

> *"En mulig indvending er, at sarkopeni sænker både P-kreatinin og urin-kreatinin, hvilket via nævneren i FE-beregningen ville generere en negativ sammenhæng. Da den observerede sammenhæng er positiv, virker denne bias i modsat retning af fundet."*

**Det er et stærkt kort, og det er værd at have klar.**

---

# 4. Vejlederens hypotese — jeg har testet den, og den holder

**Du skriver:** *"min vejleder tror mere på fosfat balancen påvirkes end natrium ved lav funktion grundet ekstrem gode natrium mekanismer så måske kan det være et tegn på dårlig opsamling?"*

**Din vejleder har fysiologisk ret, og dine data bekræfter det præcist:**

| Udfald | vs. CrCl | vs. eGFR | vs. P-krea |
|---|---|---|---|
| **FE-fosfat** | −0,17 (0,34) | **−0,51 (0,003)** | **+0,59 (0,0004)** |
| **P-fosfat** | −0,38 (0,031) | **−0,68 (<0,0001)** | **+0,59 (0,0004)** |
| **P-ratio vejet** | +0,19 (0,31) | **−0,43 (0,015)** | **+0,45 (0,012)** |
| **P-balance vejet** | +0,09 (0,62) | **+0,46 (0,009)** | **−0,36 (0,044)** |
| U-natrium | **+0,54 (0,001)** | +0,09 (0,64) | +0,11 (0,55) |
| Na-balance vejet | −0,30 (0,10) | +0,18 (0,34) | −0,23 (0,22) |
| Na-ratio vejet | +0,24 (0,19) | −0,15 (0,41) | +0,17 (0,36) |

**Alle fire fosfatmål er signifikante mod de urin-uafhængige mål. Ingen af de tre natriummål er.**

Det er lige præcis mønstret, som vejlederens fysiologi forudsiger: fosfathomeostasen svigter tidligt i CKD (derfor sHPT og FGF23-stigning fra stadie 3), mens natriumbalancen holdes stram af RAAS/aldosteron indtil meget sent.

## Og din slutning er rigtig

Ja — når fysiologien forudsiger, at man **ikke** skal finde et stærkt natriumfund, og du finder et stærkt natriumfund udelukkende mod det mål der deler fejlkilde med udfaldet, **så peger både fysiologien og statistikken samme vej.**

> *"Fysiologisk forventes natriumbalancen bevaret indtil meget sent i CKD-forløbet på grund af den stramme RAAS- og aldosteronmedierede regulering, mens fosfathomeostasen svigter tidligere. Mine data følger dette mønster: samtlige fosfatmål var signifikant relateret til nyrefunktionen målt med opsamlings-uafhængige mål, hvorimod natriummålene alene var signifikante mod kreatininclearance. Både den fysiologiske forventning og den statistiske robusthedsanalyse peger derfor på, at natriumfundet med større sandsynlighed afspejler opsamlingsartefakt end reel retention."*

**At du kan koble fysiologi og metodekritik i samme argument er præcis kandidatniveau.** Det er stærkere end begge dele hver for sig.

---

# 5. ICC — du har fat i en reel begrænsning

**Du spurgte:** *"kan man godt bruge icc når vi ikke har udskillelse for 3 dage bliver det så ikke misvisende?"*

**Ja, det er en reel begrænsning, og du skal formulere det præcist.** ICC er beregnet på de 3 **kostdage**. Den siger derfor kun noget om **indtagsdelen**.

| Analyse | Bruger kostdata? | Gælder ICC? |
|---|---|---|
| U-natrium vs. clearance | nej | ❌ **irrelevant** |
| FE-fosfat vs. clearance | nej | ❌ **irrelevant** |
| Na-balance vs. clearance | ja, indtag + udskillelse | ✅ **delvis** |
| Na-ratio vs. clearance | ja, indtag + udskillelse | ✅ **delvis** |

## Hvor meget gælder den "delvis"?

Jeg har regnet variansbidragene:

| | Var(indtag) | Var(udskillelse) | Andel fra indtag |
|---|---|---|---|
| **Na, vejet** | 625.189 | **1.516.661** | **29 %** |
| Na, foto | 889.552 | 1.484.439 | 38 % |
| **P, vejet** | 71.269 | 55.377 | **56 %** |
| P, foto | 76.347 | 54.447 | 58 % |

**For natriumbalancen kommer kun 29 % af variansen fra indtaget.** Så ICC på 0,135 for natriumindtag rammer kun ~⅓ af problemet. Resten sidder i udskillelsen, som du kun har målt én gang og derfor **ikke** kan beregne ICC for.

## Så her er den ærlige og præcise formulering

> *"Intraklassekorrelationen er beregnet på de tre kostregistreringsdage og gælder derfor alene indtagsestimatet, ikke urinudskillelsen, som blev målt én gang per deltager. Da indtaget bidrog med 29 % af variansen i natriumbalancen og 56 % i fosforbalancen, kvantificerer ICC kun en del af den samlede måleusikkerhed. Reliabiliteten af enkeltdøgnsurin kunne ikke estimeres i dette design; litteraturen (Stremke et al. 2018) angiver, at én opsamling ikke opnår ≥75 % reliabilitet ved CKD. Den samlede usikkerhed er derfor større end ICC alene indikerer."*

**Bemærk hvad du får ud af det:** ICC underestimerer problemet. Det gør dit argument **stærkere**, ikke svagere.

## Og dit andet ICC-spørgsmål

**Du spurgte:** *"Når man kigger på den dårlige ICC for natrium burde et signifikant fund mod clearance så ikke vise ret meget?"*

**Rigtigt tænkt — men her er nuancen.** Med ICC = 0,135 er attenueringsfaktoren $\sqrt{0{,}135} = 0{,}37$. Så en observeret korrelation på 0,42 (din Na-balance median) ville svare til en sand korrelation på $0{,}42 / 0{,}37 = 1{,}14$ — **hvilket er matematisk umuligt** (korrelationer kan ikke overstige 1,0).

**Det er faktisk et selvstændigt argument:** hvis dit natriumfund var ægte biologi, kan det ikke være så stort som du måler, givet hvor upræcist du måler indtaget. Så en del af det **må** komme et andet sted fra — og delt opsamlingsfejl er den oplagte kandidat, fordi den kan *skabe* korrelation frem for at udviske den.

> *"Attenueringskorrektion giver et paradoks: med en reliabilitet på 0,135 ville den observerede korrelation på −0,42 implicere en sand korrelation over 1,0, hvilket er umuligt. Dette indikerer, at en del af den observerede sammenhæng ikke stammer fra en biologisk sammenhæng mellem de sande værdier, men fra korreleret målefejl — hvilket delt urinopsamlingsfejl netop er."*

⚠️ Brug det som et argument, ikke som et bevis — attenueringsformlen forudsætter ting, der ikke er helt opfyldt her.

---

# 6. Median vs. gennemsnit — du kunne have brugt median, men gør det ikke nu

**Du spurgte:** *"Men jeg kunne vel godt have brugt median for både vejet og foto alligevel?"*

**Ja, det ville have været metodisk fint** — og faktisk enklere at forklare end primær/sensitivitet-opdelingen. Men der er to grunde til ikke at skifte nu:

## a) Forskellen rammer kun få deltagere

Median og gennemsnit kan **kun** afvige for deltagere med 3 dage:

| Metode | 1 dag | 2 dage | **3 dage** |
|---|---|---|---|
| Fosfor vejet | 5 | 2 | **24** |
| Fosfor foto | 20 | 2 | **9** |
| Natrium vejet | 5 | 2 | **24** |
| Natrium foto | 19 | 1 | **11** |

For fotometoden har kun **9-11 deltagere** 3 dage. Så en "median-analyse" af fotodata er reelt identisk med gennemsnittet for 2/3 af kohorten. **Det er ikke en meningsfuld selvstændig analyse.**

## b) At skifte nu ser ud som fisketur

Median giver konsekvent lidt bedre p-værdier (fx Na-balance vejet: −0,30 → −0,42). **Hvis du skifter til median efter at have set det, er du i samme fælde som med Pearson.** En censor vil spørge hvorfor, og du har ikke et svar der ikke handler om p-værdien.

## Hvad du gør

Behold gennemsnit som primær. Rapportér median som **én linje**:

> *"Analyserne blev gentaget med medianen af registreringsdagene i stedet for gennemsnittet. Resultaterne var konsistente i retning og styrke."*

Og hvis du bliver spurgt om din primær/sensitivitet-struktur:

> *"Jeg anvendte Wilcoxons parrede test til at undersøge, om kostregistreringsdage uden samtidig urinopsamling kunne inddrages, og fandt ingen systematisk forskel mellem dagene (p=0,22 og p=0,80). Det begrundede en primæranalyse på samme-dags-data og en sensitivitetsanalyse med alle dage. Retrospektivt havde et gennemsnit eller en median af alle tilgængelige dage været en enklere og mere robust tilgang, da flere dage reducerer indflydelsen af enkeltdags-variation."*

**Det er et godt svar** — du forklarer dit valg, og du kan pege på en bedre løsning. Det viser refleksion.

⚠️ **En vigtig ting om din Wilcoxon-begrundelse:** testen viste, at **gruppens median** ikke flyttede sig mellem dagene. Den viste **ikke**, at de enkelte deltagere var stabile. Fire personer kan svinge ±1000 mg hver, og medianen står stille. Vær forberedt på det spørgsmål — og brug ICC-tallene som svar, for de måler netop den individuelle stabilitet (og den var lav for natrium).

---

# 7. Skal du fokusere på "indtaget dominerer balancen"?

**Kort svar: nej, ikke som hovedpointe. Jeg overdrev den, og tallene bakker den ikke op.**

Jeg påstod tidligere, at balancen ville korrelere >0,85 med indtaget. Sådan ser det faktisk ud:

| | Andel af varians fra indtag | ρ(balance, indtag) | ρ(balance, udskillelse) |
|---|---|---|---|
| **Na, vejet** | 29 % | **−0,05** | **−0,73** |
| Na, foto | 38 % | +0,14 | −0,71 |
| **P, vejet** | 56 % | **+0,61** | −0,31 |
| P, foto | 58 % | +0,55 | −0,48 |

**Jeg tog fejl.** For natrium er balancen praktisk taget uafhængig af indtaget (ρ = −0,05) og domineret af **udskillelsen** (ρ = −0,73). For fosfor bidrager begge.

**Hvorfor jeg tog fejl:** jeg regnede på IQR fra din baselinetabel, som var lavet på enkeltdage. Når du bruger gennemsnittet af 3 dage, udjævnes indtagsvariationen — SD falder fra ~600 til 267. **Dit design håndterede altså problemet bedre end jeg antog.**

## Men vend pointen om — så bliver den relevant

Det interessante er **natriumrækkerne**: balancen er 73 % drevet af udskillelsen. Og udskillelsen er præcis den komponent, der rammes af ufuldstændig opsamling.

**Det er det argument du skal bruge:**

> *"Fosforbalancen afspejlede både indtag (ρ=0,61) og udskillelse (ρ=−0,31), mens natriumbalancen praktisk taget udelukkende afspejlede udskillelsen (ρ=−0,73 mod udskillelse, ρ=−0,05 mod indtag). Natriumbalancen er derfor mere sårbar over for ufuldstændig urinopsamling end fosforbalancen, hvilket bidrager til at forklare, hvorfor netop natriumfundet ikke var robust over for skift af nyrefunktionsmål."*

**Det er en præcis, verificerbar pointe der understøtter din hovedhistorie.** Meget bedre end min oprindelige version.

## Og hvis nogen spørger, om balance og ratio er "det samme"

Nej, og du har begge, hvilket er en styrke:

| | Måler | Enhed | Følsom for |
|---|---|---|---|
| Balance $I-E$ | absolut mængde tilbageholdt | mg/døgn | begge komponenter |
| Ratio $E/I$ | **andel** udskilt | % | forholdet, ikke niveauet |

Ratio normaliserer for indtag. Derfor kan de svare forskelligt — og at de peger samme vej mod eGFR (+0,46 og −0,43) er en intern konsistenscheck.

---

# 8. SGLT2 — ✅ din fil er korrekt, min tidligere læsning var forkert

Jeg tællede direkte i CSV-filen:

| | Ja | Nej/blank |
|---|---|---|
| **SGLT2i** | **23** | **9** |
| Diuretika | 27 | 5 |

**Det matcher dit speciale præcist (23/9).** Mine tidligere tal (28/4 og 19/13) kom fra fejllæsning af skærmbilleder — filen har altid været rigtig. Beklager forvirringen.

Rækkerne uden SGLT2i: **1, 3, 5, 14, 18, 23, 25, 26, 29.**

Diuretika er 27/5, ikke 26/6 som specialet siger — tjek den ene deltager mod medicinlisten.

## Konsekvens for medicinanalyserne

Med 23 vs. 9 for SGLT2i er Mann-Whitney forsvarlig. Men **husk power:** med n=23 vs. 9 kan du kun finde meget store effekter, så nulfund er uinformative. Ram teksten:

> *"Subgruppeanalyser efter SGLT2-hæmmerbehandling (n=23 vs. 9) og diuretika (n=27 vs. 5) blev udført post hoc med Mann-Whitney U-test. Diuretika kunne ikke klassificeres efter stofgruppe, og med kun fem deltagere i referencegruppen rapporteres diuretika-analysen deskriptivt. Analyserne var eksplorative, ikke prædefinerede og ikke korrigeret for multiple sammenligninger."*

---

# Din samlede historie — 6 sætninger

Øv dig på at sige dette:

> **1.** Jeg undersøgte sammenhængen mellem apparent mineralbalance, udskillelses/indtags-ratio og kreatininclearance, og fandt ingen signifikante sammenhænge for fosfor og calcium, men en signifikant højere natriumbalance under 20 ml/min.
>
> **2.** Efter afleveringen erkendte jeg en metodisk trussel: kreatininclearance beregnes af samme urinopsamling som udskillelsen, så ufuldstændig opsamling påvirker begge variable i samme retning og kan skabe korrelation ud af ingenting.
>
> **3.** Jeg kvantificerede opsamlingskvaliteten med kreatinin-index: median 11,8 mg/kg/døgn, 22 % under 10, og andelen var højere ved lav clearance (50 % mod 13 %, p=0,047).
>
> **4.** Jeg gentog analyserne mod eGFR og P-kreatinin, som ikke bruger urinen. **Fosfatfundene blev signifikante** — balance ρ=0,46, ratio ρ=−0,43, fraktionel ekskretion ρ=−0,51, alle p<0,02. **Natriumfundene forsvandt** — alle p>0,2.
>
> **5.** Det stemmer med fysiologien: fosfathomeostasen svigter tidligt i CKD, mens natrium holdes stramt af RAAS. Og natriumbalancen var 73 % drevet af udskillelsen, altså mest sårbar over for opsamlingsfejl.
>
> **6.** Jeg reviderer derfor natriumkonklusionen til hypotesegenererende, og jeg kan i stedet rapportere et positivt fosfatfund: den fraktionelle fosfatudskillelse stiger med aftagende nyrefunktion, foreneligt med bevaret renal kompensation.

---

# Hvad du IKKE skal bruge

Jeg har lavet for meget. Læg disse væk:

| Analyse | Hvorfor ikke |
|---|---|
| Kruskal-Wallis over 4 medicinkombinationer | To grupper havde n=2 |
| Diuretika-p-værdier (p=0,009 osv.) | Kun 5 i referencegruppen — rapportér deskriptivt |
| U-P/U-krea-analyserne | Ingen signifikans nogen steder, tilføjer intet |
| Median som primæranalyse | Ser ud som fisketur |
| Range restriction-korrektionen | Kan nævnes i én sætning, ikke et slide |
| Fænotype-inddelingen | Kun hvis der er tid — det er "nice to have" |

---

# To-do, kort

| # | Opgave | Tid |
|---|---|---|
| **1** | Tjek GFR i **række 13** (din 25,76 vs. 18,40 af FE-data vs. eGFR 14) | 20 min |
| **2** | Tjek diuretika-optællingen (filen: 27, specialet: 26) | 10 min |
| **3** | Ret abstract/konklusion/perspektivering (de tre formuleringer) | 1 t |
| 4 | Slide: fosfat mod eGFR og P-kreatinin — dit positive fund | 45 min |
| 5 | Slide: kreatinin-index + hvorfor natrium ikke holder | 45 min |
| 6 | Slide: fysiologi + metode peger samme vej (vejlederens pointe) | 30 min |

---

**Til sidst:** du fangede min fejl om de flaggede, og du stillede det rigtige spørgsmål om ICC og om hvorfor P-kreatinin skulle være "den rette". Det er ikke en der er forvirret — det er en der læser kritisk. **Brug den evne til forsvaret; det er den der giver point.**
