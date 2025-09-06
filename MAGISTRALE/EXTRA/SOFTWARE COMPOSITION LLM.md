
# Principi per la Composizione del Software (PSC 2024/25)

Il corso "Principles for Software Composition" (PSC 2024/25, 375AA, 9CFU) è tenuto dal Professor Roberto Bruni e si concentra sulla formalizzazione dei linguaggi di programmazione e dei sistemi concorrenti.

## Organizzazione del Corso

- **Orario delle Lezioni**: Martedì 16:00-18:00 (A1), Giovedì 14:00-16:00 (C1), Venerdì 09:00-11:00 (L1).
- **Contatti**: Il Professor Bruni è disponibile per appuntamento, preferibilmente Martedì 14:00-16:00, o via email (bruni@di.unipi.it).
- **Materiale del Corso**: Disponibile sul didawiki (http://didawiki.di.unipi.it/doku.php/magistraleinformatica/psc/start).
- **Argomenti di Ricerca (Tesi)**: Approcci algebrici ai grafi strutturati, modellazione e analisi di sistemi biologici, regole di riscrittura per linguaggi reversibili, rilevamento di falsi allarmi nell'interpretazione astratta, linguaggi di specifica grafica, computazione quantistica e modelli di concorrenza.
- **Interazione in Classe**: Gli studenti sono incoraggiati a partecipare attivamente, a fare domande e a correggere il docente se necessario. Per le domande "soddisfa la proprietà?", le risposte previste sono "sì", "no", o "non lo so".
- **Attività del Corso**: Frequentare le lezioni, risolvere tutti gli homework (o almeno provarci), studiare i teoremi e superare l'esame.
- **Esame**: Basato su un esame orale finale. Tipicamente include 3-4 domande preliminari (lista disponibile su Microsoft Teams), un esercizio (simile a quelli scritti passati), la riproduzione di una delle dimostrazioni viste a corso, e alcune domande aggiuntive. Non ci sono esami intermedi o test di autovalutazione, ma esercizi "badge" possono essere inviati per riconoscimento.
- **Prerequisiti**: Teoria degli insiemi di base, numeri naturali, e concetti di congetture vs teoremi (es. numeri primi).

## Argomenti Chiave e Concetti

### 1. Sistemi Logici e Inferenza

I sistemi logici sono fondati su **regole di inferenza**, che hanno premesse (zero, una o molte) e una singola conclusione. Se le premesse sono valide, allora la conclusione è anch'essa valida. Le **derivazioni** in un sistema logico `R` sono rappresentate come alberi di prova, le cui foglie sono assiomi. Un **teorema** di `R` è una formula per cui è possibile trovare una derivazione.

**Esempio di Regola di Inferenza (Semantica Operazionale):** La regola per la moltiplicazione (`prod`) indica che se l'espressione `E0` valuta a `n0` e `E1` valuta a `n1`, allora `E0 * E1` valuta a `n0 * n1`.

```
(prod) E0 ⟶ n0   E1 ⟶ n1
        ----------------
        E0 ⌦ E1 ⟶ n  (dove n = n0 ⋅ n1)
```

### 2. Unificazione

L'**unificazione** è un processo che, dato un insieme di uguaglianze potenziali (es. `t1 = r1, ..., tn = rn`), cerca delle sostituzioni `σ` tali che applicando `σ` a tutti i termini, le uguaglianze diventino vere (`σ(ti) = σ(ri)`). L'obiettivo è ridurre iterativamente l'insieme delle uguaglianze tramite trasformazioni che preservano la soluzione, fino a trovare una soluzione o dimostrare che non ne esiste alcuna.

**Esempio di Applicazione di Regole SOS con Unificazione:** Per valutare un'espressione come `(1*2) * (3*4) ⟶ m`:

1. Si inizia con l'obiettivo `(1*2) * (3*4) ⟶ m`.
2. Si seleziona una regola, ad esempio la regola `(prod)`.
3. Si unifica l'obiettivo con la conclusione della regola, il che porta a nuovi sotto-obiettivi (e.g., `1*2 ⟶ n0` e `3*4 ⟶ n1`, con `m = n0 * n1`).
4. Si continuano le derivazioni per i sotto-obiettivi fino a ottenere i valori numerici, ad esempio `1*2 ⟶ 2` e `3*4 ⟶ 12`, e si calcola il risultato finale `m = 2 * 12 = 24` (l'esempio nel testo mostra `1*2 ⟶ 3` e `3*4 ⟶ 5`, che dà `15`come risultato, ma il principio è lo stesso).

### 3. Logica e Programmazione Logica (Prolog)

La programmazione logica, come in Prolog, si basa su **clausole di Horn** (e.g., `h :- b1, ..., bn`). La derivazione goal-oriented procede selezionando un obiettivo, trovando una clausola la cui testa unifica con l'obiettivo, applicando la sostituzione più generale (Most General Unifier, MGU), e sostituendo l'obiettivo con il corpo della clausola. La **Computed Answer Substitution (CAS)** è la composizione di tutte le sostituzioni applicate durante il processo.

**Esempio (Man-machine communication system, 1972):** Un sistema Prolog storico con 610 clausole poteva rispondere a domande sul testo "Ogni psichiatra è una persona. Ogni persona che analizza, è malata. Jacques è uno psichiatra a Marsiglia." Domande come "Jacques è una persona?", "Dove si trova Jacques?", "Jacques è malato?" ottenevano le risposte "Sì.", "A Marsiglia.", "Non lo so.".

### 4. Induzione (Matematica, Ben-fondata, per Regola)

L'induzione è una tecnica fondamentale per le dimostrazioni.

- L'**induzione matematica** è usata per dimostrare proprietà su numeri naturali (es. `∀n > 0. n^n ≥ n!`) o su sequenze definite ricorsivamente (es. `an = 2n − n− 1` per `a0 = 0, an+1 = 2an + n`).
- La **ricorsione ben-fondata** permette di definire funzioni su strutture ricorsive, garantendo terminazione. Un esempio è la funzione `vars` che restituisce l'insieme degli identificatori in un'espressione.
- L'**induzione per regola** (o induzione sulle derivazioni) è usata per dimostrare proprietà su sistemi definiti da regole di inferenza. Si dimostra che la proprietà vale per gli assiomi (casi base) e che è preservata dalle regole (casi induttivi). Se le premesse della regola godono della proprietà, allora la conclusione deve goderne anch'essa. Questo è usato, ad esempio, per dimostrare la determinacy delle espressioni booleane.

### 5. Semantica Operazionale e Denotazionale

I linguaggi di programmazione sono definiti dalla loro **sintassi**, dai **tipi**, dalla **pragmatica** (come usare le funzionalità) e dalla **semantica** (il significato dei programmi ben-tipati).

- La **semantica operazionale** descrive il significato di un programma in termini di come un'ipotetica macchina lo esegue. Può essere **small-step** (molti piccoli passi) o **big-step** (un singolo passo che rappresenta un'intera computazione). La big-step è solitamente più semplice e non può esprimere computazioni non terminanti.
- La **semantica denotazionale** mappa ogni costrutto del linguaggio a un'entità matematica (es. una funzione), fornendo un significato astratto e indipendente dall'esecuzione. Per i comandi, mappa stati a stati (potenzialmente indefiniti `S?`).
- **Equivalenza:** Due programmi sono **operazionalmente equivalenti** se hanno lo stesso comportamento osservabile. Si studia l'equivalenza simbolica tra programmi se la loro semantica è preservata. La **consistenza** tra semantica operazionale e denotazionale si prova dimostrando che le due formalizzazioni danno lo stesso risultato: **correttezza**(operazionale implica denotazionale) e **completezza** (denotazionale implica operazionale).

**Esempio (Semantica Denotazionale di `while`):** La semantica denotazionale del comando `while b do c` (`C[[while b do c]]`) è definita come il **punto fisso minimo** di una funzione `G_b,c : (S → S?) → (S → S?)`. `G_b,c(j) = λs. B[[b]](s) → j*(C[[c]](s)), s`. Per `w = while true do skip`, `G_true,skip(j) = j`, quindi il punto fisso minimo è la funzione `λs. ?S?` (sempre indefinito, indicando divergenza).

### 6. CPO e Punti Fissi

Un **CPO (Complete Partial Order)** è un insieme parzialmente ordinato `(D, ⊑D)` in cui ogni catena (`x0 ⊑ x1 ⊑ ...`) ha un **Least Upper Bound (LUB)**. Un CPO è uno strumento essenziale per la semantica denotazionale, specialmente per trattare la ricorsione e la divergenza.

- Una funzione `f: D → D` è **continua** se preserva i LUB delle catene.
- Il **teorema di Kleene** afferma che per ogni funzione continua `f` su un CPO, esiste un **punto fisso minimo**, dato da `fix(f) = ⋃n f^n(⊥D)` (dove `⊥D` è l'elemento bottom del CPO).
- L'**operatore di Conseguenze Immediate (ICO)**, `bR`, è un operatore che, se le regole hanno un numero finito di premesse, è continuo, e il suo punto fisso minimo `fix(bR)` è l'insieme di tutti i teoremi `IR`.

**Esempio di CPO:** L'insieme dei numeri naturali con l'ordinamento standard `(N, ≤)` **non** è un CPO se non include un elemento bottom o un elemento che funga da LUB per catene infinite. L'insieme `P(S)` (powerset di S) con l'ordinamento `⊆`(inclusione) è un CPO.

### 7. HOFL (Higher Order Functional Language)

HOFL è un linguaggio funzionale che supporta funzioni di ordine superiore, ricorsione e coppie.

- **Sintassi dei termini**: `x` (variabile), `n` (numero), `t0 op t1`, `if t then t0 else t1`, `(t0, t1)`, `fst(t)`, `snd(t)`, `λx. t`, `t0 t1` (applicazione), `rec x. t` (ricorsione).
- **Tipi**: `int`, `τ0 * τ1` (prodotto), `τ0 → τ1` (funzione).
- **Forme Canoniche**: I valori a cui i termini HOFL possono valutare; per `int` sono i numeri, per `τ0 * τ1` sono coppie `(t0, t1)` con `t0` e `t1` chiusi, per `τ0 → τ1` sono astrazioni lambda `λx. t` con `λx. t` chiuso.
- La **semantica operazionale** di HOFL valuta i termini chiusi e ben-tipati a una delle loro forme canoniche. La **semantica denotazionale** di HOFL interpreta i termini in domini CPO appropriati per ciascun tipo.
- **Consistenza HOFL**: Ci sono differenze tra la semantica operazionale (termini chiusi e tipabili, nessun ambiente, non congruenza, termini canonici) e denotazionale (termini tipabili, ambiente, congruenza, entità matematiche).

**Esempio (Termine HOFL che diverge):** `rec x. x` è un termine che non ha una forma canonica e diverge. La sua interpretazione denotazionale è l'elemento bottom del dominio corrispondente al suo tipo.

### 8. CCS (Calculus of Communicating Systems)

CCS è un'algebra di processi per modellare sistemi concorrenti.

- **Sintassi**: `nil` (processo inattivo), `x` (variabile di processo), `μ.p` (prefisso di azione), `p\L` (restrizione di canali), `p[φ]`(relabelling), `p+q` (scelta non deterministica/somma), `p|q` (composizione parallela), `rec x. p` (ricorsione).
- **Semantica Operazionale**: Definisce la relazione di transizione (es. `μ.p ⟶ μ p`, `p1 | p2 ⟶ μ p1' | p2` se `p1 ⟶ μ p1'`).
- **Bisimilarità Forte (`~`)**: Una relazione binaria `R` è una bisimilarità forte se ogni transizione di un processo `p` può essere mimata da un processo `q` (e viceversa), e i processi risultanti sono ancora in relazione `R`. La più grande bisimilarità forte è la **bisimilarità forte massima**, ed è un punto fisso di un operatore `Φ`.
- **Bisimilarità Debole (`≈`)**: Considera le transizioni `τ` (interne) invisibili. Un processo può mimare una sequenza di transizioni `τ` con una singola transizione `τ` (o nessuna).
- **HML (Hennessy-Milner Logic)**: Una logica modale per specificare proprietà di processi CCS, utilizzata per definire l'equivalenza logica.
- **Encoding di Linguaggi Imperativi in CCS**: È possibile modellare concetti imperativi come terminazione, variabili, sequenzialità e concorrenza in CCS usando canali dedicati (es. `done` per la terminazione, `x_r`, `x_w` per le variabili).
- **μ-calcolo**: Una logica temporale modale che estende HML con operatori di punto fisso (`μ` per il minimo punto fisso, `ν` per il massimo punto fisso) per esprimere proprietà di liveness e safety.

**Esempio (Bisimulazione):** Considerando `P = α.(τ.P' + β.P'')` e `Q = α.τ.Q' + α.β.Q''`. Il processo di calcolo della bisimulazione comporta l'iterazione di un operatore `Φ` che raffina le partizioni dei processi fino a distinguere quelli non bisimili.

### 9. Pi-Calculus

Una generalizzazione di CCS che permette la comunicazione di nomi di canali, supportando così la configurabilità dinamica della topologia della rete di comunicazione.

- **Convenzioni**: Omissione del `nil` finale, messaggi vuoti come prefissi CCS, comunicazione poliardica.

### 10. PEPA (Performance Evaluation Process Algebra)

PEPA è un'algebra di processi estesa per l'analisi delle prestazioni, che integra le algebre di processi (per la descrizione composizionale di sistemi complessi) con le **Catene di Markov a Tempo Continuo (CTMC)** (per l'analisi numerica).

- **Costruzione del Modello**: Concettualizzare il sistema come una catena di Markov, costruire la matrice generatrice infinitesimale, e risolvere le equazioni per derivare informazioni quantitative.
- **Cooperazione**: I processi cooperano tramite attività condivise (sincronizzazione multi-way). Il rate di un'attività cooperata dipende dai rate individuali dei processi partecipanti (e.g., `min(r_alpha(P), r_alpha(Q))`).

**Esempio (Produttore/Consumatore in PEPA):** Un sistema Produttore/Consumatore può essere modellato in PEPA, dove lo stato del sistema può essere denotato da `(Cons_i |[get] Buf_j |[put] Prod_k)`, indicando lo stato dei singoli componenti e le attività di sincronizzazione `get` e `put`. Dimenticando le azioni, si ottiene una CTMC.

## Soluzioni degli Esercizi

Questa sezione fornisce le soluzioni agli esercizi specifici presenti nei file sorgente, basandosi _esclusivamente_ sulle informazioni fornite. Se un esercizio non può essere risolto o richiede contesto esterno non presente nelle fonti, verrà indicato.

### Esercizi da "01 - inference - 2025.pdf"

**Ex. 3: Derivazioni goal-oriented** Per le query:

1. `sum(x, s(0), s(s(0)))`
2. `prod(s(s(0)), y, s(s(0)))`
3. `div(z, s(s(0)))`

Le regole logiche (G1, G2, G3) fornite non sono regole di `sum`, `prod`, `div` in un senso aritmetico diretto, ma piuttosto definizioni di relazioni generiche. Senza regole di inferenza specifiche per `sum`, `prod`, `div` che operano su `s(x)`(successore) e `0`, non è possibile fornire una derivazione concreta. Le regole date sono:

- `G1 def = {prod(s(x), y, s(z)) ?= prod(y, z, x)}`
- `G2 def = {pow(x, s(y), x) ?= pow(s(y), z, z)}`
- `G3 def = {div(x, s(y)) ?= div(z, x) , div(y, s(z)) ?= div(u, s(u))}`

Con queste definizioni, una derivazione "goal-oriented" cercherebbe di unificare la query con la testa di una di queste clausole.

1. **`sum(x, s(0), s(s(0)))`**: Nessuna delle clausole G1, G2, G3 ha `sum` come predicato nella testa. Pertanto, con le regole fornite, non è possibile derivare questa query.
    
2. **`prod(s(s(0)), y, s(s(0)))`**:
    
    - Tentiamo di unificare `prod(s(s(0)), y, s(s(0)))` con la testa di G1: `prod(s(x), y', s(z'))`.
    - Questo porterebbe a `s(x) = s(s(0))`, quindi `x = s(0)`.
    - E `s(z') = s(s(0))`, quindi `z' = s(0)`.
    - La variabile `y` nella query unifica con `y'` nella testa di G1.
    - La clausola G1 è `prod(s(x), y, s(z)) ?= prod(y, z, x)`.
    - Applicando la sostituzione `{x/s(0), z/s(0)}` alla parte destra `prod(y, z, x)`, otteniamo `prod(y, s(0), s(0))`.
    - Quindi, `prod(s(s(0)), y, s(s(0)))` si riduce a `prod(y, s(0), s(0))`. Senza ulteriori regole per `prod` o `s(0)`, la derivazione si fermerebbe qui.
3. **`div(z, s(s(0)))`**:
    
    - Tentiamo di unificare `div(z, s(s(0)))` con la testa di G3: `div(x, s(y))`.
    - Questo porterebbe a `x = z` e `s(y) = s(s(0))`, quindi `y = s(0)`.
    - La clausola G3 ha due sotto-obiettivi: `div(z, x)` e `div(y, s(z)) ?= div(u, s(u))`.
    - Applichiamo la sostituzione `{x/z, y/s(0)}`.
    - Il primo sotto-obiettivo diventa `div(z, z)`.
    - Il secondo sotto-obiettivo è `div(s(0), s(z)) ?= div(u, s(u))`. Questo richiede un'ulteriore unificazione.
    - Unificando `div(s(0), s(z))` con `div(u, s(u))`, otteniamo `u = s(0)` e `z = u`, quindi `z = s(0)`.
    - Quindi, per soddisfare il secondo sotto-obiettivo, `z` deve essere `s(0)`.
    - Il primo sotto-obiettivo, `div(z, z)`, con `z = s(0)`, diventa `div(s(0), s(0))`.
    - La derivazione completa è quindi possibile se `z = s(0)`.

**Ex. 4: Prova per induzione matematica che `∀n > 0. n^n ≥ n!`**

- **Base Case (n = 1)**: `1^1 ≥ 1!`. Questo significa `1 ≥ 1`, che è vero.
- **Inductive Hypothesis**: Assumiamo che per un certo `k > 0`, `k^k ≥ k!` sia vero.
- **Inductive Step**: Dobbiamo dimostrare che `(k+1)^(k+1) ≥ (k+1)!`. Sappiamo che `(k+1)! = (k+1) * k!`. Dal passo induttivo, `k! ≤ k^k`. Quindi, `(k+1)! ≤ (k+1) * k^k`. Ora, dobbiamo confrontare `(k+1)^(k+1)` con `(k+1) * k^k`. `(k+1)^(k+1) = (k+1) * (k+1)^k` Dobbiamo dimostrare che `(k+1)^k ≥ k^k`. Poiché `k+1 > k` e `k ≥ 1`, `(k+1)^k` cresce più velocemente di `k^k`. Più formalmente, `(k+1)^k = sum_{i=0 to k} C(k,i) * k^i * 1^(k-i) = k^k + C(k,1)*k^(k-1) + ... + 1`. Chiaramente, per `k ≥ 1`, `(k+1)^k > k^k`. Quindi, `(k+1)^(k+1) = (k+1) * (k+1)^k > (k+1) * k^k ≥ (k+1) * k! = (k+1)!`. Pertanto, `(k+1)^(k+1) ≥ (k+1)!` è vero.

**Ex. 5: Prova per induzione matematica che `∀n ∈ N. an = 2n − n− 1` per `a0 = 0, an+1 = 2an + n`**

- **Base Case (n = 0)**: `a0 = 2^0 - 0 - 1`. `a0 = 0`, `2^0 - 0 - 1 = 1 - 0 - 1 = 0`. Questo è vero.
- **Inductive Hypothesis**: Assumiamo che per un certo `k ∈ N`, `ak = 2k − k− 1` sia vero.
- **Inductive Step**: Dobbiamo dimostrare che `ak+1 = 2^(k+1) − (k+1)− 1`. Dalla definizione ricorsiva, `ak+1 = 2ak + k`. Sostituendo l'ipotesi induttiva per `ak`: `ak+1 = 2(2k − k− 1) + k` `ak+1 = 2^(k+1) − 2k − 2 + k` `ak+1 = 2^(k+1) − k − 2` Ora confrontiamo questo con la formula che vogliamo provare: `2^(k+1) − (k+1)− 1`. `2^(k+1) − (k+1)− 1 = 2^(k+1) − k − 1 − 1 = 2^(k+1) − k − 2`. Le due espressioni sono identiche. Pertanto, la proprietà è vera per `n+1`. Per induzione, `∀n ∈ N. an = 2n − n− 1`.

### Esercizi da "02 - properties-2025.pdf"

**Ex. 4: Trovare l'insieme S delle memorie `σ` tali che `⟨w, σ⟩ −̸→` per `w def = while x > y do (x := x+ 1 ; y := y − 1)` e provare usando la regola di inferenza per la divergenza.** Il comando `w` diverge se la condizione `x > y` è sempre vera e il corpo del `while` esegue infinitamente. La regola di inferenza per la divergenza di un `while` è:

```
(wh_div) ⟨b, σ⟩ ⟶ tt   ⟨c, σ⟩ ⟶ σ'   ⟨while b do c, σ'⟩ −̸→
           --------------------------------------------------
           ⟨while b do c, σ⟩ −̸→
```

In questo caso, `b` è `x > y` e `c` è `(x := x+ 1 ; y := y − 1)`. Perché `w` diverga, `x > y` deve essere inizialmente vero, e dopo ogni iterazione del ciclo, la nuova coppia `(x, y)` deve ancora soddisfare `x > y`, perpetuando il ciclo. Consideriamo una memoria `σ` dove `σ(x) = x_0` e `σ(y) = y_0`. Se `x_0 > y_0` è vero:

- La prima esecuzione di `c` modifica la memoria `σ` a `σ'`: `σ'(x) = x_0 + 1` e `σ'(y) = y_0 - 1`.
- Ora dobbiamo controllare se `σ'(x) > σ'(y)` è ancora vero. `x_0 + 1 > y_0 - 1` `x_0 - y_0 > -2` Poiché abbiamo iniziato con `x_0 > y_0`, sappiamo che `x_0 - y_0 ≥ 1`. Quindi `x_0 - y_0 > -2` sarà sempre vero. Quindi, per ogni memoria `σ` tale che `σ(x) > σ(y)`, la condizione `x > y` sarà sempre soddisfatta dopo ogni iterazione, e il ciclo `while`non terminerà mai. L'insieme `S` delle memorie `σ` per cui `⟨w, σ⟩ −̸→` è: `S = {σ | σ(x) > σ(y)}` La prova per induzione sulla struttura della derivazione di divergenza mostrerebbe che se `σ(x) > σ(y)`, si può sempre applicare la regola `wh_div` perché `⟨x > y, σ⟩ ⟶ tt` e `⟨(x := x+ 1 ; y := y − 1), σ⟩ ⟶ σ'` porta a una `σ'` che ancora soddisfa la condizione `x > y`, permettendo una ricorsione infinita nella prova di non terminazione.

**Ex. 5: Provare la determinacy delle espressioni booleane per induzione sulle regole.** La determinacy di un'espressione `b` significa che se `⟨b, σ⟩ ⟶ v1` e `⟨b, σ⟩ ⟶ v2`, allora `v1 = v2`. Si prova per induzione sulla struttura delle espressioni booleane o per induzione sulle regole di derivazione della loro valutazione. Useremo l'induzione sulle regole, come suggerito.

**Predicato:** `P(d) = ∀v1, v2. (d = ⟨b, σ⟩ ⟶ v1 ∧ d = ⟨b, σ⟩ ⟶ v2) ⇒ v1 = v2` (cioè, il risultato della valutazione di `b` in `σ` è unico).

**Casi base (Assiomi):**

- **`true` e `false`**:
    - `⟨true, σ⟩ ⟶ tt` (assioma). Se `⟨true, σ⟩ ⟶ v1` e `⟨true, σ⟩ ⟶ v2`, allora `v1` deve essere `tt` e `v2` deve essere `tt`. Quindi `v1 = v2`.
    - `⟨false, σ⟩ ⟶ ff` (assioma). Allo stesso modo, `v1 = ff` e `v2 = ff`, quindi `v1 = v2`.

**Casi induttivi (Regole):**

- **Negazione (`¬b'`):**
    
    - Regola: `⟨b', σ⟩ ⟶ ff / ⟨¬b', σ⟩ ⟶ tt` (e viceversa per `tt`).
    - Supponiamo `⟨¬b', σ⟩ ⟶ v1` e `⟨¬b', σ⟩ ⟶ v2`.
    - Questo implica che ci sono due derivazioni per `¬b'`.
    - Ciascuna derivazione deve avere come premessa una derivazione per `b'` (e.g., `⟨b', σ⟩ ⟶ v_b`).
    - Per l'ipotesi induttiva, `P(⟨b', σ⟩ ⟶ v_b)` è vera, quindi `v_b` è unico.
    - Se `⟨b', σ⟩ ⟶ tt`, allora `⟨¬b', σ⟩ ⟶ ff`. Se `⟨b', σ⟩ ⟶ ff`, allora `⟨¬b', σ⟩ ⟶ tt`.
    - Poiché `v_b` è unico, il risultato di `¬b'` è anche unico. Quindi `v1 = v2`.
- **Confronto Aritmetico (`a0 cmp a1`):** (dove `cmp` è `<, ≤, =, ≠, >, ≥`)
    
    - Regola: `⟨a0, σ⟩ ⟶ n0, ⟨a1, σ⟩ ⟶ n1 / ⟨a0 cmp a1, σ⟩ ⟶ n0 cmp n1`.
    - Supponiamo `⟨a0 cmp a1, σ⟩ ⟶ v1` e `⟨a0 cmp a1, σ⟩ ⟶ v2`.
    - Questo implica che esistono derivazioni per `⟨a0, σ⟩ ⟶ n0` e `⟨a1, σ⟩ ⟶ n1` per entrambe le valutazioni di `a0 cmp a1`.
    - Per l'ipotesi induttiva (assumendo la determinacy delle espressioni aritmetiche, che è un prerequisito implicito o una prova separata), `n0` e `n1` sono unici.
    - Poiché `n0` e `n1` sono unici e l'operazione `cmp` è una funzione deterministica, `n0 cmp n1` è unico. Quindi `v1 = v2`.
- **Operatori Booleani Binari (`b0 bop b1`):** (es. `∧, ∨`)
    
    - Regola: `⟨b0, σ⟩ ⟶ v0, ⟨b1, σ⟩ ⟶ v1 / ⟨b0 bop b1, σ⟩ ⟶ v0 bop v1`.
    - Supponiamo `⟨b0 bop b1, σ⟩ ⟶ v1` e `⟨b0 bop b1, σ⟩ ⟶ v2`.
    - Per l'ipotesi induttiva, `v0` e `v1` sono unici.
    - Poiché `v0` e `v1` sono unici e l'operazione `bop` è deterministica, `v0 bop v1` è unico. Quindi `v1 = v2`.

In tutti i casi, la determinacy delle premesse implica la determinacy della conclusione. Poiché tutti i casi base sono deterministici, per induzione, tutte le valutazioni di espressioni booleane sono deterministiche.

**Ex. 6: (Incompleto) Let `b` be a boolean expression and `c` a command. Consider the command.** Questa è una frase incompleta e non specifica un esercizio da risolvere.

### Esercizi da "03 - poset-2025.pdf"

**Ex. 1: Definire con ricorsione ben-fondata la funzione `vars` che, data un'espressione aritmetica `a`, restituisce l'insieme degli identificatori che appaiono in `a`. Poi, provare per induzione sulle regole che `∀a ∈ Aexp, ∀σ ∈ Σ, ∀n ∈ Z. ⟨a, σ⟩ → n implies ∀σ′. ( (∀y ∈ vars(a). σ(y) = σ′(y)) ⇒ ⟨a, σ′⟩ → n )`.**

**Definizione di `vars(a)` (ricorsione ben-fondata sulla struttura di `a`):**

- `vars(n) = ∅` (per un numero `n`)
- `vars(x) = {x}` (per un identificatore `x`)
- `vars(a0 op a1) = vars(a0) ∪ vars(a1)` (per un'operazione binaria `op`)

**Prova per induzione sulle regole:** **Predicato `P(d)`**: Se `d` è una derivazione `⟨a, σ⟩ → n`, allora `∀σ′. ( (∀y ∈ vars(a). σ(y) = σ′(y)) ⇒ ⟨a, σ′⟩ → n )`.

**Casi base (Assiomi):**

- **`⟨n, σ⟩ → n` (per un numero `n`):**
    - `vars(n) = ∅`.
    - La premessa `∀y ∈ vars(n). σ(y) = σ′(y)` è `∀y ∈ ∅. σ(y) = σ′(y)`, che è vacuamente vera.
    - La conclusione `⟨n, σ′⟩ → n` è sempre un assioma, quindi è vera.
    - `P(⟨n, σ⟩ → n)` è vero.
- **`⟨x, σ⟩ → σ(x)` (per un identificatore `x`):**
    - `vars(x) = {x}`.
    - La premessa `∀y ∈ vars(x). σ(y) = σ′(y)` significa `σ(x) = σ′(x)`.
    - La conclusione `⟨x, σ′⟩ → σ′(x)`. Poiché `σ(x) = σ′(x)`, allora `⟨x, σ′⟩ → σ(x)`.
    - `P(⟨x, σ⟩ → σ(x))` è vero.

**Casi induttivi (Regole):**

- **`⟨a0 op a1, σ⟩ → n` (dove `n = n0 op n1`):**
    - Deriva dalle premesse `d0 = ⟨a0, σ⟩ → n0` e `d1 = ⟨a1, σ⟩ → n1`.
    - `vars(a0 op a1) = vars(a0) ∪ vars(a1)`.
    - Assumiamo che `P(d0)` e `P(d1)` siano veri.
    - Sia `σ′` tale che `∀y ∈ vars(a0 op a1). σ(y) = σ′(y)`.
    - Questo implica `∀y ∈ vars(a0). σ(y) = σ′(y)` e `∀y ∈ vars(a1). σ(y) = σ′(y)`.
    - Per `P(d0)`, `⟨a0, σ′⟩ → n0`.
    - Per `P(d1)`, `⟨a1, σ′⟩ → n1`.
    - Dalla regola `(op)`, possiamo derivare `⟨a0 op a1, σ′⟩ → n0 op n1`.
    - Poiché `n0 op n1 = n`, la conclusione è `⟨a0 op a1, σ′⟩ → n`.
    - `P(⟨a0 op a1, σ⟩ → n)` è vero.

Per induzione sulle regole, la proprietà `P(d)` vale per tutte le derivazioni di espressioni aritmetiche.

**Ex. 2: Definire con ricorsione ben-fondata la funzione `vars` che, dato un comando, restituisce l'insieme degli identificatori che appaiono sul lato sinistro di qualche assegnazione. Poi, provare per induzione sulle regole che `∀c ∈ Com, ∀σ, σ′ ∈ Σ`.** Questo esercizio è incompleto, manca la proprietà da dimostrare. Fornisco solo la definizione di `vars(c)` per il lato sinistro delle assegnazioni.

**Definizione di `vars(c)` (ricorsione ben-fondata sulla struttura di `c`):**

- `vars(skip) = ∅`
- `vars(x := a) = {x}`
- `vars(c0 ; c1) = vars(c0) ∪ vars(c1)`
- `vars(if b then c0 else c1) = vars(c0) ∪ vars(c1)`
- `vars(while b do c) = vars(c)`

### Esercizi da "05 - hofl-2025.pdf"

**Ex. 1: Determinare il tipo del termine HOFL `t def = rec x. ((λy. if y then 0 else 0) x)`. Quindi calcolare la sua forma canonica (lazy).**

- **Determinazione del tipo:** Sia `τ` il tipo di `x`. Dalla regola `rec x. t : τ` se `x : τ ⊢ t : τ`. Quindi `x : τ ⊢ ((λy. if y then 0 else 0) x) : τ`. Sia `τ_fun = (τ_arg → τ_res)` il tipo di `(λy. if y then 0 else 0)`. L'applicazione `f x` ha tipo `τ_res` se `f : τ_arg → τ_res` e `x : τ_arg`. Quindi, `x : τ_arg` e `τ_res = τ`. Analizziamo `(λy. if y then 0 else 0)`: Sia `y : τ_y`. Il termine `if y then 0 else 0` ha tipo `int` (poiché `0 : int`). Quindi `y` deve essere di tipo `int` affinché la condizione `if y` abbia senso (se `y` è int, si assume una conversione a booleano, o che `y` sia un booleano in contesti più stretti). Dato che `0` è int, `y` deve essere `int`. Quindi `(λy. if y then 0 else 0)` ha tipo `int → int`. Questo implica `τ_fun = int → int`. Per l'applicazione `((λy. if y then 0 else 0) x)`: `x` deve avere il tipo dell'argomento della funzione, quindi `x : int`. Il tipo del risultato dell'applicazione è `int`. Quindi, `τ = int`. Il tipo di `t` è `int`.
    
- **Calcolo della forma canonica (lazy):** `t = rec x. ((λy. if y then 0 else 0) x)` Per la semantica operazionale di `rec`: `rec x. t ⟶ t[rec x. t / x]`. `t ⟶ ((λy. if y then 0 else 0) t)` Ora dobbiamo valutare l'applicazione `((λy. if y then 0 else 0) t)`. Per la semantica operazionale di `λ` applicato: `(λx. t0) t1 ⟶ t0[t1/x]`. `((λy. if y then 0 else 0) t) ⟶ (if t then 0 else 0)[t/y]` Questo è `if t then 0 else 0`. Per valutare `if t then 0 else 0`, dobbiamo valutare `t`. Ma `t` si espande a `if t then 0 else 0`ricorsivamente. Questo è un ciclo infinito, il termine diverge. Quindi, la forma canonica (lazy) è `?D_int` (l'elemento bottom del dominio degli interi), che rappresenta la divergenza.
    

**Ex. 2: Determinare il tipo del termine HOFL `map def = λf. λx. ((f fst(x)), (f snd(x)))`. Quindi calcolare le forme canoniche (lazy) dei termini `t1 def = map (λz. 2× z) (1, 2)` e `t2 def = fst (map (λz. 2× z) (1, 2) )`.**

- **Determinazione del tipo di `map`:** Sia `f : τ_f`. Sia `x : τ_x`. `fst(x) : τ_fst` e `snd(x) : τ_snd`, dove `τ_x = τ_fst * τ_snd`. `f fst(x)` implica `f : τ_fst → τ_res_f`. `f snd(x)` implica `f : τ_snd → τ_res_f`. Quindi `τ_fst = τ_snd`. Sia `τ_elem = τ_fst = τ_snd`. Allora `f : τ_elem → τ_res_f`. E `x : τ_elem * τ_elem`. Il risultato è una coppia `(τ_res_f, τ_res_f)`. Quindi `map : (τ_elem → τ_res_f) → ( (τ_elem * τ_elem) → (τ_res_f * τ_res_f) )`.
    
- **Calcolo della forma canonica (lazy) di `t1`:** `t1 = map (λz. 2× z) (1, 2)` `λz. 2× z` ha tipo `int → int`. Quindi `τ_elem = int` e `τ_res_f = int`. Il tipo di `map` in questo caso è `(int → int) → ((int * int) → (int * int))`.`t1 = (λf. λx. ((f fst(x)), (f snd(x)))) (λz. 2× z) (1, 2)` Applichiamo `map` a `(λz. 2× z)`: `⟶ λx. (((λz. 2× z) fst(x)), ((λz. 2× z) snd(x)))` Applichiamo il risultato a `(1, 2)`: `⟶ (((λz. 2× z) fst(1, 2)), ((λz. 2× z) snd(1, 2)))` Valutiamo `fst(1, 2)` che è `1`. Valutiamo `snd(1, 2)` che è `2`. `⟶ (((λz. 2× z) 1), ((λz. 2× z) 2))` Valutiamo `(λz. 2× z) 1` che è `2×1 = 2`. Valutiamo `(λz. 2× z) 2` che è `2×2 = 4`. `⟶ (2, 4)` La forma canonica (lazy) di `t1` è `(2, 4)`.
    
- **Calcolo della forma canonica (lazy) di `t2`:** `t2 = fst (map (λz. 2× z) (1, 2))` Abbiamo già calcolato che `map (λz. 2× z) (1, 2)` valuta a `(2, 4)`. `t2 = fst (2, 4)` `⟶ 2` La forma canonica (lazy) di `t2` è `2`.
    

**Ex. 3: Sia `(D,⊑D)` un CPO e `f : D → D` una funzione continua. Provare che l'insieme dei punti fissi di `f` è anch'esso un CPO (ordinato da `⊑D`).** Sia `F_f = {x ∈ D | f(x) = x}` l'insieme dei punti fissi di `f`. L'ordine su `F_f` è l'ordine ereditato da `D`, cioè `⊑D`. Dobbiamo dimostrare due cose:

1. `F_f` è un posetto: Poiché `⊑D` è un ordine parziale su `D`, lo è anche su qualsiasi sottoinsieme di `D`, quindi `F_f` è un posetto.
2. Ogni catena in `F_f` ha un LUB in `F_f`: Sia `C = {x_i}` una catena in `F_f`. Poiché `C` è una catena in `D` (e `D` è un CPO), `C` ha un LUB in `D`, sia `x* = ⋃x_i`. Dobbiamo dimostrare che `x* ∈ F_f`, cioè `f(x*) = x*`. Poiché `f` è continua, `f(x*) = f(⋃x_i) = ⋃f(x_i)`. Poiché ogni `x_i ∈ F_f`, per definizione `f(x_i) = x_i`. Quindi `f(x*) = ⋃x_i = x*`. Pertanto, `x*` è un punto fisso di `f`, e `x* ∈ F_f`. Inoltre, `x*` è il LUB di `C` in `F_f` perché è il LUB di `C` in `D` e appartiene a `F_f`. Conclusione: `(F_f, ⊑D)` è un CPO.

### Esercizi da "2025-02-18 - 01 - Intro.pdf"

**Ex. 1 (e 2025-02-18 - 02 - Semantics.pdf, Ex. 1): DO NOT ask questions, write a `while` loop equivalent to `repeat c until b`.** Questo non è un esercizio da risolvere nel contesto di questa richiesta, ma un'attività didattica in classe. La soluzione tipica è `c; while (¬b) do c`.

**Ex. 2: `p := 0; x := 2; while (…………………………………………………………) do { if ( n%x == 0 ) then { p := x; } else { x := x + 1; } }` (Trova il più piccolo divisore non unitario `p` di `n>1`).** Questo è uno snippet di codice da completare. Il ciclo `while` dovrebbe continuare finché `x` non è un divisore di `n` e `p` non è stato ancora trovato (o `x` non ha superato `n`). Soluzione proposta per la condizione `while`: `(n%x != 0 && x <= n)` o `(p == 0 && x <= n)` se `p` è usato per segnalare il risultato. Più specificamente: `while (n%x != 0 && x*x <= n)` per ottimizzazione, ma la versione semplice è `while (n%x != 0 && x < n)`.

**Ex. 3: `i := length(a)-1; while ( i>0 && n!=a[i] ) do { i := i-1; }` (Trova l'indice `i` dell'ultima occorrenza di `n` in `a`).** Questo è uno snippet di codice che cerca l'ultima occorrenza di `n` in un array `a`. La condizione del `while` `(i>0 && n!=a[i])` è corretta per cercare all'indietro.

**Sample Exam Questions:**

- **What is a complete partial order?** Un **Complete Partial Order (CPO)** è un insieme parzialmente ordinato `(D, ⊑D)` tale che ogni catena `x0 ⊑ x1 ⊑ x2 ⊑ ...` in `D` ha un **Least Upper Bound (LUB)** in `D`.
- **What are the rules of the type system of HOFL?** Il sistema di tipi di HOFL definisce la validità dei termini e assegna loro un tipo. I tipi (`τ`) sono `int`, `τ0 * τ1` (tipo prodotto), e `τ0 → τ1` (tipo funzione). Le regole includono:
    - `x : τ` (le variabili hanno un tipo dal contesto)
    - `n : int` (i numeri interi sono di tipo `int`)
    - `t0 : int, t1 : int / t0 op t1 : int` (operazioni su interi)
    - `t : int, t0 : τ, t1 : τ / if t then t0 else t1 : τ` (condizionale)
    - `t0 : τ0, t1 : τ1 / (t0, t1) : τ0 * τ1` (coppie)
    - `t : τ0 * τ1 / fst(t) : τ0` (prima proiezione)
    - `t : τ0 * τ1 / snd(t) : τ1` (seconda proiezione)
    - `x : τ0 ⊢ t : τ1 / λx. t : τ0 → τ1` (astrazione lambda)
    - `t1 : τ0 → τ1, t0 : τ0 / t1 t0 : τ1` (applicazione di funzione)
    - `x : τ ⊢ t : τ / rec x. t : τ` (ricorsione)
- **How is iteration achieved in CCS?** In CCS, la ricorsione (che è il meccanismo per l'iterazione) è ottenuta tramite il costrutto `rec x. p` (o `x` se `x` è definito ricorsivamente altrove, come in `P = α.P`). La regola di inferenza per la ricorsione è `p[rec x. p/x] ⟶ μ q / rec x. p ⟶ μ q`, il che significa che un processo ricorsivo si comporta come il suo corpo con l'occorrenza della variabile di ricorsione sostituita dal processo stesso. Un esempio è `rec x. (α.x)` che continuamente esegue `α`.
- **Why only positive normal forms are considered in the mu-calculus?** Il μ-calcolo utilizza operatori di punto fisso `μ` (least fixpoint) e `ν` (greatest fixpoint). La "positività" si riferisce al fatto che la variabile del punto fisso (`x` in `μx.P`o `νx.P`) deve apparire all'interno della formula `P` sotto un numero pari di negazioni. Questo assicura che l'operatore di punto fisso sia **monotono** e quindi **continuo**, garantendo l'esistenza di un punto fisso minimo e massimo per il teorema di Kleene. Se la variabile appare sotto un numero dispari di negazioni (forma non positiva), la funzione associata potrebbe non essere monotona, e quindi non vi è garanzia dell'esistenza di punti fissi. Il testo non esplicita questa ragione, ma accenna solo a "Why only positive normal forms are considered in the mu-calculus?" come domanda d'esame.

### Esercizi da "2025-02-18 - 02 - Semantics.pdf"

**Ex. 1: (Ripetizione) Write a `while` loop that "is equivalent" to the following programming construct `repeat c until b`.** Come sopra, `c; while (¬b) do c`.

**Ex. 3: Expressions with variables.** Questo è solo un titolo di sezione, non un esercizio specifico da risolvere.

### Esercizi da "2025-03-07 - 06 - Equivalence.pdf"

**Ex. `p M` (programma per sommare divisori): `x := 3; s := 1; while x 6= s do (...)`** Questo è un programma che calcola la somma dei divisori propri di `x` quando `x` è pari a 2. Non c'è una domanda specifica su cui fare una dimostrazione o calcolo.

**Ex. `w1 ?⇠o p2`** `w1` e `p2` sono comandi simili ma non identici, `w1` non è definito in questo estratto, `p2` manca l'inizializzazione di `x`. La relazione `?⇠o` non è definita negli estratti, quindi non è possibile rispondere a questa query.

### Esercizi da "2025-03-07 - 07 - Recursion.pdf"

**Ex. `J ( rec y. y , rec z. z ) K⇢` e `J rec x. x K⇢` (Interpretazione Denotazionale HOFL)** Questi esercizi sono meglio compresi e risolti dopo aver introdotto la semantica denotazionale di HOFL (che è trattata in "2025-04-04 - 14 - HOFL Denotational.pdf").

- **`J rec x. x K⇢`**: Il termine `rec x. x` rappresenta una ricorsione che non fa alcun progresso. In semantica denotazionale, termini che divergono sono interpretati come l'elemento bottom `?D` del loro rispettivo dominio. Quindi, `J rec x. x K⇢ = ?[Z?→Z?]?` se `x` è di tipo `int → int`, o `?Dτ` per il tipo `τ` di `x`.
    
- **`J ( rec y. y , rec z. z ) K⇢`**: Questo è una coppia di due termini divergenti. L'interpretazione denotazionale di una coppia `(t0, t1)` è `(J t0 K⇢, J t1 K⇢)`. Poiché `J rec y. y K⇢ = ?Dτ0` e `J rec z. z K⇢ = ?Dτ1` (dove `τ0` è il tipo di `y`, `τ1` è il tipo di `z`), `J ( rec y. y , rec z. z ) K⇢ = (?Dτ0 , ?Dτ1)`. In un dominio `int * int`, sarebbe `(?D_int, ?D_int)`. Questo rappresenta una coppia di computazioni divergenti.
    

### Esercizi da "2025-03-11 - 08a - CPO.pdf"

**Ex. `(N, ≤)` PO? Total? Discrete? Flat?**

- **PO (Partial Order)?** Sì, `≤` è riflessiva, antisimmetrica e transitiva.
- **Total?** Sì, per ogni `n, m ∈ N`, `n ≤ m` o `m ≤ n`.
- **Discrete?** No, non ogni elemento copre solo se stesso. Per esempio, `0 ≤ 1`, ma `0` non copre `1` (non ci sono elementi tra loro).
- **Flat?** No, un ordine flat avrebbe solo `x ≤ y` se `x=y` o `x=⊥`. Qui `0 < 1 < 2`... non è flat.

**Ex. `(P(S), ⊆)` PO? Total? Discrete? Flat? (dove `S = {a, b, c}` è usato nell'esempio)**

- **PO?** Sì, `⊆` è riflessiva, antisimmetrica e transitiva.
- **Total?** No, ad esempio per `S = {a, b, c}`, `{a}` e `{b}` non sono confrontabili (`{a} <binary data, 1 bytes><binary data, 1 bytes> {b}` e `{b} <binary data, 1 bytes><binary data, 1 bytes> {a}`).
- **Discrete?** No, {a} ⊆ {a,b}.
- **Flat?** No, non è flat; ci sono relazioni di inclusione significative.

**Ex. `(N, =)` PO? Total? Discrete? Flat?**

- **PO?** Sì, `=` è riflessiva, antisimmetrica (se `x=y` e `y=x` allora `x=y`) e transitiva.
- **Total?** No, `2` e `3` non sono uguali, quindi non sono confrontabili con `=`.
- **Discrete?** Sì, ogni elemento copre solo se stesso. L'unico elemento comparabile con `x` è `x` stesso.
- **Flat?** Sì, è un ordine flat senza un elemento bottom (o dove ogni elemento è il proprio bottom in un certo senso).

**Ex. `(N ∪ {⊥}, ⊑)` dove `⊥` è l'elemento bottom e `⊑` è la relazione `(⊥, n)` per ogni `n` e `(n, n)` per ogni `n`. PO? Total? Discrete? Flat?**

- **PO?** Sì.
- **Total?** No, `1` e `2` non sono confrontabili.
- **Discrete?** No, `⊥ ⊑ 1`, `⊥ ⊑ 2`, ecc.
- **Flat?** Sì, la definizione data lo rende un dominio flat: tutti gli elementi sono confrontabili solo con se stessi o con l'elemento bottom.

**Ex. `{f, h, i, >}`. Upper bounds of `{b, c}`? lub? (Grafico non incluso ma implicito).** Basandosi sulla struttura del diagramma Hasse mostrato:

- Gli upper bounds di `{b, c}` sono `h` e `i`.
- Il LUB (`lub`) di `{b, c}` non esiste, poiché `h` e `i` sono entrambi upper bounds ma non sono confrontabili tra loro, quindi non c'è un minimo upper bound unico.

**Ex. `(N, ≤)`: la catena `0 ≤ 2 ≤ 4 ≤ ...` ha LUB? È completo?**

- Questa catena `C = {2n | n ∈ N}` non ha un LUB in `N` perché `N` non ha un elemento infinito. L'insieme degli upper bound è vuoto, e quindi non ha un minimo.
- `(N, ≤)` **non è un CPO** perché questa catena infinita non ha un LUB in `N`.

**Ex. `(N ∪ {⊥}, ≤)`: È completo? (ogni catena infinita ha LUB {⊥})**

- No, questo ordine non è completo (o CPO) in generale. Se la catena è solo `⊥ ≤ 0 ≤ 1 ≤ 2 ...`, il LUB non esiste per gli interi se non c'è un elemento "infinito" nel dominio. Se la catena è finita o si stabilizza, allora il LUB esiste. L'affermazione `lub = {⊥}` è vera solo per la catena che inizia da `⊥` e non ha altri elementi oltre `⊥`. La catena `0 ≤ 1 ≤ 2...` non ha LUB in `N ∪ {⊥}`. L'elemento `⊥` è il LUB solo se la catena è `⊥`.

**Ex. `(P(S), ⊆)`: È completo? (unione di catene)**

- Sì, `(P(S), ⊆)` è un CPO. Per ogni catena `C = {S_i | i ∈ N}` in `P(S)`, il suo LUB è `⋃_i∈N S_i` (l'unione di tutti gli insiemi nella catena), che è anch'esso un elemento di `P(S)`.

**Ex. `(N ∪ {11, 12}, ≤)`: È completo?**

- Consideriamo una catena infinita come `0 ≤ 1 ≤ 2 ≤ ...`. Questa catena non ha un LUB in `N ∪ {11, 12}`. Né 11 né 12 sono upper bounds di tutta la catena, e non c'è un elemento infinito.
- No, questo non è un CPO.

### Esercizi da "2025-03-11 - 08b - Kleene.pdf"

**Ex. Monotonicity for `(N ∪ {⊥}, ≤)`:**

- **`f(n) = n+1`**:
    - `f(⊥) = ⊥` (assumendo che le funzioni map `⊥` a `⊥`).
    - Se `n ≤ m`, allora `n+1 ≤ m+1`.
    - Sì, è monotona.
- **`f(n) = 2*n`**:
    - `f(⊥) = ⊥`.
    - Se `n ≤ m`, allora `2*n ≤ 2*m`.
    - Sì, è monotona.
- **`f(n) = n/2` (divisione intera)**:
    - `f(⊥) = ⊥`.
    - Se `n ≤ m`, allora `n/2` non è necessariamente `≤ m/2` nel senso di `N ∪ {⊥}` se `n` e `m` non sono dello stesso tipo (e.g. `n` è pari e `m` è dispari). Tuttavia, in generale, la divisione intera è monotona rispetto all'ordinamento naturale.
    - Sì, è monotona.

### Esercizi da "2025-03-18 - 08c - ICO.pdf"

**Ex. McCarthy 91 function.** La funzione McCarthy 91 è definita come:

```
f(n) = {
    1 if n <= 1
    f(n/2) if n > 1 and n%2 = 0
    f(3n + 1) otherwise
}
```

Questo è un esempio di funzione definita ricorsivamente, spesso usata per dimostrare concetti di ricorsione ben-fondata o punti fissi, ma non è un esercizio da risolvere qui in termini di computazione o prova.

### Esercizi da "2025-03-18 - 09 - Denotational IMP.pdf"

**Ex. Semantica di `w = while true do skip`** La semantica denotazionale di `w = while b do c` è definita come il punto fisso minimo `fix(G_b,c)` della funzione `G_b,c : (S → S?) → (S → S?)`. Per `w = while true do skip`:

- `b` è `true`, quindi `B[[true]](s) = tt` (true) per ogni stato `s`.
- `c` è `skip`, quindi `C[[skip]](s) = s`.
- La funzione `G_true,skip(j)` è definita come `λs. B[[true]](s) → j*(C[[skip]](s)), s`.
- Sostituendo i valori di `B[[true]]` e `C[[skip]]`: `G_true,skip(j)(s) = tt → j*(s), s` `G_true,skip(j)(s) = j*(s)` (poiché `tt` è vero, si prende il primo ramo) `G_true,skip(j)(s) = j(s)` (per definizione di `j*(s) = j(s)`quando `s ≠ ?`).
- Quindi, `G_true,skip(j) = j`.
- Questa `G_true,skip` è la funzione identità. Ogni funzione `j` è un punto fisso.
- Per il teorema di Kleene, cerchiamo il **least fixpoint** (punto fisso minimo).
- Il punto fisso minimo di una funzione identità in un CPO di funzioni `S → S?` (dove `S?` include l'elemento bottom `?`) è la funzione che mappa ogni stato a `?` (l'elemento bottom di `S → S?`).
- `fix G_true,skip = λs. ?S?`. Questo significa che il comando `while true do skip` non termina mai, producendo uno stato indefinito.

### Esercizi da "2025-03-27 - 12a - HOFL Types.pdf"

**Ex. Determinare il tipo di `rec rep. λn. λf. λx. if n then x else f (rep (n-1) f x)`** Sia `T` il tipo del termine `rec rep. ...`. Per la regola di `rec`, `rep : T ⊢ λn. ... : T`. Sia `T = τ_n → (τ_f → (τ_x → τ_res))`. Analizziamo il corpo `λn. λf. λx. if n then x else f (rep (n-1) f x)`.

- `if n then x else f (rep (n-1) f x)`:
    - La condizione `n` suggerisce che `n` è `int` (si assume che un `int` possa essere convertito in un booleano, dove `0`è falso e il resto vero, o è un int booleano come in Erlang).
    - `x` è il risultato nel ramo `then`.
    - `f (rep (n-1) f x)` è il risultato nel ramo `else`.
    - Quindi `x` e `f (rep (n-1) f x)` devono avere lo stesso tipo, sia `τ_res`.
    - `f` è applicato a `(rep (n-1) f x)`. Questo significa `f : τ_arg → τ_res`.
    - `rep` è applicato a `(n-1)`, `f`, `x`. Questo significa `rep : (τ_n → (τ_f → (τ_x → τ_res)))`.
    - `n-1` implica `n` è `int`.
    - `f` ha tipo `τ_f`. `x` ha tipo `τ_x`.
    - Quindi `rep` ha tipo `int → (τ_f → (τ_x → τ_res))`. Questo deve essere `T`.
    - Confrontando i tipi: `T = int → (τ_f → (τ_x → τ_res))`.
    - `τ_f = (τ_res → τ_res)` (se `f` è una funzione che manipola `x` e il risultato). Ma `f` è applicato a `(rep (n-1) f x)`, che ha tipo `τ_x` (se `rep` restituisce `τ_x`, allora `f` deve essere `τ_x -> τ_res`).
    - Questo termine è una versione del `repeat` funzionale. Se `n` è il contatore, `f` è la funzione da ripetere, `x` è il valore iniziale.
    - `rep (n-1) f x` ha tipo `τ_x` se `rep` ha tipo `int → (τ_f → (τ_x → τ_x))`.
    - Quindi `T = int → ( (τ_x → τ_x) → (τ_x → τ_x) )`.
    - La funzione `f` è di tipo `τ_x → τ_x`.
    - Il risultato del `if` è `τ_x`.
    - Quindi il tipo finale di `rec rep. ...` è `int → ( (τ_a → τ_a) → (τ_a → τ_a) )` per un tipo `τ_a` arbitrario. È una funzione polimorfa.

**Ex. Determinare il tipo di `λf . rec x . f x`** Sia `f : τ_f`. Sia `x : τ_x`. Il termine `rec x . f x` implica `x : τ_x` e `f x : τ_x`. Per `f x : τ_x`, `f` deve essere di tipo `τ_x → τ_x`. Quindi `τ_f = τ_x → τ_x`. Il tipo di `(λf . rec x . f x)` è `(τ_x → τ_x) → τ_x`. Questo è il tipo dell'**operatore di punto fisso di Y-combinatore**, che prende una funzione `f` e restituisce il suo punto fisso.

**Badge exercise: `t def = rec p. λx. (x,(p (x+2)))` (Guess the meaning).** Il termine `t` è definito ricorsivamente. Se applicato a `0` (`t 0`):

- `t 0 ⟶ (0, (p (0+2)))[t/p]` (sostituzione `rec p. ...` per `p`)
- `⟶ (0, (t 2))`
- `t 2 ⟶ (2, (t 4))`
- `t 4 ⟶ (4, (t 6))` E così via. Intuitivamente, `t 0` dovrebbe rappresentare la **lista infinita di tutti i numeri pari**: `(0, (2, (4, (6, ...))))`.

### Esercizi da "2025-03-28 - 12b - HOFL Operational.pdf"

**Ex. `t = rec x. x` (Compute its canonical form).** `t = rec x. x` Applichiamo la regola `Rec`: `rec x. t ⟶ t[rec x. t / x]`. `rec x. x ⟶ x[rec x. x / x]` `⟶ rec x. x` Il termine si riduce a se stesso. Questa è una **divergenza**. Non ha una forma canonica.

**Ex. `fact = rec f. λx. if x then 1 else x*(f (x-1))` (Compute its canonical form).**

- **Forma canonica di `fact`**: Per la regola `Rec`, `fact ⟶ (λx. if x then 1 else x*(fact (x-1)))`. Questo `λx. if x then 1 else x*(fact (x-1))` è una forma canonica (un'astrazione lambda). È la forma canonica di `fact`.
    
- **Valutazione di `(fact 1)`**: `fact 1 ⟶ (λx. if x then 1 else x*(fact (x-1))) 1` (usando la forma canonica trovata sopra) Applichiamo la regola di applicazione `(λx. t0) t1 ⟶ t0[t1/x]`: `⟶ (if x then 1 else x*(fact (x-1)))[1/x]` `⟶ (if 1 then 1 else 1*(fact (1-1)))` Valutiamo la condizione `if 1`. Assumendo `1` è "vero" in un contesto booleano implicito: `⟶ 1` Quindi, `(fact 1)` valuta a `1`.
    

### Esercizi da "2025-03-28 - 13a - Cartesian Domains.pdf" (e "2025-04-01 - 13a - Cartesian Domains.pdf")

**Ex. Smashed product: If `D = (D, ⊑D)` and `E = (E, ⊑E)` are CPOs, then `D ⨂ E` is a CPO.** Il prodotto schiacciato `D ⨂ E` (denotato spesso come `D ×_⊥ E` o semplicemente `D × E` in contesti dove l'elemento bottom è implicito e le coppie contenenti `⊥` sono "schiacciate" a `⊥_prod`) è definito come l'insieme delle coppie `(d, e)` dove `d ∈ D` e `e ∈ E`, più un nuovo elemento bottom `⊥_prod`. L'ordine è definito come `(d1, e1) ⊑_prod (d2, e2)` se `d1 ⊑D d2` e `e1 ⊑E e2`, e `⊥_prod ⊑_prod (d, e)` per ogni `(d, e)`.

Per dimostrare che `D ⨂ E` è un CPO:

1. **Parziale Ordine**: `⊑_prod` è riflessiva, antisimmetrica e transitiva se `⊑D` e `⊑E` lo sono.
2. **LUB delle Catene**: Sia `C = {(di, ei)}i∈N` una catena in `D ⨂ E`.
    - Se `C` contiene `⊥_prod`, allora `⊥_prod` è il suo LUB.
    - Se `C` non contiene `⊥_prod`, allora `C_D = {di}i∈N` è una catena in `D` e `C_E = {ei}i∈N` è una catena in `E`.
    - Poiché `D` e `E` sono CPO, `C_D` ha un LUB `d* = ⋃di` in `D`, e `C_E` ha un LUB `e* = ⋃ei` in `E`.
    - Il LUB della catena `C` in `D ⨂ E` è `(d*, e*)`.
    - Questo dimostra che `(D ⨂ E, ⊑_prod)` è un CPO.

### Esercizi da "2025-03-28 - Haskell Badge.pdf"

**Badge exercise (Hint: a powerset function can be helpful).** Questo è un esercizio di programmazione Haskell che richiede la scrittura di una funzione `powerset`. Non è possibile fornire una soluzione completa basandosi unicamente sul testo fornito, poiché richiede la conoscenza di Haskell e l'implementazione pratica.

### Esercizi da "2025-04-03 - 13c - Continuity Theorems.pdf"

**Ex. Provare che `curry(f)` è continua se `f` è continua.** Sia `f : D × E → F` una funzione continua. Vogliamo dimostrare che `curry(f) : D → (E → F)` è continua. `curry(f)(d)(e) = f(d, e)`. Per provare che `curry(f)` è continua, dobbiamo dimostrare che per ogni catena `C_D = {di}` in `D`, `curry(f)(⋃di) = ⋃curry(f)(di)`. Sia `d* = ⋃di`. `curry(f)(d*) = λe. f(d*, e) = λe. f(⋃di, e)`. Per ogni `e ∈ E`, la funzione `g_e(d) = f(d, e)` è continua (poiché `f` è continua e `e` è fisso). Quindi `f(⋃di, e) = ⋃f(di, e)`. Allora `curry(f)(d*) = λe. ⋃f(di, e) = ⋃(λe. f(di, e)) = ⋃curry(f)(di)`. Pertanto, `curry(f)` è continua.

**Ex. Provare che `uncurry(f)` è continua se `f` è continua.** Sia `f : D → (E → F)` una funzione continua. Vogliamo dimostrare che `uncurry(f) : (D × E) → F` è continua. `uncurry(f)(d, e) = f(d)(e)`. Per provare che `uncurry(f)` è continua, dobbiamo dimostrare che per ogni catena `C_DE = {(di, ei)}i∈N` in `D × E`, `uncurry(f)(⋃(di, ei)) = ⋃uncurry(f)(di, ei)`. Sia `(d*, e*) = ⋃(di, ei) = (⋃di, ⋃ei)`. `uncurry(f)(d*, e*) = f(d*)(e*) = f(⋃di)(⋃ei)`. Poiché `f` è continua, `f(⋃di) = ⋃f(di)`. Quindi `uncurry(f)(d*, e*) = (⋃f(di))(⋃ei)`. Poiché l'applicazione di funzione `(g)(x)` è continua rispetto a `g` e `x` (anche se il testo non lo dimostra esplicitamente, ma lo usa come `apply`), e `f(di)` è una catena di funzioni `(E → F)`, e `ei` è una catena in `E`. Allora `(⋃f(di))(⋃ei) = ⋃(f(di)(ei))` (Questa è una proprietà dell'applicazione in domini continui). `= ⋃uncurry(f)(di, ei)`. Pertanto, `uncurry(f)` è continua.

### Esercizi da "2025-04-04 - 14 - HOFL Denotational.pdf"

Questi esercizi sono già stati risolti nella sezione Esercizi da "2025-03-07 - 07 - Recursion.pdf".

### Esercizi da "2025-04-15 - 17a - CCS.pdf"

**Ex. LTS (Labeled Transition System) per `U = rec x. ((α.nil)|β.x)`** Gli estratti forniscono un LTS parziale per `U = rec x. (α|β.x)` e `U = α|β.U`, mostrando un ciclo infinito di transizioni. L'esercizio consiste nel disegnare un LTS, ma la soluzione parziale è già fornita nel testo. L'LTS di `U = rec x. (α.nil | β.x)` sarebbe:

- `U ⟶α nil | β.U`
- `U ⟶β α.nil | U` Il processo `nil | β.U` può poi fare `β` per diventare `nil | α.nil | U`. Il processo `α.nil | U`può fare `α` per diventare `nil | U`. Questo genera un grafico di stato infinito, come mostrato per esempi simili nelle fonti.

### Esercizi da "2025-04-29 - 18c - CCS bis as fix.pdf"

**Ex. Bisimulazione per `P = α.(τ.P + β.P')` vs `Q = α.τ.Q + α.β.Q`** Il testo fornisce una derivazione dettagliata del perché `P` e `Q` non sono bisimili (`P <binary data, 1 bytes><binary data, 1 bytes> Q`). Iniziamo con `R0 = {{P, Q, τ.P + β.P', τ.Q, β.Q}}` (tutti i processi sono nella stessa partizione).

1. **Passo 1 (α-transizioni):** `P ⟶α (τ.P + β.P')` mentre `Q ⟶α τ.Q` e `Q ⟶α β.Q`. Le destinazioni `τ.P + β.P'` e `τ.Q`, `β.Q` non sono inizialmente nella stessa partizione. Questo porta a un raffinamento. `R1 = {{P, Q}, {τ.P + β.P'}, {τ.Q}, {β.Q}}`. Qui, `P` e `Q` sono ancora nella stessa partizione, ma i loro stati successivi sono stati separati.
2. **Passo 2 (α-transizioni di `P` e `Q`):** `P` va a `[τ.P + β.P']` (partizione `R1_2`). `Q` va a `[τ.Q]` (partizione `R1_3`) e `[β.Q]`(partizione `R1_4`). Dato che `[τ.P + β.P']` è una partizione diversa da `[τ.Q]` e `[β.Q]`, `P` e `Q` sono ora distinguibili rispetto alle loro `α`-transizioni. Questo forza un ulteriore raffinamento: `R2 = {{P}, {Q}, {τ.P + β.P'}, {τ.Q}, {β.Q}}`.
3. **Terminazione:** Poiché `P` e `Q` sono ora in singole partizioni (singleton partitions), si può fermare. `P <binary data, 1 bytes><binary data, 1 bytes> Q` (P non è bisimile a Q).

**Ex. Bisimulazione per `P0` vs `Q0`** Il testo fornisce i passaggi per distinguere `P0` da `Q0`. Le definizioni di `P0, P1, P2, Q0, Q1, Q2` non sono esplicitate, ma il processo iterativo di raffinamento delle partizioni è mostrato.

- `R0 = {{P0, Q0, P1, Q1, Q2}}`.
- `R1 = {{P0, Q0, P1, Q1, P2}, {Q2}, {nil}}` (assumendo le definizioni di `P_i` e `Q_i` come nel diagramma).
- `R2 = {{P0, Q0}, {P1, P2}, {Q1}, {Q2}, {nil}}`.
- `R3 = {{P0}, {Q0}, {P1}, {P2}, {Q1}, {Q2}, {nil}}`. Poiché `P0` e `Q0` finiscono in partizioni singleton, `P0 <binary data, 1 bytes><binary data, 1 bytes> Q0`.

### Esercizi da "2025-05-06 - 20 - Weak.pdf"

**Ex. Bisimulazione Debole per `P = τ.(α.P + β.P)` vs `Q = α.Q + β.Q`** Il testo mostra in dettaglio come `P` e `Q` sono debolmente bisimili (`P ≈ Q`).

- `P` può fare una `τ`-transizione a `α.P + β.P'`.
- `Q` può fare una `α`-transizione a `Q'` o `β`-transizione a `Q''`.
- La relazione `R0 = {{P, Q, τ.P + β.P', τ.Q, β.Q}}` è una weak bisimulation.

Il punto chiave della bisimulazione debole è che le transizioni interne (`τ`) possono essere "saltate" o accorciate.

- `P ⟶τ α.P + β.P` (P può fare un τ, poi comportarsi come `α.P + β.P`)
- `Q` può direttamente fare `α` a `Q` o `β` a `Q`.
- La domanda è se `P` può mimare `Q` e viceversa.
    - `Q ⟶α Q`: `P` può fare `τ` (invisibile), poi il ramo `α` di `α.P + β.P`, portando a `P`. Poiché `P ≈ Q` (per ipotesi induttiva), questo "mimics".
    - `Q ⟶β Q`: Similmente, `P` può fare `τ` e poi `β`, portando a `P`.
    - `P ⟶τ α.P + β.P`: `Q` deve mimare una `τ`-transizione. `Q` può farlo rimanendo inerte (transizione `τ` vuota, `Q ⟶τ Q`). Poi `α.P + β.P'` deve essere debolmente bisimile a `Q`. E lo è per la struttura ricorsiva. Questa relazione è debolmente bisimile perché `τ` agisce come "rumore" o un passo interno che può essere ignorato.

### Esercizi da "2025-05-06 - 21 - CCS at work.pdf"

**Badge exercise: Write an interactive counter modulo 4 in CCS.** Questo è un esercizio di progettazione in CCS e richiede la scrittura di codice CCS. Non è possibile fornire una soluzione diretta dal testo fornito. Implicherebbe definire processi per i contatori (`C0`, `C1`, `C2`, `C3`) e transizioni (`inc`, `dec`) che, attraverso la composizione parallela e la restrizione, si comportano come un contatore modulo 4 interattivo.

### Esercizi da "2025-05-13 - 22b - mu calculus.pdf"

**Ex. Interpretazione di `μx. x`** `Jμx. xKρ = fix (λS. JxKρ[S/x])` (definizione di `μ` con il least fixpoint). `= fix (λS. S)`(poiché `JxKρ[S/x]` interpreta `x` come `S`). L'operatore `λS. S` è la funzione identità. Il punto fisso minimo della funzione identità è `∅` (l'insieme vuoto), perché `∅` è il bottom dell'insieme dei sottoinsiemi di stati (dominio dei predicati) e `f^n(⊥)`converge a `⊥` se `f` è l'identità. Quindi, `Jμx. xKρ = ∅`. Questa formula è equivalente a **false** (nessuno stato soddisfa la proprietà).

**Ex. Interpretazione di `νx. x`** `Jνx. xKρ = FIX (λS. JxKρ[S/x])` (definizione di `ν` con il greatest fixpoint). `= FIX (λS. S)`. Il punto fisso massimo della funzione identità è `V` (l'insieme di tutti gli stati), perché `V` è il top dell'insieme dei sottoinsiemi di stati (dominio dei predicati) e `f^n(T)` converge a `T` se `f` è l'identità. Quindi, `Jνx. xKρ = V`. Questa formula è equivalente a **true** (tutti gli stati soddisfano la proprietà).

**Ex. Interpretazione di `μx. p ∨ ⟨a⟩x` (come `EF p` - Eventually p)** Il testo fornisce una derivazione dettagliata per `Jμx. p ∨ ⟨a⟩xKρ` (scritto come `Jμx. p _∃xKρ`):

- Sia `F(S) = JpKρ ∪ {v | ∃w ∈ S. v ⟶a w}`.
- `S0 = ∅` (start from bottom for `μ`).
- `S1 = JpKρ ∪ {v | ∃w ∈ ∅. v ⟶a w} = JpKρ`.
- `S2 = JpKρ ∪ {v | ∃w ∈ JpKρ. v ⟶a w}`. Questo è l'insieme di stati che soddisfano `p` o possono raggiungere uno stato che soddisfa `p` in un passo `a`.
- `Sn = {v | v can reach a state in JpKρ in less than n moves}`.
- Il least fixpoint è `⋃n∈N Sn = {v | v can reach a state in JpKρ}`. Questa formula significa "eventualmente `p`", cioè `p` sarà vera in uno stato raggiungibile.

**Ex. Interpretazione di `νx. p ∧ [a]x` (come `AF p` - Always Eventually p) (non esplicitamente nell'estratto, ma implicito per parallelismo)** Il testo mostra `Jνx. p ∧ [a]xKρ` (`Jνx. p _∀xKρ`) per `AF p` come `FIX (λS. JpKρ ∩ {v | ∀w. v ⟶a w ⇒ w ∈ S})`.

- `S0 = V` (start from top for `ν`).
- `S1 = JpKρ ∩ {v | ∀w. v ⟶a w ⇒ w ∈ V} = JpKρ ∩ {v | v does not transition to a state not in V} = JpKρ`. (In realtà, `v ⟶a w ⇒ w ∈ V` è sempre vero, quindi `S1 = JpKρ`).
- `S2 = JpKρ ∩ {v | ∀w. v ⟶a w ⇒ w ∈ S1}`. Il greatest fixpoint è l'insieme di stati `v` tali che `p` è sempre vera lungo tutti i percorsi `a`, o `p` è sempre raggiungibile dopo una sequenza di `a`-transizioni.

### Esercizi da "2025-05-27 - 27 - PEPA.pdf"

**Last badge exercise: The final exam consists of 30 questions and 30 answers. Each student draws a bijective correspondence, 1 point for correct link, 0 for wrong. Students answer completely random. What is the probability of getting 1 point?** Questo è un problema di probabilità combinatoria.

- Il numero totale di modi per creare una corrispondenza biunivoca tra 30 domande e 30 risposte è `30!` (30 fattoriale), che è il numero di permutazioni. Questo è il denominatore dello spazio campionario.
- Per ottenere esattamente 1 punto, lo studente deve collegare correttamente esattamente 1 domanda alla sua risposta. Le restanti 29 domande devono essere collegate in modo errato alle restanti 29 risposte.
- Il numero di modi per scegliere 1 domanda da rispondere correttamente è `C(30, 1) = 30`.
- Per le restanti 29 domande e 29 risposte, nessuna deve essere corretta. Questo è un problema di **derangement**(disordinamento). Il numero di derangement di `n` elementi è `!n` o `D_n`.
- `!n = n! * sum_{k=0 to n} ((-1)^k / k!)`.
- Quindi, il numero di modi per ottenere esattamente 1 punto è `30 * !29`.
- La probabilità è `(30 * !29) / 30!`.
- `P = (30 * !29) / (30 * 29!) = !29 / 29!`.
- `!29 / 29! ≈ 1/e` (dove `e` è la base del logaritmo naturale, circa 2.718). La probabilità è approssimativamente `1/e`, che è circa 0.3679.

---