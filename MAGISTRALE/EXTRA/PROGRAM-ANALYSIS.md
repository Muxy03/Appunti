Ecco un riassunto completo dei materiali del corso, strutturato per capitoli corrispondenti alle singole fonti, con le soluzioni agli esercizi inclusi.

### 1. Introduzione all'Analisi dei Programmi
L'analisi dei programmi è l'esame sistematico di un software per determinarne le proprietà, come la ricerca di bug, l'ottimizzazione o la sicurezza. Poiché non esiste un metodo automatico, universale ed esatto, l'analisi deve rinunciare a qualcosa: automazione (richiedendo intervento umano), universalità (limitandosi a certe classi di programmi) o esattezza (introducendo approssimazioni).

*   **Sovra-approssimazione:** Include stati non raggiungibili; utile per provare la correttezza (assenza di bug), ma può generare falsi positivi.
*   **Sotto-approssimazione:** Include solo stati raggiungibili; ottima per il bug-finding, poiché ogni errore trovato è reale (nessun falso positivo), ma può mancare alcuni bug (falsi negativi).

---

### 2. Semantica Denotazionale e Collezionista
La semantica assegna un significato matematico alla sintassi. La **Semantica Collezionista** caratterizza l'insieme di tutti gli stati di memoria raggiungibili durante l'esecuzione.

*   **Esercizio (Slide 22):** Dato $c \triangleq s := \text{nondet}[1..]; \text{while } s > 1 \text{ do } \{ x := 2x; s := s-1 \}$ e $P \triangleq \{x=1\}$.
    *   **Domanda:** Cos'è $[[c]]P$?
    *   **Soluzione:** $[[c]]P = \{s=1 \land \exists n \in \mathbb{N}. x = 2^n\}$. Il programma moltiplica $x$ per 2 un numero $s-1$ di volte. Partendo da $x=1$ e con $s \geq 1$, i risultati possibili sono potenze di 2.
    *   **Esempio sovra-approssimazione:** $\{s \leq x\}$ (copre tutti gli stati reali ma ne aggiunge altri).
    *   **Esempio sotto-approssimazione:** $\{s=1 \land x=256\}$ (è un sottoinsieme dei risultati reali).

---

### 3. Logica di Hoare (HL)
La logica di Hoare utilizza triple $\{P\} c \{Q\}$ per dimostrare la **correttezza parziale**: se il programma inizia in uno stato che soddisfa $P$ e termina, lo stato finale soddisferà $Q$.

*   **Azioma dell'Assegnamento:** $\{Q[a/x]\} x := a \{Q\}$.
*   **Esercizio (Slide 38):** $\{x > 0, y = 3x, z = x\} x := x + y \{?\}$.
    *   **Soluzione:** Usando l'assioma di Floyd in avanti: $\{\exists x'. (x' > 0 \land y = 3x' \land z = x') \land x = x' + y\}$. Semplificando, dato che $y=3x'$, allora $x = x' + 3x' = 4x'$, quindi $\{x > 0 \land x = 4z \land y = 3z\}$.

---

### 4. Correttezza Totale e Invarianti
La correttezza totale garantisce sia la correttezza parziale che la terminazione. Si usa un **variante** (una funzione che decresce a ogni ciclo e ha un limite inferiore) per provare che un ciclo termina.

*   **Esercizio (Slide 44):** Trovare il variante per l'algoritmo della divisione euclidea.
    *   **Soluzione:** Il variante è $t \triangleq r$. Poiché nel ciclo $r := r - y$ e sappiamo che $y > 0$, il valore di $r$ diminuisce strettamente rimanendo limitato inferiormente da 0 (condizione del ciclo $y \leq r$).

---

### 5. Logica di Incorrettezza (IL) - Draft
Introdotta da O'Hearn, usa triple $[P] c [Q]$ per la **sotto-approssimazione**. Se uno stato soddisfa $Q$, è garantito che sia raggiungibile da uno stato in $P$.

*   **Esercizio (Slide 51):** $[true] n := \text{nondet}(); x := 0; \text{while } (n > 0) \text{ do } \{ x := x + n; n := \text{nondet}(); \} [?]$.
    *   **Soluzione:** $[x \geq 0]$. Ogni valore di $x \geq 0$ è raggiungibile. Infatti, srotolando il ciclo, se $n$ viene scelto come $k$ al primo giro e poi $0$, otteniamo $x=k$ per qualsiasi $k > 0$. Il caso $x=0$ è dato saltando il ciclo.

---

### 6. La "Vera" Logica di Incorrettezza
La IL completa distingue tra terminazione normale (`ok`) ed errori (`er`).

*   **Regola dello Short-circuit:** Se un comando $c_1$ genera un errore, il comando successivo $c_2$ non viene eseguito: $\frac{[P]c_1[er:Q]}{[P]c_1; c_2[er:Q]}$.

---

### 7. Più su IL e Condizioni Necessarie (NC)
Viene introdotta la **Logica delle Condizioni Necessarie**, dove $(P) c (Q)$ significa che se partiamo fuori da $P$, non potremo mai finire in $Q$ (ovvero $P$ è necessario per $Q$).

---

### 8. Sufficient Incorrectness Logic (SIL)
SIL lavora all'indietro per trovare le condizioni iniziali sufficienti a causare un errore: $\langle P \rangle c \langle Q \rangle$.

*   **Validità:** Qualsiasi stato in $P$ può portare a uno stato di errore in $Q$.

---

### 9. Logica di Separazione (SL)
Estende la logica di Hoare per gestire i puntatori in modo locale. L'operatore principale è la **congiunzione separativa** ($P * Q$), che indica che $P$ e $Q$ valgono su porzioni di memoria disgiunte.

---

### 10. ISL e Separation SIL
Combinano la logica di incorrettezza con la logica di separazione per trovare bug di memoria (come use-after-free) senza falsi positivi.

*   **Azioma Local Load:** $[y \mapsto v] x := [y] [ok: x = v \land y \mapsto v]$.

---

### 11. Interpretazione Astratta: Intro
L'Interpretazione Astratta approssima la semantica collezionista sostituendo i valori reali con elementi di un **dominio astratto** (es. Segni, Intervalli, Poliedri).

---

### 12. Interpretazione Astratta: Matematica
Utilizza la teoria dei punti fissi. L'analisi di un ciclo corrisponde al calcolo di un punto fisso sulle equazioni del grafo di controllo di flusso (CFG).

*   **Esercizio (Slide 176):** Calcolare gli invarianti di segno per un fattoriale.
    *   **Soluzione:** Partendo da $n > 0$, al punto (6) finale avremo $m \in \mathbb{Z}_{>0}$. Durante il ciclo, $m$ inizia a 1 ($\mathbb{Z}_{>0}$) e viene moltiplicato per $n$, che nel ciclo è sempre $>0$. Il prodotto di due positivi è positivo, quindi l'invariante $m > 0$ si mantiene.

---

### 13. Teoria degli Ordini e Connessioni di Galois
Le connessioni di Galois formalizzano il legame tra dominio concreto ($C$) e astratto ($A$) tramite le funzioni $\alpha$ (astrazione) e $\gamma$ (concretizzazione).

---

### 14. Domini Astratti Numerici
Esistono vari domini con diverso equilibrio tra precisione e complessità: Segni, Costanti, Intervalli, Congruenze, Zone, Ottagoni, Poliedri.

*   **Esercizio (Slide 207):** Dominio Pirahã (1, 2, molte).
    *   **Soluzione:** L'operazione $+^{\#}$ è definita come: $1+^{\#}1=2$, $1+^{\#}2=\top$ (molte), $2+^{\#}2=\top$. È BCA (Best Correct Approximation) perché riflette esattamente la somma concreta finché non supera il limite del dominio.

---

### 15. Analisi Astratta e Precisione
La precisione dipende da come è scritto il programma (natura intensionale dell'analisi). Due programmi equivalenti possono avere risultati astratti diversi.

---

### 16. Local Completeness Logic (LCL)
LCL è un sistema di prova che combina sovra e sotto-approssimazioni, garantendo che se non vengono trovati alert, il programma è corretto (relativamente al dominio astratto scelto).

---

### 17-18. Control Flow Analysis (CFA)
La CFA è necessaria per linguaggi con funzioni di ordine superiore (dove il chiamante non è noto staticamente). La **0-CFA** è un'analisi basata su vincoli che approssima quali funzioni possono fluire verso quali variabili.

*   **Esercizio 1 (Slide 254):** $((fn \ x \Rightarrow (x + 1)^1 )^2 \ (3)^3 )^4$.
    *   **Soluzione:** Le etichette identificano i punti del programma. In 0-CFA, i dati (costanti come 3) non fluiscono, fluiscono solo le funzioni. Quindi $\hat{C}(2) = \{fn \ x \Rightarrow \dots\}$, mentre $\hat{C}(1) = \emptyset$ (risultato della somma, non tracciato).

Ti piacerebbe approfondire il calcolo di un punto fisso con un esempio pratico o preferisci esplorare come queste logiche vengono usate nei tool industriali come Facebook Infer?
