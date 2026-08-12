# Forsvarsspørgsmål fra "Claude-censoren" (julian / kritik)

*Kritikpunkter og spørgsmål fra claude-chat.md, omskrevet til censor-spørgsmål på samme niveau som i defense-q-flah731.md.*

Disse spørgsmål er de *skarpe, metodekritiske* spørgsmål, en censor kan stille ud over de "naturlige" spørgsmål i defense-q-flah731.md. De handler især om, hvorvidt dine tal og dine formuleringer bærer den vægt, du giver dem. Bag hvert spørgsmål står en note om, hvad censor leder efter.

---

## 1. Difference-målet – måler du reelt det, du tror?

**Spørgsmål:** Din "balance difference" er $B = \text{indtag} - \text{udskillelse}$. Din spredning i indtag er langt større end i udskillelse (fosforindtag: median ~1081 mg, IQR ~467–1654; U-fosfor: ~474 mg med et smallere spænd). Hvis jeg plotter $B$ mod indtaget, får jeg efter alt at dømme $\rho > 0{,}9$. Betyder det, at din primære analyse i praksis kun tester "korrelerer fosforindtaget med CrCl?" – hvilket du isoleret set finder til $\rho = 0{,}23$ (ns)? Er dine to analyser reelt én og samme analyse?

**Censor tester:** At du forstår, at difference-målet "arver" sin variation fra indtaget, og at det derfor er et dårligt mål for renal håndtering. Du skal kunne sige, at *ratio-målet* (som normaliserer for indtag) – og endnu bedre fraktionel ekskretion – er de mere informative endpoints, og at dette faktisk er et argument for dit design, som du bare ikke har trukket frem.

---

## 2. Ufuldstændig urinopsamling – den matematiske kobling

**Spørgsmål:** Din kreatininclearance regnes som $U_{Cr} \times V / (P_{Cr} \times 1440)$. Hvis en deltager kun opsamler en andel $k$ af døgnurinen, skaleres både $E$ og CrCl med præcis samme $k$ (fordi $U_{Cr} \times V$ står i tælleren i CrCl). Det betyder, at én og samme fejl trækker både din eksponeringsvariabel og din udfaldsvariabel ned. Kan du forklare, hvad dette gør ved dine to ikke-nul-fund – natrium $\rho = -0{,}47$ og fosfor-ratio $\rho = +0{,}31$ – som begge har præcis den signatur, som undersopsamling ville producere?

**Censor tester:** At du kan se den systematiske kobling: undersopsamling giver lav målt CrCl *og* lav målt udskillelse samtidig. Du skal kunne redegøre for de to mekanismer (balance stiger vs. CrCl falder → negativ korrelation; ratio falder vs. CrCl falder → positiv korrelation) og ikke blot afvise risikoen som "støj".

---

## 3. Kan du validere, at opsamlingerne var komplette?

**Spørgsmål:** Du har $U_{Cr}$ og vægt. Den forventede døgnudskillelse hos ældre er ~0,15–0,20 mmol/kg/døgn, men din median er ~0,11 mmol/kg/døgn (8,4 mmol/døgn ved 77 kg). Er den lave værdi udtryk for ægte sarkopeni hos ældre CKD-patienter, eller kan det være systematisk undersopsamling? Har du set på fordelingen – hvor mange deltagere ligger under fx 0,08 mmol/kg/døgn? Og hvad sker der med natriumfundet, hvis du ekskluderer de mest usandsynlige opsamlinger eller plotter balancen mod urinvolumen?

**Censor tester:** At du har lavet en empirisk kvalitetskontrol af dine urinprøver, i stedet for at antage at de er korrekte. Du skal kunne tale om kreatinin-index, dets fordeling, og at du har kørt en sensitivitetsanalyse uden de flaggede deltagere.

---

## 4. Natrium i steady state – er din konklusion for stærk?

**Spørgsmål:** I gruppen med CrCl $\geq 20$ ml/min er din natriumbalance −930 mg/døgn (foto) og −554 mg/døgn (WFR). At udskille ~1 g natrium mere end man indtager er fysiologisk umuligt i steady state – det fortæller, at indtaget er systematisk underestimeret (deltagerne registrerede ikke tilsat bordsalt). Betyder det, at dine absolutte balancetal ikke er fortolkelige, og at kun gruppeforskellen kan bruges? Og kan du forsvare formuleringen i abstract og konklusion om at "sodium retention occurred below 20 ml/min", når data egentlig kun understøtter, at den *apparente* balance var signifikant højere?

**Censor tester:** At du skelner mellem *absolute* og *relative* fund og ikke overfortolker. Du skal kunne moderere formuleringen til fx "deltagere med CrCl <20 ml/min havde signifikant højere apparent natriumbalance, forenelig med – men ikke bevis for – relativ natriumretention", og ærligt erkende, at de negative balancetal i ≥20-gruppen afslører systematisk underrapportering.

---

## 5. Hvorfor måler du ikke fraktionel fosfatekskretion (FE_Pi)?

**Spørgsmål:** Du har alle fire variable til at beregne $FE_{Pi} = (U_{Pi} \times P_{Cr})/(P_{Pi} \times U_{Cr})$. Målet er volumen-uafhængigt (volumen går ud), kræver slet ikke kostregistrering, og er det klassiske mål for netop den hypotese, du undersøger – "kompenserer de resterende nefroner?". Hvorfor er det ikke med? Og hvis du beregnede $FE_{Pi}$ mod CrCl på dine data i aften – hvad ville du forvente?

**Censor tester:** At du kender det måleinstrument, som ligger tættest på din kompensationshypotese, og at du kan forklare, hvorfor det ville være immunt over for opsamlingsproblemet fra spørgsmål 2-3. Svageste svar: at forsvare at det ikke er der. Stærkeste svar: at erkende at det er den vigtigste analyse, du mangler (og evt. rapportere, hvad du fandt).

---

## 6. Medicin som konfounder – diuretika og SGLT2i

**Spørgsmål:** 81 % af dine deltagere fik diuretika og 72 % SGLT2i. Men du behandler "diuretika" som én kategori, selvom thiazider *sænker* urin-calcium og loop-diuretika *øger* det – slået sammen kan de udligne hinanden. Og SGLT2-hæmmere giver natriurese og er associeret med stigning i P-fosfat, FGF23 og PTH samt fald i fraktionel fosfatudskillelse. Du laver Mann-Whitney på alfacalcidol – hvorfor ikke på diuretikatype og SGLT2i? Og er den ikke en hovedforklaring på flere af dine fosforresultater?

**Censor tester:** At du er opmærksom på medicin som konfounder i et studie om natrium- og calciumudskillelse. Du skal kunne skelne mellem thiazid og loop, teste SGLT2i eksplorativt (n=23 vs. n=9 er brugbart), og ikke lade "alle diuretika" skjule modsatrettede effekter.

---

## 7. Alfacalcidol-fundet – er det confounding by indication?

**Spørgsmål:** Du finder, at alfacalcidol-gruppen havde lavere 24-timers calciumudskillelse (24 vs. 42 mg, p=0,018), men grupperne adskilte sig samtidig signifikant på clearance (19,6 vs. 25,7 ml/min, p=0,03). Alfacalcidol ordineres netop til de mest fremskredne patienter. Kan effekten af behandlingen overhovedet adskilles fra effekten af nyrefunktionen i dette design – og holder din konklusion i resultatafsnittet om, at forskellen skyldes alfacalcidol?

**Censor tester:** At du genkender confounding by indication og ikke overfører en associeret forskel til en kausal påstand. Med n=9 kan du ikke justere dig ud af det – den ærlige formulering er, at behandlingseffekten ikke kan adskilles fra nyrefunktionens effekt i dette design.

---

## 8. Nulfund – er "no real trend" en holdbar konklusion?

**Spørgsmål:** I "Future perspectives" skriver du, at den manglende korrelation "suggest that there is no real trend towards an increasing retention as renal function declines". Men et nulfund er ikke evidens for fravær af effekt. Dine 95 % LoA for fosfor er ca. −500 til +350 mg/døgn, mens en klinisk katastrofal fosforretention er i størrelsesordenen 50–150 mg/døgn – dit måleinstrument er altså 3–10 gange grovere end signalet. Kan du angive 95 % CI for dine centrale $\rho$-værdier? Med n=30 og $\rho = 0{,}02$ er CI ca. $[-0{,}34;\ 0{,}38]$ – er "no real trend" så holdbart, eller bør det hedde "studiet kunne ikke udelukke klinisk relevant retention"?

**Censor tester:** At du skelner mellem "fandt ingen sammenhæng" og "der er ingen sammenhæng", og at du kan bruge konfidensintervaller til at vise, hvad dine data faktisk tillader. Det er en deduktions-fejlslutning at oversætte et underpowered nulfund til fravær af effekt – censor vil belønne en revideret formulering.

---

## 9. Calcium og vand – korrektionsfaktor eller bare spørg til væske?

**Spørgsmål:** Dit calciumfund er pænt metodisk arbejde: du observerer en konsistent bias, opstiller en hypotese om vand, tester den, og bekræfter den. Men du beregnede calcium fra drikkevand ud fra *postnummer × vandhårdhed × 7,17 mg/L* – altså fra volumen, ikke fra billeder. Fejlen ligger i, at deltagerne ikke fotograferede deres vandglas. Hvorfor foreslå en korrektionsfaktor, som antager konstant underrapportering på tværs af personer med vidt forskelligt væskeindtag, frem for den langt simplere løsning – at spørge til væskeindtag separat? Og er en korrektionsfaktor på −138 mg validerbar i et andet postnummer med anden vandhårdhed?

**Censor tester:** At du kan skelne mellem to løsninger og ikke bare klistrer en konstant på. Udbedringen ligger ikke i portionstørrelsesestimatet, men i manglende registrering af vand – og det er enkelt at løse direkte frem for med en kalibreret faktor, der måske ikke generaliserer.

---

## 10. Opsamlingskvalitet – er sammenhængen med clearance tautologisk?

**Spørgsmål:** Du finder, at kreatinin-index korrelerer positivt med kreatininclearance ($\rho = +0{,}45$, p=0,009) og tolker det som tegn på, at de sygeste opsamler dårligere. Men både index og CrCl har urin-kreatinin i tælleren – er den positive sammenhæng ikke delvist tautologisk? Hvad finder du, hvis du i stedet korrelerer kreatinin-index mod eGFR, som er uafhængig af urinopsamlingen?

**Censor tester:** At du kan adskille matematisk kobling fra ægte biologi. De to mål deler $U_{Cr}$, så deres korrelation kan opstå af rent regnemæssige grunde. Mod eGFR (som er beregnet fra P-kreatinin, alder og køn) er der ikke samme positive sammenhæng – hvilket understøtter, at deltagerne med lav nyrefunktion ikke nødvendigvis havde ringere opsamling.

---

## 11. Dag-til-dag-variation – hvad tester din Wilcoxon egentlig?

**Spørgsmål:** Du tester med Wilcoxon, om dag 1 vs. dag 3 og dag 2 vs. dag 3 adskiller sig, og finder høje p-værdier, som du tolker som "consistent daily dietary intake". Men Wilcoxon tester kun, om *gruppens median* flyttede sig – den siger intet om, hvorvidt *individerne* var stabile. Kan du adskille disse to fortolkninger? Og har du vurderet reliabiliteten (fx ICC) af en enkelt dags registrering – altså hvor meget din målemetode i sig selv attenuerer korrelationerne mod nul?

**Censor tester:** At du forstår forskellen mellem gruppe-stabilitet og individuel stabilitet, og at du kender begrebet *attenuering*: din balance bygger på én kostdag + én døgnurin, og tilfældig dag-til-dag-variation trækker korrelationer systematisk mod nul. Dermed er dit design "skruet mod nulfund", og du kan ikke vende et nulfund om til "der er ingen sammenhæng".

---

## 12. Klinisk anvendelse – hvad skal diætisten gøre anderledes?

**Spørgsmål:** En diætist på et nefrologisk ambulatorium læser dit speciale i morgen. Hvad skal hun gøre anderledes i praksis? "Metoden kan bruges på gruppeniveau" er ikke en klinisk anbefaling – diætister arbejder per definition på individniveau. Hvis IBDA ikke kan bruges individuelt til fosfor, protein og natrium, hvad er så dens plads?

**Censor tester:** At du kan oversætte dit forskningsresultat til konkret klinisk praksis og samtidig erkende grænsen: hvad metoden *kan* (fx supplere WFR ved restaurantbesøg, rangere lav/høj, vurdere calcium) og hvad den *ikke kan* (individuel præcision for fosfor, natrium, protein). Du skal have svaret i konklusionen, ikke kun i diskussionen.

---

## Kort oversigt

| # | Kerne | Det, censor vil høre |
|---|---|---|
| 1 | Difference-mål ≈ indtag | Ratio/FE er de rigtige endpoints |
| 2-3 | Urinopsamlings-kobling | Artefaktets signatur + empirisk kvalitetskontrol |
| 4 | Natrium steady state | Absolut vs. relativ – moderér formuleringen |
| 5 | FE_Pi mangler | Erkend analysen, der adresserer hypotesen direkte |
| 6-7 | Medicin-konfundere | Skel mellem stofklasser + confounding by indication |
| 8 | Nulfund ≠ fravær | Brug CI, "kunne ikke udelukke" |
| 9 | Calcium-vand | Løsning er at spørge til væske, ikke korrektionsfaktor |
| 10 | Kreatinin-index tautologi | Test mod eGFR |
| 11 | Dag-til-dag / attenuering | ICC, design skruet mod nulfund |
| 12 | Klinisk anvendelse | Konkret, individniveau |

---

## Formalia – mindre spørgsmål, som du bare skal kunne svare på

- Dit forskningsspørgsmål på s. 10 er ufuldstændigt ("Additionally Is there a correlation …"). Formuler det fulde spørgsmål mundtligt.
- Calciumbalancetabellen er mærket "Table 8", men teksten henviser til "table 7" – hvilken tabel er hvilken?
- Tabel 10: "r=8153" og "r=50,89" – kan du angive de korrekte værdier (0,8153 og 0,5089)?
- Hvorfor varierer n for >20-gruppen mellem 22 og 23 i forskellige afsnit?
- Calcium-balanceratio angives både som 0,20 (tabel) og 0,09 (tekst) – hvilken er rigtig?
- I abstract skriver du "a high but consistent bias (−138mg)" – er "high" retvisende for 138 mg af ~750 mg, og mener du ikke snarere "consistent"?
- I figur 6 og 7 er clearance plottet på y-aksen frem for x-aksen (konventionen er eksponering på x) – kan du forklare valget?
- Hvor mange deltagere var egentlig i stadie 5 – baseline siger 2 ved clearance, men subgruppeafsnittet og figurteksterne siger 3? Afklar.
- Referencelisten: Schober 2018a/2018b og St-Jules 2017a/2017b er hver sin artikel opført to gange – kan du rydde op?

**Censor tester:** At du kan stå inde for detaljerne i dit eget dokument og kan svare sikkert og uden at famle rundt i forskellige tal for det samme.
