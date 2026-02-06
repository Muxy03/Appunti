# Sliding Window Maxima

![[SlidingWindowMaxima.pdf]]

# Alice & Bob

Il problema di Alice e Bob riguarda solitamente un gioco di strategia con un numero pari ($2n$) di monete o numeri disposti in fila. Alice e Bob scelgono a turno una moneta da uno dei due estremi della riga. L'obiettivo di Alice, che inizia per prima, è massimizzare il valore totale delle monete raccolte rispetto a quello di Bob.

Esiste una strategia elegante che permette ad Alice di vincere o pareggiare sempre, indipendentemente dai valori delle monete. La strategia funziona così:

- Alice calcola separatamente la somma delle monete che si trovano nelle posizioni pari e di quelle nelle posizioni dispari.
- Poiché è lei a muovere per prima, Alice può scegliere se prendere la prima moneta (posizione dispari) o l'ultima (posizione pari).
- Così facendo, Alice può forzare il gioco in modo da raccogliere tutte le monete del gruppo (pari o dispari) che ha la somma complessiva maggiore, impedendo a Bob di fare lo stesso.

Ecco un esempio numerico basato sulla sequenza: **10, 1, 3, 5, 1, 7**.

1. **Calcolo delle somme**: Alice somma i valori nelle posizioni dispari (1ª, 3ª, 5ª moneta: 10 + 3 + 1 = **14**) e quelli nelle posizioni pari (2ª, 4ª, 6ª moneta: 1 + 5 + 7 = **13**).
2. **Scelta della strategia**: Poiché 14 è maggiore di 13, Alice decide di raccogliere tutte le monete in posizione dispari.
3. **Primo turno**: Alice prende la prima moneta (10), che si trova in posizione dispari.
4. **Risposta di Bob**: Bob ora può scegliere solo tra la moneta in posizione 2 (valore 1) e quella in posizione 6 (valore 7), che sono entrambe in posizione pari.
5. **Mantenimento della parità**: Qualunque moneta scelga Bob, Alice potrà sempre scegliere una moneta in posizione dispari al turno successivo, forzando Bob a scegliere nuovamente tra le restanti posizioni pari.

In questo modo, Alice ha la certezza di ottenere almeno 14 punti, superando i 13 di Bob.

# Social Distacing

Il problema del distanziamento sociale (**Social Distancing**) è una sfida algoritmica che richiede di posizionare un numero $C$ di persone (o punti) all'interno di un set di $n$ intervalli disgiunti sulla retta reale, in modo che la distanza minima tra due persone consecutive sia massimizzata.

Ecco come viene strutturata la soluzione ottimale:

### 1. La Strategia: Ricerca Binaria sulla Risposta

La chiave per risolvere questo problema non è cercare direttamente il posizionamento, ma utilizzare la **ricerca binaria sulla risposta**.

- Sappiamo che la distanza ottimale $d^*$ deve trovarsi in un intervallo compreso tra 0 e la lunghezza totale della coordinata $L$.
- Il problema presenta una proprietà di **monotonia**: se è possibile posizionare le persone a una distanza minima $d$, allora è certamente possibile farlo per qualsiasi distanza inferiore a $d$. Questo ci permette di usare la ricerca binaria per trovare il valore massimo di $d$ che soddisfa il criterio di fattibilità.

### 2. Il Predicato di Fattibilità (Algoritmo Greedy)

Per verificare se una specifica distanza $d$ è raggiungibile, si utilizza un approccio **greedy** (miope) molto efficiente:

1. Si ordina inizialmente il set di intervalli (se non lo è già).
2. Si posiziona la prima persona all'estremo sinistro del primo intervallo disponibile.
3. Per ogni persona successiva, si cerca il primo punto valido che si trovi a una distanza di almeno $d$ dalla persona precedente.
4. Se il punto calcolato cade in uno spazio vuoto tra due intervalli, la persona viene spostata all'inizio dell'intervallo successivo disponibile.
5. Se alla fine del processo si è riusciti a piazzare tutte le $C$ persone, il predicato restituisce **Vero**, altrimenti **Falso**.

### 3. Complessità Computazionale

L'algoritmo è estremamente efficiente:

- La fase di verifica (scansione degli intervalli) richiede tempo lineare $O(n)$.
- Poiché eseguiamo questa verifica per ogni passo della ricerca binaria, la complessità totale è $O(n \log L)$.

Questa funzione verifica se è possibile posizionare $C$ persone mantenendo una distanza minima $d$.

```
funzione is_feasible(intervalli, C, d):
    conteggio = 1 # Piazza la prima persona all'inizio del primo intervallo
    ultima_pos = intervalli.inizio

    per ogni intervallo in intervalli:
        # Trova la prima posizione valida nell'intervallo corrente
        prossima_pos = max(intervallo.inizio, ultima_pos + d)

        # Piazza quante più persone possibile in questo intervallo
        mentre prossima_pos <= intervallo.fine:
            conteggio = conteggio + 1
            ultima_pos = prossima_pos
            se conteggio >= C:
                ritorna VERO
            prossima_pos = ultima_pos + d

    ritorna FALSO

# L'algoritmo principale cerca il valore massimo di $d$ in un intervallo di ricerca $[0, L]$.

funzione solve_social_distancing(intervalli, C):
    ordina_intervalli(intervalli) # Ordinamento per estremo sinistro

    low = 0
    high = posizione_massima - posizione_minima
    risposta = 0

    mentre low <= high:
        mid = (low + high) / 2
        se is_feasible(intervalli, C, mid):
            risposta = mid # d è possibile, proviamo una distanza maggiore
            low = mid + 1
        altrimenti:
            high = mid - 1 # d è troppo grande, proviamo una minore

    ritorna risposta
```

### Analisi della Complessità

- **Tempo:** $O(n \log L)$, dove $n$ è il numero di intervalli e $L$ è la coordinata massima.
- **Spazio:** $O(1)$ (oltre alla memorizzazione degli intervalli).

# Longest K-good segment

Il problema del **Longest K-good segment** (o _subarray_) richiede di identificare la porzione continua più lunga di un array che contenga al massimo $K$ valori diversi.

### La Strategia: Two Pointers (Finestra Scorrevole)

La soluzione più efficiente sfrutta la tecnica dei **due puntatori** (puntatore sinistro `L` e puntatore destro `R`), che permette di scansionare l'intero array in tempo lineare $O(n)$.

Ecco come funziona il processo:

1. **Espansione**: Sposta il puntatore `R` verso destra, un elemento alla volta, aggiungendo il valore corrente a una mappa di frequenze (o dizionario) per tenere traccia di quanti valori distinti sono presenti nella finestra attuale.
2. **Verifica**: Dopo ogni inserimento, controlla se il numero di chiavi nella mappa (valori distinti) supera $K$.
3. **Contrazione**: Se i valori distinti sono più di $K$, sposta il puntatore `L` verso destra e riduci la frequenza dell'elemento che esce dalla finestra. Se la frequenza di un elemento scende a zero, rimuovilo completamente dalla mappa.
4. **Aggiornamento del Massimo**: Per ogni posizione di `R` in cui la finestra è valida ($K$-good), calcola la lunghezza attuale ($R - L + 1$) e confrontala con il massimo trovato in precedenza per memorizzare il segmento più lungo.

### Esempio Pratico

Immaginiamo l'array $A =$ con $K=3$:

- La finestra si espande inizialmente includendo. I valori distinti sono ${1, 2, 3}$, quindi la condizione è soddisfatta ($3 \le 3$).
- Aggiungendo il valore `4`, i valori distinti diventano 4 (${1, 2, 3, 4}$), violando la regola.
- Il puntatore `L` deve avanzare finché uno dei valori (in questo caso il `2`) non viene rimosso, riportando il conteggio dei valori distinti a 3 (${1, 3, 4}$).

### Analisi della Complessità

- **Tempo**: **$O(n)$**, poiché entrambi i puntatori si muovono solo in avanti, visitando ogni elemento al massimo una volta.
- **Spazio**: **$O(K)$** (o $O(n)$ nel caso peggiore per la mappa), necessario per mantenere il conteggio dei valori distinti.

Ecco lo pseudocodice dettagliato per risolvere il problema del **Longest K-good segment** utilizzando la tecnica dei **due puntatori** (sliding window),.

```
funzione longest_k_good_segment(A, K):
    L = 0
    max_lunghezza = 0
    mappa_frequenze = {} # Memorizza il conteggio di ogni valore nella finestra
    valori_distinti = 0
    risultato_sinistro = 0
    risultato_destro = 0

    per R da 0 a lunghezza(A) - 1:
        # Espansione: Aggiungi l'elemento a destra
        se A[R] non è in mappa_frequenze oppure mappa_frequenze[A[R]] == 0:
            valori_distinti = valori_distinti + 1
        mappa_frequenze[A[R]] = mappa_frequenze.get(A[R], 0) + 1

        # Contrazione: Se ci sono più di K valori diversi, sposta L a destra
        mentre valori_distinti > K:
            mappa_frequenze[A[L]] = mappa_frequenze[A[L]] - 1
            se mappa_frequenze[A[L]] == 0:
                valori_distinti = valori_distinti - 1
            L = L + 1

        # Aggiornamento del massimo segmento trovato
        lunghezza_attuale = R - L + 1
        se lunghezza_attuale > max_lunghezza:
            max_lunghezza = lunghezza_attuale
            risultato_sinistro = L + 1 # Indice 1-based
            risultato_destro = R + 1

    ritorna (risultato_sinistro, risultato_destro)
```

### Analisi del funzionamento

1. **Mantenimento della finestra**: Il puntatore `R` definisce la fine del segmento e il puntatore `L` l'inizio,.
2. **Conteggio Efficiente**: L'uso di una mappa (o di un array di frequenze se i valori sono limitati) permette di sapere in tempo reale quanti valori distinti sono presenti nella finestra attuale,.
3. **Complessità**: Poiché entrambi i puntatori si muovono solo in avanti, l'algoritmo visita ogni elemento al massimo due volte, garantendo un tempo di esecuzione **$O(n)$**.
   
# Closet Pair of Points

Il problema del **Closest Pair of Points** consiste nel trovare la coppia di punti con la minima distanza euclidea all'interno di un insieme di $n$ punti in un piano. Mentre un approccio a forza bruta richiede tempo $O(n^2)$, esistono diverse strategie ottimizzate:

### 1. Divide et Impera ($O(n \log n)$)

Questa strategia divide ricorsivamente l'insieme di punti in due metà (sinistra e destra) tramite una linea verticale $L$.

- **Ricorsione:** Si trova la distanza minima $\delta$ separatamente nelle due metà.
- **Combinazione:** Si controlla se esiste una coppia "a cavallo" della linea $L$ con distanza minore di $\delta$. Per farlo, si analizza una striscia di larghezza $2\delta$ attorno a $L$.
- **Proprietà Geometrica:** Grazie alla struttura dello spazio, all'interno della striscia ogni punto deve essere confrontato solo con un numero costante di altri punti (al massimo 6 o 8) ordinati per coordinata $y$.

### 2. Sweep-line con BST ($O(n \log n)$)

Si processano i punti ordinati per coordinata $x$. Si mantiene un albero binario di ricerca (BST) contenente i punti già visti che si trovano entro una distanza $\delta$ (la minima attuale) dal punto corrente sulla coordinata $x$. Il BST è ordinato per coordinata $y$, permettendo di identificare rapidamente i candidati vicini.

Ecco lo pseudocodice per risolvere il problema del **Closest Pair of Points** in tempo $O(n \log n)$ utilizzando la tecnica della **sweep-line** supportata da un **BST**,.

### Pseudocodice Closest Pair (Sweep-line + BST)

```rust
pub fn distance_squared(p: (i64, i64), q: (i64, i64)) -> i64 {
    (p.0 - q.0).pow(2) + (p.1 - q.1).pow(2)
}

use std::collections::BTreeSet;
use std::ops::Bound::Included;

// Returns the (squared) Euclidean distance between the closest pair of 
// points in `points`
pub fn closest_pair(points: &mut [(i64, i64)]) -> Option<i64> {
    if points.len() < 2 {
        return None;
    }

    points.sort_unstable_by_key(|p| (p.1, p.0)); // sort by y

    let min_y = points[0].1;
    let max_y = points.last()?.1;

    let mut delta = distance_squared(points[0], points[1]);

    let mut set: BTreeSet<(i64, i64)> = BTreeSet::new();
    for &point in points.iter() {
        // Search by x and select the points with too small y-coordinate that we remove
        // to not touch them again in the future
        let to_delete: Vec<_> = set
            .range((
                Included(&(point.0 - delta, min_y)),
                Included(&(point.0 + delta, max_y)),
            ))
            .filter(|p| p.1 < point.1 - delta)
            .cloned()
            .collect();

        // Remove those points
        for p in to_delete {
            set.remove(&p);
        }

        // Search again and compute the distances with survived points.
        // Update delta if needed.
        delta = set
            .range((
                Included(&(point.0 - delta, min_y)),
                Included(&(point.0 + delta, max_y)),
            ))
            .fold(delta, |acc, &p| acc.min(distance_squared(point, p)));

        set.insert(point);
    }

    Some(delta)
}
```

# Frog and Mosquitos

Il problema delle rane e delle zanzare (**Frogs and Mosquitos**) richiede di gestire $n$ rane posizionate sull'asse X, ognuna con una lingua di lunghezza iniziale $t_i$, e $m$ zanzare che atterrano in posizioni $b_j$ con un valore nutritivo $a_j$.

Una rana mangia una zanzara se questa atterra entro la portata della sua lingua, ovvero nell'intervallo $[x_i, x_i + t_i]$. Se più rane possono mangiare la stessa zanzara, la priorità spetta a quella più a sinistra (con coordinata $x_i$ minore). Ogni pasto allunga la lingua della rana di un valore pari ad $a_j$, rendendo possibile la cattura di zanzare precedentemente fuori portata.

### Soluzione Algoritmica Ottimale

Per raggiungere la complessità target di $O((n+m) \log (n+m))$, si utilizzano le seguenti strategie:

1. **BST per le Rane**: Le rane vengono mantenute in un albero binario di ricerca (BST) ordinato per posizione $x_i$. Quando una zanzara atterra in $b_j$, si cerca il **predecessore** di $b_j$ nel BST per identificare l'unica rana potenzialmente in grado di mangiarla.
2. **Rimozione delle Sovrapposizioni**: Per garantire che la ricerca del predecessore sia corretta e veloce, gli intervalli di portata delle rane devono essere mantenuti **disgiunti**. Durante il preprocessing e dopo ogni allungamento, se una rana copre completamente l'intervallo di una rana alla sua destra, quest'ultima viene rimossa dal BST; se lo copre solo parzialmente, l'intervallo della rana a destra viene accorciato.
3. **BST per le Zanzare in Attesa**: Le zanzare che non vengono mangiate immediatamente sono inserite in un secondo BST (ordinate per posizione). Ogni volta che una lingua si allunga, l'algoritmo effettua una query di **successore** in questo BST per vedere se la rana può ora mangiare la zanzara più vicina alla sua destra. Se la mangia, la lingua si allunga ulteriormente e il processo si ripete ricorsivamente.

Questa struttura garantisce che ogni zanzara e ogni rana vengano inserite o rimosse dai BST solo un numero limitato di volte, mantenendo l'efficienza complessiva.

Ecco lo pseudocodice per risolvere il problema **Frogs and Mosquitos** con una complessità di $O((n+m) \log (n+m))$.

L'algoritmo utilizza due alberi binari di ricerca (BST): uno per le rane (ordinate per posizione $x_i$, mantenendo gli intervalli di portata $[x_i, x_i + t_i]$ disgiunti) e uno per le zanzare non ancora mangiate.

### Algoritmo Principale

```
# BST_rane: memorizza le rane disgiunte (x, t)
# BST_zanzare: memorizza zanzare in attesa (posizione, valore)

funzione zanzara_atterra(b_j, a_j):
    # 1. Trova la rana potenzialmente in grado di mangiare
    rana = BST_rane.predecessor(b_j)

    se rana esiste E b_j <= (rana.x + rana.t):
        rana.t += a_j # La rana mangia e la lingua si allunga

        # 2. Controlla se la rana può ora mangiare zanzare in attesa
        mentre vero:
            z_prossima = BST_zanzare.successor_or_equal(rana.x)
            se z_prossima esiste E z_prossima.pos <= (rana.x + rana.t):
                rana.t += z_prossima.valore
                BST_zanzare.rimuovi(z_prossima)
            altrimenti:
                interrompi

        # 3. Gestisci nuove sovrapposizioni tra rane
        pulisci_sovrapposizioni(rana)
    altrimenti:
        # La zanzara non è raggiungibile, viene messa in attesa
        BST_zanzare.inserisci(b_j, a_j)

funzione pulisci_sovrapposizioni(rana_corrente):
    mentre vero:
        successiva = BST_rane.successor(rana_corrente)
        se successiva esiste E successiva.x <= (rana_corrente.x + rana_corrente.t):
            # Se la rana corrente copre la portata della successiva
            se successiva.x + successiva.t <= (rana_corrente.x + rana_corrente.t):
                BST_rane.rimuovi(successiva) # Rimuovi rana ridondante
            altrimenti:
                # La rana corrente copre solo l'inizio; l'intervallo è ora disgiunto
                interrompi
        altrimenti:
            interrompi
```

### Note sulla complessità

- **Predecessore/Successore**: Entrambi i BST operano in tempo $O(\log n)$ o $O(\log m)$ per operazione.
- **Ammortizzazione**: Ogni zanzara e ogni rana vengono inserite o rimosse una sola volta, garantendo il rispetto del limite temporale complessivo.
# 100 prisoners

- prisoner i open drawer i with number $d_i$ 
- if $d_i == i$ he win
- otherwise he open drawer $d_i$ and continue

if we do not stop after 50, the prisoners is guaranteed to find his number

$$P(\text{All win}) = P(\text{random permutation has no cycle longer than 50})$$
only one cycle with length  l > 50 is possible

$$
\binom{100}{l}*(l-1)!*(100-l!) = \frac{100!}{l}
$$

$$
\begin{align}
\text{Total number of permutation with a cycle of length > 50} &= \sum_{l=51}^{100} {\frac{100!}{l}} \\ 
&= 100!*\sum_{l=51}^{100} {\frac{1}{l}} \\
&= 100! *(\frac{1}{51}+\frac{1}{52}+\dots+\frac{1}{100}) \\
&= 100! * (H_{100} - H_{50})
\end{align}
$$

$H_n$ = n-th Harmonic number

$$P(win) = 1 - (H_{100} - H_{50}) \approx 0.3118$$

# Duplicate elements in an Array

Il problema consiste nel trovare un duplicato in un array di $n+1$ elementi dove i valori sono compresi tra $0$ e $n-1$, garantendo la presenza di almeno un valore ripetuto per il principio dei cassetti (Pigeonhole Principle),. Esistono diverse strategie per affrontare questa sfida, variando drasticamente in termini di efficienza temporale e spaziale.

### 1. Soluzioni a Spazio Lineare ($O(n)$)

L'approccio più immediato consiste nell'utilizzare una struttura dati ausiliaria per tenere traccia degli elementi incontrati durante la scansione dell'array,.

- **Hash Set:** Si scansiona l'array da sinistra a destra inserendo ogni elemento in un Hash Set; l'algoritmo si ferma quando si tenta di inserire un valore già presente,. Questo metodo richiede tempo $O(n)$ ma anche spazio $O(n)$.
- **Bit Vector (Direct Access Table):** Poiché l'intervallo dei valori è noto e limitato, si può utilizzare un vettore di bit di dimensione $n$. Si imposta il bit in posizione $k$ a 1 quando si incontra il valore $k$; se il bit è già 1, il valore è un duplicato,. Sebbene più efficiente in pratica rispetto a una mappa, richiede comunque spazio proporzionale a $n$.

### 2. Ricostruzione Bit a Bit ($O(n \log n)$ tempo, $O(1)$ spazio)

Se l'array è di sola lettura e lo spazio è estremamente limitato, è possibile identificare il duplicato bit dopo bit eseguendo $\log n$ passaggi sull'array,.

- **Logica:** Per ogni posizione del bit (da quello meno significativo a quello più significativo), si conta quante volte compare lo 0 e quante volte compare l'1 tra i numeri dell'array,.
- Confrontando questi conteggi con la distribuzione attesa per i numeri da $0$ a $n-1$, è possibile determinare se il bit corrispondente del duplicato sia 0 o 1,. Questo approccio garantisce uno spazio costante $O(1)$ ma richiede più tempo a causa dei molteplici passaggi.
- Best if no  random access

### 3. Destroying A $\Theta(n)$ time and O(1) space

A = \[1,3,5,6,5,2,0,4,7]

- start A\[n] (A\[8] = 7)
- goto A\[7] (= 4), set A\[7] = 7
- goto A\[4] (=5), set A\[4] = 4
- goto A\[5] (= 2), set A\[5] = 5
- goto A\[2] (=5), set A\[2] = 2
- goto A\[5] (= 5) => e = 5 (elemento duplicato)

# Floyd's cycle finding

L'algoritmo di Floyd per la ricerca dei cicli, noto anche come algoritmo della "lepre e della tartaruga", è una tecnica utilizzata per rilevare un ciclo in una sequenza di elementi e trovarne l'inizio utilizzando uno spazio extra costante $O(1)$.

Il funzionamento si divide in due fasi principali:

1. **Fase di Rilevamento (Detection):** Si utilizzano due puntatori che partono dall'inizio della sequenza. Il puntatore "lento" ($S$) avanza di un passo alla volta, mentre il puntatore "veloce" ($F$) avanza di due passi. Se la sequenza ha un ciclo, i due puntatori finiranno inevitabilmente per incontrarsi in un punto all'interno del ciclo stesso.
2. **Fase di Individuazione dell'Inizio:** Una volta rilevato il ciclo, si riporta il puntatore veloce $F$ all'inizio della sequenza e si imposta la sua velocità a uno (un passo alla volta), mantenendo il puntatore $S$ nel punto dell'incontro. Facendoli avanzare entrambi allo stesso ritmo, si incontreranno di nuovo esattamente nel punto in cui inizia il ciclo.

**Perché funziona?** Sia $A$ la distanza dall'inizio della lista all'inizio del ciclo e $B$ la distanza dall'inizio del ciclo al punto del primo incontro. L'algebra dell'algoritmo dimostra che $A$ è equivalente alla distanza rimanente per completare uno o più giri del ciclo partendo da $B$ ($A = kL - B$, dove $L$ è la lunghezza del ciclo). Pertanto, percorrendo $A$ passi sia dall'inizio che dal punto di incontro, entrambi i puntatori convergeranno sull'ingresso del ciclo.

Questa tecnica è estremamente efficiente perché garantisce un tempo di esecuzione lineare $O(n)$ senza dover modificare o "distruggere" i dati originali, rendendola ideale per liste di sola lettura.

S and F met => S moved by m steps, F moved by 2m steps

m = a + b = (steps before the cycle) + (steps inside the cycle)
2m = a + b + k * l (length of the loop) => a = k * l - b -> steps by F = steps by S  (in Phase 2)

# Majority Element

Il problema dell'elemento di maggioranza (**Majority Element**) consiste nel trovare, all'interno di un array di lunghezza $n$, l'elemento che appare più di $\lfloor n/2 \rfloor$ volte. Se tale elemento esiste, è unico.

Ecco le strategie principali per risolverlo:

### 1. Soluzioni Standard

- **Sorting ($O(n \log n)$ tempo, $O(1)$ spazio):** Ordinando l'array, l'elemento di maggioranza deve necessariamente trovarsi nella posizione centrale ($n/2$).
- **HashMap ($O(n)$ tempo, $O(n)$ spazio):** Si scansiona l'array contando le frequenze di ogni elemento in una tabella hash.

### 2. Algoritmo di Boyer-Moore ($O(n)$ tempo, $O(1)$ spazio)

Questa è la soluzione ottimale che non richiede spazio extra. Si basa su un sistema di "voto" dove un elemento può "eliminare" un altro elemento diverso.

- **Fase di Selezione:** Mantieni un candidato `C` e un `counter`. Scansiona l'array: se il `counter` è 0, assegna l'elemento corrente a `C` e imposta il `counter` a 1. Se l'elemento successivo è uguale a `C`, incrementa il `counter`; altrimenti, decrementalo.
- we can use an occurence of the majority element to "kill" another element
### 3. Support Insertion/Deletion

È possibile ricostruire l'elemento bit dopo bit: per ogni posizione binaria, si contano quanti numeri hanno lo 0 e quanti l'1. L'elemento di maggioranza deve avere, in ogni posizione, il bit che appare più frequentemente. Questo metodo è utile se gli inserimenti e le cancellazioni avvengono in modo dinamico.

```
 A 5 3 1 1 2 3 1 1 1     0|1
-> 1 0 0 0 0 0 0 0 0  => 8|1 => 0 
-> 0 1 0 0 1 1 0 0 0  => 6|3 => 0
-> 1 1 1 1 0 1 1 1 1  => 1|8 => 1

e = 001 => e = 1 duplicate element
```
# Misra-Gries Heavy Hitter

Given A\[1,n], find the T-elements that occur at least $\frac{n}{T} + 1$ times

Keep a set K of T candidates with counters

```
for e in A:
	if e in K:
		K[e] += 1
	else:
		K[e] = 1
		if len(K) > T:
			for k in K.keys():
				K[k] -= 1
				if K[k] == 0:
					del(K[k])
```

$O(T*n)$ time, but actually is $\Theta(n)$ because the cost of the "for k in K" loop cannot be more than the number of element of the array.

# Maximum Number of overlapping intervals

Given n intervals $[s_i,e_i]$ we say that two intervals overlaps if

$$
\exists x \text{ such that } x \in [s_i,e_i] \land x \in [s_j,e_j]
$$
```rust
#[derive(PartialOrd, Ord, PartialEq, Eq, Debug)]
enum Event {
    Begin,
    End,
}

pub fn max_overlapping(intervals: &[(usize, usize)]) -> usize {
    let mut pairs: Vec<_> = intervals
        .iter()
        .flat_map(|&(b, e)| [(b, PointKind::Begin), (e, PointKind::End)])
        .collect();

    pairs.sort_unstable();

    pairs
        .into_iter()
        .scan(0, |counter, (_, kind)| {
            if kind == Event::Begin {
                *counter += 1;
            } else {
                *counter -= 1;
            }
            Some(*counter)
        })
        .max()
        .unwrap()
}
```

# Static Prefix Search

Given A\[1,n] of integers, we would like to support:
- Sum(i) = $\sum_{k=1}^i A[k]$
- RangeSum(i,j) = $\sum_{k=i}^j A[k]$

RangeSum(i,j) = Sum(j) - Sum(i-1)

store P such that $P[i] = \sum_{k=1}^i A[k]$ => sum(i) O(1) time and P can computed in $\Theta(n)$ time

A\[i] = RangeSum(i,i+1)

# Ilya and Queries

Il problema **Ilya and Queries** richiede di gestire una stringa binaria (composta da caratteri come 'a' e 'b') e di rispondere a diverse query su intervalli $[i, j]$. L'obiettivo di ogni query è contare quante volte appare una coppia di caratteri consecutivi uguali all'interno di quel range.

### La Strategia Risolutiva

Per risolvere il problema in modo efficiente, si utilizza la tecnica delle **somme prefisse**:

1. **Array Ausiliario**: Si crea un array $B$ di numeri interi dove $B[k] = 1$ se il carattere in posizione $k$ è uguale al carattere in $k+1$ ($S[k] == S[k+1]$), altrimenti $B[k] = 0$.
2. **Trasformazione in Range Sum**: La query originale viene trasformata in una somma di intervallo sull'array $B$. Nello specifico, per un intervallo $[i, j]$, il risultato è la somma degli elementi di $B$ tra l'indice $i$ e $j-1$.
3. **Somme Prefisse**: Calcolando preventivamente le somme prefisse di $B$, ogni query può essere risolta in tempo costante $O(1)$.

### Complessità

- **Tempo**: $O(n + m)$, dove $n$ è la lunghezza della stringa (per il preprocessamento) e $m$ è il numero di query.
- **Spazio**: $O(n)$ per memorizzare l'array delle somme prefisse.

# Little girl and Queries

Il problema richiede di permutare gli elementi di un array $A$ per massimizzare la somma totale di diverse query di intervallo (range sum) $Q$,.

![[Pasted image 20260205173230.png]]
```rust
// We assumes queries are 0-based indexed
pub fn little_girl(a: &[i64], q: &[(usize, usize)]) -> i64 {
    if a.is_empty() {
        return 0;
    }

    let mut u = vec![0i64; a.len()];

    for &(l, r) in q {
        assert!(l <= r);
        assert!(r < u.len());

        u[l] += 1;
        if r + 1 < u.len() {
            u[r + 1] -= 1;
        }
    }

    let mut f = u
        .iter()
        .scan(0, |sum, e| {
            *sum += e;
            Some(*sum)
        })
        .collect::<Vec<_>>();

    // we sort both f and a in decreasing order, nothing changes
    f.sort_unstable();
    let mut a_sorted = a.to_vec();
    a_sorted.sort_unstable();

    a_sorted
        .iter()
        .zip(f)
        .fold(0, |result, (value, freq)| result + value * freq)
}
```

# Number of Ways

![[Pasted image 20260205173511.png]]
### 1. Condizione Necessaria

Affinché esistano tre parti con la stessa somma, la somma totale $S$ di tutti gli elementi dell'array deve essere divisibile per 3 ($S \mod 3 = 0$). Ogni parte dovrà quindi avere una somma pari a $S/3$.

### 2. Strategia di Risoluzione ($O(n)$)

 La tecnica ottimale utilizza le **somme prefisse** e un conteggio progressivo:

- **Pre-calcolo dei suffissi**: Si scansiona l'array da destra a sinistra per identificare tutte le posizioni in cui la "somma suffisso" è uguale a $S/3$. Si memorizzano queste informazioni in un array ausiliario (chiamato spesso `count`) che indica quanti "punti di taglio validi" per la terza parte esistono da quella posizione fino alla fine.
- **Scansione dei prefissi**: Si attraversa l'array da sinistra a destra calcolando la somma prefissa. Ogni volta che la somma prefissa è uguale a $S/3$, abbiamo trovato un possibile termine per la prima parte.
- **Conteggio finale**: Per ogni prima parte valida trovata in posizione $i$, il numero di modi per completare la divisione è pari al numero di suffissi validi (pari a $S/3$) che iniziano dopo la posizione $i+1$.

```rust
pub fn number_of_ways(a: &[i64]) -> usize {
    let sum: i64 = a.iter().sum();

    if sum % 3 != 0 {
        return 0;
    }

    let target = sum / 3;
    let mut c: Vec<_> = a
        .iter()
        .rev()
        .scan(0, |sum, e| {
            *sum += e;
            Some(*sum)
        })
        .scan(0, |counter, sum| {
            if sum == target {
                *counter += 1usize
            };
            Some(*counter)
        })
        .collect();

    c.reverse();

    let mut result = 0;
    let mut sum = 0;
    for (i, &v) in a[..a.len() - 2].iter().enumerate() {
        sum += v;
        if sum == target {
            result += c[i + 2];
        }
    }

    result
}
```

# Fenwick Tree

Il **Fenwick Tree**, noto anche come **Binary Indexed Tree (BIT)**, è una struttura dati che permette di mantenere somme prefisse e aggiornare elementi in un array in tempo logaritmico $O(\log n)$.

Ecco i dettagli fondamentali della sua struttura:

- **Rappresentazione Implicita:** A differenza degli alberi basati su nodi e puntatori, il BIT è memorizzato interamente in un **array**. Ogni cella dell'array memorizza la somma di un particolare intervallo di elementi dell'array originale.
- **Logica del LSB (Least Significant Bit):** La struttura sfrutta la rappresentazione binaria degli indici. L'ampiezza dell'intervallo coperto da una posizione $i$ è determinata dal suo bit meno significativo impostato a 1 (LSB). Questo valore si calcola rapidamente con l'operazione bitwise `i & (-i)`.
- **Navigazione dell'Albero:**
    - **Query di Somma Prefissa:** Per calcolare la somma fino all'indice $i$, si parte da quel punto e si "risale" verso lo zero sottraendo ripetutamente l'LSB dall'indice corrente.
    - **Aggiornamento (Add):** Per aggiungere un valore a un elemento in posizione $i$, si aggiorna la cella corrispondente e si "scendono" i nodi influenzati sommando ripetutamente l'LSB all'indice fino a raggiungere la dimensione massima dell'array.
- **Efficienza:** Entrambe le operazioni richiedono $O(\log n)$ tempo. In pratica, il Fenwick Tree è spesso preferito al Segment Tree per la sua estrema velocità e semplicità di implementazione, risultando fino a 2-4 volte più rapido nei test reali.

- ![[Pasted image 20260205181133.png]]

```rust
#[derive(Debug)]
pub struct FenwickTree {
    tree: Vec<i64>,
}

impl FenwickTree {
    pub fn with_len(n: usize) -> Self {
        Self {
            tree: vec![0; n + 1],
        }
    }

    pub fn len(&self) -> usize {
        self.tree.len() - 1
    }

    /// Indexing is 0-based, even if internally we use 1-based indexing
    pub fn add(&mut self, i: usize, delta: i64) {
        let mut i = i + 1; 
        assert!(i < self.tree.len());

        while i < self.tree.len() {
            self.tree[i] += delta;
            i = Self::next_sibling(i);
        }
    }

    /// Indexing is 0-based, even if internally we use 1-based indexing
    pub fn sum(&self, i: usize) -> i64 {
        let mut i = i + 1;  

        assert!(i < self.tree.len());
        let mut sum = 0;
        while i != 0 {
            sum += self.tree[i];
            i = Self::parent(i);
        }

        sum
    }

    pub fn range_sum(&self, l: usize, r: usize) -> i64 {
        self.sum(r) - if l == 0 { 0 } else { self.sum(l - 1) }
    }

    fn isolate_trailing_one(i: usize) -> usize {
        if i == 0 {
            0
        } else {
            1 << i.trailing_zeros()
        }
    }

    fn parent(i: usize) -> usize {
        i - Self::isolate_trailing_one(i)
    }

    fn next_sibling(i: usize) -> usize {
        i + Self::isolate_trailing_one(i)
    }
}
```
# Counting Inversions

Il problema del **Counting Inversions** consiste nel contare quante coppie di elementi in un array sono "fuori ordine". Formalmente, una coppia di indici $(i, j)$ è un'inversione se $i < j$ ma $A[i] > A[j]$. Questo valore è un'ottima misura di quanto un array sia lontano dall'essere perfettamente ordinato.

![[Pasted image 20260205174731.png]]

Ecco le strategie principali per risolverlo:

### 1. Approccio Merge Sort ($O(n \log n)$)

Questa è la soluzione classica basata sul paradigma _Divide et Impera_.

- **Divisione**: Si divide l'array in due metà e si contano ricorsivamente le inversioni in ciascuna parte.
- **Conteggio durante il Merge**: Il passaggio cruciale avviene quando si fondono le due metà già ordinate ($A$ e $B$). Se un elemento $b_j$ della metà destra viene inserito nell'array finale prima di un elemento $a_i$ della metà sinistra, allora $b_j$ forma un'inversione con **tutti** gli elementi rimanenti in $A$.
- Poiché i puntatori si muovono in modo lineare, il conteggio totale avviene in tempo $O(n \log n)$.

### 2. Approccio Fenwick Tree o BIT ($O(n \log n)$)

Un'alternativa elegante sfrutta il **Binary Indexed Tree** (BIT).

- Si scansiona l'array (solitamente da destra a sinistra) e per ogni elemento si interroga il BIT per sapere quanti elementi più piccoli sono già stati incontrati.
- Dopo ogni interrogazione, si aggiorna il BIT incrementando la frequenza del valore corrente.
- Se i valori nell'array sono molto grandi, si esegue prima un **remapping** (compressione delle coordinate) per mantenere la dimensione del BIT proporzionale a $n$.
- rank remapping => A\[i] -> position of A\[i] in A sorted (increasing order)

```rust
pub fn counting_inversions(a: &[u64]) -> usize {
    if a.is_empty() {
        return 0;
    }

    let max = *a.iter().max().unwrap() as usize;
    let mut ft = FenwickTree::with_len(max + 1);

    let mut count: usize = 0;
    for &e in a {
        count += ft.range_sum((e + 1) as usize, max) as usize;
        ft.add(e as usize, 1);
    }

    count
}
```

$\Theta(n \log n)$ time

# Nested Segments

Il problema dei **Nested Segments** richiede di determinare, per ogni segmento $[L_i, R_i]$ di un insieme di $n$, quanti altri segmenti sono completamente contenuti al suo interno.

Una soluzione ottimale in tempo $O(n \log n)$ si basa sull'utilizzo dei **Fenwick Tree** e sulla tecnica del **remapping**.

![[Pasted image 20260205182307.png]]

```rust
  // Input di esempio: (l, r)
    let raw_segments = vec![(1, 5), (7, 12), (2, 10), (3, 4), (6, 8), (9, 11)];
    let n = raw_segments.len();

    // 1. Prepariamo i segmenti mantenendo l'ID originale per l'output
    let mut segments: Vec<(i32, i32, usize)> = raw_segments
        .iter()
        .enumerate()
        .map(|(i, &(l, r))| (l, r, i))
        .collect();

    // 2. Compressione delle coordinate per gli endpoint destri (R)
    // Dobbiamo mappare i valori R unici in indici 0..n-1
    let mut r_coords: Vec<i32> = raw_segments.iter().map(|s| s.1).collect();
    r_coords.sort_unstable();
    r_coords.dedup();

    let get_r_index = |val: i32| -> usize {
        r_coords.binary_search(&val).unwrap()
    };

    // 3. Inizializziamo il Fenwick Tree con la dimensione corretta (numero di R unici)
    let mut ft = FenwickTree::with_len(r_coords.len());
    
    // Popoliamo il BIT con tutti i segmenti (basandoci sugli indici compressi)
    for &(_, r, _) in &segments {
        ft.add(get_r_index(r), 1);
    }

    // 4. Ordiniamo i segmenti per L crescente (Sweep Line)
    segments.sort_by_key(|s| s.0);

    let mut results = vec![0; n];

    // 5. Processiamo i segmenti
    for (l, r, original_id) in segments {
        let r_idx = get_r_index(r);
        
        // Rimuoviamo il contributo del segmento corrente
        ft.add(r_idx, -1);
        
        // Contiamo quanti segmenti hanno R < r_attuale
        // Poiché L è crescente, quelli rimasti nel BIT hanno L > l_attuale
        results[original_id] = ft.sum(r_idx);
    }

    // 6. Stampa i risultati nell'ordine originale
    for res in results {
        println!("{}", res);
    }
```
### Complessità

- **Tempo**: $O(n \log n)$, dominato dalla fase di ordinamento e dalle operazioni sul BIT.
- **Spazio**: $O(n)$ per memorizzare il Fenwick Tree e le mappature.

# Update the Array

Il problema **Update the Array** richiede di gestire un array $A$ di $n$ elementi (inizialmente tutti pari a 0) supportando due operazioni principali: l'aggiornamento di un intero intervallo $[i, j]$ con un valore $v$ e l'accesso al valore di un singolo elemento $A[i]$.

### Strategia: Array delle Differenze + Fenwick Tree

Per risolvere entrambe le operazioni in tempo logaritmico $O(\log n)$, si utilizza un **Fenwick Tree** (o BIT) applicato a un array ausiliario delle differenze $D$.

1. **Rappresentazione Implicita**: L'array originale $A$ è rappresentato in modo che ogni elemento $A[i]$ sia la somma prefissa dell'array delle differenze $D$, ovvero $A[i] = \sum_{k=1}^{i} D[k]$.
2. **Operazione di Update (Range Update)**: Per aggiungere un valore $v$ a tutti gli elementi nell'intervallo $[i, j]$, non si modificano tutti i valori di $A$. Invece, si aggiorna l'array delle differenze $D$ in soli due punti:
    - Si aggiunge $v$ a $D[i]$.
    - Si sottrae $v$ da $D[j+1]$. Questo garantisce che la somma prefissa (ovvero il valore di $A$) aumenti di $v$ solo per gli indici compresi tra $i$ e $j$.
3. **Operazione di Accesso (Point Query)**: Per ottenere il valore corrente di $A[i]$, si esegue una query di somma prefissa sul Fenwick Tree fino all'indice $i$.

```rust
#[derive(Debug)]
struct UpdateArray {
    ft: FenwickTree,
}

impl UpdateArray {
    pub fn with_len(n: usize) -> Self {
        Self {
            ft: FenwickTree::with_len(n),
        }
    }

    pub fn len(&self) -> usize {
        self.ft.len()
    }

    pub fn access(&self, i: usize) -> i64 {
        self.ft.sum(i)
    }

    pub fn range_update(&mut self, l: usize, r: usize, v: i64) {
        assert!(l <= r);
        assert!(r < self.ft.len());

        self.ft.add(l, v);
        if r + 1 < self.ft.len() {
            self.ft.add(r + 1, -v);
        }
    }
}
```

### Complessità

- **Tempo**: Entrambe le operazioni, `Update(i, j, v)` e `Access(i)`, richiedono **$O(\log n)$** grazie alla struttura del Fenwick Tree.
- **Spazio**: **$O(n)$** per memorizzare l'albero.

Questa tecnica è estremamente efficiente rispetto a un approccio banale (che richiederebbe tempo lineare $O(n)$ per ogni aggiornamento di intervallo) e trasforma un problema di "aggiornamento di un range" in un problema di "aggiornamento puntuale e query prefissa".

# Dynamic Prefix-Sums with Range-Update

Il problema del **Dynamic Prefix-Sums con Range-Update** richiede di gestire un array in cui è possibile aggiungere un valore $v$ a tutti gli elementi in un intervallo $[l, r]$ e, contemporaneamente, calcolare la somma dei primi $i$ elementi in tempo logaritmico $O(\log n)$,.

### La sfida tecnica

In una struttura statica, le somme prefisse si calcolano in $O(1)$, ma l'aggiornamento richiede $O(n)$. Per rendere dinamiche entrambe le operazioni, si utilizza solitamente il **Fenwick Tree** (o Binary Indexed Tree),. Tuttavia, un Fenwick Tree standard supporta nativamente solo aggiornamenti puntuali e query di intervallo, o aggiornamenti di intervallo e query puntuali (tramite l'array delle differenze). Risolvere contemporaneamente **aggiornamenti di intervallo** e **somme di intervallo** richiede un approccio più sofisticato.

### Soluzione con due Fenwick Tree

L'approccio ottimale prevede l'utilizzo di due Fenwick Tree distinti ($BIT_1$ e $BIT_2$) per tracciare i cambiamenti necessari a ricostruire la somma totale,.

1. **Array delle differenze**: Si definisce un array ausiliario $D$ tale che l'elemento originale $A[i]$ sia la somma prefissa di $D$ ($A[i] = \sum_{k=1}^i D[k]$). Un aggiornamento nell'intervallo $[l, r]$ di valore $v$ si traduce in due aggiornamenti puntuali su $D$: $+v$ in posizione $l$ e $-v$ in posizione $r+1$.
2. **Scomposizione della Somma**: La somma prefissa di $A$ fino a $i$ è $\sum_{k=1}^i A[k]$. Sostituendo $A[k]$ con la sua definizione basata su $D$, otteniamo che ogni $D[m]$ compare nella somma totale $(i - m + 1)$ volte. Matematicamente: $\sum_{k=1}^i A[k] = (i + 1) \sum_{m=1}^i D[m] - \sum_{m=1}^i (m \cdot D[m])$.
3. **Gestione dei due alberi**:
    - **$BIT_1$** memorizza i valori $D[m]$ per calcolare il termine $\sum D[m]$.
    - **$BIT_2$** memorizza i valori $(m \cdot D[m])$ per calcolare il termine correttivo $\sum (m \cdot D[m])$.

```rust
#[derive(Debug)]
struct RangeUpdate {
    ft1: FenwickTree,
    ft2: FenwickTree,
}

impl RangeUpdate {
    pub fn with_len(n: usize) -> Self {
        Self {
            ft1: FenwickTree::with_len(n),
            ft2: FenwickTree::with_len(n),
        }
    }

    pub fn len(&self) -> usize {
        self.ft1.len()
    }

    pub fn sum(&self, i: usize) -> i64 {
        self.ft1.sum(i) * i as i64 + self.ft2.sum(i)
    }

    pub fn access(&self, i: usize) -> i64 {
        self.sum(i) - if i == 0 { 0 } else { self.sum(i - 1) }
    }

    pub fn add(&mut self, i: usize, v: i64) {
        self.range_update(i, i, v)
    }

    pub fn range_update(&mut self, l: usize, r: usize, v: i64) {
        self.ft1.add(l, v);

        self.ft2.add(l, -v * (l as i64 - 1));

        if r + 1 < self.len() {
            self.ft1.add(r + 1, -v);
            self.ft2.add(r + 1, v * r as i64);
        }
    }
}
```
### Complessità e Performance

Grazie a questa scomposizione, sia l'aggiornamento dell'intervallo che la query della somma prefissa possono essere eseguiti in **$O(\log n)$**,. Questa tecnica è considerata estremamente efficiente e superiore in velocità rispetto ad altre strutture come i Segment Tree in molti scenari di programmazione competitiva.

# Segment Tree

Il **Segment Tree** è una struttura dati estremamente flessibile utilizzata per risolvere problemi di query su intervalli (come somme, minimi o massimi) e aggiornamenti dinamici in tempo logaritmico $O(\log n)$.

### Struttura e Costruzione

- **Rappresentazione ad Albero**: È un albero binario costruito sopra gli elementi di un array. La radice rappresenta l'intero intervallo $[0, n-1]$, mentre le foglie corrispondono alle singole posizioni dell'array originale.
- **Nodi Interni**: Ogni nodo intermedio è responsabile di un sotto-intervallo specifico e memorizza la "risposta" (somma, minimo, ecc.) per quel range. Questo valore viene calcolato combinando i risultati dei suoi due figli.
- **Memorizzazione**: Viene solitamente implementato tramite un **vettore**, dove i nodi sono indicizzati in modo simile a un heap: se un nodo è in posizione $i$, i suoi figli si trovano in $2i$ e $2i+1$. A differenza del Fenwick Tree, richiede spazio extra per memorizzare i nodi interni.

### Funzionamento delle Operazioni

1. **Aggiornamento (Update)**: Quando un elemento viene modificato, è necessario aggiornare tutti i nodi lungo il percorso dalla foglia alla radice ($O(\log n)$). Ogni nodo viene ricalcolato semplicemente guardando i nuovi valori dei suoi figli.
2. **Query di Intervallo**: La ricerca di un valore in un range $[i, j]$ è un processo ricorsivo che parte dalla radice e analizza tre casi:
    - **Overlap Totale**: Se l'intervallo del nodo è completamente contenuto nel range della query, si restituisce direttamente il valore memorizzato nel nodo.
    - **Overlap Parziale**: Se solo una parte del nodo è coinvolta, la query prosegue ricorsivamente su entrambi i figli e i risultati vengono combinati.
    - **Nessun Overlap**: Se l'intervallo del nodo è fuori dal range richiesto, la ricorsione in quel ramo si ferma.

### Complessità ed Efficienza

Entrambe le operazioni, aggiornamento e query, richiedono tempo **$O(\log n)$**. Sebbene la costante possa essere leggermente più alta rispetto a un Fenwick Tree (circa 4 volte il logaritmo per via della gestione dei figli), il Segment Tree è molto più potente perché può gestire operazioni non invertibili come il calcolo del minimo o del massimo in un intervallo (RMQ).

# ST problem 1

A\[1,n] no negative integers

- Add(i,v)
- RangeSum(i,j)
- Search(s): reports the position of the shortest prefix of A such that $\sum_{k=1}^i A[k] >= s$

Il **Segment Tree** è una scelta eccellente per questo problema, poiché permette di gestire aggiornamenti, somme di intervalli e ricerche di soglia in tempo logaritmico $O(\log n)$.

Ecco come si implementano le operazioni richieste:

- **Add(i, v):** Si parte dalla foglia che rappresenta l'indice $i$ e si risale verso la radice, aggiornando la somma in ogni nodo incontrato lungo il percorso. Questa operazione richiede tempo $O(\log n)$.
- **RangeSum(i, j):** La query attraversa l'albero combinando i valori dei nodi che coprono completamente o parzialmente l'intervallo $[i, j]$. Grazie alla struttura dell'albero, vengono visitati al massimo $4 \log n$ nodi, garantendo una complessità $O(\log n)$.
- **Search(s):** Poiché l'array non contiene numeri negativi, le somme dei prefissi sono monotone. Invece di una ricerca binaria esterna (che costerebbe $O(\log^2 n)$), puoi "scendere" nell'albero in $O(\log n)$. Se la somma memorizzata nel figlio sinistro è $\ge s$, ti muovi a sinistra; altrimenti, sottrai la somma del figlio sinistro da $s$ e ti muovi a destra.

Rispetto al Fenwick Tree, il Segment Tree richiede più memoria (circa $4n$ nodi) ma è più flessibile per generalizzare il problema a operazioni non invertibili come il minimo o il massimo (RMQ).

# ST Problem 2

A\[1,n] integers
- add(i,v)
- occs(i,j,v) = report the number of occurences ov v in A\[i..j]

Per risolvere il problema del conteggio delle occorrenze in un intervallo dinamico con un **Segment Tree**, ogni nodo dell'albero deve memorizzare una struttura dati (come una `HashMap` o un vettore ordinato) che tenga traccia delle frequenze di tutti gli elementi presenti nel suo sotto-intervallo.

Ecco come funzionano le operazioni:

- **`add(i, v)`**: Quando si aggiorna un elemento $A[i]$, l'algoritmo risale dalla foglia corrispondente fino alla radice. In ogni nodo incontrato lungo il percorso, si aggiorna la struttura dati interna (ad esempio, rimuovendo o decrementando il vecchio valore e inserendo o incrementando il nuovo) in tempo logaritmico rispetto alla profondità dell'albero.
- **`occs(i, j, v)`**: La query di intervallo decompone il range $[i, j]$ in al più $O(\log n)$ nodi. Per ogni nodo che rientra completamente nell'intervallo richiesto, si interroga la sua mappa (o il suo vettore) per ottenere il numero di occorrenze di $v$, sommando poi i risultati parziali.

**Complessità e considerazioni:** Questa soluzione richiede uno spazio di $O(n \log n)$ per memorizzare le informazioni distribuite nei nodi. Il tempo per ogni operazione dipende dall'efficienza della struttura dati scelta per i nodi: con una `HashMap`, il tempo atteso è $O(\log n)$, mentre con un vettore ordinato (usando la ricerca binaria) è $O(\log^2 n)$.

# ST Problem 3

Per risolvere il problema del successore in un intervallo dinamico con un **Segment Tree**, ogni nodo dell'albero deve memorizzare gli elementi del proprio sotto-intervallo in una struttura dati che supporti la ricerca ordinata, come un **vettore ordinato** o un **albero binario di ricerca (BST)**. Il successore di $k$ è definito come il più piccolo valore $y$ nell'intervallo tale che $y \ge k$.

Ecco come si implementano le operazioni:

- **`add(i, v)`**: L'algoritmo parte dalla foglia corrispondente all'indice $i$ e risale verso la radice aggiornando circa $O(\log n)$ nodi. In ogni nodo, è necessario rimuovere il vecchio valore $A[i]$ e inserire il nuovo valore aggiornato nella struttura dati interna (BST o vettore) per mantenere l'ordinamento.
- **`successor(i, j, k)`**: La query decompone l'intervallo richiesto $[i, j]$ in un massimo di $O(\log n)$ nodi canonici. Per ogni nodo coinvolto, si interroga la struttura interna per trovare il minimo elemento $\ge k$ (tramite ricerca binaria o ricerca nel BST). Il successore globale dell'intervallo sarà il minimo tra tutti i successori locali trovati.

**Complessità e considerazioni:** Questa struttura richiede uno spazio di **$O(n \log n)$** per memorizzare gli elementi duplicati nei vari livelli dell'albero. Il tempo di esecuzione per entrambe le operazioni è tipicamente **$O(\log^2 n)$** se si usa la ricerca binaria su vettori ordinati, ma può essere ottimizzato in base alla struttura interna scelta.

# Triplets

Il problema di contare le triplette $(i, j, k)$ tali che $A[i] < A[j] < A[k]$ con indici $i < j < k$ può essere risolto efficacemente sfruttando la logica dell'elemento centrale e strutture dati avanzate per ottimizzare i tempi di ricerca.

### 1. Strategia dell'elemento centrale

L'approccio più intuitivo per superare la forza bruta $O(n^3)$ consiste nel fissare l'elemento $A[j]$ come il "centro" della tripletta. Per ogni posizione $j$, il numero di triplette valide è dato dal prodotto tra:

- Il numero di elementi a sinistra di $j$ ($i < j$) che sono strettamente minori di $A[j]$.
- Il numero di elementi a destra di $j$ ($k > j$) che sono strettamente maggiori di $A[j]$.

Sommando questi prodotti per ogni possibile $j$ (da $1$ a $n-2$), si ottiene il numero totale di triplette.

### 2. Ottimizzazione con Fenwick Tree (BIT)

Per evitare una scansione lineare per ogni $j$, che porterebbe a una complessità $O(n^2)$, si può utilizzare un **Fenwick Tree** (o Binary Indexed Tree) per contare gli elementi in tempo logaritmico $O(\log n)$,.

- **Passaggio a sinistra**: Si scansiona l'array da sinistra a destra. Per ogni elemento $A[j]$, si interroga il BIT per sapere quanti elementi minori di $A[j]$ sono stati inseriti finora, quindi si aggiunge $A[j]$ al BIT,.
- **Passaggio a destra**: Si esegue una procedura simile partendo da destra per contare gli elementi maggiori, oppure si calcola il valore per differenza conoscendo le frequenze totali.

### 3. Gestione di valori grandi (Remapping)

Se gli interi nell'array $A$ sono molto grandi o sparsi, la dimensione del Fenwick Tree diventerebbe eccessiva. In questo caso, è necessario applicare la tecnica del **remapping** (o compressione delle coordinate),:

1. Si ordinano i valori distinti presenti in $A$.
2. Si sostituisce ogni valore con il suo "rango" (la sua posizione nell'ordinamento).
3. L'array risultante conterrà solo valori nell'intervallo $[1, n]$, permettendo l'uso di un BIT di dimensioni contenute,.

### Complessità Finale

- **Tempo**: $O(n \log n)$, dominato dall'ordinamento per il remapping e dalle $n$ operazioni sul Fenwick Tree,.
- **Spazio**: $O(n)$ per memorizzare il Fenwick Tree e gli array ausiliari per i conteggi,.

Questa tecnica è una generalizzazione di quella usata per il problema del _Counting Inversions_, dove però si cercano coppie "fuori ordine" anziché triplette ordinate.

# ST Range Update with lazy propagation

#TODO FROM IPAD

# Persistent ST

Un **Persistent Segment Tree** è una variante del Segment Tree che permette di mantenere e interrogare tutte le versioni passate della struttura dati dopo ogni aggiornamento.

Ecco il piano che ti propongo per esplorare l'argomento:

1. **Concetto di Persistenza**: Come l'albero "ricorda" la sua storia.
2. **Meccanismo di Node-Sharing**: Come risparmiare memoria riutilizzando i nodi.
3. **Analisi della Complessità**: Perché è efficiente in termini di tempo e spazio.
4. **Applicazioni classiche**: Problemi come il _K-th smallest element_ in un range.

### Cos'è la Persistenza?

In una struttura dati persistente, un aggiornamento non sovrascrive i dati esistenti, ma crea una nuova versione preservando quella precedente. In un Segment Tree, questo si ottiene creando un nuovo nodo radice per ogni operazione di modifica.

### Come funziona (Node-Sharing)

Invece di copiare l'intero albero (che costerebbe $O(n)$), si sfruttano le proprietà degli alberi binari:

- **Percorso di aggiornamento**: Ogni modifica a una foglia influenza solo il percorso diretto dalla foglia alla radice ($O(\log n)$ nodi).
- **Riutilizzo dei nodi**: I nodi che non appartengono a questo percorso rimangono invariati e vengono "condivisi" tra la vecchia e la nuova versione.
- **Puntatori**: La nuova radice punterà a una combinazione di nuovi nodi (quelli modificati) e nodi esistenti della versione precedente.

#TODO FROM IPAD
### Complessità

- **Tempo**: $O(\log n)$ per ogni aggiornamento, poiché si visitano e creano solo i nodi lungo un singolo percorso.
- **Spazio**: $O(\log n)$ per ogni aggiornamento, poiché si aggiungono solo circa $\log n$ nuovi nodi alla memoria totale.

# Mo's Algo

L'**Algoritmo di Mo** è una tecnica potente per risolvere problemi di query su intervalli (range queries) in modalità **offline**, ovvero quando tutte le query sono note in anticipo.

### 1. La Strategia Core: Reordinamento
 
Il segreto dell'efficienza di Mo non risiede in una struttura dati complessa, ma nel modo in cui le query vengono ordinate per minimizzare il movimento di due puntatori, `L` e `R`.

1. **Divisione in blocchi**: L'array di dimensione $N$ viene diviso idealmente in blocchi di dimensione $\sqrt{N}$ .
2. **Ordinamento**: Le query $[L, R]$ vengono ordinate:
    - Primariamente in base al **blocco** in cui cade l'indice sinistro $L$ ($L / \sqrt{N}$) .
    - Secondariamente (in caso di parità di blocco) in base all'indice destro $R$ .

### 2. Funzionamento (Puntatori Mobili)

L'algoritmo mantiene un risultato corrente e due puntatori che delimitano l'intervallo attuale . Per passare da una query alla successiva, i puntatori vengono spostati verso i nuovi estremi. Ogni spostamento invoca una di due funzioni fondamentali :

- **`add(pos)`**: Aggiunge l'elemento alla posizione `pos` nel calcolo corrente.
- **`remove(pos)`**: Rimuove l'elemento alla posizione `pos` dal calcolo corrente.

```rust
pub fn three_or_more(a: &[usize], queries: &[(usize, usize)]) -> Vec<usize> {
    let mut counters: Vec<usize> = vec![0; a.len()];
    let mut answers = Vec::with_capacity(queries.len());

    let mut cur_l = 0;
    let mut cur_r = 0; // here right endpoint is excluded
    let mut answer = 0;

    for &(l, r) in queries {
        let mut add = |i| {
            counters[a[i]] += 1;
            if counters[a[i]] == 3 {
                answer += 1
            }
        };

        while cur_l > l {
            cur_l -= 1;
            add(cur_l);
        }

        while cur_r <= r {
            add(cur_r);
            cur_r += 1;
        }

        let mut remove = |i| {
            counters[a[i]] -= 1;
            if counters[a[i]] == 2 {
                answer -= 1
            }
        };

        while cur_l < l {
            remove(cur_l);
            cur_l += 1;
        }

        while cur_r > r + 1 {
            cur_r -= 1;
            remove(cur_r);
        }

        answers.push(answer);
    }

    answers
}

pub fn mos(a: &[usize], queries: &[(usize, usize)]) -> Vec<usize> {
    // Sort the queries by bucket and get the permutation induced by this sorting.
    // The latter is needed to permute the answers back to the original ordering
    let mut sorted_queries: Vec<_> = queries.iter().cloned().collect();
    let mut permutation: Vec<usize> = (0..queries.len()).collect();

    let sqrt_n = (a.len() as f64) as usize + 1;
    sorted_queries.sort_by_key(|&(l, r)| (l / sqrt_n, r));
    permutation.sort_by_key(|&i| (queries[i].0 / sqrt_n, queries[i].1));

    let answers = three_or_more(a, &sorted_queries);

    let mut permuted_answers = vec![0; answers.len()];
    for (i, answer) in permutation.into_iter().zip(answers) {
        permuted_answers[i] = answer;
    }

    permuted_answers
}
```

### 3. Analisi della Complessità

Grazie all'ordinamento per blocchi, i puntatori non "viaggiano" troppo :

- Il puntatore destro $R$ si muove in modo monotono all'interno di ogni blocco.
- Il puntatore sinistro $L$ si muove al massimo di $\sqrt{N}$ per ogni query.
- **Tempo totale**: **$O((N+Q)\sqrt{N})$**, dove $Q$ è il numero di query. Questo è circa $\sqrt{N}$ volte più veloce dell'approccio a forza bruta $O(N \cdot Q)$.

### Applicazioni

È ideale per problemi dove la risposta per un intervallo $[L, R]$ non può essere calcolata facilmente con somme prefisse o Segment Tree, come il conteggio degli **elementi distinti** o di elementi che appaiono almeno $K$ volte .

# Static RMQ

Il problema **Static RMQ** (Range Minimum Query) consiste nel trovare il valore minimo (o la sua posizione) all'interno di un intervallo specifico $[i, j]$ di un array che non subisce modifiche nel tempo,,. L'obiettivo ideale è ottenere una risposta in tempo costante $O(1)$ con una fase di pre-elaborazione efficiente,.

Ecco le principali strategie risolutive analizzate nei sorgenti:

### 1. Tabulazione Completa ($O(n^2)$ spazio, $O(1)$ query)

L'approccio più semplice consiste nel pre-calcolare le risposte per ogni possibile coppia di indici $[i, j]$ e memorizzarle in una tabella,.

- **Vantaggio**: La query è un semplice accesso a una matrice.
- **Svantaggio**: Richiede tempo e spazio quadratici, rendendolo inutilizzabile per array di grandi dimensioni,.

### 2. Sparse Table ($O(n \log n)$ spazio, $O(1)$ query)

Questa tecnica sfrutta la proprietà che il minimo di un intervallo può essere ottenuto combinando i risultati di due intervalli sovrapposti la cui lunghezza è una potenza di 2,.

- **Pre-elaborazione**: Si calcolano i minimi per tutti gli intervalli di lunghezza $2^k$. Ogni posizione $i$ memorizza circa $\log n$ risposte.
- **Query**: Per un intervallo $[i, j]$, si selezionano due blocchi pre-calcolati di lunghezza $2^k$ (dove $2^k$ è la più grande potenza di 2 che non supera la lunghezza dell'intervallo) che coprono interamente il range sovrapponendosi.
- **Efficienza**: È una delle soluzioni più comuni grazie al tempo di query costante e allo spazio gestibile.

#TODO FROM IPAD
### 3. Alberi Cartesiani e LCA ($O(n)$ spazio, $O(1)$ query)

Una tecnica avanzata permette di ridurre lo spazio a lineare trasformando l'RMQ in un problema di **Lowest Common Ancestor (LCA)** su un albero,,.

- **Costruzione**: Si crea un **Albero Cartesiano** in cui la radice è il valore minimo dell'array e i sottoalberi sinistro e destro sono costruiti ricorsivamente sulle porzioni rimanenti dell'array.
- **Logica**: Il minimo tra due indici $i$ e $j$ corrisponde esattamente al Lowest Common Ancestor dei nodi $i$ e $j$ nell'albero costruito.
- **Risultato**: Utilizzando algoritmi specifici per l'LCA, si ottiene una query $O(1)$ con spazio $O(n)$.

#TODO FROM IPAD

# Colored Range Query

Il **Colored Range Query Problem** richiede di identificare tutti i colori distinti all'interno di un intervallo $[i, j]$ di un array $A$ di $n$ elementi. La sfida principale è fornire una risposta in tempo proporzionale al numero $k$ di colori distinti trovati, indipendentemente dall'ampiezza dell'intervallo.

Esistono due approcci principali per risolverlo:

### 1. Soluzione con Segment Tree

In questa configurazione, ogni nodo dell'albero memorizza un `HashSet` (o un vettore ordinato) contenente i colori unici presenti nel suo sotto-intervallo.

- **Query**: Si decompone l'intervallo $[i, j]$ nei nodi canonici e si fondono i loro set.
- **Complessità**: Richiede uno spazio di $O(n \log n)$ e il tempo di query dipende dall'efficienza dell'unione dei set.

### 2. Soluzione Ottimale tramite RMQ

Questa tecnica riduce il problema a una serie di **Range Minimum Queries** su un array ausiliario $P$.

- **Array dei Puntatori ($P$)**: Per ogni posizione $k$, $P[k]$ memorizza l'indice dell'occorrenza precedente dello stesso colore di $A[k]$ (o $-1$ se è la prima occorrenza).
- **Intuizione**: Un colore in posizione $k$ è la "prima" occorrenza all'interno di $[i, j]$ se e solo se il suo puntatore precedente $P[k]$ è fuori dall'intervallo a sinistra ($P[k] < i$).
- **Algoritmo**:
    1. Esegui un RMQ sull'intervallo $[i, j]$ dell'array $P$ per trovare l'indice $min$ con il valore minimo.
    2. Se $P[min] < i$, il colore $A[min]$ è un nuovo colore distinto: riportalo.
    3. Dividi ricorsivamente l'intervallo in $[i, min-1]$ e $[min+1, j]$ e ripeti finché il minimo trovato è $\ge i$.

**Complessità finale**: Utilizzando una struttura RMQ statica (come una Sparse Table) che risponde in $O(1)$, l'intero processo richiede tempo **$O(k)$** e spazio **$O(n)$**.

# Dynamic Programming

## Fibonacci

I numeri di Fibonacci sono definiti dalla relazione ricorsiva $F_n = F_{n-1} + F_{n-2}$, con i casi base $F_0 = 0$ e $F_1 = 1$. Un approccio ricorsivo banale ha una complessità temporale esponenziale $O(\phi^n)$, poiché ricalcola ripetutamente gli stessi sotto-problemi.

Per risolvere il problema in modo efficiente, si possono utilizzare diverse strategie:

- **Programmazione Dinamica (Top-Down):** Attraverso la _memoization_, i risultati dei sotto-problemi vengono salvati in un array per essere riutilizzati, riducendo il tempo a $O(n)$.
- **Approccio Iterativo (Bottom-Up):** Si riempie un array partendo dai casi base fino a $n$, richiedendo tempo lineare $O(n)$ e spazio costante se si mantengono solo gli ultimi due valori.
- **Esponenziazione di Matrici:** Utilizzando la matrice magica 
$$
\begin{pmatrix} 
1 & 1 \\
1 & 0 
\end{pmatrix} ^n
$$ e l'algoritmo di _fast exponentiation_, è possibile calcolare l'ennesimo numero di Fibonacci in tempo logaritmico $O(\log n)$.

## Rod Cutting

Il problema del **Rod Cutting** consiste nel determinare come tagliare un'asta di lunghezza $n$ in pezzi più corti per massimizzare il ricavo totale, dato un listino prezzi $p_i$ per ogni lunghezza di pezzo $i$.

Ecco i dettagli della soluzione basata sulla programmazione dinamica:

### 1. Substruttura Ottimale e Ricorrenza

Il problema esibisce una **substruttura ottimale**: una soluzione ottimale per un'asta di lunghezza $n$ incorpora le soluzioni ottimali per sottoproblemi più piccoli (i pezzi rimanenti dell'asta). La formula di ricorrenza per il ricavo massimo $r_n$ è: $r_n = \max_{1 \le i \le n} (p_i + r_{n-i})$ In questa formulazione, consideriamo un primo pezzo di lunghezza $i$ che non viene più tagliato e lo combiniamo con la soluzione ottimale per la parte rimanente di lunghezza $n-i$.
### 2. Approccio di Programmazione Dinamica (DP)

Per ottimizzare, si memorizzano i risultati dei sottoproblemi in una tabella per evitare calcoli ridondanti:

- **Bottom-up**: È il metodo più comune. Si risolvono i sottoproblemi in ordine di dimensione crescente (da 0 a $n$) e si salvano le risposte in un array `r[0..n]`.
- **Top-down con Memoization**: Si mantiene la struttura ricorsiva ma si controlla se la soluzione per una determinata lunghezza è già presente nella tabella prima di procedere.

```
def rod(n):
	R = [0] *(n+1)
	for i in range(n+1):
		for l in range(i):
			R[i] = max(R[i], R[i-l] + p[l])
```

### 4. Complessità

Entrambi i metodi DP riducono drasticamente il tempo di calcolo:

- **Tempo**: $O(n^2)$, dovuto ai due cicli annidati che scorrono le lunghezze dell'asta e i possibili tagli.
- **Spazio**: $O(n)$ per memorizzare l'array dei ricavi ottimali.

### 5. Ricostruzione della Soluzione

Per non limitarsi a conoscere il valore massimo ma sapere esattamente dove tagliare, si utilizza un array ausiliario `s[j]` che registra la dimensione del primo pezzo scelto per ottenere il massimo profitto per la lunghezza $j$. Iterando su questo array partendo da $n$, è possibile stampare tutte le dimensioni dei pezzi tagliati.
## Shortest path on a DAG

Il calcolo del cammino minimo su un **Grafo Diretto Aciclico (DAG)** è un problema che può essere risolto in tempo lineare $\Theta(V + E)$, risultando molto più efficiente degli algoritmi di Dijkstra o Bellman-Ford applicati a grafi generici.

Ecco la strategia dettagliata suddivisa nei suoi passaggi fondamentali:

### 1. Ordinamento Topologico (Linearizzazione)

Il primo passo consiste nell'eseguire un **ordinamento topologico** dei vertici. Questo processo dispone i nodi in una sequenza lineare tale che, per ogni arco diretto $(u, v)$, il nodo $u$ preceda sempre il nodo $v$ nella sequenza.

- **Perché è fondamentale:** Garantisce che quando processiamo un nodo $v$, abbiamo già considerato e calcolato definitivamente i cammini minimi verso tutti i nodi che possono raggiungere $v$.

### 2. Inizializzazione

Si preparano i valori delle distanze:

- Si imposta la distanza del nodo sorgente $s$ a $0$ ($s.d = 0$).
- Si impostano le distanze di tutti gli altri nodi a infinito ($\infty$).
- I predecessori ($\pi$) vengono inizializzati a NIL.

### 3. Rilassamento degli archi

Seguendo l'ordine stabilito dal sort topologico, si esamina ogni nodo $u$ una sola volta. Per ogni nodo $u$:

- Si analizzano tutti i suoi archi uscenti verso i vicini $v$.
- Si esegue l'operazione di **rilassamento (RELAX)**: se il percorso che passa per $u$ è più breve di quello memorizzato attualmente per $v$, si aggiorna la distanza di $v$.
- La formula è: $v.d = \min(v.d, u.d + w(u, v))$.

### Perché questa strategia è superiore?

- **Niente Code di Priorità:** A differenza di Dijkstra, non serve un heap per estrarre il minimo, poiché l'ordine topologico ci fornisce già la sequenza corretta di elaborazione.
- **Passata Singola:** Mentre Bellman-Ford richiede $|V|-1$ passate su tutti gli archi, nel DAG è sufficiente una sola scansione.
- **Archi Negativi:** L'algoritmo funziona correttamente anche in presenza di pesi negativi, poiché l'assenza di cicli impedisce la formazione di cicli di peso negativo.

### Complessità

- **Tempo:** $\Theta(V + E)$, poiché il sort topologico richiede $\Theta(V + E)$ e ogni arco viene rilassato esattamente una volta.
- **Spazio:** $\Theta(V)$ per memorizzare distanze e predecessori.

Questa tecnica è così potente che molte soluzioni di **Programmazione Dinamica** (come il problema del _Rod Cutting_ o la _Longest Common Subsequence_) possono essere modellate e risolte proprio come una ricerca del cammino massimo o minimo su un DAG.

## Facebook Robber

Il problema **Facebook Robber** (o _House Robber_) consiste nel determinare come svaligiare una fila di $n$ case per massimizzare il bottino, sapendo che non è possibile derubare due case adiacenti senza far scattare l'allarme.

### Soluzione con Programmazione Dinamica

La strategia ottimale prevede di calcolare il profitto massimo $M[i]$ per ogni casa $i$ utilizzando la seguente ricorrenza: $M[i] = \max(v_i + M[i-2], M[i-1])$. In ogni passaggio, si decide se:

1. **Rubare nella casa attuale**: aggiungendo il suo valore $v_i$ al profitto ottenuto fino a due case precedenti.
2. **Saltare la casa attuale**: mantenendo il profitto accumulato fino alla casa immediatamente precedente.

### Modellazione tramite DAG

È possibile visualizzare il problema come la ricerca del **cammino più lungo** in un Grafo Diretto Aciclico (DAG). In questo modello, ogni casa è un nodo e gli archi collegano solo case compatibili (non adiacenti), con pesi corrispondenti al valore del bottino.

#TODO FROM IPAD
### Efficienza

- **Tempo:** $O(n)$, in quanto è sufficiente una singola passata attraverso l'array delle case.
- **Spazio:** $O(n)$ se si usa un array di supporto, riducibile a $O(1)$ mantenendo solo i risultati delle ultime due case.

## Snakes and ladders

Il problema **Snakes and Ladders** (Serpenti e Scale) consiste nel trovare il numero minimo di lanci di dado necessari per raggiungere l'ultima casella di un tabellone partendo dalla prima. 
### 1. Modellazione tramite Grafo

Il modo più efficace per risolvere il problema è rappresentare il tabellone come un **grafo diretto**.

- **Vertici**: Ogni casella del tabellone (da 1 a 100) corrisponde a un nodo del grafo.
- **Archi**: Ogni lancio di dado rappresenta un potenziale spostamento. Da ogni casella partono 6 archi, corrispondenti ai risultati del dado (1-6).

### 2. Gestione di Scale e Serpenti

Scale e serpenti non sono nodi separati, ma influenzano la destinazione degli archi:

- **Scale**: Se un lancio di dado porta alla base di una scala, il giocatore viene trasportato immediatamente alla casella in cima. L'arco punterà quindi direttamente alla cella finale della scala.
- **Serpenti**: Se un lancio porta alla testa di un serpente, il giocatore scivola verso la coda. L'arco punterà alla casella di arrivo del serpente.

### 3. Algoritmo Risolutivo

Poiché ogni lancio di dado ha lo stesso costo (pari a 1 mossa), il problema di trovare il numero minimo di lanci equivale a cercare il **cammino minimo** in un grafo con pesi unitari.

- L'algoritmo ottimale per questo scenario è la **Breadth-First Search (BFS)**.
- La BFS esplora il grafo "a ondate", garantendo che la prima volta che si raggiunge la casella finale, lo si faccia attraverso il percorso più breve possibile.

### 4. Complessità

- **Tempo**: $O(V + E)$, dove $V$ è il numero di caselle (es. 100) ed $E$ è il numero di archi (circa $6 \times V$). In un tabellone standard, il calcolo è quasi istantaneo.
- **Spazio**: $O(V)$ per memorizzare le distanze e la coda della BFS.

## Minimum Cost Path

Il problema del **Minimum Cost Path** richiede di trovare il percorso con il costo totale minimo per spostarsi dall'angolo in alto a sinistra all'angolo in basso a destra di una matrice $n \times m$ contenente numeri interi.

### Vincoli e Movimento

La regola fondamentale è che ci si può spostare esclusivamente in due direzioni: verso il **basso** o verso **destra**. Il costo di un percorso è dato dalla somma dei valori numerici incontrati nelle celle attraversate.

### Strategia di Risoluzione: Programmazione Dinamica

Per risolvere il problema in modo efficiente, si utilizza la programmazione dinamica costruendo una matrice dei costi $C$ dove ogni cella $(i, j)$ memorizza il costo minimo per raggiungerla.

1. **Casi Base**: Il costo per la cella di partenza $C$ è semplicemente il valore $A$. Per le celle nella prima riga o nella prima colonna, il costo è la somma cumulativa dei valori precedenti, poiché esiste un solo percorso possibile (tutto a destra o tutto in basso).
2. **Relazione di Ricorrenza**: Per ogni altra cella $(i, j)$, il costo minimo è calcolato come: $C[i, j] = A[i, j] + \min(C[i-1, j], C[i, j-1])$. In pratica, scegliamo la cella di provenienza (quella sopra o quella a sinistra) che ha il costo accumulato minore.

### Modellazione tramite DAG

Il problema può essere visualizzato anche come la ricerca del **cammino minimo in un Grafo Diretto Aciclico (DAG)**. In questo modello, ogni cella della matrice diventa un vertice e gli archi collegano ogni nodo ai suoi vicini raggiungibili (destra e basso), con pesi corrispondenti ai valori delle celle di destinazione.

### Complessità

- **Tempo**: $O(n \times m)$, poiché l'algoritmo deve esaminare ogni cella della matrice esattamente una volta.
- **Spazio**: $O(n \times m)$ per memorizzare la matrice dei costi, sebbene sia possibile ottimizzarlo a $O(\min(n, m))$ mantenendo solo le informazioni necessarie della riga precedente.

## Longest Common Sequence (LCS)

Il problema della **Longest Common Subsequence (LCS)** consiste nel trovare la sottosequenza più lunga comune a due stringhe $X$ e $Y$. Una sottosequenza è definita come la sequenza originale a cui sono stati rimossi zero o più elementi, mantenendo l'ordine dei simboli rimanenti.

### Sottostruttura Ottimale

La risoluzione tramite programmazione dinamica si basa sulla scomposizione in sottoproblemi relativi ai prefissi delle stringhe. La relazione di ricorrenza prevede due casi principali:

1. **Match**: Se gli ultimi caratteri dei prefissi coincidono ($x_i = y_j$), la lunghezza dell'LCS è $1 +$ la lunghezza dell'LCS dei prefissi ridotti ($X_{i-1}, Y_{j-1}$).
2. **Mismatch**: Se i caratteri non coincidono ($x_i \neq y_j$), si prende il valore massimo tra l'LCS di ($X_{i-1}, Y_j$) e l'LCS di ($X_i, Y_{j-1}$).
3. LCS(i,j) = 0 (i == 0 or j == 0) | 1+LCS(i-1,j-1) (X\[i] == Y\[i]) | max(LCS(i-1,j), LCS(i,j-1)) (otherwise)

### Algoritmo e Complessità

L'approccio ottimale prevede una soluzione **Bottom-Up**, riempiendo una tabella di dimensioni $m \times n$ (dove $m$ e $n$ sono le lunghezze delle stringhe).

- **Tempo**: $O(m \times n)$, poiché ogni cella della tabella viene calcolata in tempo costante.
- **Spazio**: $O(m \times n)$ per memorizzare la matrice dei risultati. Tuttavia, se è richiesta solo la lunghezza della sequenza e non la sequenza stessa, lo spazio può essere ridotto a $O(\min(m, n))$ mantenendo solo due righe della tabella.

### Ricostruzione della Soluzione

Per ottenere i simboli che compongono l'LCS, è necessario tracciare a ritroso il percorso nella tabella partendo dalla cella finale ($c[m, n]$). Ogni volta che il valore di una cella è stato determinato da un "match", il carattere corrispondente viene incluso nella soluzione.

## 0/1 Knapsack

Il problema del **0/1 Knapsack** consiste nel selezionare un sottoinsieme di $n$ oggetti, ognuno con un peso $w_i$ e un valore $v_i$, per massimizzare il valore totale senza superare una capacità massima $W$. Il termine "0/1" indica che ogni oggetto deve essere interamente incluso o escluso, rendendo l'approccio greedy inefficace per questa variante.

### Strategia Risolutiva: Programmazione Dinamica

Il problema presenta una **substruttura ottimale**: una soluzione ottima per $i$ oggetti e capacità $w$ incorpora le soluzioni ottime per i primi $i-1$ oggetti.

**Equazione di ricorrenza:** Sia $OPT(i, w)$ il valore massimo ottenibile utilizzando i primi $i$ oggetti con capacità residua $w$:

- Se $w < w_i$: $OPT(i, w) = OPT(i-1, w)$ (l'oggetto è troppo pesante).
- Altrimenti: $OPT(i, w) = \max(OPT(i-1, w), v_i + OPT(i-1, w - w_i))$.
- K\[i,j] = 0 (i == 0 or j == 0) | max($v_i+K[i-1,j-w_i],K[i-1,j]$)

### Complessità ed Efficienza

- **Tempo e Spazio:** L'algoritmo riempie una tabella di dimensioni $(n+1) \times (W+1)$, richiedendo tempo **$O(nW)$**.
- **Natura Pseudo-polinomiale:** Poiché la complessità dipende dal valore numerico di $W$ e non solo dal numero di bit necessari a rappresentarlo, l'algoritmo è considerato pseudo-polinomiale. Se $W$ è estremamente grande, il problema diventa computazionalmente intrattabile (NP-hard).

### Varianti e Ottimizzazioni

1. **Reclupero della soluzione:** È possibile ricostruire l'insieme degli oggetti scelti tracciando a ritroso le decisioni memorizzate nella tabella $M$ in tempo $O(n)$.
2. **Knapsack basato sui valori:** Se i pesi sono molto grandi ma i valori sono piccoli, si può utilizzare una ricorrenza alternativa che minimizza il peso per un dato profitto, con complessità $O(n^2 v_{max})$.
3. **Approssimazione (PTAS):** Per istanze con valori molto grandi, si possono arrotondare e scalare i valori degli oggetti per ottenere una soluzione entro un fattore $(1 + \epsilon)$ dall'ottimo in tempo polinomiale.

## Fractional Knapsack 

Il **Fractional Knapsack problem** (o problema dello zaino frazionario) è una variante del classico problema dello zaino in cui è possibile selezionare frazioni di oggetti anziché doverli includere o escludere interamente (0/1). Questa proprietà lo rende risolvibile in modo ottimale tramite un **approccio greedy**, a differenza della versione 0/1 che richiede la programmazione dinamica.

Ecco come funziona la strategia risolutiva:

- **Calcolo del rapporto valore/peso:** Per ogni oggetto $i$, si calcola il rapporto $v_i/w_i$, che rappresenta il valore per unità di peso.
- **Ordinamento:** Si ordinano gli oggetti in ordine decrescente in base a questo rapporto.
- **Selezione Greedy:** Si scorre la lista degli oggetti così ordinata e si inseriscono nello zaino:
    1. L'intero oggetto, se la capacità residua lo consente.
    2. La frazione necessaria a riempire completamente lo zaino, se l'oggetto è più pesante della capacità rimanente.

### Complessità e Intuizione

L'algoritmo richiede tempo **$O(n \log n)$**, dominato dalla fase di ordinamento. L'intuizione dietro l'ottimalità è che, potendo frazionare gli oggetti, conviene sempre dare priorità a quelli che offrono il maggior guadagno per ogni singola unità di peso aggiunta, come se si scegliessero i segmenti con la pendenza maggiore in un grafico valore-peso.

Questa soluzione è utile anche come punto di partenza per approssimare la versione 0/1 del problema in tempi molto rapidi.

## Coin Problem

Il problema delle $n$ coppie di monete con vincolo di dipendenza può essere risolto efficacemente tramite **Programmazione Dinamica**, riducendolo a una variante del problema dello zaino (Knapsack).

Ecco le strategie principali per risolverlo:

### 1. Soluzione con Programmazione Dinamica

L'approccio ottimale consiste nel considerare ogni coppia $i$ come un set di scelte mutuamente esclusive. Per ogni coppia $i$, hai tre opzioni:

1. Non selezionare alcuna moneta (Peso 0, Valore 0).
2. Selezionare solo la prima moneta (Peso 1, Valore $c_{i,1}$).
3. Selezionare entrambe le monete (Peso 2, Valore $c_{i,1} + c_{i,2}$).

**Relazione di ricorrenza:** Sia $DP[i][j]$ il valore massimo ottenibile usando le prime $i$ coppie con esattamente $j$ monete selezionate: $$DP[i][j] = \max(DP[i-1][j], DP[i-1][j-1] + c_{i,1}, DP[i-1][j-2] + c_{i,1} + c_{i,2})$$

**Complessità:**

- **Tempo:** $O(n \cdot K)$, poiché dobbiamo riempire una tabella di dimensioni $n \times K$ e ogni cella richiede tempo costante.
- **Spazio:** $O(n \cdot K)$, ottimizzabile a $O(K)$ mantenendo solo la riga precedente della matrice.

### 2. Modellazione come cammino massimo su DAG

Il problema può essere visualizzato come la ricerca del **cammino massimo in un Grafo Diretto Aciclico (DAG)**.

- **Nodi:** Ogni stato è rappresentato da una coppia $(i, j)$, dove $i$ è l'indice della coppia di monete corrente e $j$ è il numero di monete accumulate.
- **Archi:** Da ogni nodo $(i, j)$ partono tre archi verso $(i+1, j)$, $(i+1, j+1)$ e $(i+1, j+2)$, con pesi corrispondenti al valore aggiunto dalla scelta.
- La soluzione è il peso del cammino più lungo dal nodo $(0, 0)$ al nodo $(n, K)$.

### 3. Approccio Greedy e versione frazionaria

Se il problema permettesse di selezionare frazioni di monete, la strategia ottimale sarebbe **Greedy**:

- Calcola il rapporto valore/peso per le due opzioni di ogni coppia: $R_1 = c_{i,1}/1$ e $R_2 = (c_{i,1} + c_{i,2})/2$.
- Ordina le opzioni per rapporto decrescente e seleziona fino a esaurire la capacità $K$.
- **Nota:** Questo approccio non garantisce l'ottimo nella versione intera (0/1), ma fornisce un'ottima base per approssimazioni rapide.
- $\Theta(n \log n)$ time

## Longest Increasing Sequence

Il problema della **Longest Increasing Subsequence (LIS)** consiste nel trovare la sottosequenza più lunga di una data sequenza di $n$ elementi in cui i valori appaiono in ordine strettamente crescente. A differenza di una sottostringa, gli elementi di una sottosequenza non devono necessariamente essere contigui nell'array originale, purché il loro ordine relativo sia preservato.

Ecco le principali strategie per risolvere questo problema:

### 1. Programmazione Dinamica ($O(n^2)$)

L'approccio standard scompone il problema in sottoproblemi basati sui prefissi della sequenza.

- **Definizione del sottoproblema**: $LIS(i)$ rappresenta la lunghezza della più lunga sottosequenza crescente che termina esattamente con l'elemento in posizione $i$.
- **Relazione di ricorrenza**: Per calcolare $LIS(i)$, si esaminano tutti gli elementi precedenti $j < i$. Se $A[j] < A[i]$, l'elemento $i$ può estendere la sottosequenza che terminava in $j$. La formula è: $LIS(i) = 1 + \max({LIS(j) \mid j < i \text{ e } A[j] < A[i]} \cup {0})$.
- **Risultato finale**: La soluzione globale è il valore massimo presente nella tabella delle $LIS(i)$ calcolate.

### 2. Modellazione tramite DAG ($O(n^2)$)

Il problema può essere ridotto alla ricerca del **cammino più lungo** in un Grafo Diretto Aciclico (DAG).

- Ogni elemento della sequenza corrisponde a un vertice del grafo.
- Viene creato un arco diretto dal vertice $i$ al vertice $j$ se e solo se $i < j$ e $A[i] < A[j]$.
- Ogni cammino in questo DAG corrisponde a una sottosequenza crescente; pertanto, il cammino con il maggior numero di nodi rappresenta la LIS.

### 3. Ottimizzazione con Ricerca Binaria ($O(n \log n)$)

Per gestire sequenze molto grandi, è possibile abbattere la complessità temporale a $O(n \log n)$ utilizzando il concetto di **posizioni dominanti**.

- **Intuizione**: Invece di confrontare ogni elemento con tutti i precedenti, si mantiene un array (o un BST) che memorizza il più piccolo valore finale possibile per ogni lunghezza di sottosequenza trovata finora.
- **Procedura**: Per ogni nuovo elemento della sequenza, si esegue una **ricerca binaria** (predecessor query) nell'array delle posizioni dominanti per trovare la sottosequenza più lunga che esso può estendere.
- **Aggiornamento**: Se l'elemento permette di ottenere una sottosequenza di lunghezza esistente con un valore finale più piccolo, si aggiorna la posizione dominante corrispondente; altrimenti, si crea una nuova lunghezza massima.

### 4. Applicazioni e Varianti

- **Teorema di Erdős–Szekeres**: Questo teorema sfrutta le tabelle LIS per dimostrare che ogni sequenza di $(m-1)(n-1)+1$ numeri distinti contiene una sottosequenza crescente di lunghezza $m$ o una decrescente di lunghezza $n$.

## Longest Bitonic Sequence

Il problema della **Longest Bitonic Subsequence (LBS)** consiste nel trovare la sottosequenza più lunga di una data sequenza $S$ che prima aumenta e poi diminuisce. Una sequenza è considerata bitonica se esiste un indice $k$ tale che gli elementi precedenti a $k$ siano in ordine crescente e quelli successivi in ordine decrescente.

### Strategia di Risoluzione

L'approccio più efficiente per risolvere questo problema sfrutta la programmazione dinamica e si basa sulla scomposizione della sequenza in due parti distinte: una crescente e una decrescente.

1. **Calcolo della LIS (Longest Increasing Subsequence):** Si scansiona l'array da sinistra a destra per calcolare, per ogni posizione $i$, la lunghezza della più lunga sottosequenza crescente che termina esattamente in quel punto.
2. **Calcolo della LDS (Longest Decreasing Subsequence):** Si esegue una scansione simile, ma procedendo da destra verso sinistra (oppure cercando la sottosequenza decrescente che inizia in $i$).
3. **Combinazione dei risultati:** Per ogni indice $i$, si sommano i valori di $LIS[i]$ e $LDS[i]$ e si sottrae 1. Il valore risultante rappresenta la lunghezza della più lunga sottosequenza bitonica che ha l'elemento $S[i]$ come "picco". Il decremento di 1 è necessario perché l'elemento centrale $S[i]$ viene conteggiato in entrambe le sottosequenze.

### Esempio Pratico

**LBS finale (LIS + LDS - 1)**

Data la sequenza $S = [2, -1, 4, 3, 5, -1, 3, 2]$, i calcoli procedono come segue:

| **S**   | **2** | **-1** | **4** | **3** | **5** | **-1** | **3** | **2** |
| ------- | ----- | ------ | ----- | ----- | ----- | ------ | ----- | ----- |
| **LIS** | 1     | 1      | 2     | 2     | 3     | 1      | 2     | 2     |
| **LDS** | 2     | 1      | 3     | 2     | 3     | 1      | 2     | 1     |
| **LBS** | 2     | 1      | 4     | 3     | 5     | 1      | 3     | 2     |
### Complessità

- **Temporale:** Utilizzando l'algoritmo ottimale per la LIS basato sulla ricerca binaria, il problema può essere risolto in **$O(n \log n)$**.
- **Spaziale:** È richiesto uno spazio **$O(n)$** per memorizzare gli array di supporto necessari ai calcoli della LIS e della LDS.

## Largest independent set on trees

![[Pasted image 20260206172136.png]]
# Greedy

## Activity Selection

L'**Activity Selection Problem** consiste nel selezionare il maggior numero possibile di attività compatibili che condividono una risorsa comune. Due attività sono considerate compatibili se i loro intervalli temporali non si sovrappongono.

La strategia ottimale per risolvere questo problema è di tipo **greedy**: si sceglie sempre l'attività disponibile che termina per prima, ovvero quella con il minor tempo di fine ($f_i$). Questa scelta è vincente perché lascia la risorsa libera il prima possibile, massimizzando lo spazio temporale rimanente per le altre attività.

A livello di prestazioni, se le attività sono già ordinate per tempo di fine, l'algoritmo impiega tempo lineare $\Theta(n)$; in caso contrario, il costo totale è dominato dall'ordinamento iniziale, risultando in $O(n \log n)$. Sebbene il problema presenti una sottostruttura ottimale che permetterebbe l'uso della programmazione dinamica, l'approccio greedy è preferibile perché molto più efficiente.

Per risolvere l'**Activity Selection Problem**, la strategia greedy si basa su un lemma fondamentale che giustifica la scelta locale dell'attività che termina per prima. Ecco il dettaglio del lemma e della sua dimostrazione basata su un argomento di scambio.

### Il Lemma della Scelta Greedy

**Lemma:** Considerato un qualsiasi sottoproblema non vuoto $S_k$, sia $a_m$ l'attività in $S_k$ con il tempo di fine più anticipato. Allora $a_m$ è inclusa in un qualche sottoinsieme di dimensione massima di attività mutualmente compatibili di $S_k$.

### La Dimostrazione (Argomento di Scambio)

La dimostrazione mostra che se esiste una soluzione ottima che non include l'attività che finisce per prima, possiamo trasformarla in una soluzione altrettanto valida che invece la include,.

1. **Ipotesi:** Sia $A_k$ un sottoinsieme massimo (una soluzione ottima) di attività compatibili in $S_k$. Supponiamo che $a_j$ sia l'attività in $A_k$ con il tempo di fine più anticipato.
2. **Caso 1 ($a_j = a_m$):** Se l'attività che finisce prima nella nostra soluzione ottima è proprio $a_m$, il lemma è già dimostrato.
3. **Caso 2 ($a_j \neq a_m$):** Se $a_j$ è diversa da $a_m$, costruiamo un nuovo insieme $A'_k$ sostituendo $a_j$ con $a_m$ ($A'_k = A_k \setminus {a_j} \cup {a_m}$).
4. **Verifica della compatibilità:** Poiché $a_m$ è l'attività che finisce prima in assoluto nel sottoproblema, il suo tempo di fine $f_m$ è minore o uguale al tempo di fine $f_j$ di $a_j$ ($f_m \le f_j$),. Dato che $A_k$ era un insieme compatibile e $a_j$ era la prima a finire, $a_m$ non può interferire con nessuna delle altre attività rimaste in $A_k \setminus {a_j}$,.
5. **Conclusione:** Poiché l'insieme $A'_k$ ha lo stesso numero di attività di $A_k$ ($|A'_k| = |A_k|$), esso è ancora una soluzione di dimensione massima, ma questa volta include $a_m$,.

### Ottimalità dell'Algoritmo (Per Induzione)

Sulla base di questo lemma, possiamo dimostrare per induzione che l'algoritmo greedy produce sempre una soluzione ottima:

- **Passo Induttivo:** Dopo aver scelto l'attività $a_1$ (quella che finisce prima), il lemma ci assicura che questa scelta è "sicura" e fa parte di almeno una soluzione ottima.
- **Riduzione:** Una volta effettuata la scelta, restiamo con un unico sottoproblema: trovare la soluzione ottima per le attività che iniziano dopo la fine di $a_1$,.
- **Conclusione:** Per l'ipotesi induttiva, l'algoritmo continuerà a fare scelte ottimali su sottoproblemi sempre più piccoli fino a completare la pianificazione massima,.

Questo approccio permette di risolvere il problema in tempo $\Theta(n)$ se le attività sono già ordinate per tempo di fine, o in $O(n \log n)$ se è necessario l'ordinamento iniziale.

## Job sequencing

Il **Job Sequencing Problem** consiste nel massimizzare il profitto totale eseguendo una serie di lavori, ognuno caratterizzato da una scadenza (deadline) e un guadagno associato. In questo modello, ogni lavoro richiede esattamente un'unità di tempo per essere completato.

### La Strategia Risolutiva

La soluzione ottimale si basa su un **approccio greedy**:

1. **Ordinamento**: Si ordinano i lavori in base al profitto in ordine decrescente.
2. **Assegnazione**: Si processano i lavori uno alla volta seguendo l'ordine stabilito.
3. **Scelta dello slot**: Per ogni lavoro, si cerca di occupare l'ultimo slot temporale disponibile che sia minore o uguale alla sua scadenza. Questa scelta è fondamentale perché "risparmia" gli slot temporali precedenti per lavori che potrebbero avere scadenze più imminenti.

### Implementazione Efficiente

Per evitare una ricerca lineare degli slot che porterebbe a una complessità quadratica, si può ottimizzare il processo utilizzando un **Binary Search Tree (BST)**:

- Si memorizzano nel BST tutti gli slot temporali ancora vuoti.
- Per ogni lavoro, si esegue una **query di predecessore** sulla sua deadline per trovare istantaneamente l'ultimo slot utile.
- Una volta occupato lo slot, lo si rimuove dal BST.
- If too empty slots, use a BST on intervals.

Questa strategia permette di risolvere il problema in **$O(n \log n)$**, dove $n$ è il numero di lavori. Se invece i lavori avessero durate diverse e tempi di inizio fissi, si passerebbe al problema del _Weighted Job Scheduling_, risolvibile con la programmazione dinamica.

## Magic Numbers

Il **Magic Numbers Problem** consiste nel determinare se un dato numero intero, rappresentato come una stringa di cifre, sia composto esclusivamente dalla concatenazione dei numeri `1`, `14` e `144`.

### 1. Definizione e Vincoli

Un numero è considerato "magico" solo se può essere interamente suddiviso nei tre blocchi permessi senza che avanzino cifre o vengano utilizzati altri numeri.

- **Esempi positivi**: `114`, `114144`, `14` sono tutti numeri magici perché formati solo dai blocchi validi.
- **Esempi negativi**: `1444` non è magico perché, dopo il blocco `144`, rimane un `4` che non può essere preceduto da un `1` per formare un nuovo blocco valido. Allo stesso modo, qualsiasi numero contenente cifre diverse da `1` o `4` viene immediatamente scartato.

### 2. Strategia Risolutiva: Approccio Greedy

Il problema può essere risolto in tempo lineare $O(n)$, dove $n$ è il numero di cifre della stringa, utilizzando una strategia **greedy**.

L'algoritmo procede analizzando la stringa da sinistra a destra:

1. Ad ogni posizione corrente, si tenta di trovare il match più lungo possibile tra i pattern disponibili, partendo dal più lungo (`144`), passando per quello intermedio (`14`) e arrivando al più corto (`1`).
2. Se viene trovato un match (ad esempio `144`), la posizione di lettura avanza di un numero di cifre pari alla lunghezza del blocco trovato.
3. Se in una determinata posizione non è possibile far corrispondere nessuno dei tre blocchi, si conclude immediatamente che il numero non è magico.
4. Se si riesce a raggiungere la fine della stringa consumando tutti i caratteri, il numero è dichiarato magico.

### 3. Perché funziona il match più lungo?

La scelta del match più lungo ad ogni passo (priorità a `144` rispetto a `14` o `1`) è fondamentale per minimizzare il numero di passaggi e garantire che le sequenze di `4` siano sempre correttamente precedute dalla cifra `1`. Poiché ogni blocco deve necessariamente iniziare con la cifra `1`, non c'è ambiguità: un `4` può esistere solo se fa parte di un `14` o un `144` già identificato.

L'algoritmo **Lempel-Ziv** (spesso associato a varianti come LZ77 o LZ78) è il capostipite di una famiglia di algoritmi di compressione "dizionari" che include formati moderni come lo **ZIP**. 

Ecco una spiegazione dettagliata del funzionamento basata sulla strategia **greedy**:

### 1. Logica di Funzionamento

A differenza della codifica di Huffman, che lavora sulla frequenza dei singoli simboli, Lempel-Ziv sfrutta le **ripetizioni di intere sequenze** all'interno del testo. La strategia procede analizzando il testo da sinistra a destra:

- In ogni posizione corrente, l'algoritmo cerca la **ripetizione più lunga** (chiamata "frase") che è già apparsa nella parte di testo precedente.
- Una volta identificata, la sequenza non viene riscritta: viene invece sostituita con un **riferimento all'indietro**.

### 2. Struttura del Riferimento

Ogni blocco compresso è solitamente composto da una coppia di valori:

- **Distanza**: quanto bisogna tornare indietro nel testo per trovare l'inizio della sequenza originale.
- **Lunghezza**: quanti caratteri devono essere copiati da quella posizione.

### 3. Efficienza della Strategia Greedy

L'uso della scelta locale ottimale (trovare sempre la corrispondenza più lunga possibile) garantisce matematicamente che il testo venga scomposto nel **minor numero possibile di frasi**. Questo approccio permette di sostituire lunghi segmenti di dati con pochi bit necessari a descrivere il puntatore, rendendolo estremamente efficace per file con molte ridondanze (come testi in linguaggio naturale o codici sorgente).

## Lexicographically Maximum Subsequence

Il problema della **Lexicographically Maximum Subsequence** consiste nel trovare, all'interno di una sequenza $S$, la sottosequenza che sia la più grande possibile secondo l'ordine lessicografico (alfabetico). In questo ordinamento, una stringa è considerata maggiore di un'altra se, al primo carattere in cui differiscono, presenta un simbolo che segue nell'ordine alfabetico, oppure se è più lunga pur condividendo lo stesso prefisso.

### Strategia Risolutiva

L'approccio ottimale per risolvere questo problema sfrutta una strategia **greedy** procedendo da **destra verso sinistra**:

1. Si scansiona la sequenza partendo dall'ultimo elemento e mantenendo traccia del carattere massimo incontrato finora.
2. Un simbolo viene incluso nella sottosequenza (posizionandolo all'inizio della soluzione corrente) se e solo se è maggiore o uguale al massimo attuale.
3. I simboli più piccoli del massimo corrente vengono scartati, poiché la loro inclusione renderebbe la sottosequenza lessicograficamente inferiore rispetto a una selezione che inizi con un carattere più grande situato alla loro sinistra.

### Analisi e Applicazioni

- **Complessità:** L'algoritmo richiede tempo lineare **$O(n)$**, poiché esamina ogni carattere una sola volta.
- **Connessioni:** Questa logica è concettualmente identica a quella utilizzata per calcolare la frontiera di Pareto (Pareto optimal curve) in un insieme di punti bidimensionali.

Una soluzione **Pareto ottima** si riferisce a un punto all'interno di un insieme di dati che non può essere migliorato in una dimensione senza sacrificare la qualità in un'altra dimensione. Questo concetto è fondamentale per definire la **frontiera di Pareto**, che rappresenta l'insieme di tutti i punti "ottimali" in quanto non sono dominati da nessun altro punto disponibile.

Ecco i dettagli tecnici basati sulle fonti:

- **Definizione di Dominanza:** Un punto $(x, y)$ domina un altro punto $(x', y')$ se è superiore in entrambi i parametri considerati, ad esempio se $x > x'$ e $y > y'$. Se un punto è dominato, significa che esiste un'altra soluzione che è migliore sotto ogni punto di vista.
- **Applicazioni nei Sistemi:** Questo modello è spesso utilizzato per analizzare il compromesso (trade-off) tra risorse diverse, come tempo e spazio. Una soluzione è considerata preferibile se riesce a essere contemporaneamente più veloce e meno esosa in termini di memoria rispetto alle alternative.
- **Strategia di Calcolo:** L'algoritmo per identificare la frontiera di Pareto è concettualmente identico a quello utilizzato per trovare la **Lexicographically Maximum Subsequence**.
- **Funzionamento dell'Algoritmo:**
    1. Si ordinano inizialmente i punti in base a una delle dimensioni (ad esempio l'asse $x$).
    2. Si esegue una scansione dei punti (spesso procedendo da destra verso sinistra o seguendo l'ordine stabilito) per identificare quali mantengono una posizione di superiorità rispetto alla seconda coordinata.
    3. I punti che risultano inferiori al massimo corrente incontrato durante la scansione vengono scartati, poiché sono dominati da soluzioni migliori.

## Wood Cutter

Il problema del **Wood Cutter** (Tagliaboschi) consiste nel massimizzare il numero di alberi abbattuti in una foresta, dato un insieme di $n$ alberi ciascuno con una posizione $x_i$ e un'altezza $h_i$.

### Regole e Vincoli

Ogni albero può essere abbattuto in due direzioni: verso sinistra (occupando lo spazio da $x_i - h_i$ a $x_i$) o verso destra (da $x_i$ a $x_i + h_i$). L'unica condizione è che l'albero caduto non deve colpire altri alberi, siano essi ancora in piedi o già abbattuti.

### Strategia Risolutiva (Greedy)

La soluzione ottimale si ottiene elaborando gli alberi in ordine da sinistra a destra con un approccio **greedy**:

1. **Priorità a sinistra**: Se il primo albero può cadere a sinistra, lo si abbatte sempre in quella direzione poiché non influenza la posizione di nessun altro albero successivo. Per gli alberi successivi, se lo spazio tra la posizione attuale $x_i$ e l'ingombro dell'ultimo albero abbattuto è sufficiente, si sceglie la caduta a sinistra.
2. **Tentativo a destra**: Se la caduta a sinistra è impedita, si controlla se l'albero può cadere a destra senza colpire la posizione $x_{i+1}$ dell'albero successivo. Se possibile, lo si abbatte a destra.
3. **Omissione**: Se l'albero non può cadere in nessuna delle due direzioni, viene lasciato in piedi per non ostacolare i vicini.

### Perché è efficace?

Questa strategia è vincente perché far cadere un albero a sinistra è un "guadagno pulito" che non restringe le opzioni future. Farlo cadere a destra, sebbene possa bloccare il successivo, garantisce comunque un'unità nel conteggio totale degli alberi abbattuti, pareggiando o migliorando qualsiasi altra scelta locale.

## Queue Problem

Il problema della coda (**Queue Problem**) consiste nel ricostruire l'ordine originale di $n$ persone in una fila partendo da due informazioni per ogni individuo: l'altezza ($H_i$) e il numero di persone più alte (o di pari altezza) che si trovavano davanti a lui nella coda originale ($A_i$).

Ecco la strategia risolutiva basata sulle fonti:
### 1. Strategia Greedy (Approccio Ottimale)

La chiave per risolvere il problema è elaborare le persone in **ordine di altezza decrescente**.

- **Ordinamento**: Si ordinano le persone dalla più alta alla più bassa. Se due persone hanno la stessa altezza, si ordinano in base al valore $A_i$ crescente.
- **Inserimento**: Si inserisce ogni persona in una nuova lista esattamente nella posizione indicata dal suo valore $A_i$.

**Perché funziona?** Quando inseriamo la persona $i$-esima (più bassa di tutte quelle già inserite), la sua posizione finale dipende solo dal numero di persone più alte già presenti nella fila. Poiché tutte le persone già inserite sono più alte di lei, il valore $A_i$ corrisponde esattamente all'indice della posizione in cui deve essere inserita.

### 2. Esempio Pratico

Se abbiamo persone con altezze e valori $A_i$ come `(7, 0), (7, 1), (6, 1), (5, 0)`:

1. Inseriamo `(7, 0)` in posizione 0: `[(7, 0)]`.
2. Inseriamo `(7, 1)` in posizione 1: `[(7, 0), (7, 1)]`.
3. Inseriamo `(6, 1)` in posizione 1: `[(7, 0), (6, 1), (7, 1)]`.
4. Inseriamo `(5, 0)` in posizione 0: `[(5, 0), (7, 0), (6, 1), (7, 1)]`.

### 3. Complessità

- **Tempo**: Utilizzando un semplice array o vettore, l'inserimento richiede lo spostamento degli elementi a destra, portando a una complessità **$O(n^2)$**.
- **Ottimizzazioni**: È possibile ridurre la complessità a **$O(n \log n)$** utilizzando strutture dati più avanzate come i **Segment Tree**, i **Fenwick Tree** o le **Skip List** per gestire gli inserimenti in modo efficiente.

Una **Skip List** è una struttura dati probabilistica che funge da alternativa agli alberi di ricerca bilanciati (come gli AVL) per implementare dizionari e risolvere il "predecessor problem".

### Struttura e Funzionamento

A differenza di una lista collegata standard dove la ricerca è lineare ($O(n)$), la Skip List utilizza una gerarchia di livelli:

- **Livello base:** Contiene tutti gli elementi ordinati.
- **Livelli superiori:** Includono sottoinsiemi di elementi scelti casualmente con una probabilità che decresce esponenzialmente ($1/2, 1/4, 1/8$, ecc.).
- **Ricerca:** L'algoritmo inizia dal livello più alto, saltando ampie porzioni di dati (come in un'autostrada), e scende ai livelli inferiori solo quando si avvicina al valore target.

#TODO FROM IPAD

### Efficienza e Complessità

- **Tempo:** Tutte le operazioni principali (ricerca, inserimento, cancellazione) richiedono tempo **$O(\log n)$** con alta probabilità.
- **Spazio:** L'occupazione di memoria è lineare, **$O(n)$**, poiché il numero totale di nodi su tutti i livelli è circa il doppio del numero di elementi nel livello base.

Questa struttura è particolarmente apprezzata per la sua semplicità di implementazione rispetto agli alberi bilanciati, pur mantenendo prestazioni simili.

## Boxes

Esistono diverse varianti del **problema delle scatole** (Boxes Problem) nella teoria degli algoritmi, solitamente incentrate sulla costruzione di torri o sull'incastro (nesting) di volumi.
### 1. Torre di Scatole (Peso e Durabilità)

In questa variante, hai $n$ scatole, ognuna con un peso $W_i$ e una durabilità $D_i$ (il carico massimo che può sopportare sopra di sé). L'obiettivo è costruire la torre più alta possibile.

- **Strategia Risolutiva**: Richiede una combinazione di approccio **greedy** e **programmazione dinamica**.
- **Ordinamento (Greedy)**: È fondamentale stabilire un ordine ottimale prima di applicare la DP. Le scatole devono essere ordinate in base alla somma di peso e durabilità ($W_i + D_i$).
- **DP**: Si definisce un sottoproblema che calcola il **peso minimo** di una torre di altezza $k$ utilizzando solo le prime $i$ scatole dell'ordinamento. Per ogni scatola, si decide se includerla (se il peso della torre sovrastante è $\le$ alla sua durabilità) o escluderla.
- **Complessità**: Il tempo di esecuzione è tipicamente quadratico, $O(n^2)$.

## Hero

Hero (Potyczki 2014) Bitor has H health points and he must defeat n (n ≤ 105) monsters. The i-th monster deals di damage, but after death it drops a potion that restores ai hp (hp can be above the initial value). Can Bitor choose the order of fights in such a way that his hp never drops below 0? Print "NO" or "YES" with the order of monsters.

Il problema **Hero** si risolve dividendo i mostri in due categorie e applicando un approccio **greedy** differenziato, basato sul principio della scelta locale ottimale.

### 1. Mostri con Guadagno Netto ($a_i \ge d_i$)

Per questa categoria, la strategia vincente consiste nell'ordinare i mostri per **danno $d_i$ crescente**. L'intuizione è che affrontare prima i nemici che infliggono meno danno permette di accumulare punti vita tramite le pozioni, aumentando il margine di sicurezza necessario per sconfiggere i mostri più forti in seguito.

### 2. Mostri con Perdita Netta ($a_i < d_i$)

Questa categoria è più sottile e richiede di ordinare i mostri per **valore della pozione $a_i$ decrescente**. Questa scelta può essere dimostrata tramite un **argomento di scambio** (exchange argument): se si affronta prima un mostro che rilascia una pozione più grande, si mantiene una riserva di punti vita superiore per assorbire il colpo del mostro successivo. Scambiare l'ordine di due mostri in questa lista non può migliorare la soluzione se non si rispetta l'ordine decrescente di $a_i$.

### Algoritmo Risolutivo

1. **Divisione**: Separa i mostri in due liste: `Vantaggiosi` ($a_i \ge d_i$) e `Svantaggiosi` ($a_i < d_i$).
2. **Ordinamento**:
    - Ordina `Vantaggiosi` per $d_i$ in ordine ascendente.
    - Ordina `Svantaggiosi` per $a_i$ in ordine discendente.
3. **Simulazione**: Esegui i combattimenti nell'ordine ottenuto (prima tutti i `Vantaggiosi`, poi gli `Svantaggiosi`).
    - Se in qualsiasi momento $H - d_i \le 0$, interrompi e stampa **"NO"**.
    - Se riesci a sconfiggere tutti i mostri, stampa **"YES"** seguito dall'ordine degli indici.

Questa strategia garantisce la correttezza in tempo $O(n \log n)$, dominato dalla fase di ordinamento.