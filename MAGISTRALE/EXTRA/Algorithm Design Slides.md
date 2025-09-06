### Diametro nei Grafi e Complessità Computazionale

#### Definizione del Diametro
Il diametro (D) di un grafo `G = (V, E)` è definito come la massima distanza `d(u,v)` tra tutte le coppie di nodi `u, v` nel grafo [1]. Alternativamente, può essere visto come il massimo dell'eccentricità `e(u)` di tutti i nodi, dove `e(u)` è la massima distanza da `u` a qualsiasi altro nodo `v` nel grafo [1].
La distanza `d(u,v)` può essere calcolata utilizzando l'algoritmo BFS (Breadth-First Search) per grafi non pesati o l'algoritmo di Dijkstra per grafi pesati (senza cicli negativi) [1].

#### Algoritmo Base per il Calcolo del Diametro
L'algoritmo base per calcolare il diametro consiste nell'eseguire BFS o Dijkstra per ciascun nodo del grafo [2].
*   Per grafi non pesati, questo si traduce in un costo di `O(n(n+m))` tempo [1].
*   Per grafi pesati, è `O(n(n log n + m))` o `O(n^3)` per grafi densi [1].
*   Per grafi sparsi (`m = O(n)`), il tempo diventa `O(n^2)` [2].
Tuttavia, per le reti del mondo reale, che sono spesso molto grandi, questo algoritmo di base `O(n^2)` non è computazionalmente fattibile [2].

#### Difficoltà Computazionale del Diametro
Un'importante congettura nella complessità fine-grained afferma che non esiste un algoritmo con un tempo `O(n^(3-ε))` (per qualsiasi `ε > 0`) per determinare se il diametro di un grafo non pesato sia 2 o 3, a meno che l'Ipotesi Forte del Tempo Esponenziale (SETH) sia falsa [2, 3]. Questa è una congettura condizionale del lower bound [2].

**Strong Exponential-Time Hypothesis (SETH):**
*   SETH afferma che non esiste un algoritmo che possa risolvere il problema di soddisfacibilità booleana (SAT) in `O(2^((1-ε)n'))` tempo per qualsiasi `ε > 0`, dove `n'` è il numero di variabili booleane [3, 4].
*   SAT è un problema NP-completo che chiede se una data formula booleana può essere resa vera assegnando valori di verità alle sue variabili [5]. L'algoritmo di base per SAT consiste nel testare tutte le `2^n'` possibili assegnazioni, impiegando `O(2^n' * poly(n'))` tempo [4, 5]. SETH suggerisce che questo non può essere migliorato in modo significativo [4].

**Connessione tra D=2 vs D=3 e SETH:**
*   Si può dimostrare che decidere se il diametro di un grafo è 2 o 3 è un problema computazionalmente difficile [3].
*   Viene presentata una riduzione che trasforma un'istanza SAT (`F` con `n'` variabili) in un grafo `G_F` [4].
    *   Questo grafo `G_F` ha `O(2^(n'/2))` nodi totali e ha una struttura che include nodi per le assegnazioni di verità e per le clausole [4, 6].
    *   La proprietà cruciale di questa costruzione è che:
        *   La formula `F` è *non soddisfacibile* se e solo se il diametro di `G_F` è 2 [7, 8].
        *   La formula `F` è *soddisfacibile* se e solo se il diametro di `G_F` è 3 [8].
*   Pertanto, se esistesse un algoritmo per decidere `D=2` vs `D=3` in `O(n^(2-ε))` tempo, questo algoritmo potrebbe risolvere SAT in `O(2^((1-ε)n'))` tempo, il che contraddirebbe SETH [8]. Questo stabilisce la difficoltà intrinseca del problema di distinguere tra diametro 2 e 3 [8].

#### Algoritmi di Approssimazione per il Diametro
Nonostante la difficoltà nel calcolare il diametro esatto, esistono approcci pratici e teorici per approssimarlo:
*   **Euristiche:** Esistono buone euristiche, come il "2-SWEEP", che sono quasi a tempo lineare nelle reti del mondo reale [3]. Tuttavia, queste euristiche non offrono garanzie di accuratezza [3].
*   **Algoritmi Randomizzati di Approssimazione:** Esiste un algoritmo randomizzato che può fornire un'approssimazione `D_approssimato` tale che `(2/3)D <= D_approssimato <= D` con alta probabilità, con un costo temporale di `O(n * m^(1/2))` [3].
*   **PTAS (Polynomial Time Approximation Scheme):** In generale, non è possibile avere un PTAS per il diametro, il che significa che non si può approssimare il diametro con precisione arbitrariamente piccola in tempo polinomiale [3].