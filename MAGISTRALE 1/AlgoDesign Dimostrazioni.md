![[Pasted image 20250605232352.png]]

---

### Febbraio 24, 2025

**Algorithm Design: Topics and Tools**

- **Insegnamenti:**
    - Randomizzazione come strumento.
    - Attacco a problemi di "hardness" (difficoltà).
    - Algoritmi di approssimazione (grafi).
    - Algoritmi parametrizzati.
    - Teoria algoritmica dei giochi.
- **Randomizzazione:**
    - `random(a, b)`: sceglie `x ∈ [a..b]` uniformemente con probabilità `1/(b-a+1)`.
    - **Building block:** Concentration bounds.
    - **W.h.p. (With High Probability):** `pr = 1 - 1/n^c`, dove `n` è la dimensione dell'input e `c` è una costante.
    - **Variabile indicatrice:** Una variabile binaria che assume valore 1 se un evento accade, 0 altrimenti.

**Variabile Indicatrice e Valore Atteso**

- **Definizione:** Per un evento con probabilità `P`, `X = 1` se l'evento accade, `0` altrimenti.
- **Valore Atteso:** `E[X] = 1 * P + 0 * (1 - P) = P = Pr[X=1]`.
- **Linearità del Valore Atteso:** `E[X + Y] = E[X] + E[Y]`, anche se `X` e `Y` non sono indipendenti.

**Birthday Paradox (Esempio)**

- **Problema:** Calcolare il numero atteso di coppie di persone con lo stesso compleanno in un anno non bisestile (`n = 365` giorni) per `m` persone.
- **Variabile Indicatrice:** `Xij = 1` se le persone `i` e `j` hanno lo stesso compleanno, `0` altrimenti.
- **Probabilità:** `Pr[Xij = 1] = 1/n` (se ogni persona è nata in un giorno con probabilità uniforme).
- **Valore Atteso:** `E[Xij] = 1/n`.
- **Numero Totale Atteso di Coppie con lo Stesso Compleanno:**
    - `E[Σ Xij]` (somma su tutte le coppie `(i,j)` con `i < j`).
    - Per linearità del valore atteso: `E[Σ Xij] = Σ E[Xij] = (m choose 2) * (1/n)`.
    - `(m choose 2) = m(m-1)/2`.
    - Quindi, `E[Σ Xij] = m(m-1)/(2n)`.
    - **Esempio Numerico:** Se `n = 365` e `E[...] = 1`, si trova `m ≈ 27` persone.

---

### Febbraio 26, 2025

**Algorithmic Game Theory**

- Dr. Filippo Geraci.
- Date delle lezioni temporanee: Lunedì 3/3, Giovedì 6/3, Venerdì 7/3, Mercoledì 12/3, Giovedì 13/3, Venerdì 13/3.

**Esempio: Comprare Cuffie**

- `n` cuffie, numerate `1, ..., n`.
- `xi` rappresenta la "bontà" della cuffia `i`.
- Costo = 1.
- `X_i` = 1 se la cuffia `i` è la migliore.
- `E[costo] = E[Σ X_i] = Σ E[X_i] = Σ Pr[X_i = 1]`.
- L'ordine delle cuffie può influenzare il costo.
- `H = [x1, x2, ..., xn]` è una permutazione delle cuffie.
- La probabilità che `X_i = 1` (la cuffia `i` è la migliore) è `1/n`.
- Questo problema può essere legato alla somma armonica.

**Mescolamento (Shuffling)**

- **Obiettivo:** Permutare casualmente un array `A` di `n` elementi distinti in modo uniforme (ogni permutazione ha probabilità `1/n!`).
- **Algoritmo:**
    
    ```
    for i = 1 .. n-1 do:
        j = random(i .. n)
        Swap A[i] and A[j]
    ```
    
- **Esercizio (Usando Variabile Indicatrice):** Mostrare che questo ciclo `for` produce una delle `n!` permutazioni con probabilità `1/n!`.
    - **Hint:** Si può usare l'induzione su `i`.
    - In ogni passo `i`, l'elemento `A[i]` è scambiato con un elemento scelto uniformemente da `A[i..n]`. La probabilità che un certo elemento finisca in `A[i]` è `1/(n-i+1)`.
    - La probabilità che un prefisso `A[1..i]` sia una data permutazione è `1 / ((n-0) * (n-1) * ... * (n-i+1))`.
    - Il numero di permutazioni che estendono da `i` a `n` è `(n-i)!`.

**Randomized QuickSort (QS)**

- **Concetto:** Sceglie un valore pivot `v` uniformemente a caso tra gli `n` elementi dell'array `A`.
- **Algoritmo Randomizzato:** Il costo atteso dipende dalla probabilità specifica della randomizzazione.
- **Algoritmo Deterministico:** Il costo atteso è fisso.
- **Costo:** Il numero totale di confronti fatti dal QS randomizzato.
- `Xij = 1` quando `zi` e `zj` sono confrontati, `0` altrimenti.
- `zi` e `zj` sono confrontati al massimo una volta.
- **Costo Atteso `E[X]`:**
    - `E[Σ Xij] = Σ E[Xij] = Σ Pr[Xij = 1]`.
    - `Pr[Xij = 1]` = probabilità che `zi` e `zj` siano confrontati.
    - `zi` e `zj` sono confrontati se uno di essi è un pivot scelto casualmente nel sottoarray che li contiene.
    - In un sottoarray di `k` elementi, la probabilità che un elemento specifico sia scelto come pivot è `1/k`.
    - Questo porta a un costo atteso `O(n log n)`. Questo deriva dal fatto che `Pr[Xij = 1] = 2/(j-i+1)` per `zi < zj`. La somma di queste probabilità è legata alla somma armonica `Hn`.

---

### Febbraio 27, 2025

**Karp-Rabin Fingerprints / Rolling Hashing**

- **Obiettivo:** Verificare rapidamente l'uguaglianza tra file o stringhe utilizzando le "impronte digitali".
- **Funzione Fingerprint:** Una sequenza `S = s0s1...sn-1` può essere vista come un grande numero `s0 * b^0 + s1 * b^1 + ...`. `F(s) = S mod p` per un primo `p` casuale.
- **Errore 1-sided:** `F(s) = F(s')` ma `s ≠ s'` (falso positivo).
- **Probabilità di Errore:**
    - Se `K1 mod p = K2 mod p`, allora `p` divide `(K1 - K2)`.
    - Un numero `X` con `n` bit ha meno di `n` primi distinti che lo dividono.
    - Scegliendo `p` uniformemente e casualmente in un intervallo `[2 .. T]` con `T` sufficientemente grande, la probabilità di errore può essere resa arbitrariamente piccola (`≤ n/π(T)`). `π(T)` è la funzione di conteggio dei numeri primi. `π(T) ≈ T/ln(T)`.
- **Rolling Hashing:** Calcolare l'hash di una finestra scorrevole.
    - Esempio: `F(BRAC) = B*b^3 + R*b^2 + A*b^1 + C*b^0 mod p`.
    - Per calcolare `F(RACA)` da `F(BRAC)` in `O(1)` tempo: `F(RACA) = (F(BRAC) - B*b^3) * b + A mod p`.
- **String Matching (KR-Algorithm):** Trovare occorrenze di un pattern `P` (lunghezza `m`) in un testo `T` (lunghezza `n`).
    - **Baseline:** Confronto diretto: `O(n * m)` tempo.
    - **KR-Algorithm:**
        1. Calcola `p = F(P)`.
        2. Per `i = 1 .. n-m+1`: calcola `t = F(T[i..i+m-1])`.
        3. Se `p = t`, confronta `P` con `T[i..i+m-1]`.
    - Questo è un **Monte Carlo Algorithm**.
        - Tempo di esecuzione garantito `O(n+m)`.
        - Errore 1-sided (falsi positivi).
    - Per renderlo un **Las Vegas Algorithm** (nessun errore, tempo di esecuzione atteso):
        - Se `p = t`, si esegue un confronto carattere per carattere `P = T[i..i+m-1]`.
        - Tempo di esecuzione atteso `O(n + m + E[X] * m)` dove `X` è il numero di falsi positivi.
        - `Pr[X_i = 1]` (probabilità di falso positivo in una posizione) è `1/T`. La probabilità di almeno un errore è `n/T`.

---

### Marzo 3, 2025

**La Teoria della Scelta Razionale**

- **Assunto:** Un decisore sceglie l'azione migliore secondo le sue preferenze tra tutte le azioni disponibili.
- **Modello:**
    - Un insieme `A` di tutte le azioni possibili.
    - Una specifica delle preferenze del decisore.
- Il decisore è di fronte a un sottoinsieme di `A` e deve scegliere un singolo elemento, prendendolo come dato (non influenzato dalle sue preferenze).
- **Preferenze:** Il decisore sa quale azione preferisce o se le considera equivalenti per ogni coppia di azioni.
- **Funzione di Payoff (o Utilità) `u()`:** Rappresenta le preferenze associando un numero a ciascuna azione, in modo che azioni con numeri più alti siano preferite. `u(a) > u(b)` se e solo se `a` è preferita a `b`.
- **Informazione Ordinale:** Le funzioni di payoff trasmettono solo informazioni ordinali (es. `a` è preferito a `b` che è preferito a `c`), non "quanto" una sia preferita all'altra.
    - Esempio: `u(a)=0, u(b)=1, u(c)=100` significa solo `c` > `b` > `a`, non che `c` sia "molto" più preferito di `b`.
- **Consistenza:** Le scelte devono essere coerenti con la teoria.
    - Esempio di inconsistenza: Se si sceglie sempre `a` da `{a,b}`, ma a volte si sceglie `b` da `{a,b,c}`. La prima implicazione è `a` preferito a `b`. Allora, da `{a,b,c}` si dovrebbe scegliere solo `a` o `c`, mai `b`.

**Giochi Strategici**

- **Modello:** Interazione tra decisori, chiamati "giocatori".
- **Componenti (con preferenze ordinali):**
    1. Un insieme di giocatori.
    2. Per ogni giocatore, un insieme di azioni.
    3. Per ogni giocatore, preferenze sugli **action profiles** (combinazioni di scelte di tutti i giocatori).
- **Payoff Functions:** Conveniente per specificare le preferenze, ma hanno solo significato ordinale.
- **Simultaneità:** I giocatori scelgono le azioni "simultaneamente" (nessun giocatore è informato delle scelte altrui al momento della sua scelta). Il tempo è assente dal modello.

**Esempi di Giochi Strategici:**

- **Dilemma del Prigioniero**
    
    - **Giocatori:** Due sospetti.
    - **Azioni:** `{Quiet, Fink}` (restare in silenzio, tradire).
    - **Payoff (da migliore a peggiore per Suspect 1):**
        1. `(Fink, Quiet)` (3,0)
        2. `(Quiet, Quiet)` (2,2)
        3. `(Fink, Fink)` (1,1)
        4. `(Quiet, Fink)` (0,3)
    - La matrice dei payoff mostra: | Suspect 2 | Quiet | Fink | | :-------- | :---- | :--- | | **Suspect 1** | | | | Quiet | 2,2 | 0,3 | | Fink | 3,0 | 1,1 |
    - Modella situazioni in cui la cooperazione è vantaggiosa, ma ogni giocatore ha un incentivo a "free ride" (tradire).
- **Gioco dell'Inquinamento (Estensione del Dilemma del Prigioniero)**
    
    - `n` paesi, ognuno può scegliere di controllare l'inquinamento o meno.
    - Costo controllo: 3. Costo inquinamento altrui: 1 per paese.
    - Se `k` paesi non controllano: costo `k` per loro. Costo `k+3` per gli altri `n-k`.
    - Soluzione stabile (Nash Equilibrium): Nessun paese controlla (costo `n` per tutti). Se tutti controllassero, il costo sarebbe solo 3 per tutti.
- **Bach or Stravinsky (BoS)**
    
    - **Giocatori:** Due persone che vogliono uscire insieme.
    - **Azioni:** `{Bach, Stravinsky}`.
    - **Preferenze:** Preferiscono andare insieme, ma uno preferisce Bach, l'altro Stravinsky.
    - **Payoff (Player 1, Player 2):** | Player 2 | Bach | Stravinsky | | :-------- | :--- | :----------- | | **Player 1** | | | | Bach | 2,1 | 0,0 | | Stravinsky | 0,0 | 1,2 |
- **Matching Pennies**
    
    - **Giocatori:** Due persone, scelgono Testa o Croce simultaneamente.
    - **Regole:** Se uguali, Player 2 paga Player 1. Se diversi, Player 1 paga Player 2.
    - **Payoff (Player 1, Player 2):** | Player 2 | Head | Tail | | :-------- | :--- | :--- | | **Player 1** | | | | Head | 1,-1 | -1,1 | | Tail | -1,1 | 1,-1 |
    - Gioco puramente conflittuale.
- **Stag Hunt**
    
    - **Giocatori:** `n` cacciatori.
    - **Azioni:** `{Stag, Hare}` (Cacciare il cervo, cacciare la lepre).
    - **Regole:** Tutti cacciano il cervo -> condividono il cervo (preferito). Se uno caccia la lepre, il cervo scappa, e la lepre è sua (meno preferito).
    - **Preferenze (Player `i`):** Tutti Cervo (2) > Player `i` lepre (1) > Player `i` cervo ma almeno un altro lepre (0).
    - **Per `n=2`:** | Hunter 2 | Stag | Hare | | :-------- | :--- | :--- | | **Hunter 1** | | | | Stag | 2,2 | 0,1 | | Hare | 1,0 | 1,1 |

---

### Marzo 6, 2025

**Nash Equilibrium**

- **Concetto:** La migliore azione per un giocatore dipende dalle azioni degli altri. Un giocatore deve formare una **credenza** sulle azioni degli altri giocatori.
- **Assunzioni:**
    - La credenza deriva dall'esperienza passata nel gioco.
    - Ogni giocata è vista in isolamento.
    - Non c'è familiarità con il comportamento di avversari specifici.
    - L'azione è scelta secondo il modello di scelta razionale, data la credenza sugli altri giocatori.
    - La credenza di ogni giocatore sulle azioni degli altri è **corretta**.
- **Definizione:** Un profilo di azioni `a* = {a1*, ..., an*}` è un Nash Equilibrium se nessun giocatore `i` può migliorare scegliendo un'azione diversa da `ai*`, dato che tutti gli altri giocatori `j` aderiscono a `aj*`.
    - Equivalente: per ogni giocatore `i`, `u_i(a*) ≥ u_i(ai, a*[-i])` per ogni azione `ai` di `i`.
- **Significato:** Incarna una "norma sociale" stabile: se tutti gli altri vi aderiscono, nessun individuo desidera deviare da essa.
- I giocatori conoscono le preferenze altrui e considerano ciò che ogni giocatore può dedurre sull'azione altrui dalla loro razionalità.

**Esempi di Nash Equilibrium:**

- **Dilemma del Prigioniero**
    
    - Matrice dei payoff: | Suspect 2 | Quiet | Fink | | :-------- | :---- | :--- | | **Suspect 1** | | | | Quiet | 2,2 | 0,3 | | Fink | 3,0 | 1,1 |
    - `(Quiet, Quiet)`: NON è un NE. Se Player 2 sceglie Quiet, Player 1 preferisce Fink (3 > 2). Viceversa per Player 2.
    - `(Quiet, Fink)`: NON è un NE. Se Player 2 sceglie Fink, Player 1 preferisce Fink (1 > 0).
    - `(Fink, Quiet)`: NON è un NE (ragionamento simmetrico al precedente).
    - **(Fink, Fink)**: **È un Nash Equilibrium**. Se l'altro giocatore tradisce (Fink), la migliore risposta è tradire (Fink).
    - **Nota:** Il Nash Equilibrium non implica la migliore soluzione per tutti i giocatori (in questo caso, (Quiet, Quiet) è preferito da entrambi a (Fink, Fink)).
- **Bach or Stravinsky?**
    
    - Matrice dei payoff: | Player 2 | Bach | Stravinsky | | :-------- | :--- | :----------- | | **Player 1** | | | | Bach | 2,1 | 0,0 | | Stravinsky | 0,0 | 1,2 |
    - `(Bach, Stravinsky)` e `(Stravinsky, Bach)`: NON sono NE, perché è meglio andare insieme che dividersi.
    - **(Bach, Bach)** e **(Stravinsky, Stravinsky)**: **Sono Nash Equilibria**. Anche se i giocatori hanno opinioni diverse su quale sia migliore, una volta che sono d'accordo, nessuno ha incentivo a deviare.
- **Cooperation Game (Variante di Bach or Stravinsky?)**
    
    - Entrambi i giocatori preferiscono Bach a Stravinsky.
    - Matrice dei payoff: | Player 2 | Bach | Stravinsky | | :-------- | :--- | :----------- | | **Player 1** | | | | Bach | 2,2 | 0,0 | | Stravinsky | 0,0 | 1,1 |
    - `(Bach, Stravinsky)` e `(Stravinsky, Bach)`: NON sono NE.
    - **(Bach, Bach)** e **(Stravinsky, Stravinsky)**: **Sono ENTRAMBI Nash Equilibria**. Se sono in (Stravinsky, Stravinsky), nessun giocatore ha interesse a cambiare la sua azione.
- **Matching Pennies**
    
    - Matrice dei payoff: | Player 2 | Head | Tail | | :-------- | :--- | :--- | | **Player 1** | | | | Head | 1,-1 | -1,1 | | Tail | -1,1 | 1,-1 |
    - `(Head, Head)` e `(Tail, Tail)`: NON sono NE, Player 2 avrebbe convenienza a cambiare.
    - `(Head, Tail)` e `(Tail, Head)`: NON sono NE, Player 1 avrebbe convenienza a cambiare.
    - **Questo gioco NON ha Nash Equilibria**.
- **Stag Hunt**
    
    - Per `n=2` (Tabella): | Hunter 2 | Stag | Hare | | :-------- | :--- | :--- | | **Hunter 1** | | | | Stag | 2,2 | 0,1 | | Hare | 1,0 | 1,1 |
    - **(Stag, ..., Stag)**: **È un Nash Equilibrium**. Ogni giocatore preferisce questo profilo a quello in cui solo lui sceglie Hare.
    - **(Hare, ..., Hare)**: **È un Nash Equilibrium**. Ogni giocatore preferisce questo profilo a quello in cui solo lui caccia il cervo.
    - Nessun altro profilo è un Nash Equilibrium.

**Nash Equilibria Stretti vs. Non Stretti**

- **Stretto (Strict):** L'azione di equilibrio di ogni giocatore è **strettamente migliore** di tutte le sue altre azioni, date le azioni degli altri giocatori. `u_i(a*) > u_i(ai, a*[-i])`.
- **Non Stretto:** Un giocatore è indifferente tra la sua azione di equilibrio e qualche altra azione, date le azioni degli altri.
    - Esempio: | Player 2 | L | M | R | | :-------- | :- | :- | :- | | **Player 1** | | | | | T | 1,1 | 1,0 | 0,1 | | B | 1,0 | 0,1 | 1,0 |
    - Unico NE: `(T, L)`. Se Player 2 sceglie `L`, Player 1 è ugualmente felice scegliendo `T` o `B` (payoff 1 in entrambi i casi). Quindi `(T, L)` non è un equilibrio stretto.

**Best Response Functions**

- Quando il numero di giocatori o azioni è grande, ispezionare tutti i profili di azioni per trovare i NE può non essere fattibile.
- **Definizione `Bi(a-i)`:** Sottoinsieme di azioni che danno al giocatore `i` il payoff più alto, date le azioni degli altri giocatori `a-i`.
    - `B_i(a_{-i}) = {a_i ∈ A_i : u_i(a_i, a_{-i}) ≥ u_i(a_i', a_{-i}) ∀a_i' ∈ A_i}`.
- **Proposizione:** Un profilo di azioni `a*` è un Nash Equilibrium se e solo se l'azione di ogni giocatore è una best response alle azioni degli altri giocatori. Formalmente: `a_i* ∈ B_i(a*[-i])` per ogni giocatore `i`.
- **Algoritmo per trovare i Nash Equilibria:**
    1. Trovare la funzione di best response di ogni giocatore.
    2. Trovare i profili di azione `a_i* ∈ B_i(a*[-i])` per ogni giocatore `i`.

**Variante di Stag Hunt**

- Solo `m` cacciatori (`2 ≤ m < n`) devono cacciare il cervo per prenderlo.
- C'è ancora un solo cervo.
- Il cervo è condiviso solo dai cacciatori che lo catturano.
- Ogni cacciatore preferisce la frazione `1/n` del cervo a una lepre.
- L'algoritmo basato sulle best response riduce la necessità di valutare tutte le preferenze dei giocatori.

---

### Marzo 19, 2025

**Universal Hash Family**

- **Obiettivo:** Selezionare una funzione hash casualmente da una famiglia `H`.
- **Definizione:** Una famiglia `H` di funzioni hash `h: U -> [m]` (dove `U` è l'universo degli elementi, `[m] = {0, ..., m-1}`) è universale se per ogni `k1 ≠ k2 ∈ U`, `Pr[h(k1) = h(k2)] ≤ 1/m` quando `h` è scelta uniformemente a caso da `H`.
- **Esempio di Costruzione:** `hab(x) = ((a * x + b) % p) % m`.
    - `p` è un primo maggiore di `m`.
    - `a` è scelto da `{1, ..., p-1}` uniformemente a caso.
    - `b` è scelto da `{0, ..., p-1}` uniformemente a caso.
    - Scegliere una funzione `h` da questa famiglia è equivalente a scegliere una coppia di interi `(a,b)` casuali.
- **Perché è Universale?**
    - Si considera quando si ha una collisione: `hab(k1) % m = hab(k2) % m`.
    - Questo significa `(a*k1 + b) % p` e `(a*k2 + b) % p` differiscono per un multiplo di `m`.
    - Il numero di scelte di `a` e `b` che causano una collisione è al massimo `(p-1) * (p/m)`.
    - La probabilità di collisione è `(p-1) * (p/m) / (p*p) ≈ 1/m`.

**Perfect Hashing**

- **Obiettivo:** Una funzione hash `h: U -> [m]` dove non ci sono collisioni (`h(k1) ≠ h(k2)` per tutte le `k1 ≠ k2 ∈ S`, dove `S` è l'insieme di chiavi da memorizzare).
- È possibile quando si conosce l'insieme `S` da memorizzare.
- **Costruzione:**
    1. **Top Level:** Una funzione `h1: U -> [m]` dove `m = 2n`. Qui si accettano collisioni, ma in modo controllato.
    2. **Bottom Level:** Per ogni slot `j` nella tabella del top level, se `nj` chiavi sono mappate a `j`, si usa una funzione hash `hj: Sj -> [nj^2]` per mappare queste `nj` chiavi senza collisioni.
- **Prima Affermazione (Bottom Level):** `Pr(hj` è perfetta per `Sj)` `≥ 1/2`.
    - **Dimostrazione:** Si usano variabili indicatrici casuali `X_xy = 1` se `x` e `y` collidono con `hj(x) = hj(y)`.
    - `E[X] = Σ E[X_xy] = Σ Pr[X_xy=1]` (somma su tutte le coppie `x,y ∈ Sj`).
    - `Pr[X_xy=1] = 1/mj` dove `mj = nj^2`.
    - `E[X] = (nj choose 2) * (1/nj^2) = nj(nj-1)/(2nj^2) = (nj-1)/(2nj) < 1/2`.
    - Per la disuguaglianza di Markov: `Pr[X ≥ 1] ≤ E[X] < 1/2`.
    - Quindi `Pr[X=0]` (nessuna collisione, la funzione è perfetta) `>= 1 - E[X] > 1/2`.

---

### Marzo 20, 2025

**Concentration Bounds (Riepilogo)**

- **Markov's Inequality:** `Pr[X ≥ a] ≤ E[X]/a` per una variabile casuale non negativa `X` e `a > 0`.

**k-wise Limited Independence**

- Un insieme di variabili casuali `X1, ..., Xn` è `k`-wise indipendente se ogni sottoinsieme di `k` variabili è indipendente.
- Nel caso `k=2` (pairwise independent), usato per universal hashing `h(x) = ((ax+b)%p)%m`.
    - `Pr(h(x)=i \land h(y)=j) = Pr(h(x)=i) * Pr(h(y)=j)`.

**Cuckoo Hashing (Dettaglio dell'Implementazione)**

- Garantisce `O(1)` lookup nel caso peggiore (come perfect hashing) ma usando solo due funzioni hash `h1, h2`.
- Può essere aggiornato in `O(1)` tempo atteso ammortizzato.
- **Problema:** Cicli.
- **`Insert(x)`:**
    1. Se `T[h1(x)]` o `T[h2(x)]` è vuoto, memorizza `x` in quella entry.
    2. Altrimenti, sia `y` la chiave in una di queste entry occupate. `x` viene memorizzata al posto di `y`, e `y` diventa il nuovo `x` (cioè `y` è ora "senza casa").
    3. Questa operazione è tracciata come un percorso in un grafo `G = (V,E)`.
        - `V = {0, 1, ..., m-1}` (slot della tabella).
        - `E = {{h1(x), h2(x)} : x ∈ S}` (archi corrispondenti alle chiavi memorizzate).
        - L'inserimento di `x` corrisponde all'aggiunta dell'arco `{h1(x), h2(x)}`.
- **Tre situazioni possibili:**
    1. `x` trova presto un'entry vuota: `O(1)` tempo.
    2. Le posizioni `h1(x)` e `h2(x)` sono già occupate. L'inserimento segue un percorso in `G` che parte da `{h1(x), h2(x)}` e termina in una posizione vuota. Costo: `O(1 + L)` dove `L` è la lunghezza del percorso.
        - **Lemma:** La probabilità che un percorso abbia lunghezza `L` decresce esponenzialmente. `P(path length is L) ≤ (c/m)^(L/2)`.
        - Costo atteso: `O(1)`.
    3. Il percorso contiene un ciclo: si esegue un re-hashing in `O(n)` tempo.
        - **Probabilità di ciclo in G:** `Pr(cycle in G) = O(1/n)`. Questo perché un ciclo implica un percorso da `i` a `j` e poi di nuovo a `i`, che è raro.
        - Il numero atteso di re-hashing è `Σ i * p^i = O(1)` se `p` è la probabilità di re-hashing (che è piccola).

---

### Marzo 27, 2025

**Bloom Filters (Dettagli)**

- **Problema:** Memorizzare chiavi usando funzioni hash, ma senza memorizzare le chiavi stesse, per controllare l'appartenenza.
- **Impostazione:**
    - Insieme `S` di `n` chiavi.
    - Scegliere `k` funzioni hash universali `h1, ..., hk : U -> [m]`.
- **Costruzione:**
    1. `B =` vettore binario di `m` bit (tutti 0 inizialmente).
    2. Per ogni `x ∈ S`: per ogni `i ∈ [1..k]`, `B[hi(x)] = 1`.
    3. `S` può essere distrutto.
    4. Il processo è incrementale (si possono aggiungere nuove chiavi).
- **Query `x ∈ U`:**
    1. Restituisce `B[h1(x)] AND B[h2(x)] AND ... AND B[hk(x)]`.
- **Errore:** Falso positivo (query TRUE, ma `x ∉ S`). L'obiettivo è minimizzare questa probabilità.
- **Analisi della Probabilità di Errore:**
    - `Pr[B[q] = 0]` (una posizione `q` è 0). Per una singola funzione hash `hi`, `Pr[hi(x) = q] = 1/m`.
    - Per una singola chiave `x ∈ S`, la probabilità che `hi(x)` non sia `q` è `(1 - 1/m)`.
    - La probabilità che una posizione `q` rimanga 0 dopo che tutte le `n` chiavi di `S` sono state inserite (con `k` hash ciascuna) è `(1 - 1/m)^(kn)`.
    - Sia `p = 1 - (1 - 1/m)^(kn)` la probabilità che una posizione sia 1.
    - La probabilità di falso positivo per una query `x ∉ S` è `f = p^k = (1 - (1 - 1/m)^(kn))^k`.
    - **Minimizzazione di `f`:** Per `m` grande, `(1 - 1/m)^(kn) ≈ e^(-kn/m)`.
        - `f ≈ (1 - e^(-kn/m))^k`.
        - Per minimizzare `f`, si trova che il numero ottimale di funzioni hash `k = (m/n) * ln(2)`.
        - Sostituendo `k` in `f`, si ottiene `f ≈ (1 - e^(-ln2))^k = (1 - 1/2)^k = (1/2)^k`.
        - Oppure, `f ≈ (0.618)^k`.
- **Spazio:**
    - `m` bit per il vettore `B`.
    - Memorizzare `k` funzioni hash (ognuna `a,b` interi).
    - Il numero di bit per chiave è `m/n ≈ ln(1/f) / ln(2)`.
    - I Bloom filters sono convenienti quando `m` è molto più piccolo del numero di bit necessari per memorizzare `S`.

---

### Marzo 28, 2025

**Lower Bound per Dizionari Approssimati**

- **Contesto:** Bloom Filters sono un esempio di dizionari approssimati (membership `X ∈ S` con probabilità di errore `δ`).
- **Teoria dell'Informazione:** Se si ha una classe di `K` oggetti, sono necessari almeno `log(K)` bit per distinguerli. Per `n`chiavi da un universo di `m` chiavi, sono necessari `log(m choose n)` bit.
- **Dizionari Approssimati:** Un dizionario approssimato con probabilità di errore `f` riconosce un insieme `S'` invece di `S`, dove `S'` è l'insieme di tutti gli elementi per cui il BF dice YES.
- **Argomento del Lower Bound:**
    - Sia `b` il numero minimo di bit necessari per memorizzare un dizionario approssimato per `S`.
    - Questi `b` bit descrivono `S'`.
    - Si possono aggiungere `n` bit per indicare quali elementi di `S'` sono anche in `S` (quindi `n` bit sono 1).
    - In totale, si usano `b + log(m choose n)` bit per codificare `S'` e quali sono in `S`.
    - Questo significa che `S` è codificato con `b + n + log(m choose n)` bits.
    - Per la teoria dell'informazione, qualsiasi codifica di `S` richiede `log(m choose n)` bit nel caso peggiore.
    - Quindi `b + n + log(m choose n) ≥ log(m choose n)`.
    - Il risultato è che `b ≥ n log(1/f)` bit sono richiesti per chiave.

**Succinct Rank Data Structure**

- **Input:** Un vettore binario `B` di `m` bit, dove `n` bit sono 1.
- **Obiettivo:** Una struttura dati che codifica implicitamente `B` e supporta query `rank(B, i)` in tempo costante.
    - `rank(B, i)`: numero di 1 in `B[1..i]`.
    - `B[i] = 1` se e solo se `rank(B, i-1) ≠ rank(B, i)`.
- **Implementazione:**
    - **Prima Idea:** Memorizzare `rank(B, i)` per ogni `i`. Costo: `m * log(m)` bit. Troppo spazio.
    - **Seconda Idea:** Campionare le somme di prefisso a intervalli regolari. Spazio ridotto a `O(m/log m)` bit. Tempo di query `O(log m)`.
    - **Miglriore Approccio:** `O(m)` bit per lo storage e `O(1)` tempo di query. Questo usa una tabella di `O(sqrt(m))`.

---

### Aprile 2, 2025

**Min-Hash (Permutazioni Min-wise Indipendenti)**

- **Permutazioni:** Un riordinamento degli elementi in un insieme `X`.
    - Il "minimo" di una permutazione è il primo elemento.
- **Famiglia di funzioni hash `H`:** "Permutano" un universo `U`, assegnando un ordinamento agli elementi.
- **Definizione Min-wise Indipendente:** Una famiglia `H` è min-wise indipendente se per ogni sottoinsieme `X ⊆ U` e per ogni `a ∈ X`, `Pr[h(a) = min_h(X)] = 1/|X|` quando `h` è scelta uniformemente a caso da `H`.
    - Cioè, ogni elemento di `X` ha la stessa probabilità di essere il minimo dopo essere stato permutato da `h`.
- **Applicazioni:** Controllare la somiglianza tra documenti, pagine web, ecc..
    - Un documento è trattato come un "bag of words" (insieme di parole distinte).
    - `U` è l'insieme di tutte le parole possibili.
- **Jaccard's Index `J(A,B)`:** Misura la somiglianza tra due insiemi `A` e `B`. `J(A,B) = |A ∩ B| / |A ∪ B|`.
    - Calcolare `J(Di, Dj)` per ogni coppia di documenti in una collezione massiva è costoso: `O(|Di| + |Dj|)` per ogni coppia.
- **Min-Hash aiuta (chiamato anche Sim-Hash):**
    - **Proprietà Interessante:** `Pr(min_h(A) = min_h(B)) = J(A,B)` per qualsiasi `A, B ⊆ U`.
        - **Dimostrazione:** `|A ∩ B| = b`, `|A ∪ B| = r+b+g` (dove `r` è in `A\B`, `g` è in `B\A`).
        - Se `h` è min-wise indipendente, ogni elemento `a ∈ A ∪ B` ha la stessa probabilità di essere il minimo.
        - La probabilità che `min_h(A) = min_h(B)` è la probabilità che l'elemento minimo di `A ∪ B` appartenga anche a `A ∩ B`. Questa probabilità è `|A ∩ B| / |A ∪ B| = J(A,B)`.
- **Problemi e Soluzioni:**
    1. **Problema:** Permutare `U` (universo) è infattibile se `U` è enorme.
        - **Soluzione:** Usare una famiglia di hashing universale è "quasi" buono come usare una permutazione casuale.
    2. **Problema:** Usare una singola `h` non dà abbastanza precisione.
        - **Soluzione:** Ripetere l'esperimento `k` volte (K-min sketch).
- **Estimatore `Y` di `J(A,B)`:**
    - `k` funzioni hash `h1, ..., hk` da una famiglia universale.
    - `Xi = 1` se `min_hi(A) = min_hi(B)` con probabilità `J(A,B)`.
    - `Y = (Σ Xi) / k` è uno stimatore.
    - **Prima Attenzione (Chernoff Bounds):** `k = O(ε^-2 * M)` dove `M = |A| + |B|`. Non è desiderabile se `M` è molto grande.
    - **Secondo e Migliore Attenzione (Azuma-Hoeffding (AH) bound):**
        - Per variabili casuali `Xi` dove `Σ Xi` è una martingala.
        - `Pr[|Y - μ| ≥ ε] ≤ 2e^(-2kε^2)`.
        - In questo caso `k = O(ε^-2 log(1/δ))`. Questo è un buon risultato (FPTAS).
- **Applicazione: Network Analysis**
    - Stimare il numero di triangoli in un grafo (indicatore di rete "sociale").
    - Un triangolo `(x,y,z)` implica che `x` e `y` sono amici, e hanno un amico comune `z` (`z ∈ N(x) ∩ N(y)`).
    - Il numero di amici comuni `|N(x) ∩ N(y)|` può essere stimato usando l'approssimazione di Jaccard Index. `|N(x) ∩ N(y)| ≈ J_hat(N(x), N(y)) * (|N(x)| + |N(y)|)`.

---

### Aprile 3, 2025

**Min-Cut in Grafi (Randomized Algorithm)**

- **Grafo `G = (V, E)`:** `n` nodi, `m` archi (archi multipli ammessi).
- **Cut `C = (V1, V2)`:** Partizione dei nodi `V` in `V1` e `V2`.
- **Cutset `E(V1, V2)`:** Insieme degli archi che connettono un nodo in `V1` a un nodo in `V2`.
- **Min-Cut:** Un cut `C` è un min-cut se `|E(C)|` è minimo.
    - Il min-cut non è necessariamente unico.
    - `|E(C)| ≤ deg(v)` per qualsiasi nodo `v`.
- **Contrazione di Archi `G/uv`:** Unisce i nodi `u` e `v` in un singolo nodo `uv`, rimuovendo gli archi tra `u` e `v` e collegando `uv` a tutti i vicini di `u` e `v`.
    - **Intuizione:** Contrarre `u` e `v` significa che `u` e `v` appartengono allo stesso lato del taglio finale.
- **Relazione tra Contrazioni e Tagli:**
    - **Teorema A:** Qualsiasi sequenza di contrazioni di archi che lascia solo 2 nodi produce un taglio `(V1, V2)`.
    - **Teorema B:** Dato un taglio `C=(V1, V2)`, non necessariamente esiste una sequenza di contrazioni che porta a solo 2 nodi.

**Algoritmo Karger (GuessMinCut)**

- **Algoritmo:**
    1. `G_0 = G`.
    2. `while |V| > 2`: a. Scegli un arco `uv ∈ E` uniformemente e casualmente. b.  `G = G / uv` (contrazione).
    3. `return |E(G)|` (il numero di archi multipli rimasti quando solo 2 nodi rimangono).
- **Quando l'algoritmo fallisce?**
    - Fallisce se l'arco `uv` scelto appartiene a **ogni** min-cut set.
    - Un arco `uv` è "BAD" se `uv ∈ E(C)` per ogni min-cut `C`.
- **Proprietà Cruciale:** Ci sono al massimo `K` archi "BAD" in `G`, dove `K` è la dimensione del min-cut.
    - `Pr[uv is BAD] ≤ K / (2m/n)` (perché `2m/n` è il grado medio, `deg(u) ≥ K` per ogni nodo `u`). `Pr[uv is BAD] ≤ 2K/2m = K/m`.
- **Probabilità di successo `P(n)`:** Probabilità che GuessMinCut trovi correttamente un min-cut.
    - `P(n) = P(n-1) * (1 - Pr[chosen edge is BAD])`.
    - `P(n) ≥ (1 - K/(deg_avg)) * P(n-1)`.
    - `P(n) ≥ (1 - K/m_i) * P(n-1)`.
    - `P(n) ≥ (1 - K / (2m/(n-i+1))) * P(n-1)`.
    - `P(n) ≥ (1 - 2/(n-i+1))`.
    - Eseguendo ricorsivamente, `P(n) ≥ (n-2)/n * (n-3)/(n-1) * ... * 1/3 * 2/2 = 2 / (n(n-1))`. `P(n) ≥ 2/n^2`.
- **Boosting la Probabilità:**
    - Ripetere l'esecuzione di GuessMinCut `N` volte e restituire il valore minimo tra i risultati.
    - La probabilità di errore diventa `(1 - 2/n^2)^N`.
    - Per ridurre la probabilità di errore a `1/n^c`, `N = O(n^2 log n)` esecuzioni sono necessarie.

---

### Aprile 7, 2025

**Load Balancing (Dettagli)**

- **Scenario:** `m` server, `n` job (`0..n-1`), `n ≥ m`. Fair load: `n/m` job per server.
- **Implementazione:** Scegliere casualmente una funzione hash `h` da una famiglia universale, assegnando il job `i` al server `h(i)`.
- **`Xj`:** Variabile indicatrice per la load sul server `j` (numero di job assegnati a `j`).
- **`E[Xj] = n/m`**.
- **Concentration Bounds (ripasso e applicazione):**
    - **Markov's Inequality:** `Pr[X ≥ a] ≤ E[X]/a`.
    - **Chebyshev's Inequality:** `Pr[|X - E[X]| ≥ α] ≤ Var[X]/α^2`.
        - `Var[Xj] = E[Xj^2] - (E[Xj])^2`.
        - Poiché `h` è 2-way indipendente (pairwise independent), `Pr[h(i)=j \land h(i')=j] = Pr[h(i)=j] * Pr[h(i')=j] = (1/m)^2` per `i ≠ i'`.
        - `Var[Xj] = n * (1/m) * (1 - 1/m)`.
        - `Var[Xj] = n/m * (1 - 1/m) < n/m`.
    - **Union Bound:** `Pr[A U B] ≤ Pr[A] + Pr[B]`.
    - **Max Load:** `Pr[max(Xj - E[X]) ≥ εn] = Pr[∪j (Xj - n/m) ≥ εn] ≤ Σ Pr[(Xj - n/m) ≥ εn]`.
    - Usando Chebyshev e Union Bound: `Pr[max_j Xj > n/m + α] ≤ m * Var[Xj] / α^2 = m * (n/m * (1 - 1/m)) / α^2 = n(1 - 1/m) / α^2`.
    - Scegliendo `α = εn`, si ottiene `Pr[max_j Xj > n/m + εn] ≤ n(1 - 1/m) / (εn)^2 = (1 - 1/m) / (ε^2 n)`.
    - **Chernoff's Bounds:**
        - Per `n = m`, `μ = 1`. `Pr[X ≥ (1 + δ)μ] ≤ e^(-μδ^2/3)` (per `δ > 0`).
        - Per `Pr[X ≥ μ + c ln n] ≤ 1/n^c`.
        - Il carico massimo è `n/m + O(sqrt(log m))` con alta probabilità.

---

### Aprile 9, 2025

**Sketches: Systematic View**

- **Concetto:** Strutture dati che usano spazio "limitato" per rispondere a query.
- **Rank function `r: U -> [0, 1)`:** Una funzione scelta casualmente che assegna un ordinamento agli elementi.
- **Sketch `S(A)` di un insieme `A`:** Una rappresentazione compressa di `A`.
- **Operazioni Supportate:**
    - `INIT(A)`: Costruire `S(A)` da `A`.
    - `UPDATE`: Ottenere `S(A ∪ {u})` da `S(A)` e `u`.
    - `UNION`: Ottenere `S(A ∪ B)` da `S(A)` e `S(B)`.
    - `SIZE`: Stimare `|A|` usando `S(A)`.
- **Min-Sketch (Esempio):**
    - `INIT(A)`: `S(A) = {min_i ri(A) : 1 ≤ i ≤ k}` (minimo di `k` funzioni rank).
    - `UPDATE`: `S(A ∪ {u}) = {min(ri(di), ri(u)) : 1 ≤ i ≤ k}`.
    - `UNION`: `S(A ∪ B) = {min(ri(ai), ri(bi)) : 1 ≤ i ≤ k}`.
    - `SIZE`: La stima di `|A|` si basa sulla media dei valori minimi.

**Bottom-k Sketch**

- **Concetto:** Usare una singola funzione rank `r`.
- `INIT(A)`: `S(A) =` gli `k` elementi più piccoli in `A` secondo `r`.
- `UPDATE`: `S(A ∪ {u}) =` gli `k` elementi più piccoli in `S(A) ∪ {u}`.
- `UNION`: `S(A ∪ B) =` gli `k` elementi più piccoli in `S(A) ∪ S(B)`. Costo `O(k)`.
- `SIZE`: Stimare `|A|` usando il `k`-esimo elemento più piccolo `r(ak)`: `|A| ≈ k / r(ak)`.

**Threshold Sketch**

- **Concetto:** Usare una singola funzione rank `r` e una soglia `t ∈`.
- `INIT(A)`: `S(A) = {a ∈ A : r(a) < t}`. (La dimensione di `S(A)` può variare).
- `UPDATE`: `S(A ∪ {u}) = S(A) ∪ {u}` se `r(u) < t`, altrimenti `S(A)`.
- `UNION`: `S(A ∪ B) = S(A) ∪ S(B)`.
- `SIZE`: `|A| ≈ |S(A)| / t`.

**Jaccard Index con Sketches**

- **Bottom-k Sketch per Jaccard Index:**
    
    - `Rk(X) =` i `k` elementi più piccoli in `X` secondo `r()`.
    - `Estimate(A,B) = |Rk(A) ∩ Rk(B)| / |Rk(A) ∪ Rk(B)|`.
    - Questo è uno stimatore **non distorto** (unbiased) di `J(A,B)`.
    - `E[Estimate(A,B)] = J(A,B)`.
    - La distribuzione degli elementi che appartengono sia ad `A ∩ B` sia a `Rk(A ∪ B)` è ipergeometrica.
- **Threshold Sketch per Jaccard Index:**
    
    - Sia `A' = S(A)` e `B' = S(B)` (gli elementi con `r(a) < t`).
    - `Yxy = 1` se `x ∈ A' ∩ B'`, `0` altrimenti.
    - `Pr[Yxy = 1] = J(A,B)`.
    - `E[Estimate(A,B)] = E[Yxy]`.

---

### Aprile 14, 2025

**Streaming Algorithms**

- **Concetto:** Elaborare dati (uno "stream") con spazio limitato, spesso `O(1)` parole di memoria.
- **Esempio 1: Trovare il Max**
    - Mantieni `current_max`. Se `current_item > current_max`, aggiorna `current_max`.
    - Spazio: `O(1)` parola.
- **Esempio 2: Trovare l'elemento mancante**
    - Input: `n-1` interi distinti da `[1..n]`.
    - **a) Inefficiente:** Vettore binario `B` di `n` bit. Segna `B[item] = 1`. Scansiona `B` per trovare lo 0. Spazio `O(n)`.
    - **b) Migliore (Gauss Sum):** Somma tutti gli elementi visti `S_current`. La somma attesa è `n(n+1)/2`. L'elemento mancante è `n(n+1)/2 - S_current`. Spazio: `O(log n)` bit.
    - **c) Ottima (XOR):** Inizializza `S_xor = 0`. Per ogni item `i`, `S_xor = S_xor XOR i`. L'elemento mancante è `(XOR_{j=1}^n j) XOR S_xor`. Spazio: `O(log n)` bit.
- **Frequenza degli elementi in uno Stream**
    - `fa`: frequenza dell'elemento `a`.
    - **Esercizio:** Algoritmo streaming `O(1)` parole per trovare l'elemento più frequente (`fa > m/2`).
        - Una soluzione non banale per questo è l'algoritmo di Boyer-Moore majority vote, che non è nelle fonti ma è un algoritmo noto che fa questo in `O(1)` spazio.

---

### Aprile 16, 2025

**Count-Min Sketch (Estensioni e Approfondimenti)**

- **Operazione di Decremento (`F[i]--`):** Supportata.
    - Per gestire decrementi e migliorare la precisione, la stima `F[i]` è la **mediana** dei valori `T[j][hj(i)]` su tutte le righe `j`.
    - Questo garantisce `|F[i] - F(i)| < 2ε ||F||1` con alta probabilità.
    - La probabilità di errore `Pr[|F[i] - F(i)| ≥ 2ε ||F||1]` è controllata usando le Chernoff Bounds.
    - Il numero di righe `r = O(ln(1/δ))` e il numero di colonne `c = O(e/ε)`.
- **Query su Intervalli (`[X..Y]`):** Stimare `Σ_{i=X}^Y F(i)`.
    - **Baseline:** Sommare le stime individuali `F[i]` per ogni `i` nell'intervallo. Questo è lento (`O((Y-X+1) * r)`) e l'errore può essere molto grande.
    - **Approccio Migliore: Intervalli Diadici ("Dyadic Intervals")**
        - Si mantengono meno di `2N` contatori invece di `N`.
        - Gli intervalli sono potenze di 2 (es. `,`).
        - Quando `F(i)++`, si incrementano i contatori corrispondenti lungo il percorso foglia-radice in un albero binario completo implicito. Costo: `O(log N * r)` tempo.
        - **Query:** Per `F[X..Y]`, l'intervallo `[X,Y]` può essere decomposto in `O(log N)` intervalli diadici che non si sovrappongono. Si sommano le stime di questi intervalli diadici. Costo: `O(log N * r)` tempo.
        - **Errore:** `F[X..Y] ≤ F(X..Y) + 2 * N * ε ||F||1`. (Errore cumulativo).

---

### Aprile 23, 2025 (Parte 1)

**Milgram's Experiment (Six Degrees of Separation)**

- **Obiettivo:** Misurare la distanza media in una rete di amicizie.
- **Impostazione:** 296 volontari che dovevano inviare una lettera a un "target" a Boston, passando la lettera solo a persone che conoscevano.
- **Risultato:** 64 lettere consegnate con successo. La distanza media (numero di intermediari + 1) era 6.2. Questo ha dato origine al termine "Six degrees of separation".
- **Tempi moderni (Facebook):** L'esperimento è stato ripetuto, e la distanza media era 4.74.

**Computational Task (Stimare la distanza media)**

- **`Nh`:** Frazione di coppie di nodi ordinate `(u,v)` a distanza esattamente `h`. `Nh = |{(u,v) : d(u,v) = h}| / (n(n-1))`.
- **Distanza media:** `Σ h * Nh` (somma pesata).
- **Approccio:** Approssimare `Nh` attraverso campionamento casuale sui nodi.
    - Scegliere casualmente un sottoinsieme `U ⊆ V` di nodi.
    - Definire `N_U = |{(u,v) : u ∈ U, v ∈ V, d(u,v) = h}| / (|U|(n-1))`.
    - Per un piccolo `U`, si ottiene `N_U ≈ Nh`.
    - Questo implica eseguire BFS/Dijkstra solo dai nodi scelti casualmente in `U`.
    - Tempo di esecuzione da `O(n^2)` a `O(|U| * (n+m))`.
- **Garanzia di Approssimazione (FPTAS):** Usando la Azuma-Hoeffding (AH) bound, si può ottenere un FPTAS `(ε, δ)` quando `|U| = O(log(1/δ) / ε^2)`.
    - `Xi = Niv` (frazione di coppie a distanza `i`). `E[Xi] = Ni`.
    - `Pr[|ΣXi - Ni| ≥ ε] ≤ 2e^(-2kε^2)`.

---

### Aprile 28, 2025

**Diameter in Graphs (Approximation)**

- **2-SWEEP (Heuristic):**
    - Mantiene un limite inferiore `L` e un limite superiore `U` per il diametro `D` (`L ≤ D ≤ U`).
    - **Idea:** Usare BFS per raffinare `L` e `U`.
        - Scegliere un nodo `r` uniformemente a caso.
        - Eseguire `BFS(r)` per trovare `a` (il nodo più lontano da `r`). `d(r,a)` è una stima del diametro.
        - Eseguire `BFS(a)` per trovare `b` (il nodo più lontano da `a`). `d(a,b)` è un'altra stima.
        - **Aggiornare L e U:**
            - `L = max(L, d(r,a), d(a,b))`. (`d(x,y)` da BFS è un lower bound).
            - `U = min(U, 2*d(r,a), 2*d(a,b))`. (Per disuguaglianza triangolare `D ≤ 2*e(x)` per ogni `x`).
    - Non c'è garanzia che `L` e `U` convergano a `D`, ma funziona sorprendentemente bene in reti reali.
- **Difficoltà dell'Approssimazione:** Non è possibile ottenere un algoritmo di approssimazione `(1-ε)D ≤ D̂ ≤ D` per qualsiasi `ε` arbitrariamente piccolo, a meno che SETH non sia falsa.
    - Questo perché la distinzione tra `D=2` e `D=3` è difficile (connessa a SETH).
    - Un algoritmo `(1-ε)`-approx permetterebbe di decidere `D=2` o `D=3`.
    - La migliore approssimazione sperata è `(2/3)D ≤ D̂ ≤ D`.
- **Algoritmo Randomizzato per Approssimazione del Diametro:** Trova un'approssimazione `D̂` tale che `(2/3)D ≤ D̂ ≤ D` con alta probabilità in `O(n * m^(1/2))` tempo.
    - **Idea:** Trovare un sottoinsieme "intelligente" `Z` di nodi tale che `|Z| = O(sqrt(n) log n)` e `D̂ = max_{u ∈ Z} BFS(u)` approssimi `D`.
    - **Algoritmo:**
        1. Scegli un insieme `S` di `O(sqrt(n) log n)` nodi casualmente e uniformemente da `V`.
        2. Per ogni `s ∈ S`, esegui `BFS(s)` e trova `w` (il nodo più lontano da `s`).
        3. Sia `Z = S ∪ NH(w)` dove `NH(w)` è l'insieme dei primi `H` nodi scoperti da `BFS(w)` (i.e., `H` è un raggio).
        4. Calcola `D̂ = max_{u ∈ Z} e(u)` eseguendo `BFS(u)` per tutti gli `u ∈ Z`.
    - **Costo Totale:** `O(|S| * (n+m) + |Z| * (n+m))`. Poiché `|S| = O(sqrt(n) log n)` e `|Z| = O(sqrt(n) log n)` (se `H` è scelto opportunamente), e `m = O(n)` per grafi sparsi, il costo è `O(n sqrt(n) log n)`.
    - **Perché funziona?** `S` è un "hitting set" per qualsiasi `NH(u)` con alta probabilità.
    - Si dimostra che `2h + z ≤ D̂ ≤ D` con alta probabilità, dove `D = 3h + z`.

---

### Aprile 30, 2025

**Hardness and NP-Completeness**

- **SAT (Satisfiability of Boolean formulas):**
    - Input: `n` variabili booleane `x1, ..., xn ∈ {0,1}`.
    - Formula in CNF (Conjunctive Normal Form), es. `(x1 ∨ ¬x2) ∧ (...)`.
    - Problema: Esiste un assegnamento di verità che rende la formula `TRUE`?.
    - **Cook-Levin Theorem:** SAT è NP-completo. Ogni problema in NP si riduce polinomialmente a SAT.
    - NP: Classe di problemi per cui una soluzione può essere verificata in tempo polinomiale (es. con un "certificato" o "testimone").
- **Come affrontare problemi NP-Hard/Complete:**
    - Calcolo esatto per casi speciali.
    - Calcolo esatto con algoritmi parametrizzati.
    - Soluzioni vicine all'ottimale (algoritmi di approssimazione).

**Knapsack Problem**

- **Definizione:**
    - `n` file (item) con dimensione `wi` e valore `vi`.
    - Capacità massima `W`.
    - Obiettivo: Scegliere un sottoinsieme di file che massimizza il valore totale `Σvi` rispettando il vincolo di capacità `Σwi ≤ W`. I file non possono essere divisi.
- **NP-Completeness:** La versione decisionale (esiste un sottoinsieme con valore ≥ V?) è NP-completa.
- **Soluzioni Esatte:**
    - **Forza Bruta:** Esaminare tutti i `2^n` sottoinsiemi. Costo: `O(2^n * poly(n))`.
    - **Dynamic Programming (DP1):** `T[i][w]` = valore massimo scegliendo dai primi `i` elementi con capacità `w`.
        - `T[i][w] = max( T[i-1][w], T[i-1][w - wi] + vi )`.
        - Costo: `O(nW)` tempo. Questo è pseudo-polinomiale perché dipende da `W`, che può essere grande.
    - **Dynamic Programming (DP2):** `T[i][v]` = dimensione minima per ottenere valore `v` dai primi `i` elementi.
        - `T[i][v] = min( T[i-1][v], T[i-1][v - vi] + wi )`.
        - Costo: `O(n * Vmax)` dove `Vmax` è la somma massima possibile dei valori. Anche questo è pseudo-polinomiale.

**Counting Problem (#P)**

- **Knapsack Counting (#Knapsack):** Contare tutte le possibili scelte di sottoinsiemi `S` tali che `Σwi ≤ W`.
- **Soluzione:** Basata su DP1 in `O(nW)` tempo.
    - `T[i][j]` = numero di modi per scegliere dagli `i` elementi per ottenere peso `j`.
    - `T[i][j] = T[i-1][j] + T[i-1][j-wi]`.
- **Campionamento Uniforme (da Problemi di Conteggio):** Se si sa come contare il numero di soluzioni (tramite DP), si può campionare uniformemente una soluzione usando le probabilità condizionali.
    - **Caveat:** Funziona solo se lo schema di programmazione dinamica non sovrappone le soluzioni (non overcounting).
- **Classe #P:** Corrisponde a NP per i problemi di conteggio.
    - Un problema `Π` è in #P se esiste un verificatore polinomiale `V(x,y)` e l'output è il numero di certificati `y` validi per l'input `x`.
    - **#P-completi:** Problemi "più difficili" in #P.
    - Sorprendentemente, alcuni problemi in P sono #P-completi (es. topological sorting, perfect matching, contare stringhe rappresentate da espressioni regolari).

---

### Maggio 5, 2025

**Approximation Algorithms**

- **Obiettivo:** Trovare una soluzione `S` a un problema NP-Hard (minimizazione o massimizzazione) il cui costo `cost(S)` sia "vicino" al costo ottimale `OPT`.
- **`r`-Approssimazione:**
    - **Minimizzazione:** `cost(S) ≤ r * OPT` (con `r ≥ 1`).
    - **Massimizzazione:** `cost(S) ≥ r * OPT` (con `r ≤ 1`). (A volte si usa `r ≥ 1` e `OPT / r ≤ cost(S)`).
- **Knapsack Problem (Esempio):** Massimizzare `Σvi` con `Σwi ≤ W`.

**2-Approssimazione (Algoritmo Greedy)**

- **Idea:** Dare priorità agli item con il miglior rapporto valore/peso (`vi/wi`).
- **Algoritmo (Semplice):**
    1. Ordina gli item in base al rapporto `vi/wi` in ordine decrescente.
    2. `S = {}`, `W_current = W`.
    3. Per `i = 1..n` (ordinati): se `wi ≤ W_current`, aggiungi `i` a `S` e `W_current = W_current - wi`.
    4. `return S`.
- **Problema:** Questo greedy non garantisce il valore OPT. Esempio: `V1=V2=...=Vn-1=1`, `W1=W2=...=Wn-1=1`. `Vn=W`, `Wn=W`. Se `W` è grande, il greedy può scegliere solo item piccoli e scartare l'item grande che sarebbe l'ottimale.
- **Fissare il Problema (Versione Migliorata):**
    - Aggiungi un terzo passo: `return max(Greedy_Value, Vmax)`, dove `Vmax` è il valore dell'item più prezioso tra tutti.
    - Questo garantisce una **2-approssimazione**. `OPT ≤ 2 * max(Greedy_Value, Vmax)`.
    - **Dimostrazione (Sketch):**
        - Sia `j` il primo item che non entra nello zaino del greedy.
        - La somma degli item `1..j-1` è quasi `W`.
        - `OPT < (Σ_{i=1}^{j-1} Vi) + Vj`. (La somma `T_j` è la capacità totale, `V_j` è il valore del j-esimo item).
        - Il valore ottenuto dal greedy è `Σ_{i=1}^{j-1} Vi`.
        - Si dimostra che `OPT ≤ 2 * max(Greedy_Value, Vmax)`.

**FPTAS (Fully Polynomial-Time Approximation Scheme)**

- **Obiettivo:** Un algoritmo di approssimazione `(1-ε)` per qualsiasi `ε > 0`, con tempo di esecuzione polinomiale in `n`, `1/ε`, `log W`.
- **Idea:** Scalare i valori per rendere `Vmax` più piccolo, permettendo l'uso di DP2 (che è pseudo-polinomiale in `Vmax`).
- **Algoritmo:**
    1. Istanza originale: `Vi, Wi, W`.
    2. Scegli un fattore di scala `k = ε * Vmax / n`.
    3. Istanza scalata: `Vi' = floor(Vi / k)`, `Wi`, `W`.
    4. Applica DP2 all'istanza scalata per trovare la soluzione ottimale `S'`.
    5. `return S'` (come soluzione per l'istanza originale).
- **Garanzia:** `OPT * (1-ε) ≤ cost(S')`.
    - **Dimostrazione (Sketch):**
        - `Vi' = floor(Vi / k)`. Quindi `Vi/k - 1 < Vi' ≤ Vi/k`.
        - `k * Vi' ≤ Vi`.
        - Sia `S*` la soluzione ottimale per l'istanza originale.
        - `OPT_scaled = Σ_{i ∈ S*} Vi' = Σ_{i ∈ S*} floor(Vi/k) ≥ Σ_{i ∈ S*} (Vi/k - 1) = OPT/k - |S*|`.
        - Poiché `S'` è ottimale per l'istanza scalata, `Σ_{i ∈ S'} Vi' ≥ OPT_scaled`.
        - `Σ_{i ∈ S'} Vi = Σ_{i ∈ S'} k*Vi' + k*(Vi - k*Vi') ≥ k * OPT_scaled = k * (OPT/k - |S*|) = OPT - k*|S*|`.
        - Poiché `|S*| ≤ n` e `k = ε * Vmax / n`, allora `k*|S*| ≤ k*n = ε*Vmax`.
        - Inoltre, `Vmax ≤ OPT` (dato che `OPT` include almeno l'item più prezioso).
        - Quindi `cost(S') ≥ OPT - ε*OPT = OPT * (1-ε)`.
- **Tempo di Esecuzione:** `O(n^2 * Vmax_scaled) = O(n^2 * (Vmax / k)) = O(n^2 * (Vmax / (ε * Vmax / n))) = O(n^3 / ε)`.

---

### Maggio 7, 2025

**Approximate Counting**

- **Contesto:** Contare il numero di soluzioni per problemi NP-Hard (come Knapsack), specialmente quando il range `W`è grande e il calcolo esatto `O(nW)` è troppo lento.
- **Idea Principale:** Scalare i pesi invece dei valori.
    - Sia `H = floor(n/ε)` un fattore di scala.
    - **Istanza Originale:** `Vi, Wi, W`. `F` è l'insieme di tutti i sottoinsiemi fattibili.
    - **Istanza Scalata:** `Vi, Wi' = floor(Wi/H)`, `W' = floor(W/H)`. `F'` è l'insieme dei sottoinsiemi fattibili nell'istanza scalata.
    - Risolvere esattamente l'istanza scalata ha un costo `O(n * W') = O(n * W/H) = O(n * W * ε / n) = O(Wε)` tempo. Questo è polinomiale in `n` e `W` (ma non in `W` stesso, bensì `W/H`).
- **Relazione tra `F` e `F'`:**
    - `F ⊆ F'` (ogni soluzione fattibile nell'originale è fattibile nello scalato, perché `ΣWi >= H * ΣWi'`).
    - `|F|` e `|F'|` sono simili.
- **Dimostrazione della Somiglianza di Dimensione:**
    - Si definisce una mappatura `f: F' -> F` tale che `f(S') = S'` se `S' ∈ F`, altrimenti `f(S') = S' \ {w_max}`(rimuove l'elemento con peso massimo da `S'`).
    - Si dimostra che per ogni `S' ∈ F`, esistono al massimo `n+1` insiemi `S ∈ F'` tali che `f(S) = S'`.
    - Questo implica `|F'| ≤ (n+1) * |F|`.
    - Quindi, `|F'|` è una buona approssimazione di `|F|` (a meno di un fattore polinomiale).
- **FPRAS (Fully Polynomial-Time Randomized Approximation Scheme)**
    - **Definizione:** Un FPTAS con randomizzazione (`δ` errore di probabilità).
    - **Idea:** Stimare `P = |F| / |F'|` usando il campionamento.
    - **Algoritmo:**
        1. Ripeti `N` volte (per `N` scelto opportunamente): a. Campiona casualmente un insieme fattibile `S ∈ F'`. b. Sia `X_t = 1` se `S ∈ F`, `0` altrimenti.
        2. Sia `X = Σ X_t`.
        3. `return Z = X / N`.
    - **`Z` è uno stimatore non distorto:** `E[Z] = P`.
    - **Utilizzo delle Chernoff Bounds:** `Pr[|Z - P| ≥ εP] ≤ 2e^(-ε^2 N P / 2)`.
        - Scegliendo `N = O(log(1/δ) / (ε^2 * P))` per ottenere `Pr[...] ≤ δ`.
    - **Costo Totale:** `O(nW * ε)` (per il DP sull'istanza scalata) + `O(N*n)` (per il campionamento).
    - Il campionamento uniforme di un insieme fattibile `S ∈ F'` da un problema #P può essere fatto usando la DP (se si sanno contare le soluzioni).

---

### Maggio 12, 2025

**Min-Cut vs. Max-Cut**

- **Cut `(S, S̄)`:** Partizione dei nodi `V` in `S` e `S̄ = V \ S`.
    
- **Cutset `E(S, S̄)`:** Insieme degli archi che attraversano il taglio.
    
- **Min-Cut:** Trovare un taglio con un numero minimo di archi nel cutset (risolvibile in tempo polinomiale).
    
- **Max-Cut:** Trovare un taglio con un numero massimo di archi nel cutset (NP-hard).
    
    - Concettualmente, trovare una 2-colorazione con il massimo numero di archi tra nodi di colore diverso.
- **Approcci per Max-Cut (2-approssimazione):**
    
    1. **Local Search:**
        
        - Parti con un taglio iniziale (es. `S = V`).
        - `while` esiste un nodo `u ∈ V` tale che spostare `u` da `S` a `S̄` (o viceversa) aumenta strettamente la dimensione di `|E(S, S̄)|`: sposta `u`.
        - **Terminazione:** Garantita, perché `|E(S, S̄)|` aumenta strettamente e `|E|` è finito.
        - **Garanzia:** Fornisce una **2-approssimazione**. `cost(S) ≥ |E|/2`. `OPT ≤ |E|` è un limite superiore triviale.
    2. **Greedy:**
        
        - Numerare i nodi `1, ..., n` (ordine arbitrario).
        - Inizializza `S = {}`.
        - Per `u = 1..n`: assegna `u` a `S` o `S̄` in modo da massimizzare `|E(S, S̄)|` (considerando solo gli archi che si connettono ai nodi già assegnati).
        - Costo: `O(|V|)` passi.
        - **Garanzia:** Fornisce una **2-approssimazione**. `cost(S) ≥ |E|/2`.
        - **Dimostrazione (Sketch):** Per ogni nodo `u`, almeno metà degli archi incidenti a `u` devono contribuire al cutset per massimizzare il guadagno. `cost(S) = Σ_{u ∈ V} r_u`, dove `r_u` è il numero di archi per cui `u` è "responsabile".
    3. **Random Coin Tossing:**
        
        - **Algoritmo Randomizzato 2-coloring:**
            - `S = {}`.
            - Per ogni nodo `u ∈ V`: assegna `u` a `S` con probabilità `1/2`, altrimenti a `S̄`.
        - **Probabilità che un arco `ij` sia nel cutset `E(S, S̄)`:** `Pr[ij ∈ E(S, S̄)] = 1/2` (se `i` e `j` hanno colori diversi).
        - **Valore Atteso del Cutset:** `E[|E(S, S̄)|] = E[Σ X_ij] = Σ E[X_ij] = Σ Pr[ij ∈ E(S, S̄)] = |E| * (1/2)`.
        - Questo è uno stimatore non distorto.

**Negative Results for Approximation (TSP)**

- **TSP (Traveling Salesperson Problem):**
    - `n` città, distanze `Dij`.
    - Obiettivo: Trovare un tour (permutazione di città) che visita tutte le città una volta e ritorna al punto di partenza, minimizzando il costo totale.
- **Proposizione:** Non si può trovare una `r`-approssimazione in tempo polinomiale per TSP a meno che P=NP.
    - **Dimostrazione (Gap Method):** Per contraddizione, supponiamo che esista un algoritmo `A_r` di `r`-approssimazione per TSP.
        1. Costruiamo un'istanza TSP `D` da un'istanza `G` di Hamiltonian Cycle (HAM).
        2. `D_ij = 1` se `(i,j) ∈ E` (arco esiste in `G`), `D_ij = 2 + r*n` altrimenti.
        3. Eseguiamo `A_r` su questa istanza `D`.
        4. Se `G` è Hamiltoniano: `OPT_TSP = n` (costo di un ciclo di archi di peso 1). L'algoritmo `A_r` restituirà `C ≤ r * OPT_TSP = r*n`.
        5. Se `G` NON è Hamiltoniano: Qualsiasi tour deve usare almeno un arco di peso `(2+r*n)`. Quindi `OPT_TSP ≥ (n-1) + (2+r*n) = n+1+r*n`. L'algoritmo `A_r` restituirà `C ≥ OPT_TSP > n`.
        6. Quindi, se `C ≤ n`, `G` è Hamiltoniano. Se `C > n`, `G` non è Hamiltoniano.
        7. Questo significa che `A_r` risolve HAM in tempo polinomiale, il che implicherebbe P=NP, una contraddizione.

**Metric TSP (con disuguaglianza triangolare)**

- Se vale la disuguaglianza triangolare (`D_ik ≤ D_ij + D_jk`), TSP ammette un'approssimazione.
- **Algoritmo 2-Approssimazione:**
    1. Costruisci un grafo completo `G'=(V,E')` con pesi `W_ij = D_ij`.
    2. Calcola un **Minimum Spanning Tree (MST)** `S` di `G'`.
    3. Esegui una **pre-order traversal** dell'MST `S` per ottenere un tour `T`.
- **Garanzia:** `cost(T)` è una 2-approssimazione per Metric TSP.
    - **Dimostrazione:**
        - Un tour TSP ottimale `T*` meno un arco è un albero ricoprente. Quindi `cost(S) ≤ OPT_TSP`.
        - Un percorso DFS che visita tutti gli archi dell'MST due volte ha un costo `2 * cost(S)`.
        - Grazie alla disuguaglianza triangolare, saltare nodi non aumenta il costo. Quindi `cost(T) ≤ 2 * cost(S)`.
        - Combinando, `cost(T) ≤ 2 * cost(S) ≤ 2 * OPT_TSP`.

---

### Maggio 14, 2025

**Approximation Algorithm Recap**

- **Tecniche:** Greedy, Local Search, Dynamic Programming, Randomization + Derandomization.
- **Linear Programming (LP):** Non trattato in dettaglio.

**Problemi e Limiti di Approssimazione**

- **TSP (Traveling Salesperson Problem):** NP-hard, non ammette approssimazione a meno che P=NP.
- **Vertex Cover (VC):** `S ⊆ V` è un Vertex Cover se per ogni arco `uv ∈ E`, `u ∈ S` o `v ∈ S`.
    - **2-Approssimazione:**
        
        1. `S = {}`.
        2. Per ogni arco `uv ∈ E`: se né `u` né `v` sono in `S`, allora aggiungi `u` e `v` a `S`.
        3. `return S`.
        
        - Questo algoritmo restituisce un VC `S` tale che `|S| ≤ 2 * k_min` (dove `k_min` è la dimensione del VC ottimale). Ogni arco processato aggiunge al più due nodi a `S`, e ogni arco è "coperto". Inoltre, gli archi scelti non condividono endpoint.
- **Set Cover:** Dato un universo `U` e una collezione `C` di sottoinsiemi di `U`, trovare una sottocollezione `C' ⊆ C` che copre `U` (unione di tutti gli insiemi in `C'` è `U`) con il minimo numero di insiemi.
    - **`O(log n)`-Approssimazione:** Algoritmo greedy.
        - `C' = {}`.
        - `while` ci sono elementi non coperti in `U`: scegli l'insieme `S ∈ C` che copre il maggior numero di elementi non coperti, aggiungilo a `C'` e rimuovi gli elementi coperti da `U`.

**Parameterized Algorithms**

- **Obiettivo:** Risolvere problemi NP-Hard in `O(f(k) * poly(n))` tempo.
    - `k` è un "parametro significativo" del problema (spesso non correlato a `n` o `m`).
    - `f(k)` può crescere molto rapidamente, ma solo in `k`.
- **Vertex Cover (Esempio):** Trovare un VC `S` di dimensione `k`.
- **Prima Idea (Brute Force):** Controllare tutti i sottoinsiemi di dimensione `k`. Costo `O((n choose k) * poly(n))`, che non è `O(f(k) * poly(n))`.
- **Migliore Idea: Tecnica di Kernelization**
    - Trasforma il grafo `G` in un "kernel" `G_K` con `O(k^2)` nodi e archi, mantenendo la proprietà che `G` ha un VC di dimensione `k` se e solo se `G_K` ha un VC di dimensione `k'`.
    - **Regole di Riduzione:**
        1. Se `v` è un nodo isolato: risolvi `G-v` con `k`.
        2. Se `v` ha grado `> k`: `v` deve appartenere a ogni VC. Risolvi `G-v` con `k-1`.
        3. Se le regole 1 e 2 non sono più applicabili: Se `G_K` (il grafo ridotto) ha più di `k^2` archi (o nodi, se il grado è `≤ k`), allora non esiste una soluzione (non c'è un VC di dimensione `k`).
    - Dopo la kernelization, si può applicare un algoritmo esponenziale su `G_K`. Costo `O(f(k) + poly(n))`.

**Kernelization by Branching**

- **Idea:** Se `v` è un nodo con grado massimo `d_v > 0`:
    1. O `v` è nel VC: risolvere ricorsivamente `G-v` con `k-1`.
    2. O `v` NON è nel VC: allora tutti i suoi vicini `N(v)` devono essere nel VC. Risolvere ricorsivamente `G - N(v)`con `k - |N(v)|`.
- **Albero di Ricorsione:** Ogni chiamata genera due chiamate.
    - Il numero di foglie è `O(φ^k)` dove `φ ≈ 1.618` (rapporto aureo, come Fibonacci).
    - Costo totale: `O(1.618^k * poly(n))`.
- **Miglioramenti:**
    - Se il grado massimo è `d_v > 2`, allora `L(k) = L(k-1) + L(k-d_v)`. Per `d_v = 3`, il costo è `O(1.464^k * poly(n))`.
    - Combinando con la kernelization: `O(1.41^k * poly(k) + poly(n))`.

---

### Maggio 19, 2025

**MAX-CUT (Approfondimenti)**

- **Randomization (2-coloring):**
    
    - Assegna ogni nodo `u` a `S` con probabilità `1/2` o a `S̄` con probabilità `1/2`.
    - La probabilità che un arco `ij` sia nel cutset è `1/2` (se `i` e `j` hanno colori diversi).
    - Il valore atteso `E[|E(S, S̄)|] = |E|/2`.
- **Derandomization:** Convertire un algoritmo randomizzato in uno deterministico che abbia almeno la stessa performance attesa (o migliore).
    
    1. **Tecnica 1: Universal Hash Family**
        
        - Invece di provare tutte le `2^n` 2-colorazioni (costo esponenziale), si può usare una famiglia di hash universale.
        - Scegliere `h ∈ H` dove `h: V -> {0,1}` (m=2).
        - `color(u) = h(u)`.
        - Poiché `h` è universale, `Pr[h(i) ≠ h(j)] = 1/2` per `i ≠ j`.
        - Il numero di funzioni in una famiglia universale è `O(n^2)`.
        - Algoritmo deterministico:
            - `best_cutsize = 0`.
            - Per ogni possibile `h ∈ H`:
                - Calcola `cutsize` per la 2-colorazione indotta da `h`.
                - Se `cutsize > best_cutsize`, aggiorna `best_cutsize`.
            - `return best_cutsize`.
        - Questo riduce il numero di 2-colorazioni da `2^n` a `O(n^2)`, preservando la probabilità che un arco sia nel cutset.
    2. **Tecnica 2: Conditional Expectations**
        
        - `E[X] ≤ max(E[X|Y], E[X|¬Y])`.
        - Si decide il colore di un nodo alla volta, scegliendo per ogni nodo il colore che massimizza il valore atteso del cutset condizionato dalle scelte precedenti.
        - Passo `i`: decidere il colore per il nodo `i`, dato che i nodi `1, ..., i-1` sono già stati colorati.
        - Si calcola `E[cutsize | nodi 1..i-1 colorati, nodo i = color X]` e `E[cutsize | nodi 1..i-1 colorati, nodo i = color Y]` e si sceglie il massimo.
        - Il numero di scelte è `2*n` anziché `2^n`.
        - Questo approccio porta all'algoritmo **Greedy** per Max-Cut.

---

### Maggio 21, 2025

**FPT (Fixed-Parameter Tractable) Algorithms**

- **Obiettivo:** Risolvere problemi NP-hard in `O(f(k) * n^O(1))` tempo.
    
    - `n` è la dimensione dell'input, `k` è un parametro rilevante (piccolo).
    - `f(k)` è una funzione che dipende solo da `k` e può essere molto grande (esponenziale), ma la dipendenza da `n` è polinomiale.
- **Randomization in FPT Algorithms (Monte Carlo):**
    
    1. **Color Coding:**
        
        - **Esempio: k-path** (trovare un cammino semplice di `k` nodi in un grafo `G`). Questo è NP-hard (Hamiltonian Path è un caso speciale quando `k=n`).
        - **Idea:** Assegna casualmente un colore `χ(u) ∈ [k]` a ogni nodo `u ∈ G` (random k-coloring).
        - Un sottoinsieme `V' ⊆ V` è **COLORFUL** se tutti i nodi in `V'` hanno colori distinti.
        - **Proprietà:** Un cammino di `k` nodi è un `k`-path se e solo se esiste una `k`-colorazione tale che il cammino sia colorful.
        - **Probabilità che un `k`-path dato `V'` sia COLORFUL:** `Pr[V' is COLORFUL] = k! * ( (n-k)! / n! ) * (1/k)^k`. La probabilità è `k! / k^k * (n-k)! / n!`. Che è `e^(-k)` per `k` grande.
        - **Algoritmo con Dynamic Programming:**
            - `PATH[i][S]` = `TRUE` se esiste un cammino colorful di lunghezza `|S|` che termina in `i` e usa i colori nell'insieme `S`.
            - Ricorsione: `PATH[u][S] = OR_{v ∈ N(u)} PATH[v][S \ {χ(u)}]` se `χ(u) ∈ S`.
            - Costo: `O(k * 2^k * n * m)` o `O(k * 2^k * n^2)`.
            - Per trovare un `k`-path (se esiste) con probabilità costante, si eseguono `O(e^k)` colorazioni casuali.
            - Costo totale: `O(e^k * k * 2^k * n^2) = O((2e)^k * n^2)`. Questo è FPT.
    2. **Randomized Separation:**
        
        - **Esempio: Subgraph Isomorphism** (trovare se `H` è un sottografo isomorfo a un sottografo di `G`).
        - **Parametrizzazione:** `k = |VH|` (numero di nodi in H). Non è FPT a meno che P=NP. `k = |VH|`, `Δ_H = max_degree(H)` (grado massimo in H). Questo è FPT.
        - **Idea:** Disconnettere `H` dal resto di `G` usando una 2-colorazione casuale degli archi.
        - Una 2-colorazione `χ: E -> {Red, Blue}` è **SUCCESSFUL** se:
            - Tutti gli archi in `E_H` (gli archi di H nel sottografo di G) hanno lo stesso colore (es. Red).
            - Tutti gli archi `M` che connettono `H` al resto di `G` hanno il colore opposto (es. Blue).
        - **Algoritmo FPT:**
            - Ripeti `2^k` volte.
            - Esegui una 2-colorazione casuale degli archi di `E`.
            - Costruisci `G_R` (parte di `G` indotta dagli archi Red) e `G_B` (parte di `G` indotta dagli archi Blue).
            - Per ogni componente connessa `C` di `G_R` e `G_B`: controlla se `C` è isomorfa a `H`. Se sì, restituisci `C` e termina.
            - Costo del controllo di isomorfismo: `O(k! * k^2)`.
            - Costo totale: `O(2^k * k! * k^2 * poly(n))`. Questo è FPT.

---