# Compilation Techniques (0073A) — Formal Review Handout
**Corso di Laurea — University of Pisa**  
**Teachers:** Andrea Corradini (andrea.corradini@unipi.it), Roberta Gori (roberta.gori@unipi.it)  
**Textbooks:** K. Cooper & L. Torczon, *Engineering a Compiler* (EaC); Hopcroft, Motwani & Ullman, *Introduction to Automata Theory, Languages, and Computation*.
> **Nota sui riferimenti:** le citazioni del tipo `[file.pdf, Slide N]` sono indicative (la numerazione può variare tra le versioni del materiale); in caso di discordanza fa fede l'argomento/sezione citata.

---

## Table of Contents
1. [Capitolo 1 — Introduzione e Architettura dei Compilatori](#cap1) — *IntroMio.pdf*
2. [Capitolo 2 — Fondamenti Formali dei Linguaggi e Automi](#cap2) — *LinguaggiI.pdf*
3. [Capitolo 3 — Analisi Lessicale (Lexing)](#cap3) — *Lexer.pdf*
4. [Capitolo 4 — Parsing Top-Down e Parser LL(1)](#cap4) — *ParsingMio.pdf / TableConstruction.pdf*
5. [Capitolo 5 — Parsing Bottom-Up e Tabelle LR(1)](#cap5) — *Bottom_up_Parsing.pdf / TableConstruction.pdf*
6. [Capitolo 6 — Analisi Semantica e Sintassi Yacc](#cap6) — *ContextsensitiveAnalysisv.pdf*
7. [Capitolo 7 — Ottimizzazione del Codice (Middle-End)](#cap7) — *OptimizationI.pdf*
8. [Capitolo 8 — Il Framework Dataflow](#cap8) — *Data-FlowFirst.pdf / Data-Flow2.pdf*
9. [Capitolo 9 — Astrazione delle Procedure e Gestione della Memoria](#cap9) — *TheProcedureAbstraction.pdf*
10. [Capitolo 10 — Generazione del Codice (Instruction Selection & Scheduling)](#cap10) — *IntroCodeGeneration.pdf*
11. [Capitolo 11 — Allocazione dei Registri](#cap11) — *RegisterAlloc1.pdf / RegisterAlloc2.pdf*
12. [Capitolo 12 — Monografia rustc (L'Architettura del Compilatore Rust)](#cap12) — *COMP-01...06-RUST_COMPILATION.pdf* (consolidated)
13. [Appendice — Esperienze di Laboratorio e Toolchain](#appendice) — *Laboratory Materials*

---

## Indice degli Esempi Svolti

| Argomento | Sezione |
|---|---|
| Derivazione `x + 2 - y`; SheepNoise; grammatica Goal/Expr | §1.3 |
| Determinizzazione NFA→DFA (almeno due 1) | §2.5 |
| Minimizzazione DISTINCT su $(a\|b)^+$ | §2.7 |
| PDA per $xcx^R$, traccia di `abcba` | §2.9 |
| Non-CF: $a^n b^n c^n$ | §2.10 |
| Registri generici + tighter $r_0$–$r_{31}$ (tabelle δ e α) | §3.4 |
| Dangling-else e grammatica di disambiguazione | §4.1 |
| Espressioni classiche: FIRST/FOLLOW/tabella LL(1) | §4.5 |
| Grammatica begin-end — **TODO** | §4.4 |
| Grammatica con nullificabili S→AB — **TODO** | fine Cap. 4 |
| Shift-reduce `x − 2 * y` | §5.4 |
| SheepNoise: `baa`, `baa baa` | §5.4 |
| Grammatica bcfa — **TODO** | §5.4 |
| Grammatica attribuita `-101`; grammatica circolare | §6.2 |
| Liveness: 3 sweep backward | §8.5 |
| Reaching Definitions: fattoriale fino al fixpoint | §8.6 |
| LVN con value numbers; edge case del naming | §7.2 |
| MAXLIVE e spill con 3 registri | §11.2 |
| Coloring $k{=}3$; optimistic coloring $k{=}2$ | §11.3 |
| MIR del condizionale `let z = if …` | §12.3 |
| Dangling reference; move path; closure capture | §12.5 |
| uHaskell / Algorithm W | §12.7 |

---

<a id="cap1"></a>
## CAPITOLO 1: Introduzione e Architettura dei Compilatori
**Source:** *IntroMio.pdf*

### 1.1 Definizioni Formali e Concetti Fondamentali
*   **Definizione di Compilatore (Compiler):** Un compilatore è un programma che accetta in input un altro programma (il *programma sorgente*) scritto in un linguaggio ad alto livello e lo traduce in un programma equivalente scritto in un linguaggio target, in genere il linguaggio macchina/instruction set di un'architettura hardware target [IntroMio.pdf, Slide 16, 60]. Il compilatore può anche tradurre verso un altro linguaggio ad alto livello (in tal caso si parla di *source-to-source translators*) [IntroMio.pdf, Slide 61]. Più informalmente, "un programma che prende altri programmi e li prepara per l'esecuzione" [IntroMio.pdf, Slide 16, 60].
*   **Definizione di Interprete (Interpreter):** Un interprete è un traduttore che, a differenza del compilatore, accetta in input il programma sorgente e i relativi dati di input, e lo traduce ed esegue linea per riga, direttamente a runtime, senza produrre un file eseguibile separato [IntroMio.pdf, Slide 18, 63].
*   **Differenze operative (Compilatori vs Interpreti):**
    *   **Tempistiche della traduzione:** Nel compilatore la traduzione avviene una sola volta, interamente, *prima* dell'esecuzione. Nell'interprete la traduzione avviene *durante* l'esecuzione, a runtime [IntroMio.pdf, Slide 62, 63].
    *   **Generazione dell'eseguibile:** Il compilatore genera un file eseguibile binario autonomo e indipendente; l'interprete non produce alcun file eseguibile separato [IntroMio.pdf, Slide 62, 63].
    *   **Velocità di esecuzione:** L'esecuzione del codice compilato è tipicamente molto più veloce rispetto all'esecuzione interpretata [IntroMio.pdf, Slide 62, 63].
    *   **Gestione e visualizzazione degli errori:** Il compilatore rileva e mostra tutti gli errori lessicali e sintattici solo al termine della compilazione, in blocco. L'interprete rileva l'errore a runtime nel momento esatto in cui incontra la riga errata, interrompendo immediatamente l'esecuzione del programma [IntroMio.pdf, Slide 62, 63].
*   **Proprietà dell'implementazione:** È importante notare che l'essere compilato o interpretato non è una proprietà intrinseca del linguaggio di programmazione, bensì della sua specifica *implementazione* [IntroMio.pdf, Slide 65].
    *   Linguaggi come *C* e *C++* sono tipicamente compilati [IntroMio.pdf, Slide 64].
    *   *Scheme* è tipicamente interpretato [IntroMio.pdf, Slide 64].
    *   *Python* è tipicamente interpretato, ma la sua implementazione standard (CPython) prima compila il codice sorgente in bytecode e poi lo interpreta tramite una macchina virtuale. Altre implementazioni, come PyPy, usano la compilazione Just-In-Time (JIT), mentre Cython o Nuitka traducono il codice Python direttamente in codice C compilato [IntroMio.pdf, Slide 64].
    *   *Java* adotta un approccio ibrido: il compilatore `javac` compila il codice sorgente in un formato indipendente dall'hardware detto *bytecode* [IntroMio.pdf, Slide 65]. Successivamente, la Java Virtual Machine (JVM) può interpretare il bytecode oppure, per ottimizzare le performance a runtime, compilarlo in codice macchina nativo usando un compilatore Just-In-Time (JIT) [IntroMio.pdf, Slide 65].
*   **AOT (Ahead-Of-Time) vs JIT (Just-In-Time):**
    *   **AOT (Ahead-Of-Time):** La traduzione del sorgente in codice macchina avviene interamente in anticipo rispetto al runtime. Produce un eseguibile standalone, ha un tempo di startup estremamente rapido, performance prevedibili e non introduce alcun overhead di compilazione durante l'esecuzione [IntroMio.pdf, Slide 65, 66].
    *   **JIT (Just-In-Time):** La compilazione avviene dinamicamente durante l'esecuzione del programma. Il codice parte inizialmente interpretato (o parzialmente compilato) e le porzioni di codice eseguite più frequentemente ("hot spots") vengono identificate e compilate a runtime in codice macchina nativo altamente ottimizzato. Ha uno startup più lento dovuto all'overhead di compilazione a runtime, ma può raggiungere performance elevate adattandosi dinamicamente al comportamento reale del programma [IntroMio.pdf, Slide 66, 67].
*   **I due principi fondamentali della compilazione:**
    1.  Il compilatore **deve preservare rigorosamente il significato** del programma sorgente originale (la correttezza semantica è un vincolo assoluto) [IntroMio.pdf, Slide 20, 71].
    2.  Il compilatore **deve migliorare** l'efficacia del programma di input secondo metriche prestabilite (velocità, spazio di memoria, consumo energetico) [IntroMio.pdf, Slide 20, 71].

### 1.2 Architettura del Compilatore e Rappresentazioni Intermedie
*   **Compilatore a due passate (Two-pass compiler):**
    $$\text{Source Code} \rightarrow \text{Front End} \xrightarrow{\text{IR}} \text{Back End} \rightarrow \text{Machine Code}$$
    *   Il **Front-End** si occupa di analizzare il codice sorgente, verificarne la legalità sintattica e semantica e mapparlo in una rappresentazione intermedia (IR) [IntroMio.pdf, Slide 21, 72]. Ha una complessità computazionale pari a $O(n)$ o $O(n \log n)$ [IntroMio.pdf, Slide 21, 72].
    *   Il **Back-End** accetta l'IR e la mappa nel codice macchina target [IntroMio.pdf, Slide 21, 72]. Poiché deve risolvere problemi di ottimizzazione ottimali (Instruction Selection, Instruction Scheduling, Register Allocation), la sua complessità computazionale è intrinsecamente NP-Completa [IntroMio.pdf, Slide 21, 72].
*   **Separazione degli interessi (Separation of concerns):** Questo principio di ingegneria del software garantisce che il Front-End dipenda unicamente dal linguaggio sorgente, mentre il Back-End dipenda unicamente dall'architettura hardware target [IntroMio.pdf, Slide 72, 73].
*   **L'argomento matematico $m \times n$:** Se vogliamo supportare $m$ linguaggi sorgente su $n$ architetture target distinte:
    *   Con un design monolitico a passata singola, avremmo bisogno di sviluppare $m \cdot n$ compilatori completi [IntroMio.pdf, Slide 22].
    *   Con un'architettura a due passate basata su un'unica IR condivisa, sono necessari solo $m$ Front-End e $n$ Back-End (ovvero $m+n$ componenti totali). Qualsiasi ottimizzatore scritto per l'IR lavorerà per tutte le $m \times n$ combinazioni [IntroMio.pdf, Slide 22].
*   **Compilatore tradizionale a tre parti (Three-part compiler):** Inserisce una terza macro-componente tra il Front-End e il Back-End: l'**Ottimizzatore (Middle-End)** [IntroMio.pdf, Slide 23, 73].
    $$\text{Source Code} \rightarrow \text{Front End} \xrightarrow{\text{IR}} \text{Optimizer} \xrightarrow{\text{IR}} \text{Back End} \rightarrow \text{Machine Code}$$
    L'ottimizzatore analizza l'IR e la trasforma in una versione semanticamente equivalente ma più efficiente (riducendo i tempi di esecuzione, lo spazio occupato o l'energia consumata) [IntroMio.pdf, Slide 73, 74]. L'ottimizzazione è strutturata come una sequenza di *passate (passes)* indipendenti [IntroMio.pdf, Slide 23, 74].
*   **Tipi di Rappresentazione Intermedia (IR):**
    *   **Strutturali (Grafiche):** Mantengono la struttura gerarchica del programma. L'esempio principale è l'**Abstract Syntax Tree (AST)** [ContextsensitiveAnalysisv.pdf, Slide 34]. Sono molto usate nei traduttori source-to-source ma tendono a occupare molto spazio in memoria [ContextsensitiveAnalysisv.pdf, Slide 34].
    *   **Lineari:** Rappresentano il programma come una sequenza di istruzioni per una macchina astratta, eseguite nell'ordine di apparizione [ContextsensitiveAnalysisv.pdf, Slide 34, 35]. Un esempio tipico è il codice a tre indirizzi (Three-Address Code) come l'**ILOC** [ContextsensitiveAnalysisv.pdf, Slide 34, 35].
    *   **Ibride:** Combinano elementi grafici (come il Control Flow Graph) e codice lineare all'interno dei singoli nodi del grafo [ContextsensitiveAnalysisv.pdf, Slide 34].
*   **Confronto: Parse Tree vs Abstract Syntax Tree (AST):** Il *Parse Tree* rappresenta l'intera sequenza di derivazioni grammaticali, includendo ogni simbolo non-terminale della grammatica. L'*Abstract Syntax Tree (AST)* conserva la struttura essenziale del programma eliminando i non-terminali e i dettagli sintattici superflui, risultando estremamente più compatto ed efficiente da elaborare [IntroMio.pdf, Slide 79; ContextsensitiveAnalysisv.pdf, Slide 34].
*   **Confronto: Stack-Machine Code vs Three-Address Code:**
    *   Il codice per macchine a stack esegue le operazioni basandosi unicamente su push e pop sulla pila (es. `push 2`, `push b`, `multiply`) [ContextsensitiveAnalysisv.pdf, Slide 34].
    *   Il codice a tre indirizzi (Three-Address Code) usa espressioni con al massimo tre operandi nella forma `t3 <- t1 op t2`, permettendo al compilatore di assegnare un nome esplicito (un registro virtuale) al risultato di ogni singola operazione e di conservarlo per riusi successivi [ContextsensitiveAnalysisv.pdf, Slide 34; IntroCodeGeneration.pdf, Slide 53].

### 1.3 Grammatiche d'Esempio e Derivazioni
*   **SheepNoise (BNF, slide):**
    ```
    SheepNoise → SheepNoise baa
               | baa
    ```
    La grammatica "giocattolo" del corso: definisce l'insieme dei belati di una pecora e sarà usata per il parsing LR (Cap. 5).
*   **Grammatica per espressioni semplici (slide):**
    ```
    S = { Goal }                1. Goal → Expr
    T = { number, id, +, - }    2. Expr  → Expr Op Term
    N = { Goal, Expr,           3.        | Term
          Term, Op }            4. Term  → number
    P = {1, …, 7}               5.        | id
                                6. Op    → +
                                7.        | -
    ```
*   **Derivazione di `x + 2 - y` (slide):**

| Produzione | Risultato          |
| ---------- | ------------------ |
| —          | `Goal`             |
| 1          | `Expr`             |
| 2          | `Expr Op Term`     |
| 5          | `Expr Op y`        |
| 7          | `Expr - y`         |
| 2          | `Expr Op Term - y` |
| 4          | `Expr Op 2 - y`    |
| 6          | `Expr + 2 - y`     |
| 3          | `Term + 2 - y`     |
| 5          | `x + 2 - y`        |

Per *riconoscere* una frase si ripercorre il processo all'indietro costruendo il **parse tree**; i compilatori usano di norma l'**AST** (privo di non-terminali), molto più compatto, come IR.

### 1.4 Esempi di Performance dell'Astrazione
*   **Caso di studio (gcc 4.1 con ottimizzazione -O3 su un array 10000×10000):** Mostra come la scelta del pattern di scrittura influenzi drasticamente i tempi di esecuzione a causa della cache e dell'efficacia delle passate di ottimizzazione del compilatore [IntroMio.pdf, Slide 24, 70, 71]:
    *   *Row-major traversal (scansione per righe):* `for(i) for(j) A[i][j]=0` $\rightarrow$ **0.51 s** (ottimale grazie al principio di località spaziale) [IntroMio.pdf, Slide 24, 71].
    *   *Column-major traversal (scansione per colonne):* `for(i) for(j) A[j][i]=0` $\rightarrow$ **1.65 s** (circa 3 volte più lento a causa dei continui cache misses) [IntroMio.pdf, Slide 24, 71].
    *   *Pointer form:* `*p++ = 0` $\rightarrow$ **0.11 s** (la forma più veloce ed esplicita sul target) [IntroMio.pdf, Slide 24, 71].
    *   *Standard library:* `bzero(...)` $\rightarrow$ **0.52 s** [IntroMio.pdf, Slide 24, 71].
    Un compilatore ideale dovrebbe conoscere intimamente questi trade-off hardware e generare sempre il codice migliore indipendentemente dalla forma scelta dal programmatore; all'atto pratico, pochissimi compilatori reali ci riescono [IntroMio.pdf, Slide 24, 71].


<a id="cap2"></a>
## CAPITOLO 2: Fondamenti Formali dei Linguaggi e Automi
**Source:** *LinguaggiI.pdf*

### 2.1 Alfabeti, Stringhe e Operazioni Formali
*   **Definizione di Alfabeto (Alphabet):** Un alfabeto $\Sigma$ è un insieme finito e non vuoto di simboli [LinguaggiI.pdf, Slide 8, 87].
    *   *Esempi:* $\Sigma_1 = \{a, b, c, \dots, z\}$ (lettere dell'alfabeto); $\Sigma_2 = \{0, 1\}$ (cifre binarie); $\Sigma_3 = \{(, )\}$ (parentesi tonde) [LinguaggiI.pdf, Slide 8, 87].
*   **Definizione di Stringa (String):** Una stringa su un alfabeto $\Sigma$ è una sequenza finita di simboli appartenenti a $\Sigma$ [LinguaggiI.pdf, Slide 8, 87]. La *stringa vuota*, indicata con $\epsilon$, è la stringa priva di simboli [LinguaggiI.pdf, Slide 8, 88].
*   **Lunghezza di una stringa $|x|$:** Corrisponde al numero di simboli che compongono la stringa $x$ [LinguaggiI.pdf, Slide 8, 88].
    *   *Esempi:* $|abfbz| = 5$; $|110010| = 6$; $|\epsilon| = 0$ [LinguaggiI.pdf, Slide 8, 88].
*   **Concatenazione di stringhe:** L'operazione che unisce due stringhe $x$ e $y$ accostandole per formare la stringa $xy$ [LinguaggiI.pdf, Slide 88]. È un'operazione associativa che ammette la stringa vuota $\epsilon$ come elemento neutro ($x\epsilon = \epsilon x = x$) [LinguaggiI.pdf, Slide 88].
*   **Sottostringa, Prefisso e Suffisso:** Una stringa $s$ è una sottostringa di $x$ se esistono due stringhe $y$ e $z$ tali che $x = ysz$ [LinguaggiI.pdf, Slide 88].
    *   Se $y = \epsilon$, allora $s$ è un **prefisso** di $x$ [LinguaggiI.pdf, Slide 88].
    *   Se $z = \epsilon$, allora $s$ è un **suffisso** di $x$ [LinguaggiI.pdf, Slide 88].
    *   $\epsilon$ è sia prefisso sia suffisso di qualsiasi stringa [LinguaggiI.pdf, Slide 89]. I prefissi di `abc` sono: $\epsilon$, `a`, `ab`, `abc` [LinguaggiI.pdf, Slide 89].
*   **Potenze di un alfabeto (Powers of an alphabet):**
    *   $\Sigma^n$ indica l'insieme di tutte le stringhe sull'alfabeto $\Sigma$ di lunghezza esattamente pari a $n$ [LinguaggiI.pdf, Slide 9, 89]. Per definizione, $\Sigma^0 = \{\epsilon\}$ [LinguaggiI.pdf, Slide 9, 89].
    *   **Chiusura di Kleene (Kleene Closure) $\Sigma^*$:** L'insieme di tutte le stringhe di qualsiasi lunghezza finita (inclusa la stringa vuota) sull'alfabeto $\Sigma$ [LinguaggiI.pdf, Slide 9, 90]:
        $$\Sigma^* = \bigcup_{i=0}^{\infty} \Sigma^i$$
    *   **Chiusura Positiva (Positive Closure) $\Sigma^+$:** L'insieme di tutte le stringhe sull'alfabeto $\Sigma$ ad esclusione della stringa vuota [LinguaggiI.pdf, Slide 9, 90]:
        $$\Sigma^+ = \bigcup_{i=1}^{\infty} \Sigma^i = \Sigma^* \setminus \{\epsilon\}$$

### 2.2 Teoria dei Linguaggi e Grammatiche Generative
*   **Definizione di Linguaggio (Language):** Un linguaggio $L$ su un alfabeto $\Sigma$ è un sottoinsieme di $\Sigma^*$ ($L \subseteq \Sigma^*$) [LinguaggiI.pdf, Slide 10, 91].
    *   *Esempi:* $L_1 = \{x \in \Sigma_1^* \mid x \text{ contiene la sottostringa "fool"}\}$; $L_2 = \{x \in \Sigma_2^* \mid x \text{ rappresenta un numero binario divisibile per 7}\}$ [LinguaggiI.pdf, Slide 91].
*   **Operazioni sui linguaggi:** Poiché i linguaggi sono insiemi, ereditano le operazioni standard della teoria degli insiemi (Unione $A \cup B$, Intersezione $A \cap B$, Differenza $A \setminus B$, Complemento $\bar{A} = \Sigma^* \setminus A$) [LinguaggiI.pdf, Slide 11, 120]. Sono definite inoltre:
    *   **Concatenazione di linguaggi:** $AB = \{ab \mid a \in A \land b \in B\}$ [LinguaggiI.pdf, Slide 11, 92].
    *   **Chiusura di Kleene $L^*$:**
        $$L^* = \bigcup_{i=0}^{\infty} L^i, \quad \text{dove } L^0 = \{\epsilon\}$$
        [LinguaggiI.pdf, Slide 11, 92]. Nota: il linguaggio vuoto $\emptyset \neq \{\epsilon\}$ [LinguaggiI.pdf, Slide 92].
*   **Definizione di Grammatica:** Una grammatica $G$ è definita formalmente come una quadrupla:
    $$G = (\Sigma, N, S, P)$$
    dove $\Sigma$ è l'alfabeto dei simboli terminali, $N$ è l'insieme dei simboli non terminali (con $\Sigma \cap N = \emptyset$), $S \in N$ è il simbolo non terminale iniziale (starting symbol) e $P$ è l'insieme finito di regole di produzione (rewriting rules) del tipo $U \rightarrow V$ [LinguaggiI.pdf, Slide 12, 93].

### 2.3 La Gerarchia di Chomsky e Complessità
La Gerarchia di Chomsky classifica le grammatiche in quattro classi (Tipi) in base alle restrizioni applicate alla forma delle produzioni $U \rightarrow V$ (con $U \in (\Sigma \cup N)^+$ e $V \in (\Sigma \cup N)^*$) [LinguaggiI.pdf, Slide 13, 95, 96]:

1.  **Tipo 0 (Unrestricted / Phrase-Structure):** Nessuna restrizione sulle produzioni. Riconosciute dalle **Macchine di Turing** [LinguaggiI.pdf, Slide 13, 96, 128, 129].
2.  **Tipo 1 (Context-Sensitive):** Regole del tipo $\alpha A \beta \rightarrow \alpha \gamma \beta$ (oppure $|U| \le |V|$). Riconosciute dagli **automi a spazio limitato (Linear Bounded Automata, LBA)** [LinguaggiI.pdf, Slide 13, 95, 128, 129].
3.  **Tipo 2 (Context-Free):** Regole della forma $A \rightarrow V$ con $A \in N$ (la parte sinistra deve essere un singolo non-terminale). Riconosciute dagli **Automi a Pila (Pushdown Automata - PDA)** [LinguaggiI.pdf, Slide 13, 96, 128, 129].
4.  **Tipo 3 (Regular):** Regole della forma $A \rightarrow aB$ oppure $A \rightarrow a$ (Grammatiche Regolari Destre). Riconosciute dagli **Automi a Stati Finiti (FSA)** [LinguaggiI.pdf, Slide 13, 97, 128, 129].

#### Tabella di Decidibilità e Complessità dei Problemi d'Esame:
*   **Membership (\(w \in L(G)\)?):** Decidibile in tempo polinomiale ($P$) per i linguaggi Regolari e Context-Free. Decidibile in spazio polinomiale ($PSPACE$) per i Context-Sensitive. Non decidibile ($U$ - Undecidable) per il Tipo 0 [LinguaggiI.pdf, Slide 13, 96, 128].
*   **Emptiness (\(L(G) = \emptyset\)?):** Decidibile in tempo polinomiale ($P$) per Regolari e Context-Free. Non decidibile ($U$) per i Tipi 1 e 0 [LinguaggiI.pdf, Slide 13, 96, 128].
*   **Equivalenza (\(L(G_1) \equiv L(G_2)\)?):** Decidibile in $PSPACE$ per i linguaggi regolari. Non decidibile ($U$) per tutti gli altri livelli della gerarchia [LinguaggiI.pdf, Slide 13, 96, 128].

### 2.4 Automi a Stati Finiti e Cinque Formalismi Equivalenti
I cinque formalismi equivalenti per rappresentare e riconoscere un linguaggio regolare sono:
1.  **Grammatiche Regolari (RG)** [LinguaggiI.pdf, Slide 14, 97].
2.  **Automi a Stati Finiti Deterministici (DFA)** [LinguaggiI.pdf, Slide 14, 97].
3.  **Automi a Stati Finiti Non Deterministici (NFA)** [LinguaggiI.pdf, Slide 14, 97].
4.  **Automi a Stati Finiti Non Deterministici con \(\epsilon\)-transizioni (\(\epsilon\)-NFA)** [LinguaggiI.pdf, Slide 14, 97].
5.  **Espressioni Regolari (RE)** [LinguaggiI.pdf, Slide 14, 97].

*   **Definizione di Grammatica Regolare Destra (Right Regular Grammar):** Una grammatica in cui ogni produzione ha la forma $A \rightarrow aB$ o $A \rightarrow a$ (con $A, B \in N$ e $a \in \Sigma$). Solo per il simbolo iniziale è ammessa la produzione $S \rightarrow \epsilon$ [LinguaggiI.pdf, Slide 14, 97].
*   **Definizione Formale di DFA:** Un Automa a Stati Finiti Deterministico $M$ è una quintupla:
    $$M = (Q, \Sigma, \delta, q_0, F)$$
    dove $Q$ è un insieme finito di stati, $\Sigma$ è l'alfabeto di input, $\delta: Q \times \Sigma \rightarrow Q$ è la funzione di transizione deterministica, $q_0 \in Q$ è lo stato iniziale, $F \subseteq Q$ è l'insieme degli stati finali o accettanti [LinguaggiI.pdf, Slide 14, 98]. La funzione estesa alle stringhe $\hat{\delta}: Q \times \Sigma^* \rightarrow Q$ è definita per induzione:
    $$\hat{\delta}(q, \epsilon) = q, \quad \hat{\delta}(q, wa) = \delta(\hat{\delta}(q, w), a)$$
    Una stringa $x$ è accettata se $\hat{\delta}(q_0, x) \in F$ [LinguaggiI.pdf, Slide 15, 100, 101, 102].
*   **Definizione Formale di NFA:** Un Automa a Stati Finiti Non Deterministico ammette transizioni multiple per lo stesso simbolo. Si differenzia dal DFA unicamente per la funzione di transizione, che restituisce un insieme di stati:
    $$\delta: Q \times \Sigma \rightarrow \mathcal{P}(Q)$$
    [LinguaggiI.pdf, Slide 16, 102]. Una stringa $w$ è accettata se l'insieme di stati raggiungibili interseca gli stati accettanti: $\hat{\delta}(q_0, w) \cap F \neq \emptyset$ [LinguaggiI.pdf, Slide 16].

### 2.5 Algoritmi di Trasformazione Costruttiva
*   **Da Grammatiche Regolari a NFA (Theorem 1):** Dato $RG = (\Sigma, N, S, P)$, si costruisce l'equivalente $NFA = (N \cup \{F_{new}\}, \Sigma, \delta, S, F_{NFA})$ in cui:
    1.  Se $A \rightarrow a \in P \Rightarrow F_{new} \in \delta(A, a)$ [LinguaggiI.pdf, Slide 27, 57, 103].
    2.  Se $A \rightarrow aB \in P \Rightarrow B \in \delta(A, a)$ [LinguaggiI.pdf, Slide 27, 57, 103].
    3.  L'insieme degli stati accettanti è $F_{NFA} = \{F_{new}\} \cup \{S\}$ se $S \rightarrow \epsilon \in P$, altrimenti $F_{NFA} = \{F_{new}\}$ [LinguaggiI.pdf, Slide 27, 57, 103].
*   **Da NFA a Grammatiche Regolari (Theorem 2):** Dato un automa non deterministico $NFA = (Q, \Sigma, \delta, q_0, F)$, si costruisce l'equivalente grammatica regolare destra $RG = (\Sigma, Q', q_0', P)$ seguendo questi passi costruttivi [LinguaggiI.pdf, Slide 28, 58, 103]:
    1.  **Regole per le transizioni:** Per ciascuna transizione nell'automa, se $B \in \delta(A, a)$ (con $A, B \in Q$ e $a \in \Sigma$), si aggiunge la produzione $A \rightarrow aB$ al set $P$.
    2.  **Regole per gli stati finali:** Se lo stato di arrivo $B$ appartiene all'insieme degli stati finali dell'automa ($B \in F$), si aggiunge anche la produzione terminale $A \rightarrow a$ al set $P$.
    3.  **Gestione della stringa vuota (start state in F):** 
        *   Se lo stato iniziale appartiene agli stati finali dell'automa ($q_0 \in F$, ossia la stringa vuota $\epsilon$ appartiene al linguaggio), si introduce un nuovo simbolo iniziale non terminale $q$ (ponendo $Q' = Q \cup \{q\}$) e si aggiungono le produzioni $q \rightarrow q_0 \mid \epsilon$ in $P$, impostando il nuovo stato iniziale $q_0' = q$.
        *   Altrimenti, se $q_0 \notin F$, si pone $Q' = Q$ e il simbolo iniziale rimane invariato ($q_0' = q_0$).
*   **Da NFA a DFA (Subset Construction):** Algoritmo di determinizzazione. Dato l'NFA $M_N = (Q_N, \Sigma, \delta_N, q_0, F_N)$, si costruisce l'equivalente DFA $M_D = (Q_D, \Sigma, \delta_D, q_D, F_D)$ ponendo:
    1.  $Q_D = \mathcal{P}(Q_N)$ (l'insieme delle parti di $Q_N$) [LinguaggiI.pdf, Slide 17].
    2.  Lo stato iniziale del DFA è l'insieme singoletto contenente lo stato iniziale dell'NFA: $q_D = \{q_0\}$ [LinguaggiI.pdf, Slide 17].
    3.  Per ciascuno stato macro-stato $P \in Q_D$ e simbolo $a \in \Sigma$, la transizione è data dall'unione delle transizioni dei singoli stati:
        $$\delta_D(P, a) = \bigcup_{p \in P} \delta_N(p, a)$$
        [LinguaggiI.pdf, Slide 17].
    4.  $F_D = \{P \in Q_D \mid P \cap F_N \neq \emptyset\}$ (sono accettanti tutti i macro-stati che contengono almeno uno stato accettante dell'NFA) [LinguaggiI.pdf, Slide 17].
    5.  Si eliminano tutti i macro-stati non raggiungibili a partire dallo stato iniziale $q_D$ [LinguaggiI.pdf, Slide 106, 107].
    6. ![[Pasted image 20260825164940.png]]
*   **$\epsilon$-NFA ed eliminazione transizioni:**
    *   Un $\epsilon$-NFA consente transizioni spontanee sulla stringa vuota $\epsilon$ [LinguaggiI.pdf, Slide 21, 108, 109, 110].
    *   **$\epsilon$-closure (Epsilon-chiusura):** L'$\epsilon$-closure di uno stato $q$ (o di un insieme di stati $P$) è l'insieme di tutti gli stati raggiungibili da $q$ effettuando esclusivamente zero o più transizioni spontanee su $\epsilon$ [LinguaggiI.pdf, Slide 22, 108, 109, 110, 111].
    *   **Conversione da $\epsilon$-NFA a NFA:** Dato l'$\epsilon$-NFA $M = (Q, \Sigma, \delta, q_0, F)$, si costruisce l'NFA equivalente $M' = (Q, \Sigma, \delta', q_0, F')$ ponendo:
        1.  $\delta'(q, a) = \hat{\delta}(q, a) = \bigcup_{p \in \hat{\delta}(q, \epsilon)} \epsilon\text{-closure}(\delta(p, a))$ [LinguaggiI.pdf, Slide 23, 111, 112, 117].
        2.  $F' = F \cup \{q_0\}$ se $\epsilon\text{-closure}(q_0) \cap F \neq \emptyset$, altrimenti $F' = F$ [LinguaggiI.pdf, Slide 23, 117, 118, 119].
        3. ![[Pasted image 20260825165700.png]]

#### Esempio Svolto di Determinizzazione (slide)
NFA su $\Sigma = \{0,1\}$ con $F = \{q_2\}$:

| $\delta_N$ | 0 | 1 |
|---|---|---|
| $\to q_0$ | $\{q_0\}$ | $\{q_0, q_1\}$ |
| $q_1$ | $\{q_1\}$ | $\{q_0, q_2\}$ |
| $*q_2$ | $\{q_1, q_2\}$ | $\{q_0, q_1, q_2\}$ |

Costruzione dei **soli sottoinsiemi raggiungibili**:
1.  $s_0 = \{q_0\}$: su 0 → $\{q_0\} = s_0$; su 1 → $\{q_0, q_1\} = s_1$ (nuovo);
2.  $s_1 = \{q_0, q_1\}$: su 0 → $\{q_0\} \cup \{q_1\} = s_1$; su 1 → $\{q_0,q_1\} \cup \{q_0,q_2\} = \{q_0,q_1,q_2\} = s_2$ (nuovo);
3.  $s_2 = \{q_0, q_1, q_2\}$: su 0 e su 1 → $s_2$ (stato pozzo).

| $\delta_D$ | 0 | 1 |
|---|---|---|
| $\to s_0 = \{q_0\}$ | $s_0$ | $s_1$ |
| $s_1 = \{q_0, q_1\}$ | $s_1$ | $s_2$ |
| $*s_2 = \{q_0, q_1, q_2\}$ | $s_2$ | $s_2$ |

Finali = i macro-stati contenenti $q_2$ (solo $s_2$). Linguaggio riconosciuto: $L = \{x \in \{0,1\}^* \mid x \text{ contiene almeno 2 occorrenze di } 1\}$. (La tabella completa su $\mathcal{P}(Q_N)$ mostrerebbe che la maggior parte degli stati è irraggiungibile.)

### 2.6 Espressioni Regolari (RE) e Ulteriori Conversioni
*   An inductive definition of RE and their language $L(r)$ [LinguaggiI.pdf, Slide 33, 120].
*   **Da RE a $\epsilon$-NFA (Thompson's Inductive Construction):**
    *   *Casi base:* Per $\emptyset$ (automa senza transizioni), per $\epsilon$ (due stati uniti da transizione $\epsilon$), per $a$ (due stati uniti da transizione $a$) [LinguaggiI.pdf, Slide 34, 120].
    *   *Operatore Unione $r+s$:* Unisce in parallelo gli automi di $r$ e $s$ tramite un nuovo stato iniziale e un nuovo stato finale connessi con transizioni $\epsilon$ [LinguaggiI.pdf, Slide 34, 120].
    *   *Operatore Concatenazione $rs$:* Connette lo stato finale dell'automa di $r$ allo stato iniziale dell'automa di $s$ tramite una transizione $\epsilon$ (oppure fondendoli) [LinguaggiI.pdf, Slide 34, 120].
    *   *Operatore Chiusura di Kleene $r^*$:* Introduce un ciclo di feedback con transizioni $\epsilon$ per consentire ripetizioni infinite o il salto completo dell'automa [LinguaggiI.pdf, Slide 34, 120].
    * ![[Pasted image 20260825170054.png]]
    * ![[Pasted image 20260825170128.png]]
*   **Da DFA a RE (State Elimination Method):** Si eliminano progressivamente gli stati intermedi dell'automa riscrivendo le etichette degli archi come espressioni regolari. Per eliminare uno stato intermedio $q_s$ — con self-loop etichettato $S$, archi in ingresso $R_{is}$ e archi in uscita $R_{sj}$ — si aggiorna l'etichetta di ogni arco diretto da $q_i$ a $q_j$ (precedentemente $R_{ij}$) con:
    $$R_{ij} \; := \; R_{ij} + R_{is}\, S^{*}\, R_{sj}$$
    Il processo si ripete eliminando uno stato intermedio per volta, fino a ridurre l'automa a un unico stato iniziale e un unico stato finale: l'etichetta dell'arco residuo è l'espressione regolare del linguaggio [LinguaggiI.pdf, Slide 36, 37 / 124].
    
	![[Pasted image 20260825170253.png]]
	
	One initial state and several final states s1, s2, … sn => Repeat the previous steps for each s_i turning any other final state in non final => R1 + R2 + . . . + RN
### 2.7 Algoritmo di Minimizzazione del DFA
Consente di trovare il DFA minimo equivalente riducendo il numero di stati. Si basa sul concetto di stati indistinguibili [LinguaggiI.pdf, Slide 35 / 133].

*   **Algoritmo Pairwise DISTINCT-Table (Algoritmo Principale delle Slide d'Esame):**
    Questo è l'algoritmo primario presentato in dettaglio nelle slide del corso d'esame. Utilizza una tabella triangolare inferiore per calcolare le coppie di stati distinguibili e poi fondere quelle indistinguibili [LinguaggiI.pdf, Slide 35 / 133].
    1.  **Inizializzazione della Tabella triangolare:** Si crea una tabella triangolare inferiore chiamata `DISTINCT` per tutte le coppie di stati $(p, q)$ con $p \neq q$, inizialmente vuota (blank).
    2.  **Passo Base (Stati finali vs non finali):** Per ogni coppia di stati $(p, q)$, se uno è uno stato finale (accettante) e l'altro non lo è, allora la coppia è immediatamente distinguibile. Si scrive $\epsilon$ nella corrispondente cella: $DISTINCT[p, q] = \epsilon$ [LinguaggiI.pdf, Slide 35 / 133].
    3.  **Passo Induttivo (Loop Principale):** Si esegue un loop fino a quando un'intera iterazione non produce alcun cambiamento sulla tabella. Per ogni coppia di stati $(p, q)$ la cui cella è ancora vuota, e per ciascun simbolo dell'alfabeto $a \in \Sigma$:
        *   Si calcolano i target di transizione $\delta(p, a)$ e $\delta(q, a)$.
        *   Se la cella corrispondente ai target, $DISTINCT[ \delta(p, a), \delta(q, a) ]$, **non è vuota** (cioè i target sono già provati essere distinguibili), allora anche $(p, q)$ sono distinguibili. Si annota il simbolo che li distingue scrivendo $a$ nella cella: $DISTINCT[p, q] = a$ [LinguaggiI.pdf, Slide 35 / 133].
    4.  **Fusione degli Stati equivalenti:** Al termine del ciclo, tutte le celle che sono rimaste vuote (blank) indicano che i relativi stati sono indistinguibili (equivalenti). Questi stati vengono uniti (fusi) tra loro per formare i nuovi stati del DFA minimo [LinguaggiI.pdf, Slide 35 / 133].
    * ![[Pasted image 20260825171035.png]]
    * ![[Pasted image 20260825170929.png]] 
    * **Complessità temporale:** L'algoritmo pairwise DISTINCT-table ha complessità $O(k \cdot n^2)$, dove $n = |Q|$ è il numero di stati e $k = |\Sigma|$ è la cardinalità dell'alfabeto.

*   **Algoritmo di Hopcroft (Alternativa O(n log n)):**
    Le slide menzionano soltanto che esiste un algoritmo più complesso basato sulla partizione progressiva (Hopcroft's partition refinement) che raggiunge una complessità ottima di $O(k \cdot n \log n)$, ma l'algoritmo di riferimento per gli esercizi d'esame è quello pairwise della tabella DISTINCT descritto sopra [LinguaggiI.pdf, Slide 35 / 135].

#### Esempio Svolto di Minimizzazione (slide: DFA per $(a|b)^+$)
DFA con $s_0$ iniziale (non finale) e $s_1, s_2$ finali.
1.  **Passo base:** una cella per volta, gli stati finali contro i non finali ⇒ $DISTINCT[s_0, s_1] = \epsilon$ e $DISTINCT[s_0, s_2] = \epsilon$;
2.  **Loop principale:** nessuna coppia a cella vuota ha transizioni verso celle già marcate ⇒ nessun cambiamento in un'intera iterazione;
3.  **Fusione:** $DISTINCT[s_1, s_2]$ resta vuota ⇒ $s_1 \equiv s_2$: il DFA minimo ha **2 stati**.

### 2.8 Proprietà di Chiusura e Limiti dei Linguaggi Regolari
*   **Proprietà di Chiusura:** I linguaggi regolari sono chiusi rispetto alle operazioni di: Unione, Concatenazione, Kleene Closure, Complementazione, Intersezione e Differenza [LinguaggiI.pdf, Slide 40, 124].
*   **Pumping Lemma per i Linguaggi Regolari:** Se $L$ è un linguaggio regolare infinito, esiste un intero $k$ (costante di pompaggio) tale che ogni stringa $z \in L$ con $|z| \ge k$ può essere decomposta in tre sottostringhe $z = uvw$ che soddisfano le seguenti condizioni [LinguaggiI.pdf, Slide 40, 122]:
    1.  $|uv| \le k$
    2.  $|v| > 0$
    3.  $\forall i \ge 0: u v^i w \in L$
*   **Uso in forma negativa per dimostrare la non-regolarità:** Per dimostrare che $L = \{a^n b^n \mid n \in \mathbb{N}\}$ non è regolare, prendiamo la stringa $z = a^k b^k \in L$ [LinguaggiI.pdf, Slide 41, 123]. Qualsiasi scomposizione $z = uvw$ con $|uv| \le k$ forza la stringa $v$ a essere composta esclusivamente da simboli `a` (poiché si trova interamente entro i primi $k$ caratteri di $z$) [LinguaggiI.pdf, Slide 41, 123]. Di conseguenza, pompando $v$ con $i=2$, la stringa risultante $u v^2 w = a^{k+|v|} b^k$ conterrà più simboli `a` che `b`, non appartenendo al linguaggio $L$, il che nega la tesi del lemma e dimostra che $L$ non è regolare [LinguaggiI.pdf, Slide 41, 123].


### 2.9 Automi a Pila (Pushdown Automata)
*   **Struttura:** controllo a stati finiti + nastro di input + **pila**; la testa legge la cima ed esegue *push*, *pop*, *empty*.
*   **Definizione (slide):** $M = (Q, \Sigma, R, \delta, q_0, Z_0, F)$ con $R$ alfabeto dei simboli di pila, $Z_0 \in R$ simbolo iniziale, e
    $$\delta : Q \times (\Sigma \cup \{\epsilon\}) \times R \to \mathcal{P}(Q \times R^*)$$
*   **Descrizioni istantanee:** triple $(q, w, \gamma)$ — stato corrente, input residuo, contenuto della pila; un passo:
    $$(q_0, aw, Z\eta) \vdash (q_1, w, \gamma\eta) \quad \text{se} \quad (q_1, \gamma) \in \delta(q_0, a, Z)$$
*   **Linguaggio accettato:** per **stati finali** $F$, oppure per **pila vuota** (con $F = \emptyset$).
*   **Esempio svolto (slide):** $L = \{x\,c\,x^R \mid x \in \{a,b\}^*\}$, riconosciuto **per pila vuota** da
    $M = (\{q_0, q_1\}, \{a,b,c\}, \{Z,A,B\}, \delta, q_0, Z, \emptyset)$ con (celle non specificate riempibili in modo da forzare il rigetto):

    | $\delta$ | $a$ | $b$ | $c$ |
    |---|---|---|---|
    | $q_0, Z$ | $(q_0, ZA)$ | $(q_0, ZB)$ | $(q_1, \epsilon)$ |
    | $q_1, Z$ | $(q_1, Z)$ | $(q_1, Z)$ | — |
    | $q_1, A$ | $(q_1, \epsilon)$ | $(q_1, Z)$ | $(q_1, Z)$ |
    | $q_1, B$ | $(q_1, Z)$ | $(q_1, \epsilon)$ | $(q_1, Z)$ |

    **Traccia di `abcba`** (pila scritta dal fondo alla cima):
    ```
    (q0, abcba, Z)  ⊢  (q0, bcba, ZA)   [δ(q0,a,Z)=(q0,ZA): push A]
                    ⊢  (q0, cba,  ZBA)  [δ(q0,b,Z)=(q0,ZB): push B]
                    ⊢  (q1, ba,   BA)   [δ(q0,c,Z)=(q1,ε):  pop Z, cambio stato]
                    ⊢  (q1, a,    A)    [δ(q1,b,B)=(q1,ε):  pop B]
                    ⊢  (q1, ε,    ε)    [δ(q1,a,A)=(q1,ε):  pop A]
    ```

    Input consumato **e** pila vuota ⇒ accettato. La sintassi dei linguaggi di programmazione è progettata con marcatori (`if`, `while`, `then`, …) proprio perché il parsing sia realizzabile con un PDA **deterministico**.
    
    ![[Pasted image 20260825171521.png]]

### 2.10 Pumping Lemma per i Linguaggi Context-Free
*   **Enunciato (slide):** se $L$ è context-free, esiste $k \in \mathbb{N}$ tale che per ogni $z \in L$ con $|z| \ge k$ esiste una scomposizione $z = u\,v\,w\,x\,y$ con:
    1.  $|vwx| \le k$
    2.  $|vx| > 0$
    3.  $\forall i \ge 0: \; u\,v^i w\,x^i y \in L$
*   **Uso in forma negativa:** se per ogni $k$ esiste $z \in L$, $|z| \ge k$, tale che **nessuna** scomposizione soddisfa le tre condizioni, allora $L$ non è context-free.
*   **Esempio svolto (slide):** $L = \{a^n b^n c^n \mid n \in \mathbb{N}\}$ non è CF. Sia $z = a^k b^k c^k$. Poiché $|vwx| \le k$, $v$ e $x$ insieme coprono al più **due blocchi adiacenti** di lettere; pompando con $i \neq 0$ si alterano al più due dei tre esponenti (es. $a^k b^{k+i} c^{k+j}$ con $i + j \neq 0$), e la stringa ottenuta non appartiene a $L$. Contraddizione ⇒ $L$ non è CF. ∎
*   **Esercizi (slide):** dire se sono CF: $\{0^n 1^{kn}\}$, $\{a^i b^j c^k \mid i = j \text{ o } j = k\}$, $\{a^i b^j c^k \mid k \neq i+j\}$, $\{w \mid w \neq vv\}$.

<a id="cap3"></a>
## CAPITOLO 3: Analisi Lessicale (Lexing)
**Source:** *Lexer.pdf*

### 3.1 Il Ruolo del Lexer nella Pipeline del Front-End
*   **Perché separare lo Scanner (analisi lessicale) dal Parser (analisi sintattica)?**
    1.  **Semplicità del design:** Consente di gestire i dettagli di basso livello della lettura dei caratteri (spazi bianchi, commenti, formattazione) isolandoli dal parser [Lexer.pdf, Slide 4, 84].
    2.  **Efficienza prestazionale:** Lo scanner è l'unica fase del compilatore che esamina ogni singolo carattere del sorgente [Lexer.pdf, Slide 85]. Un design ottimizzato e snello dello scanner permette di rimuovere preventivamente l'overhead di basso livello, consentendo al parser di operare su flussi di token molto più compatti, migliorando la velocità complessiva di compilazione [Lexer.pdf, Slide 4, 84].
    3.  **Portabilità:** Rende il compilatore più modulare e semplice da manutenere [Lexer.pdf, Slide 4, 84].
*   **Definizioni formali:**
    *   **Token:** Una coppia ordinata $\langle\text{part of speech, lexeme}\rangle$ [Lexer.pdf, Slide 6, 84]. Rappresenta l'unità sintattica elementare che viene passata al parser (es. `NUMBER`, `IDENTIFIER`, `IF`) [Lexer.pdf, Slide 6, 84].
    *   **Lessema (Lexeme):** La sequenza concreta di caratteri letta dal file sorgente che costituisce l'istanza del token (es. `3.14`, `x`, `while`) [Lexer.pdf, Slide 6, 84].
    *   **Pattern:** La regola di corrispondenza, tipicamente espressa sotto forma di espressione regolare (RE), che descrive l'insieme dei possibili lessemi associabili a quel token [Lexer.pdf, Slide 6, 84].
    *   **Errore Lessicale (Lexical Error):** Qualsiasi sequenza di caratteri che non corrisponde al pattern di alcun token legale definito nella grammatica lessicale del linguaggio (es. un identificatore che inizia con un numero o caratteri non consentiti) [Lexer.pdf, Slide 6, 84].

### 3.2 Pipeline di Costruzione di uno Scanner Automatizzato
La generazione automatica di uno scanner a partire da specifiche formali (come Lex o Flex) segue rigorosamente 5 fasi sequenziali:
1.  **Specificare la micro-sintassi:** Si definiscono le espressioni regolari (RE) per ogni classe di token del linguaggio [Lexer.pdf, Slide 12, 85].
2.  **Costruire l'\(\epsilon\)-NFA:** Si applica la costruzione induttiva di Thompson per ottenere un automa a stati finiti non deterministico con transizioni spontanee per ciascuna RE [Lexer.pdf, Slide 12, 85].
3.  **Determinizzare l'automa (NFA to DFA):** Si applica l'algoritmo di subset construction per ottenere un DFA equivalente esente da scelte non deterministiche [Lexer.pdf, Slide 12, 85].
4.  **Minimizzare il DFA:** Si applica l'algoritmo di Hopcroft per unire gli stati indistinguibili e ridurre al minimo le dimensioni della tabella di transizione [Lexer.pdf, Slide 12, 85].
5.  **Generare il Driver Code:** Si converte la matrice di transizione risultante in un recognizer table-driven efficiente, in genere basato su cicli di lettura caratteri e lookup veloci [Lexer.pdf, Slide 12, 85].

### 3.3 Risoluzione delle Ambiguità Lessicali
Durante la scansione possono sorgere conflitti in cui più regole o lessemi corrispondono all'input. Vengono usate due euristiche standard per risolverli deterministicamente:
*   **Longest Match (Maximal Munch):** Lo scanner seleziona sempre il lessema più lungo possibile che corrisponde a una regola valida. Ad esempio, la stringa di input `while_var` verrà riconosciuta interamente come un unico identificatore `while_var` anziché come la parola chiave `while` seguita dall'identificatore `_var` [Lexer.pdf, Slide 13].
*   **First Fit (Precedenza delle regole):** Se un lessema corrisponde esattamente e con la stessa lunghezza a più regole contemporaneamente, lo scanner preferisce la regola dichiarata per prima nella specifica lessicale. Questo risolve il conflitto tra le parole chiave (es. `if`, `while`) e gli identificatori generici: poiché le keyword sono dichiarate prima, l'input `if` viene mappato sul token della parola chiave `IF` anziché sull'identificatore generico [Lexer.pdf, Slide 13].

### 3.4 Casi di Studio ed Esempi d'Esame

**Caso di Studio 1 — specifica generica (slide).** `Register → r (0|…|9)(0|…|9)*`: almeno una cifra, lunghezza arbitraria. DFA:

```
        r            (0|…|9)
  s0 ───────► s1 ────────► s2 (finale)
   │           │r            │r
   ▼           ▼             ▼
  (qualsiasi altro carattere porta allo stato di errore se)
```

Comportamento: `r17` → $s_0, s_1, s_2$ accettato; `r` → $s_0, s_1$ rigettato; `0` → $s_e$ subito.

**Skeleton recognizer (table-driven, O(1) per carattere):**
```
Char  ← next character
State ← s0
while (Char ≠ EOF)
    State ← δ(State, Char)
    Char  ← next character
if (State is final) then report success else report failure
```

| δ | r | 0…9 | altri |
|---|---|---|---|
| s0 | s1 | se | se |
| s1 | se | s2 | se |
| s2 | se | s2 | se |
| se | se | se | se |

**Tabella delle azioni α (slide):** affiancata a δ, associa a ogni transizione un'azione (tipicamente *catturare il lessema*):

```
Char ← next character;   State ← s0
while (Char ≠ EOF)
    Next ← δ(State, Char)
    Act  ← α(State, Char)
    esegui Act
    State ← Next
    Char ← next character
if (State is final) then report success else report failure
```

*   **Caso di Studio 2 — Tighter Register Specification (slide):**
    Nelle macchine virtuali come ILOC, i registri fisici sono spesso limitati da $r_0$ a $r_{31}$ [Lexer.pdf, Slide 15]. Se si usasse l'espressione regolare generica `r[0-9]+`, lo scanner accetterebbe lessemi errati come $r_{32}$ o $r_{99}$, delegando il controllo delle violazioni alle fasi semantiche successive.
    Per bloccare gli errori lessicalmente alla fonte, le slide presentano una specifica rigorosa (tighter specification) tramite la seguente RE d'esame [Lexer.pdf, Slide 15 / 42]:
    $$Register \rightarrow r \ ( \ (0 \mid 1 \mid 2)(Digit \mid \epsilon) \mid (4 \mid 5 \mid 6 \mid 7 \mid 8 \mid 9) \mid (3 \mid 30 \mid 31) \ )$$
    *Nota semantica:* Questa espressione regolare d'esame accetta esattamente l'intervallo $[r_0, r_{31}]$. Analizzandone i rami: $(0|1|2)(Digit|\epsilon)$ genera $r_0 \dots r_2$, $r_{00} \dots r_{29}$; il ramo $(4|5|6|7|8|9)$ genera $r_4 \dots r_9$; il ramo $(3|30|31)$ genera $r_3, r_{30}, r_{31}$. L'unione copre esattamente i registri validi.

    La relativa tabella di transizione $\delta$ e la tabella delle azioni $\alpha$ codificate nel driver dello scanner sono riprodotte di seguito [Lexer.pdf, Slide 15 / 43, 44]:

    ##### Tabella di Transizione $\delta$ (Tighter Register Specification):
	```
	    +-------+-----+-----+-----+-----+-----+-----------+
	    | State |  r  | 0,1 |  2  |  3  | 4-9 | All other |
	    +-------+-----+-----+-----+-----+-----+-----------+
	    |  s0   | s1  | se  | se  | se  | se  |    se     |
	    |  s1   | se  | s2  | s2  | s5  | s4  |    se     |
	    |  s2   | se  | s3  | s3  | s3  | s3  |    se     |
	    |  s3   | se  | se  | se  | se  | se  |    se     |
	    |  s4   | se  | se  | se  | se  | se  |    se     |
	    |  s5   | se  | s6  | se  | se  | se  |    se     |
	    |  s6   | se  | se  | se  | se  | se  |    se     |
	    |  se   | se  | se  | se  | se  | se  |    se     |
	    +-------+-----+-----+-----+-----+-----+-----------+
    ```

    ##### Tabella delle Azioni $\alpha$ (Tighter Register Specification):
    *(Nota: s1, s2, s3, s4, s5, s6 sono gli stati dell'automa; 'start' inizializza la lettura, 'add' cattura il carattere nel lessema corrente, 'exit' indica il completamento con successo se lo stato corrente è accettante)* [Lexer.pdf, Slide 15 / 44].
    
| State      | r        | 0,1    | 2      | 3      | 4–9    | other   |
| ---------- | -------- | ------ | ------ | ------ | ------ | ------- |
| s0         | 1, start | e      | e      | e      | e      | e       |
| s1         | e        | 2, add | 2, add | 5, add | 4, add | e       |
| s2         | e        | 3, add | 3, add | 3, add | 3, add | e, exit |
| s3, s4, s6 | e        | e      | e      | e      | e      | e, exit |
| s5         | e        | 6, add | e      | e      | e      | e, exit |
| se         | e        | e      | e      | e      | e      | e       |

### 3.5 Rollback e Limiti degli Scanner DFA
*   **Rollback (slide):** avanzando lo scanner può superare l'ultimo stato finale; uno **stack degli stati traversati** permette di tornare indietro:
	![[Pasted image 20260825173232.png]]
	
	Se non esiste alcun stato finale su cui tornare ⇒ **errore lessicale**. Tutte le implementazioni (table-driven, direct-coded, hand-coded) costano O(1) per carattere più il costo del rollback.
*   **Priorità tra categorie (slide):** combinando tutte le RE in un unico DFA, alcune stringhe matchano più categorie (keyword vs identificatori): si risolve per **ordine di dichiarazione delle RE**. Esempio slide: con `Identifier → Letter (Letter|Digit)*` e `key → if | …`, la stringa `ife` è classificata come **identificatore**.
*   **Eccezioni al modello DFA (slide):** *contextual keywords* (`async`, `await`, `record` — keyword solo in certi contesti sintattici: richiedono cooperazione lexer/parser) e sintassi **sensibile all'indentazione** (Python: il lexer traccia i livelli ed emette `INDENT`/`DEDENT`). Storicamente le feature che rompono la regolarità lessicale non hanno avuto successo.
<a id="cap4"></a>
## CAPITOLO 4: Parsing Top-Down e Parser LL(1)
**Sources:** *ParsingMio.pdf / TableConstruction.pdf*

### 4.1 Limiti dell'Analisi Lessicale e Introduzione al CFG
*   **Perché i linguaggi regolari non bastano?**
    Le espressioni regolari e gli automi a stati finiti non hanno memoria sufficiente per gestire strutture gerarchiche annidate arbitrarie o corrispondenze non locali. Non possono verificare se:
    1.  Le parentesi tonde, quadre o graffe sono correttamente bilanciate ad un livello di annidamento arbitrario: $L = \{(^n )^n \mid n \ge 0\}$ non è regolare [ParsingMio.pdf, Slide 12, 134].
    2.  I blocchi di codice annidati con strutture `begin ... end` o `{ ... }` sono bilanciati correttamente [ParsingMio.pdf, Slide 12, 134].
    3.  Una lista di argomenti passata a funzioni annidate (es. `f(a, g(b, c), h(d))`) deve distinguere le virgole dei parametri interni da quelle dello scope esterno [ParsingMio.pdf, Slide 12, 134].
*   **Definizione di Grammatica Context-Free (CFG):** Una grammatica context-free (Tipo 2) ha produzioni della forma:
    $$A \rightarrow \beta$$
    dove $A \in N$ è un singolo simbolo non terminale e $\beta \in (\Sigma \cup N)^+$ (e solo per il simbolo iniziale $S$ è ammessa la produzione $S \rightarrow \epsilon$ per generare la stringa vuota) [LinguaggiI.pdf, Slide 13, 42 / 96; ParsingMio.pdf, Slide 13, 78].
*   **Derivazioni, Sentential Form e Parse Tree:**
    *   Una **derivazione** consiste in una sequenza di passaggi di riscrittura a partire dal simbolo iniziale:
        $$S \Rightarrow \gamma_0 \Rightarrow \gamma_1 \Rightarrow \dots \Rightarrow \gamma_n \Rightarrow w$$
        [ParsingMio.pdf, Slide 14, 135].
    *   Ogni $\gamma_i$ è una **forma sentenziale** (*sentential form*) se contiene almeno un non-terminale; se contiene solo terminali, allora è una frase o sentenza del linguaggio ($w \in L(G)$) [ParsingMio.pdf, Slide 14, 135].
    *   **Leftmost derivation:** Ad ogni passo viene espanso il non-terminale più a sinistra [ParsingMio.pdf, Slide 14, 135].
    *   **Rightmost derivation:** Ad ogni passo viene espanso il non-terminale più a destra [ParsingMio.pdf, Slide 135].
    *   In una grammatica non ambigua, ogni stringa del linguaggio ammette esattamente un'unica derivazione leftmost e un'unica derivazione rightmost. La derivazione leftmost e la derivazione rightmost differiscono nel loro ordine di riscrittura, ma corrispondono entrambe allo stesso identico albero di parsing (*Parse Tree*) [ParsingMio.pdf, Slide 136].
*   **Ambiguità:** Una grammatica è ambigua se esiste una frase che ammette più alberi di parsing differenti (o più derivazioni leftmost/rightmost distinte) [ParsingMio.pdf, Slide 136]. Un esempio tipico è il problema del *dangling-else* nei costrutti condizionali `if-then-else` [ParsingMio.pdf, Slide 136, 137].

*   **Esempio svolto: dangling-else (slide).** Con
    ```
    Stmt → if Expr then Stmt
         | if Expr then Stmt else Stmt
         | … altre istruzioni …
    ```
    la frase `if E1 then if E2 then S1 else S2` ammette **due parse tree** (else abbinato all'if interno o a quello esterno) ⇒ grammatica ambigua, e i due alberi implicano **semantiche diverse**. Riscrittura non ambigua (ogni else all'if più interno):
    ```
    0. Stmt     → if Expr then Stmt
    1.           | if Expr then WithElse else Stmt
    2.           | Other Statements
    3. WithElse → if Expr then WithElse else WithElse
    4.           | Other Statements
    ```
    Intuizione: dentro `WithElse` non si può generare un else non accoppiato; un if finale senza else può arrivare solo dalla regola 0 ⇒ l'esempio ha un'unica derivazione rightmost.
### 4.2 Parser LL(1) e Problemi di Ricorsione
*   Il parsing top-down tenta di ricostruire una derivazione leftmost a partire dal simbolo iniziale, procedendo verso il basso.
*   **Backtracking:** Se la grammatica contiene scelte non deterministiche, il parser deve andare per tentativi ed effettuare il backtracking su errore, il che degrada le performance.
*   **Non-terminazione su Ricorsione a Sinistra:** Una grammatica è ricorsiva a sinistra se esiste una derivazione del tipo $A \Rightarrow^+ A\alpha$ [ParsingMio.pdf, Slide 138]. I parser top-down (LL) entrano in un ciclo infinito di chiamate ricorsive su grammatiche ricorsive a sinistra, portando alla non-terminazione del compilatore [ParsingMio.pdf, Slide 138].
*   **Algoritmo di Eliminazione della Ricorsione a Sinistra Immediata:**
    Data la regola $A \rightarrow A\alpha \mid \beta$ (dove $\beta$ non inizia con $A$), si riscrive introducendo un nuovo non-terminale $A'$:
    $$A \rightarrow \beta A'$$
    $$A' \rightarrow \alpha A' \mid \epsilon$$
*   **Esempio di trasformazione generale (Slide d'Esame):**
    Prendendo l'ordine di simboli $G, E, T$:
    *   *Sorgente ricorsiva:*
        $$E \rightarrow E + T \mid T$$
        $$T \rightarrow E * T \mid id$$
    *   *Dopo trasformazione:*
        $$E \rightarrow T E'$$
        $$E' \rightarrow + T E' \mid \epsilon$$
        $$T \rightarrow id T'$$
        $$T' \rightarrow E' * T T' \mid \epsilon$$
        [ParsingMio.pdf, Slide 139].
*   **Left Factoring:** Consente di rimuovere i prefissi comuni dalle produzioni per evitare backtracking:
    $$A \rightarrow \alpha\beta_1 \mid \alpha\beta_2 \quad \Rightarrow \quad A \rightarrow \alpha A', \quad A' \rightarrow \beta_1 \mid \beta_2$$

### 4.3 Calcolo Formale degli Insiemi di Parsing Predittivo
Per costruire un parser deterministico con lookahead di un simbolo, calcoliamo tre insiemi fondamentali:
*   **Insieme FIRST:** FIRST($\alpha$) è l'insieme di tutti i terminali che possono trovarsi all'inizio di una qualsiasi stringa derivata da $\alpha$. Se $\alpha \Rightarrow^* \epsilon$, allora $\epsilon \in \text{FIRST}(\alpha)$ [ParsingMio.pdf, Slide 15, 140, 142].
*   **Insieme FOLLOW:** Per ogni non-terminale $A$, FOLLOW($A$) è l'insieme dei simboli terminali che possono apparire immediatamente dopo $A$ in una qualche forma sentenziale valida [ParsingMio.pdf, Slide 16, 142]. Se $S$ è lo start symbol, allora il marcatore di fine file $\$ \in \text{FOLLOW}(S)$ [ParsingMio.pdf, Slide 16, 142].
*   **Insieme FIRST+ (Predictive Set):** Si applica a una singola produzione $A \rightarrow \beta$ ed è definito come:
    $$\text{FIRST}^+(A \rightarrow \beta) = \begin{cases} \text{FIRST}(\beta) & \text{se } \epsilon \notin \text{FIRST}(\beta) \\ (\text{FIRST}(\beta) \setminus \{\epsilon\}) \cup \text{FOLLOW}(A) & \text{se } \epsilon \in \text{FIRST}(\beta) \end{cases}$$
    [ParsingMio.pdf, Slide 17, 144].

### 4.4 Costruzione della Tabella di Parsing LL(1)
*   **Proprietà LL(1):** Una grammatica è LL(1) se e solo se, per ogni coppia di produzioni distinte dello stesso non-terminale $A \rightarrow \alpha$ e $A \rightarrow \beta$, si ha:
    $$\text{FIRST}^+(A \rightarrow \alpha) \cap \text{FIRST}^+(A \rightarrow \beta) = \emptyset$$
    Questo garantisce la scelta di un'unica produzione adatta esaminando solo il simbolo corrente [ParsingMio.pdf, Slide 18, 140].
*   **Algoritmo di Riempimento della Tabella:**
    Per ciascuna produzione $A \rightarrow \beta$:
    Per ciascun terminale $t \in \text{FIRST}^+(A \rightarrow \beta)$, aggiungi la produzione $A \rightarrow \beta$ alla cella $M[A, t]$ della tabella.
    Se una qualsiasi cella contiene più di una produzione, la grammatica non è LL(1) [ParsingMio.pdf, Slide 18].

### 4.5 Caso di Studio Svolto: la Grammatica delle Espressioni Classica
Grammatica (dopo eliminazione della ricorsione sinistra) con la numerazione delle slide:
```
0.  Goal   → Expr
1.  Expr   → Term Expr'
2.  Expr'  → + Term Expr'
3.         | - Term Expr'
4.         | ε
5.  Term   → Factor Term'
6.  Term'  → * Factor Term'
7.         | / Factor Term'
8.         | ε
9.  Factor → ( Expr )
10.         | number
11.         | id
```

**FIRST (slide, calcolati "dal basso"):** `FIRST(F) = FIRST(T) = FIRST(E) = FIRST(Goal) = {(, id, num}` (F non nullificabile); `FIRST(E') = {+, -, ε}`; `FIRST(T') = {*, /, ε}`.

**FOLLOW (slide, passo-passo):**
*   `FOLLOW(E) = {$, )}` (start symbol; E compare in `F → (E)`);
*   `FOLLOW(E') = FOLLOW(E) = {$, )}` (E' è ultimo in `E → T E'` e in `E' → + T E'`);
*   `FOLLOW(T) = FIRST(E')\{ε} ∪ FOLLOW(E) ∪ FOLLOW(E') = {+, -, $, )}` (E' nullificabile);
*   `FOLLOW(T') = FOLLOW(T) = {+, -, $, )}`;
*   `FOLLOW(F) = FIRST(T')\{ε} ∪ FOLLOW(T) ∪ FOLLOW(T') = {*, /, +, -, $, )}` (T' nullificabile).

**Tabella di parsing LL(1) (slide):**

| NT \ T | + | − | * | / | id | num | ( | ) | $ |
|---|---|---|---|---|---|---|---|---|---|
| **Goal** | | | | | 0 | 0 | 0 | | |
| **Expr** | | | | | 1 | 1 | 1 | | |
| **Expr'** | 2 | 3 | | | | | | 4 | 4 |
| **Term** | | | | | 5 | 5 | 5 | | |
| **Term'** | 8 | 8 | 6 | 7 | | | | 8 | 8 |
| **Factor** | | | | | 10 | 9 | 11 | | |

Nessuna cella contiene più di una produzione ⇒ **grammatica LL(1)**.

### 4.6 Skeleton Parser LL(1) (table-driven)
```
word ← NextWord()
push $ onto Stack              // la pila traccia la frontiera del parse tree
push the start symbol S onto Stack
TOS ← top of Stack
loop forever
    if TOS = $ and word = EOF then
        break & report success
    else if TOS is a terminal then
        if TOS matches word then
            pop Stack;  word ← NextWord()
        else report error looking for TOS
    else                              // TOS è un non-terminale
        if TABLE[TOS, word] = A → B1B2…Bk then
            pop Stack
            push Bk, Bk−1, …, B1      // in quest'ordine
        else break & report error expanding TOS
    TOS ← top of Stack
```

#### ✴️ Esercizio d'Esame: La grammatica begin-end
Consideriamo la grammatica formale proposta nelle slide ufficiali d'esame:
1.  $P \rightarrow begin\ L\ end$
2.  $L \rightarrow ST$
3.  $T \rightarrow ST \mid \epsilon$
4.  $S \rightarrow id := E; \mid read(id); \mid write(E);$
5.  $E \rightarrow FG$
6.  $G \rightarrow + FG \mid \epsilon$
7.  $F \rightarrow (E) \mid id$

> **TODO (esercizio da svolgere):** la soluzione **non** è presente nelle slide. Si richiede di: (1) calcolare gli insiemi FIRST per ogni simbolo (partire dai non-terminali "foglia" $F$ e $G$ e risalire: $E$, $S$, $L$, $T$, $P$); (2) calcolare gli insiemi FOLLOW ($\$ \in FOLLOW(P)$; attenzione ai non-terminali nullificabili $T$ e $G$, le cui produzioni $\epsilon$ ereditano FOLLOW); (3) derivare $\text{FIRST}^+$ per tutte le produzioni; (4) costruire la tabella di parsing $M[A, t]$ e verificare la condizione LL(1) (nessuna cella con più di una produzione).


#### ✴️ Esercizio d'Esame: grammatica con nullificabili (slide)
Costruire la tabella per parser discendente per:
```
S → AB | eDa
A → ab | c
B → dC
C → eC | g
D → fD | g
```
> **TODO (esercizio da svolgere):** la soluzione **non** è presente nelle slide. Calcolare FIRST e FOLLOW per ogni simbolo, derivare FIRST$^+$ e costruire la tabella LL(1) verificando che nessuna cella contenga più di una produzione.

<a id="cap5"></a>
## CAPITOLO 5: Parsing Bottom-Up e Tabelle LR(1)
**Sources:** *Bottom_up_Parsing.pdf / TableConstruction.pdf*

### 5.1 Principio dello Shift-Reduce
*   Il parsing bottom-up tenta di ricostruire una derivazione rightmost procedendo all'indietro (bottom-up), partendo dalle foglie e risalendo verso la radice (Goal) [Bottom_up_Parsing.pdf, Slide 3, 1, 2].
*   **Definizione di Manico (Handle):** Data una forma sentenziale destra $\beta$ in $\alpha \beta w$ (dove $w$ contiene solo terminali), si definisce *handle* la sottostringa più a sinistra che corrisponde alla parte destra di una produzione valida $A \rightarrow \beta$, tale che la sostituzione di $\beta$ con $A$ rappresenti un passo corretto nella riduzione all'indietro della derivazione [Bottom_up_Parsing.pdf, Slide 5, 2, 3].
*   **La Pila Semantica e le 4 Azioni Fondamentali:**
    L'automa a pila per il parsing bottom-up memorizza sulla pila coppie del tipo `(simbolo, stato)` ed esegue quattro azioni guidate dalle tabelle ACTION e GOTO [Bottom_up_Parsing.pdf, Slide 8, 5]:
    1.  **Shift $s_i$:** Spinge il token di input corrente e lo stato associato $s_i$ sulla pila, leggendo il token successivo dallo scanner [Bottom_up_Parsing.pdf, Slide 8, 5].
    2.  **Reduce $A \rightarrow \beta$:** Rileva il manico sulla sommità della pila, estrae $2 \cdot |\beta|$ elementi (coppie simbolo-stato), e inserisce sulla pila il non-terminale di sinistra $A$ e il nuovo stato determinato tramite la tabella GOTO\[$s_{top}$, $A$] [Bottom_up_Parsing.pdf, Slide 8, 5].
    3.  **Accept:** Dichiara il successo del parsing se sulla pila rimane solo il simbolo iniziale e lo scanner ha raggiunto la fine del file [Bottom_up_Parsing.pdf, Slide 8, 5].
    4.  **Error:** Solleva un'eccezione se nessuna azione legale è definita nelle tabelle per lo stato e il token correnti [Bottom_up_Parsing.pdf, Slide 8, 5].

*   **Definizione formale (coppia, slide):** un handle di una forma sentenziale destra $\gamma$ è la coppia $\langle A \to \beta, k \rangle$ con $A \to \beta \in P$ e $k$ = posizione in $\gamma$ del simbolo **più a destra** di $\beta$; sostituire $\beta$ in posizione $k$ con $A$ produce la forma sentenziale da cui $\gamma$ deriva nella derivazione rightmost. **Proprietà:** poiché $\gamma$ è right-sentential, a destra di un handle ci sono **soli terminali**.
*   **Teorema (unicità dell'handle, slide):** se $G$ è non ambigua, ogni forma sentenziale destra ha un handle unico. Bozza: $G$ non ambigua ⇒ derivazione rightmost unica ⇒ unica produzione applicata ⇒ unica posizione ⇒ unica coppia $\langle A \to \beta, k \rangle$. ∎
*   **Attenzione (slide):** trovare un rhs che fa match **non basta**. Con `Goal → aABe;  A → Abc | b;  B → d` e input `abbcde`, il primo handle riduce il **primo** `b` (posizione 2, regola `A → b`): `abbcde → aAbcde → aAde → aABe → Goal`.
### 5.2 Gli Item LR e gli Algoritmi di Chiusura
*   **Definizione di Item LR(1):** Un item LR(1) è una coppia ordinata:
    $$[A \rightarrow \beta \bullet \gamma, a]$$
    dove $A \rightarrow \beta\gamma$ è una produzione e $a \in T \cup \{\$\}$ è un simbolo terminale di lookahead [TableConstruction.pdf, Slide 12, 6.1].
    *   Il punto $\bullet$ indica lo stato di avanzamento del parser: ciò che si trova a sinistra è stato riconosciuto, ciò che è a destra è atteso [TableConstruction.pdf, Slide 12, 6.1].
    *   L'item $[A \rightarrow \beta \bullet, a]$ indica che il parser ha riconosciuto l'intera riga destra $\beta$ e deve ridurre a $A$, ma solo se il simbolo di lookahead corrente è esattamente $a$ [TableConstruction.pdf, Slide 12, 6.1].
*   **Algoritmo di Punto Fisso CLOSURE(I):**
    Consente di completare un insieme di item includendo tutte le possibili produzioni attese.
    ![[Pasted image 20260825175633.png]]
    [TableConstruction.pdf, Slide 15, 6.2].
*   **Algoritmo GOTO(I, X):**
    Rappresenta la transizione dall'insieme di item $I$ dopo aver letto il simbolo grammaticale $X$ (terminale o non-terminale).
    
    ![[Pasted image 20260825175550.png]]
    $$\text{GOTO}(I, X) = \text{CLOSURE}(\{ [A \rightarrow \beta X \bullet \gamma, a] \mid [A \rightarrow \beta \bullet X \gamma, a] \in I \})$$
    [TableConstruction.pdf, Slide 15, 6.2].
*   **Collezione Canonica degli Insiemi di Item LR(1):**
    Si costruisce l'insieme di tutti gli stati dell'automa del parser calcolando la chiusura dello stato iniziale aumentato $[S' \rightarrow \bullet S, \$]$ e applicando ripetutamente GOTO su ciascun simbolo grammaticale fino al raggiungimento del punto fisso [TableConstruction.pdf, Slide 15].

### 5.3 Riempimento delle Tabelle ACTION e GOTO
*   **Regole di Popolamento delle Tabelle:**
    Per ciascuno stato $i$ (corrispondente all'insieme di item $I_i$):
    *   Se $[A \rightarrow \beta \bullet a \gamma, b] \in I_i$ e $\text{GOTO}(I_i, a) = I_j$ (con $a$ terminale), allora imposta $\text{ACTION}[i, a] = \text{Shift } j$ [TableConstruction.pdf, Slide 15].
    *   Se $[A \rightarrow \beta \bullet, a] \in I_i$, imposta $\text{ACTION}[i, a] = \text{Reduce } A \rightarrow \beta$ (escluso il caso di $S'$) [TableConstruction.pdf, Slide 15].
    *   Se $[S' \rightarrow S \bullet, \$] \in I_i$, imposta $\text{ACTION}[i, \$] = \text{Accept}$ [TableConstruction.pdf, Slide 15].
    *   Se $\text{GOTO}(I_i, A) = I_j$ (con $A$ non-terminale), imposta $\text{GOTO}[i, A] = j$ [TableConstruction.pdf, Slide 15].
*   **Risoluzione dei Conflitti:**
    *   **Conflitto Shift/Reduce:** Si verifica se una cella contiene sia un'azione di shift sia una di reduce. Viene tipicamente risolto assegnando priorità allo shift (come nel caso del dangling-else) [TableConstruction.pdf, Slide 22, 6.3].
    *   **Conflitto Reduce/Reduce:** Si verifica se una cella contiene due diverse riduzioni accettabili sullo stesso lookahead. Indica che la grammatica è ambigua e deve essere modificata strutturalmente [TableConstruction.pdf, Slide 22, 6.3].

### 5.4 Tracce d'Esame Svolte
#### Esempio 0: parsing shift-reduce di `x - 2 * y` (slide)
Grammatica classica left-recursive (`Goal → Expr`; `Expr → Expr + Term | Expr - Term | Term`; `Term → Term * Factor | Term / Factor | Factor`; `Factor → number | id | ( Expr )`), input `id - num * id`:

| Pila | Input | Handle | Azione |
|---|---|---|---|
| `$` | `id - num * id` | nessuno | shift |
| `$ id` | `- num * id` | 8,1 | reduce 8 (`Factor → id`) |
| `$ Factor` | `- num * id` | 6,1 | reduce 6 (`Term → Factor`) |
| `$ Term` | `- num * id` | 3,1 | reduce 3 (`Expr → Term`) |
| `$ Expr` | `- num * id` | nessuno | **shift — Expr qui NON è un handle** (non occorre in questo punto di una derivazione rightmost di `id - num * id`) |
| `$ Expr -` | `num * id` | nessuno | shift |
| `$ Expr - num` | `* id` | 7,3 | reduce 7 (`Factor → number`) |
| `$ Expr - Factor` | `* id` | 6,3 | reduce 6 |
| `$ Expr - Term` | `* id` | nessuno | shift |
| `$ Expr - Term *` | `id` | nessuno | shift |
| `$ Expr - Term * id` | | 8,5 | reduce 8 |
| `$ Expr - Term * Factor` | | 4,5 | reduce 4 (`Term → Term * Factor`) |
| `$ Expr - Term` | | 2,3 | reduce 2 (`Expr → Expr - Term`) |
| `$ Expr` | | 0,1 | reduce 0 (`Goal → Expr`) |
| `$ Goal` | | — | **accept** |

5 shift + 9 reduce + 1 accept; il parse tree corrispondente è `x − (2 * y)`. Morale: **matchare un rhs ≠ avere l'handle**; servono contesto sinistro (gli stati) e lookahead ⇒ LR(1).

#### Esempio 1: Grammatica SheepNoise
Consideriamo la grammatica formale dei belati di una pecora [Bottom_up_Parsing.pdf, Slide 5 / 3]:
1.  $Goal \rightarrow SheepNoise$
2.  $SheepNoise \rightarrow SheepNoise\ baa$
3.  $SheepNoise \rightarrow baa$

L'automa a pila bottom-up utilizza le seguenti tabelle d'azione e di transizione costruite dalle slide [Bottom_up_Parsing.pdf, Slide 5 / 3, 4, 5]:

##### Tabella ACTION:
```
+-------+----------+----------+
| State |   baa    |   EOF    |
+-------+----------+----------+
|   0   | shift 2  |    -     |
|   1   | shift 3  | reduce 1 |
|   2   | reduce 3 | reduce 3 |
|   3   | reduce 2 | reduce 2 |
|   4   |    -     |  accept  |
+-------+----------+----------+
```

##### Tabella GOTO:
```
+-------+------------+------+
| State | SheepNoise | Goal |
+-------+------------+------+
|   0   |     1      |  4   |
|   1   |     —      |  —   |
|   2   |     —      |  —   |
|   3   |     —      |  —   |
+-------+------------+------+
```

##### Esempio di Parsing 1 (per la stringa `baa`):
Questo tracciamento descrive passo-passo la pila del parser, l'input rimanente e l'azione intrapresa [Bottom_up_Parsing.pdf, Slide 5 / 3, 4, 5]:
1.  **Pila:** `$ s0` | **Input:** `baa EOF` | **Azione:** `shift 2` (carica il terminale e lo stato 2).
2.  **Pila:** `$ s0 baa s2` | **Input:** `EOF` | **Azione:** `reduce 3` ($SheepNoise \rightarrow baa$).
    *   *Spiegazione:* Il lato destro ha lunghezza 1 ($baa$), quindi si estraggono 2 elementi dalla pila (`baa s2`).
    *   La cima della pila temporanea è ora `s0`.
    *   Si consulta la tabella GOTO per `s0` sul non terminale `SheepNoise`: $GOTO[0, SheepNoise] = 1$.
    *   Si caricano `SheepNoise` e `s1` sulla pila.
3.  **Pila:** `$ s0 SheepNoise s1` | **Input:** `EOF` | **Azione:** `reduce 1` ($Goal \rightarrow SheepNoise$).
    *   *Spiegazione:* Si rimuovono 2 elementi (`SheepNoise s1`), cima pila `s0`.
    *   $GOTO[0, Goal] = 4$. Si caricano `Goal` e `s4`.
4.  **Pila:** `$ s0 Goal s4` | **Input:** `EOF` | **Azione:** `accept` (il parsing termina con successo).

##### Esempio di Parsing 2 (per la stringa `baa baa`):
Questo tracciamento mostra la gestione dei belati ripetuti [Bottom_up_Parsing.pdf, Slide 5 / 5, 6, 7, 8]:
1.  **Pila:** `$ s0` | **Input:** `baa baa EOF` | **Azione:** `shift 2`
2.  **Pila:** `$ s0 baa s2` | **Input:** `baa EOF` | **Azione:** `reduce 3` ($SheepNoise \rightarrow baa$).
    *   *Spiegazione:* Rimuove `baa s2`. Cima pila `s0`, $GOTO[0, SheepNoise] = 1$.
    *   La pila diventa `$ s0 SheepNoise s1`.
3.  **Pila:** `$ s0 SheepNoise s1` | **Input:** `baa EOF` | **Azione:** `shift 3` (carica `baa s3` sulla pila).
4.  **Pila:** `$ s0 SheepNoise s1 baa s3` | **Input:** `EOF` | **Azione:** `reduce 2` ($SheepNoise \rightarrow SheepNoise\ baa$).
    *   *Spiegazione:* Il lato destro ha lunghezza 2, quindi si rimuovono 4 elementi (`baa s3` e `SheepNoise s1`).
    *   La cima pila temporanea è `s0`.
    *   $GOTO[0, SheepNoise] = 1$. Si caricano `SheepNoise` e `s1`.
    *   La pila diventa `$ s0 SheepNoise s1`.
5.  **Pila:** `$ s0 SheepNoise s1` | **Input:** `EOF` | **Azione:** `reduce 1` ($Goal \rightarrow SheepNoise$).
    *   *Spiegazione:* Rimuove `SheepNoise s1`. Cima pila `s0`, $GOTO[0, Goal] = 4$.
    *   La pila diventa `$ s0 Goal s4`.
6.  **Pila:** `$ s0 Goal s4` | **Input:** `EOF` | **Azione:** `accept`.

#### Esempio 2: Grammatica dei Lookahead Critici (esercizio d'esame)
Analizziamo la grammatica complessa presentata nelle slide d'esame (TableConstruction.pdf, esercizio finale):
1.  $Start \rightarrow S$
2.  $S \rightarrow A\ a$
3.  $A \rightarrow B\ C \mid B\ C\ f$
4.  $B \rightarrow b$
5.  $C \rightarrow c$

Si augmenti la grammatica con $S' \rightarrow S$ (lookahead $\$).

> **TODO (esercizio da svolgere):** la soluzione **non** è presente nelle slide. Si richiede di: (a) costruire la collezione canonica degli insiemi di item LR(1) con Closure e GOTO a partire da $Closure(\{[S' \rightarrow \bullet S, \$]\})$ — attenzione: la closure degli item con il punto davanti ad $A$ genera anche gli item su $C$ (lookahead $a$ e $f$), e $Goto(S_0, c)$ produce lo **stesso insieme** di item di $Goto(S_3, c)$, che quindi collassano in un unico stato della collezione; (b) riempire le tabelle ACTION e GOTO con le regole di §5.3; (c) controllare i conflitti: esaminare lo stato contenente $[A \rightarrow BC \bullet, a]$ insieme a $[A \rightarrow BC \bullet f, a]$ — in LR(0) sarebbe un conflitto shift/reduce; verificare se e come il lookahead lo risolve; (d) tracciare il parsing di `bcfa` e di `bca` riportando pila, input restante e azione a ogni passo.


### 5.5 Confronto LR(k) vs LL(k) (slide)
*   **LR(k):** ogni riduzione è individuabile con il contesto sinistro **completo**, la frase da ridurre e i $k$ terminali alla sua destra.
*   **LL(k):** la produzione va scelta con il contesto sinistro e i prossimi $k$ terminali, *prima* di aver riconosciuto il corpo.

⇒ LR(k) esamina più contesto; esistono grammatiche LR(0) che non sono LL(k) per alcun $k$ (Knuth 1971; Lewis–Rosenkrantz–Stearns 1976).

| | Vantaggi | Svantaggi |
|---|---|---|
| Top-down / LL(1) | veloce, buona località, semplice, buona diagnosi d'errore | hand-coded, alta manutenzione, associatività a destra |
| LR(1) | veloce, linguaggi deterministici, automatizzabile, associatività a sinistra | working set grandi, messaggi d'errore poveri, tabelle grandi |

<a id="cap6"></a>
## CAPITOLO 6: Analisi Semantica e Sintassi Yacc
**Source:** *ContextsensitiveAnalysisv.pdf*

### 6.1 Analisi Sensibile al Contesto (Oltre la Sintassi)
*   **Limiti delle Grammatiche Context-Free:** Molte proprietà fondamentali dei linguaggi di programmazione non possono essere espresse tramite regole grammaticali context-free. Ad esempio, una grammatica Tipo 2 non può stabilire [ContextsensitiveAnalysisv.pdf, Slide 6, 31]:
    1.  Se un identificatore è stato preventivamente dichiarato o se ci sono duplicati nello stesso scope.
    2.  Quale specifica dichiarazione di `x` viene referenziata da un dato uso.
    3.  Se i tipi usati in un'espressione complessa sono mutuamente compatibili.
    4.  Se il numero di argomenti passati a una chiamata corrisponde all'arità dichiarata nella definizione della funzione.
*   **Analisi dei sei errori semantici d'esame:**
    Consideriamo il codice d'esempio delle slide ufficiali d'esame per illustrare le violazioni rilevabili unicamente tramite analisi sensibile al contesto [ContextsensitiveAnalysisv.pdf, Slide 10, 31]:
    ```c
    fie(int a, int b, int c, int d) { ... }
    fee() {
        int f[3], g[0], h, i, j, k;
        char *p;
        fie(h, i, "ab", j, k); // Errori 1 e 2
        k = f * i + j;         // Errore 3
        h = g[17];             // Errore 4
        printf("%s, %s\n", p, q); // Errore 5
        p = 10;                // Errore 6
    }
    ```
    *   **Errore 1 (Wrong number of arguments):** La chiamata a `fie` viene effettuata passando 5 parametri invece dei 4 dichiarati formalmente [ContextsensitiveAnalysisv.pdf, Slide 10, 31].
    *   **Errore 2 (Type mismatch):** Viene passata la costante stringa `"ab"` come terzo argomento, laddove la dichiarazione formale attende un intero `int c` [ContextsensitiveAnalysisv.pdf, Slide 10, 31].
    *   **Errore 3 (Invalid dimension usage):** L'array `f` (dichiarato come `int f[3]`) viene usato direttamente come scalare in un'operazione di moltiplicazione `f * i` [ContextsensitiveAnalysisv.pdf, Slide 10, 31].
    *   **Errore 4 (Array out of bounds):** Viene effettuato un accesso all'indice `g[17]` su un array dichiarato formalmente con dimensione 0 `g[0]` [ContextsensitiveAnalysisv.pdf, Slide 10, 31].
    *   **Errore 5 (Undeclared variable):** Viene tentata la stampa del valore di `q` nella `printf`, ma l'identificatore `q` non è stato mai dichiarato nello scope locale o globale [ContextsensitiveAnalysisv.pdf, Slide 10, 31].
    *   **Errore 6 (Incompatible assignment):** Viene assegnata la costante numerica intera `10` alla variabile `p` che è un puntatore a carattere `char *p` [ContextsensitiveAnalysisv.pdf, Slide 10, 31].

### 6.2 Grammatiche Attribuite (Attribute Grammars)
Le grammatiche attribuite estendono le CFG associando valori (attributi) ai simboli e definendo regole funzionali per calcolarli [ContextsensitiveAnalysisv.pdf, Slide 15].
*   **Attributi Sintetizzati (Synthesized):** Il valore dell'attributo sul nodo padre dipende unicamente dai valori degli attributi dei nodi figli nel parse tree. Vengono calcolati in una singola passata bottom-up e si integrano perfettamente con il parsing LR [ContextsensitiveAnalysisv.pdf, Slide 15, 32].
*   **Attributi Ereditati (Inherited):** Il valore sul nodo dipende dai valori dei nodi genitori o dei nodi fratelli (flusso top-down o orizzontale) [ContextsensitiveAnalysisv.pdf, Slide 15, 32].
*   **Problema della Circularità:** Una grammatica attribuita è circolare se le sue regole definiscono dipendenze cicliche tra attributi per qualche albero sintattico (es. $A$ dipende da $B$ che a sua volta dipende da $A$) [ContextsensitiveAnalysisv.pdf, Slide 22, 7.3]. Le grammatiche circolari portano a computazioni indeterminate e devono essere tassativamente evitate [ContextsensitiveAnalysisv.pdf, Slide 22, 7.3].
*   **Test SNC (Strongly Non-Circular):** Poiché rilevare la circularità generale su qualsiasi albero è un problema NP-completo (esponenziale), si utilizza la classe delle grammatiche **Strongly Non-Circular (SNC)**, testabili in tempo polinomiale, come barriera di sicurezza nei generatori di compilatori.

*   **Esempio svolto (slide): valore dei numeri binari con segno.** Grammatica
    ```
    Number → Sign List
    List   → List Bit | Bit
    Bit    → 0 | 1        Sign → + | -
    ```
    Attributi: `Number.val` (sintetizzato), `Sign.neg` (sintetizzato), `List.pos` (ereditato), `List.val` (sintetizzato), `Bit.pos` (ereditato), `Bit.val` (sintetizzato). Regole (slide):
    ```
    Number → Sign List     Number.val ← if Sign.neg then −List.val else List.val
    Sign → +               Sign.neg ← false        Sign → −      Sign.neg ← true
    List0 → List1 Bit      List0.pos ← List1.pos + 1;   Bit.pos ← List0.pos
                           List0.val ← List1.val + Bit.val
    List → Bit             List.pos ← 0;  Bit.pos ← List.pos;  List.val ← Bit.val
    Bit → 0                Bit.val ← 0              Bit → 1       Bit.val ← 2^Bit.pos
    ```
    **Valutazione di `-101` (slide):** `Sign.neg = true`; `List(pos 0).val = 5`; `List(pos 1).val = 4`; `List(pos 2).val = 4`; `Bit(pos 2)='1' → val 4`; `Bit(pos 1)='0' → val 0`; `Bit(pos 0)='1' → val 1`; `Number.val = −5`. Un ordine di valutazione coerente col grafo delle dipendenze: `List.pos, Sign.neg, Bit.pos, Bit.val, List.val, Number.val` (regola di Knuth: prima gli attributi indipendenti, poi quelli man mano disponibili). Togliendo l'albero resta il **grafo delle dipendenze**, che deve essere **aciclico**.
*   **Esempio di grammatica circolare (slide):** con `Number → List;  List → List Bit | Bit;  Bit → 0 | 1` e regole
    `List1.a ← List0.a + 1`, `List0.b ← List1.b`, `List1.c ← List1.b + Bit.val`, `List0.b ← List0.a + List0.c + Bit.val`
    si forma il ciclo **List0.b → List1.b → List1.c → List0.b**: valori indeterminati, i valutatori algorithmici falliscono. ⚠️ La circularità sta nelle **regole di attribuzione**, non nella CFG sottostante; il test di non-circularità generale è esponenziale, mentre le grammatiche **SNC** sono testabili in tempo polinomiale.
### 6.3 Traduzione Guidata dalla Sintassi Ad-Hoc (SDT) e Yacc
A causa dell'alto numero di "regole di copia" richieste dalle grammatiche attribuite formali (che aumentano drasticamente lo spazio occupato in memoria) [ContextsensitiveAnalysisv.pdf, Slide 33], i compilatori reali usano tecniche di traduzione ad-hoc [ContextsensitiveAnalysisv.pdf, Slide 25].
*   **Sintassi Yacc:** Associa snippet di codice (azioni) scritti in C a ciascuna regola della grammatica, che vengono eseguiti durante i passi di riduzione del parser [ContextsensitiveAnalysisv.pdf, Slide 25, 35].
    *   **`$$`** rappresenta l'attributo associato al non-terminale sul lato sinistro della produzione (*left-hand side*) [ContextsensitiveAnalysisv.pdf, Slide 25, 35, 7.4].
    *   **`$1, $2, ..., $n`** rappresentano i valori associati ai rispettivi simboli sul lato destro della produzione, contati da sinistra verso destra [ContextsensitiveAnalysisv.pdf, Slide 25, 35, 7.4].
*   **Pila Semantica parallela:** Per implementare questo meccanismo, il parser LR mantiene una pila semantica che opera in parallelo rispetto alla pila degli stati del parser, memorizzando i valori degli attributi [ContextsensitiveAnalysisv.pdf, Slide 25].
*   **Uso delle Symbol Table:** Invece di propagare le informazioni di scope e di tipo lungo tutto l'albero tramite regole di copia, Yacc usa una Symbol Table centralizzata globale, che memorizza i record informativi per ciascun identificatore, consentendo accessi e aggiornamenti rapidi [ContextsensitiveAnalysisv.pdf, Slide 25, 33].
*   **Esempio di Costruzione dell'AST in Yacc:**
    Utilizziamo le routine di creazione dei nodi per generare l'Abstract Syntax Tree di un'espressione aritmetica [ContextsensitiveAnalysisv.pdf, Slide 35]:
    ```yacc
    Goal   : Expr           { $$ = $1; }
    Expr   : Expr '+' Term  { $$ = MakeAddNode($1, $3); }
           | Expr '-' Term  { $$ = MakeSubNode($1, $3); }
           | Term           { $$ = $1; }
    Term   : Term '*' Factor { $$ = MakeMulNode($1, $3); }
           | Term '/' Factor { $$ = MakeDivNode($1, $3); }
           | Factor         { $$ = $1; }
    Factor : '(' Expr ')'   { $$ = $2; }
           | number         { $$ = MakeNumNode(token); }
           | ident          { $$ = MakeIdNode(token); }
    ```
    [ContextsensitiveAnalysisv.pdf, Slide 35].


*   **Emissione di ILOC (slide):** con `NextRegister()`, `Emit(op, r1, r2, r3)`, `EmitLoad(id, r) = loadAI rarp, @id, r` e `Emit(loadI, n, r)`, la traduzione di `a×2 + a×2×b` genera:
    ```
    loadAI rarp, @a, r0 ;  loadI 2, r1 ;  mult r0, r1, r2 ;
    loadAI rarp, @a, r3 ;  loadI 2, r4 ;  mult r3, r4, r5 ;
    loadAI rarp, @b, r6 ;  mult r5, r6, r7 ;  add r2, r7, r8
    ```
*   **Inizializzazione con produzione spezzata (trucco da slide):** per azzerare un costo globale si introduce `Block → Init Series` e la riduzione di `Init` esegue `cost ← 0`: si spezza una produzione **solo** per appendervi un'action.
*   **Integrazione nel parser LR (slide):** la pila memorizza **3 elementi per simbolo** (simbolo, attributo `$$`, stato); a ogni reduce si poppano $3 \cdot |\beta|$ elementi e una grande `case` sul numero di produzione calcola `$$`; `$n$` si mappa sulla locazione di pila $top - 3(n-1) - 1$. Costo: lieve aumento di tempo di parse e di spazio sulla pila.
<a id="cap7"></a>
## CAPITOLO 7: Ottimizzazione del Codice (Middle-End)
**Source:** *OptimizationI.pdf*

### 7.1 Ruolo dell'Ottimizzatore e Struttura a Passate
*   L'ottimizzatore riceve in input l'IR generata dal Front-End, analizza il codice per estrarre informazioni sul contesto d'esecuzione e riscrive l'IR in una forma più efficiente [IntroMio.pdf, Slide 73, 74, 81; OptimizationI.pdf, Slide 130].
*   **Requisiti rigorosi per le passate di ottimizzazione:**
    1.  **Safety:** La passata deve essere sicura e preservare rigorosamente il significato originario del codice; non può alterare l'output di un programma d'esecuzione corretto [OptimizationI.pdf, Slide 130, 131].
    2.  **Profitability:** La passata deve apportare un reale beneficio prestazionale (misurabile in termini di tempo di runtime, spazio occupato o consumo energetico) [OptimizationI.pdf, Slide 130, 131].
*   **Definizione di Ridondanza:** Una computazione è ridondante in un punto se il suo valore è già stato precedentemente calcolato lungo tutti i cammini che giungono a quel punto, e nessuno dei suoi operandi è stato modificato (ridefinito) lungo tali percorsi.
*   **Classificazione degli ambiti (scope) di ottimizzazione:**
    1.  **Locale:** L'ottimizzazione opera esclusivamente entro i confini di un singolo **blocco base (Basic Block)**, ovvero una sequenza di istruzioni lineari a ingresso singolo e uscita singola [OptimizationI.pdf, Slide 12; RegisterAlloc2.pdf, Slide 148].
    2.  **Regionale:** L'ottimizzazione si estende su più blocchi base, ad esempio su interi cicli (loops) o su blocchi base estesi (EBB).
    3.  **Globale / Intraprocedurale:** L'ottimizzazione analizza l'intero grafo del flusso di controllo (CFG) di una singola procedura d'esecuzione [OptimizationI.pdf, Slide 12].
    4.  **Interprocedurale:** L'analisi e l'ottimizzazione attraversano i confini di più procedure, analizzando l'intero Call Graph del programma d'esecuzione.

### 7.2 Tecniche di Ottimizzazione Locale
*   **Algoritmo di Local Value Numbering (LVN):**
    LVN mappa ciascuna espressione all'interno di un singolo blocco base su un numero identificativo univoco (il *value number*) memorizzato in una tabella hash. Se una nuova espressione produce un hash già presente in tabella, significa che il valore è già disponibile, consentendo di riscrivere l'istruzione ridondante per utilizzare direttamente il risultato precedentemente memorizzato [OptimizationI.pdf, Slide 12, 133].
*   **Estensione con identità algebriche:**
    LVN può essere potenziato per identificare e semplificare a tempo di compilazione relazioni ed identità matematiche note [OptimizationI.pdf, Slide 25, 10.1]:
    *   *Elementi neutri:* $x + 0 \rightarrow x$, $x \times 1 \rightarrow x$.
    *   *Elementi assorbenti:* $x \times 0 \rightarrow 0$.
    *   *Proprietà commutativa:* $x + y$ e $y + x$ ricevono lo stesso value number.
*   **Effetto collaterale di LVN (Register Pressure):**
    Sebbene l'eliminazione delle computazioni ridondanti riduca il numero complessivo di istruzioni, essa introduce un effetto collaterale critico: **estende il range di vitalità (*live range*) delle variabili d'appoggio** [OptimizationI.pdf, Slide 18, 10.1].
    Prendiamo l'esempio classico d'esame [OptimizationI.pdf, Slide 18, 133]:
    ```iloc
    a <- b + c
    b <- a - d
    c <- b + c
    d <- a - d  // Ottimizzato tramite LVN in: d <- b
    ```
    Avendo ottimizzato l'operazione `a - d` alla riga 4 sfruttando il valore precedentemente calcolato alla riga 2 e memorizzato in `b`, costringiamo la variabile `b` a rimanere "viva" fino alla riga 4 [OptimizationI.pdf, Slide 18]. Se non avessimo ottimizzato, `b` sarebbe morta subito dopo la riga 3. Questa estensione della vitalità aumenta la richiesta di registri simultanei (pressione sui registri), forzando l'allocatore ad effettuare operazioni di scaricamento in memoria (*spill*), il che può vanificare l'ottimizzazione prestazionale [OptimizationI.pdf, Slide 18].

*   **Esempio con value numbers (slide):**

    | Originale | Con VN | Riscritto |
    |---|---|---|
    | `a ← b + c` | `a₃ ← b₁ + c₂` | `a ← b + c` |
    | `b ← a - d` | `b₅ ← a₃ - d₄` | `b ← a - d` |
    | `c ← b + c` | `c₆ ← b₅ + c₂` | `c ← b + c` |
    | `d ← a - d` | `d₅ ← a₃ - d₄` | **`d ← b`** |

*   **Edge case: il naming (slide).**

    | Originale | Con VN | Riscritto |
    |---|---|---|
    | `a ← x + y` | `a₃ ← x₁ + y₂` | `a₃ ← x₁ + y₂` |
    | `b ← x + y` | `b₃ ← x₁ + y₂` | `b₃ ← a₃` |
    | `a ← 17` | `a₄ ← 17` | `a₄ ← 17` |
    | `c ← x + y` | `c₃ ← x₁ + y₂` | `c₃ ← a₃` **(oops!)** |

    L'ultima riscrittura è **sbagliata** (`a` è stata ridefinita): serve un mapping VN → nome corrente, oppure il **renaming alla SSA** (nomi unici per valore: $a^0_3, a^1_4, \dots$), dopo cui la riscrittura funziona. Con gli **assegnamenti indiretti** (`*p ← 0`) il compilatore non isola la locazione (**riferimento ambiguo**): serve pointer analysis, altrimenti si invalida in modo conservativo.
*   **Algoritmo LVN completo (slide):** per ogni $T_i \leftarrow L_i\ Op_i\ R_i$: (1) VN di $L_i, R_i$; (2) **constant folding** se entrambi costanti; (3) **identità algebriche** ($x+0,\ x{\times}1,\ x{\times}0,\ x{-}x,\ x{\div}x,\ \max(x,x), \dots$) → copy/assignment; (4) **commutatività**: se $Op_i$ commuta e $V_1 > V_2$, scambia (ordine canonico); (5) hash $\langle V_1, Op_i, V_2 \rangle$: se presente → copy con il VN noto, altrimenti nuovo VN.
### 7.3 Ottimizzazioni Tipiche
*   **Constant Folding:** Valuta a tempo di compilazione le operazioni tra costanti note (es. `2 + 3` diventa direttamente `5`) [IntroCodeGeneration.pdf, Slide 52; OptimizationI.pdf, Slide 12, 132].
*   **Copy Propagation:** Se è presente un assegnamento di copia `x <- y`, sostituisce gli usi successivi di `x` direttamente con `y` per eliminare l'istruzione di copia.
*   **Loop-Invariant Code Motion (LICM):** Identifica computazioni costanti all'interno di un ciclo (i cui operandi non cambiano tra le iterazioni) e le sposta all'esterno del ciclo (nel *pre-header*), riducendone i tempi complessivi di esecuzione [OptimizationI.pdf, Slide 12, 132].
*   **Dead Code Elimination (DCE):** Individua ed elimina le istruzioni che calcolano valori che non verranno mai utilizzati in futuro lungo alcun percorso del flusso di controllo [OptimizationI.pdf, Slide 12, 132].


### 7.4 Oltre il Blocco: EBB e Loop Unrolling (slide)
*   **CFG d'esempio (slide):** blocchi $A \dots G$ con $E = \{(A,B),(A,C),(B,G),(C,D),(C,E),(D,F),(E,F),(F,E)\}$, $|N|=7$, $|E|=8$. LVN trova le ridondanze intra-blocco (`m←a+b; n←a+b` in A) ma **perde** quelle cross-blocco (`a+b` in A, C, F, G; `c+d` in B, C, E, F, G; `e+f` in D, E, F).
*   **Extended Basic Block (EBB):** insieme massimale di blocchi $B_1 \dots B_n$ dove ogni $B_i$ ($i>1$) ha **esattamente un predecessore, interno all'EBB**. Nell'esempio $\{A,B,C,D,E\}$ è un EBB con 3 cammini: $(A,B)$, $(A,C,D)$, $(A,C,E)$; $\{F\}$ e $\{G\}$ sono EBB degeneri. **Superlocal value numbering:** applica LVN ai cammini degli EBB con hash table **scoped** (inizializzata dal padre; i **kill** — ridefinizioni di nomi — richiedono il ripristino del mapping VN→nome all'uscita dallo scope).
*   **Loop unrolling (slide):**
    1.  *completo* (bounds fissi, poche iterazioni): il loop diventa codice rettilineo — sempre sicuro se i bounds sono giusti;
    2.  *per fattore* (es. 4): `do i=1 to 100 by 4: a(i); a(i+1); a(i+2); a(i+3) end` — test e branch ridotti del 25%;
    3.  *bounds ignoti — guard loop:* loop principale `do while (i+3 < n) …; i ← i+4 end` + loop di coda `do while (i < n) …; i ← i+1 end`;
    4.  *unroll-and-rename:* per `a(i) = a(i) + b(i) + b(i-1)` l'unroll by 2 con renaming elimina le copie `t1 ← t2` a fine loop (artefatto di naming).

    ⚠️ **Rischi (slide):** crescita del codice; maggiore domanda di registri; se gli spill risultanti generano più traffico di memoria del beneficio ottenuto, l'ottimizzazione è controproducente.

<a id="cap8"></a>
## CAPITOLO 8: Il Framework Dataflow
**Sources:** *Data-FlowFirst.pdf / Data-Flow2.pdf*

### 8.1 Fondamenti Matematici dell'Analisi del Flusso di Dati
*   L'analisi dataflow raccoglie informazioni statiche sul comportamento a runtime del programma risolvendo sistemi di equazioni ricorsive sul Control Flow Graph (CFG) [Data-FlowFirst.pdf, Slide 12; Data-Flow2.pdf, Slide 12].
*   **Teoria dei Reticoli (Lattices):** Ciascuna analisi modella le proprietà come elementi di un reticolo parzialmente ordinato (CPO).
    *   L'operatore di combinazione dei rami è il **Join Semilattice (\(\sqcup\))** o il **Meet Semilattice (\(\sqcap\))**, che definisce il limite superiore/inferiore comune [Data-Flow2.pdf, Slide 12, 43].
    *   **Teorema di Kleene (Fixed Point):** Garantisce che, se la funzione di trasferimento associata alle equazioni di flusso è monotona su un dominio finito con elementi di minimo e massimo ($\perp$ e $\top$), l'algoritmo iterativo convergerà necessariamente e in modo stabile verso un unico punto fisso stabile [Data-Flow2.pdf, Slide 12, 43].

### 8.2 Classificazione del Framework Unificato
Ciascuna analisi del flusso di dati viene categorizzata in modo univoco sulla base di due caratteristiche geometriche e insiemistiche fondamentali [Data-Flow2.pdf, Slide 18, 12.1]:

1.  **Direzione (Direction):**
    *   **Forward (In avanti):** L'informazione si propaga seguendo la direzione d'esecuzione del codice (dagli ingressi dei blocchi verso le uscite) [Data-Flow2.pdf, Slide 18, 12.1].
    *   **Backward (All'indietro):** L'informazione risale la corrente d'esecuzione, partendo dall'uscita del programma verso i blocchi d'ingresso [Data-Flow2.pdf, Slide 18, 12.1].
2.  **Operatore di Merge (Combinazione):**
    *   **May (Possibile / Unione \(\cup\)):** La proprietà vale se è vera lungo *almeno uno* dei cammini che convergono nel punto. Si associa all'operazione insiemistica di unione [Data-Flow2.pdf, Slide 18, 12.1].
    *   **Must (Definito / Intersezione \(\cap\)):** La proprietà deve valere *su tutti* i cammini d'esecuzione che giungono al punto. Si associa all'operazione di intersezione [Data-Flow2.pdf, Slide 18, 12.1].

**Catalogo delle quattro analisi (slide):**

| | **May** ($\cup$) — vale su *qualche* cammino | **Must** ($\cap$) — vale su *tutti* i cammini |
|---|---|---|
| **Forward** | Reaching Definitions | Available Expressions |
| **Backward** | Live Variables | Very Busy Expressions |

**Schema comune (slide):** $A[n] = \bigwedge_{m \in N(n)} B[m]$, $\; B[n] = f_n(A[n])$, con $N(n) = PRED$ o $SUCC$ e $\bigwedge = \cup$ (may) o $\cap$ (must): un unico algoritmo iterativo generico, istanziabile per ogni analisi.

### 8.3 Analisi Classiche e Relazioni GEN/KILL
*   **Live Variables (Liveness Analysis):**
    *   *Classificazione:* Backward + May (Unione) [Data-FlowFirst.pdf, Slide 12; Data-Flow2.pdf, Slide 12, 12.1].
    *   *Scopo:* Determinare se il valore memorizzato in una variabile verrà letto in futuro prima che la variabile stessa venga sovrascritta [Data-FlowFirst.pdf, Slide 12; Data-Flow2.pdf, Slide 37]. Se non è viva, la variabile è "morta" e l'assegnamento associato può essere rimosso (Dead Code Elimination) [Data-FlowFirst.pdf, Slide 12, 46].
    *   *Equazioni di flusso:*
        $$in[n] = use[n] \cup (out[n] \setminus def[n])$$
        $$out[n] = \bigcup_{m \in post[n]} in[m]$$
        [Data-FlowFirst.pdf, Slide 12; Data-Flow2.pdf, Slide 12, 11.1].
*   **Reaching Definitions:**
    *   *Classificazione:* Forward + May (Unione) [Data-Flow2.pdf, Slide 18, 12.1].
    *   *Scopo:* Trovare quali definizioni (assegnamenti a variabili) attive arrivano a un dato punto d'esecuzione senza essere sovrascritte.
*   **Available Expressions (AE):**
    *   *Classificazione:* Forward + Must (Intersezione) [Data-Flow2.pdf, Slide 18, 44, 12.1].
    *   *Scopo:* Identificare se un'espressione matematica è già stata calcolata lungo tutti i percorsi precedenti ed è ancora valida (consente l'eliminazione delle sottoespressioni comuni - CSE) [Data-Flow2.pdf, Slide 18, 44, 12.1].
    *   *Equazioni:*
        $$in[n] = \bigcap_{q \in pre[n]} out[q]$$
        $$out[n] = gen[n] \cup (in[n] \setminus kill[n])$$
        [Data-Flow2.pdf, Slide 43].
*   **Very Busy Expressions (VBE):**
    *   *Classificazione:* Backward + Must (Intersezione) [Data-Flow2.pdf, Slide 18, 44, 45, 12.1].
    *   *Scopo:* Individuare se un'espressione verrà sicuramente calcolata in futuro a prescindere dal ramo d'esecuzione scelto, consentendo di anticiparne il calcolo (expression hoisting) per risparmiare spazio [Data-Flow2.pdf, Slide 44, 45].
    *   *Equazioni di flusso:*
        $$out[n] = \begin{cases} \emptyset & \text{se } n \text{ è un nodo finale} \\ \bigcap_{q \in post[n]} in[q] & \text{altrimenti} \end{cases} \qquad in[n] = gen[n] \cup (out[n] \setminus kill[n])$$
        con $kill[n] = kill_{AE}(n)$ (espressioni contenenti variabili ridefinite in $n$) mentre $gen[n] = gen_{VB}(n) \neq gen_{AE}(n)$: un'espressione è VB-generata se **valutata** in $n$ (es. $x := x + 1$ genera $x+1$ per VBE ma nulla per AE).

### 8.4 La Regola d'Oro dell'Inizializzazione
La stabilità e la correttezza matematica del calcolo del punto fisso dipendono strettamente dall'inizializzazione corretta dei set all'inizio delle iterazioni [Data-Flow2.pdf, Slide 22, 12.2]:
*   **Nei sistemi May (unione \(\cup\)):** Tutti i set `IN` e `OUT` (ad eccezione dei blocchi di ingresso) devono essere inizializzati al **set vuoto (\(\emptyset\))**. In questo modo, l'algoritmo risale dal basso verso l'alto (least fixed point) [Data-Flow2.pdf, Slide 22, 12.2].
*   **Nei sistemi Must (intersezione \(\cap\)):** Tutti i set devono essere inizializzati al **set universale (\(\mathcal{U}\))**. Se si inizializzasse erroneamente al set vuoto, l'operazione di intersezione iniziale con l'insieme vuoto continuerebbe a produrre il vuoto ad ogni passo ("avvelenamento da intersezione"), facendo collassare l'intero sistema a $\emptyset$ [Data-Flow2.pdf, Slide 22, 12.2].
*   **Condizioni al bordo (boundary conditions):** alcuni set sono imposti a priori e non partecipano all'iterazione: per le analisi *forward* il nodo iniziale riceve un valore fissato (RD: $\iota = \{(x,?) \mid x \in Vars\}$, le definizioni "non ancora inizializzate"; AE: $\emptyset$); per le analisi *backward* i nodi finali hanno $out = \emptyset$ (sia LV che VBE).

### 8.5 Algoritmi Iterativi d'Esame: Esercizio di Liveness Svolto
Consideriamo l'algoritmo iterativo applicato al CFG strutturato con un ciclo proposto nelle slide d'esame [Data-FlowFirst.pdf, Slide 20; Data-Flow2.pdf, Slide 42]:
*   **CFG d'Esempio:**
    *   *Blocco 1:* `a := 0;` ($def=\{a\}$)
    *   *Blocco 2:* `b := a + 1;` ($use=\{a\}$, $def=\{b\}$)
    *   *Blocco 3:* `c := c + b;` ($use=\{b, c\}$, $def=\{c\}$)
    *   *Blocco 4:* `a := b * 2;` ($use=\{b\}$, $def=\{a\}$)
    *   *Blocco 5:* `a < N;` ($use=\{a\}$, loop-back su Blocco 2, uscita su Blocco 6)
    *   *Blocco 6:* `return c;` ($use=\{c\}$)

*   **L'impatto dell'ordine di visita (Ordering):**
    Poiché l'analisi di liveness è un'analisi *Backward*, l'ordine ottimale di elaborazione dei blocchi è l'inverso dell'ordine d'esecuzione (visita da 6 a 1, ovvero in *reverse post-order*) [Data-FlowFirst.pdf, Slide 20; Data-Flow2.pdf, Slide 42].
    *   Eseguendo la visita dei nodi nell'ordine backward **(da 6 a 1)**, l'algoritmo propaga immediatamente i set riga per riga e raggiunge la convergenza completa al punto fisso in soli **3 passi d'iterazione** [Data-FlowFirst.pdf, Slide 20; Data-Flow2.pdf, Slide 42].
    *   Se si eseguisse erroneamente l'analisi nell'ordine sequenziale forward (da 1 a 6), sarebbero necessarie ben **7 iterazioni** per far risalire l'informazione del loop a ritroso, sprecando tempo computazionale.

#### Tabella Finale di Convergenza d'Esame (Liveness):

| Block |  use   | def | in (Iter 1) | out (Iter 1) | in (Iter 2) | out (Iter 2) | in (Iter 3) | out (Iter 3) |
| :---: | :----: | :-: | :---------: | :----------: | :---------: | :----------: | :---------: | :----------: |
| **6** |  {c}   |     |     {c}     | $\emptyset$  |     {c}     | $\emptyset$  |     {c}     | $\emptyset$  |
| **5** |  {a}   |     |   {a, c}    |    {a, c}    |   {a, c}    |    {a, c}    |   {a, c}    |    {a, c}    |
| **4** |  {b}   | {a} |   {b, c}    |    {a, c}    |   {b, c}    |    {a, c}    |   {b, c}    |    {a, c}    |
| **3** | {b, c} | {c} |   {b, c}    |    {b, c}    |   {b, c}    |    {b, c}    |   {b, c}    |    {b, c}    |
| **2** |  {a}   | {b} |   {a, c}    |    {b, c}    |   {a, c}    |    {b, c}    |   {a, c}    |    {b, c}    |
| **1** |        | {a} |     {c}     |    {a, c}    |     {c}     |    {a, c}    |     {c}     |    {a, c}    |

[Data-FlowFirst.pdf, Slide 20; Data-Flow2.pdf, Slide 42].

*Ogni colonna "Iter $k$" è il risultato del $k$-esimo sweep **backward** (visita $6 \to 1$, con $out[n]$ calcolato prima di $in[n]$); tra Iter 2 e Iter 3 nessun set cambia più, quindi l'algoritmo è convergenza al punto fisso (least fixed point, iterazione partita da $\bot$).*


### 8.6 Esercizio Svolto: Reaching Definitions fino alla Convergenza (slide)
Programma fattoriale: `1: input n;   2: m := 1;   3: n > 1 ?;   4: m := m*n;   5: n := n-1;   6: output m`, archi $1 \to 2 \to 3$, $3 \to 4 \to 5 \to 3$ (back-edge), $3 \to 6$.

**gen/kill (slide):**

| $p$ | $kill_{RD}[p]$ | $gen_{RD}[p]$ |
|---|---|---|
| 1 | (n,?) | (n,1) |
| 2 | (m,?)(m,2) | (m,2) |
| 3 | $\emptyset$ | $\emptyset$ |
| 4 | (m,?)(m,2)(m,4) | (m,4) |
| 5 | (n,?)(n,1)(n,5) | (n,5) |
| 6 | $\emptyset$ | $\emptyset$ |

**Equazioni (forward, may):** $RDentry(p) = \iota = \{(x,?) \mid x \in Vars\}$ se $p$ è iniziale, altrimenti $\bigcup \{RDexit(q) \mid q \in pre[p]\}$; $\quad RDexit(p) = (RDentry(p) - kill_{RD}[p]) \cup gen_{RD}[p]$.

**Iterazione 1 (slide):**
```
RDentry(1)={(n,?),(m,?)}   RDexit(1)={(n,?),(m,?)}
RDentry(2)={(n,?),(m,?)}   RDexit(2)={(n,?),(m,2)}
RDentry(3)={(n,?),(m,2)}   RDexit(3)={(n,?),(m,2)}
RDentry(4)={(n,?),(m,2)}   RDexit(4)={(n,?),(m,4)}
RDentry(5)={(n,?),(m,4)}   RDexit(5)={(n,5),(m,4)}
RDentry(6)={(n,?),(m,2)}   RDexit(6)={(n,?),(m,2)}
```
**Iterazione 2 (slide):** il back-edge $5 \to 3$ porta $(n,5),(m,4)$ dentro il loop:
```
RDentry(3)=RDexit(3)={(n,?),(m,2),(n,5),(m,4)}
RDentry(4)=stesso set      RDexit(4)={(n,?),(n,5),(m,4)}
RDentry(5)={(n,?),(n,5),(m,4)}   RDexit(5)={(n,5),(m,4)}
RDentry(6)=RDexit(6)={(n,?),(m,2),(n,5),(m,4)}
```
Iterazione 3 = Iterazione 2 ⇒ **punto fisso** (least fixed point, iterazione partita da $\bot$).

**Lettura (slide):** in $RDentry(3)$ coesistono $(m,2)$ e $(m,4)$ ⇒ $m$ **non è costante** nel loop; $(n,?)$ non muore mai ⇒ $n$ *potrebbe* essere usato non inizializzato (warning). **Applicazione — loop-invariant code motion:** se per ogni $y \in vars(exp)$ le definizioni che raggiungono l'entry del loop coincidono con quelle che raggiungono il punto $n$, allora `x := exp` può essere issato **prima** del loop (slide: `x = y+z` con `y:=3; z:=5` fuori dal for ⇒ hoisted).

<a id="cap9"></a>
## CAPITOLO 9: Astrazione delle Procedure e Gestione della Memoria
**Source:** *TheProcedureAbstraction.pdf*

### 9.1 Le Tre Astrazioni delle Procedure
La procedura è l'astrazione fondamentale per rendere gestibili e modulari i software di grandi dimensioni [TheProcedureAbstraction.pdf, Slide 152]. Offre tre astrazioni principali:
1.  **Astrazione di Controllo:** Consente un unico punto di ingresso e uscita ordinato, con passaggio controllato dei parametri e gestione del flusso di ritorno [TheProcedureAbstraction.pdf, Slide 154, 155].
2.  **Namespace pulito (Scoping):** Ogni procedura eredita uno spazio di nomi isolato. Le variabili locali sono visibili solo all'interno del proprio blocco d'esecuzione, e lo *shadowing* permette di oscurare variabili omonime dichiarate negli scope esterni [TheProcedureAbstraction.pdf, Slide 154].
3.  **Interfaccia Uniforme e Compilazione Separata:** Permette a parti distinte del software di essere scritte, compilate in anticipo ed ottimizzate in modo indipendente, venendo poi unite durante la fase di collegamento (*linking*) [TheProcedureAbstraction.pdf, Slide 154].

### 9.2 Record di Attivazione (Activation Record - AR)
Poiché le procedure possono essere invocate ricorsivamente, lo spazio per le variabili locali non può essere assegnato in modo statico a tempo di compilazione. Ogni singola invocazione della procedura richiede la creazione a runtime di un **Record di Attivazione** (chiamato anche *Stack Frame* o *Activation Record*) [TheProcedureAbstraction.pdf, Slide 12, 153].
*   **Struttura standard di un AR:**
    *   *Parametri attuali:* Valori o indirizzi passati alla routine chiamante [TheProcedureAbstraction.pdf, Slide 12, 9.1].
    *   *Area di salvataggio dei registri:* Utilizzata per preservare i registri fisici dell'hardware [TheProcedureAbstraction.pdf, Slide 12, 9.1].
    *   *Valore di ritorno:* Spazio allocato per memorizzare il risultato calcolato dalla funzione [TheProcedureAbstraction.pdf, Slide 12, 9.1].
    *   *Indirizzo di ritorno:* La posizione nel codice in cui riprendere l'esecuzione nel chiamante [TheProcedureAbstraction.pdf, Slide 12, 9.1].
    *   *Puntatore del chiamante (Caller's ARP):* Indirizzo dell'AR precedente per ripristinare il frame del chiamante al termine [TheProcedureAbstraction.pdf, Slide 12, 9.1].
    *   *Variabili Locali e Spill:* Spazio allocato per le variabili locali della procedura e per accogliere i registri virtuali "scaricati" in memoria dall'allocatore (*spills*) [TheProcedureAbstraction.pdf, Slide 12, 9.1].
*   **Activation Record Pointer (ARP):** Pointed to by register `rarp` in ILOC [TheProcedureAbstraction.pdf, Slide 15, 9.1]. Tutte le variabili locali sono referenziate staticamente tramite la formula **`rarp + offset`** [TheProcedureAbstraction.pdf, Slide 15, 9.1].

*   **Layout standard dell'AR (slide):**
    ```
    +------------------------------+ ▲
    | parameters                   | | parametri per la routine corrente
    | register save area           | | registri salvati
    | return value                 | | valore di ritorno (se funzione)
    | return address               | | indirizzo di ripresa del chiamante
    | access link                  | | supporto all'accesso non-locale
    | caller's ARP                 | | ripristino dell'AR del chiamante
    | local variables (+ spill)    | | variabili locali e registri scaricati
    +------------------------------+ ▼
    ```
### 9.3 Indirizzamento e Risoluzione dei Nomi Non Locali
*   **Coordinate Statiche $\langle level, offset \rangle$:**
    A tempo di compilazione, ogni variabile è identificata univocamente da una coppia:
    *   `level`: Il livello lessicale di annidamento in cui la variabile è dichiarata [TheProcedureAbstraction.pdf, Slide 156].
    *   `offset`: Lo scostamento fisso e noto dall'inizio del record d'attivazione [TheProcedureAbstraction.pdf, Slide 156].
*   **Access Links (Collegamenti di accesso):**
    Utilizzati nei linguaggi con scoping lessicale annidato (come Pascal o Rust).
    *   Ogni record di attivazione contiene un puntatore (Access Link) all'AR del suo antenato lessicale immediato (che non coincide necessariamente con il chiamante a runtime) [TheProcedureAbstraction.pdf, Slide 22, 160].
    *   Per accedere a una variabile non locale distanziata di $d$ livelli lessicali, il codice generato deve dereferenziare la catena di Access Link per $d$ volte consecutive, risalendo gli AR fino a trovare l'ARP corretto [TheProcedureAbstraction.pdf, Slide 160, 161].
    *   *Esempio di codice generato in ILOC per l'accesso a $\langle 1, 12 \rangle$ da livello lessicale 2:*
        ```iloc
        loadAI rarp, -4 => r1  // Risale l'access link di un livello
        loadAI r1, 12   => r10 // Carica la variabile dall'offset 12 nell'AR dell'antenato
        ```
        [TheProcedureAbstraction.pdf, Slide 161].
*   **Display:**
    Un array globale di puntatori, allocato in memoria o registri, in cui l'elemento all'indice $i$ contiene l'indirizzo dell'AR corrente attivo per il livello lessicale $i$ [TheProcedureAbstraction.pdf, Slide 22, 162].
    *   *Vantaggi:* L'accesso a qualsiasi variabile non locale richiede un costo fisso costante ($O(1)$) indipendentemente dal livello di annidamento [TheProcedureAbstraction.pdf, Slide 162].
    *   *Svantaggi:* Richiede la manutenzione dell'array globale ad ogni chiamata e ritorno e l'occupazione di un registro fisso dedicato [TheProcedureAbstraction.pdf, Slide 162].
*   **Procedure Linkage (Sequenze d'Invocazione):**
    La creazione e distruzione dell'ambiente d'esecuzione dell'AR è regolata da convenzioni di chiamata concordate (*linkage convention*) suddivise in:
    1.  *Pre-call (Chiamante):* Alloca lo spazio per i parametri, valuta le espressioni dei parametri, salva l'indirizzo di ritorno e i registri *caller-saved* volatili.
    2.  *Prologue (Chiamato):* Completa l'allestimento dell'AR, aggiorna l'ARP, alloca le variabili locali, inizializza i dati e salva i registri *callee-saved* non volatili [TheProcedureAbstraction.pdf, Slide 12].
    3.  *Epilogue (Chiamato):* Inserisce il valore di ritorno, ripristina i registri salvati nel prologo e carica l'indirizzo di ritorno.
    4.  *Post-return (Chiamante):* Dealloca l'AR del chiamato, legge il valore di ritorno e ripristina i propri registri.
*   **Allocazione dell'AR: Stack vs Heap:**
    *   *Stack (Pila):* Se la vita dell'AR coincide strettamente con l'invocazione (LIFO, classico in C o Pascal), gli AR sono gestiti sulla pila di sistema per massima efficienza [TheProcedureAbstraction.pdf, Slide 158].
    *   *Heap (Sottofondo):* Se le variabili locali o la procedura stessa possono "sopravvivere" al termine della routine (come nel caso delle *closures* con variabili catturate in ML o Rust), gli Activation Record non possono essere deallocati e devono essere mantenuti nello heap [TheProcedureAbstraction.pdf, Slide 158].


*   **Manutenzione degli access link (slide)** — chiamante a livello $p$, chiamato definito a livello $q$:
    *   $q = p+1$ (il chiamato è annidato nel chiamante): il link del chiamato è l'**ARP corrente**;
    *   $q = p$: il chiamato **copia** l'access link del chiamante;
    *   $q < p$: risalire la catena fino all'ARP di livello $q-1$ e usarlo come link.

    Il costo di manutenzione è proporzionale alla distanza lessicale.
*   **Esempio Display (slide)** — livello corrente 2, display all'etichetta `_disp`, celle da 4 byte; accesso a $\langle 1, 12 \rangle$:
    ```iloc
    loadI  _disp => r1      // indirizzo del display
    loadAI r1, 4  => r1     // ARP del livello 1   (4 × level)
    loadAI r1, 12 => r10    // variabile
    ```

    Accesso a **costo costante**; manutenzione: all'ingresso al livello $j$ salvare il vecchio $Display[j]$ nell'AR (*saved ptr.*) e scriverci l'ARP; all'uscita ripristinarlo. Contro: l'indirizzo del display consuma un registro.
*   ⚠️ **Catena statica ≠ catena delle chiamate (slide):** con `main ⊃ p1, p2 ⊃ q1, q2 ⊃ r1, r2` e la chiamata `r2 → p1` ("call *up* from level 3 to level 1"), lo stack runtime è `main, p2, q2, r2, p1, …` mentre la nesting lessicale è `main → p2 → q2 → r2`: **l'antenato lessicale non coincide con il chiamante**.
<a id="cap10"></a>
## CAPITOLO 10: Generazione del Codice (Instruction Selection & Scheduling)
**Source:** *IntroCodeGeneration.pdf*

### 10.1 Complessità e Vincoli del Back-End
La generazione del codice nel Back-End deve tradurre la rappresentazione intermedia (IR) in codice assembly nativo risolvendo tre problemi NP-Completi strettamente accoppiati [IntroCodeGeneration.pdf, Slide 6, 50, 51]:
1.  **Instruction Selection:** Seleziona le specifiche istruzioni hardware per implementare ciascuna operazione dell'IR [IntroCodeGeneration.pdf, Slide 51].
2.  **Instruction Scheduling:** Riordina la sequenza di istruzioni per nascondere le latenze di esecuzione ed evitare stalli della pipeline hardware [IntroCodeGeneration.pdf, Slide 51].
3.  **Register Allocation:** Mappa l'insieme potenzialmente illimitato di registri virtuali usati nell'IR sull'insieme finito di registri fisici dell'hardware reale [IntroCodeGeneration.pdf, Slide 51].

### 10.2 Il Concetto di "Code Shape"
*   **Definizione di Code Shape:** Indica la scelta della specifica strategia implementativa (la "forma" del codice risultante) tra le molteplici alternative logicamente equivalenti messe a disposizione dall'ISA target [IntroCodeGeneration.pdf, Slide 12, 52].
    *   *Esempio (Somma Ternaria):* La traduzione dell'espressione $x + y + z$ può essere implementata in modi diversi sfruttando le proprietà associative e commutative dell'addizione [IntroCodeGeneration.pdf, Slide 52]:
        *   Forma 1: $(x + y) + z$ (un'istruzione `add` intermedia) [IntroCodeGeneration.pdf, Slide 52].
        *   Forma 2: $(x + z) + y$ [IntroCodeGeneration.pdf, Slide 52].
        *   Forma 3: $(y + z) + x$ [IntroCodeGeneration.pdf, Slide 52].
    *   La scelta della forma ottimale dipende interamente dal contesto circostante e dalla conoscenza delle costanti (se $x$ e $z$ sono costanti, es. $2$ e $3$, il compilatore dovrebbe riordinare la somma per calcolare a tempo di compilazione $2+3=5$ tramite constant folding, riducendo le istruzioni a runtime) [IntroCodeGeneration.pdf, Slide 52].

### 10.3 Postorder Treewalk Evaluator
Un modo intuitivo per generare codice a partire da un Abstract Syntax Tree (AST) consiste nell'eseguire una visita ricorsiva in ordine postorder (*postorder treewalk*), che visita prima i figli e poi emette l'operazione associata al nodo padre [IntroCodeGeneration.pdf, Slide 15, 54].
*   **Algoritmo ricorsivo formale `expr(node)`:**
    ```text
    expr(node) {
        register result, t1, t2;
        switch (type(node)) {
            case x, /, +, - :
                t1 <- expr(left child(node));
                t2 <- expr(right child(node));
                result <- NextRegister();
                emit (op(node), t1, t2, result);
                break;
            case IDENTIFIER:
                t1 <- base(node); // recupera l'indirizzo base rarp
                t2 <- NextRegister();
                emit (loadI, offset(node), none, t2);
                result <- NextRegister();
                emit (loadAO, t1, t2, result);
                break;
            case NUMBER:
                result <- NextRegister();
                emit (loadI, val(node), none, result);
                break;
        }
        return result;
    }
    ```
    [IntroCodeGeneration.pdf, Slide 15, 54, 55].
*   **Traccia di traduzione naif per $x + y$:**
    1.  *Chiamata per il nodo `x` (IDENTIFIER):*
        *   Emette `loadI @x => r1` (carica l'offset di `x` in un registro temporaneo) [IntroCodeGeneration.pdf, Slide 56].
        *   Emette `loadAO rarp, r1 => r2` (carica il valore reale dall'offset `rarp + r1` nel registro `r2`) [IntroCodeGeneration.pdf, Slide 56].
    2.  *Chiamata per il nodo `y` (IDENTIFIER):*
        *   Emette `loadI @y => r3` [IntroCodeGeneration.pdf, Slide 56].
        *   Emette `loadAO rarp, r3 => r4` [IntroCodeGeneration.pdf, Slide 56].
    3.  *Chiamata per il nodo operatore `+`:*
        *   Emette `add r2, r4 => r5` (somma i valori e inserisce il risultato finale nel nuovo registro `r5`) [IntroCodeGeneration.pdf, Slide 56].

### 10.4 Generazione del Codice per Strutture di Controllo
*   **Generazione dei Cicli (Loops):** Un ciclo generico `while (cond) { body }` viene tradotto strutturando i blocchi sul Control Flow Graph (CFG) in tre parti principali:
    1.  *Pre-test:* Valuta l'espressione condizionale e, in caso di esito falso, salta all'uscita tramite un'istruzione di salto condizionato.
    2.  *Body:* Esegue il corpo del ciclo.
    3.  *Post-test / Loop-back:* Esegue un salto incondizionato alla testa del pre-test per rivalutare la condizione.
*   **Generazione del costrutto Case/Switch:**
    La traduzione di un costrutto di selezione multipla `switch (x)` ammette tre diverse forme (shapes) alternative:
    1.  **Linear Search (Scansione Lineare):** Genera una sequenza di istruzioni condizionali `if (x == c1) goto label1; else if (x == c2) ...`. Adatto per un numero ridotto di casi.
    2.  **Binary Search (Ricerca Binaria):** Genera una struttura ad albero binario di confronti condizionali su un array ordinato delle costanti di case, riducendo la complessità di ricerca a $O(\log N)$.
    3.  **Jump Table (Tabella dei Salti):** Genera una tabella contenente direttamente gli indirizzi dei blocchi di destinazione, indicizzata dal valore di `x` (previa sottrazione del limite inferiore). Esegue il salto in tempo costante $O(1)$ tramite l'istruzione di salto indiretto `jumpI`. È la forma più veloce ma richiede che il set dei case sia denso per evitare un eccessivo spreco di memoria dovuto a celle vuote.


<a id="cap11"></a>
## CAPITOLO 11: Allocazione dei Registri
**Sources:** *RegisterAlloc1.pdf / RegisterAlloc2.pdf*

### 11.1 Allocazione vs Assegnamento
Nel Back-End del compilatore si distinguono due fasi logiche fondamentali per la gestione dei registri [RegisterAlloc1.pdf, Slide 15; RegisterAlloc2.pdf, Slide 15]:
*   **Register Allocation (Allocazione):** La decisione su quali variabili e valori intermedi debbano risiedere all'interno dei registri e quali invece debbano essere posizionati in memoria o scaricati [RegisterAlloc1.pdf, Slide 15; RegisterAlloc2.pdf, Slide 15].
*   **Register Assignment (Assegnamento):** L'assegnazione fisica di specifici registri reali della CPU target (es. `r0`, `r1`) ai valori precedentemente selezionati nella fase di allocazione [RegisterAlloc1.pdf, Slide 15; RegisterAlloc2.pdf, Slide 15].

#### Modelli di Gestione della Memoria:
*   **Register-to-register model (Modello registro-registro):** L'Instruction Selection assume un numero teoricamente infinito di registri virtuali e delega interamente all'allocatore dei registri il compito di ridurli e di inserire le necessarie operazioni di `load` e `store` per gestire lo scaricamento (*spill*) sul set di registri fisici limitati dell'hardware target [IntroCodeGeneration.pdf, Slide 51; RegisterAlloc1.pdf, Slide 146].
*   **Memory-to-memory model (Modello memoria-memoria):** Assume che tutti i valori risiedano originariamente in memoria. L'allocatore agisce come una passata di ottimizzazione, decidendo quali variabili portare temporaneamente nei registri fisici per migliorarne la velocità di accesso [IntroCodeGeneration.pdf, Slide 51].

### 11.2 Allocazione Locale (slide)
*   **Live range locali = intervalli $[i, j]$** nel blocco: un valore è vivo dalla definizione all'ultimo uso (una seconda definizione ne apre uno nuovo).
*   **MAXLIVE** = massimo numero di valori simultaneamente vivi su un'istruzione del blocco. Se $MAXLIVE \le k$ l'allocazione è diretta; se $MAXLIVE > k$ occorre riservare $F$ registri per lo spill (di norma 2: indirizzo + dato). I live set si calcolano **a ritroso**: si parte dall'insieme vuoto e a ogni operazione si rimuove il target e si aggiungono gli operandi (in ILOC la freccia ⇒ separa usi da definizioni; **eccezione**: `store` usa tutti i propri operandi di registro).
*   **Esempio svolto (slide):**

    ```
    loadI   1028    ⇒ r1    // {r1}
    load    r1      ⇒ r2    // {r1 r2}
    mult    r1, r2  ⇒ r3    // {r1 r2 r3}
    load    x       ⇒ r4    // {r1 r2 r3 r4}  ← MAXLIVE = 4
    sub     r4, r2  ⇒ r5    // {r1  r3  r5}
    load    z       ⇒ r6    // {r1  r3  r5 r6}
    mult    r5, r6  ⇒ r7    // {r1  r3      r7}
    sub     r7, r3  ⇒ r8    // {r1          r8}
    store   r8      ⇒ r1    // { }   (r1 qui è un USE, non una definizione)
    ```

*   **Allocatore top-down (frequency count, slide):** conta le occorrenze di ogni registro virtuale, ordina, assegna i primi $k - r$ ai registri fisici, riscrive il resto con load/store. Con $k = 3$: `r1` è più usato di `r3` ⇒ si spilla `r3` (`store r3 ⇒ 16` dopo la definizione, `load 16 ⇒ r3` prima di ogni uso successivo): `r3` diventa **due live range minimi** che si sovrappongono a meno valori. Il codice è più lento ma **corretto** su 3 registri — *correctness is a virtue*. Debolezza: un registro fisico è dedicato a un virtuale per **tutto il blocco**.
*   **Allocatore bottom-up (distance to next use, slide):** *load on demand*; quando i registri sono esauriti si **spilla il valore il cui prossimo uso è il più lontano nel futuro**, preferendo i valori *clean* (costanti o già in memoria: niente store) ai *dirty* (da riscrivere). Con $k = 3$: all'istruzione `loadI x ⇒ r4` tutti i registri sono occupati; il prossimo uso di `r1` (lo store finale) è il più lontano ⇒ `store r1 ⇒ 20`, riuso del suo registro, `load 20 ⇒ r1` prima dello store finale.
*   **Dal locale al regionale (edge case, slide):** se `x` è in registro alla fine di $B_1$ e $B_2$ (entrambi predecessori di un join) con un solo registro disponibile, l'unica soluzione corretta è **store di `x` a fine di entrambi i blocchi** — è il motivo per cui serve l'allocazione globale.

### 11.3 Allocazione Globale via Colorazione del Grafo
Consiste nel mappare il problema dell'assegnamento ottimale dei registri sul problema (NP-Completo) della **colorazione di un grafo d'interferenza** con $k$ colori distinti, in cui ogni colore corrisponde ad un registro fisico reale [RegisterAlloc2.pdf, Slide 15, 14.1].
*   **Grafo di Interferenza (Interference Graph):**
    *   **Nodi:** Ciascun nodo rappresenta un *live range* (la "ragnatela" o *web* di definizioni e usi interconnessi di una variabile) [RegisterAlloc2.pdf, Slide 15, 14.1].
    *   **Archi:** Esiste un arco non orientato tra due nodi se i rispettivi live range si sovrappongono temporaneamente (cioè le due variabili sono contemporaneamente vive in un qualsiasi punto del CFG) [RegisterAlloc2.pdf, Slide 15, 14.1].

#### La Pipeline di Chaitin-Briggs:
L'algoritmo di Chaitin-Briggs esegue l'allocazione globale tramite 5 fasi sequenziali [RegisterAlloc2.pdf, Slide 15, 14.1]:
1.  **Build (Costruzione):** Analizza il CFG della procedura, esegue l'analisi di liveness e costruisce il Grafo di Interferenza [RegisterAlloc2.pdf, Slide 15, 14.1].
2.  **Coalesce (Fusione):** Elimina le istruzioni di copia non necessarie (es. `x <- y`). Se i nodi di `x` e `y` non interferiscono, i due nodi vengono fusi in un unico super-nodo [RegisterAlloc2.pdf, Slide 15, 14.1].
3.  **Spill Cost (Stima dei Costi):** Calcola per ciascun nodo il costo stimato in termini d'istruzioni se dovesse essere scaricato in memoria, pesando maggiormente gli accessi eseguiti all'interno dei cicli annidati [RegisterAlloc2.pdf, Slide 15, 14.1].
4.  **Simplify (Semplificazione):** Algoritmo basato sul criterio di Kempe. Cerca un nodo con grado inferiore a $k$ (numero di registri fisici). Se esiste, lo rimuove dal grafo e lo spinge su una pila. Se tutti i nodi rimasti hanno grado $\ge k$, l'algoritmo deve scegliere un candidato allo spill (spill candidate) in base al costo calcolato al punto 3, lo rimuove e lo spinge sulla pila comunque (**spill ottimistico di Briggs**) [RegisterAlloc2.pdf, Slide 15, 14.1].
5.  **Select (Colorazione):** Estrae progressivamente i nodi dalla pila e tenta di assegnare loro un colore (un registro) non utilizzato dai nodi vicini nel grafo originario.
    *   Se un nodo precedentemente selezionato per lo spill non trova colori disponibili, si verifica uno **spill reale**: il compilatore deve inserire istruzioni di `store` e `load` prima e dopo ogni uso della variabile, dividendo il live range, e riavviando l'intera pipeline dal punto 1 [RegisterAlloc2.pdf, Slide 15, 14.1].

#### Esempi Svolti di Colorazione (slide)
*   **Chaitin, $k = 3$ register.** Grafo su $\{1, \dots, 5\}$ con archi $\{1\text{-}2,\ 1\text{-}3,\ 2\text{-}4,\ 2\text{-}5,\ 3\text{-}4,\ 3\text{-}5,\ 4\text{-}5\}$; gradi: $1{:}2$, $2{:}3$, $3{:}3$, $4{:}3$, $5{:}3$ — solo il nodo 1 ha grado $< 3$.
    1.  push 1 (grado $2 < 3$); la rimozione abbassa a 2 i gradi di 2 e 3;
    2.  push 2; la rimozione porta **tutti** i rimanenti a grado $< 3$;
    3.  push 4, push 3; resta solo 5 ⇒ push 5 (candidato spill "ottimistico");
    4.  pop 5 → colore 1;  pop 3 (vicini 1,4,5: solo 5 colorato) → colore 2;  pop 4 (vicini 2,3,5: colori 1,2 usati) → colore 3;  pop 2 → colore 2;  pop 1 → colore 1.

    Colorazione valida su 3 registri **senza alcuno spill**.
*   **Briggs — optimistic coloring, $k = 2$ register.** Grafo a diamante: archi $1\text{-}2$, $2\text{-}4$, $4\text{-}3$, $3\text{-}1$; **tutti** i nodi hanno grado esattamente 2 ⇒ nessun nodo con grado $< 2$: Chaitin spillerebbe immediatamente. Briggs pusha comunque un nodo, diciamo 1; la rimozione porta 2 e 3 a grado 1; push 3; ora 2 e 4 hanno grado $< 2$; push 2, push 4. In fase di select: pop 4 → colore 1; pop 2 → colore 2; pop 3 → colore 2 (il vicino 4 ha colore 1); pop 1 → i vicini 2 e 3 usano entrambi il colore 2 ⇒ **il colore 1 è disponibile!** 2-colorazione trovata, zero spill: il grado è solo un **limite superiore lasco** sulla colorabilità (un nodo può avere $k+2$ vicini che usano meno di $k$ colori).
*   **Coalescing (slide):** per una copia `i2i LR1 ⇒ LR2` con $\langle LR_1, LR_2 \rangle \notin E_I$ (sorgente e destinazione di una copia **non interferiscono mai**) si fondono i due live range e si elimina la copia: riduce il grado dei vicini comuni. ⚠️ Il nodo fuso $LR_{ab}$ ha grado $deg(LR_a) + deg(LR_b)$: il grafo può diventare **più difficile da colorare**; inoltre l'ordine di coalescenza conta (un coalescing può precluderne altri) ⇒ si usano strategie *safe*.

### 11.4 Rappresentazione Static Single Assignment (SSA)
*   **Principio Cardine:** La forma Static Single Assignment (SSA) richiede che **ciascuna variabile venga definita esattamente una volta** all'interno del testo del programma [RegisterAlloc2.pdf, Slide 148].
*   **Funzioni Phi (\(\phi\)-functions):** Nei punti di convergenza (join) del CFG in cui confluiscono percorsi d'esecuzione con definizioni diverse per la stessa variabile (es. rami then/else), il compilatore inserisce una funzione speciale $\phi$ del tipo $x_3 \leftarrow \phi(x_1, x_2)$ per unificare il valore corretto a seconda del cammino di provenienza reale [RegisterAlloc2.pdf, Slide 148].
*   La forma SSA semplifica enormemente molte analisi di ottimizzazione (come il value numbering globale e la propagazione delle costanti) e riduce la complessità dell'allocazione dei registri.


<a id="cap12"></a>
## CAPITOLO 12: Monografia rustc (L'Architettura del Compilatore Rust)
**Sources:** *COMP-01...06-RUST_COMPILATION.pdf*

### 12.1 Il Sistema di Compilazione Demand-Driven
A differenza delle architetture tradizionali basate su passate sequenziali e immutabili, il compilatore di Rust (`rustc`) è strutturato come un **sistema basato su query** (*demand-driven system*) [COMP-01_RUST_COMPILATION.pdf, Slide 18, 9].
*   **Funzionamento:** Invece di eseguire fasi rigide per l'intero codice, `rustc` definisce una serie di query memoizzate (es. `type_of(def_id)`, `optimized_mir(def_id)`, `mir_borrowck(def_id)`) [COMP-01_RUST_COMPILATION.pdf, Slide 18; COMP-02_RUST_COMPILATION.pdf, Slide 18].
*   **Vantaggi:**
    *   **Compilazione Incrementale:** Se il codice sorgente subisce una modifica, il compilatore ri-esegue esclusivamente le query i cui dati di input diretti o dipendenze siano stati effettivamente alterati, riutilizzando i risultati memoizzati memorizzati nella cache per tutto il resto [COMP-01_RUST_COMPILATION.pdf, Slide 18, 9].
    *   **Modularità:** Offre una separazione pulita e altamente strutturata dei vari componenti logici del compilatore [COMP-01_RUST_COMPILATION.pdf, Slide 18, 9].

### 12.2 I Quattro Livelli di Rappresentazione Intermedia (IR)
Perché un solo AST non è sufficiente nel compilatore Rust?
*   L'AST è troppo legato alla sintassi concreta del programmatore, include costrutti ad alto livello ("sugar" sintattico) e nasconde l'esplicito ordine di valutazione temporale e i reali confini del Control Flow Graph (CFG) [COMP-01_RUST_COMPILATION.pdf, Slide 12, 11].
*   Senza IR intermedie dedicate, ogni singola analisi semantica (type checking, borrow checking, drop elaboration) dovrebbe re-implementare autonomamente la decodifica del sugar sintattico, rendendo lo sviluppo complesso e incline a bug [COMP-01_RUST_COMPILATION.pdf, Slide 11].

Per ovviare a ciò, `rustc` implementa quattro livelli sequenziali di IR [COMP-01_RUST_COMPILATION.pdf, Slide 20, 21, 27]:
1.  **AST (Abstract Syntax Tree):** Albero sintattico generato direttamente dal parser ricorsivo a discesa `rustc_parse` [COMP-01_RUST_COMPILATION.pdf, Slide 19, 9]. Rappresenta la sintassi di superficie del programmatore [COMP-01_RUST_COMPILATION.pdf, Slide 19, 9].
2.  **HIR (High-Level IR):** Costruito a partire dall'AST dopo l'espansione delle macro e la risoluzione dei nomi (*name resolution*) [COMP-01_RUST_COMPILATION.pdf, Slide 20, 13]. È una rappresentazione più regolare e pulita, adatta per i controlli semantici e la diagnostica del Front-End, in cui parte del sugar sintattico è già stata normalizzata [COMP-01_RUST_COMPILATION.pdf, Slide 20, 13].
3.  **THIR (Typed HIR):** Ottenuto arricchendo l'HIR con informazioni di tipo locali esplicite per i corpi delle funzioni [COMP-01_RUST_COMPILATION.pdf, Slide 20, 14; COMP-02_RUST_COMPILATION.pdf, Slide 10]. Rende esplicite tutte le decisioni semantiche dipendenti dai tipi (come le conversioni implicite o il dereferenziamento automatico) [COMP-02_RUST_COMPILATION.pdf, Slide 10].
4.  **MIR (Mid-Level IR):** Un Control Flow Graph (CFG) tipizzato, composto da blocchi base, statements, operandi e terminatori espliciti [COMP-01_RUST_COMPILATION.pdf, Slide 27, 15]. È l'IR centrale su cui si eseguono il Borrow Checker, la Drop Elaboration, la qualificazione delle costanti e le ottimizzazioni prima del passaggio a LLVM [COMP-01_RUST_COMPILATION.pdf, Slide 21, 27; COMP-02_RUST_COMPILATION.pdf, Slide 18].

### 12.3 Analisi della Traduzione di un'Istruzione condizionale Rust
Analizziamo come l'istruzione condizionale Rust `let z = if x > 0 { x + 1 } else { 0 };` viene progressivamente ridotta lungo le quattro IR [COMP-01_RUST_COMPILATION.pdf, Slide 12, 13, 14, 15, 16]:
*   **Livello AST:** Struttura ad albero gerarchica che preserva le espressioni annidate del blocco `Stmt::Local` contenente l'espressione condizionale `Expr::If` con i rami `then` e `else` intatti [COMP-01_RUST_COMPILATION.pdf, Slide 12, 12, 13]. Il risultato finale è implicito.
*   **Livello HIR & THIR:** La struttura ad albero rimane simile, ma vengono annotate esplicitamente le informazioni tipizzate locali: viene registrato che `z`, `x` e le costanti `0` e `1` hanno tipo `i32`, e che l'espressione di confronto condizionale ha tipo `bool` [COMP-01_RUST_COMPILATION.pdf, Slide 14, 14, 15].
*   **Livello MIR (CFG):** La singola riga di assegnamento viene riscritta ed esplosa in un grafo del flusso di controllo esplicito, in cui vengono introdotti registri temporanei locali (`_t0`, `_t1`) e i blocchi base (`bb0`, `bb1`, `bb2`) [COMP-01_RUST_COMPILATION.pdf, Slide 16, 16]:
    ```rust
    let mut _z: i32;
    let mut _t0: bool;
    let mut _t1: i32;
    bb0: {
        _t0 = Gt(copy _x, const 0_i32);
        switchInt(copy _t0) -> [0: bb2, otherwise: bb1];
    }
    bb1: {
        _t1 = Add(copy _x, const 1_i32);
        _z = _t1;
        goto -> bb3;
    }
    bb2: {
        _z = const 0_i32;
        goto -> bb3;
    }
    bb3: { ... }
    ```
    [COMP-01_RUST_COMPILATION.pdf, Slide 16, 16].

### 12.4 Drop Elaboration
*   In Rust, la gestione della memoria si basa sulla deallocazione deterministica automatica di ciascuna risorsa non appena il suo proprietario esce dallo scope d'esecuzione (regola RAII) [COMP-03_RUST_COMPILATION.pdf, Slide 19].
*   La **Drop Elaboration** è la fase del compilatore che rispecchia questa semantica a livello di MIR [COMP-02_RUST_COMPILATION.pdf, Slide 18].
*   **Funzionamento:** Analizza la vitalità delle variabili e converte i punti di rilascio impliciti del codice in blocchi di controllo espliciti e terminatori MIR di tipo `Drop` [COMP-01_RUST_COMPILATION.pdf, Slide 21; COMP-02_RUST_COMPILATION.pdf, Slide 18].
*   **Drop Flags Condizionali:** Se lo stato d'inizializzazione di una variabile non può essere determinato in modo statico a tempo di compilazione (es. se la variabile viene mossa all'interno di un ramo condizionale `if-else`), il compilatore introduce dei registri temporanei booleani invisibili detti **drop flags** [COMP-02_RUST_COMPILATION.pdf, Slide 22, 15.2]. Lo stato del drop flag viene modificato dinamicamente a runtime nel corso delle esecuzioni, e il terminatore `Drop` viene avvolto in un ramo condizionale che verifica il drop flag prima di eseguire la deallocazione, prevenendo errori critici di doppia deallocazione (*double free*) o rilascio di risorse non inizializzate [COMP-02_RUST_COMPILATION.pdf, Slide 22, 15.2].

### 12.5 Il MIR Borrow Checker e i Non-Lexical Lifetimes (NLL)
Il Borrow Checker è il componente fondamentale che garantisce staticamente e a costo zero la sicurezza della memoria in Rust, verificando l'assenza di violazioni e data race [COMP-01_RUST_COMPILATION.pdf, Slide 7, 10].
*   **Funzionamento:** Opera sul grafo MIR CFG analizzando quattro domini intrecciati: variabili inizializzate, move paths, tempi di vita (lifetimes / regioni) e prestiti attivi (*loans*) [COMP-04_RUST_COMPILATION.pdf, Slide 20].
*   **Analisi dei Move e Inizializzazione:**
    *   Traccia lo stato d'inizializzazione delle variabili tramite analisi di dataflow.
    *   **Regola d'oro d'esame:** Lo spostamento (*move*) di una variabile padre invalida (uccide) tutti i suoi campi figli [COMP-03_RUST_COMPILATION.pdf, Slide 12, 15.2]. Al contrario, lo spostamento di un singolo campo figlio non uccide i fratelli, consentendo un ragionamento preciso a livello di singola componente (partial-move reasoning) [COMP-03_RUST_COMPILATION.pdf, Slide 12, 15.2].
*   **Non-Lexical Lifetimes (NLL) e Region Inference:**
    *   Nelle vecchie versioni di Rust, i lifetimes erano lessicali, legati rigidamente alla struttura dei blocchi sintattici `{ ... }`.
    *   I **Non-Lexical Lifetimes (NLL)** estendono l'analisi basandola sul Control Flow Graph (CFG) a livello MIR, riducendo drasticamente i falsi positivi del compilatore [COMP-03_RUST_COMPILATION.pdf, Slide 4; COMP-04_RUST_COMPILATION.pdf, Slide 20].
    *   **Generazione dei vincoli:** La tipizzazione del MIR introduce variabili di regione (lifetimes indicati con $'a$) e genera vincoli di inclusione del tipo **`'a: 'b`** (la regione $'a$ deve sopravvivere alla regione $'b$) [COMP-03_RUST_COMPILATION.pdf, Slide 4; COMP-04_RUST_COMPILATION.pdf, Slide 20].
    *   **Region Inference sul DAG delle SCC:** Per risolvere in modo ottimale il sistema di vincoli di outlives ed evitare ricalcoli ciclici, `rustc` modella le relazioni di inclusione come un grafo orientato [COMP-04_RUST_COMPILATION.pdf, Slide 12, 15.3]. Identifica le Componenti Fortemente Connesse (SCC - Strongly Connected Components) del grafo e le collassa in singoli super-nodi equivalenti [COMP-04_RUST_COMPILATION.pdf, Slide 12, 15.3]. Successivamente, esegue la propagazione dei vincoli sul grafo risultante, che è un **Grafo Diretto Aciclico (DAG) di SCC**, seguendo un ordinamento topologico inverso, garantendo la risoluzione efficiente e stabile del punto fisso in tempo lineare $O(n)$ [COMP-04_RUST_COMPILATION.pdf, Slide 12, 15.3].
*   **Two-Phase Borrows (Reservation vs Activation):**
    Consente di supportare pattern sintattici d'uso frequenti ma complessi (come le mutazioni annidate, es. `vec.push(vec.len())`). Il compilatore divide il prestito mutabile in due fasi distinte: una fase iniziale di *reservation* (in cui il prestito mutabile è inattivo e si comporta temporaneamente come un prestito immutabile, consentendo letture parallele) ed una successiva fase di *activation* (in cui avviene l'effettivo utilizzo mutabile esclusivo), prevenendo violazioni fittizie delle regole di borrowing [COMP-04_RUST_COMPILATION.pdf, Slide 20].

#### Le Regole di Ownership e Borrowing (slide)
```
[O1] Ogni valore è posseduto da una variabile, identificata da un nome o path.
[O2] Ogni valore ha al più un owner alla stessa istante.
[O3] Quando l'owner esce dallo scope, il valore viene 'dropped'.
[B1] Al più un riferimento mutabile a una risorsa può esistere alla stessa istante.
[B2] Se esiste un riferimento mutabile, nessun riferimento immutabile può esistere.
[B3] Se non esistono riferimenti mutabili, possono coesistere più riferimenti immutabili.
[B4] L'owner non può liberare o mutare la risorsa mentre è immutably borrowed.
[B5] L'owner non può perfino leggerla mentre è mutably borrowed.
```
Sintesi: **alias XOR mutation**. Esempi slide:
```rust
let mut s = String::from("example");
let r1 = &mut s; let r2 = &mut s;   // NON compila — viola [B1]
let r1 = &s;     let r2 = &mut s;   // NON compila — viola [B2]
let r1 = &s;     let r2 = &s;       // OK — [B3]
```
**Move semantics (slide):** `let x = Box::new(3); let _y = x; println!("{}", x);` ⇒ errore (l'ownership è mossa a `_y`); per i tipi `Copy` (`let x = 3; let _y = x;`) va bene: [O2] resta valido perché viene creato un nuovo valore.

#### Le Fasi del MIR Borrow Checker (query `mir_borrowck`, slide)
1.  duplicazione e preparazione del MIR (copia locale, mutata in place);
2.  **region variable initialization**: `replace_regions_in_mir` sostituisce i lifetime con variabili d'inferenza fresche;
3.  **dataflow** su mosse e inizializzazione (cosa è moved/initialized/invalidato sul CFG);
4.  **MIR type check** (seconda type-check) ⇒ genera i **vincoli tra regioni** ($'a{:}'b$) e i type test;
5.  **region inference**: risolve i vincoli a punto fisso (propagazione sul **DAG delle SCC**);
6.  **borrows in scope**: quali prestiti sono attivi a ogni punto del CFG;
7.  **validation finale**: ogni operazione (es. `*a + 1`) è controllata contro stato d'inizializzazione, regole di borrowing e vincoli di mutabilità.

#### Esempio Svolto: Dangling Reference (slide)
```rust
fn bad() -> &i32 { let x = 10; &x }
```
MIR: `_1 = const 10;   _0 = &'r1 _1;   return` con `_0 : &'r0 i32`. Dall'assegnamento discende il vincolo **`'r1 : 'r0`** ("'r1 outlives 'r0": il prestito deve vivere almeno quanto il ritorno). Inferenza sui punti $[p_1]\,_1 = 10$, $[p_2]\,_0 = \&'r1\_1$, $[p_3]$ return: $'r1 = \{p_2, p_3\}$, $'r0 = \{p_3, \text{contesto del chiamante}\}$ ⇒ $'r1$ non copre tutti i punti di $'r0$ ⇒ **errore**. ⚠️ L'errore **non è locale al borrow**: emerge globalmente dopo la region inference (vincoli + CFG + drop ⇒ sistema insoddisfabile).

#### Move Analysis: Tabella GEN/KILL (slide)
Dominio = insiemi di **move path** ($a$, $a.0$, $a.b.c$: albero con query padre/figli; sono esclusi gli elementi di array `foo[1]` e i dereference `*foo`). $OUT[n] = GEN[n] \cup (IN[n] - KILL[n])$; $\; IN[n] = \bigcup OUT[p]$ sui predecessori.

| Statement | GEN | KILL |
|---|---|---|
| init `a` (tupla) | {a, a.0, a.1} | ∅ |
| `b = a` | {b} | {a, a.0, a.1} |
| `b = a.0` | {b} | {a.0} |

Muovere il **padre uccide tutti i figli**; muovere un figlio **non** uccide i fratelli (dopo `b = a.0` resta valido `a.1`); `c = a` dopo il partial move ⇒ errore *use of partially moved value a*; `drop(a)` rimuove `a` ⇒ uso successivo = *use of uninitialized value*.

#### Closure Capture Inference (slide)
Le closure compilano in **struct che catturano gli upvar**; rustc inferisce la modalità partendo da un borrow immutabile e rilassandola al bisogno: sola lettura ⇒ `&T` (**Fn**); mutazione ⇒ `&mut T` (**FnMut**); consumo (es. `drop`) ⇒ by value (**FnOnce**). Meccanismo: `upvars_mentioned` individua gli upvar; `euv::ExprUseVisitor` cammina il corpo invocando le callback del trait **Delegate** (`consume`, `borrow`, `mutate`, ciascuna con un `cmt` = Category/Mutability/Type); `InferBorrowKind` registra la modalità finale (`ByValue` / `ByRef{ImmBorrow, UniqueImmBorrow, MutBorrow}`). Esempi slide (MIR): `|| println!("{}", x)` ⇒ `_4 = &_1;  _3 = closure{x: move _4}`; `|| x += 10` ⇒ `_4 = &mut _1; …`; `|| drop(x)` ⇒ `_4 = closure{x: move _1}`.

### 12.6 Monomorfizzazione e Generazione del Codice nel Back-End
*   **Monomorfizzazione (Monomorphization):** Consiste nel duplicare e specializzare il codice generico generato dal programmatore (es. funzioni con generics `fn print_val<T>(x: T)`) producendo istanze separate e concrete per ogni tipo di dato effettivamente utilizzato (es. `print_val::<i32>` e `print_val::<String>`) [COMP-05_RUST_COMPILATION.pdf, Slide 12, 23].
*   **Monomorphization Collector:** Gestisce la raccolta delle istanze concrete scorrendo il MIR CFG [COMP-05_RUST_COMPILATION.pdf, Slide 23, 26]. Rust supporta due strategie d'esame [COMP-05_RUST_COMPILATION.pdf, Slide 26]:
    *   *Lazy collection (default):* Raccoglie solo le istanze concrete che vengono provatamente referenziate nel codice generato, minimizzando il codice risultante.
    *   *Eager collection:* Istanzia preventivamente più combinazioni per favorire e accelerare la compilazione incrementale [COMP-05_RUST_COMPILATION.pdf, Slide 26].
    *   *Mentioned Items:* Per evitare che errori di costante (fallimenti di const evaluation) dipendano da ottimizzazioni successive che rimuovono rami di codice morto (dead code), il compilatore traccia tutti gli elementi menzionati sintatticamente nel MIR (`mentioned items`), riportando in modo stabile e coerente eventuali violazioni [COMP-05_RUST_COMPILATION.pdf, Slide 26].
*   **Codegen Units (CGUs):**
    Il partizionatore suddivide la collezione delle istanze monomorfizzate in sotto-moduli distinti chiamati **Codegen Units (CGUs)** [COMP-05_RUST_COMPILATION.pdf, Slide 27]. Ciascun CGU viene compilato e ottimizzato asincronamente in parallelo in un thread separato tramite un modulo LLVM distinto [COMP-05_RUST_COMPILATION.pdf, Slide 27].
    *   **Il trade-off fondamentale delle CGU:**
        *   *Molti piccoli CGU:* Accelera drasticamente la compilazione incrementale (se cambia una funzione, LLVM deve ricostruire e ri-ottimizzare solo quel piccolo modulo) ma inibisce le ottimizzazioni globali, l'inlining cross-modulo e degrada la velocità d'esecuzione dell'eseguibile risultante [COMP-05_RUST_COMPILATION.pdf, Slide 28].
        *   *Pochi grandi CGU:* Consente a LLVM di effettuare analisi globali, inlining aggressivo e generare un codice macchina estremamente efficiente, a scapito di tempi di compilazione molto più lunghi e pesanti [COMP-05_RUST_COMPILATION.pdf, Slide 28].
    *   *Heuristica basata sui moduli sorgente:* Per bilanciare questo trade-off, `rustc` applica un'euristica creando, per ciascun modulo sorgente, un CGU dedicato alle monomorfizzazioni volatili generiche e un CGU separato destinato al codice stabile non generico [COMP-05_RUST_COMPILATION.pdf, Slide 28].

### 12.7 Sistema di Unificazione e Analisi Statica (Lints)
*   **Unificazione del Primo Ordine (Martelli-Montanari):** `rustc` applica l'algoritmo formale di Martelli-Montanari per risolvere i sistemi di equazioni di vincoli sui tipi estratti dal codice [COMP-06_RUST_COMPILATION.pdf, Slide 12, 15.5].
*   **Type Inference:** Si basa sulla logica formale induttiva di Hindley-Milner (Algoritmo W) per dedurre i tipi delle variabili locali senza necessità di annotazione esplicita del programmatore [COMP-06_RUST_COMPILATION.pdf, Slide 12, 15.5].
*   **Classificazione dei Lints:** I lints sono controlli statici non bloccanti integrati nella pipeline per identificare stili non idiomatici o potenziali bug. Si dividono in [COMP-06_RUST_COMPILATION.pdf, Slide 30]:
    *   *Early Lints:* Vengono eseguiti direttamente sull'AST subito dopo l'espansione delle macro, sfruttando informazioni meramente sintattiche (es. `unused_parens`, che individua parentesi superflue) [COMP-06_RUST_COMPILATION.pdf, Slide 30].
    *   *Late Lints:* Vengono eseguiti al termine dell'analisi semantica sull'HIR o sul MIR tipizzato, sfruttando la ricchezza semantica completa e i tipi definitivi (es. `unused_mut`, che rileva variabili dichiarate mutabili ma mai mutate nel CFG, o controlli su variabili non inizializzate) [COMP-06_RUST_COMPILATION.pdf, Slide 30].


*   **Livelli dei lints (slide):** `allow` → `expect` → `warn` → `force-warn` → `deny` → `forbid` (gli ultimi due non silenziabili). Configurazione: flag `-A/-W/--force-warn/-D/-F`, attributi (`#![warn(missing_docs)]`, `#[allow(unused_mut, reason = "…")]`), `--cap-lints LEVEL` (Cargo compila le dipendenze con `--cap-lints allow`, così i loro warning non inquinano il build) e **lint group** (`nonstandard-style`, `unused`, `future-incompatible`, …). **Clippy** = collezione ufficiale di lints registrata nell'infrastruttura di rustc: *rustc verifica che il programma sia Rust valido; Clippy che sia buon Rust*.
*   **Type inference per uHaskell / Algorithm W (slide):** pipeline = parse tree → variabili di tipo sui nodi → **generazione dei vincoli** (applicazione: $t_0 = t_1 \to t_2$; definizione $f\ x = e$: $t_0 = t_1 \to t_2$; costanti/operatori dall'ambiente) → **unificazione** → le variabili non vincolate diventano **polimorfe**. Esempio svolto `f x = 2 + x`: vincoli $t_0 = t_1 \to t_6$, $t_4 = t_1 \to t_6$, $t_2 = t_3 \to t_4$, $t_2 = Int \to Int \to Int$, $t_3 = Int$; unificando: $t_3 = Int$, $t_4 = Int \to Int$, $t_1 = Int$, $t_6 = Int$ ⇒ **`f :: Int → Int`**. Polimorfismo: `f g = g 2` ⇒ $t_0 = t_1 \to t_4$, $t_1 = t_3 \to t_4$, $t_3 = Int$ ⇒ **`f :: (Int → t₄) → t₄`** con $t_4$ universale (`f add = 4`, `f isEven = True`). Datatypes: da `length [] = 0;  length (x:rest) = 1 + (length rest)`, inferendo ogni clausola e imponendo l'uguaglianza dei tipi tra clausole ⇒ **`length :: [t₁] → Int`**.
<a id="appendice"></a>
## Appendice — Esperienze di Laboratorio e Toolchain
**Source:** *Laboratory Materials*

### A.1 Infrastruttura LLVM e Analisi del Flusso di Controllo
L'attività pratica di laboratorio correda la comprensione teorica tramite l'uso della suite di compilatori LLVM e lo sviluppo di passate di analisi personalizzate in C++ o moduli Python.
*   **Rappresentazione intermedia di LLVM (LLVM IR):**
    *   LLVM IR adotta una forma fortemente tipizzata, indipendente dall'hardware, basata sulla rappresentazione Static Single Assignment (SSA) [COMP-01_RUST_COMPILATION.pdf, Slide 6, 8].
    *   Gli identificatori dei registri virtuali locali iniziano con `%` (es. `%t1`), mentre le variabili globali e le funzioni iniziano con `@` (es. `@main`).
*   **Strategie di Risoluzione dei Solver Dataflow:**
    Durante lo sviluppo pratico di risolutori dataflow per l'analisi di liveness o l'eliminazione di sottoespressioni comuni, si confrontano due distinte strategie algoritmiche d'esame [Laboratory, Slide 12]:
    1.  **Round-Robin Iterativo:** Valuta ciclicamente tutti i blocchi base del CFG uno dopo l'altro in una sequenza fissa ad ogni iterazione, fino a quando non viene rilevata alcuna variazione in nessuno stato (convergenza al punto fisso) [Data-FlowFirst.pdf, Slide 20]. Sebbene semplice da implementare, comporta un elevato numero di ricalcoli ridondanti per blocchi i cui set d'ingresso non hanno subito modifiche.
    2.  **Worklist Strategy (Algoritmo a Coda di Lavoro):** Utilizza una struttura dati dinamica (worklist) contenente esclusivamente i blocchi base i cui set informativi di output (o input, a seconda della direzione) hanno effettivamente subito una modifica nell'ultimo passaggio d'analisi [Laboratory, Slide 12].
        *   Ad ogni passo, il solver estrae un blocco dalla worklist, ne ricalcola la funzione di trasferimento e, se il set d'ingresso varia, aggiunge alla worklist tutti i suoi blocchi predecessori (per analisi Backward) o successori (per analisi Forward) [Laboratory, Slide 12].
        *   Questa euristica riduce drasticamente il numero di valutazioni necessarie, velocizzando significativamente la convergenza dell'algoritmo soprattutto su CFG complessi con loop nidificati.


### A.2 Materiali di Laboratorio
File del corso: `intro`, `llvm` / `llvm2` (IR LLVM), `cfg` (grafi del flusso di controllo), `dataflow` (solver per le analisi del Cap. 8), `optimizations`, `types`, `semantics`.
