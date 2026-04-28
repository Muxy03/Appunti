Ecco un riassunto completo degli argomenti trattati nelle fonti fornite, organizzato per capitoli corrispondenti ai file PDF selezionati.

### 1-Presentation.pdf: Obiettivi e Struttura del Corso
Il corso esplora i concetti fondamentali del calcolo parallelo e le architetture dei sistemi (memoria condivisa, distribuita e GPGPU). L'obiettivo è padroneggiare la programmazione parallela strutturata utilizzando C++ moderno, OpenMP, FastFlow e MPI. L'esame prevede un progetto (modulare o singolo) e una prova orale incentrata sulla teoria e sulla discussione del codice.

### 2-Intro.pdf: Perché il Calcolo Parallelo?
Il calcolo parallelo serve a risolvere problemi più velocemente o a gestire problemi di dimensioni maggiori. La Legge di Moore e il superamento del "Free Lunch" (fine dell'aumento automatico delle prestazioni sequenziali) hanno reso necessaria la gestione software di prestazioni, efficienza energetica e scalabilità.

### 3-MMexample-LeisersonMIT.pdf: Caso di Studio Moltiplicazione di Matrici
Le prestazioni possono essere migliorate drasticamente tramite ottimizzazioni del codice. Si passa da un'implementazione "naïve" a tecniche di **tiling** (suddivisione in blocchi) per sfruttare la cache e a algoritmi **Divide and Conquer** (ricorsivi) che espongono un parallelismo naturale.

**Esercizio: Ottimizzazione Moltiplicazione Matrici**
*   **Domanda:** Perché l'approccio ricorsivo (Divide and Conquer) è vantaggioso rispetto ai cicli for nidificati?
*   **Soluzione:** L'approccio ricorsivo permette di suddividere il problema in 8 moltiplicazioni di sottomatrici più piccole. Questo massimizza l'uso della cache (data locality) perché le sottomatrici finiscono per risiedere interamente nei livelli più veloci della memoria, riducendo i trasferimenti lenti dalla RAM principale. Inoltre, le chiamate ricorsive possono essere eseguite in parallelo (es. `cilk_spawn`).

### 4-Classification.pdf: Classificazione delle Architetture
Le architetture parallele si differenziano per l'organizzazione della memoria e l'interconnessione.
*   **Tassonomia di Flynn:** Classifica i sistemi in SISD, SIMD (vettoriali), e MIMD (multicore/cluster).
*   **SHM vs DM:** I sistemi a memoria condivisa (Shared Memory) permettono a tutti i processori di accedere a uno spazio di indirizzamento comune, mentre i sistemi a memoria distribuita (Distributed Memory) richiedono il passaggio di messaggi tra i nodi.

### 6-Shared-Memory.pdf: Sistemi a Memoria Condivisa
Il collo di bottiglia di **von Neumann** è il divario crescente tra la velocità della CPU e la larghezza di banda della memoria.
*   **Cache:** Fondamentali per mitigare il divario, ma introducono problemi di coerenza.
*   **False Sharing:** Problema di prestazioni dove thread su core diversi aggiornano variabili diverse che risiedono nella stessa linea di cache, forzando inutili invalidazioni.

### 7-SIMD-on-CPU.pdf e 7-SIMT-on-GPU.pdf: SIMD e SIMT
*   **SIMD (Single Instruction, Multiple Data):** Utilizza istruzioni vettoriali sulla CPU per operare su più dati contemporaneamente.
*   **SIMT (Single Instruction, Multiple Threads):** Modello tipico delle GPU (CUDA), dove migliaia di thread eseguono lo stesso codice su dati diversi, mascherando la latenza di memoria con il multithreading massivo.

### 8-Metrics_and_Laws.pdf: Metriche di Prestazione e Leggi
Il successo della parallelizzazione è misurato dallo **Speedup** e dall'**Efficienza**.
*   **Legge di Amdahl:** Il limite massimo dello speedup è dettato dalla frazione sequenziale del codice ($f$).

**Esercizio: Calcolo Speedup Teorico**
*   **Domanda:** Se il 95% di un programma è parallelizzabile, qual è lo speedup massimo su 6 processori?
*   **Soluzione:** Applicando la Legge di Amdahl: $Speedup = \frac{1}{0.05 + (0.95 / 6)} \approx 4.8$. Anche con processori infiniti, lo speedup non supererebbe mai $1/0.05 = 20$.

### 9-TypesOfParallelism.pdf: Tipi di Parallelismo
Esistono diverse forme di parallelismo basate su come vengono gestiti i dati e i compiti:
*   **Data Parallelism:** Stessa operazione applicata a una collezione di dati (Map, Reduce, Scan).
*   **Stream Parallelism:** Una sequenza di dati (stream) attraversa una serie di stadi (Pipeline).
*   **Task Parallelism:** Compiti diversi eseguiti simultaneamente.

### 10-C++Essentials.pdf: Fondamenti di C++ per SPM
Il corso assume la conoscenza di C++20. Elementi chiave includono la deduzione dei tipi (`auto`), la gestione delle risorse tramite **RAII**, le semantiche di movimento (**Move semantics**) e l'uso intensivo della **STL** e degli algoritmi standard paralleli.

### 12-WorkloadBalancing.pdf: Bilanciamento del Carico
La distribuzione dei compiti tra i lavoratori (Workers) deve essere equilibrata per evitare colli di bottiglia.

**Esercizio: Insieme di Mandelbrot**
*   **Domanda:** Cosa accade se calcoliamo l'insieme di Mandelbrot dividendo i pixel staticamente tra 3 thread?
*   **Soluzione:** Il carico risulterebbe sbilanciato. Le aree nere dell'insieme di Mandelbrot richiedono molte più iterazioni rispetto alle aree esterne. Un thread che riceve una porzione "nera" lavorerà molto più a lungo degli altri, portando a una bassa efficienza complessiva.

### 13-ModelsOfComputation.pdf: Modelli di Calcolo
Il modello **BSP (Bulk Synchronous Parallel)** struttura l'algoritmo in superstep composti da calcolo locale, comunicazione e barriera di sincronizzazione.

### 16-OpenMP1.pdf: Introduzione a OpenMP
OpenMP è un'API basata su direttive (`#pragma omp`) per il parallelismo a memoria condivisa in C/C++. Permette di parallelizzare cicli facilmente e gestire riduzioni in modo sicuro.

**Esercizio: Stima di $\pi$ con OpenMP**
*   **Domanda:** Come si può approssimare $\pi$ integrando la funzione $f(x) = 4/(1+x^2)$ in $$?
*   **Soluzione:** Si suddivide l'intervallo $$ in $N$ rettangoli. Ogni thread calcola la somma delle aree di un sottoinsieme di rettangoli. Infine, si usa una clausola `reduction(+:sum)` per sommare i risultati parziali in modo thread-safe.

### FastFlow3-Intro.pdf: FastFlow e Pattern Paralleli
FastFlow è una libreria C++ che fornisce **Algorithmic Skeletons** (Pipeline, Farm) come blocchi predefiniti per costruire applicazioni parallele efficienti. È lo strumento principale per il progetto d'esame.

### Structured-Parallel-Programming-Chapter2.pdf: Teoria delle Prestazioni
Introduce concetti come le dipendenze dai dati, il grafo delle attività e il **Brent's Lemma**, che fornisce una stima del tempo di esecuzione parallela basata sul lavoro totale ($T_1$) e il percorso critico ($T_\infty$).

### notes2024spm-Danelutto.pdf: Esempi Concettuali
Include analogie come la traduzione di un libro: dividere il libro in pagine tra più traduttori riduce il tempo totale ($T_{seq} = m \times t_{page}$ diventa $T_{par} \approx \frac{m}{n} \times t_{page}$), ma introduce il costo del coordinamento.

---

### Formulario e Legenda

| Formula | Descrizione | Legenda |
| :--- | :--- | :--- |
| $S_p = \frac{T_1}{T_p}$ | **Speedup**: Misura di quanto il programma è più veloce con $p$ processori. | $T_1$: Tempo sequenziale; $T_p$: Tempo con $p$ processori. |
| $E_p = \frac{S_p}{p}$ | **Efficienza**: Frazione di utilizzo dei processori. | $p$: Numero di processori. |
| $S_p = \frac{1}{f + \frac{1-f}{p}}$ | **Legge di Amdahl**: Limite dello speedup basato sulla parte sequenziale. | $f$: Frazione di codice non parallelizzabile ($0 \leq f \leq 1$). |
| $T_{step} = w + hg + l$ | **Costo Superstep BSP**: Tempo totale di un passo di calcolo e comunicazione. | $w$: Lavoro locale; $h$: Dati scambiati; $g$: Costo unitario comm.; $l$: Latenza/Sincronizzazione. |
| $C = R \cdot L$ | **Legge di Little**: Relazione tra concorrenza, throughput e latenza. | $C$: Concorrenza; $R$: Throughput (rate); $L$: Latenza. |
| $\gamma = \alpha / \beta$ | **Rapporto Calcolo/Comm.**: Misura il bilanciamento tra lavoro e overhead. | $\alpha$: Peso del calcolo; $\beta$: Peso della comunicazione. |

Ti servono approfondimenti su un particolare esercizio o un capitolo specifico?
