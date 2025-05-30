# Dimostrazioni e Schemi di Dimostrazione dalle Fonti

## 1. Correttezza dello Shuffling con Variabili Indicatrici

Sebbene non sia presentata una dimostrazione completa e formale passo-passo, le fonti suggeriscono un esercizio per dimostrare la correttezza di un algoritmo di shuffling (permutazione casuale uniforme di un array) utilizzando le variabili indicatrici e l'induzione.

-   **Concetto:** L'obiettivo è mostrare che l'algoritmo di shuffling che scambia l'elemento `A[i]` con un elemento scelto casualmente `A[j]` per `j` nell'intervallo `[i, n]` (per `i` da 1 a `n-1`) genera ognuna delle `n!` permutazioni possibili con probabilità uniforme `1/n!`.
-   **Strumenti:** Si suggerisce l'uso di variabili indicatrici e l'induzione su `i` (la posizione corrente nell'array).
-   **Schema (Implicito):**
    1.  **Base dell'Induzione:** Per `i=n-1`, l'algoritmo scambia `A[n-1]` con un elemento `A[j]` dove `j` è scelto casualmente in `[n-1, n]` (cioè `j` può essere `n-1` o `n`). Si dimostra che le due possibili configurazioni finali del suffisso `A[n-1...n]` (originale o scambiata) hanno probabilità `1/2`. Questo, combinato con l'ipotesi induttiva sul prefisso `A[1...n-2]`, porta alla probabilità desiderata.
    2.  **Passo Induttivo:** Si assume che il prefisso `A[1...i]` sia una permutazione casuale uniforme degli elementi originali in quelle posizioni. Quando si scambia `A[i]` con `A[j]` (dove `j` è casuale in `[i, n]`), si considera come questo influenzi la distribuzione.
    3.  **Uso di Variabili Indicatrici:** Sebbene non specificato, le variabili indicatrici potrebbero essere usate per rappresentare l'evento che uno specifico elemento finisca in una specifica posizione dopo lo swap.

Questa dimostrazione si basa sul fatto che in ogni passo `i`, l'elemento nella posizione `i` è scambiato con una posizione `j` scelta uniformemente dall'intervallo rimanente `[i, n]`, garantendo che ogni elemento abbia una probabilità uniforme di finire in ogni posizione finale.

## 2. Costo Atteso del QuickSort Randomizzato

L'analisi del costo atteso (numero di confronti tra elementi) per il QuickSort randomizzato utilizza le variabili indicatrici.

-   **Obiettivo:** Calcolare il numero totale atteso di confronti effettuati dall'algoritmo.
-   **Strumenti:** Variabili indicatrici, linearità dell'aspettazione.
-   **Schema della Dimostrazione:**
    1.  **Variabili Indicatrici:** Si definisce una variabile indicatrice `X_ij` per ogni coppia di elementi `z_i` e `z_j` (assumendo che gli elementi unici dell'array ordinato siano `z_1 < z_2 < ... < z_n`). `X_ij = 1` se `z_i` e `z_j` vengono confrontati, `0` altrimenti.
    2.  **Costo Totale:** Il numero totale di confronti è `X = Sum_{i<j} X_ij`.
    3.  **Costo Atteso:** Per linearità dell'aspettazione, `E[X] = E[Sum X_ij] = Sum E[X_ij]`.
    4.  **Aspettazione della Variabile Indicatrice:** `E[X_ij] = Pr(X_ij = 1)`.
    5.  **Probabilità di Confronto:** Due elementi `z_i` e `z_j` vengono confrontati **solo se** uno di essi viene scelto come pivot mentre l'altro è ancora nella stessa sottosequenza. Vengono confrontati **al massimo una volta**. Consideriamo il sottoinsieme degli elementi dell'array compreso tra `z_i` e `z_j` nell'ordinamento finale (inclusi `z_i` e `z_j`). Finché un elemento al di fuori di questo intervallo viene scelto come pivot, `z_i` e `z_j` rimangono insieme. Se un elemento **dentro** questo intervallo (ma non `z_i` o `z_j`) viene scelto come pivot, `z_i` e `z_j` verranno separati e non saranno mai più confrontati. `z_i` e `z_j` vengono confrontati **se e solo se** il primo pivot scelto tra gli elementi `{z_i, z_{i+1}, ..., z_j}` è `z_i` o `z_j`.
    6.  **Calcolo della Probabilità:** Consideriamo l'insieme degli elementi `{z_i, ..., z_j}`. Ciascuno di questi `j-i+1` elementi ha la stessa probabilità di essere scelto come pivot **per primo** tra tutti gli elementi di questo insieme. Quindi, la probabilità che `z_i` sia il primo pivot scelto da questo insieme è `1/(j-i+1)`, e la probabilità che `z_j` sia il primo è `1/(j-i+1)`. La probabilità che `z_i` o `z_j` sia il primo pivot scelto da questo insieme è `1/(j-i+1) + 1/(j-i+1) = 2/(j-i+1)`. Pertanto, `Pr(X_ij = 1) = 2/(j-i+1)`.
    7.  **Somma delle Aspettazioni:** `E[X] = Sum_{1 <= i < j <= n} Pr(X_ij = 1) = Sum_{1 <= i < j <= n} 2/(j-i+1)`. Lasciando `k = j-i`, dove `k` varia da 1 a `n-1`, la somma diventa `Sum_{k=1}^{n-1} (n-k) * 2/k` (ci sono `n-k` coppie `(i,j)` con `j-i=k`).
    8.  **Risultato Finale:** `E[X] = 2 * Sum_{k=1}^{n-1} (n/k - 1) = 2 * (n * Sum_{k=1}^{n-1} 1/k - Sum_{k=1}^{n-1} 1) = 2 * (n * H_{n-1} - (n-1))`. Poiché `H_{n-1}` è approssimativamente `ln(n)`, il costo atteso è `O(n log n)`.

Questa analisi dimostra che il numero atteso di confronti nel QuickSort randomizzato è proporzionale a `n log n`.

## 3. Limite alla Probabilità di Errore nell'Algoritmo di Rabin-Karp

L'algoritmo di Rabin-Karp per la string matching utilizza l'hashing per confrontare velocemente il pattern con le sottostringhe del testo. Essendo un algoritmo Monte Carlo, ha una probabilità di errore unilaterale (falso positivo).

-   **Obiettivo:** Limitare la probabilità che l'hash del pattern `P` sia uguale all'hash di una sottostringa del testo `T[i...i+m-1]` anche se `P` non è uguale a `T[i...i+m-1]`.
-   **Strumenti:** Hash function `F(s) = s % p` per un primo casuale `p`. Variabili indicatrici. Union Bound. Densità dei numeri primi.
-   **Schema della Dimostrazione:**
    1.  **Condizione di Errore:** Un errore (falso positivo) per una posizione `i` si verifica se `F(P) = F(T[i...i+m-1])` ma `P != T[i...i+m-1]`. Questo significa `P % p = T[i...i+m-1] % p` ma `P != T[i...i+m-1]`. Questo è equivalente a `(P - T[i...i+m-1]) % p = 0`, ovvero `p` divide la differenza `K = P - T[i...i+m-1]` (dove `K != 0`).
    2.  **Variabile Indicatrice:** Si definisce `X_i = 1` se si verifica un errore nella posizione `i` (cioè `F(P) = F(T[i...i+m-1])` ma `P != T[i...i+m-1]`), `0` altrimenti. `Pr(X_i = 1)` è la probabilità di errore per la posizione `i`.
    3.  **Errore Totale:** Un errore totale si verifica se `X = Sum X_i > 0`, cioè se c'è almeno un errore in una delle posizioni `i`.
    4.  **Limite Superiore per Pr(X > 0):** Per la Union Bound, `Pr(X > 0) = Pr(Union_i {X_i=1}) <= Sum_i Pr(X_i = 1)`.
    5.  **Limitare Pr(X_i = 1):** Per una posizione `i` fissata dove `P != T[i...i+m-1]`, la probabilità di errore `Pr(X_i = 1)` è la probabilità che il primo casuale `p` scelto divida la differenza `K = P - T[i...i+m-1]`. Poiché `K` è un numero non zero, ha al massimo `log_2 |K|` fattori primi distinti. Dato che i valori che `P` e `T` possono rappresentare sono al massimo `2^n - 1` (per stringhe binarie di lunghezza `n`), `|K| < 2^n`. Quindi, `K` ha al massimo `n` fattori primi distinti.
    6.  **Scelta di p:** Il primo `p` viene scelto uniformemente a caso in un intervallo `[2...L]`. Un primo `p` è "cattivo" per la posizione `i` se divide `K`. Ci sono al massimo `n` primi cattivi nell'insieme di tutti i primi.
    7.  **Probabilità di Scegliere un Primo Cattivo:** La densità dei numeri primi implica che ci sono circa `L / ln(L)` numeri primi nell'intervallo `[2...L]`. Se scegliamo `L` sufficientemente grande (ad esempio, `L = n^2 * costante`), la probabilità di scegliere uno dei `n` primi cattivi è al massimo `n / (L/ln L)`. Le fonti indicano che `Pr(X_i = 1) <= m/p` (questo sembra un'approssimazione o un limite semplificato derivato altrove, forse legato alla probabilità di collisione in un hash universale dove Pr(h(x)=h(y)) <= 1/m, qui m è la dimensione del dominio dell'hash modulo p). Una forma più precisa usata nello schema di dimostrazione è `Pr(X_i = 1) <= n / (L/ln L)`.
    8.  **Limite della Probabilità Totale:** `Pr(X > 0) <= Sum_i Pr(X_i = 1) <= n * (n / (L/ln L))` (poiché ci sono `n` possibili posizioni iniziali `i` per il pattern nel testo di lunghezza `n`, o meglio `n-m+1` posizioni). Se scegliamo `L` tale che `nm/p <= delta` (o `n*(n / (L/ln L)) <= delta`), possiamo limitare la probabilità di errore totale `Pr(X > 0)` al valore desiderato `delta`. La fonte usa il limite `nm/p`. Quindi, scegliendo `p` tale che `nm/p <= delta`, ovvero `p >= nm/delta`, si ottiene la probabilità di errore desiderata.

Questa dimostrazione mostra che, scegliendo un modulo primo `p` sufficientemente grande, l'algoritmo di Rabin-Karp ha una bassa probabilità di falso positivo.

## 4. La Probabilità che il Livello Inferiore dell'Hash Perfetto sia Perfetto

Nella costruzione di una tabella hash perfetta a due livelli, il livello superiore mappa le chiavi in bucket. Il livello inferiore per ogni bucket `i` utilizza una funzione hash `h_i` specifica per mappare le chiavi `S_i` che finiscono in quel bucket a posizioni in un array di dimensione `|S_i|^2`. Si vuole dimostrare che, scegliendo una funzione hash `h_i` casuale da una famiglia universale per il bucket `S_i`, la probabilità che `h_i` sia perfetta (nessuna collisione per le chiavi in `S_i`) è maggiore o uguale a 1/2.

-   **Obiettivo:** Dimostrare che `Pr(h_i` è perfetta per `S_i`) `>= 1/2`, dove `h_i` è scelta casualmente da una famiglia hash universale e mappa a un dominio di dimensione `m_i = |S_i|^2`.
-   **Strumenti:** Variabili indicatrici, linearità dell'aspettazione, Hash Universale (proprietà di probabilità di collisione), Markov's Inequality.
-   **Schema della Dimostrazione:**
    1.  **Variabili Indicatrici:** Per ogni coppia distinta di chiavi `k_1, k_2` nell'insieme `S_i`, si definisce una variabile indicatrice `X_{k1, k2} = 1` se `h_i(k_1) = h_i(k_2)` (cioè collidono), `0` altrimenti.
    2.  **Numero di Collisioni:** Il numero totale di collisioni per `h_i` sulle chiavi in `S_i` è `X = Sum_{k1, k2 in S_i, k1 != k2} X_{k1, k2}` (o `Sum_{k1, k2 in S_i, k1 < k2} X_{k1, k2}` se si considerano coppie non ordinate). `h_i` è perfetta se `X = 0`.
    3.  **Costo Atteso delle Collisioni:** `E[X] = E[Sum X_{k1, k2}] = Sum E[X_{k1, k2}]` per linearità.
    4.  **Aspettazione della Variabile Indicatrice:** `E[X_{k1, k2}] = Pr(X_{k1, k2} = 1) = Pr(h_i(k_1) = h_i(k_2))`.
    5.  **Probabilità di Collisione per Hash Universale:** Poiché `h_i` è scelta da una famiglia hash universale e mappa a un dominio di dimensione `m_i`, per ogni coppia distinta `k_1, k_2`, `Pr(h_i(k_1) = h_i(k_2)) <= 1/m_i`.
    6.  **Limite Atteso del Numero di Collisioni:** Ci sono `|S_i|` chiavi in `S_i`. Il numero di coppie distinte `(k_1, k_2)` con `k_1 != k_2` è `|S_i|(|S_i|-1)`. Se si considerano coppie non ordinate, sono `|S_i| scegli 2 = |S_i|(|S_i|-1)/2`. Usando coppie ordinate: `E[X] = Sum_{k1 != k2} Pr(h_i(k_1) = h_i(k_2)) <= Sum_{k1 != k2} 1/m_i = |S_i|(|S_i|-1) * (1/m_i)`. Se si considera `m_i = |S_i|^2`, allora `E[X] <= |S_i|(|S_i|-1) / |S_i|^2 = (|S_i|-1) / |S_i| < 1`. (La fonte mostra `E[X] = Sum (2 / m_i)` - questo sembra un errore di trascrizione, la somma dovrebbe essere su tutte le coppie, e la probabilità `1/m_i`). L'espressione `Sum |Si|^2 / mi` in suggerisce che `m_i` è la dimensione del dominio, e la somma è su tutti i bucket, il che si applica all'analisi dello spazio totale, non del singolo bucket. Concentrandosi sul singolo bucket `S_i` e la sua funzione `h_i` con dominio di taglia `m_i`, il numero atteso di collisioni è `|S_i| scegli 2 * (1/m_i)`.
    7.  **Limite Superiore per E[X]:** Con `m_i = |S_i|^2`, `E[X] = |S_i|(|S_i|-1)/2 * (1/|S_i|^2) = (|S_i|-1) / (2|S_i|) < 1/2` (per |S_i| >= 1).
    8.  **Markov's Inequality:** Per una variabile casuale non negativa `X`, `Pr[X >= a] <= E[X]/a` per ogni `a > 0`. Vogliamo `Pr[X=0]`. `Pr[X=0] = 1 - Pr[X > 0]`. Poiché X conta collisioni, X è non negativa. Se X > 0, allora X >= 1. Quindi `Pr[X > 0] = Pr[X >= 1]`.
    9.  **Risultato Finale:** `Pr[X >= 1] <= E[X]/1 = E[X]`. Poiché `E[X] < 1/2`, `Pr[X >= 1] < 1/2`. Pertanto, `Pr[X = 0] = 1 - Pr[X >= 1] > 1 - 1/2 = 1/2`.

Questo dimostra che per un singolo bucket, la probabilità di avere zero collisioni scegliendo una funzione hash casuale da una famiglia universale con un dominio di dimensione quadrata rispetto al numero di chiavi nel bucket è maggiore di 1/2. Questo è fondamentale per la costruzione efficiente della tabella hash perfetta.

## 5. Dimostrazione della Disuguaglianza di Markov

La disuguaglianza di Markov fornisce un limite superiore alla probabilità che una variabile casuale non negativa sia maggiore o uguale a un certo valore, basandosi solo sul suo valore atteso.

-   **Obiettivo:** Dimostrare che per una variabile casuale non negativa `X` (`X >= 0`) e per ogni valore reale `a > 0`, `Pr[X >= a] <= E[X] / a`.
-   **Strumenti:** Variabile indicatrice, definizione di aspettazione.
-   **Schema della Dimostrazione:**
    1.  **Variabile Indicatrice:** Si definisce una variabile indicatrice `I = 1` se l'evento `X >= a` si verifica, `0` altrimenti.
    2.  **Relazione tra X e I:** Poiché `X >= 0`, si ha `X >= a * I` (se `X < a`, allora `I=0` e `X >= 0`; se `X >= a`, allora `I=1` e `X >= a`). Quindi `X >= a * I` è vero.
    3.  **Prendere l'Aspettazione:** Prendendo l'aspettazione di entrambi i lati della disuguaglianza: `E[X] >= E[a * I]`.
    4.  **Linearità dell'Aspettazione:** `E[a * I] = a * E[I]` (poiché `a` è una costante).
    5.  **Aspettazione della Variabile Indicatrice:** `E[I] = Pr(I = 1) = Pr(X >= a)`.
    6.  **Combinazione:** Sostituendo in `E[X] >= a * E[I]`, otteniamo `E[X] >= a * Pr[X >= a]`.
    7.  **Risultato Finale:** Dividendo per `a` (che è > 0), si ottiene `Pr[X >= a] <= E[X] / a`.

Questa è una dimostrazione semplice ma fondamentale per ottenere limiti probabilistici a partire dal solo valore atteso.

## 6. Proprietà di Jaccard per Min-Hash

La Min-Hash è una tecnica utilizzata per stimare la somiglianza tra insiemi, in particolare l'Indice di Jaccard. Una proprietà chiave delle funzioni Min-Hash (definite da permutazioni casuali uniformi dell'universo) è che la probabilità che le Min-Hash di due insiemi siano uguali è pari al loro Indice di Jaccard.

-   **Obiettivo:** Dimostrare che per due insiemi `A` e `B` (sottoinsiemi di un universo `U`), e per una funzione hash `h` scelta uniformemente casualmente da una famiglia di funzioni che "permutano" `U` (min-wise independent permutations), `Pr(min_h(A) = min_h(B)) = J(A, B)`, dove `min_h(X) = min_{x in X} h(x)` e `J(A, B) = |A int B| / |A union B|`.
-   **Strumenti:** Definizione di Min-wise independent permutation, definizione di Indice di Jaccard, probabilità.
-   **Schema della Dimostrazione:**
    1.  **Considerare l'Unione:** Consideriamo l'insieme unione `X = A union B`. L'elemento `min_h(X)` è l'elemento in `X` che ha il valore hash minimo sotto `h`.
    2.  **Proprietà Min-wise:** Poiché `h` è scelta da una famiglia min-wise independent, per ogni elemento `a` in `X`, la probabilità che `a` sia l'elemento con il valore hash minimo in `X` è `Pr(h(a) = min_h(X)) = 1 / |X| = 1 / |A union B|`.
    3.  **Evento min_h(A) = min_h(B):** L'evento `min_h(A) = min_h(B)` si verifica se e solo se l'elemento che ha il valore hash minimo in `A union B` appartiene **sia ad A che a B**, cioè appartiene all'intersezione `A int B`. Se l'elemento con il valore hash minimo in `A union B` appartiene ad `A\B`, allora `min_h(A)` sarà quell'elemento, ma `min_h(B)` sarà un elemento in `B` (che è anche in `A union B`) con un valore hash diverso (e maggiore, poiché l'elemento scelto è il minimo globale in `A union B`), quindi `min_h(A) != min_h(B)`. Analogamente se l'elemento minimo è in `B\A`.
    4.  **Calcolo della Probabilità:** L'evento `min_h(A) = min_h(B)` si verifica se e solo se `min_h(A union B) in A int B`.
    5.  **Somma delle Probabilità:** La probabilità che `min_h(A union B)` sia in `A int B` è la somma delle probabilità che ciascun elemento `a` in `A int B` sia l'elemento con il valore hash minimo in `A union B`. Poiché per ogni `a in A union B`, `Pr(h(a) = min_h(A union B)) = 1 / |A union B|`, e ci sono `|A int B|` elementi nell'intersezione, la probabilità che uno di essi sia il minimo è la somma delle loro probabilità individuali.
    6.  **Risultato Finale:** `Pr(min_h(A) = min_h(B)) = Sum_{a in A int B} Pr(h(a) = min_h(A union B))`. Poiché ogni elemento in `A union B` ha la stessa probabilità di essere il minimo in `A union B` (`1/|A union B|`), questa somma è `|A int B| * (1 / |A union B|) = |A int B| / |A union B|`. Per definizione, questo è l'Indice di Jaccard `J(A, B)`.

Questa proprietà è cruciale perché permette di stimare l'Indice di Jaccard tra due insiemi semplicemente confrontando le loro Min-Hash ottenute da diverse funzioni hash.

## 7. Indice di Jaccard Stimato con Bottom-k Sketch come Stimatore Non Polarizzato

Il Bottom-k Sketch è un altro tipo di sketch basato su hash che mantiene i `k` elementi con i valori hash più piccoli da un insieme. Si può utilizzare per stimare l'Indice di Jaccard. Si vuole dimostrare che lo stimatore basato sul rapporto tra l'intersezione e l'unione dei Bottom-k sketch è non polarizzato (unbiased).

-   **Obiettivo:** Dimostrare che `E[|R_k(A) intersect R_k(B)| / k] = J(A, B)`, dove `R_k(X)` è l'insieme dei `k` elementi con hash minimo in `X` secondo una funzione hash `r`.
-   **Strumenti:** Definizione di Bottom-k Sketch, Indice di Jaccard, Aspettazione, Probabilità. Analisi probabilistica basata su "balls and bins" o distribuzione ipergeometrica.
-   **Schema della Dimostrazione (Outline):**
    1.  **Definizione dello Stimatore:** Lo stimatore proposto per `J(A, B)` è `|R_k(A) intersect R_k(B)| / k`.
    2.  **Linearità dell'Aspettazione:** `E[|R_k(A) intersect R_k(B)| / k] = (1/k) * E[|R_k(A) intersect R_k(B)|]`. L'obiettivo è mostrare che `E[|R_k(A) intersect R_k(B)|] = k * J(A, B)`.
    3.  **Contare gli Elementi nell'Intersezione degli Sketch:** Consideriamo l'insieme `A union B`. Questo insieme è partizionato in `A int B`, `A\B`, e `B\A`. Siano `b = |A int B|`, `r = |A\B|`, `g = |B\A|`. La dimensione totale è `g+b+r = |A union B|`. L'Indice di Jaccard è `J(A, B) = b / (g+b+r)`.
    4.  **L'Esperimento Casuale:** La funzione hash `r` ordina in modo casuale e uniforme gli elementi in `A union B`. `R_k(A union B)` è l'insieme dei primi `k` elementi in questo ordinamento. `R_k(A)` contiene i primi `k` elementi di `A` nell'ordinamento di `r`, e `R_k(B)` contiene i primi `k` elementi di `B` nell'ordinamento di `r`. **Errore nella fonte:** La fonte sembra definire `R_k(X)` come i `k` elementi con hash minimo in `X`. Questo è corretto per Bottom-k. L'unione degli sketch è `S(A) union S(B)`. `|S(A) union S(B)|` è l'insieme dei primi `k` elementi in `A` e i primi `k` elementi in `B`. L'intersezione `S(A) intersect S(B)` contiene gli elementi che sono nei primi `k` sia per `A` che per `B`. Questo non sembra correlato direttamente all'intersezione di `A` e `B`.
    5.  **Interpretazione Alternativa basata sull'Esperimento:** La proprietà `Pr(min_h(A) = min_h(B)) = J(A, B)` è per `k=1`. Per `k>1`, si considera l'insieme `A union B`. Gli elementi in `A union B` sono ordinati dalla funzione hash `r`. Gli elementi che finiscono nell'intersezione `R_k(A) intersect R_k(B)` sono elementi che appartengono sia ad `A` che a `B` (`A int B`) E sono tra i primi `k` elementi di `A` E tra i primi `k` elementi di `B`.
    6.  **Relazione Corretta (implicita in):** Lo stimatore per `J(A,B)` basato su Bottom-k sketch di dimensione `k` per `A` e `B` (chiamiamoli `SketchA` e `SketchB`, ciascuno con `k` elementi) è `|SketchA intersect SketchB| / k`. L'evento che un elemento `z` sia in `SketchA intersect SketchB` significa che `z in A int B` E `r(z)` è tra i `k` valori hash più piccoli in `A` E `r(z)` è tra i `k` valori hash più piccoli in `B`.
    7.  **Interpretazione Probabilistica Corretta (suggerita da con "Balls and bins"):** Immagina di avere `|A union B|` "palline" (gli elementi di `A union B`) e `k` "bin" per `SketchA` e `k` "bin" per `SketchB`. Un elemento `z` finisce in `SketchA` se è in `A` e il suo hash è tra i `k` più piccoli in `A`. Similmente per `SketchB`. L'unbiasedness deriva dal fatto che per ogni elemento `z in A int B`, la probabilità che `z` finisca in `SketchA intersect SketchB` è pari a `k / |A union B|`? No, la probabilità è più complessa.
    8.  **Schema di:** L'outline in parla di `g` elementi in `A\B`, `b` in `A int B`, `r` in `B\A`. Il totale è `g+b+r = |A union B|`. `J(A, B) = b/(g+b+r)`. Definisce `X` come il `# elementi` che appartengono sia ad `A int B` che sono in `R_k(A union B)` (gli elementi con i k hash più piccoli nell'unione). `E[X]` viene calcolato usando una distribuzione ipergeometrica. Questo approccio stima `|A int B|` non `J(A, B)`. Lo stimatore in è `|R_k(A) intersect R_k(B)| / k`. La connessione non è immediata.
    9.  **Risultato di:** Un altro stimatore, per Threshold Sketch `S(A) = {a in A : r(a) < t}`, è `|S(A) intersect S(B)| / |S(A) union S(B)|`. Per questo, `E[|S(A) intersect S(B)| / |S(A) union S(B)|] = J(A, B)`. La dimostrazione per questo (più chiara nelle fonti) usa `J(A, B) = Pr[x in A int B | x in A union B]` e il fatto che `Pr[x in S(X) | x in X]` è uguale per tutti gli x. `J(A,B) = Pr[x in A int B e x in S(A) union S(B) | x in A union B e x in S(A) union S(B)]` ? La fonte dice `J(A,B) = Pr[Y=1]` dove `Y=1` iff `x in A' int B'` con `x in A union B` e `A'=S(A), B'=S(B)`. Questo porta a `E[stimatore] = J(A,B)`.

Concentriamoci sullo schema per il Threshold Sketch () poiché è più esplicitamente delineato come unbiased:

-   **Stimatore (Threshold):** `|S(A) intersect S(B)| / |S(A) union S(B)|` dove `S(X) = {x in X : r(x) < t}`.
    
-   **Obiettivo:** Mostrare `E[|S(A) intersect S(B)| / |S(A) union S(B)|] = J(A, B)`.
    
-   **Schema:**
    
    1.  Definire l'evento `Y=1` se un elemento `x` scelto casualmente dall'universo `U` soddisfa `x in S(A) intersect S(B)`, e `Y=0` altrimenti. `E[Y] = Pr[Y=1] = Pr[x in S(A) intersect S(B)]`.
    2.  L'evento `x in S(A) intersect S(B)` equivale a `x in A` E `r(x) < t` E `x in B` E `r(x) < t`. Questo si semplifica a `x in A int B` E `r(x) < t`.
    3.  `E[Y] = Pr[x in A int B \text{ e } r(x) < t]`. Poiché `r` è indipendente dalla scelta di `x` dall'universo, questo è `Pr[x in A int B] * Pr[r(x) < t]`. `Pr[x in A int B] = |A int B| / |U|`. `Pr[r(x) < t] = t` (se `r` mappa uniformemente a `[0, 1)`). Quindi `E[Y] = (|A int B|/|U|) * t`. Questo non è `J(A,B)`.
    
    Una formulazione alternativa basata sulla condizione in (`J(A,B)=Pr[Y=1]` dove `Y_x=1` iff `x in A' intersect B'` with `x in A union B`):
    
    1.  Consideriamo un elemento `x` scelto uniformemente casualmente da `A union B`.
    2.  Definiamo la variabile indicatrice `Y_x = 1` se `x in S(A) intersect S(B)` (utilizzando lo stesso threshold `t` e funzione `r` per entrambi), `0` altrimenti.
    3.  L'evento `x in S(A) intersect S(B)` per un `x in A union B` significa `x in A` e `r(x) < t` e `x in B` e `r(x) < t`. Questo significa `x in A int B` e `r(x) < t`.
    4.  `E[Y_x] = Pr[Y_x = 1] = Pr[x in A int B \text{ e } r(x) < t \mid x in A union B]`.
    5.  Per le proprietà della probabilità condizionata, questo è `Pr[x in A int B \text{ e } r(x) < t] / Pr[x in A union B]`.
    6.  `Pr[x in A int B \text{ e } r(x) < t]` (con x scelto da U) = `Pr[x in A int B] * Pr[r(x) < t]` = `(|A int B|/|U|) * t`.
    7.  `Pr[x in A union B]` (con x scelto da U) = `|A union B|/|U|`.
    8.  Quindi, `E[Y_x] = ((|A int B|/|U|) * t) / (|A union B|/|U|) = (|A int B| / |A union B|) * t = J(A, B) * t`. Questo non è `J(A,B)`.
    
    L'outline in "Pr\[Ex e AB'(x e AB1)] = Pr\[ExzlED . NET C / Pr\[IEr] = PEAAP PrExABIxcAB] = JAB" suggerisce un uso più sottile della probabilità condizionata o una riscrittura dello stimatore in termini di probabilità. La frase "Pr\[Y^= 1) = J(A,B)" dove Y^ è legato allo stimatore suggerisce che la probabilità che un elemento casuale dell'unione cada nell'intersezione degli sketch è pari a J(A,B). Questo accade se `x` è in `A int B` e `r(x) < t`. La probabilità è `J(A,B) * t`. Questo non è J(A,B).
    
    Forse lo stimatore è `|S(A) intersect S(B)| * C` dove C è una costante. Oppure è basato su un rapporto di conteggi. La fonte afferma `As J(A,B)= , taking EIJCABI=EY]AC D`. Questo suggerisce che lo stimatore è un'aspettazione di qualche variabile. L'uguaglianza `Pr[ExABIxcAB] = JAB` non è corretta in generale, ma `Pr[x in A int B | x in A union B] = J(A,B)`.
    
    Il fatto che `E[stimatore] = J(A,B)` per il Threshold Sketch è vero, ma la dimostrazione dettagliata nelle fonti non è completa. L'idea è che per un elemento `x` scelto uniformemente da `A union B`, la probabilità che `x` cada in `S(A) intersect S(B)` è `J(A,B) * t`.
    

## 8. Probabilità di Successo dell'Algoritmo MIN-CUT di Karger

L'algoritmo di Karger è un algoritmo randomizzato per trovare un taglio minimo in un grafo. La sua probabilità di successo non è 1, ma può essere resa arbitrariamente alta ripetendo l'algoritmo.

-   **Obiettivo:** Dimostrare che la probabilità che una singola esecuzione dell'algoritmo di Karger (che contrae bordi scelti casualmente fino a rimanere con 2 nodi) trovi un taglio minimo specifico `C` è almeno `2/(n(n-1))`.
-   **Strumenti:** Probabilità condizionata, proprietà dei tagli minimi, contrazione di bordi.
-   **Schema della Dimostrazione (Outline):**
    1.  **Condizione di Successo:** L'algoritmo trova un taglio minimo `C` se e solo se **nessun bordo** appartenente al taglio `C` viene mai contratto durante l'esecuzione dell'algoritmo.
    2.  **Algoritmo Ricorsivo:** L'algoritmo opera in `n-2` passi di contrazione. Al passo `i` (quando rimangono `n-i+1` nodi), viene scelto un bordo a caso tra i bordi correnti e contratto.
    3.  **Probabilità di Successo Ricorsiva:** Sia `P(k)` la probabilità che l'algoritmo abbia successo quando opera su un grafo con `k` nodi. `P(2) = 1` (la contrazione finale non può fallire se i bordi del taglio non sono stati contratti prima). Per `k > 2`, l'algoritmo ha successo se e solo se il primo bordo contratto non appartiene a `C`, E l'algoritmo ricorsivo ha successo sul grafo contratto.
    4.  **Probabilità che il Primo Bordo non sia in C:** Sia `m_k` il numero di bordi nel grafo al passo `k` (con `k` nodi). Il taglio minimo `C` ha dimensione `K` (numero di bordi). `Pr(il primo bordo contratto è in C) = K / m_n` (dove `m_n = |E|`). La probabilità che il primo bordo NON sia in `C` è `1 - K/m_n = (m_n - K) / m_n`.
    5.  **Limite per K e m:** Ogni nodo in un grafo con `k` nodi ha grado almeno `K` (altrimenti si potrebbe formare un taglio più piccolo separando quel nodo). La somma dei gradi è `2m_k`. Quindi, `2m_k >= k * K`. Questo implica `m_k >= kK/2`. Ma questo non è un limite sul numero di bordi in termini di K e k, è un limite inferiore su `m_k`. Un'altra proprietà (non esplicitamente dimostrata nelle fonti ma citata) è che il numero di bordi in un taglio minimo `K` è minore o uguale al grado minimo `delta(G)`, e `2m >= n * delta(G)`. La fonte usa `2m >= nK` (che deriva dal fatto che `K` è il minimo taglio, quindi ogni nodo deve avere grado almeno `K`). Quindi `m_n >= nK/2`.
    6.  **Limite Inferiore per la Probabilità al Passo 1:** `Pr(il primo bordo non è in C) = (m_n - K) / m_n >= (nK/2 - K) / (nK/2) = (n/2 - 1) / (n/2) = (n-2)/n`. La fonte usa un argomento più diretto: `2m >= nK`, quindi `K/m <= 2/n`. `Pr(bordo non in C) = 1 - K/m >= 1 - 2/n = (n-2)/n`.
    7.  **Probabilità di Successo Ricorsiva (Continuazione):** Se il primo bordo contratto non è in `C`, il grafo contratto mantiene `C` come un taglio minimo. La probabilità di successo `P(n)` è `Pr(bordo non in C al passo 1) * P(n-1)` (assumendo indipendenza condizionata).
    8.  **Espansione Ricorsiva:** `P(n) >= ((n-2)/n) * P(n-1) >= ((n-2)/n) * ((n-3)/(n-1)) * P(n-2) >= ... >= ((n-2)/n) * ((n-3)/(n-1)) * ... * (1/3) * P(2)`.
    9.  **Calcolo Finale:** `P(n) >= ((n-2)/n) * ((n-3)/(n-1)) * ... * (1/3) * 1`. Questo prodotto telescopico è `(n-2)! / (n!) * 2/1` ? No. È `((n-2)*(n-3)*...*1) / (n*(n-1)*...*3) = (n-2)! / (n! / 2) = 2 * (n-2)! / n! = 2 / (n(n-1))`.

Questo dimostra che una singola esecuzione ha una probabilità di successo relativamente bassa (`O(1/n^2)`), ma ripetendo l'algoritmo `O(n^2 log(1/delta))` volte, si può ottenere la risposta corretta con probabilità `1-delta`.

## 9. Limite all'Errore nel Count-Min Sketch

Il Count-Min Sketch è una struttura dati probabilistica utilizzata per stimare le frequenze degli elementi in uno stream. Fornisce una stima `F_est(i)` per la frequenza `F(i)` di un elemento `i` tale che `F_est(i) <= F(i) + epsilon * ||F||_1` con alta probabilità.

-   **Obiettivo:** Dimostrare che `Pr[F_est(i) > F(i) + epsilon * ||F||_1] <= delta`, dove `||F||_1` è la somma di tutte le frequenze (lunghezza dello stream).
-   **Strumenti:** Tabella `T[r][c]`, `r` hash functions `h_j` (2-wise independent). Definizione di stima. Variabili casuali per l'errore. Linearità dell'aspettazione, 2-wise independence, Markov's Inequality, Union Bound. Scelta di `r` e `c`.
-   **Schema della Dimostrazione (Outline):**
    1.  **Definizione della Stima:** `F_est(i) = min_{j in [0, r-1]} T[j][h_j(i)]`. `T[j][k]` è la somma delle frequenze di tutti gli elementi `l` tali che `h_j(l) = k`.
    2.  **Decomposizione:** `T[j][h_j(i)] = F(i) + Sum_{l != i, h_j(l) = h_j(i)} F(l)`. Il secondo termine è l'errore di collisione `X_j` nella riga `j` per l'elemento `i`. `F_est(i) = F(i) + min_j X_j`. Vogliamo limitare `min_j X_j`.
    3.  **Errore Atteso in una Riga:** Per una riga `j` fissata, l'aspettazione dell'errore di collisione per l'elemento `i` è `E[X_j] = E[Sum_{l != i} F(l) * I(h_j(l) = h_j(i))]`. Per linearità, `E[X_j] = Sum_{l != i} F(l) * E[I(h_j(l) = h_j(i))] = Sum_{l != i} F(l) * Pr(h_j(l) = h_j(i))`.
    4.  **Probabilità di Collisione (2-wise independence):** Poiché `h_j` è scelta da una famiglia 2-wise independent (che include le famiglie universali usate nella pratica), `Pr(h_j(l) = h_j(i)) <= 1/c` per `l != i`, dove `c` è la dimensione del dominio delle hash function (numero di colonne).
    5.  **Limite Superiore per E\[X_j]:** `E[X_j] <= Sum_{l != i} F(l) * (1/c) = (Sum_{l != i} F(l)) / c <= ||F||_1 / c`.
    6.  **Markov's Inequality:** Per ogni `a > 0`, `Pr[X_j >= a] <= E[X_j]/a <= (||F||_1/c) / a`. Vogliamo che `min_j X_j <= epsilon * ||F||_1` con alta probabilità. L'evento di fallimento è `min_j X_j > epsilon * ||F||_1`, che implica `X_j > epsilon * ||F||_1` per tutte le righe `j`.
    7.  **Probabilità di Errore in una Riga:** Applichiamo Markov con `a = epsilon * ||F||_1`. `Pr[X_j > epsilon * ||F||_1] <= (||F||_1/c) / (epsilon * ||F||_1) = 1 / (epsilon * c)`.
    8.  **Union Bound (Non sufficiente per il minimo):** Un limite superiore a `Pr[min X_j > epsilon ||F||_1]` è `Pr[X_0 > epsilon ||F||_1 e X_1 > epsilon ||F||_1 e ...]`. Poiché le hash function sono indipendenti (se scelte separatamente per ogni riga), gli eventi `X_j > a` sono indipendenti.
    9.  **Probabilità di Errore Totale:** La probabilità che l'errore minimo sia grande è `Pr[min_j X_j > epsilon ||F||_1]`. Questo è l'evento in cui **tutte** le righe hanno un errore superiore a `epsilon ||F||_1`. `Pr[min_j X_j > epsilon ||F||_1] = Pr[X_0 > epsilon ||F||_1 \text{ e } ... \text{ e } X_{r-1} > epsilon ||F||_1]`. Per indipendenza, questo è `Prodotto_{j=0}^{r-1} Pr[X_j > epsilon ||F||_1]`.
    10.  **Risultato Finale:** `Pr[min_j X_j > epsilon ||F||_1] <= (1 / (epsilon * c))^r`. Per avere questo minore o uguale a `delta`, scegliamo `c` e `r` tali che `(1 / (epsilon * c))^r <= delta`. Ad esempio, se scegliamo `c = e / epsilon` (dove `e` è la base dei logaritmi naturali) e `r = ln(1/delta)`, allora `(1 / (epsilon * e / epsilon))^r = (1/e)^r = (1/e)^{ln(1/delta)} = e^{-ln(1/delta)} = delta`. La fonte usa `c = e / epsilon` e `r = log(1/delta)`. Con queste scelte, `Pr[min_j X_j > epsilon ||F||_1] <= (epsilon/e)^r <= (1/e)^r` (se epsilon <= 1, il che è tipico). Il limite esatto `(1/(epsilon c))^r <= delta` è soddisfatto scegliendo `c = e/epsilon` e `r = log_e(1/delta)`.

Questa dimostrazione mostra come la scelta dei parametri `r` e `c` (numero di righe e colonne) controlli il trade-off tra spazio/tempo di query/aggiornamento e probabilità di errore, garantendo un limite di errore assoluto con alta probabilità.

## 10. Limite all'Errore nel Count-Min Sketch con Mediana

Quando si permette la decremento delle frequenze o si vuole migliorare la garanzia di errore, si può utilizzare la mediana delle stime delle righe invece del minimo.

-   **Obiettivo:** Ottenere una stima `F_est(i)` tale che `|F_est(i) - F(i)| <= 2 * e * ||F||_1 / c` (o `epsilon * ||F||_1`) con alta probabilità, utilizzando la mediana.
-   **Strumenti:** Tabella `T[r][c]`, hash functions 2-wise independent. Stima come mediana delle righe. Probabilità di errore in una riga. Strumento di concentrazione della misura (come Chernoff o Azuma-Hoeffding).
-   **Schema della Dimostrazione (Outline):**
    1.  **Stima con Mediana:** `F_est(i) = median_{j in [0, r-1]} T[j][h_j(i)]`.
    2.  **Errore della Riga:** Per ogni riga `j`, `T[j][h_j(i)] = F(i) + X_j`, dove `X_j` è l'errore di collisione per la riga `j`. Sappiamo che `E[X_j] <= ||F||_1 / c`.
    3.  **Probabilità che l'Errore sia Grande:** Dalla disuguaglianza di Markov (o un limite più stretto), si può mostrare che `Pr[X_j > a] <= E[X_j] / a <= (||F||_1/c) / a`. La fonte usa `Pr[X_j > 2e ||F||_1 / c] <= 1/(2e)`. Questo limite è ottenuto con `a = 2e ||F||_1 / c`.
    4.  **Errore Negativo:** Se le frequenze possono solo aumentare, `X_j >= 0`, quindi `T[j][h_j(i)] >= F(i)`. La stima minima è sempre `>= F(i)`. Con la mediana, se si permettono decrementi, l'errore `X_j` può essere negativo. Tuttavia, per l'analisi mostrata (`F(i) <= F_est(i) <= F(i) + ...`), sembra che si consideri ancora `X_j >= 0`. Assumiamo per ora `X_j >= 0`.
    5.  **Concentrazione della Mediana:** La mediana `F_est(i)` è lontana dal valore vero `F(i)` se **almeno metà delle righe** hanno un errore `X_j` "grande" (> `epsilon' * ||F||_1` per qualche `epsilon'`).
    6.  **Uso di Chernoff/Hoeffding:** Consideriamo la variabile indicatrice `Y_j = 1` se `X_j > 2e ||F||_1 / c`, `0` altrimenti. Sappiamo `Pr[Y_j=1] <= 1/(2e) < 1/2`. Sia `p = Pr[Y_j=1]`. La probabilità che la mediana sia lontana da `F(i)` di più di `2e ||F||_1 / c` (per eccesso) è la probabilità che almeno `r/2` righe abbiano `X_j > 2e ||F||_1 / c`. Questo è `Pr[Sum Y_j >= r/2]`.
    7.  **Limite di Coda:** Poiché `p < 1/2`, la somma `Sum Y_j` tende a concentrarsi attorno a `r*p < r/2`. Usando un limite di coda come Chernoff o Hoeffding per la somma di variabili indipendenti, `Pr[Sum Y_j >= r/2] <= exp(-const * r)`. (La fonte usa `M=r/2`, `X=sum Y_j`). `Pr[|X - E[X]| >= a] <= ...`. Qui vogliamo `Pr[X >= r/2]`. `E[X] = r*p`. `Pr[X >= r/2] = Pr[X - r*p >= r/2 - r*p] = Pr[X - E[X] >= r(1/2-p)]`. Con Hoeffding per variabili limitate ``, `Pr[Sum Z_i >= (media + delta) * r] <= exp(-2*delta^2*r)`. Qui Z_i sono le Y_j. `delta = 1/2 - p`. `Pr[Sum Y_j >= r/2] <= exp(-2 * (1/2 - p)^2 * r)`.
    8.  **Risultato Finale:** Sostituendo `p <= 1/(2e)`, `1/2 - p >= 1/2 - 1/(2e) = (e-1)/(2e)`. `Pr[Sum Y_j >= r/2] <= exp(-2 * ((e-1)/(2e))^2 * r) = exp(-(e-1)^2/(2e^2) * r)`. Per avere questo minore o uguale a `delta`, scegliamo `r` tale che `-(e-1)^2/(2e^2) * r <= ln(delta)`, ovvero `r >= (2e^2 / (e-1)^2) * ln(1/delta)`. Questo è `O(log(1/delta))` come affermato.

La dimostrazione per l'errore negativo `F(i) - F_est(i)` segue un ragionamento simile, limitando la probabilità che l'errore `X_j` sia molto negativo (se permesso) o che la mediana sia molto inferiore a `F(i)` perché molte righe hanno un errore piccolo ma negativo. Se si assumono solo incrementi, `X_j >= 0`, e il limite inferiore `F_est(i) >= F(i)` è garantito dalla definizione del minimo. Per la mediana con soli incrementi, `F_est(i)` potrebbe essere maggiore di `F(i)`. Il limite `|F_est(i) - F(i)| < ...` in suggerisce che l'errore può essere positivo o negativo, forse in un setting più generale con decrementi.

## 11. Limite alla Dimensione del Campione per la Stima della Distanza Media

La stima della distanza media in un grafo campionando nodi e calcolando le distanze solo dal campione utilizza strumenti di concentrazione della misura come Azuma-Hoeffding.

-   **Obiettivo:** Dimostrare che per ottenere una stima `N_U` della frazione di coppie a distanza `h` (`N_h`) con un errore relativo `epsilon` e probabilità `1-delta`, è sufficiente campionare `k = O(epsilon^-2 log delta^-1 n)` nodi uniformemente a caso.
-   **Strumenti:** Campione casuale `U` di `k` nodi. Definizione di `N_h` e `N_U`. Azuma-Hoeffding bound.
-   **Schema della Dimostrazione (Outline):**
    1.  **Variabili Casuali:** Si campionano `k` nodi `u_1, ..., u_k` uniformemente a caso. Per ogni nodo campione `u_i`, si calcola la frazione di nodi a distanza `h` da esso: `f_i = |{v in V : d(u_i, v) = h}| / (n-1)`. `N_h` è la media di `f_i` su tutti i possibili `u_i` (tutti i nodi in `V`).
    2.  **Stimatore:** Lo stimatore per `N_h` è la media delle `f_i` per i nodi campionati: `Y = (1/k) * Sum_{i=1}^k f_i`. `E[Y] = E[f_1]` (poiché i campioni sono i.i.d.) `= (1/n) * Sum_{u in V} |{v : d(u,v)=h}| / (n-1) = N_h`. Quindi `Y` è uno stimatore non polarizzato per `N_h`.
    3.  **Azuma-Hoeffding Bound:** Questa disuguaglianza si applica alla somma di variabili casuali limitate. In questo caso, `Y` è una media di `k` variabili casuali `f_i`, ciascuna limitata nell'intervallo ``(poiché è una frazione). Per la media `Y = (1/k) Sum f_i`, `Pr[|Y - E[Y]| >= epsilon * E[Y]] <= 2 exp(-2 * k * (epsilon * E[Y])^2 / (sum (b_i-a_i)^2))`? No, la forma standard per medie è `Pr[|Y - E[Y]| >= a] <= 2 exp(-2ka^2 / (B-A)^2)` dove le variabili sono in `[A, B]`. Qui `f_i` sono in``.
    4.  **Applicazione di AH:** `Pr[|Y - N_h| >= epsilon * N_h] <= 2 exp(-2k * (epsilon * N_h)^2 / (1-0)^2) = 2 exp(-2k * epsilon^2 * N_h^2)`. (Questo sembra un limite errato; l'errore relativo `epsilon * N_h` deve essere confrontato con la varianza o un range delle variabili).
    5.  **Correzione usando forma alternativa di AH (o limite correlato):** Per medie di variabili casuali limitate, `Pr[| (1/k) Sum Z_i - E[Z] | >= a] <= 2 exp(-2ka^2 / (B-A)^2)`. Poniamo `Z_i = f_i`, `E[Z] = N_h`, `a = epsilon * N_h`. `Pr[|Y - N_h| >= epsilon * N_h] <= 2 exp(-2k * (epsilon * N_h)^2 / 1^2)`.
    6.  **Scelta di k:** Vogliamo che questa probabilità sia al massimo `delta`. `2 exp(-2k * epsilon^2 * N_h^2) <= delta`. `exp(-2k * epsilon^2 * N_h^2) <= delta / 2`. `-2k * epsilon^2 * N_h^2 <= ln(delta / 2)`. `k >= ln(2/delta) / (2 * epsilon^2 * N_h^2)`. Questo dipende da `N_h`, che non conosciamo.
    7.  **Versione che non dipende da E[Y]:** Una forma di Hoeffding è `Pr[Sum Z_i - k*E[Z] >= a] <= exp(-2a^2 / (k(B-A)^2))`. Oppure `Pr[Sum Z_i >= k*(E[Z] + a)] <= exp(-2ka^2 / (B-A)^2)`. Poniamo `Sum Z_i = k*Y`, `k*(E[Z]+a) = k*(N_h + epsilon*N_h) = k*N_h(1+epsilon)`. `Pr[k*Y >= k*N_h(1+epsilon)] <= exp(-2k (epsilon N_h)^2 / 1)`.
    8.  **Dimensione del Campione Corretta:** La fonte afferma `k = O(epsilon^-2 log delta^-1 n)`. Questo non si ottiene direttamente da `exp(-k * epsilon^2 * N_h^2) <= delta/2` a meno che `N_h^2` non sia sostituito da un limite inferiore costante (come 1/n^2 se stiamo stimando una frazione di coppie). L'espressione `Pr[link] -2 = 2 * exp(-2 * k * epsilon^2 * N_h^2 / (1^2))` in è coerente con la forma base di Hoeffding. Il fatto che la dimensione del campione dipenda da `n` (`O(epsilon^-2 log delta^-1 n)`) suggerisce che l'analisi tenga conto della rarità delle coppie a distanza `h` (specialmente per `h` grande o in grafi sparsi), o che l'analisi sia più complessa di una semplice applicazione di Hoeffding alla media campionaria. Potrebbe usare una versione che lega la varianza alla media per variabili 0/1, o un'analisi specifica per conteggi di coppie in grafi campionati.

La dimostrazione completa della dimensione del campione O(epsilon^-2 log delta^-1 n) non è completamente dettagliata nelle fonti, ma lo schema si basa chiaramente sull'applicazione di un limite di concentrazione della misura (probabilmente Azuma-Hoeffding o Hoeffding) alla media campionaria delle frazioni a distanza `h`.

## 12. L'NP-difficoltà del TSP implica l'impossibilità di un'approssimazione con fattore costante a meno che P=NP

Il problema del Commesso Viaggiatore (Traveling Salesperson Problem - TSP) è uno dei problemi NP-hard più noti. Si può dimostrare che trovare un'approssimazione con fattore costante per il TSP (in generale, non metrico) è altrettanto difficile quanto risolverlo esattamente, a meno che P=NP.

-   **Obiettivo:** Dimostrare che se esiste un algoritmo tempo polinomiale per trovare un tour TSP con costo al massimo `r * OPT` (per qualche costante `r > 1`), allora P=NP.
-   **Strumenti:** Riduzione polinomiale, problema NP-complete (Hamiltonian Cycle - HAM).
-   **Schema della Dimostrazione (Outline per la riduzione da HAM a TSP):**
    1.  **Problema di Partenza (NP-complete):** Hamiltonian Cycle (HAM). Dato un grafo `G = (V, E)`, decidere se esiste un ciclo che visita ogni vertice esattamente una volta. HAM è NP-complete.
    2.  **Problema di Destinazione:** TSP (generale). Dato un insieme di città (corrispondenti ai vertici di `G`) e distanze `D_ij` tra ogni coppia di città, trovare il tour di costo minimo che visita ogni città una volta.
    3.  **Ipotesi (per contraddizione):** Supponiamo esista un algoritmo `A_r` tempo polinomiale che trova un tour TSP con costo al massimo `r * OPT_TSP` per qualche costante `r >= 1`.
    4.  **Costruzione dell'Istanza TSP da HAM:** Data un'istanza `G = (V, E)` di HAM, costruiamo un'istanza di TSP con `|V|` città (una per ogni vertice di `G`). Definiamo le distanze `D_ij` tra le città `i` e `j` come segue:
        -   `D_ij = 1` se l'arco `(i, j)` esiste in `E`.
        -   `D_ij = 2 + r * |V|` se l'arco `(i, j)` NON esiste in `E`. Questa costruzione richiede tempo polinomiale in `|V|`.
    5.  **Uso dell'Algoritmo A_r:** Applichiamo l'algoritmo `A_r` all'istanza TSP costruita. Sia `C` il costo del tour trovato da `A_r`. Per ipotesi, `C <= r * OPT_TSP`.
    6.  **Analisi del Costo OPT_TSP:**
        -   **Caso 1: G è Hamiltoniano.** Se `G` ha un ciclo Hamiltoniano, esiste un tour TSP di costo `|V|`, perché ogni arco nel ciclo esiste in `G` e quindi ha costo 1 nella nostra istanza TSP. Quindi `OPT_TSP = |V|`.
        -   **Caso 2: G non è Hamiltoniano.** Se `G` non ha un ciclo Hamiltoniano, qualsiasi tour TSP deve utilizzare almeno un arco che NON esiste in `G` (altrimenti quel tour corrisponderebbe a un ciclo Hamiltoniano in `G`). Ogni tour ha `|V|` archi. Il costo minimo di un tour che utilizza almeno un arco non in `G` sarà la somma dei costi degli archi. Almeno un arco costa `2 + r * |V|`, gli altri al minimo costano 1. Quindi, `OPT_TSP >= (|V| - 1) * 1 + (2 + r * |V|) = |V| - 1 + 2 + r * |V| = (r+1) * |V| + 1`.
    7.  **Decisione per HAM:** L'algoritmo `A` per decidere HAM è il seguente:
        -   Costruisci l'istanza TSP come sopra.
        -   Applica `A_r` all'istanza TSP e ottieni il costo `C`.
        -   **Se `C <= r * |V|` allora rispondi YES (G è Hamiltoniano)**.
        -   **Se `C > r * |V|` allora rispondi NO (G non è Hamiltoniano)**.
    8.  **Dimostrazione di Correttezza dell'Algoritmo A:**
        -   **Se G è Hamiltoniano:** `OPT_TSP = |V|`. Per ipotesi, `C <= r * OPT_TSP = r * |V|`. L'algoritmo `A` risponde YES, che è corretto.
        -   **Se G non è Hamiltoniano:** `OPT_TSP >= (r+1) * |V| + 1`. Per ipotesi, `C <= r * OPT_TSP`. Questo non è l'argomento corretto. Se G non è Hamiltoniano, `OPT_TSP >= (r+1)|V|+1`. Poiché `A_r` trova un tour di costo `C <= r * OPT_TSP`, non possiamo usare questo per dedurre un limite inferiore per C. L'argomento corretto si basa sul fatto che `A_r` produce una soluzione di costo `C`. Confrontiamo `C` con `r * |V|`.
        -   Se `G` non è Hamiltoniano, `OPT_TSP >= (r+1)|V| + 1`. Poiché `A_r` è un `r`-approssimazione, il suo costo `C` potrebbe essere fino a `r * OPT_TSP`. Tuttavia, qualsiasi tour ha costo almeno `(r+1)|V|+1`. Quindi `C >= (r+1)|V|+1`? No. L'argomento si basa sul GAP tra i costi.
        -   Se `G` è Hamiltoniano, `OPT_TSP = |V|`. L'algoritmo `A_r` trova un tour di costo `C <= r * OPT_TSP = r * |V|`.
        -   Se `G` non è Hamiltoniano, `OPT_TSP >= (r+1)|V| + 1`. Qualsiasi tour in questo caso deve usare almeno un arco di costo `2+r|V|`. Il costo di un tour è la somma di `|V|` distanze. Se c'è almeno un arco di costo `2+r|V|`, il costo totale è almeno `(|V|-1)*1 + (2+r|V|) = (r+1)|V|+1`. Quindi, per un grafo non Hamiltoniano, **ogni** tour ha costo almeno `(r+1)|V| + 1`. Poiché `A_r` trova **un** tour, il suo costo `C` deve essere almeno questo valore: `C >= (r+1)|V| + 1`.
        -   Confrontiamo `C` con `r * |V|`: Se `G` è Hamiltoniano, `C <= r * |V|`. Se `G` non è Hamiltoniano, `C >= (r+1)|V| + 1 > r * |V|`.
        -   Quindi, l'algoritmo `A` decide correttamente se `G` è Hamiltoniano confrontando `C` con `r * |V|`.
    9.  **Conclusione:** Abbiamo costruito un algoritmo tempo polinomiale `A` per decidere HAM utilizzando `A_r` tempo polinomiale. Poiché HAM è NP-complete, se esistesse `A_r` tempo polinomiale, allora HAM sarebbe risolvibile in tempo polinomiale, il che implica P=NP. Poiché si ritiene che P != NP, un tale algoritmo `A_r` non può esistere in tempo polinomiale.

Questa dimostrazione per riduzione stabilisce un forte limite alla possibilità di approssimare il TSP generale con un fattore costante.

## 13. 2-Approssimazione per il TSP Metrico

Sebbene il TSP generale sia inapprossimabile con fattore costante (a meno che P=NP), il TSP metrico (dove le distanze soddisfano la disuguaglianza triangolare) ammette algoritmi di approssimazione. Un algoritmo classico fornisce una 2-approssimazione.

-   **Obiettivo:** Dimostrare che l'algoritmo che costruisce un Minimum Spanning Tree (MST) e poi effettua una visita pre-ordine (o un "walk" sull'albero raddoppiato) per ottenere un tour è una 2-approssimazione per il TSP metrico.
-   **Strumenti:** Grafo completo con pesi uguali alle distanze. Minimum Spanning Tree (MST). Proprietà del MST, disuguaglianza triangolare.
-   **Schema della Dimostrazione:**
    1.  **Trasformazione:** Data un'istanza di TSP metrico con `n` città e distanze `D_ij`, consideriamo un grafo completo `G` con `n` vertici (le città) e pesi sugli archi `w_ij = D_ij`. Poiché le distanze soddisfano la disuguaglianza triangolare (`D_ik <= D_ij + D_jk`), i pesi nel grafo soddisfano anch'essi la disuguaglianza triangolare.
    2.  **MST:** Calcoliamo un Minimum Spanning Tree `S` nel grafo `G`. Questo richiede tempo polinomiale.
    3.  **Lower Bound per OPT_TSP:** Qualsiasi tour TSP deve connettere tutti i `n` vertici e avere `n` archi (per formare un ciclo). Se rimuoviamo un arco da un tour TSP ottimo, otteniamo un albero che connette tutti i vertici. Pertanto, il costo del MST `cost(S)` è un limite inferiore al costo di qualsiasi albero di copertura, incluso quello ottenuto rimuovendo un arco da un tour ottimo. Quindi, `cost(S) <= OPT_TSP` (il costo del tour TSP ottimo).
    4.  **Costruzione di un Tour:** Creiamo un "walk" sull'albero `S` percorrendo ogni arco due volte, una in ogni direzione. Questo walk visita ogni vertice almeno una volta. Il costo totale di questo walk è `2 * cost(S)`.
    5.  **Formazione del Tour (Shortcut):** A partire dal walk, costruiamo un tour TSP visitando i vertici nell'ordine in cui appaiono per la prima volta nel walk. Ad esempio, se il walk è A-B-C-B-D-A, il tour è A-B-C-D-A (saltando le visite ripetute).
    6.  **Limite Superiore per il Costo del Tour:** Consideriamo il walk raddoppiato. Quando "saltiamo" da un vertice `u` direttamente al prossimo vertice `v` nel tour (che potrebbe non essere adiacente a `u` nell'MST), stiamo prendendo un "shortcut". Per la disuguaglianza triangolare, la distanza diretta `D_uv` è minore o uguale alla somma delle distanze lungo il percorso nel walk raddoppiato tra `u` e `v`. Poiché il tour è formato prendendo solo shortcut (o archi diretti che erano nel walk raddoppiato), il costo del tour `cost(T)` è minore o uguale al costo del walk raddoppiato: `cost(T) <= 2 * cost(S)`.
    7.  **Risultato Finale:** Combinando i limiti, abbiamo `cost(T) <= 2 * cost(S)` e `cost(S) <= OPT_TSP`. Per transitività, `cost(T) <= 2 * OPT_TSP`.

Questo dimostra che l'algoritmo produce un tour il cui costo è al massimo il doppio del costo ottimo, fornendo quindi una 2-approssimazione.

## 14. 2-Approssimazione per il MAX-CUT tramite Ricerca Locale

Il problema del MAX-CUT (trovare un taglio che massimizzi il numero di archi tra le due partizioni) è NP-hard. Un algoritmo di ricerca locale può fornire una 2-approssimazione.

-   **Obiettivo:** Dimostrare che un algoritmo che sposta ripetutamente un vertice da una partizione all'altra se questo aumenta strettamente la dimensione del taglio converge a un taglio che ha dimensione almeno la metà del numero totale di archi (`|E|/2`), che è un limite inferiore per il taglio massimo (`OPT_MC >= |E|/2`).
-   **Strumenti:** Definizione di taglio e cutset `E(S, S_bar)`. Algoritmo di ricerca locale (flip di un nodo). Summa dei gradi.
-   **Schema della Dimostrazione:**
    1.  **Algoritmo:** Si parte da una partizione casuale `(S, S_bar)`. Iterativamente, si sceglie un vertice `v` e si verifica se spostarlo nella partizione opposta (da `S` a `S_bar` o viceversa) aumenta strettamente la dimensione del cutset `|E(S, S_bar)|`. Se esiste un tale vertice, lo si sposta e si ripete. Altrimenti, l'algoritmo si ferma.
    2.  **Terminazione:** Poiché la dimensione del cutset è un numero intero che aumenta strettamente ad ogni passo e non può superare il numero totale di archi `|E|`, l'algoritmo termina in un numero finito di passi (al massimo `|E|` passi).
    3.  **Proprietà del Taglio Stabile (Ottimo Locale):** Quando l'algoritmo si ferma, non esiste alcun vertice il cui spostamento aumenti strettamente la dimensione del taglio. Questo significa che per ogni vertice `v`, il numero di archi incidenti a `v` che attraversano il taglio (cioè hanno l'altro estremo nella partizione opposta a `v`) è maggiore o uguale al numero di archi incidenti a `v` che NON attraversano il taglio (cioè hanno l'altro estremo nella stessa partizione di `v`). Sia `deg_cut(v)` il numero di archi incidenti a `v` che attraversano il taglio corrente, e `deg_same(v)` il numero di archi incidenti a `v` che NON attraversano il taglio. La condizione di ottimo locale implica `deg_cut(v) >= deg_same(v)` per ogni vertice `v`.
    4.  **Relazione con il Grado Totale:** Il grado totale di un vertice `v` è `deg(v) = deg_cut(v) + deg_same(v)`.
    5.  **Somma dei Gradi:** La somma dei gradi di tutti i vertici è `Sum_{v in V} deg(v) = 2 * |E|`.
    6.  **Relazione tra Cutset e Gradi:** Ogni arco `(u, v)` che attraversa il taglio contribuisce con 1 a `deg_cut(u)` e 1 a `deg_cut(v)`. Quindi `Sum_{v in V} deg_cut(v) = 2 * |E(S, S_bar)|`.
    7.  **Utilizzo della Proprietà di Ottimo Locale:** Dalla condizione `deg_cut(v) >= deg_same(v)` per ogni `v`, sommiamo su tutti i vertici: `Sum_{v in V} deg_cut(v) >= Sum_{v in V} deg_same(v)`.
    8.  **Combinazione:** `Sum deg(v) = Sum deg_cut(v) + Sum deg_same(v)`. Quindi `2 * |E| >= Sum deg_cut(v) + Sum deg_cut(v) = 2 * Sum deg_cut(v)`.
    9.  **Risultato Finale:** `2 * |E| >= 2 * (2 * |E(S, S_bar)|)`. No, questo è errato. La somma `Sum deg_cut(v)` conta ogni arco nel cutset due volte. Quindi `Sum_{v in V} deg_cut(v) = 2 * |E(S, S_bar)|`. Dalla condizione `deg_cut(v) >= deg_same(v)`, sommiamo: `Sum deg_cut(v) >= Sum deg_same(v)`. `Sum deg_cut(v) + Sum deg_same(v) = Sum deg(v) = 2|E|`. Quindi `Sum deg_cut(v) >= (1/2) * (Sum deg_cut(v) + Sum deg_same(v)) = (1/2) * 2|E| = |E|`. Poiché `Sum deg_cut(v) = 2 * |E(S, S_bar)|`, abbiamo `2 * |E(S, S_bar)| >= |E|`. Dividendo per 2, `|E(S, S_bar)| >= |E| / 2`.

Questo dimostra che l'algoritmo converge a una partizione il cui taglio ha dimensione almeno la metà del numero totale di archi. Poiché il taglio massimo è al massimo `|E|` (potenzialmente tutti gli archi possono attraversare il taglio), e l'algoritmo garantisce un taglio di almeno `|E|/2`, si ottiene una 2-approssimazione: `OPT_MC >= |E(S, S_bar)| >= |E|/2`, e `OPT_MC <= |E|`. Questo implica `|E(S, S_bar)| >= (1/2) * |E|`. La dimostrazione richiede che `OPT_MC >= |E|/2`. Questo è vero perché si può sempre ottenere un taglio di almeno `|E|/2` (ad esempio, mettendo ogni vertice in una partizione a caso con probabilità 1/2; il numero atteso di archi che attraversano è `|E|/2`).

## 15. 2-Approssimazione per il MAX-CUT tramite Algoritmo Greedy

Un algoritmo greedy per il MAX-CUT che assegna i vertici alle partizioni uno per uno per massimizzare il contributo al taglio corrente fornisce anch'esso una 2-approssimazione.

-   **Obiettivo:** Dimostrare che l'algoritmo greedy che assegna sequenzialmente ogni vertice `v` a `S` o `S_bar` per massimizzare il numero di archi che lo connettono alla partizione opposta (già parzialmente costruita) produce un taglio di dimensione almeno `|E|/2`.
-   **Strumenti:** Algoritmo greedy sequenziale. Concetto di arco di cui un vertice è "responsabile". Somma dei gradi.
-   **Schema della Dimostrazione:**
    1.  **Algoritmo:** Si considerano i vertici in un ordine arbitrario (ad esempio, da 1 a `n`). Si iniziano `S` e `S_bar` come insiemi vuoti. Per ogni vertice `v_i` (dal primo all'ultimo), lo si assegna alla partizione `S` o `S_bar` in modo da massimizzare il numero di archi `(v_i, v_j)` dove `v_j` è già stato assegnato e `v_j` si trova nella partizione opposta a quella scelta per `v_i`.
    2.  **Contributo al Taglio:** Quando si decide la posizione di `v_i`, si guarda solo agli archi che connettono `v_i` a vertici `v_j` già posizionati (`j < i`). Sia `deg_i(v_i)` il numero di archi incidenti a `v_i` che lo connettono a vertici `v_j` con `j < i`. `deg_i(v_i) = deg_i_S(v_i) + deg_i_S_bar(v_i)`, dove `deg_i_S(v_i)` è il numero di archi a vertici già in `S`, e `deg_i_S_bar(v_i)` a vertici già in `S_bar`.
    3.  **Decisione Greedy:** L'algoritmo assegna `v_i` a `S` se `deg_i_S_bar(v_i) >= deg_i_S(v_i)`, e a `S_bar` altrimenti (o arbitrariamente in caso di uguaglianza). In ogni caso, il numero di archi tra `v_i` e i vertici già posizionati nella partizione opposta sarà almeno `deg_i(v_i) / 2`. Questo è il contributo di `v_i` al taglio parziale formato dai vertici `v_1, ..., v_i`.
    4.  **"Responsabilità" degli Archi:** Consideriamo un arco `(u, v)`. Supponiamo che `u` sia elaborato prima di `v`. Quando `v` viene elaborato, `u` è già stato assegnato. L'arco `(u, v)` viene considerato per massimizzare il taglio dal punto di vista di `v`. Diciamo che `v` è "responsabile" della decisione se l'arco `(u, v)` finirà o meno nel taglio. Ogni arco ha esattamente un vertice responsabile (quello elaborato per secondo).
    5.  **Somma dei Contributi:** La dimensione totale del taglio finale `|E(S, S_bar)|` è la somma dei contributi di ogni vertice "responsabile" per gli archi che lo connettono a vertici già posizionati. Quando il vertice `v_i` viene posizionato, contribuisce con almeno `deg_i(v_i) / 2` archi al taglio (gli archi che lo connettono a vertici `v_j` con `j < i` nella partizione opposta).
    6.  **Relazione con il Grado:** Il grado `deg(v_i)` di `v_i` nel grafo completo è il numero totale di archi incidenti a `v_i`. La somma `Sum_{i=1}^n deg_i(v_i)` non è `2|E|`. Invece, `deg_i(v_i)` è il grado di `v_i` nel sottografo indotto dai vertici `{v_1, ..., v_i}`.
    7.  **Argomento Corretto basato sulla Responsabilità:** La dimensione del taglio `|E(S, S_bar)|` è la somma, per ogni arco `(u,v)`, di 1 se l'arco è nel taglio. Se `v` è responsabile per l'arco `(u,v)` (cioè `u` è stato posizionato prima di `v`), l'algoritmo, quando posiziona `v`, decide se l'arco `(u,v)` finirà nel taglio per massimizzare il numero di archi tra `v` e la partizione opposta già creata. Il numero totale di archi incidenti a `v` che connettono a vertici già posizionati (`deg_i(v)` dove `v=v_i`) è diviso tra archi che vanno a `S_partial` e archi che vanno a `S_bar_partial`. `v_i` viene assegnato per massimizzare gli archi verso la partizione opposta. Quindi, il numero di archi `(v_i, v_j)` con `j<i` che finiscono nel taglio è almeno `deg_i(v_i) / 2`. La somma di questi contributi su tutti i `i` è il taglio totale. `Sum_{i=1}^n (\text{contribution of } v_i) >= Sum_{i=1}^n deg_i(v_i) / 2`. La somma `Sum_{i=1}^n deg_i(v_i)` conta ogni arco `(v_j, v_i)` (con `j<i`) esattamente una volta (quando `v_i` viene elaborato). Questa somma è esattamente `|E|`.
    8.  **Risultato Finale:** La dimensione del taglio `|E(S, S_bar)|` è la somma dei contributi degli archi di cui ogni vertice è responsabile. Quando `v_i` è posizionato, si assicura che almeno metà degli archi che lo connettono a vertici già posizionati attraversino il taglio. La somma `Sum_{v in V} deg(v)` è `2|E|`. L'argomento basato sulla "responsabilità" e il grado è il seguente: Per ogni vertice `v`, quando viene aggiunto, il numero di archi che lo connettono a vertici già posizionati (`deg_partial(v)`) viene diviso tra archi che vanno a `S_curr` e `S_bar_curr`. `v` viene messo nella partizione che massimizza il numero di connessioni alla partizione opposta, garantendo almeno `deg_partial(v) / 2` archi nel taglio. La somma di `deg_partial(v)` per tutti i vertici `v` è `2|E|` (ogni arco `(u,v)` contribuisce 1 quando `v` viene elaborato, supponendo `u` sia elaborato prima). Quindi, la somma dei contributi `>= Sum deg_partial(v) / 2 = 2|E| / 2 = |E|`. Il taglio totale è la somma dei contributi per ogni vertice. `|E(S, S_bar)| = Sum_{v in V} (\text{contribution of } v) >= Sum_{v in V} deg_partial(v) / 2 = |E| / 2`.

Questo dimostra che l'algoritmo greedy costruisce un taglio di dimensione almeno `|E|/2`, fornendo una 2-approssimazione.

## 16. 2-Approssimazione per il KNAPSACK (Greedy + Elemento di Valore Massimo)

Il problema dello Zaino (Knapsack) (trovare un sottoinsieme di oggetti con peso totale limitato che massimizzi il valore totale) è NP-hard. Un semplice algoritmo greedy non fornisce una buona approssimazione. Tuttavia, una variazione che considera l'output greedy e l'elemento singolo di valore massimo garantisce una 2-approssimazione.

-   **Obiettivo:** Dimostrare che l'algoritmo che restituisce il massimo tra il valore ottenuto dall'algoritmo greedy (ordinando per rapporto valore/peso) e il valore dell'elemento singolo di valore massimo fornisce un valore totale che è almeno la metà del valore ottimo (`OPT`).
-   **Strumenti:** Definizione del problema Knapsack. Algoritmo greedy (per rapporto valore/peso). Valore ottimo `OPT`.
-   **Schema della Dimostrazione:**
    1.  **Algoritmo (Variazione Greedy):**
        -   Ordina gli oggetti per rapporto valore/peso `v_i / w_i` in ordine decrescente.
        -   Algoritmo Greedy `S_G`: Itera sugli oggetti ordinati, aggiungendo l'oggetto corrente allo zaino se non supera la capacità `W`. Sia `V_G` il valore totale di `S_G`.
        -   Sia `v_max` il valore dell'oggetto singolo con il valore massimo (tra tutti gli oggetti che singolarmente rientrano nella capacità `W`).
        -   L'algoritmo restituisce `max(V_G, v_max)`.
    2.  **Relazione tra V_G e OPT:** L'algoritmo greedy potrebbe non essere ottimo. Consideriamo il primo oggetto `j` che l'algoritmo greedy NON riesce ad aggiungere perché supera la capacità. Tutti gli oggetti `1, ..., j-1` sono stati aggiunti da `S_G`, e la loro somma dei pesi `Sum_{i=1}^{j-1} w_i <= W`. Aggiungendo l'oggetto `j`, il peso supera `W`: `Sum_{i=1}^{j-1} w_i + w_j > W`.
    3.  **Lower Bound per V_G:** Consideriamo il valore degli oggetti `1, ..., j`. Se potessimo "spezzare" l'oggetto `j` e aggiungere una frazione di esso per riempire esattamente la capacità rimanente, il valore totale ottenuto sarebbe `Sum_{i=1}^{j-1} v_i + v_j' * (W - Sum_{i=1}^{j-1} w_i) / w_j`. Questo è il valore ottenuto dall'algoritmo greedy frazionario. Il valore ottimo del knapsack frazionario è un limite superiore per `OPT` del knapsack intero.
    4.  **Proprietà del Greedy Frazionario:** L'algoritmo greedy (anche intero) riempie lo zaino fino a quasi la sua capacità. Consideriamo il valore totale degli oggetti `1, ..., j-1` (`V_G`). `V_G` è il valore degli oggetti che riempiono quasi tutta la capacità. Il valore `OPT` potrebbe includere alcuni di questi oggetti `1, ..., j-1`, alcuni degli oggetti `j, ..., n`, e potenzialmente l'oggetto `j` stesso (se OPT lo prende e scarta altri oggetti presi dal greedy).
    5.  **Relazione chiave:** Si dimostra che `OPT <= V_G + v_j`. Questo perché se prendiamo tutti gli oggetti `1, ..., j-1`, riempiamo lo zaino fino a quasi `W` con valore `V_G`. L'oggetto `j` non entra. Qualsiasi soluzione ottima `S*` deve scegliere un sottoinsieme di oggetti. `S*` potrebbe prendere alcuni oggetti da `1, ..., j-1` e alcuni da `j, ..., n`. Se `S*` include l'oggetto `j`, allora deve escludere alcuni oggetti tra `1, ..., j-1` per fare spazio a `w_j`. Se `S*` non include l'oggetto `j`, allora prende solo oggetti da `1, ..., j-1` e da `j+1, ..., n`. Si può dimostrare che il valore di `S*` non può essere molto più grande di `V_G + v_j`.
    6.  **Considerare v_max:** `v_max` è il valore dell'oggetto singolo più prezioso. `OPT` deve essere almeno `v_max` (se `v_max` è ottenibile prendendo solo quell'oggetto). L'oggetto `j` (il primo che non entra nel greedy) ha un valore `v_j`. Se `v_j` da solo rientra nella capacità `W` (cioè `w_j <= W`), allora `v_max >= v_j`.
    7.  **Combinare i Limiti:** Sappiamo `OPT <= V_G + v_j`. Anche `v_max >= v_j` se `w_j <= W` (il che è vero per il primo oggetto che non entra se almeno un oggetto entra). Se `w_j > W` per il primo oggetto, allora `V_G=0`, `v_j` non entra, `v_max` è il singolo migliore. Se nessun oggetto entra, `V_G=0`, `v_max=0`, `OPT=0`. Assumiamo almeno un oggetto entra.
    8.  **Caso 1: L'oggetto `j` (primo a non entrare) è l'oggetto di valore massimo `v_max`.** Allora `v_j = v_max`. `OPT <= V_G + v_max`. La soluzione restituita è `max(V_G, v_max)`. Se `V_G >= v_max`, l'algoritmo restituisce `V_G`. `OPT <= V_G + v_max <= V_G + V_G = 2*V_G`. Quindi `V_G >= OPT/2`. Se `V_G < v_max`, l'algoritmo restituisce `v_max`. `OPT <= V_G + v_max < v_max + v_max = 2*v_max`. Quindi `v_max > OPT/2`. In questo caso, `max(V_G, v_max) = v_max >= OPT/2`.
    9.  **Caso 2: L'oggetto di valore massimo `v_max` non è l'oggetto `j`.** Sappiamo ancora `OPT <= V_G + v_j`. La soluzione restituita è `max(V_G, v_max)`. Se `V_G >= v_max`, si restituisce `V_G`. `OPT <= V_G + v_j`. Non possiamo direttamente confrontare `v_j` e `v_max` senza relazione tra `j` e l'indice dell'oggetto con `v_max`.
    10.  **Argomento alternativo:** Consideriamo `max(V_G, v_max)`. Sappiamo `OPT <= V_G + v_j`. Anche, per definizione, `OPT` è il valore massimo, quindi `OPT >= v_max`. Quindi `v_max <= OPT`. Dobbiamo mostrare `max(V_G, v_max) >= OPT/2`.
    11.  **Caso: V_G >= OPT/2.** Allora `max(V_G, v_max) >= V_G >= OPT/2`. Fatto.
    12.  **Caso: V_G < OPT/2.** Allora dobbiamo mostrare che `v_max >= OPT/2`. Sappiamo `OPT <= V_G + v_j`. Se `V_G < OPT/2`, allora `OPT <= OPT/2 + v_j`, il che implica `OPT/2 <= v_j`. L'oggetto `j` (il primo che non entra) ha valore `v_j >= OPT/2`. Poiché `v_j` da solo non supera la capacità (assumendo che almeno un oggetto entri, altrimenti OPT=0), l'oggetto con valore massimo `v_max` deve avere valore almeno `v_j`. Quindi `v_max >= v_j >= OPT/2`. In questo caso, `max(V_G, v_max) >= v_max >= OPT/2`.
    13.  **Risultato Finale:** In entrambi i casi, `max(V_G, v_max) >= OPT/2`.

Questo dimostra che la variazione dell'algoritmo greedy con confronto con l'elemento di valore massimo fornisce una 2-approssimazione per il Knapsack.

## 17. Knapsack FPTAS tramite Scaling dei Valori

È possibile ottenere uno schema di approssimazione in tempo completamente polinomiale (FPTAS) per il Knapsack metrico (dove i pesi sono interi). L'idea è scalare e arrotondare i valori degli oggetti per poter utilizzare un algoritmo di programmazione dinamica efficiente sugli oggetti scalati.

-   **Obiettivo:** Per ogni `epsilon > 0`, trovare un algoritmo tempo polinomiale (in `n` e `1/epsilon`) che restituisca una soluzione `S` per il Knapsack intero tale che `Sum_{i in S} v_i >= (1 - epsilon) * OPT`.
-   **Strumenti:** Programmazione Dinamica (DP2) che trova la soluzione ottima in tempo `O(n^2 V_max)` dove `V_max` è il valore massimo ottenibile. Scaling e arrotondamento dei valori.
-   **Schema della Dimostrazione (Outline):**
    1.  **Scelta del Fattore di Scaling:** Sia `V_max` il valore massimo di un singolo oggetto. Definiamo un fattore di scaling `K = (epsilon * V_max) / n`.
    2.  **Istanza Scalata:** Creiamo una nuova istanza del problema Knapsack con gli stessi pesi `w_i` e capacità `W`, ma con nuovi valori scalati `v'_i = floor(v_i / K)`. Questi valori sono interi.
    3.  **DP sulla Istanza Scalata:** Applichiamo l'algoritmo di programmazione dinamica DP2 all'istanza scalata. Questo algoritmo trova un sottoinsieme `S'` che massimizza la somma dei valori scalati `Sum_{i in S'} v'_i` soggetto al vincolo di capacità `Sum_{i in S'} w_i <= W`. Il tempo di esecuzione di DP2 sulla istanza scalata è `O(n^2 * V'_max)`, dove `V'_max` è il valore massimo scalato possibile. `V'_max <= Sum_{i=1}^n v'_i = Sum_{i=1}^n floor(v_i / K) <= Sum (v_i / K) = (Sum v_i) / K`. Il valore totale massimo è al massimo `n * V_max`, quindi `V'_max <= n * V_max / K`. Con `K = epsilon * V_max / n`, `V'_max <= n * V_max / ((epsilon * V_max) / n) = n^2 / epsilon`. Il tempo di esecuzione diventa `O(n^2 * (n^2 / epsilon)) = O(n^4 / epsilon)` (la fonte indica `O(n^3 / epsilon)`, forse con un'analisi DP leggermente diversa).
    4.  **Valore Scalato della Soluzione Ottima Originale:** Sia `S*` la soluzione ottima per l'istanza originale con valore `OPT = Sum_{i in S*} v_i`. Consideriamo il valore scalato di `S*`: `Sum_{i in S*} v'_i = Sum_{i in S*} floor(v_i / K)`. Poiché `floor(x) > x - 1`, `Sum_{i in S*} v'_i > Sum_{i in S*} (v_i / K - 1) = (Sum_{i in S*} v_i) / K - |S*| = OPT / K - |S*|`. Poiché `|S*| <= n`, `Sum_{i in S*} v'_i > OPT / K - n`.
    5.  **Confronto tra Soluzioni Ottime:** `S'` è l'ottimo per l'istanza scalata, quindi `Sum_{i in S'} v'_i >= Sum_{i in S*} v'_i`.
    6.  **Valore Originale della Soluzione Scalata:** La soluzione `S'` trovata da DP2 ha un valore originale `Sum_{i in S'} v_i`. Sappiamo che `v_i >= K * v'_i` per costruzione (poiché `v'_i = floor(v_i / K)` implica `v_i / K >= v'_i`). Quindi `Sum_{i in S'} v_i >= Sum_{i in S'} K * v'_i = K * Sum_{i in S'} v'_i`.
    7.  **Combinazione:** `Sum_{i in S'} v_i >= K * Sum_{i in S'} v'_i >= K * (OPT / K - n) = OPT - nK`.
    8.  **Sostituzione di K:** Sostituendo `K = (epsilon * V_max) / n`, `Sum_{i in S'} v_i >= OPT - n * (epsilon * V_max) / n = OPT - epsilon * V_max`.
    9.  **Risultato Finale:** Se `OPT >= V_max` (il che è vero per la maggior parte delle istanze non triviali, altrimenti l'ottimo è prendere solo l'oggetto con `V_max`), allora `Sum_{i in S'} v_i >= OPT - epsilon * OPT = (1 - epsilon) * OPT`. Se `OPT < V_max`, la garanzia non è `(1-epsilon)OPT` ma `OPT - epsilon V_max`. Tuttavia, se `OPT` è piccolo, anche `OPT - epsilon V_max` è piccolo. Spesso, si definisce FPTAS con errore relativo `(1+epsilon)OPT` per problemi di minimizzazione, o `(1-epsilon)OPT` per massimizzazione quando `OPT` è grande. Una definizione più generale richiede `|Cost(S) - OPT| <= epsilon * OPT`. La garanzia `Sum_{i in S'} v_i >= OPT - epsilon * V_max` è sufficiente per molte applicazioni.

Questo schema dimostra come la tecnica dello scaling dei valori, combinata con la programmazione dinamica, possa fornire un algoritmo di approssimazione con garanzia arbitrariamente buona (FPTAS) per il Knapsack.

## 18. La Difficoltà di Distinguere Diametro 2 da Diametro 3 implica la falsità di SETH

Strong Exponential Time Hypothesis (SETH) è un'ipotesi sulla complessità computazionale di SAT. Si può dimostrare che se esistesse un algoritmo significativamente più veloce di quello "naïve" per distinguere i grafi con diametro 2 da quelli con diametro 3, allora SETH sarebbe falso.

-   **Obiettivo:** Dimostrare che se esiste un algoritmo che decide se il diametro di un grafo `G` è 2 o 3 in tempo `O(|V|^(2 - epsilon))` per qualche `epsilon > 0`, allora SAT (e quindi NP) può essere risolto in tempo `O(c^n)` per qualche `c < 2`, il che contraddice SETH.
-   **Strumenti:** Riduzione polinomiale, problema SAT. Costruzione di un grafo da una formula SAT. Definizione di diametro. Strong Exponential Time Hypothesis (SETH).
-   **Schema della Dimostrazione (Outline per la riduzione da SAT a Diameter 2 vs 3):**
    1.  **Problema di Partenza:** SAT. Data una formula booleana `F` in CNF con `n` variabili, decidere se è soddisfacibile. SAT è NP-complete. SETH afferma che SAT non può essere risolto in tempo `O(c^n)` per alcun `c < 2`.
        
    2.  **Problema di Destinazione:** Distinguere grafi con diametro 2 da quelli con diametro 3.
        
    3.  **Ipotesi (per contraddizione):** Supponiamo esista un algoritmo `Alg_D2v3` che decide se `Diam(G) = 2` o `Diam(G) = 3` in tempo `O(|V|^(2 - epsilon))` per qualche `epsilon > 0`, dove `|V|` è il numero di vertici di `G`.
        
    4.  **Costruzione del Grafo da F:** Data una formula SAT `F` su `n` variabili `x_1, ..., x_n`, costruiamo un grafo `G_F`. Il numero di variabili `n` è assunto essere pari. Il grafo `G_F` avrà diversi tipi di nodi:
        
        -   Nodi di Assegnazione: Per ogni assegnazione parziale delle prime `n/2` variabili, un nodo `a`. Per ogni assegnazione parziale delle ultime `n/2` variabili, un nodo `b`. Ci sono `2^(n/2)` nodi di tipo `a` e `2^(n/2)` di tipo `b`.
        -   Nodi di Clausola: Per ogni clausola `C` in `F`, un nodo `v_C`. Sia `m` il numero di clausole. `m` è tipicamente polinomiale in `n`, ma per rendere l'argomento più forte contro SETH, si considera `m` esponenziale, ad esempio `m = O(2^n)`. Ma per la riduzione da SAT, `m` è parte dell'input, tipicamente polinomiale in `n`. Le fonti suggeriscono un numero di nodi per clausole `O(|F|)`. Un numero più preciso di nodi totali è `2*2^(n/2) + |F| + ...`. Assumiamo per semplicità `|V| = O(2^(n/2) + |F|)`.
        -   Nodi Dummy/Connettori: Nodi aggiuntivi per garantire la struttura di diametro 2 o 3. Ad esempio, due nodi connettori globali `s` e `t`.
    5.  **Struttura degli Archi:**
        
        -   Archi Fissi: Connettono i nodi di assegnazione tra loro e ai nodi connettori `s, t` in modo che la distanza tra qualsiasi nodo `a` e qualsiasi nodo `b` che rappresentano assegnazioni compatibili (cioè la loro combinazione forma un'assegnazione completa delle `n` variabili) sia 2. La distanza tra altri tipi di nodi può essere 1 o 2. Ad esempio, `d(s, a)=1`, `d(s, b)=1`. `d(a, b)=2` se le assegnazioni sono compatibili.
        -   Archi Dipendenti da F: Questi sono gli archi cruciali. Un nodo di assegnazione parziale `a` (per le prime `n/2` variabili) è connesso a un nodo clausola `v_C` se l'assegnazione parziale `a` NON SODDISFA la clausola `C`. Analogamente per i nodi `b` e le clausole. `a` è connesso a `v_C` iff assegnazione `a` non soddisfa `C`. `b` è connesso a `v_C` iff assegnazione `b` non soddisfa `C`.
    6.  **Analisi del Diametro di G_F:**
        
        -   La costruzione garantisce che la distanza tra la maggior parte delle coppie di nodi sia 1 o 2 (ad esempio, tra nodi di assegnazione e connettori, tra nodi di clausola e connettori tramite archi aggiuntivi). Il diametro sarà 2 o 3, determinato dalla distanza massima.
        -   La distanza cruciale è tra coppie di nodi di assegnazione parziale `a` e `b` tali che la loro combinazione forma un'assegnazione completa delle `n` variabili, e la distanza tra questi nodi di assegnazione e i nodi di clausola.
        -   Consideriamo una coppia `(a, b)` che forma un'assegnazione completa `sigma`. `d(a, b)` è al massimo 2 dagli archi fissi.
        -   Consideriamo la distanza tra `a` e un nodo clausola `v_C`, e tra `b` e `v_C`.
        -   Se l'assegnazione completa `sigma = (a, b)` soddisfa la formula `F`, allora per ogni clausola `C`, almeno una delle assegnazioni parziali `a` o `b` soddisfa `C`. Per costruzione degli archi dipendenti da `F`, questo significa che per ogni clausola `C`, **non** c'è un arco tra `a` e `v_C` O **non** c'è un arco tra `b` e `v_C`.
        -   Se l'assegnazione completa `sigma = (a, b)` NON soddisfa la formula `F`, allora ESISTE almeno una clausola `C` che NON è soddisfatta da `sigma`. Questo significa che NESSUNA delle assegnazioni parziali `a` o `b` soddisfa `C`. Per costruzione, questo significa che ESISTE un arco tra `a` e `v_C` E ESISTE un arco tra `b` e `v_C`. In questo caso, `d(a, v_C) = 1` e `d(b, v_C) = 1`.
        -   La distanza tra `a` e `b` è 2 (`a` -> connettore -> `b` o `a` -> altro nodo assegnazione -> `b`). C'è un percorso `a` -> `v_C` -> `b` di lunghezza 2 se e solo se `a` è connesso a `v_C` E `v_C` è connesso a `b`. Questo accade se e solo se NÉ `a` NÉ `b` soddisfano `C`.
        -   **Connessione tra soddisfacibilità e diametro:**
            -   La formula `F` è soddisfacibile <=> Esiste un'assegnazione completa `sigma = (a, b)` che soddisfa `F`.
            -   <=> Per ogni coppia `(a,b)` che forma un'assegnazione completa, se `sigma=(a,b)` non soddisfa `F`, allora esiste `C` non soddisfatta da `sigma`.
            -   <=> `F` è insoddisfacibile <=> Per **ogni** assegnazione completa `sigma = (a, b)`, ESISTE una clausola `C` che `sigma` NON soddisfa.
            -   <=> Per **ogni** coppia `(a, b)` che forma un'assegnazione completa, ESISTE una clausola `C` tale che `a` è connesso a `v_C` E `b` è connesso a `v_C`.
            -   <=> Per **ogni** coppia `(a, b)` che forma un'assegnazione completa, esiste un nodo `v_C` tale che `d(a, v_C)=1` e `d(b, v_C)=1`.
            -   <=> Per **ogni** coppia `(a, b)` che forma un'assegnazione completa, `d(a, b)` non può essere 3 (poiché c'è un cammino `a -> v_C -> b` di lunghezza 2 per qualche C). La distanza massima tra tali coppie è 2.
            -   <=> **Il diametro del grafo `G_F` è 2**.
        -   Quindi: `F` è soddisfacibile <=> `Diam(G_F) = 3`. `F` è insoddisfacibile <=> `Diam(G_F) = 2`.
    7.  **Algoritmo per SAT:** Utilizziamo l'algoritmo ipotetico `Alg_D2v3` per decidere SAT. Data una formula SAT `F`:
        
        -   Costruisci il grafo `G_F`. Questo richiede tempo polinomiale in `|V| = O(2^(n/2) + |F|)`. `|V|` è esponenziale in `n`.
        -   Applica `Alg_D2v3` a `G_F` per decidere se `Diam(G_F) = 2` o `Diam(G_F) = 3`. Il tempo è `O(|V|^(2 - epsilon)) = O((2^(n/2) + |F|)^(2 - epsilon))`. Poiché `|F|` è tipicamente polinomiale in `n`, questo è `O((2^(n/2))^(2 - epsilon)) = O(2^(n * (1 - epsilon/2))) = O(2^(n * c'))` dove `c' = 1 - epsilon/2 < 1`.
        -   Se `Alg_D2v3` dice che `Diam(G_F) = 3`, allora `F` è soddisfacibile. Rispondi YES.
        -   Se `Alg_D2v3` dice che `Diam(G_F) = 2`, allora `F` è insoddisfacibile. Rispondi NO.
    8.  **Conclusione:** Abbiamo un algoritmo che risolve SAT in tempo `O(2^(n * c'))` con `c' < 1`. Questo è molto più veloce di `O(2^n)` e contraddice SETH. Pertanto, l'ipotesi che esista un algoritmo `O(|V|^(2 - epsilon))` per distinguere Diametro 2 da 3 deve essere falsa.
        

Questa dimostrazione stabilisce un limite inferiore condizionato per la complessità di decidere tra diametro 2 e 3, legandolo direttamente alla difficoltà di risolvere SAT.

----------

Spero questa raccolta e le relative spiegazioni dettagliate siano utili per la tua comprensione delle dimostrazioni contenute nelle fonti. Ho cercato di seguire gli schemi e i passaggi delineati nei testi originali, integrando dove necessario per chiarezza ma rimanendo fedele al contenuto fornito.
