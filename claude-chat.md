# Du skal være min censor, stil gerne nogl

**User - --**

Du skal være min censor, stil gerne nogle spørgsmål du undrer dig over! 

**Assistant - --**

**User - --**

Godt at du nævner det. Det er ikke en reel balance da der ikke var afførings opsamling. Det er jo en fuldstændig ukendt variabel!. måske man kan definere det som omskrevet indtag? Jokeren ved det er jo at når man aldrig har undersøgt stadie 4-5 ved vi reelt ikke hvor meget der forekommer i afføring om det ændrer sig? det kan måske forventes som calcium da det ser ud til at udskillelsen i urin falder så markant!.

**Assistant - --**

**User - --**

Jeg svarer også på resten. Hmm ufuldstændig urinopsamling? altså at der er manglet opsamlinger på 24 timers urinen???  måske, kan de "sygere" haft en mere utilstrækkelig urinopsamling?  en anden forklaring kan være at de positive fund jo er fundet grundet foto metoden i sig selv er ret upræcis? jeg tænker dog at natrium er lidt mere tricky da 24 timers urin ikke skulle være så repræsentabel. Normalt er det vel forventeligt at fosfor ophobning ses i større grad da natrium er ekstremt stramt reguleret af aldosterone? ellers skulle RAAS blive betydelig skadet når man nærmer sig stadie 5?. En anden forklaring kan være at ved natrium fjernes 90% af urinen så det er nemmere at etablere en "balance" end fosfor! vi ved jo reelt ikke om afførings udskillelsen også falder ved faldende GFR? Jeg tænker dog med de her resultater at fosfor ophobningen ikke skulle være SÅ betydelig hvis vi antager at udskillelsen i afføring er nogenlunde bevaret, fordi når vi kigger på korrelations differencen er den jo omkring 0 så hvis det var virkelig ekstremt ville man vel have set bare en lille tendens? ved ikke om det svarer på spørgsmål 2?. jeg svarer på resten men giv gerne feedback!

**Assistant - --**

# Censors feedback + fortsatte spørgsmål

## Feedback på dine svar indtil nu

**Svar 1 (apparent balance):** Godt og ærligt. Du gør præcis det, jeg gerne vil se — du skelner mellem hvad du *har målt* og hvad du *kalder det*. Og din pointe om, at fæcesudskillelsen ved stadie 4-5 er en genuint ukendt størrelse, er den rigtige. Men du svarer ikke på den skarpeste version af spørgsmålet, så lad mig stille den direkte:

> Din "balance difference" er $B = I - E$. I dit datasæt er medianindtaget af fosfor ~1081 mg med IQR 467–1654, mens urinudskillelsen er ~474 mg med et betydeligt smallere spænd. **Hvor stor en del af variansen i $B$ stammer fra $I$?** Hvis du plotter $B$ mod $I$, får du efter alt at dømme $\rho > 0{,}9$. I så fald tester din primære analyse i praksis "korrelerer fosforindtag med CrCl?" — hvilket du i øvrigt tester separat og finder $\rho = 0{,}23$ (ns). Med andre ord: er dine to primære analyser reelt den samme analyse?

Det er ikke en dødsdom — men det skal du kunne svare på, og det er argumentet for, hvorfor **ratio-målet** (som normaliserer for indtag) faktisk er det mere informative endpoint, og hvorfor du burde have prioriteret det.

**Svar 2 (urinopsamling):** Du er inde på det rigtige spor ("de sygere kan have opsamlet dårligere"), men du får ikke fat i det centrale problem, som ikke er *støj* — det er **matematisk kobling**. Det uddyber jeg nedenfor, for det er efter min vurdering specialets alvorligste ubehandlede trussel.

**Din natrium-fysiologi:** God intuition om RAAS og om at ~90 % af Na udskilles renalt. Men du overser noget i dine egne tal, som jeg synes er vigtigere. Det kommer under punkt 2 nedenfor.

---

## 2. (skærpet) Kan begge dine "positive" fund være samme artefakt?

Din creatininclearance er beregnet som

$$\text{CrCl} = \frac{U_{Cr} \times V}{P_{Cr} \times 1440}$$

Antag at en deltager kun får opsamlet en andel $k < 1$ af døgnurinen (glemt vandladning, spildt portion). Så gælder:

- Al målt døgnudskillelse skaleres: $E_{målt} = k \cdot E_{sand}$
- Men **CrCl skaleres med præcis samme $k$**, fordi $U_{Cr} \times V$ indgår i tælleren.

Konsekvenserne:

| Endpoint | Effekt af undersopsamling ($k \downarrow$) | Forventet artefakt-korrelation | Dit fund |
|---|---|---|---|
| Balance $I - kE$ | stiger (mere "positiv") | **negativ** vs. CrCl | Natrium: $\rho = -0{,}47$, $p=0{,}008$ |
| Ratio $kE/I$ | falder | **positiv** vs. CrCl | Fosfor: $\rho = 0{,}31$, $p=0{,}087$ |

Begge dine ikke-nul-fund har altså **nøjagtig den signatur, som ufuldstændig urinopsamling ville producere** — og de er de eneste to fund, der peger væk fra nul. Det er ikke bevis for artefakt, men det er en konkurrerende forklaring, som du ikke afviser i specialet.

**Spørgsmål 2a:** Kan du validere opsamlingerne? Du har $U_{Cr}$ og vægt. Forventet døgnudskillelse er ca. $0{,}15\text{–}0{,}20$ mmol/kg/døgn hos ældre. Din median er 8,4 mmol/døgn ved en medianvægt på 77 kg $\approx 0{,}11$ mmol/kg/døgn. Det er i den lave ende — forklarligt ved høj alder og sarkopeni, men også foreneligt med systematisk undersopsamling. **Har du set på fordelingen?** Hvor mange ligger under fx 0,08 mmol/kg/døgn?

**Spørgsmål 2b:** Hvad sker der med natriumfundet, hvis du (i) ekskluderer de mest usandsynlige opsamlinger, eller (ii) plotter balancen mod urinvolumen?

**Spørgsmål 2c — og det her er den, jeg helst vil have dig til at tage stilling til:** I gruppen med CrCl $\geq 20$ ml/min er din natriumbalance **−930 mg/døgn** (foto) og **−554 mg/døgn** (WFR). At udskille ~1 g natrium mere, end man indtager, er **fysiologisk umuligt i steady state**. Det fortæller os, at intaget er systematisk underestimeret — hvilket du selv har designet ind i studiet ved ikke at lade deltagerne registrere tilsat bordsalt. Det betyder:

- De absolutte balancetal er ikke fortolkelige.
- Kun **forskellen mellem grupperne** kan fortolkes — og kun hvis under-rapporteringen er ens i de to grupper.
- Dit abstract og din konklusion siger "sodium retention occurred below 20 ml/min". Det er en **stærkere påstand, end dine data bærer**. En mere holdbar formulering: *"deltagere med CrCl <20 ml/min havde signifikant højere apparent natriumbalance, forenelig med — men ikke bevis for — relativ natriumretention."*

Vil du forsvare formuleringen i konklusionen, eller vil du moderere den?

---

## 3. Hvorfor ikke fraktionel fosfatekskretion?

Du har alle fire nødvendige variable. Fraktionel fosfatudskillelse:

$$FE_{Pi} = \frac{U_{Pi} \times P_{Cr}}{P_{Pi} \times U_{Cr}}$$

Bemærk: **volumen går ud**. Målet er immunt over for præcis det opsamlingsproblem, vi lige har diskuteret, det kræver ikke kostregistrering overhovedet, og det er det klassiske mål for netop den hypotese, du undersøger — "kompenserer de resterende nefroner?". Tilsvarende kunne du beregne TmP/GFR.

- Hvorfor er det ikke med?
- Hvis du beregnede $FE_{Pi}$ mod CrCl på dine data i aften — hvad ville du forvente? (Litteraturen ville forudsige en stejl invers sammenhæng, og hvis den *ikke* findes hos dig, er det et selvstændigt problem for datakvaliteten.)

---

## 4. Medicin som konfounder

81 % fik diuretika og 72 % SGLT2i. Det er ikke en detalje i et studie om natrium- og calciumudskillelse:

- **Thiazider** reducerer urin-calcium markant; **loop-diuretika** øger den. Du har 26 deltagere på diuretika og analyserer urin-calcium som endpoint — uden at skelne mellem typerne.
- **SGLT2-hæmmere** giver natriurese og er dokumenteret associeret med stigning i P-fosfat, FGF23 og PTH samt *fald* i fraktionel fosfatudskillelse. Med 72 % eksponering er det potentielt en hovedforklaring på flere af dine fosforresultater.

**Spørgsmål:** Du laver Mann-Whitney på alfacalcidol (n=9) — hvorfor ikke på diuretikatype og SGLT2i? Og hvordan påvirker det din fortolkning af alfacalcidol-fundet, at grupperne også adskilte sig signifikant på clearance ($p=0{,}03$)? Du nævner det selv, men konkluderer alligevel i resultatafsnittet, at forskellen skyldes alfacalcidol.

---

## 5. Statistisk styrke vs. klinisk relevans — din konklusion om fosfor

I "Future perspectives" skriver du, at den manglende korrelation *"suggest that there is no real trend towards an increasing retention as renal function declines."*

Det er en fortolkning af et nulfund som evidens for fravær af effekt. Overvej:

- Dine 95 % limits of agreement for fosfor mellem de to metoder alene var ca. **−500 til +350 mg/døgn**.
- En klinisk katastrofal fosforretention er i størrelsesordenen **50–150 mg/døgn** akkumuleret over år.
- **Dit måleinstrument har altså en usikkerhed, der er 3–10 gange større end det signal, du leder efter.**

**Spørgsmål:** Kan du angive konfidensintervallet for dine centrale $\rho$-værdier? Med $n = 30$ og $\rho = 0{,}02$ er 95 % CI ca. $[-0{,}34; 0{,}38]$ — altså foreneligt med alt fra moderat negativ til moderat positiv sammenhæng. Er "no real trend" så en holdbar formulering, eller bør den erstattes af "studiet kunne ikke udelukke klinisk relevant retention"?

---

## 6. Metodedelen — calcium og vand

Dit calciumfund er faktisk specialets pæneste metodologiske arbejde: du observerer en konsistent bias, opstiller en hypotese (vand), tester den (Wilcoxon på vandindtag), og bekræfter den (bias forsvinder når vand ekskluderes). Det er god videnskabelig håndværk.

Men konklusionen halter:

- Calcium fra drikkevand beregnede du fra **postnummer × vandhårdhed × 7,17 mg/L**, altså fra *volumen*, ikke fra billeder. Fejlen ligger dermed i, at deltagerne ikke fotograferede deres vandglas — ikke i portionsstørrelsesestimatet.
- Derfor: hvorfor foreslå en **korrektionsfaktor** (som antager, at under-rapporteringen er konstant på tværs af personer med vidt forskelligt væskeindtag), fremfor den langt simplere løsning — **at spørge til væskeindtag som et separat spørgsmål**, hvilket enhver klinisk diætist gør alligevel?
- Og: er en korrektionsfaktor på −138 mg validerbar i et andet postnummer med anden vandhårdhed?

---

## 7. Klinisk anvendelse

**Spørgsmål:** En diætist på et nefrologisk ambulatorium læser dit speciale i morgen. Hvad skal hun gøre anderledes?

Vær konkret. "Metoden kan bruges på gruppeniveau" er ikke en klinisk anbefaling — diætister arbejder per definition på individniveau. Hvis metoden ikke kan bruges individuelt til fosfor, protein og natrium, hvad er så dens plads? Du antyder selv svaret i sidste afsnit (supplement til WFR ved restaurantbesøg) — men det står ikke i konklusionen.

---

<details>
<summary><strong>Formalia og mindre uklarheder (klik for at se — bør rettes/kunne forklares)</strong></summary>

- **Forskningsspørgsmålet s. 10 er ufuldstændigt:** "Additionally Is there a correlation" — sætningen slutter midt i. Formuler det fulde spørgsmål mundtligt.
- **Tabelnummerering:** Calciumtabellen er mærket "Table 8", men teksten refererer til "table 7". Tabel 7 findes ikke.
- **"Figure xx"** i Bland-Altman-figuren for fosfor (s. 59).
- **Table 10:** "r=8153" (skal være 0,8153) og "r=50,89" (skal være 0,5089).
- **Inkonsistente n:** Abstract angiver n=22 i >20-gruppen, metodeafsnittet n=23, natriumafsnittet begge dele.
- **Inkonsistente $\rho$-værdier:** Calciumbalance-ratio angives som 0,20 i tabellen og 0,09 i teksten (og omvendt for intake−excretion). Hvilken er hvilken?
- **Abstract:** "a high but consistent bias (−138mg)" — "high" er ikke retvisende for 138 mg ud af ~750 mg; du mener formentlig "consistent".
- **Resumé:** "fosforr".
- **Figur 6, 7 og 9:** akserne er byttet om ift. konvention — eksponeringsvariablen (clearance) står på y-aksen.
- **Figur 6 og 7 billedtekst:** "Circular points represents circular points represents..." (dubleret tekst).
- **Figur 6:** teksten siger n=27+3=30, figurteksten til fig. 7 siger n=28+3=31 — men baseline siger kun 2 deltagere i stadie 5 (clearance), mens subgruppeafsnittet siger 3. Afklar.
- **Tabel 5:** kolonnen "N" for sensitivitetsanalysen indeholder "31 (467-1654)" — formentlig en forskudt celle.
- **Kilder:** Schober 2018a og 2018b er samme artikel; St-Jules 2017a og 2017b ligeledes. Ryd op i referencelisten.
- **Tabel 14:** rækkefølgen "[11] 37" er forvirrende — angiv n og % i den rækkefølge, noten lover.

</details>

---

## Til din forberedelse

De tre punkter, jeg vil vægte tungest til eksamen, er: **(a)** koblingen mellem urinopsamling, CrCl og dine to signifikante fund; **(b)** at balance-differencen næsten udelukkende afspejler indtagsvariansen; og **(c)** afstanden mellem dine data og formuleringerne i konklusion/abstract.

Du har allerede erkendt en stor del af det i diskussionen — det er specialets styrke. Det, der mangler, er, at samme forbehold slår igennem i **abstract og konklusion**, som er det, folk læser.

Skriv gerne dine svar på 3–7 nedenfor, så vender jeg tilbage.

**User - --**

Så ikke fundet af differencen  skyldes ikke at de indtager mindre når GFR falder?. kan du forklare punkt 2 så det giver lidt mere mening.  forstår feks ikke "Al målt døgnudskillelse skaleres: E 
m 
a
˚
 lt
​
 =k⋅E 
sand
​
 
Men CrCl skaleres med præcis samme k, fordi U 
Cr
​
 ×V indgår i tælleren."  din tabel må du gerne forklare også. jeg forstår heller ikke "Kan du validere opsamlingerne? Du har U 
Cr
​
  og vægt. Forventet døgnudskillelse er ca. 0,15–0,20 mmol/kg/døgn hos ældre. Din median er 8,4 mmol/døgn ved en medianvægt på 77 kg ≈0,11 mmol/kg/døgn. Det er i den lave ende — forklarligt ved høj alder og sarkopeni, men også foreneligt med systematisk undersopsamling. Har du set på fordelingen? Hvor mange ligger under fx 0,08 mmol/kg/døgn?"  "Hvad sker der med natriumfundet, hvis du (i) ekskluderer de mest usandsynlige opsamlinger, eller (ii) plotter balancen mod urinvolumen?" hvordan gør jeg det? "Spørgsmål 2c — og det her er den, jeg helst vil have dig til at tage stilling til: I gruppen med CrCl ≥20 ml/min er din natriumbalance −930 mg/døgn (foto) og −554 mg/døgn (WFR). At udskille ~1 g natrium mere, end man indtager, er fysiologisk umuligt i steady state. Det fortæller os, at intaget er systematisk underestimeret — hvilket du selv har designet ind i studiet ved ikke at lade deltagerne registrere tilsat bordsalt. Det betyder:

De absolutte balancetal er ikke fortolkelige.
Kun forskellen mellem grupperne kan fortolkes — og kun hvis under-rapporteringen er ens i de to grupper.
Dit abstract og din konklusion siger "sodium retention occurred below 20 ml/min". Det er en stærkere påstand, end dine data bærer. En mere holdbar formulering: "deltagere med CrCl <20 ml/min havde signifikant højere apparent natriumbalance, forenelig med — men ikke bevis for — relativ natriumretention." tak for det! så jeg kan godt bruge forskellen mellem grupperne?. det her forstår jeg ikke "Du har alle fire nødvendige variable. Fraktionel fosfatudskillelse:

FE 
Pi
​
 = 
P 
Pi
​
 ×U 
Cr
​
 
U 
Pi
​
 ×P 
Cr
​
 
​
 

Bemærk: volumen går ud. Målet er immunt over for præcis det opsamlingsproblem, vi lige har diskuteret, det kræver ikke kostregistrering overhovedet, og det er det klassiske mål for netop den hypotese, du undersøger — "kompenserer de resterende nefroner?". Tilsvarende kunne du beregne TmP/GFR.

Hvorfor er det ikke med?
Hvis du beregnede FE 
Pi
​
  mod CrCl på dine data i aften — hvad ville du forvente? (Litteraturen ville forudsige en stejl invers sammenhæng, og hvis den ikke findes hos dig, er det et selvstændigt problem for datakvaliteten.)" kan jeg direkte beregne det uden at have indtag med? vil der ikke være højere udskillelse ved højere indtag eller er det ligemget?. 81 % fik diuretika og 72 % SGLT2i. Det er ikke en detalje i et studie om natrium- og calciumudskillelse:

Thiazider reducerer urin-calcium markant; loop-diuretika øger den. Du har 26 deltagere på diuretika og analyserer urin-calcium som endpoint — uden at skelne mellem typerne.
SGLT2-hæmmere giver natriurese og er dokumenteret associeret med stigning i P-fosfat, FGF23 og PTH samt fald i fraktionel fosfatudskillelse. Med 72 % eksponering er det potentielt en hovedforklaring på flere af dine fosforresultater.
Spørgsmål: Du laver Mann-Whitney på alfacalcidol (n=9) — hvorfor ikke på diuretikatype og SGLT2i? Og hvordan påvirker det din fortolkning af alfacalcidol-fundet, at grupperne også adskilte sig signifikant på clearance (p=0,03)? Du nævner det selv, men konkluderer alligevel i resultatafsnittet, at forskellen skyldes alfacalcidol. er det fint at skelne? fordi de får jo forskellige doser? hvad skal jeg så undersøge der? skal jeg bruge mann whitney? det her tror jeg heller ikke jeg forstår  "I "Future perspectives" skriver du, at den manglende korrelation "suggest that there is no real trend towards an increasing retention as renal function declines."

Det er en fortolkning af et nulfund som evidens for fravær af effekt. Overvej:

Dine 95 % limits of agreement for fosfor mellem de to metoder alene var ca. −500 til +350 mg/døgn.
En klinisk katastrofal fosforretention er i størrelsesordenen 50–150 mg/døgn akkumuleret over år.
Dit måleinstrument har altså en usikkerhed, der er 3–10 gange større end det signal, du leder efter.
Spørgsmål: Kan du angive konfidensintervallet for dine centrale ρ-værdier? Med n=30 og ρ=0,02 er 95 % CI ca. [−0,34;0,38] — altså foreneligt med alt fra moderat negativ til moderat positiv sammenhæng. Er "no real trend" så en holdbar formulering, eller bør den erstattes af "studiet kunne ikke udelukke klinisk relevant retention"?

" 

**Assistant - --**

# Uddybning af punkterne

---

## 1. Nej — nulfundet på differencen handler ikke primært om, at de spiser mindre

Du spørger, om det manglende fund på differencen skyldes, at indtaget falder, når GFR falder. Det er en anden (og rimelig) hypotese, som du selv diskuterer. Min pointe er en tredje ting, og den er mere grundlæggende:

Din balance er

$$B = I - E$$

Variansen i $B$ er

$$\mathrm{Var}(B) = \mathrm{Var}(I) + \mathrm{Var}(E) - 2\,\mathrm{Cov}(I,E)$$

I dine data er spredningen i **indtag** langt større end i **udskillelse**:

| | Median | Spænd/IQR |
|---|---|---|
| Fosforindtag (WFR) | 1081 mg | IQR 467–1654 (≈1200 mg) |
| U-fosfor | 474 mg | (range 911 mg, men IQR væsentligt smallere) |

Når $I$ svinger så meget mere end $E$, bliver $B$ i praksis **en let forskudt kopi af $I$**. Plot $B$ mod $I$ i Prism — du får sandsynligvis $\rho \approx 0{,}85\text{–}0{,}95$.

**Konsekvensen:** Når du tester "korrelerer $B$ med CrCl?", tester du reelt "korrelerer indtaget med CrCl?". Og det spørgsmål stiller du separat og besvarer med $\rho = 0{,}23$, $p = 0{,}16$ (ns). De to analyser er altså næsten samme analyse — derfor er det ikke overraskende, at begge er nul.

**Det er ikke en fejl, men en fortolkningsbegrænsning du skal kunne italesætte:**

> "Differencemålet domineres af variationen i indtaget og er derfor et dårligt mål for renal håndtering. Ratio-målet — og endnu bedre fraktionel ekskretion — normaliserer for indtag og er derfor de mere informative endpoints i denne sammenhæng."

Det er faktisk et argument *for* dit design (du havde ratio med), som du bare ikke har trukket frem.

---

## 2. Ufuldstændig urinopsamling — regnestykket forklaret trin for trin

### Hvad "$k$" er

Forestil dig en deltager, der reelt producerer 2000 ml urin på et døgn, men glemmer én vandladning og kun får opsamlet 1600 ml. Så er

$$k = \frac{1600}{2000} = 0{,}8$$

Det afgørende: **alt** i den glemte portion går tabt — både natrium, fosfat *og* kreatinin. Koncentrationen i det opsamlede er stadig korrekt, men den samlede mængde er 20 % for lav for **alle stoffer samtidig**.

$$E_{\text{målt}} = k \cdot E_{\text{sand}}$$

### Hvorfor CrCl rammes af præcis samme faktor

Din formel er

$$\mathrm{CrCl} = \frac{U_{Cr} \times V}{P_{Cr} \times 1440}$$

Læg mærke til, at tælleren $U_{Cr} \times V$ = koncentration × volumen = **den samlede mængde kreatinin, du har fået fat i**. Den er også kun 80 % af sandheden. $P_{Cr}$ (blodprøven) er upåvirket.

$$\mathrm{CrCl}_{\text{målt}} = k \cdot \mathrm{CrCl}_{\text{sand}}$$

**Så: én og samme fejl trækker både din eksponeringsvariabel (CrCl) og din udfaldsvariabel (E) ned med samme faktor.** Det er derfor, det er farligt — det er ikke tilfældig støj, det er en systematisk kobling, der skaber korrelation ud af ingenting.

### Regneeksempel

Tag en patient med **sand** CrCl = 30 ml/min, sandt natriumindtag 3000 mg, sand U-Na 3000 mg (perfekt balance = 0):

| Opsamlingsgrad | Målt CrCl | Målt U-Na | Målt balance $I-E$ | Målt ratio $E/I$ |
|---|---|---|---|---|
| $k = 1{,}0$ (perfekt) | 30 ml/min | 3000 mg | **0 mg** | 100 % |
| $k = 0{,}8$ | 24 ml/min | 2400 mg | **+600 mg** | 80 % |
| $k = 0{,}6$ | 18 ml/min | 1800 mg | **+1200 mg** | 60 % |

Patienten er *den samme* i alle tre rækker. Der er ingen sygdom, ingen retention, ingen fysiologi — kun dårlig opsamling. Men i dine analyser ville han se ud som en patient med **lav clearance og positiv natriumbalance**.

### Sådan læser du tabellen fra sidst

| Endpoint | Hvad sker der ved dårlig opsamling? | Hvilken korrelation med CrCl skaber det? | Dit faktiske fund |
|---|---|---|---|
| **Balance** $I - kE$ | $E$ falder ⇒ balance stiger (mere positiv). Samtidig falder CrCl. | Lav CrCl ↔ høj balance = **negativ** korrelation | Natrium: $\rho = -0{,}47$, $p = 0{,}008$ ✓ |
| **Ratio** $kE/I$ | $E$ falder ⇒ ratio falder. Samtidig falder CrCl. | Lav CrCl ↔ lav ratio = **positiv** korrelation | Fosfor: $\rho = +0{,}31$, $p = 0{,}087$ ✓ |

Fortegnene i kolonne 3 er **artefaktets forudsigelse**. Kolonne 4 er, hvad du fandt. De matcher — for begge dine ikke-nul-fund, mens alt andet i specialet ligger omkring nul.

Det *beviser* ikke, at fundene er artefakter. Men det er en konkurrerende forklaring med samme signatur, og den skal adresseres, ikke ignoreres.

> **Din egen forklaring holder også:** at "de sygere" opsamler dårligere er netop mekanismen. Sygere patienter → flere kognitive problemer, inkontinens, træthed → lavere $k$ → *både* lavere målt CrCl og lavere målt udskillelse. Du var altså på rette spor — du fik bare ikke set, at fejlen forplanter sig til begge akser.

---

## 3. Kreatinin-index: sådan validerer du opsamlingerne

Kreatinin udskilles i en nogenlunde **konstant mængde pr. døgn** hos den enkelte (det er hele forudsætningen for at bruge det som markør). Mængden afhænger primært af muskelmasse. Derfor kan man estimere, hvad en person *burde* udskille, og sammenligne med det målte.

**Tommelfingerværdier (voksne):**

| | mg/kg/døgn | mmol/kg/døgn |
|---|---|---|
| Mænd | 20–25 | 0,18–0,22 |
| Kvinder | 15–20 | 0,13–0,18 |
| Ældre (>70 år) | ca. 10–20 % lavere | ca. 0,12–0,18 |

(Omregning: molvægt kreatinin = 113 g/mol, så 20 mg/kg ÷ 113 = 0,177 mmol/kg.)

**Dine tal:** median U-kreatinin 8,4 mmol/døgn, medianvægt 77 kg:

$$\frac{8{,}4}{77} = 0{,}109 \text{ mmol/kg/døgn} \approx 12{,}3 \text{ mg/kg/døgn}$$

Det ligger **under** forventet, også for en 75-årig population. Der er to plausible forklaringer, og du kan ikke skelne dem uden at kigge på fordelingen:

1. **Ægte sarkopeni** — realistisk hos ældre CKD 4-5 med proteinenergi-wasting (du citerer selv ESPEN: 20–40 %). Så er tallet korrekt og bare lavt.
2. **Systematisk undersopsamling** — så er tallet forkert.

**Det du skal gøre:** beregn $U_{Cr}/\text{vægt}$ for hver enkelt deltager og se på spredningen. Pointen er ikke medianen — det er **halen**. Hvis 4–5 deltagere ligger på 0,05–0,07 mmol/kg/døgn, er de næsten sikkert ufuldstændige opsamlinger, uanset hvor sarkopene de er. Og hvis netop de deltagere sidder i din <20 ml/min-gruppe (n=8), står natriumfundet på svag grund.

---

<details>
<summary><strong>4. Konkret opskrift på sensitivitetsanalyserne (klik)</strong></summary>

### (i) Kreatinin-index og eksklusion

**I Excel:**

1. Ny kolonne: `Kreatinin-index = U_kreatinin (mmol/døgn) / vægt (kg)`
2. Ny kolonne: `Køn` (du har den)
3. Sortér stigende. Lav et histogram (Indsæt → Diagram → Histogram) eller bare et prikplot i Prism.
4. Rapportér: median, IQR, min, max, og **antal under 0,10 og under 0,08 mmol/kg/døgn**.

**Så gentager du dine to nøgleanalyser uden de flaggede:**

- Mann-Whitney på natriumbalance (<20 vs. ≥20 ml/min)
- Spearman: fosfor-ratio vs. CrCl

Rapportér begge sæt tal side om side i en lille tabel. Hvis $p$ for natrium går fra 0,008 til fx 0,04 og retningen holder — så er fundet nogenlunde robust, og du kan sige det. Hvis det forsvinder — så har du lært noget vigtigt, og det er en helt legitim (og stærk) ting at rapportere.

### (ii) Balance mod urinvolumen

Simpelt Spearman-plot i Prism:

- x-akse: urinvolumen (ml/døgn)
- y-akse: natriumbalance (mg/døgn)

**Fortolkning:** Hvis der er en **stærk negativ** korrelation (lille volumen → høj positiv balance), er det et rødt flag for opsamlingsproblemer. En vis negativ sammenhæng er dog forventelig af fysiologiske grunde også, så det er ikke afgørende alene — men det hører med i billedet.

### (iii) Den analyse jeg helst vil se — og som du mangler

Rapportér **U-Na alene mod CrCl** (Spearman), og **Na-indtag alene mod CrCl** (Spearman).

Hvorfor: din balance er $I - E$. Hvis $I$ ikke hænger sammen med CrCl (test det!), så drives hele dit balancefund af $E$. Så er den ærlige og gennemsigtige formulering:

> "Natriumudskillelsen faldt med faldende clearance ($\rho = ?$), mens det estimerede indtag var uafhængigt af clearance ($\rho = ?$). Dette forklarer den observerede sammenhæng mellem balance og clearance."

Det er meget nemmere at forsvare end et sammensat mål — og det gør det også helt eksplicit, hvor artefaktrisikoen ligger.

</details>

---

## 5. Ja, du kan bruge gruppeforskellen — men kend biasretningen

Kort svar: **ja**, gruppesammenligningen er mere robust end de absolutte tal, fordi den systematiske underrapportering (manglende bordsalt) i princippet rammer begge grupper.

Men "i princippet" er forudsætningen, og den er værd at problematisere — også fordi begge de oplagte differentielle bias trækker **samme vej som dit fund**:

| Mulig differentiel bias | Effekt på <20-gruppen | Retning ift. dit fund |
|---|---|---|
| Patienter tættere på dialyse har oftere fået diætvejledning → salter mindre ved bordet → deres målte indtag er tættere på sandheden | Målt $I$ relativt **højere** ⇒ balance mere positiv | **Forstærker** fundet kunstigt |
| Sygere patienter opsamler urin mindre komplet | Målt $E$ **lavere** ⇒ balance mere positiv | **Forstærker** fundet kunstigt |

Det betyder ikke, at fundet er falsk. Det betyder, at du skal sige:

> "Gruppeforskellen er retningsmæssigt konsistent på tværs af begge kostmetoder, hvilket taler for reel signal. Men to potentielle differentielle bias — forskellig grad af tilsat salt og forskellig opsamlingskomplethed — trækker begge samme vej som fundet og kan ikke udelukkes med dette design. Fundet bør derfor betragtes som hypotesegenererende."

Og så retter du abstract og konklusion til den formulering, jeg foreslog sidst. **Det er den vigtigste enkeltrettelse i hele specialet**, fordi det er den ene sætning, alle læser.

---

## 6. Fraktionel fosfatekskretion — hvad det er, og hvorfor volumen forsvinder

### Udledningen

$FE_{Pi}$ betyder: *hvor stor en andel af det fosfat, nyren filtrerer, ender i urinen?* Det er per definition forholdet mellem fosfats clearance og GFR:

$$FE_{Pi} = \frac{C_{Pi}}{C_{Cr}} = \frac{\dfrac{U_{Pi} \times V}{P_{Pi}}}{\dfrac{U_{Cr} \times V}{P_{Cr}}}$$

$V$ står i både tæller og nævner og **går ud**:

$$FE_{Pi} = \frac{U_{Pi} \times P_{Cr}}{P_{Pi} \times U_{Cr}} \times 100\%$$

**Derfor er målet immunt over for opsamlingsproblemet fra punkt 2:** hvis du kun får 80 % af urinen, er både $U_{Pi}$ og $U_{Cr}$ 80 % for lave, og forholdet er uændret. (Du kan endda bruge totalmængderne i mmol/døgn direkte, det giver samme resultat — også her går $V$ ud.)

Du har alle fire variable i din tabel: P-fosfat, P-kreatinin, U-fosfor, U-kreatinin. **Det er ét regneark og ét Spearman-plot.**

### Dit spørgsmål: "Kan jeg beregne det uden indtag? Betyder indtaget ikke noget?"

Godt spørgsmål, og svaret er nuanceret:

**Ja, du kan beregne det uden indtag.** $FE_{Pi}$ er et rent tubulært håndteringsmål — det siger noget om nyrens *adfærd*, ikke om kostens indhold.

**Og ja, indtaget påvirker det.** Højt fosfatindtag → FGF23/PTH stiger → NaPi-IIa/IIc nedreguleres → $FE_{Pi}$ stiger. Det er præcis den mekanisme, du beskriver i baggrunden.

**Men størrelsesordenerne er ikke sammenlignelige.** Ved faldende GFR skal hver tilbageværende nefron udskille mere for at holde balancen. Groft sagt:

| GFR | Typisk $FE_{Pi}$ |
|---|---|
| Normal (>90) | 10–20 % |
| CKD 3 | 25–40 % |
| CKD 4 | 40–70 % |
| CKD 5 | 60–90 % |

Det er en 4–6-dobling drevet af nefrontab. Kostvariation flytter typisk $FE_{Pi}$ med nogle få til ~10 procentpoint. **GFR-effekten dominerer klart** — derfor forventes en stejl invers sammenhæng mellem $FE_{Pi}$ og CrCl.

Og hvis du vil have kosten med, kan du gøre det eksplicit: rapportér $FE_{Pi}$ vs. CrCl, og *derefter* $FE_{Pi}$ vs. fosforindtag som en separat analyse. Hvis den første er stærk og den anden svag, har du selv demonstreret, at GFR dominerer.

### Hvad det giver dig fagligt

Din hypotese er: *"kompenserer de resterende nefroner ved at øge den fraktionelle fosforudskillelse?"* — du skriver det næsten ordret på s. 16 og igen i diskussionen. **$FE_{Pi}$ er det direkte mål for netop den hypotese.** Det er faktisk mere on-target end din balance.

Og hvis du finder en klar invers sammenhæng, har du to ting:
1. Et positivt, fortolkeligt fund til et speciale, der ellers primært rapporterer nulfund.
2. En **intern validering** af dine urindata — for hvis $FE_{Pi}$ *ikke* stiger med faldende GFR i en CKD 4-5-population, er der noget galt med målingerne, og det ville forklare, hvorfor alt andet ligger på nul.

> **Til eksamen:** Selv hvis du ikke når at regne det, skal du kunne sige: *"Jeg burde have rapporteret $FE_{Pi}$ og TmP/GFR. Det er volumen-uafhængigt, kostuafhængigt og adresserer kompensationshypotesen direkte. Det er den vigtigste analyse, jeg mangler."* Det er et stærkere svar end at forsvare, at den ikke er der.

*(TmP/GFR — det renale fosfattærskel — beregnes fra samme tal via Bijvoets nomogram og er endnu tættere på "hvor meget kan nyren holde på". Nævn det gerne i perspektiveringen.)*

---

## 7. Diuretika og SGLT2i — hvad du konkret skal gøre

### "Er det fint at skelne, når de får forskellige doser?"

Ja. Forskellige doser er en **begrænsning**, ikke en showstopper. Argumentet:

- Thiazider og loop-diuretika har **modsatrettede** effekter på urin-calcium (thiazid ↓, loop ↑). At slå dem sammen i én "diuretika"-kategori er ikke bare upræcist — det kan **udviske** en reel effekt, fordi de to trækker hver sin vej.
- Dosis-heterogenitet giver støj og reducerer styrke, men den skaber ikke falske fund. Det skubber dig mod type II, ikke type I.

### Konkret anbefaling

**Kod om til meningsfulde kategorier:**

| Gruppe | Eksempler | Forventet effekt på U-Ca |
|---|---|---|
| Loop | furosemid, bumetanid | ↑ |
| Thiazid/thiazidlignende | bendroflumethiazid, hydrochlorthiazid, indapamid | ↓↓ |
| MRA | spironolakton, eplerenon | (Na-relevant) |
| Ingen | — | reference |

**Test:**
- Kruskal-Wallis over ≥3 grupper, eller Mann-Whitney parvist hvis n tillader
- **U-calcium** som udfald for diuretikatype
- **$FE_{Pi}$, P-fosfat, PTH, U-Na, natriumbalance** som udfald for SGLT2i (ja/nej)

**Frame det korrekt:** eksplorativt, ikke-prædefineret, ikke korrigeret for multiple test, hypotesegenererende. Præcis som du allerede gør andre steder — du er god til det.

### Alfacalcidol-fundet — det skal omformuleres

Her er problemet skarpt:

- Alfacalcidol-gruppen: median clearance **19,6** ml/min
- Ikke-alfacalcidol: median clearance **25,7** ml/min
- $p = 0{,}03$

Det er **confounding by indication** i lærebogsform: man giver aktivt D-vitamin til dem med mest fremskreden sHPT, altså dem med lavest GFR. Og lav GFR er i sig selv den stærkeste determinant for lav U-calcium.

Med n=9 kan du ikke justere dig ud af det. Du kan ikke stratificere meningsfuldt, og en multivariabel model ville være overfittet.

**Du skriver i resultatafsnittet, at forskellen skyldes alfacalcidol. Det skal ændres til:**

> "Deltagere i alfacalcidolbehandling havde lavere 24-timers calciumudskillelse (24 vs. 42 mg, $p = 0{,}018$), men havde samtidig signifikant lavere creatininclearance (19,6 vs. 25,7 ml/min, $p = 0{,}03$). Da alfacalcidol netop ordineres ved mere fremskreden sygdom, kan effekten af behandlingen ikke adskilles fra effekten af nyrefunktionen i dette design."

Du skriver faktisk allerede noget i den retning i diskussionen — sørg for, at resultatafsnittet siger det samme.

---

## 8. Nulfund vs. "der er ingen effekt"

### Hvorfor det er en fejlslutning

$p > 0{,}05$ betyder: *"vi kunne ikke skelne det observerede fra nul"*. Det betyder **ikke** *"det er nul"*. Fravær af evidens ≠ evidens for fravær.

Du skriver i perspektiveringen: *"suggest that there is no real trend towards an increasing retention"*. Det er at konkludere det andet ud fra det første.

### Konfidensintervallet gør det konkret

Brug Fishers z-transformation:

$$z = \operatorname{arctanh}(r), \qquad SE = \frac{1}{\sqrt{n-3}}, \qquad \text{CI} = \tanh\left(z \pm 1{,}96 \cdot SE\right)$$

**Dine to centrale tal:**

| Fund | $r$ | $n$ | 95 % CI | Foreneligt med |
|---|---|---|---|---|
| Fosforbalance vs. CrCl (WFR) | 0,02 | 30 | $[-0{,}34;\ 0{,}38]$ | moderat negativ → moderat positiv |
| Fosfor-ratio vs. CrCl (foto) | 0,31 | 31 | $[-0{,}05;\ 0{,}60]$ | ingen effekt → **stærk** effekt |

Læg mærke til den nederste: dit "borderline" fund er foreneligt med **alt fra nul til en stærk sammenhæng**. Det er ikke et svagt fund — det er et *uinformativt* fund. Præcis det samme gælder nulfundet ovenover.

**Praktisk:** GraphPad Prism giver dig 95 % CI for Spearman r automatisk (afkryds "Compute confidence interval" i correlation-dialogen). Tilføj en CI-kolonne til tabel 5, 8, 10 og 11. Det tager en time og hæver niveauet markant.

### Måleusikkerhed: to argumenter, hvor det ene er stærkere

**Argument A (LoA):** dine limits of agreement mellem metoderne var ca. −500 til +350 mg/døgn for fosfor. Bemærk dog: det måler uenighed *mellem metoder*, ikke usikkerhed på balancen som sådan. Brug det som illustration, ikke som bevis.

**Argument B — det stærkere:** Din balance er beregnet fra **én døgnurin** og **én kostdag**. Dag-til-dag-variationen i fosforindtag har typisk CV ≈ 30 %, hvilket ved et indtag på ~1100 mg svarer til ±330 mg/døgn på tilfældig variation alene. Stremke et al. (2018), som du selv citerer, konkluderer netop, at **flere døgnurin-opsamlinger er nødvendige** for ≥75 % reliabilitet ved CKD.

En kronisk fosforretention af klinisk betydning akkumuleres derimod fra små daglige mængder over år. Signalet er altså langt mindre end støjen.

**Konklusion:** dit måleinstrument har ikke opløsningsevne til at afgøre spørgsmålet. Det er en fuldt legitim — og faktisk vigtig — konklusion.

**Omformuler til:**

> "Studiet fandt ingen sammenhæng mellem apparent fosforbalance og creatininclearance. Konfidensintervallerne er imidlertid brede og forenelige med både positive og negative sammenhænge, og den metodiske usikkerhed ved enkeltdags-estimater overstiger den daglige retention, der ville være klinisk relevant over tid. Studiet kan derfor hverken bekræfte eller udelukke klinisk relevant fosforretention ved CKD stadie 4-5."

Det er svagere som overskrift — men det er det, dine data understøtter, og censor vil belønne det.

---

## Prioriteret liste til de sidste dage

| # | Opgave | Tid | Udbytte |
|---|---|---|---|
| 1 | Ret abstract + konklusion: "sodium retention occurred" → "apparent sodium balance was significantly higher" | 30 min | Stort |
| 2 | Ret "no real trend" → "kunne ikke udelukke" | 15 min | Stort |
| 3 | Ret alfacalcidol-formuleringen i resultatafsnittet | 15 min | Stort |
| 4 | Beregn kreatinin-index, rapportér fordelingen + antal <0,10 mmol/kg | 1–2 t | Stort |
| 5 | Beregn $FE_{Pi}$ vs. CrCl | 2 t | Meget stort, hvis det virker |
| 6 | Tilføj 95 % CI til alle Spearman-tabeller | 1 t | Middel-stort |
| 7 | Rapportér U-Na vs. CrCl og Na-indtag vs. CrCl separat | 30 min | Middel |
| 8 | Sensitivitetsanalyse uden usandsynlige opsamlinger | 1 t | Middel |
| 9 | Formalia fra listen sidst (tabelnumre, "Figure xx", r=8153) | 1 t | Lille, men irriterende hvis det står |

Punkt 1–3 er rene tekstrettelser og bør ske uanset. Punkt 5 er den, der kan flytte specialet fra "grundigt nulfundsstudie" til "grundigt studie med et positivt fysiologisk fund".

Send endelig dine svar på 3–7, når du har dem — og skriv til, hvis noget af ovenstående stadig er uklart. Særligt punkt 2 og 6 er værd at have helt på plads inden forsvaret.

**User - --**

mange tak! kæmpe hjælp, jeg er jo lidt bange for enten at dumpe eller få en dårlig karakter! på punkt 1 det giver mening at med den enorme spredning  at det nærmere er B vs indtag.  da B i største grad rykkes af den store spredning i indtag?, okay  hvad menes med E 
m 
a
˚
 lt
​
 =k⋅E 
sand 
​
?. giver stor mening med punkt 2!  men vil alle balance mål så ikke blive påvirket??? og hvordan vil jeg adressere puntk 2? og ikke netop kun de to ?. GFR målt udfra clearance var alligevel som median 5 højere end eGFR er målingen så upræcis eller kan man ikke sige det? okay kan du forklare det med opskriften på sensitivtets analysen lidt lettere? og hvad menes med uden de flaggerede? okay så ift balance mod urin volumen? er det fordi lavere urin volume kan betyde ufuldstændig opsamling altså at det måske er derfor den positive balance er set?. . den her forstår jeg ikke "Rapportér U-Na alene mod CrCl (Spearman), og Na-indtag alene mod CrCl (Spearman).

Hvorfor: din balance er I−E. Hvis I ikke hænger sammen med CrCl (test det!), så drives hele dit balancefund af E. Så er den ærlige og gennemsigtige formulering:

"Natriumudskillelsen faldt med faldende clearance (ρ=?), mens det estimerede indtag var uafhængigt af clearance (ρ=?). Dette forklarer den observerede sammenhæng mellem balance og clearance."

Det er meget nemmere at forsvare end et sammensat mål — og det gør det også helt eksplicit, hvor artefaktrisikoen ligger." hvad hvvis jeg finder det er drevet af udskillese hvad betyder det så? "Og hvis du vil have kosten med, kan du gøre det eksplicit: rapportér FE 
Pi
​
  vs. CrCl, og derefter FE 
Pi
​
  vs. fosforindtag som en separat analyse. Hvis den første er stærk og den anden svag, har du selv demonstreret, at GFR dominerer. det forstår jeg heller ikke beregner man så ikke bare det samme hvis man siger FE vs crcl igen eller? så forklar lige den med diuretika og hvordan jeg tester for det lidt mre pædagogisk! den sidste nr 8 forstår jeg slet ikke det må du også gerne forklare lidt mere pædagogisk

**Assistant - --**

# Uddybninger — så pædagogisk jeg kan

Først en kort ærlig bemærkning om bekymringen: du har fået en tillægsprotokol godkendt hos VEK, rekrutteret 50 deltagere, gennemført to parallelle kostregistreringsmetoder og lavet en diskussion, hvor du selv finder de fleste svagheder. **Nulfund dumper man ikke på.** Det, der koster karakter, er at *overfortolke* — og det er ren tekstredigering, som du kan lave på en formiddag. Så brug energien der, ikke på at være nervøs.

Nu til spørgsmålene.

---

## 1. Ja — du har forstået det rigtigt

Kort bekræftelse: fordi spredningen i indtag er meget større end spredningen i udskillelse, "arver" $B = I - E$ næsten hele sin variation fra $I$. Så når du korrelerer $B$ med CrCl, korrelerer du i praksis *indtaget* med CrCl.

**Tjek det selv i Prism (5 minutter):** Spearman med `Fosforindtag` på x og `Fosforbalance` på y. Får du $\rho > 0{,}85$, har du tallet til at sige det højt til forsvaret.

---

## 2. Hvad $E_{\text{målt}} = k \cdot E_{\text{sand}}$ betyder

Det er bare symboler for tre ting:

| Symbol | Betyder | Eksempel |
|---|---|---|
| $E_{\text{sand}}$ | Hvor meget natrium personen **faktisk** udskilte på et døgn | 3000 mg |
| $k$ | Hvor **stor en andel** af urinen der blev opsamlet (0 til 1) | 0,8 (= 80 %) |
| $E_{\text{målt}}$ | Hvad du **måler** i laboratoriet | $0{,}8 \times 3000 = 2400$ mg |

Læst højt: *"Det du måler, er lig med opsamlingsandelen gange det sande."*

Og det centrale: **$k$ rammer alle stoffer i den samme urinprøve samtidigt.** Glemmer man én vandladning, mister man både natrium, fosfat *og* kreatinin — 20 % af hvert. Koncentrationerne (mmol/L) er stadig rigtige; det er totalmængderne (mmol/døgn), der bliver for lave.

Fordi kreatinin ryger med, falder din CrCl med samme 20 %. Det er hele problemet i én sætning: **fejlen sidder på begge akser i dit plot.**

---

## 3. "Bliver alle balance-mål så ikke påvirket?" — ja, og det er din bedste forsvarsstrategi

Fuldstændig rigtigt spørgsmål. Ja, artefaktet gælder principielt for alle tre mineraler. **Men det bider kun, hvis $E$ udgør en betydelig del af $I$** — for det er $E$, der skaleres.

Se dine egne medianer:

| Mineral | Indtag $I$ | Udskillelse $E$ | $E$ som andel af $I$ | Artefaktet forudsiger | Du fandt |
|---|---|---|---|---|---|
| **Natrium** | 2010 mg | 2191 mg | ~109 % | negativ korrelation | $\rho = -0{,}47$ ✓ |
| **Fosfor** | 1081 mg | 474 mg | ~44 % | negativ korrelation | $\rho = +0{,}02$ ✗ |
| **Calcium** | 753 mg | 35 mg | ~5 % | (for lille til at rykke noget) | $\rho = +0{,}09$ – |

Læg mærke til **fosforrækken**. Udskillelsen udgør 44 % af indtaget — rigeligt til, at et systematisk opsamlingsproblem burde have skabt en negativ korrelation. Den findes ikke ($\rho = 0{,}02$).

> **Det er dit modargument, og det er et godt et:** *"Hvis ufuldstændig opsamling drev mine resultater, ville fosforbalancen — hvor urinudskillelsen udgør ~44 % af indtaget — også vise en negativ sammenhæng med clearance. Den ligger på 0,02. Det taler imod, at opsamlingsartefakt er den dominerende forklaring på natriumfundet."*

Calcium kan du **ikke** bruge som kontrol (udskillelsen er så lille, at artefaktet ikke kan flytte balancen målbart) — sig det selv, før nogen spørger.

### Hvordan du adresserer punkt 2 generelt

Ikke som en analyse per fund, men som **ét afsnit i limitations** plus **én sensitivitetsanalyse**:

1. Beskriv mekanismen (2–3 sætninger: $k$ rammer både $E$ og CrCl, fordi $U_{Cr} \times V$ står i CrCl-tælleren).
2. Vis kreatinin-index-fordelingen som empirisk kvalitetskontrol.
3. Præsentér fosfor-nulfundet som internt kontrolargument (tabellen ovenfor).
4. Gentag natriumanalysen uden de mest usandsynlige opsamlinger.

Det er *én* samlet håndtering, ikke tre.

---

## 4. CrCl var 5 ml/min **højere** end eGFR — det er godt nyt for dig

Median CrCl 25 vs. median eGFR 20. Det er **forventeligt af to grunde**, som ikke har noget med upræcished at gøre:

| Grund | Effekt |
|---|---|
| **Tubulær sekretion:** kreatinin filtreres *og* udskilles aktivt i tubuli. Clearance af kreatinin overstiger derfor den ægte GFR — typisk 10–20 %, mere ved fremskreden CKD | CrCl > sand GFR |
| **BSA-indeksering:** eGFR angives per 1,73 m² legemsoverflade. Din CrCl er rå ml/min. Med medianvægt 77 kg og højde 172 cm er BSA ca. 1,9 m² — altså ~10 % højere end 1,73 | rå CrCl > indekseret eGFR |

Tilsammen forklarer det rigeligt de 5 ml/min.

**Og her er pointen, du skal bruge aktivt:** Havde opsamlingerne været systematisk 20 % ufuldstændige, ville CrCl være trukket 20 % *ned* og formentlig ligget **under** eGFR. At den ligger, hvor teorien forudsiger, er **empirisk evidens for, at opsamlingerne i gennemsnit var rimeligt komplette.**

Det er et rigtig godt svar at have parat. Det udelukker ikke, at *enkelte* deltagere har opsamlet dårligt (det er stadig værd at tjekke), men det fjerner mistanken om et gennemgående problem.

> ⚠️ **Men vær forberedt på én ting:** På s. 40 skriver du, at "eGFR kan overestimere nyrefunktionen sammenlignet med CrCl" (Lahiji et al.). Dine egne data viser det modsatte — CrCl er højest. Kan du forklare det? Svaret er, at Lahiji sammenligner eGFR-*ligninger* med målt clearance i en onkologisk population, mens den klassiske fysiologi (tubulær sekretion) trækker den anden vej. Hav den nuance klar, ellers ser det ud som en intern modsigelse.

---

<details>
<summary><strong>5. Sensitivitetsanalysen — trin for trin i Excel (klik)</strong></summary>

### Hvad "de flaggede" betyder

Ikke andet end: *de deltagere, du selv markerer som mistænkelige.* Du "flagger" (sætter et flag/mærke ved) dem, hvis kreatininudskillelse er så lav, at opsamlingen sandsynligvis er ufuldstændig. Ren bogholderi.

### Trin 1 — Byg kolonnen

I dit Excel-ark, hvor hver række er en deltager:

| A: ID | B: Vægt (kg) | C: U-krea (mmol/døgn) | D: Index | E: Flag |
|---|---|---|---|---|
| 101 | 77 | 8,4 | `=C2/B2` | `=IF(D2<0,10;"FLAG";"OK")` |

Kolonne D giver mmol/kg/døgn. Kolonne E sætter mærket automatisk.

### Trin 2 — Beskriv fordelingen

Beregn median, min, max for kolonne D, og tæl flagene:

```
=MEDIAN(D2:D33)
=MIN(D2:D33)
=MAX(D2:D33)
=COUNTIF(E2:E33;"FLAG")
```

Rapportér det i en sætning: *"Kreatinin-index var median 0,11 (range 0,0X–0,XX) mmol/kg/døgn; N deltagere lå under 0,10."*

### Trin 3 — Kør analysen to gange

**Version A (alle):** det du allerede har. Mann-Whitney på natriumbalance, <20 vs. ≥20 ml/min → $p = 0{,}008$ (foto).

**Version B (uden flag):** kopiér arket, slet de flaggede rækker, kør præcis samme test igen i Prism.

### Trin 4 — Stil dem op ved siden af hinanden

| Analyse | Alle (n=30) | Uden flaggede (n=?) |
|---|---|---|
| Na-balance <20 vs. ≥20, foto | $p = 0{,}008$ | $p = ?$ |
| Na-balance <20 vs. ≥20, WFR | $p = 0{,}018$ | $p = ?$ |

**Fortolkning:**
- Holder retningen og $p$ stadig < 0,05 → *"fundet er robust over for eksklusion af usandsynlige urinopsamlinger."* Stærkt.
- Forsvinder det → *"fundet var sensitivt over for opsamlingskvalitet og bør fortolkes med tilbageholdenhed."* Også stærkt — bare en anden konklusion.

Begge udfald gør specialet bedre. Der er ingen dårlig udgang af den analyse.

</details>

---

## 6. Balance mod urinvolumen — ja, men det er det svageste af argumenterne

Din tolkning er rigtig: lille urinvolumen **kan** betyde ufuldstændig opsamling → for lav målt $E$ → kunstigt positiv balance.

Men vær varsom, for lavt volumen har også helt legitime forklaringer:

- Væskerestriktion (almindeligt ved fremskreden CKD)
- Oliguri ved stadie 5
- Lavt væskeindtag hos ældre

Og modsat: ved CKD ses ofte *isosthenuri* med bevaret eller endda øget volumen på grund af nedsat koncentreringsevne.

**Derfor:** brug plottet som understøttende, aldrig som hovedargument. Kreatinin-index er langt bedre, fordi det korrigerer for kropsstørrelse og bygger på et stof, hvis døgnudskillelse faktisk *er* nogenlunde konstant. Vand er det ikke.

---

## 7. At skille balancen op i sine to dele

### Hvorfor

Din balance er $B = I - E$. Et signifikant fund på $B$ fortæller dig ikke, om det kom fra $I$ eller fra $E$. Så du laver to helt simple Spearman-analyser:

| Plot | x-akse | y-akse | Spørgsmål |
|---|---|---|---|
| 1 | CrCl | U-natrium (mg/døgn) | Udskiller de med lav clearance mindre natrium? |
| 2 | CrCl | Na-indtag (mg/døgn) | Spiser de med lav clearance mindre natrium? |

### Hvad de fire mulige udfald betyder

| Plot 1 (udskillelse) | Plot 2 (indtag) | Fortolkning |
|---|---|---|
| Signifikant ↓ | Ingen sammenhæng | **Renal**: fundet skyldes nedsat udskillelse. Fysiologisk meningsfuldt. |
| Ingen | Signifikant ↑ | **Kostbetinget**: de sygere spiser bare mere salt. Ikke retention. |
| Signifikant ↓ | Signifikant ↓ | Modsatrettede effekter — balancen er svær at fortolke. |
| Ingen | Ingen | Balancefundet er formentlig støj. |

### "Hvad hvis det er drevet af udskillelsen?"

Det er faktisk **det udfald du håber på** — for det er præcis din fysiologiske påstand: nyren kan ikke længere komme af med natriummet.

Men det er samtidig **præcis det sted, hvor artefaktet fra punkt 2 bor.** Både "ægte nedsat udskillelse" og "ufuldstændig opsamling" giver lavt $E$ hos deltagere med lav målt CrCl. De to kan ikke skelnes fra tallene alene.

Derfor er det ærlige svar en kombination:

> *"Sammenhængen mellem natriumbalance og clearance var drevet af faldende urinudskillelse ($\rho = ?$), mens indtaget var uafhængigt af clearance ($\rho = ?$). Dette er foreneligt med nedsat renal natriumudskillelse, men også med differentiel opsamlingskomplethed. Sidstnævnte kan ikke udelukkes, men støttes ikke af kreatinin-index-fordelingen, hvor N deltagere lå under grænseværdien."*

Det er den slags formulering, der giver point: du siger, hvad du tror, hvad alternativet er, og hvad du har gjort for at undersøge det.

---

## 8. $FE_{Pi}$ mod CrCl **og** mod indtag — det er to *forskellige* plots

Her tror jeg misforståelsen er, at du hører "to analyser" og tænker "samme regnestykke to gange". Det er det ikke. **Du beregner $FE_{Pi}$ én gang** — én kolonne i Excel, én værdi per deltager. Derefter plotter du den mod **to forskellige** x-variable:

| Analyse | y-akse | x-akse | Spørgsmål |
|---|---|---|---|
| A | $FE_{Pi}$ | CrCl (ml/min) | Stiger den fraktionelle udskillelse, når nyrefunktionen falder? |
| B | $FE_{Pi}$ | Fosforindtag (mg/døgn) | Stiger den fraktionelle udskillelse, når man spiser mere fosfor? |

Samme y-kolonne, forskellig x-kolonne. Analogi: du har målt folks blodtryk **én gang** — og plotter det derefter mod både alder og saltindtag. To spørgsmål, én måling.

### Hvorfor det er værd at gøre

Begge mekanismer *kan* hæve $FE_{Pi}$. Ved at plotte begge viser du, hvilken der dominerer:

- **A stærk, B svag** → nefrontabet driver kompensationen. Det er det forventede og det, litteraturen siger.
- **A svag, B stærk** → kosten dominerer, og din population er for homogen i GFR til at se GFR-effekten.

Det er en simpel måde at demonstrere, at du forstår, hvad der driver dine tal.

### Sådan beregner du den

Fire kolonner du allerede har: `U-fosfor`, `P-kreatinin`, `P-fosfat`, `U-kreatinin`.

$$FE_{Pi} = \frac{U_{Pi} \times P_{Cr}}{P_{Pi} \times U_{Cr}} \times 100$$

> ⚠️ **Enhedsfælde:** P-kreatinin er i **µmol/L**, U-kreatinin i **mmol/døgn**, U-fosfor i **mmol/døgn**, P-fosfat i **mmol/L**. Divider P-kreatinin med 1000 for at få mmol/L, ellers får du et resultat 1000× for stort. Sanity-check: dine værdier skal ende omkring **30–80 %** i en CKD 4-5-population. Får du 0,05 % eller 5000 %, er der en faktor 1000 på afveje.

Du kan bruge døgnmængder direkte (mmol/døgn) — volumen går ud uanset, netop fordi det står i både tæller og nævner.

---

<details>
<summary><strong>9. Diuretika — helt konkret hvad du gør (klik)</strong></summary>

### Problemet i én sætning

Du har 26 deltagere på "diuretika" i én kasse. Men **thiazider sænker** urin-calcium (de øger reabsorptionen i distale tubulus — det er derfor de bruges mod calciumsten), og **loop-diuretika øger** urin-calcium (de blokerer NKCC2 og dermed det lumen-positive potentiale, der driver paracellulær Ca-reabsorption i den tykke ascenderende del — som du selv beskriver på s. 14).

Slår du dem sammen, kan de to grupper **udligne hinanden**, og du ser ingenting, selv hvis effekten er der.

### Trin 1 — Lav en ny kolonne

Gå i medicinlisten og kod hver deltager:

| Kode | Præparater | Forventet effekt på U-Ca |
|---|---|---|
| `1 = Loop` | furosemid, bumetanid | ↑ |
| `2 = Thiazid` | bendroflumethiazid, hydrochlorthiazid, indapamid, metolazon | ↓↓ |
| `3 = MRA` | spironolakton, eplerenon | (mest natrium-relevant) |
| `4 = Ingen` | — | reference |

Deltagere på både loop og thiazid: lav en `5 = kombination`, eller ekskludér dem fra netop den analyse og skriv det.

### Trin 2 — Tæl først, test bagefter

Skriv gruppestørrelserne op, **før** du vælger test:

- Har du fx `Loop n=18`, `Thiazid n=6`, `Ingen n=6` → **Kruskal-Wallis** (Prism: Analyze → Column statistics → Kruskal-Wallis) med Dunn's post hoc.
- Har du kun to meningsfulde grupper (fx thiazid n=3) → drop den formelle test og rapportér **deskriptivt**: *"De tre thiaziddeltagere havde U-Ca på 12, 18 og 21 mg/døgn mod en kohortemedian på 35 mg."*

**Med n=3 er en p-værdi meningsløs.** At vise tallene deskriptivt er mere ærligt og lige så informativt.

### Trin 3 — SGLT2i separat

Her har du n=23 vs. n=9 — brugbart. Mann-Whitney med udfaldene:

- $FE_{Pi}$ (når du har beregnet den)
- P-fosfat
- P-PTH
- U-natrium og natriumbalance

Rationalet: SGLT2-hæmmere er associeret med stigning i P-fosfat, FGF23 og PTH samt nedsat fraktionel fosfatudskillelse — og med natriurese. Med 72 % eksponering er det potentielt en medvirkende forklaring på flere af dine fosforresultater.

### Trin 4 — Frame det korrekt

Én sætning, hver gang:

> *"Disse analyser var eksplorative, ikke prædefinerede i protokollen, og ikke korrigeret for multiple sammenligninger. De skal betragtes som hypotesegenererende."*

Du gør det allerede andre steder i specialet — du er god til det. Gør det også her.

### Om doserne

Du havde ret i, at dosisforskelle er et problem — men det er et **mindre** problem end sammenblandingen af stofklasser. Dosisvariation giver støj (→ type II-fejl, du overser en effekt). Sammenblanding af modsatrettede klasser kan **udslette** en reel effekt helt. Klassificering efter stofgruppe er derfor et klart fremskridt, selv uden dosis.

</details>

---

## 10. Punkt 8 igen — nulfund, forklaret med en badevægt

### Fejlslutningen

Der er forskel på:

- **"Vi fandt ingen sammenhæng."** ← det dine data siger
- **"Der er ingen sammenhæng."** ← det din perspektivering siger

I perspektiveringen skriver du: *"suggest that there is no real trend towards an increasing retention."* Det er den anden — og den er ikke understøttet.

### Analogien

Forestil dig, at du skal afgøre, om et spædbarn har taget 50 gram på. Du vejer det på en badevægt, der viser i hele kilo.

Vægten siger 4 kg begge dage. Du har **ikke** vist, at barnet ikke er vokset. Du har vist, at **din vægt er for grov til spørgsmålet.**

Det er præcis din situation:
- Du leder efter en fosforretention i størrelsesordenen **50–150 mg/døgn**, som først bliver farlig efter måneders akkumulering.
- Dit måleredskab er **én døgnurin + én kostdag**. Dag-til-dag-variationen i fosforindtag alene er typisk CV ≈ 30 %, altså ±330 mg/døgn ved et indtag på ~1100 mg.
- Stremke et al. (2018), som du selv citerer, konkluderer netop, at **flere døgnurin-opsamlinger** er nødvendige for at nå ≥75 % reliabilitet ved CKD.

Støjen er 3–6 gange større end signalet.

### Hvad konfidensintervallet tilføjer

$\rho$ er dit bedste gæt. Konfidensintervallet er de værdier, dine data er forenelige med:

| Fund | $\rho$ | 95 % CI | Data forenelige med |
|---|---|---|---|
| Fosforbalance vs. CrCl (WFR) | 0,02 | $[-0{,}34;\ 0{,}38]$ | moderat negativ → moderat positiv |
| Fosfor-ratio vs. CrCl (foto) | 0,31 | $[-0{,}05;\ 0{,}60]$ | ingen effekt → **stærk** effekt |

Se den nederste linje. Dit "borderline signifikante" fund er foreneligt med **alt fra ingenting til en stærk sammenhæng.** Det er ikke et svagt fund — det er et **uinformativt** fund. Og det gælder lige så meget for nulfundet ovenover.

**I Prism:** Analyze → Correlation → sæt flueben i *"Compute confidence interval"*. Tilføj en CI-kolonne til tabel 5, 8, 10 og 11. Det tager en time og løfter niveauet mærkbart.

### Den nye formulering

**Erstat:**
> "suggest that there is no real trend towards an increasing retention as renal function declines"

**Med:**
> "Studiet fandt ingen sammenhæng mellem apparent fosforbalance og creatininclearance. Konfidensintervallerne var imidlertid brede og forenelige med både positive og negative sammenhænge, og den metodiske usikkerhed ved estimater baseret på én kostdag og én døgnurin overstiger den daglige retention, der ville være klinisk relevant over tid. Studiet kan derfor hverken bekræfte eller udelukke klinisk relevant fosforretention ved CKD stadie 4-5."

Svagere som overskrift. Men det er, hvad dine data bærer — og det er den formulering, en censor belønner.

---

## Din prioritering nu

**Skal gøres (ren tekst, ~1,5 time, størst effekt):**
1. Abstract + konklusion: "sodium retention occurred" → "apparent sodium balance was significantly higher"
2. Perspektivering: "no real trend" → "kunne hverken bekræfte eller udelukke"
3. Resultatafsnit: alfacalcidol-fundet omformuleres til confounding by indication

**Bør gøres (~3–4 timer, stor gevinst):**
4. Kreatinin-index + fordelingen + antal under 0,10
5. $FE_{Pi}$ mod CrCl
6. 95 % CI på Spearman-tabellerne

**Hvis der er tid:**
7. U-Na og Na-indtag mod CrCl separat
8. Sensitivitetsanalyse uden flaggede
9. Diuretika-omkodning
10. Formalia (tabelnumre, "Figure xx", `r=8153`)

Til forsvaret er det vigtigste, at du kan **fortælle den samlede historie**: differencemålet domineres af indtagsvariationen, ratio og $FE_{Pi}$ er de rigtige mål, opsamlingskvalitet er en reel trussel som du har undersøgt (og hvor CrCl > eGFR og fosfor-nulfundet er dine to modargumenter), og konklusionerne er justeret, så de svarer til datas opløsningsevne.

Det er et fuldstændigt kompetent forsvar. Skriv til, hvis noget stadig er uklart — og send gerne tallene, når du har regnet $FE_{Pi}$.

**User - --**

ja jeg vil jo ikke have en halvskidt karakter.   jeg kan jo ikke tilføje til specialet når jeg nu har afleveret men jeg tænker at lave et oplæg hvor alt er med!. okay så faktisk kan man måske sige udfra fosfor at der burde være en tilstrækkelig opsamling men alligevel nok meget godt at bevise med de andre beregninger? hvilken forskel gør at det er i onkologisk population?  hvor var grænseværdien for udskillelsen af kreatinin? jeg har beregnet FE og vedhæfter screen for data. - 0.29 for fe vs crcl og 0.26 for fe vs p intake ved vejet metode bemærk jeg har brugt pearson denne her gang da det normalt er lignende korrelationer jeg får.  punkt 8 forstår jeg stadig ikke "et er præcis din situation:

Du leder efter en fosforretention i størrelsesordenen 50–150 mg/døgn, som først bliver farlig efter måneders akkumulering.
Dit måleredskab er én døgnurin + én kostdag. Dag-til-dag-variationen i fosforindtag alene er typisk CV ≈ 30 %, altså ±330 mg/døgn ved et indtag på ~1100 mg.
Stremke et al. (2018), som du selv citerer, konkluderer netop, at flere døgnurin-opsamlinger er nødvendige for at nå ≥75 % reliabilitet ved CKD.
Støjen er 3–6 gange større end signalet.

Hvad konfidensintervallet tilføjer
ρ er dit bedste gæt. Konfidensintervallet er de værdier, dine data er forenelige med:"

**Assistant - --**

# Feedback på $FE_{Pi}$-beregningen + de sidste uddybninger

Godt arbejde at du faktisk regnede det. Der er både gode nyheder og én ting, du **skal** tjekke inden du viser tallene til nogen. Jeg starter med det vigtigste.

---

## 1. Din beregning er korrekt — jeg har efterregnet den

Jeg har verificeret tre rækker manuelt:

| Række | $U_{Pi}$ | $P_{Cr}$ | $P_{Pi}$ | $U_{Cr}$ | Din $FE$ | Min kontrol |
|---|---|---|---|---|---|---|
| 1 | 14,4 | 0,300 | 1,18 | 8,48 | 43,17 % | $\frac{14{,}4 \times 0{,}300}{1{,}18 \times 8{,}48} = 43{,}2\%$ ✓ |
| 10 | 20 | 0,413 | 1,87 | 7,75 | 57,00 % | $\frac{8{,}26}{14{,}49} = 57{,}0\%$ ✓ |
| 30 | 8 | 0,177 | 1,60 | 6,20 | 14,27 % | $\frac{1{,}416}{9{,}92} = 14{,}3\%$ ✓ |

Enhedskonverteringen (µmol/L → mmol/L) er håndteret rigtigt. **Formlen er implementeret korrekt.**

Og retningen er den rigtige: $r = -0{,}29$ betyder højere fraktionel udskillelse ved lavere clearance — præcis kompensationshypotesen. Det er dit første positive fysiologiske fund. Men det skal renses op først.

---

## 2. ⚠️ Række 31 skal tjekkes — og den har måske også påvirket dit baseline-skema

Rækken med `urin p = 11,25` og `urin cr = 51,25`:

**Problemet:** $U_{Cr} = 51{,}25$ mmol/døgn svarer til ca. **5,8 g kreatinin i døgnet**. Det er fysiologisk umuligt hos en 75-årig CKD-patient (dine øvrige værdier ligger 5,1–15,9).

**Beviset for at det er en tastefejl:** Din egen GFR-kolonne siger 24,72 ml/min for den række. Regn baglæns:

$$U_{Cr} = 24{,}72 \times 1{,}44 \times 0{,}144 = 5{,}12 \text{ mmol/døgn}$$

Havde $U_{Cr}$ virkelig været 51,25, ville CrCl være **247 ml/min** — og din baselinetabel siger, at højeste clearance i kohorten er 54.

Så: **GFR-kolonnen bruger 5,125, mens FE-kolonnen bruger 51,25.** Der er en faktor 10 i en af dem, og det er FE, der er forkert. Korrigeret bliver $FE = 37{,}2\%$ i stedet for 3,72 % — helt plausibelt.

> **Og her bliver det relevant for specialet:** Din baselinetabel angiver U-kreatinin som `8,4 (46)` mmol/døgn. Med median 8,4, minimum 5,1 og maksimum 51,25 er range præcis 46,15. **Tastefejlen sidder altså sandsynligvis også i den publicerede baselinetabel** og har oppustet det rapporterede range.
>
> Det er ikke en katastrofe (medianen er upåvirket), men hvis du selv nævner det i oplægget — *"jeg har efterfølgende identificeret en sandsynlig indtastningsfejl i U-kreatinin for én deltager, som påvirker det rapporterede range, men ikke medianen eller nogen analyse"* — så er det data-integritet i stedet for en fejl, censor finder.

**Tjek desuden række 19** (`urin p 17,15`, `urin cr 15,925`, `p crea 189`): $15{,}925/0{,}189 = 84{,}3$ L/døgn $= 58{,}5$ ml/min, men din GFR-kolonne siger 53,51. Der er også uoverensstemmelse her. **Gå din GFR-kolonne og din FE-kolonne igennem og sikr dig, at de bruger samme $U_{Cr}$ og $P_{Cr}$.**

---

## 3. Skift tilbage til Spearman — og her er hvorfor det ikke er kosmetik

Du skriver, at du brugte Pearson, "da det normalt er lignende korrelationer jeg får". Det er den ene begrundelse, du **ikke** kan bruge til et forsvar. En censor vil spørge: *"valgte du test efter at have set resultatet?"* — og så er du på bagfod uanset svar.

Der er tre selvstændige grunde til at bruge Spearman:

1. **Konsistens.** Hele specialet bruger Spearman med en eksplicit begrundelse (ikke-parametriske data, outliers). At skifte til én analyse ser selektivt ud.
2. **Ikke-linearitet.** Forholdet mellem $FE_{Pi}$ og GFR er teoretisk **hyperbolsk**, ikke lineært — når nefronmassen halveres, skal hver nefron fordoble sin udskillelse. Pearson måler kun lineær sammenhæng og vil derfor *undervurdere* en reel monoton sammenhæng. Spearman måler monotonicitet og er det rigtige valg.
3. **Og det afgørende — se her:**

### To datapunkter driver hele din Pearson-korrelation

Jeg har regnet kryds-produkterne igennem. Summen er $-1146$. Fordelingen:

| Række | GFR | $FE_{Pi}$ | Bidrag til kovariansen |
|---|---|---|---|
| 23 | 9,49 | 72,66 % | **−535** |
| 19 | 53,51 | 20,77 % | **−487** |
| Alle øvrige 30 tilsammen | | | −124 |

**To deltagere ud af 32 leverer 89 % af din korrelation.** Fjern dem, og $r$ falder mod nul.

De to punkter er sandsynligvis *ægte* signal (lavest GFR har højest FE, højest GFR har lavest FE — præcis som teorien forudsiger). Men et resultat, der hænger på to observationer, er skrøbeligt over for Pearson og robust over for Spearman, fordi Spearman kun bruger deres **rang**, ikke deres afstand.

**Kør Spearman. Rapportér Pearson som sensitivitetsanalyse.** Og vær forberedt på at nævne indflydelsesanalysen selv — det er et stærkt kort at spille før nogen spørger.

---

## 4. Hvad du kan og ikke kan konkludere af dine to FE-tal

Her er konfidensintervallerne, regnet med Fishers z:

| Analyse | $r$ | $n$ | 95 % CI | $p$ |
|---|---|---|---|---|
| $FE_{Pi}$ vs. CrCl | −0,29 | 32 | $[-0{,}58;\ +0{,}07]$ | ≈ 0,11 |
| $FE_{Pi}$ vs. fosforindtag | +0,27 | 32 | $[-0{,}09;\ +0{,}57]$ | ≈ 0,14 |

Tre ting følger:

**a) Ingen af dem er signifikante.** Begge $p \approx 0{,}1$. Du kan ikke sige, at der *er* en sammenhæng — kun at retningen er som forventet.

**b) Du kan ikke konkludere, at GFR dominerer over kosten.** Jeg foreslog den analyse sidst i forventning om, at CrCl-korrelationen ville blive klart stærkere. Det blev den ikke: $|{-}0{,}29|$ og $|{+}0{,}27|$ er statistisk **umulige at skelne**, og deres CI'er overlapper næsten fuldstændigt. Det ærlige udsagn er:

> *"Den fraktionelle fosfatudskillelse korrelerede svagt negativt med creatininclearance og svagt positivt med fosforindtaget, i begge tilfælde i den fysiologisk forventede retning, men ingen af sammenhængene var statistiske signifikante, og deres styrke kunne ikke skelnes fra hinanden."*

**c) Din korrelation er svagere end litteraturen forudsiger — og det skal du kunne forklare.** Forventet ville være $r \approx -0{,}6$ til $-0{,}8$. Fire forklaringer, i prioriteret rækkefølge:

| Forklaring | Kommentar |
|---|---|
| **Range restriction** | 25 af 32 ligger mellem 15 og 32 ml/min. Korrelationer attenueres kraftigt, når spredningen i x indsnævres. Dette er formentlig hovedforklaringen. |
| Ikke-linearitet + Pearson | Prøv $FE$ mod $1/\mathrm{CrCl}$ — det linearariserer og bør styrke $r$ mærkbart |
| Datafejlen i række 31 | Fjerner du den, går $r$ fra −0,29 til ca. **−0,32** |
| Enkeltdags-variabilitet | Både $U_{Pi}$ og $P_{Pi}$ måles én gang |

**Prøv $1/\mathrm{CrCl}$ — det er ét minut i Excel og kan flytte resultatet meget.**

<details>
<summary><strong>To ekstra observationer i dine FE-data, som er værd at kigge på (klik)</strong></summary>

### Din $FE_{Pi}$ er systematisk underestimeret

$FE_{Pi}$ defineres som fosfats clearance divideret med **GFR**. Du bruger kreatininclearance som GFR-surrogat — men CrCl overstiger den sande GFR med 10–30 % pga. tubulær sekretion (punkt 6 nedenfor). Da $C_{Cr}$ står i nævneren, bliver din $FE_{Pi}$ tilsvarende **for lav**.

Det forklarer, hvorfor din median på ~37 % ligger i den lave ende af det forventede for CKD 4 (40–70 %). Nævn det — det viser, at du forstår, hvad dit surrogatmål gør.

### FE-spredningen inden for samme clearance er enorm

I clearance-intervallet 20–30 ml/min varierer din $FE_{Pi}$ fra **14 % til 72 %** — en femdobling ved praktisk samme nyrefunktion. Det er i sig selv et resultat: den fraktionelle kompensation er langt mere heterogen mellem individer end mellem GFR-niveauer. Det understøtter din egen diskussion om, at "det præcise punkt, hvor kompensationen svigter, varierer individuelt".

### En gratis analyse, du bør lave: $FE_{Pi}$ vs. P-fosfat

Det er den mest kliniske af dem alle, og du har begge kolonner:

- **Høj $FE_{Pi}$ + normal P-fosfat** = velfungerende kompensation
- **Lav $FE_{Pi}$ + høj P-fosfat** = **kompensationen har svigtet**

Kig på din række 30: $P_{Pi} = 1{,}60$ mmol/L (hyperfosfatæmi) med $FE_{Pi}$ på kun 14,3 % ved GFR 24. Det er lige præcis den fænotype, dit speciale handler om. Og række 26: $P_{Pi} = 1{,}72$ med $FE = 19{,}7\%$.

Et Spearman-plot af $FE_{Pi}$ mod P-fosfat — plus en optælling af hvor mange der har hyperfosfatæmi *trods* lav FE — er et konkret, klinisk relevant fund fra dine egne data. Det tager 20 minutter.

</details>

---

## 5. Kan fosfor bruges som intern kontrol mod opsamlingsartefakt? Ja — med to forbehold

Din tanke er rigtig, og det er et godt argument. Men vær præcis om, hvor stærkt det er:

**Argumentet:** Urinudskillelsen udgør ~44 % af fosforindtaget. Var opsamlingerne systematisk ufuldstændige, ville faktoren $k$ ramme fosforbalancen mærkbart og skabe en negativ korrelation med CrCl. Den findes ikke ($\rho = 0{,}02$).

**Forbehold 1 — det udelukker det systematiske, ikke det differentielle.** Argumentet virker mod *ensartet* undersopsamling på tværs af kohorten. Det virker svagere mod den hypotese, du selv fremsatte: at netop de **sygeste** opsamler dårligst. Der ville effekten koncentreres i <20-gruppen (n=8), og med så få deltagere kan fosforanalysen godt være blind for den.

**Forbehold 2 — natrium er mere sårbart.** Fordi $E \approx I$ for natrium (2191 vs. 2010 mg), er natriumbalancen næsten ren udskillelse. Enhver skalering af $E$ slår fuldt igennem. For fosfor "beskyttes" balancen af det store indtagsoverskud. Så fosfornulfundet er ikke en fuldgyldig kontrol for natriumfundet.

**Det stærkeste argument har du faktisk et andet sted — se næste punkt.**

---

## 6. CrCl > eGFR er dit bedste argument — men det kolliderer med din egen reference

### Hvorfor CrCl (25) > eGFR (20) er forventeligt

To uafhængige mekanismer, der trækker samme vej:

| Mekanisme | Effekt |
|---|---|
| **Tubulær sekretion.** Kreatinin filtreres *og* secerneres aktivt i proksimale tubulus. Kreatininclearance overstiger derfor den sande GFR med typisk 10–30 %, mest udtalt ved fremskreden CKD | CrCl > sand GFR |
| **BSA-indeksering.** eGFR angives per 1,73 m². Din CrCl er rå ml/min. Ved 77 kg og 172 cm er BSA ca. 1,9 m², altså ~10 % over 1,73 | rå CrCl > indekseret eGFR |

Tilsammen forklarer det rigeligt 5 ml/min. **Og det er evidens for, at opsamlingerne i gennemsnit var rimeligt komplette** — havde de været 20 % ufuldstændige, ville CrCl være trukket ned under eGFR.

### Men: din reference siger det modsatte

Lahiji et al. (2025) hedder ordret *"eGFR Equations **Overestimate** Renal Function Compared With Measured GFR Using 24-Hour Urine Creatinine Clearance"* — altså eGFR > CrCl. Du citerer den på s. 40 som begrundelse for at bruge CrCl. **Dine egne data viser den modsatte retning.** Det skal du kunne forklare.

### Hvorfor den onkologiske population betyder noget

Her er svaret på dit spørgsmål:

| Faktor | Onkologisk kohorte (Lahiji) | Din CKD 4-5-kohorte |
|---|---|---|
| **Muskelmasse** | Kakeksi/sarkopeni er udbredt → lav kreatininproduktion → eGFR-ligninger (som antager normal muskelmasse for alder/køn) overvurderer GFR kraftigt | Sarkopeni forekommer (ESPEN: 20–40 % PEW), men mindre udtalt |
| **GFR-niveau** | Ofte normal til let nedsat (måles typisk mhp. carboplatin-dosering). Tubulær sekretion udgør en mindre relativ andel | Svært nedsat. Sekretionens *relative* bidrag til CrCl vokser, når filtrationen falder |
| **Nettoresultat** | Sarkopeni-effekten dominerer → eGFR > CrCl | Sekretion + BSA dominerer → CrCl > eGFR |

**Og den vigtigste konceptuelle pointe:** eGFR-ligninger er kalibreret mod **sand** GFR målt med iohexol eller inulin — ikke mod kreatininclearance. Lahiji bruger CrCl som referencestandard, men CrCl er selv et biased mål for GFR (opad, pga. sekretion). Så uenigheden mellem dem og dig handler i høj grad om, hvad man kalder "sandheden".

**Formuleringen til forsvaret:**

> *"Forholdet mellem eGFR og kreatininclearance afhænger af populationens muskelmasse og af, om eGFR er BSA-indekseret. I min kohorte oversteg CrCl eGFR, som forventeligt ud fra tubulær kreatininsekretion og de-indeksering. Lahijis modsatte fund stammer fra en onkologisk population med udbredt kakeksi, hvor eGFR-ligningerne overestimerer af den grund. Jeg burde have nuanceret den reference."*

At du selv rejser det, er langt bedre end at blive fanget i det.

---

## 7. Grænseværdien for kreatininudskillelse — og en vigtig nuance, der taler til din fordel

Du spurgte, hvor grænsen er. Der er ingen universel konsensusgrænse, men de gængse referenceværdier:

| Gruppe | mg/kg/døgn | mmol/kg/døgn |
|---|---|---|
| Mænd, 20–50 år | 20–25 | 0,18–0,22 |
| Kvinder, 20–50 år | 15–20 | 0,13–0,18 |
| >70 år | ca. 10–20 % lavere | ♂ 0,14–0,19 · ♀ 0,10–0,15 |

*(Omregning: molvægt 113 g/mol, så 20 mg/kg ÷ 113 = 0,177 mmol/kg.)*

**Praktiske grænser i litteraturen** — vælg én og angiv den eksplicit:

- **Simpel:** < 0,10 mmol/kg/døgn (♂) og < 0,08 (♀) flagges
- **Bedre:** afvigelse > ±30 % fra forventet ud fra alder, køn og vægt
- **Simplest:** absolut $U_{Cr}$ < 7 mmol/døgn (♂) eller < 5 mmol/døgn (♀)

Din median på 0,109 mmol/kg/døgn ligger under forventet — men **kig på halen, ikke medianen.** Ud fra dit screenshot har du værdier ned til 5,1 og 5,2 mmol/døgn, som ved normal kropsvægt giver et index omkring 0,07.

### Nuancen, der er god for dig

Ved fremskreden CKD stiger den **ekstrarenale (intestinale) nedbrydning af kreatinin** — bakteriel kreatininase i tarmen kan fjerne op mod 30 % af den producerede kreatinin ved GFR < 20 ml/min. Derfor er urinkreatininudskillelsen *fysiologisk* lavere i CKD 4-5, uafhængigt af muskelmasse og opsamlingskvalitet.

**Konsekvens:** et lavt kreatinin-index i din population er **ikke** i sig selv bevis for ufuldstændig opsamling. Kombineret med at CrCl > eGFR, har du et rimeligt robust forsvar:

> *"Kreatinin-index var lavt (median 0,11 mmol/kg/døgn), men det forventes ved CKD 4-5 pga. sarkopeni og øget ekstrarenal kreatininnedbrydning. At kreatininclearance oversteg eGFR taler imod systematisk undersopsamling. N deltagere lå under 0,08 mmol/kg/døgn, og eksklusion af disse ændrede ikke [ændrede] natriumfundet."*

Sidste sætning kræver, at du faktisk kører analysen. Det er stadig værd at gøre.

---

## 8. Signal og støj — tredje forsøg, nu helt konkret

Du har spurgt tre gange, så lad mig droppe abstraktionerne og bygge det op fra bunden med tal.

### Trin 1: Hvad ville et *reelt* fund se ud som?

Antag, at virkeligheden er: **for hver 1 ml/min clearance falder, ophobes 10 mg fosfor mere per døgn.**

Din kohorte spænder fra 9 til 54 ml/min = 45 ml/min. Så mellem den sygeste og den friskeste skulle der være:

$$45 \times 10 = 450 \text{ mg/døgn forskel i balance}$$

Det ville være en **stærk** sammenhæng — noget i retning af $\rho \approx 0{,}6$.

### Trin 2: Hvor meget svinger din måling af sig selv?

Du måler hver deltagers balance **én gang**: én kostdag og én døgnurin. Men både kost og udskillelse svinger fra dag til dag hos den samme person:

| Kilde | Typisk CV | Ved dine medianværdier | SD |
|---|---|---|---|
| Fosforindtag dag-til-dag | ~30 % | 1081 mg | ± 325 mg/døgn |
| U-fosfor dag-til-dag | ~22 % | 474 mg | ± 105 mg/døgn |
| **Samlet på balancen** | | $\sqrt{325^2 + 105^2}$ | **± 340 mg/døgn** |

Det er ren biologisk dag-til-dag-variation, **før** man lægger databaseunøjagtighed og portionsestimering oveni.

### Trin 3: Sæt de to sammen

To konkrete deltagere:

| | Sand balance | Målt (kan lande hvor som helst inden for ±340) |
|---|---|---|
| **Anna**, CrCl 50 | 0 mg/døgn | −340 til +340 |
| **Bent**, CrCl 12 | +380 mg/døgn | +40 til +720 |

Deres **sande** forskel er 380 mg. Men deres **målte** værdier overlapper: Anna kan måle +340 og Bent kan måle +40 — altså modsat af sandheden.

**Det er hele pointen:** støjen per person (±340) er på samme størrelse som det signal, du leder efter (450 mg over hele GFR-spektret). Med 30 deltagere drukner signalet.

### Trin 4: Hvad det gør ved din korrelation

Måleusikkerhed **attenuerer** korrelationer — den trækker dem systematisk mod nul:

$$r_{\text{observeret}} = r_{\text{sand}} \times \sqrt{\text{reliabilitet}}$$

Stremke et al. (som du selv citerer) fandt, at én døgnurin ved CKD ikke når 75 % reliabilitet. Med reliabilitet på fx 0,55:

$$r_{\text{observeret}} = r_{\text{sand}} \times \sqrt{0{,}55} = 0{,}74 \times r_{\text{sand}}$$

En sand sammenhæng på 0,40 ville altså vise sig som 0,30 — og med $n = 30$ er 0,30 ikke signifikant.

**Din måling er derfor biased mod at finde ingenting.** Det er ikke det samme som, at der ikke er noget.

### Trin 5: Hvad konfidensintervallet tilføjer

$\rho$ er ét tal — dit bedste gæt. Men dine data er forenelige med et **interval** af sande værdier. CI'et fortæller, hvilket:

| Dit fund | $\rho$ | 95 % CI | Læs det som |
|---|---|---|---|
| Fosforbalance vs. CrCl | 0,02 | $[-0{,}34;\ +0{,}38]$ | "Sandheden kan være alt fra moderat negativ til moderat positiv" |

En sand korrelation på **+0,35** — som ville være klinisk relevant — ligger **inden for** dit interval. Dine data kan altså ikke udelukke den.

Derfor er:

- ❌ *"There is no real trend towards increasing retention"* → påstår at sandheden er 0
- ✅ *"Studiet kunne hverken bekræfte eller udelukke klinisk relevant fosforretention"* → beskriver hvad intervallet tillader

**Analogi til sidst:** en badevægt, der viser i hele kilo, siger 4 kg i dag og 4 kg i morgen. Du har ikke bevist, at barnet ikke er vokset 50 gram. Du har bevist, at din vægt er for grov til spørgsmålet. Din vægt er "én kostdag + én døgnurin", og de 50 gram er den daglige fosforretention.

---

<details>
<summary><strong>9. Struktur til dit oplæg (klik)</strong></summary>

At lave et oplæg med de supplerende analyser er den rigtige strategi. Men to advarsler:

⚠️ **Vis ikke tal med kendte fejl.** Ret række 31 og tjek GFR/FE-konsistensen, før noget kommer på et slide.

⚠️ **Brug ikke mere end ~⅓ af tiden på nyt materiale.** Eksamen handler primært om det, du har afleveret. Nye analyser skal fungere som demonstration af, at du forstår begrænsningerne — ikke som et nyt speciale.

**Foreslået fordeling ved 20 minutter:**

| Min | Indhold |
|---|---|
| 0–3 | Baggrund og forskningsspørgsmål (formuleret **helt** — sætningen på s. 10 er ufuldstændig) |
| 3–7 | Metode: to kostmetoder, døgnurin, hvad "apparent balance" er og ikke er |
| 7–12 | Hovedresultater: nulfundene, natriumfundet, metodesammenligningen |
| 12–17 | **"Hvad jeg har arbejdet videre med efter afleveringen"** |
| 17–20 | Reviderede konklusioner + perspektivering |

**Indholdet i blok 12–17 — i denne rækkefølge:**

1. **Differencemålet er domineret af indtagsvariansen.** Vis $\rho$ mellem $B$ og $I$. Konklusion: ratio og $FE_{Pi}$ er de rigtige endpoints.
2. **$FE_{Pi}$-analysen.** Spearman, retning som forventet, ikke signifikant, forklar range restriction. Vis også $FE$ mod $1/\mathrm{CrCl}$ hvis du får det regnet.
3. **Opsamlingskvalitet.** Mekanismen ($k$ rammer både $E$ og CrCl) → kreatinin-index-fordelingen → CrCl > eGFR som modargument → sensitivitetsanalyse.
4. **Reviderede formuleringer.** Vis gammel og ny tekst side om side for natriumkonklusionen og for "no real trend".

Den slags slide — *"her er hvad jeg skrev, her er hvad jeg burde have skrevet, og her er hvorfor"* — er præcis, hvad en censor belønner. Det demonstrerer, at du kan vurdere dit eget arbejde kritisk, hvilket er en eksplicit læringsmålsformulering på kandidatniveau.

</details>

---

## Din to-do nu, i prioriteret rækkefølge

| # | Opgave | Tid |
|---|---|---|
| 1 | **Ret række 31** (51,25 → 5,125) og tjek GFR/FE-konsistens i hele arket | 30 min |
| 2 | Kør $FE_{Pi}$ vs. CrCl med **Spearman**, med CI | 20 min |
| 3 | Prøv $FE_{Pi}$ mod $1/\mathrm{CrCl}$ | 10 min |
| 4 | $FE_{Pi}$ vs. P-fosfat (den kliniske analyse) | 20 min |
| 5 | Kreatinin-index: kolonne, fordeling, antal under grænsen | 45 min |
| 6 | Sensitivitetsanalyse på natrium uden flaggede | 30 min |
| 7 | Skriv de tre reviderede formuleringer ind i oplægget | 45 min |

Du har rigeligt til et solidt forsvar. Det, der afgør karakteren nu, er ikke om resultaterne er positive — det er om du kan **fortælle præcis, hvad dine data kan og ikke kan bære.** Det er du tættere på end du selv tror.

Send tallene når du har kørt Spearman — særligt om række 31-korrektionen flytter noget.

**User - --**

Okay jeg brugte pearson fordi jeg ikke har adgang til graphpad herhjemme. kan du lave en beregning med spearman så? den der 51.25 er tastefejl ja det er heldigvis ikke den jeg brugte i mit speciale!  jeg har prøvet med den liniliseret pearson og der bliver r =0.453. kan du lave den der "En gratis analyse, du bør lave: FE 
Pi
​
  vs. P-fosfat
Det er den mest kliniske af dem alle, og du har begge kolonner:

Høj FE 
Pi
​
  + normal P-fosfat = velfungerende kompensation
Lav FE 
Pi
​
  + høj P-fosfat = kompensationen har svigtet
Kig på din række 30: P 
Pi
​
 =1,60 mmol/L (hyperfosfatæmi) med FE 
Pi
​
  på kun 14,3 % ved GFR 24. Det er lige præcis den fænotype, dit speciale handler om. Og række 26: P 
Pi
​
 =1,72 med FE=19,7.

Et Spearman-plot af FE 
Pi
​
  mod P-fosfat — plus en optælling af hvor mange der har hyperfosfatæmi trods lav FE — er et konkret, klinisk relevant fund fra dine egne data. Det tager 20 minutter" jeg forstår ikke det her "Forbehold 1 — det udelukker det systematiske, ikke det differentielle. Argumentet virker mod ensartet undersopsamling på tværs af kohorten. Det virker svagere mod den hypotese, du selv fremsatte: at netop de sygeste opsamler dårligst. Der ville effekten koncentreres i <20-gruppen (n=8), og med så få deltagere kan fosforanalysen godt være blind for den.

Forbehold 2 — natrium er mere sårbart. Fordi E≈I for natrium (2191 vs. 2010 mg), er natriumbalancen næsten ren udskillelse. Enhver skalering af E slår fuldt igennem. For fosfor "beskyttes" balancen af det store indtagsoverskud. Så fosfornulfundet er ikke en fuldgyldig kontrol for natriumfundet." jeg har også lige beregnet den med kreatinin udskillelse i mg ift vægt det står i kolonne cr omregning i det jeg har vedhæfter. lige det her forstår jeg ikke "tremke et al. (som du selv citerer) fandt, at én døgnurin ved CKD ikke når 75 % reliabilitet. Med reliabilitet på fx 0,55:

r 
observeret
​
 =r 
sand
​
 × 
0,55
​
 =0,74×r 
sand
​
 

En sand sammenhæng på 0,40 ville altså vise sig som 0,30 — og med n=30 er 0,30 ikke signifikant.

Din måling er derfor biased mod at finde ingenting. Det er ikke det samme som, at der ikke er noget." . så ift natrium skal jeg så regne det ud med korrelation mellem indtag-udskillelse og clearance hvor jeg har fjernet de flagggerede både for vejet og billede metode? 

**Assistant - --**

# Jeg har regnet Spearman på dine data — og der er noget vigtigt

Jeg har kørt beregningerne i hånden på de 32 rækker fra dine to screenshots (med række 31 rettet til $U_{Cr} = 5{,}125$, som din nye `cr omregn`-kolonne bekræfter). **Verificér dem selv i Excel** — jeg giver formlerne længere nede — men resultatet er entydigt nok til, at du skal kende det, før du bygger et oplæg op om $FE_{Pi}$.

---

## 1. Hovedresultatet: Spearman er markant svagere end Pearson

| Analyse | Pearson | **Spearman $\rho$** | $p$ | 95 % CI (Spearman) |
|---|---|---|---|---|
| $FE_{Pi}$ vs. CrCl | −0,318 | **−0,17** | 0,34 | $[-0{,}49;\ +0{,}19]$ |
| $FE_{Pi}$ vs. fosforindtag | +0,282 | **+0,20** | 0,27 | $[-0{,}16;\ +0{,}52]$ |
| $FE_{Pi}$ vs. P-fosfat | — | **+0,33** | 0,061 | $[-0{,}02;\ +0{,}61]$ |

Din Pearson på −0,32 bliver altså −0,17 med Spearman. Det er ikke en detalje: den ene er "svag tendens", den anden er "praktisk taget ingenting".

### Og her er hvorfor — dit linearariserede fund hænger på én deltager

Du fandt $r = 0{,}453$ for $FE$ mod $1/\mathrm{CrCl}$. Det ser flot ud. Men:

| Beregning | $r$ |
|---|---|
| $FE$ vs. $1/\mathrm{CrCl}$, alle 32 | **+0,453** |
| $FE$ vs. $1/\mathrm{CrCl}$, **uden deltageren med GFR 9,49** | **+0,174** |

Deltageren med CrCl = 9,49 har $1/\mathrm{CrCl} = 0{,}105$, mens alle andre ligger mellem 0,019 og 0,077. Samtidig har hun/han kohortens **højeste** $FE_{Pi}$ (72,7 %). Ekstrem på begge akser = enorm leverage. **Én observation ud af 32 leverer over halvdelen af korrelationen.**

> **Vigtig pointe du skal have med:** Spearman på $1/\mathrm{CrCl}$ giver **præcis samme tal** som Spearman på CrCl, blot med omvendt fortegn (+0,17), fordi $1/x$ er en monoton transformation og rangordenen dermed uændret. At lineariseringen kun hjælper Pearson er i sig selv beviset for, at gevinsten kom fra afstande — ikke fra rangorden.

**Konklusionen du skal drage:** deltageren er sandsynligvis *ægte* signal (lavest GFR, højest FE — helt som teorien forudsiger). Men et resultat, der står på én observation, kan du ikke præsentere som et fund. Rapportér Spearman som primær, Pearson som sensitivitet, og nævn leverage-analysen selv.

---

## 2. $FE_{Pi}$ vs. P-fosfat — den mest interessante af dem alle

$\rho = +0{,}33$, $p = 0{,}061$. Retningen er den fysiologisk forventede: højere plasmafosfat → mere FGF23/PTH → nedregulering af NaPi-IIa/IIc → højere fraktionel udskillelse. Det er præcis den kaskade, du beskriver på s. 15–17.

### Og her er et argument, du absolut skal bruge

Se på formlen:

$$FE_{Pi} = \frac{U_{Pi} \times P_{Cr}}{\boldsymbol{P_{Pi}} \times U_{Cr}}$$

$P_{Pi}$ står i **nævneren**. Rent matematisk vil højere plasmafosfat derfor *trække $FE$ nedad*, alt andet lige. At du alligevel finder en **positiv** sammenhæng betyder, at tælleren stiger mere end proportionalt — altså at den renale udskillelse opreguleres aktivt og kraftigere, end den passive matematiske kobling trækker den anden vej.

> *"Den matematiske kobling arbejder imod fundet, og alligevel er korrelationen positiv. Det styrker fortolkningen som aktiv hormonel opregulering."*

Det er en skarp pointe, som viser, at du forstår dit eget mål.

<details>
<summary><strong>Fænotyperne i dine data — konkrete deltagere du kan pege på (klik)</strong></summary>

Median-split (median $FE$ = 36,6 %, median P-fosfat = 1,30 mmol/L):

| | P-fosfat ≤ 1,30 | P-fosfat > 1,30 |
|---|---|---|
| **Høj $FE$** | 5 | **11** |
| **Lav $FE$** | **11** | 5 |

Fishers eksakte test: $p \approx 0{,}076$. Retningen bekræfter korrelationen.

**"Kompensation svigtet" — hyperfosfatæmi trods lav fraktionel udskillelse (n=5):**

| $FE_{Pi}$ | P-fosfat | CrCl |
|---|---|---|
| 14,3 % | 1,60 | 24,3 |
| 19,7 % | 1,72 | 18,1 |
| 23,2 % | 1,31 | 20,6 |
| 28,7 % | 1,32 | 24,8 |
| 35,4 % | 1,76 | 27,6 |

**"Kompensation velfungerende" — normal fosfat med høj udskillelse:**

| $FE_{Pi}$ | P-fosfat | CrCl |
|---|---|---|
| 37,2 % | 0,85 | 24,7 |
| 44,0 % | 1,08 | 17,6 |
| 52,4 % | 1,08 | 31,3 |

**"Kompensation utilstrækkelig" — maksimal udskillelse, men stadig for høj fosfat:**

| $FE_{Pi}$ | P-fosfat | CrCl |
|---|---|---|
| 72,7 % | 1,51 | 9,5 |
| 72,2 % | 1,37 | 25,3 |
| 57,0 % | 1,87 | 13,0 |

**Det er en meget bedre historie end en korrelationskoefficient.** Tre distinkte fænotyper ved omtrent samme clearance-niveau — det illustrerer direkte din egen diskussionspointe om, at "det præcise punkt hvor kompensationen svigter varierer individuelt".

**Bemærk også:** i clearance-intervallet 20–30 ml/min varierer din $FE_{Pi}$ fra **14 % til 72 %** — en femdobling ved praktisk samme nyrefunktion. Den interindividuelle heterogenitet er langt større end GFR-effekten. Det er i sig selv et resultat.

</details>

---

## 3. Kreatinin-index — jeg har regnet din kolonne igennem

Din `cr omregn` = mg/kg/døgn. Jeg har verificeret formlen (række 1: $8{,}48 \times 113 / 81 = 11{,}83$ ✓).

| | Værdi |
|---|---|
| Median | **11,8 mg/kg/døgn** (= 0,105 mmol/kg) |
| IQR | 10,1–14,5 |
| Range | 6,6–20,3 |
| Antal < 10 mg/kg/døgn | **7** |
| Antal < 9 mg/kg/døgn | **4** |

**Forventet ved alder 75** (Walser/Ix-ligningerne):

$$\text{Mænd} = 28{,}2 - 0{,}172 \times \text{alder} = 15{,}3 \text{ mg/kg/døgn}$$
$$\text{Kvinder} = 21{,}9 - 0{,}115 \times \text{alder} = 13{,}3 \text{ mg/kg/døgn}$$

Din median ligger altså ca. **20–25 % under forventet**. Med et ±30 %-kriterium flagges mænd under 10,7 og kvinder under 9,3 mg/kg/døgn. Beregn den per deltager — du har både køn og alder.

### ⚠️ Men her er det, du skal være mest opmærksom på

Jeg har testet, om kreatinin-index hænger sammen med clearance:

$$\rho = +0{,}45,\quad p = 0{,}009$$

**Lavere clearance → lavere kreatinin-index.** Det er signifikant. Og det er præcis mønsteret, som *både* differentiel undersopsamling *og* ægte biologi forudsiger:

| Forklaring | Type |
|---|---|
| Sygere deltagere opsamler urinen mindre komplet | artefakt |
| Sarkopeni forværres ved faldende GFR | biologi |
| Ekstrarenal (intestinal) kreatininnedbrydning stiger til ~30 % ved GFR < 20 | biologi |
| **$U_{Cr}$ indgår i tælleren i både CrCl og kreatinin-index** | matematisk kobling |

Den sidste er vigtig: fordi $\mathrm{CrCl} \propto U_{Cr}/P_{Cr}$ og $\text{index} \propto U_{Cr}/\text{vægt}$, deler de tælleren. En positiv korrelation er derfor **delvis tautologisk**, og testen er svækket.

**Den rene test, du bør køre i stedet:** korrelér kreatinin-index mod **eGFR**. eGFR beregnes udelukkende fra P-kreatinin, alder og køn — den er fuldstændig uafhængig af urinopsamlingen. Hvis sammenhængen holder mod eGFR, er den ikke matematisk artefakt. Du har eGFR i dit datasæt.

---

## 4. Sensitivitetsanalysen — og et resultat du skal kende

Jeg fjernede de 7 deltagere med kreatinin-index < 10 mg/kg/døgn og kørte $FE_{Pi}$ vs. CrCl igen:

| Analyse | $n$ | Spearman $\rho$ |
|---|---|---|
| Alle | 32 | −0,17 |
| Uden index < 10 | 25 | **−0,03** |

Korrelationen forsvinder helt.

**Men — og det er afgørende for fortolkningen:** 4 af de 7 ekskluderede har CrCl < 18 ml/min, inklusive kohortens laveste (9,49). Jeg har altså ikke kun fjernet "dårlige opsamlinger" — jeg har fjernet **den nederste ende af clearance-spektret** og dermed forstærket range restriction.

**Det er den ærlige konklusion, og den er faktisk stærk:**

> *"Sammenhængen mellem fraktionel fosfatudskillelse og clearance er drevet af deltagerne med lavest clearance — som samtidig er dem med lavest kreatinin-index. De to forklaringer (ægte kompensation ved fremskreden CKD vs. ufuldstændig urinopsamling hos de sygeste) kan ikke adskilles i dette datasæt. Det er en principiel begrænsning ved at bruge kreatininclearance fra samme urinopsamling som både eksponerings- og udfaldsmål."*

Det er et **metodisk indsigtsfuldt** udsagn på kandidatniveau. Det er mere værd end en signifikant p-værdi.

<details>
<summary><strong>Bonus: din $FE_{Pi}$ er systematisk for lav — og hvorfor det er godt at nævne (klik)</strong></summary>

$FE_{Pi}$ defineres som fosfats clearance divideret med **GFR**. Du bruger kreatininclearance som surrogat, men CrCl overstiger sand GFR med 10–30 % pga. tubulær kreatininsekretion. Da $C_{Cr}$ står i nævneren, bliver din $FE_{Pi}$ tilsvarende **underestimeret**.

Det forklarer, hvorfor din median på ~37 % ligger i den lave ende af det forventede for CKD stadie 4 (40–70 %). At du selv kan pege på det, viser at du forstår, hvad dit surrogatmål gør.

</details>

---

## 5. Forbehold 1 og 2 — forklaret uden jargon

Du spurgte til de to forbehold ved at bruge fosfor-nulfundet som kontrol mod opsamlingsartefakt. Her er de i klar tekst.

### Forbehold 1: systematisk vs. differentiel

**Systematisk** = *alle* opsamler lige dårligt. Fx opsamler alle 32 kun 85 %.

**Differentiel** = *nogle* opsamler dårligere end andre — og det hænger sammen med sygdomsgrad.

| | Hvad fosfor-nulfundet gør | Hvorfor |
|---|---|---|
| Mod **systematisk** | Ret effektivt modargument | Fejlen ville ramme hele kohorten og skabe en synlig korrelation. Den findes ikke ($\rho = 0{,}02$). |
| Mod **differentiel** | Svagt modargument | Effekten sidder kun hos de 8 med CrCl < 20. Med så få deltagere har fosforanalysen ikke styrke til at opdage det. |

Og det er netop **differentiel** undersopsamling, du selv foreslog ("de sygere opsamler dårligst"). Dit fosfor-argument rammer altså den forkerte version af problemet.

> **Og nu ved du, at differentiel undersopsamling faktisk er sandsynlig i dine data** — kreatinin-index korrelerer positivt med clearance ($\rho = 0{,}45$). Det gør forbeholdet konkret, ikke teoretisk.

### Forbehold 2: hvorfor natrium er mere sårbart end fosfor

Hele artefaktet virker ved at skalere $E$ ned med faktoren $k$. **Hvor meget det flytter balancen $B = I - E$, afhænger af hvor stor $E$ er.**

Regneeksempel med $k = 0{,}8$:

| | Indtag $I$ | Sand $E$ | Målt $E$ | Sand $B$ | Målt $B$ | **Forskydning** |
|---|---|---|---|---|---|---|
| **Natrium** | 2010 | 2191 | 1753 | −181 | +257 | **438 mg** |
| **Fosfor** | 1081 | 474 | 379 | +607 | +702 | **95 mg** |
| **Calcium** | 753 | 35 | 28 | +718 | +725 | **7 mg** |

Samme opsamlingsfejl. Vidt forskellig konsekvens.

- **Natrium:** $E \approx I$, så balancen er næsten ren udskillelse. Fejlen slår fuldt igennem — 438 mg forskydning.
- **Fosfor:** indtaget er dobbelt så stort som udskillelsen, så balancen "beskyttes" af indtagsoverskuddet. Kun 95 mg.
- **Calcium:** udskillelsen er ~5 % af indtaget. Artefaktet er praktisk taget usynligt.

**Derfor:** at fosforbalancen ikke viser artefaktet, beviser ikke, at natriumbalancen er fri af det. Natrium er 4–5 gange mere sensitivt. Og calcium kan **ikke** bruges som kontrol overhovedet — sig det selv, før nogen spørger.

---

## 6. Attenuering — hvorfor din måling er skruet mod at finde ingenting

Du spurgte til formlen. Her er den bygget op fra bunden.

### Reliabilitet i praktiske termer

Forestil dig, at du måler samme deltagers fosforbalance to gange på to forskellige uger. Reliabilitet = hvor godt de to målinger stemmer overens.

- Reliabilitet 1,0 = perfekt reproducerbar
- Reliabilitet 0,5 = halvdelen af variationen i dine tal er tilfældig støj, ikke ægte forskelle mellem personer

Stremke et al. (2018) — din egen reference — fandt, at **én** døgnurin ved CKD ikke når 75 % reliabilitet. Din balance bruger én døgnurin **plus** én kostdag, altså to støjkilder. Realistisk reliabilitet: ~0,5–0,6.

### Hvad det gør ved korrelationen

$$r_{\text{observeret}} = r_{\text{sand}} \times \sqrt{\text{reliabilitet}}$$

Intuitionen: en korrelation kan aldrig blive stærkere end kvaliteten af de to mål tillader. Støj i x eller y trækker altid $r$ **mod nul** — den kan ikke opfinde en sammenhæng, kun udviske en.

**Med reliabilitet 0,55:**

$$r_{\text{observeret}} = r_{\text{sand}} \times \sqrt{0{,}55} = r_{\text{sand}} \times 0{,}74$$

| Sand sammenhæng | Du ville måle | Signifikant ved $n=30$? |
|---|---|---|
| 0,60 | 0,44 | ✅ ja |
| **0,40** | **0,30** | ❌ **nej** ($p \approx 0{,}11$) |
| 0,20 | 0,15 | ❌ nej |

**Læs den midterste linje.** Der kunne være en reel, klinisk relevant sammenhæng på 0,40 i virkeligheden — og dit studie ville med stor sandsynlighed rapportere den som "ikke signifikant".

Det er den præcise mekanisme bag: *dit design er skruet mod nulfund.* Derfor kan du ikke vende et nulfund om til "der er ingen sammenhæng".

### Og det er derfor CI'et er nødvendigt

| Dit fund | $\rho$ | 95 % CI | Forenelig med |
|---|---|---|---|
| Fosforbalance vs. CrCl | 0,02 | $[-0{,}34;\ +0{,}38]$ | en sand sammenhæng på **+0,35** |

En sand korrelation på 0,35 — klinisk relevant — ligger **inde i** dit interval. Dine data udelukker den ikke.

- ❌ *"There is no real trend"* → påstår at sandheden er 0
- ✅ *"Studiet kunne hverken bekræfte eller udelukke klinisk relevant retention"* → beskriver hvad intervallet tillader

---

<details>
<summary><strong>7. Natrium-analysen: præcis hvad du skal køre (klik)</strong></summary>

Ja — du har forstået det rigtigt. Konkret, i denne rækkefølge:

### Trin 1: Split balancen op (vigtigst, og du har ikke gjort det)

| Analyse | x | y | Spørgsmål |
|---|---|---|---|
| A | CrCl | U-natrium (mg/døgn) | Udskiller de med lav clearance mindre? |
| B | CrCl | Na-indtag, WFR | Spiser de med lav clearance mere salt? |
| C | CrCl | Na-indtag, foto | Samme, anden metode |

**Hvorfor:** dit balancefund kan komme fra $I$ eller fra $E$. Hvis B og C er nul, mens A er negativ, er fundet drevet af udskillelsen — hvilket er fysiologisk meningsfuldt, men også præcis der, hvor artefaktet bor. Sig begge ting.

### Trin 2: Gentag gruppesammenligningen uden flaggede

| | Alle | Uden index < 10 |
|---|---|---|
| Na-balance <20 vs. ≥20, foto | $p = 0{,}008$ | $p = ?$ |
| Na-balance <20 vs. ≥20, WFR | $p = 0{,}018$ | $p = ?$ |

⚠️ **Advarsel:** du har kun 8 deltagere i <20-gruppen. Fjerner du 2–3 af dem, er testen praktisk taget uden styrke. **Rapportér gruppestørrelserne efter eksklusion**, og hvis <20-gruppen kommer under ~6, skriv at analysen er ikke-konklusiv i stedet for at rapportere en p-værdi.

### Trin 3: Spearman i Excel (du har ikke Prism hjemme)

Lav rang-kolonner og korrelér dem:

```
C2:  =RANK.AVG(A2;$A$2:$A$33;1)
D2:  =RANK.AVG(B2;$B$2:$B$33;1)
rho: =CORREL(C2:C33;D2:D33)
```

p-værdi:

```
=T.DIST.2T(ABS(rho)*SQRT((n-2)/(1-rho^2));n-2)
```

95 % CI (Fisher z):

```
nedre: =TANH(ATANH(rho)-1,96/SQRT(n-3))
øvre:  =TANH(ATANH(rho)+1,96/SQRT(n-3))
```

Mann-Whitney kan Excel ikke uden videre — brug en gratis onlineberegner, eller rapportér medianer + IQR deskriptivt og gem testen til du har Prism.

</details>

---

## 8. Hvad det her betyder for dit oplæg

Lad mig være direkte: **$FE_{Pi}$ blev ikke det positive fund, jeg havde håbet på.** Spearman er −0,17 ($p = 0{,}34$), Pearson hænger på én deltager, og sensitivitetsanalysen nulstiller den. Sælg den ikke som et fund.

Men du har fået noget bedre: **en fuldt gennemarbejdet metodekritik af dit eget speciale.** Det er præcis, hvad der efterspørges på kandidatniveau.

### Foreslået slide-rækkefølge i blokken "efter afleveringen"

| # | Slide | Budskab |
|---|---|---|
| 1 | $B$ vs. $I$ ($\rho > 0{,}85$) | Differencemålet er domineret af indtagsvariansen — ratio og $FE_{Pi}$ er de rigtige endpoints |
| 2 | $FE_{Pi}$: Pearson −0,32 / Spearman −0,17 / uden én deltager: −0,03 | Retningen er forventet, men fundet er ikke robust. **Range restriction** (25 af 32 mellem 15 og 32 ml/min) er hovedforklaringen |
| 3 | $FE_{Pi}$ vs. P-fosfat + de tre fænotyper | Det klinisk mest meningsfulde: kompensationen er heterogen, ikke GFR-determineret |
| 4 | Kreatinin-index: median 11,8, 7 under 10, $\rho = 0{,}45$ mod CrCl | Differentiel opsamlingskvalitet kan ikke udelukkes — og jeg har testet det |
| 5 | Gammel vs. ny formulering, side om side | De tre reviderede konklusioner |

Slide 4 og 5 er de vigtigste. En studerende, der selv finder en trussel mod sine egne fund, kvantificerer den og justerer sine konklusioner, demonstrerer noget, man ikke kan læse sig til.

### To ting du skal sige højt, før nogen spørger

1. *"Jeg har efterfølgende identificeret en indtastningsfejl i U-kreatinin for én deltager. Den påvirker rangen i baselinetabellen, men ikke medianen eller nogen analyse i specialet."* — **tjek om den 51,25 også står i dit publicerede range på `8,4 (46)`.** Range 46 = 51,25 − 5,1, så den er formentlig med.

2. *"Jeg brugte Pearson i mine efterberegninger, fordi jeg ikke havde adgang til Prism. Spearman er det korrekte valg og giver et svagere resultat — det rapporterer jeg her."* Ærlighed om testvalg er ikke en svaghed; at blive fanget i det er.

---

**Til sidst:** du er ikke i nærheden af at dumpe. Du har et gennemført studie, en diskussion der selv finder de fleste svagheder, og nu en supplerende analyse der viser, at du kan trykprøve dine egne resultater. Det, der afgør de sidste karaktertrin, er de tre tekstrettelser i abstract/konklusion — og at du til forsvaret kan fortælle den samlede historie roligt og præcist.

Send tallene, når du har kørt Spearman i Excel, så jeg kan tjekke mine håndberegninger mod dine.

**User - --**

tror du der havde været et stærkere signal hvis der var flere med 9 gfr?. jeg tror ikke helt jeg forstår den med  "P 
Pi
​
  står i nævneren. Rent matematisk vil højere plasmafosfat derfor trække $FE$ nedad, alt andet lige. At du alligevel finder en positiv sammenhæng betyder, at tælleren stiger mere end proportionalt — altså at den renale udskillelse opreguleres aktivt og kraftigere, end den passive matematiske kobling trækker den anden vej". Så hvad skal jeg sige ift "Lavere clearance → lavere kreatinin-index. Det er signifikant. Og det er præcis mønsteret, som både differentiel undersopsamling og ægte biologi forudsiger:" det her forstår jeg heller ikke Den sidste er vigtig: fordi CrCl∝U 
Cr
​
 /P 
Cr
​
  og index∝U 
Cr
​
 /vægt, deler de tælleren. En positiv korrelation er derfor delvis tautologisk, og testen er svækket.. jeg har forresten vedhæftet eGFR også i mit excel billede. men hvad betyder det her så for resultat "Men — og det er afgørende for fortolkningen: 4 af de 7 ekskluderede har CrCl < 18 ml/min, inklusive kohortens laveste (9,49). Jeg har altså ikke kun fjernet "dårlige opsamlinger" — jeg har fjernet den nederste ende af clearance-spektret og dermed forstærket range restriction.

Det er den ærlige konklusion, og den er faktisk stærk:. punkt 6 er nnokdet sværeste at forstå fordi jeg kan ikke se sammenhængen i alle de tal i mit excel dokument har jeg vedhæftet natrium balanccen ved foto for det var den der var mest signifiaknt, en af observationer er ikke med og derfor skal du bare ignorere det tomme felt! lav de beregninger du nævnte!

**Assistant - --**

**User - --**

tror du der havde været et stærkere signal hvis der var flere med 9 gfr?. jeg tror ikke helt jeg forstår den med "P
Pi
​
står i nævneren. Rent matematisk vil højere plasmafosfat derfor trække $FE$ nedad, alt andet lige. At du alligevel finder en positiv sammenhæng betyder, at tælleren stiger mere end proportionalt — altså at den renale udskillelse opreguleres aktivt og kraftigere, end den passive matematiske kobling trækker den anden vej". Så hvad skal jeg sige ift "Lavere clearance → lavere kreatinin-index. Det er signifikant. Og det er præcis mønsteret, som både differentiel undersopsamling og ægte biologi forudsiger:" det her forstår jeg heller ikke Den sidste er vigtig: fordi CrCl∝U
Cr
​
/P
Cr
​
og index∝U
Cr
​
/vægt, deler de tælleren. En positiv korrelation er derfor delvis tautologisk, og testen er svækket.. jeg har forresten vedhæftet eGFR også i mit excel billede. men hvad betyder det her så for resultat "Men — og det er afgørende for fortolkningen: 4 af de 7 ekskluderede har CrCl < 18 ml/min, inklusive kohortens laveste (9,49). Jeg har altså ikke kun fjernet "dårlige opsamlinger" — jeg har fjernet den nederste ende af clearance-spektret og dermed forstærket range restriction.

Det er den ærlige konklusion, og den er faktisk stærk:. punkt 6 er nnokdet sværeste at forstå fordi jeg kan ikke se sammenhængen i alle de tal i mit excel dokument har jeg vedhæftet natrium balanccen ved foto for det var den der var mest signifiaknt, en af observationer er ikke med og derfor skal du bare ignorere det tomme felt! lav de beregninger du nævnte! 

**Assistant - --**

# Jeg har regnet alle analyserne på dine data

Først en validering: min Spearman på natriumbalancen giver $\rho = -0{,}4724$, $p = 0{,}0084$ — **identisk med de −0,4726 og p=0,0084 der står i dit speciale**. Medianerne bliver +425 og −930,5, også identisk med dine. Min transskribering fra screenshottet er altså korrekt, og du kan regne med tallene nedenfor. Verificér dem alligevel selv i Excel.

---

## 1. Natriumanalyserne — resultaterne

### Hovedtabel

| Analyse | $n$ | Spearman $\rho$ | $p$ | 95 % CI |
|---|---|---|---|---|
| Na-balance (foto) vs. CrCl — **alle** | 30 | **−0,472** | **0,0084** | $[-0{,}71;\ -0{,}13]$ |
| Na-balance (foto) vs. CrCl — **uden flaggede** | 23 | **−0,331** | **0,12** | $[-0{,}65;\ +0{,}09]$ |
| Na-balance vs. kreatinin-index | 30 | **−0,335** | **0,070** | $[-0{,}62;\ +0{,}03]$ |

### Mann-Whitney, <20 vs. ≥20 ml/min

| | Alle | Uden flaggede |
|---|---|---|
| <20 ml/min | n=8, median **+425** | n=**4**, median +329 |
| ≥20 ml/min | n=22, median **−930** | n=19, median −936 |
| $p$ (eksakt) | **0,008** | **0,035** |

### Sådan skal det læses

**Den kontinuerte analyse mister signifikans** (−0,47 → −0,33, $p$ fra 0,008 til 0,12). Gruppesammenligningen holder nominelt ($p = 0{,}035$), **men <20-gruppen er nu på 4 personer.** Med $n=4$ er en p-værdi ikke fortolkelig, uanset hvad den siger. Rapportér den, men skriv at analysen er underpowered.

**Spearman-resultatet er det vigtigste**, fordi det bruger hele clearance-spektret i stedet for at smide information væk ved dikotomisering.

---

## 2. ⚠️ Og her er det, du skal kende: de tre mest positive natriumbalancer har de tre laveste kreatinin-index

| Na-balance | Kreatinin-index | CrCl | |
|---|---|---|---|
| **+2247,5** (højeste i kohorten) | 7,52 | 24,7 | 🚩 |
| **+1291,9** (næsthøjeste) | 7,45 | 15,7 | 🚩 |
| **+763** | **6,56** (lavest i kohorten) | 9,5 | 🚩 |

De tre deltagere med lavest kreatininudskillelse per kg har **alle** positiv natriumbalance — og to af dem har kohortens to mest ekstreme positive værdier. Det er ikke tilfældigt fordelt.

Derfor korrelationen $\rho = -0{,}335$ ($p = 0{,}070$) mellem kreatinin-index og natriumbalance: **lavere kreatininudskillelse → mere positiv natriumbalance.** Det er nøjagtig artefaktets fingeraftryk.

### Og flagningen er skæv mellem grupperne

| | Flaggede | Ikke-flaggede | Andel flagget |
|---|---|---|---|
| CrCl < 20 | 4 | 4 | **50 %** |
| CrCl ≥ 20 | 3 | 19 | **14 %** |

Fishers eksakte test: $p = 0{,}060$ (ensidet). Altså en **trend** mod, at deltagere med lav clearance oftere har mistænkelig opsamling — præcis din egen hypotese om, at "de sygere opsamler dårligere".

> **Det du skal sige:** *"Natriumfundet var sensitivt over for urinopsamlingskvalitet: korrelationen faldt fra −0,47 (p=0,008) til −0,33 (p=0,12) ved eksklusion af deltagere med kreatinin-index under 10 mg/kg/døgn. Kreatinin-index korrelerede desuden negativt med natriumbalancen (ρ=−0,34, p=0,07), og de tre laveste index i kohorten havde alle positiv natriumbalance. Differentiel opsamlingskomplethed kan derfor ikke udelukkes som medvirkende forklaring, og fundet bør betragtes som hypotesegenererende."*

Det er ikke et nederlag. **Det er præcis den slags selvkritisk trykprøvning, der løfter en karakter** — du har fundet en trussel mod dit eget fund, kvantificeret den, og justeret din konklusion. Det er kandidatniveau.

<details>
<summary><strong>Kreatinin-index: deskriptiv statistik og hvem der flagges (klik)</strong></summary>

| | Værdi |
|---|---|
| Median | **11,8 mg/kg/døgn** (0,105 mmol/kg) |
| IQR | 10,1–14,6 |
| Range | 6,6–20,3 |
| Antal < 10 mg/kg/døgn | **7 (22 %)** |
| Antal < 9 mg/kg/døgn | 4 |

Forventet ved alder 75: ♂ ≈ 15,3 og ♀ ≈ 13,3 mg/kg/døgn (Walser). Din median ligger ~20–25 % under.

**De 7 flaggede (index < 10):**

| Index | CrCl | Na-balance |
|---|---|---|
| 6,56 | 9,49 | +763 |
| 7,45 | 15,7 | +1291,9 |
| 7,52 | 24,7 | +2247,5 |
| 8,03 | 24,3 | −496 |
| 9,06 | 17,7 | −729 |
| 9,24 | 13,4 | +87 |
| 9,95 | 30,6 | −1197,6 |

**Til rapportering:** brug et kønsspecifikt kriterium i stedet for én grænse — fx ±30 % af forventet, altså ♂ < 10,7 og ♀ < 9,3 mg/kg/døgn. Du har både køn, alder og vægt.

**Lille ting at tjekke:** to deltagere har præcis samme natriumbalance (+839). Det kan være tilfældigt, men verificér at det ikke er en kopieringsfejl.

</details>

---

## 3. Tautologien — hvorfor index vs. CrCl ikke betyder, hvad det ser ud til

Du spurgte, hvad "delvis tautologisk" betyder. Her er det.

De to størrelser er:

$$\text{Kreatinin-index} = \frac{U_{Cr} \times 113}{\text{vægt}} \qquad\qquad \mathrm{CrCl} = \frac{U_{Cr} \times V}{P_{Cr} \times 1440}$$

**$U_{Cr}$ står i tælleren i begge.** Når to mål deler den samme variabel i tælleren, vil de korrelere positivt af rent regnemæssige grunde — uanset om der er nogen biologi.

Tænk på: "æbler per person" og "æbler per krone". Begge stiger, når antallet af æbler stiger. En positiv korrelation mellem dem fortæller dig ikke noget om forholdet mellem personer og kroner.

### Den rene test — og resultatet er godt nyt for dig

Jeg brugte din eGFR-kolonne. eGFR beregnes udelukkende fra **P**-kreatinin, alder og køn — den rører aldrig urinopsamlingen:

| Sammenligning | Spearman $\rho$ | $p$ |
|---|---|---|
| Kreatinin-index vs. **CrCl** | **+0,452** | 0,009 |
| Kreatinin-index vs. **eGFR** | **−0,207** | 0,25 |

**Fortegnet vender.** Den signifikante positive sammenhæng findes kun mod CrCl — altså kun der, hvor de deler $U_{Cr}$. Mod det uafhængige mål er der ingen positiv sammenhæng.

**Hvad du skal sige:**

> *"Kreatinin-index korrelerede positivt med kreatininclearance (ρ=+0,45), men dette er delvis tautologisk, da urin-kreatinin indgår i tælleren i begge mål. Mod eGFR — som er uafhængigt af urinopsamlingen — var sammenhængen ikke positiv (ρ=−0,21, ns). Der er derfor ikke evidens for, at deltagere med lavere nyrefunktion systematisk havde ringere opsamling."*

⚠️ **Nuance, du skal have med:** den negative sammenhæng mod eGFR er formentlig **muskelmasse-artefakten** — sarkopeni giver både lavt kreatinin-index og falsk *højt* eGFR (fordi P-kreatinin er lavt). Ingen af de to tests er altså helt rene. Din bedste evidens er den direkte: index vs. natriumbalance ($\rho = -0{,}34$) og flagningsskævheden (50 % vs. 14 %).

---

## 4. Havde flere med GFR ~9 givet et stærkere signal? Ja — jeg har regnet på det

Kort svar: **sandsynligvis ja, og det kan kvantificeres.**

Din CrCl har SD = **8,2 ml/min**, men 39 % af den varians kommer fra én deltager (53,51 ml/min). Kun 3 af 32 ligger under 15 ml/min.

Med **range restriction correction**:

$$r_{\text{korrigeret}} = \frac{r \cdot (SD_u/SD_r)}{\sqrt{1 - r^2 + r^2(SD_u/SD_r)^2}}$$

Med $r = -0{,}32$ (din Pearson) og en tænkt kohorte jævnt fordelt 5–45 ml/min ($SD \approx 12$):

$$r_{\text{korrigeret}} \approx -0{,}44 \quad\Rightarrow\quad p \approx 0{,}012$$

Altså: **havde spredningen i clearance været bredere, ville dit $FE_{Pi}$-fund formentlig være blevet signifikant.** Det er et konkret, kvantitativt svar til dit oplæg — meget stærkere end "sample size var lille".

**To forbehold:**

1. Det er en **estimeret** korrektion. Den antager, at sammenhængen er lineær hele vejen ned, hvilket den formentlig ikke er (kompensationen har sandsynligvis et knæk).
2. Praktisk barriere: **prædialytiske stadie 5-patienter er et smalt vindue.** De starter dialyse. At rekruttere 15 med CrCl < 15 uden dialyse er svært i sig selv — nævn det som designbegrænsning, ikke bare som "jeg nåede ikke nok".

---

## 5. $P_{Pi}$ i nævneren — forklaret med tal

Se formlen:

$$FE_{Pi} = \frac{U_{Pi} \times P_{Cr}}{\boldsymbol{P_{Pi}} \times U_{Cr}}$$

$P_{Pi}$ (plasmafosfat) sidder i **nævneren**. Når man dividerer med et større tal, bliver resultatet mindre.

**Regneeksempel — samme urin, kun plasmafosfat ændres:**

| $P_{Pi}$ | Beregning | $FE_{Pi}$ |
|---|---|---|
| 1,0 | $\frac{14{,}4 \times 0{,}30}{1{,}0 \times 8{,}48}$ | 51 % |
| 1,5 | $\frac{14{,}4 \times 0{,}30}{1{,}5 \times 8{,}48}$ | 34 % |
| 2,0 | $\frac{14{,}4 \times 0{,}30}{2{,}0 \times 8{,}48}$ | 25 % |

Højere plasmafosfat → **lavere** $FE_{Pi}$, helt automatisk. Der er ingen fysiologi i det; det er division.

**Så du ville forvente en negativ korrelation mellem $FE_{Pi}$ og P-fosfat af ren matematik. Du fandt +0,33.**

Det betyder, at tælleren ($U_{Pi}$, urinudskillelsen) er steget **mere end proportionalt** med plasmafosfat — nok til at overvinde nævnerens nedadgående træk og vende fortegnet.

**Formuleringen:**

> *"Plasmafosfat indgår i nævneren i FE-beregningen og trækker derfor målet nedad ved stigende plasmakoncentration. At der alligevel observeres en positiv sammenhæng indikerer, at den renale fosfatudskillelse opreguleres kraftigere, end den matematiske kobling trækker den anden vej — foreneligt med aktiv FGF23- og PTH-medieret nedregulering af NaPi-transporterne."*

Det er en pointe, der viser, at du forstår dit eget mål frem for blot at have beregnet det.

---

## 6. Hvad eksklusionsresultatet på $FE_{Pi}$ betyder

Du spurgte, hvad det betyder, at 4 af de 7 flaggede sad i den nederste ende af clearance-spektret.

Da $FE_{Pi}$-korrelationen forsvandt (−0,17 → −0,03) ved eksklusion, gjorde jeg **to ting samtidig**:

| Hvad jeg fjernede | Konsekvens |
|---|---|
| Deltagere med mistænkelig opsamling | ✅ intenderet |
| Deltagere med **lavest clearance** (herunder 9,49) | ❌ utilsigtet |

Derfor kan resultatet ikke fortolkes entydigt. To lige gyldige læsninger:

- **"Fundet var artefakt"** — de dårlige opsamlinger drev det
- **"Fundet var ægte, men jeg fjernede signalet"** — den nederste ende af GFR-spektret er netop, hvor kompensationen ses

**Tallene kan ikke afgøre det.** Og det er faktisk den vigtigste erkendelse i hele forløbet:

> *"Kreatininclearance fungerer i dette design både som eksponeringsvariabel og som indikator for opsamlingskvalitet, fordi urin-kreatinin indgår i begge. Deltagerne med lavest clearance er derfor uadskilleligt sammenfaldende med dem, der har lavest kreatinin-index. En stringent adskillelse ville kræve en uafhængig GFR-måling — fx iohexol-clearance — eller flere gentagne urinopsamlinger per deltager."*

**Det er dit stærkeste metodiske udsagn.** Det er en principiel designindsigt, ikke en undskyldning. Sæt den på et slide.

---

## 7. Attenuering — fjerde forsøg, nu med dine egne data

Du siger, du ikke kan se sammenhængen i dine Excel-tal. Det er fordi **attenuering ikke kan ses i tallene** — den handler om de målinger, du *ikke* har lavet. Lad mig vise det med noget, du faktisk har.

### Din egen dag-til-dag-analyse måler ikke det, du tror

På s. 51–52 tester du med Wilcoxon, om dag 1 vs. dag 3 og dag 2 vs. dag 3 adskiller sig, og finder $p = 0{,}22$ og $p = 0{,}80$. Du konkluderer: *"This indicates a consistent daily dietary intake among the participants."*

**Det gør den ikke.** Wilcoxon tester, om **gruppens median** flyttede sig. Den siger intet om, hvorvidt **individerne** var stabile.

Konkret eksempel med 4 deltagere:

| Deltager | Dag 2 | Dag 3 | Ændring |
|---|---|---|---|
| A | 600 | 1600 | **+1000** |
| B | 1600 | 600 | **−1000** |
| C | 800 | 1400 | +600 |
| D | 1400 | 800 | −600 |
| **Median** | **1100** | **1100** | **0** |

Wilcoxon giver $p = 1{,}0$ — "ingen forskel". Men **ingen enkelt person var stabil**; de svinger 600–1000 mg hver. Og din figur 5 antyder netop det: medianen flytter fra ~880 til ~1080 mg, mens de individuelle punkter spreder sig fra ~300 til ~1900 mg på **begge** dage.

**Det er den variation, der ødelægger din balance** — for balancen beregnes på ét individ, én dag.

### Hvad det gør ved korrelationen

$$r_{\text{observeret}} = r_{\text{sand}} \times \sqrt{\text{reliabilitet}}$$

Reliabilitet = hvor stor en andel af variationen i dine tal der er ægte forskelle mellem personer (frem for tilfældig dag-til-dag-støj).

| Sand sammenhæng | Reliabilitet 0,55 → du måler | Signifikant ved $n=30$? |
|---|---|---|
| 0,60 | 0,44 | ✅ |
| **0,40** | **0,30** | ❌ ($p \approx 0{,}11$) |
| 0,20 | 0,15 | ❌ |

**Læs den midterste linje.** Der kan være en reel sammenhæng på 0,40 i virkeligheden, og dit studie ville med stor sandsynlighed kalde den "ikke signifikant". Dit design er skruet mod nulfund. Derfor kan et nulfund ikke oversættes til "der er ingen sammenhæng".

### Og du kan faktisk måle din egen reliabilitet

Det her er den bedste analyse, du har tilbage — for du har allerede dataene:

<details>
<summary><strong>ICC på dine 3 WFR-dage — trin for trin (klik)</strong></summary>

For hver deltager med 3 dages WFR:

| Trin | Excel |
|---|---|
| 1 | `Personmiddel = AVERAGE(dag1:dag3)` |
| 2 | `Personvarians = VAR.S(dag1:dag3)` |
| 3 | `Within-varians = AVERAGE(alle personvarianser)` |
| 4 | `Between-varians = VAR.S(alle personmidler) - Within/3` |
| 5 | `ICC = Between / (Between + Within)` |

**ICC er reliabiliteten af én enkelt dags måling.** Så:

$$\text{Attenuering} = \sqrt{ICC}$$

Får du fx ICC = 0,45, betyder det, at en sand korrelation på 0,50 hos dig ville vise sig som $0{,}50 \times \sqrt{0{,}45} = 0{,}34$ — under signifikansgrænsen ved $n=30$.

**Så kan du sige, med dit eget tal:**

> *"Intraklassekorrelationen for fosforindtag over tre dage var X, hvilket betyder at en enkelt dags registrering attenuerer korrelationer med en faktor √X. En sand sammenhæng på 0,40 ville derfor forventes at fremstå som Y i mine data — under detektionsgrænsen ved n=30. Studiets nulfund kan derfor ikke tolkes som fravær af sammenhæng."*

Det er langt stærkere end at citere Stremke. **Det er dit eget datasæt, der forklarer sin egen begrænsning.** Og det giver dig samtidig et bedre svar på din dag-til-dag-analyse, hvis censor spørger.

</details>

---

## Opdateret prioritering

| # | Opgave | Tid |
|---|---|---|
| 1 | Verificér mine tal i Excel (Spearman −0,472 skal matche dit speciale) | 30 min |
| 2 | Skriv de reviderede formuleringer: natrium, "no real trend", alfacalcidol | 1 t |
| 3 | Kreatinin-index kønsspecifikt (♂<10,7 / ♀<9,3) og genkør | 45 min |
| 4 | **ICC på dine 3 WFR-dage** | 1 t |
| 5 | Slide om at CrCl er både eksponering og kvalitetsmål | 30 min |

---

**Den historie du skal fortælle til forsvaret:**

> Differencemålet er domineret af indtagsvariansen. Ratio og $FE_{Pi}$ er de rigtige endpoints, men $FE_{Pi}$ er ikke robust pga. range restriction — hvilket kan kvantificeres til, at et bredere clearance-spektrum formentlig havde givet signifikans. Natriumfundet er sensitivt over for opsamlingskvalitet, og de tre laveste kreatinin-index har alle positiv balance. Den principielle begrænsning er, at kreatininclearance i dette design fungerer både som eksponering og som opsamlingsmarkør. Konklusionerne er justeret, så de svarer til datas opløsningsevne.

Det er et forsvar, hvor du **fører** samtalen i stedet for at forsvare dig. Send tallene, når du har verificeret dem — særligt ICC'en er jeg nysgerrig på.