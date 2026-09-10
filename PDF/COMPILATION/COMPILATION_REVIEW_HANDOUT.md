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
| Grammatica begin-end | §4.4 |
| Grammatica con alternative disgiunte S→AB\|eDa | fine Cap. 4 |
| Shift-reduce `x − 2 * y` | §5.4 |
| SheepNoise: `baa`, `baa baa` | §5.4 |
| Grammatica bcfa/bca (lookahead critici) | §5.4 |
| Grammatica attribuita `-101`; grammatica circolare | §6.2–6.3 |
| Costo di un basic block; type inference (2 esempi Yacc) | §6.4–6.5 |
| Liveness: 3 sweep backward | §8.5 |
| CPO/dominio formale della liveness ($Vars=\{a,b\}$) | §8.1bis |
| Reaching Definitions: fattoriale fino al fixpoint | §8.6 |
| LVN con value numbers; edge case del naming | §7.2 |
| MAXLIVE e spill con 3 registri | §11.2 |
| Coloring $k{=}3$; optimistic coloring $k{=}2$ | §11.3 |
| MIR del condizionale `let z = if …` | §12.4 |
| Dangling reference; move path; closure capture | §12.8 |
| uHaskell / Algorithm W | §12.16 |

---

<a id="cap1"></a>
<a id="cap1"></a>
## CAPITOLO 1: Introduzione e Architettura dei Compilatori

**Source:** _IntroMio.pdf_

> **Nota di revisione:** questo capitolo è stato ricontrollato per intero contro il testo completo di `IntroMio.pdf` (incluse le slide con diagrammi, fornite come immagini trascritte). Il nucleo era già corretto (definizioni compilatore/interprete, AOT/JIT, principi fondamentali, architettura a due/tre passate, front-end/back-end). Sono stati integrati sei blocchi di contenuto concreto assenti dalla stesura precedente: (1) il diagramma delle fasi del compilatore con lo strato "Infrastructure", (2) un secondo esempio concreto di analisi lessicale (tokenizzazione di un while-loop, con un token invalido), (3) un secondo esempio di AST (per lo stesso while-loop), (4) la tabella operazionale formale di ILOC, (5) il codice ILOC realmente generato per instruction selection/register allocation/instruction scheduling sull'esempio $a=(a\times2\times b\times c)\times d$ (con conteggio dei cicli prima/dopo lo scheduling), (6) l'esempio di loop-invariant code motion presentato nell'introduzione del corso.

### 1.1 Definizioni Formali e Concetti Fondamentali

- **Definizione di Compilatore (Compiler):** "un programma che prende altri programmi e li prepara per l'esecuzione"; più precisamente, un programma che traduce un programma sorgente in un linguaggio target, in genere l'instruction set di un'architettura hardware, oppure — nel caso dei _source-to-source translator_ — un altro linguaggio ad alto livello orientato all'uomo [IntroMio.pdf].
- **Compilatori vs Interpreti:** entrambi sono programmi che traducono codice scritto in un linguaggio ad alto livello in codice macchina; la differenza fondamentale è **quando e come** avviene la traduzione [IntroMio.pdf].
    - **Compilatore:** traduce l'intero programma in codice macchina _prima_ dell'esecuzione. Funzionamento: (1) si scrive il sorgente; (2) il compilatore traduce tutto il codice in un solo passaggio; (3) viene prodotto un file eseguibile; (4) l'eseguibile viene lanciato. Caratteristiche: la traduzione avviene una sola volta prima dell'esecuzione; il risultato è un programma eseguibile separato; l'esecuzione è generalmente più veloce; gli errori sono mostrati tutti insieme dopo la compilazione. Analogia della slide: compilare è come tradurre un intero libro prima di stamparlo — una volta tradotto lo si può leggere quante volte si vuole senza ritradurlo [IntroMio.pdf].
        
    - **Interprete:** legge il programma e i suoi dati di input e traduce/esegue riga per riga, a runtime. Funzionamento: (1) si scrive il sorgente; (2) l'interprete legge una riga; (3) la traduce ed esegue immediatamente; (4) passa alla riga successiva. Caratteristiche: la traduzione avviene durante l'esecuzione; non viene prodotto alcun file eseguibile separato; l'esecuzione è generalmente più lenta; gli errori appaiono immediatamente, interrompendo l'esecuzione. Analogia della slide: un interprete è come un traduttore simultaneo che traduce ogni frase mentre viene pronunciata [IntroMio.pdf].
        
    - **Tabella di confronto (slide):**
        
        ||Compilatore|Interprete|
        |---|---|---|
        |Traduzione|Tutto il programma in una volta|Riga per riga|
        |Output|Crea un file eseguibile|Nessun eseguibile separato|
        |Velocità di esecuzione|Più veloce|Più lenta|
        |Errori|Mostrati dopo la compilazione|Mostrati immediatamente|
        
        [IntroMio.pdf]
        
- **Proprietà dell'implementazione, non del linguaggio:** essere compilato o interpretato **non è una proprietà intrinseca del linguaggio**, ma della sua specifica implementazione [IntroMio.pdf]:
    - _C_ e _C++_ sono tipicamente compilati; _Scheme_ è tipicamente interpretato [IntroMio.pdf].
    - _Python_ è tipicamente interpretato, ma CPython compila prima il sorgente in bytecode per poi interpretarlo tramite macchina virtuale; PyPy usa la compilazione JIT; Cython o Nuitka traducono Python direttamente in codice C compilato [IntroMio.pdf].
    - _Java_ è sia compilato sia interpretato: `javac` compila il sorgente in bytecode, che la JVM può poi interpretare oppure compilare JIT in codice macchina nativo [IntroMio.pdf].
- **AOT (Ahead-Of-Time) vs JIT (Just-In-Time):** entrambe sono tecniche per tradurre codice in codice macchina; la differenza sta in **quando** avviene la traduzione [IntroMio.pdf].
    - **AOT:** la traduzione avviene interamente in anticipo, prima del runtime. Produce un eseguibile standalone, ha startup rapido, prestazioni prevedibili, nessun overhead di compilazione durante l'esecuzione. Analogia della slide: l'AOT è come cucinare un pasto completamente prima di servirlo [IntroMio.pdf].
    - **JIT:** la compilazione avviene durante l'esecuzione. Il codice parte interpretato o parzialmente compilato; le parti più eseguite ("hot spot") vengono identificate e compilate a runtime in codice nativo ottimizzato, con prestazioni che migliorano progressivamente. Startup più lento, ma può raggiungere prestazioni molto elevate adattandosi al comportamento reale del programma. Analogia della slide: il JIT è come iniziare a cucinare mentre gli ospiti stanno già mangiando, migliorando la ricetta a ogni ripetizione [IntroMio.pdf].

### 1.2 Perché Studiare i Compilatori, e Perché Sono Difficili

- **Motivazioni (slide):** comprensione profonda dei linguaggi di programmazione; ottimizzazione delle prestazioni (velocità/memoria); base per la progettazione di nuovi linguaggi; i compilatori sono il cuore di IDE, debugger, analizzatori statici; problem solving trasferibile ad altri campi (algoritmi, strutture dati); numerose opportunità di ricerca aperta, specie in programmazione parallela e analisi del codice [IntroMio.pdf].
- **La compilazione è interdisciplinare (slide):** attinge ad Intelligenza Artificiale (algoritmi greedy, ricerca euristica), Algoritmi (algoritmi su grafi, union-find, programmazione dinamica), Teoria (DFA e PDA, pattern matching, algoritmi a punto fisso), Sistemi (allocazione e naming, sincronizzazione, località), Architettura (gestione di pipeline e gerarchia di memoria, uso dell'instruction set) [IntroMio.pdf].
- **Riduzione del costo dell'astrazione (slide):** l'informatica è "l'arte di creare oggetti virtuali e renderli utili"; un compilatore ben scritto rende tale astrazione economicamente sostenibile — il costo di esecuzione dovrebbe riflettere il lavoro sottostante e non il modo in cui il programmatore ha scelto di scriverlo; un cambiamento nell'espressione dovrebbe comportare un piccolo cambiamento di prestazioni; non ci si può però aspettare che il compilatore inventi algoritmi migliori (non ci si aspetta che il compilatore trasformi un bubblesort in un quicksort) [IntroMio.pdf].
- **Citazione storica (John Backus, primo compilatore FORTRAN):** se il primo compilatore FORTRAN avesse prodotto codice anche solo la metà più lento del codice scritto a mano, l'accettazione del sistema sarebbe stata in serio pericolo, e l'adozione di linguaggi come FORTRAN sarebbe stata seriamente ritardata [IntroMio.pdf].

### 1.3 Principi Fondamentali della Compilazione

- **I due principi fondamentali (slide):**
    1. Il compilatore **deve preservare il significato** del programma che sta compilando [IntroMio.pdf].
    2. Il compilatore **deve migliorare** il programma di input in qualche modo percepibile [IntroMio.pdf].
- **Vista ad alto livello (slide):** un compilatore è una scatola nera Source Code → Compiler → Machine Code (con possibili Errori in output). Implicazioni: deve riconoscere programmi legali (e illegali); deve generare codice corretto; deve gestire lo storage di tutte le variabili (e del codice); deve concordare con OS e linker sul formato del codice oggetto — un grande salto rispetto al linguaggio assembly [IntroMio.pdf].

### 1.4 Architettura del Compilatore

- **Compilatore tradizionale a due passate (Two-pass compiler, slide):** $$\text{Source Code} \rightarrow \text{Front End} \xrightarrow{\text{IR}} \text{Back End} \rightarrow \text{Machine Code}$$ Il Front-End dipende principalmente dal linguaggio sorgente, il Back-End dipende principalmente dalla macchina target. Implicazioni della divisione: si usa una rappresentazione intermedia (IR); il Front-End mappa il sorgente legale in IR; il Back-End mappa l'IR in codice macchina target; l'uso di più passate consente codice migliore. **Il Front-End ha complessità $O(n)$ o $O(n \log n)$; il Back-End è NP-Completo** [IntroMio.pdf].
    
- **Vantaggi della divisione in due passate — Separation of Concerns (slide):** è un classico principio dell'ingegneria del software. Poiché l'IR incapsula tutta la conoscenza che il compilatore ha sul programma: **la stessa architettura (Front-End) può avere come target diverso codice macchina** — uno stesso Front-End può essere accoppiato a più Back-End differenti per generare codice per diverse macchine target; e **la stessa architettura (Back-End) può avere come target un diverso codice sorgente** — uno stesso Back-End può essere riusato per più linguaggi sorgente che condividono la stessa IR [IntroMio.pdf]. Questo evita di dover scrivere un compilatore dedicato per ogni coppia (linguaggio, macchina target).
    
- **Compilatore tradizionale a tre parti (Three-part compiler, slide):** si inserisce un **Ottimizzatore (Middle-End)** fra Front-End e Back-End: $$\text{Source Code} \rightarrow \text{Front End} \xrightarrow{\text{IR}} \text{Optimizer} \xrightarrow{\text{IR}} \text{Back End} \rightarrow \text{Machine Code}$$ Il compito dell'ottimizzatore (Code Improvement) è analizzare e trasformare l'IR; il suo obiettivo primario è ridurre il tempo di esecuzione del codice compilato, e/o ridurre lo spazio occupato, il consumo energetico, i page fault; **deve comunque preservare il "significato" del codice** [IntroMio.pdf].
    
- **Le fasi del compilatore in dettaglio, con l'infrastruttura condivisa (slide "The phases of a Compiler"):** ciascuna delle tre macro-fasi si articola a sua volta in componenti concrete:
    
    - **Front End:** _Scanner_ → _Parser_ → _Elaboration_ (elaborazione/analisi semantica).
    - **Optimizer:** una sequenza di passate _Optimization 1_, _Optimization 2_, …, _Optimization n_.
    - **Back End:** _Instruction Selection_ → _Instruction Scheduling_ → _Register Allocation_.
    
    Tutte le componenti di tutte e tre le fasi si appoggiano a un livello comune di **Infrastructure** (strutture dati condivise — symbol table, gestione degli errori, rappresentazione della IR, ecc.) [IntroMio.pdf]. **Nell'architettura reale, ciascuna fase è divisa in una serie di passate**; l'ottimizzatore in particolare contiene passate che usano analisi e trasformazioni distinte per migliorare il codice [IntroMio.pdf].
    

### 1.5 Il Front-End: Scanner, Parser, Grammatiche

- **Responsabilità del Front-End (slide):** riconoscere programmi legali (e illegali); segnalare gli errori in modo utile; produrre la IR e una mappa di storage preliminare; dare forma (shape) al codice per il resto del compilatore; buona parte della costruzione del Front-End può essere automatizzata [IntroMio.pdf].
    
- **Lo Scanner (analisi lessicale):** mappa il flusso di caratteri in un flusso di parole (_lexical analysis_); determina se il flusso di caratteri costituisce una parola legale; produce coppie _parola & parte del discorso_ — ad es. `x = x + y ;` diventa `<id,x> <op,=> <id,x> <op,+> <id,y> <op,;>`; parole tipiche includono numeri, identificatori, `+`, `–`, `new`, `while`, `if`. La velocità è importante: i testi accademici raccomandano la generazione automatica dello scanner, ma nella pratica commerciale gli scanner sono spesso scritti a mano [IntroMio.pdf].
    
- **Esempio concreto di analisi lessicale (slide "Lexical analysis"):** l'obiettivo è dividere il programma in singole parole dotate di senso. Per il frammento
    
    ```
    while (y < z) {
        int x = a + b;
        y += x; }
    ```
    
    lo scanner produce la sequenza di token:
    
    ```
    T_While, T_LeftParen, T_Identifier(y), T_Less, T_Identifier(z), T_RightParen, T_OpenBrace,
    T_Int, T_Identifier(x), T_Assign, T_Identifier(a), T_Plus, T_Identifier(b), T_Semicolon,
    T_Identifier(y), T_PlusAssign, T_Identifier(x), T_Semicolon, T_CloseBrace
    ```
    
    [IntroMio.pdf]. La slide sottolinea inoltre un caso di errore lessicale: **`1g2h3i` non è né un identificatore valido né un numero valido** — nessuna regola lessicale del linguaggio lo riconosce, quindi lo scanner lo segnalerebbe come errore [IntroMio.pdf].
    
- **Il Parser (analisi sintattica):** verifica la sintassi e segnala errori; determina se il flusso di parole è una frase legale del linguaggio sorgente; costruisce la IR per il programma sorgente. I parser scritti a mano sono relativamente facili da costruire, ma la maggior parte dei testi raccomanda l'uso di generatori automatici di parser [IntroMio.pdf].
    
- **Grammatiche per il Front-End (definizione formale, slide):** una grammatica $G = (S, N, T, P)$ dove $S$ è il simbolo iniziale, $N$ è l'insieme dei non-terminali, $T$ è l'insieme dei terminali (parole), $P$ è l'insieme delle produzioni o regole di riscrittura $P: N \rightarrow N \cup T$. È scritta in una variante della forma di Backus-Naur (BNF) [IntroMio.pdf].
    
- **SheepNoise, la grammatica "giocattolo" del corso (slide):**
    
    ```
    SheepNoise → SheepNoise baa
               | baa
    ```
    
    Definisce l'insieme dei belati che una pecora emette in circostanze normali [IntroMio.pdf]. Questa stessa grammatica ricompare come esempio guida per il parsing bottom-up LR(1) nel Cap. 5.
    
- **Grammatica per espressioni semplici (slide):**
    
    ```
    S = Goal                     1. Goal → Expr
    T = { number, id, +, - }     2. Expr  → Expr Op Term
    N = { Goal, Expr,            3.        | Term
          Term, Op }             4. Term  → number
    P = { 1, 2, 3, 4, 5, 6, 7 }  5.        | id
                                 6. Op    → +
                                 7.        | -
    ```
    
    Definisce espressioni semplici con `+` e `-` su numeri e identificatori; è un esempio di **grammatica context-free (CFG)** [IntroMio.pdf].
    
- **Derivazione di `x + 2 - y` (slide):** dato un CFG possiamo derivare frasi per sostituzione ripetuta; per _riconoscere_ una frase valida si inverte il processo, partendo da `x + 2 - y`:
    
    |Produzione|Risultato|
    |---|---|
    |—|`Goal`|
    |1|`Expr`|
    |2|`Expr Op Term`|
    |5|`Expr Op y`|
    |7|`Expr - y`|
    |2|`Expr Op Term - y`|
    |4|`Expr Op 2 - y`|
    |6|`Expr + 2 - y`|
    |3|`Term + 2 - y`|
    |5|`x + 2 - y`|
    
    [IntroMio.pdf]
    
- **Parse Tree vs Abstract Syntax Tree (AST) (slide):** per riconoscere se `x + 2 - y` appartiene al linguaggio si costruisce l'albero di parsing (_parsing tree_ o _syntax tree_), che include ogni non-terminale coinvolto nella derivazione [IntroMio.pdf]. I compilatori usano spesso un **Abstract Syntax Tree** al posto del parse tree: l'AST riassume la struttura grammaticale senza includere i dettagli della derivazione, è molto più conciso, e può essere usato direttamente come rappresentazione intermedia [IntroMio.pdf].
    
- **Secondo esempio di AST (slide "Syntax analysis"):** per il frammento già usato nell'esempio lessicale,
    
    ```
    while (y < z) {
        int x = a + b;
        y += x; }
    ```
    
    l'AST prodotto ha come radice `While`, con due figli: la condizione `<` (con figli `y`, `z`) e il corpo `Sequence`, che a sua volta ha due figli `=` — il primo con figli `x` e `+(a,b)`, il secondo con figli `y` e `+(y,x)` [IntroMio.pdf]. Questo esempio illustra concretamente come l'AST **elimini i dettagli della derivazione grammaticale** (non ci sono nodi per `Stmt`, `Block`, ecc.) mantenendo solo la struttura semantica rilevante — coerentemente con la nota della slide precedente ("l'AST riassume la struttura grammaticale senza includere il dettaglio della derivazione") [IntroMio.pdf].
    

### 1.6 La Rappresentazione Intermedia (IR): AST vs Codice a Tre Indirizzi

Consideriamo l'espressione sorgente `a = b × c + d` come esempio guida (slide):

- **Se la IR è l'Abstract Syntax Tree**, il Front-End produce un albero con radice `=`, il cui sottoalbero destro è `+`, con figli `×(b,c)` e `d` [IntroMio.pdf].
    
- **Se la IR è codice a tre indirizzi (Three-Address Code)**, considerando lo statement esteso `a = b×c+d; e = f + b×c+d`, il Front-End produce (slide):
    
    ```
    load  @b   ⇒ r1
    load  @c   ⇒ r2
    mult  r1,r2 ⇒ r3
    load  @d   ⇒ r4
    add   r3,r4 ⇒ r5
    store r5   ⇒ @a
    load  @f   ⇒ r6
    add   r5,r6 ⇒ r7
    store r7   ⇒ @e
    ```
    
    [IntroMio.pdf]. Si osservi come al risultato di ogni singola operazione binaria venga assegnato un nome esplicito (un registro virtuale `r_i`), consentendone il riutilizzo nelle istruzioni successive (`r5`, calcolato per `a`, viene riusato nel calcolo di `e`) — un vantaggio strutturale del three-address code rispetto a una rappresentazione a stack puro.
    
- **About ILOC (slide):** ILOC (_Intermediate Language for an Optimizing Compiler_) è un linguaggio assembly per una semplice macchina RISC, usato nel corso come forma concreta di codice a tre indirizzi [IntroMio.pdf]. **Tabella operazionale (slide "About ILOC"):**
    
    |Operazione ILOC|Significato|
    |---|---|
    |`loadAI r1,c2 ⇒ r3`|$\text{Memory}(r_1+c_2) \to r_3$|
    |`loadI c1 ⇒ r2`|$c_1 \to r_2$|
    |`mult r1,r2 ⇒ r3`|$r_1 \times r_2 \to r_3$|
    |`storeAI r1 ⇒ r2,c3`|$r_1 \to \text{Memory}(r_2+c_3)$|
    
    [IntroMio.pdf]. Questa tabella fornisce la semantica precisa delle istruzioni ILOC usate negli esempi di questo capitolo e nei Cap. 9–11.
    
- **L'ottimizzatore e il contesto (slide):** la IR emessa dal Front-End viene generata guardando ogni statement isolatamente, quindi contiene codice che deve funzionare per qualunque contesto circostante. L'ottimizzatore può invece scoprire proprietà del contesto osservando l'intera IR, e usare questa conoscenza per migliorare il codice [IntroMio.pdf].
    
- **Esempio di ottimizzazione — loop invariant code motion (slide "Example of optimizations: loop invariant"):** dato il codice
    
    ```
    b ← …
    c ← …
    a ← 1
    for i = 1 to n
        read d
        a ← a × (2 × b × c) × d
    end
    ```
    
    l'ottimizzatore riconosce che la sottoespressione `2 × b × c` è **costante rispetto al ciclo** (non dipende da `i` né da `d`, che cambia solo dentro il loop tramite `read`) e la issa (hoist) fuori dal ciclo in un nuovo temporaneo:
    
    ```
    b ← …
    c ← …
    a ← 1
    t ← 2 × b × c
    for i = 1 to n
        read d
        a ← a × d × t
    end
    ```
    
    [IntroMio.pdf]. Questo è il primo esempio concreto di loop-invariant code motion incontrato nel corso; la tecnica viene approfondita formalmente al Cap. 7 (§7.3) e applicata al calcolo di indirizzi array nei loop al Cap. 10 (§10.7).
    

### 1.7 Il Back-End: Instruction Selection, Register Allocation, Instruction Scheduling

- **Responsabilità del Back-End (slide):** tradurre la IR in codice macchina target; scegliere le istruzioni per implementare ogni operazione della IR; decidere quali valori mantenere nei registri; riordinare le istruzioni per guadagnare efficienza. L'automazione ha avuto meno successo nel Back-End che nel Front-End [IntroMio.pdf].
- **Instruction Selection:** deve tradurre il codice IR in una sequenza di istruzioni dell'ISA target, sfruttando le caratteristiche della macchina target; assume un numero infinito di registri (virtuali); è tipicamente vista come un problema di pattern matching (metodi ad-hoc o pattern matching); la forma della IR influenza la tecnica scelta; le architetture RISC hanno semplificato questo problema [IntroMio.pdf].
    - **Esempio concreto (slide "Instruction selection for a = (a × 2 × b × c) × d"):** il codice ILOC generato è:
        
        ```iloc
        loadAI  rarp, @a ⇒ ra    // load 'a'loadI   2        ⇒ r2    // constant 2 into r2loadAI  rarp, @b ⇒ rb    // load 'b'loadAI  rarp, @c ⇒ rc    // load 'c'loadAI  rarp, @d ⇒ rd    // load 'd'mult    ra, r2   ⇒ ra    // ra ← a × 2mult    ra, rb   ⇒ ra    // ra ← (a × 2) × bmult    ra, rc   ⇒ ra    // ra ← (a × 2 × b) × cmult    ra, rd   ⇒ ra    // ra ← (a × 2 × b × c) × dstoreAI ra       ⇒ rarp, @a  // write ra back to 'a'
        ```
        
        [IntroMio.pdf].
- **Register Allocation:** deve mappare i registri virtuali su registri fisici, gestendo un insieme limitato di risorse; può cambiare le scelte di istruzione e inserire istruzioni di LOAD/STORE aggiuntive quando i registri non bastano (_spilling_); **l'allocazione ottima è NP-Completa nella maggior parte dei contesti pratici**, per cui i compilatori ne approssimano la soluzione [IntroMio.pdf].
    - **Confronto concreto a 6 registri vs 3 registri (slide "Register allocation for a = (a × 2 × b × c) × d"):** la versione **non allocata** (una variabile per registro virtuale, 6 registri: $r_a,r_2,r_b,r_c,r_d$ più eventuali temporanei) coincide col codice di instruction selection sopra. La versione **allocata su soli 3 registri**, che riusa $r_1$ come accumulatore e $r_2$ come registro di scratch per ciascun operando caricato:
        
        ```iloc
        loadAI rarp, @a ⇒ r1      // load 'a'add    r1, r1   ⇒ r1      // r1 ← a × 2   (implementato come somma)loadAI rarp, @b ⇒ r2      // load 'b'mult   r1, r2   ⇒ r1      // r1 ← (a × 2) × bloadAI rarp, @c ⇒ r2      // load 'c'mult   r1, r2   ⇒ r1      // r1 ← (a × 2 × b) × cloadAI rarp, @d ⇒ r2      // load 'd'mult   r1, r2   ⇒ r1      // r1 ← (a × 2 × b × c) × dstoreAI r1      ⇒ rarp, @a  // write ra back to 'a'
        ```
        
        [IntroMio.pdf]. Il confronto rende esplicito il compromesso: usare **3 registri** invece di **6** riduce la pressione sui registri al prezzo di riusare (e quindi serializzare) $r_1$ e $r_2$ per più valori successivi.
- **Instruction Scheduling:** riordina la sequenza di istruzioni per evitare stalli e interlock, usando produttivamente tutte le unità funzionali disponibili; può aumentare il tempo di vita delle variabili, cambiando così l'allocazione dei registri; **la schedulazione ottima è NP-Completa in quasi tutti i casi**, ma esistono tecniche euristiche ben sviluppate [IntroMio.pdf].
    - **Esempio numerico completo (slide "Before/After the instruction scheduling"):** con costi `loadAI`/`storeAI` = 3 cicli, `mult` = 2 cicli, tutte le altre istruzioni (incluso `add`) = 1 ciclo, e assumendo la versione a 3 registri sopra:
        
        - **Prima della schedulazione** (esecuzione strettamente sequenziale, ogni istruzione attende il completamento della precedente): la tabella Start/End della slide mostra `loadAI` (cicli 1–3), `add` (4–4), `loadAI` (5–7), `mult` (8–9), `loadAI` (10–12), `mult` (13–14), `loadAI` (15–17), `mult` (18–19), `storeAI` (20–22) — **22 cicli totali** [IntroMio.pdf].
        - **Dopo la schedulazione** (le tre `loadAI` indipendenti vengono anticipate ed eseguite in parallelo/sovrapposte, sfruttando unità funzionali multiple): `loadAI` (1–3), `loadAI` (2–4), `loadAI` (3–5), `add` (4–4), `mult` (5–6), `loadAI` (6–8), `mult` (7–8), `mult` (9–10), `storeAI` (11–13) — **13 cicli totali** [IntroMio.pdf].
        
        Lo scheduling riduce il tempo totale da 22 a 13 cicli (una riduzione di circa il 41%) semplicemente riordinando le istruzioni indipendenti per sovrapporne l'esecuzione, senza alcuna modifica al risultato calcolato [IntroMio.pdf].
        

### 1.8 Esempi di Performance dell'Astrazione

- **Caso di studio (gcc 4.1, `-O3`, Intel T9600 @ 2.8GHz, array 10.000×10.000, slide "Simple Examples"):** tre varianti dello stesso azzeramento di matrice mostrano tempi di esecuzione molto diversi — **tutti e tre i loop hanno prestazioni distinte** [IntroMio.pdf]:
    
    - _Row-major traversal:_ `for(i) for(j) A[i][j]=0` → **0.51 s** ($\approx 5\times$ la versione a puntatore).
    - _Column-major traversal:_ `for(i) for(j) A[j][i]=0` → **1.65 s** ($\approx 15\times$ la versione a puntatore, per i continui cache miss).
    - _Forma a puntatore:_ `p=&A[0][0]; t=n*n; for(i<t) *p++=0;` → **0.11 s** (la più veloce).
    - _Libreria standard:_ `bzero((void*)&A[0][0], n*n*sizeof(int))` → **0.52 s** ($\approx 5\times$ più lento della forma a puntatore).
    
    Un buon compilatore dovrebbe conoscere questi trade-off, per ogni target, e generare sempre il codice migliore; **pochi compilatori reali ci riescono** [IntroMio.pdf].


<a id="cap2"></a>
## CAPITOLO 2: Fondamenti Formali dei Linguaggi e Automi

**Source:** _LinguaggiI.pdf_

> **Nota di revisione:** questo capitolo è stato ricontrollato per intero contro il testo integrale di `LinguaggiI.pdf` (fornito come testo semplice continuo, senza numerazione di pagina/slide affidabile — a differenza dei deck "a zip" con OCR per singola slide usati per altri capitoli). Per questo motivo le citazioni `[LinguaggiI.pdf, Slide N]` della versione precedente, che riportavano numerazioni specifiche, sono state sostituite da citazioni generiche `[LinguaggiI.pdf]`: non è possibile verificare a quale slide fisica corrisponda un dato passaggio, ma il contenuto stesso è stato confrontato riga per riga con la fonte. Sono stati integrati sette blocchi di contenuto assenti dalla stesura precedente: (1) gli esempi svolti di conversione DFA→RE con state elimination (inclusi i casi speciali "un solo stato finale" e "più stati finali"), (2) il "More Complex Example" e i due esercizi di minimizzazione DFA, (3) l'elenco completo degli esercizi sul Pumping Lemma regolare, (4) la definizione formale di Parse Tree con l'esempio guidato della grammatica booleana, (5) il secondo esempio di PDA (palindromo $ww^R$) e i relativi esercizi di design, (6) l'esempio completo di Grammatica Context-Sensitive per ${a^ib^ic^i}$, (7) il riepilogo esplicito della gerarchia dei linguaggi con automi corrispondenti. Il resto del capitolo (§2.1–2.5, §2.7 nucleo, §2.8 nucleo, §2.9 nucleo, §2.10 nucleo) era già corretto ed è qui preservato.

### 2.1 Alfabeti, Stringhe e Operazioni Formali

- **Definizione di Alfabeto (Alphabet):** Un alfabeto $\Sigma$ è un insieme finito e non vuoto di simboli [LinguaggiI.pdf].
    - _Esempi:_ $\Sigma_1 = {a, b, c, \dots, z}$ (lettere dell'alfabeto); $\Sigma_2 = {0, 1}$ (cifre binarie); $\Sigma_3 = {(, )}$ (parentesi tonde) [LinguaggiI.pdf].
- **Definizione di Stringa (String):** Una stringa su un alfabeto $\Sigma$ è una sequenza finita di simboli appartenenti a $\Sigma$ [LinguaggiI.pdf]. La _stringa vuota_, indicata con $\epsilon$, è la stringa priva di simboli [LinguaggiI.pdf].
- **Lunghezza di una stringa $|x|$:** Corrisponde al numero di simboli che compongono la stringa $x$ [LinguaggiI.pdf].
    - _Esempi:_ $|abfbz| = 5$; $|110010| = 6$; $|))()(()| = 7$; $|\epsilon| = 0$ [LinguaggiI.pdf].
- **Concatenazione di stringhe:** L'operazione che unisce due stringhe $x$ e $y$ accostandole per formare la stringa $xy$ [LinguaggiI.pdf]. È un'operazione associativa che ammette la stringa vuota $\epsilon$ come elemento neutro ($x\epsilon = \epsilon x = x$) [LinguaggiI.pdf].
- **Sottostringa, Prefisso e Suffisso:** Una stringa $s$ è una sottostringa di $x$ se esistono due stringhe $y$ e $z$ tali che $x = ysz$ [LinguaggiI.pdf].
    - Se $y = \epsilon$ (cioè $x = sz$), allora $s$ è un **prefisso** di $x$ [LinguaggiI.pdf].
    - Se $z = \epsilon$ (cioè $x = ys$), allora $s$ è un **suffisso** di $x$ [LinguaggiI.pdf].
    - $\epsilon$ è sia prefisso sia suffisso di qualsiasi stringa, inclusa $\epsilon$ stessa [LinguaggiI.pdf]. I prefissi di `abc` sono: $\epsilon$, `a`, `ab`, `abc` [LinguaggiI.pdf].
- **Potenze di un alfabeto (Powers of an alphabet):**
    - $\Sigma^n$ indica l'insieme di tutte le stringhe sull'alfabeto $\Sigma$ di lunghezza esattamente pari a $n$ [LinguaggiI.pdf]. Per definizione, $\Sigma^0 = {\epsilon}$ [LinguaggiI.pdf]. Esempio con $\Sigma={0,1}$: $\Sigma^0={\epsilon}$, $\Sigma^1={0,1}$, $\Sigma^2={00,01,10,11}$, $\Sigma^3={000,001,010,011,100,101,110,111}$ [LinguaggiI.pdf].
    - **Chiusura di Kleene (Kleene Closure) $\Sigma^*$:** L'insieme di tutte le stringhe di qualsiasi lunghezza finita (inclusa la stringa vuota) sull'alfabeto $\Sigma$ [LinguaggiI.pdf]: $$\Sigma^* = \bigcup_{i=0}^{\infty} \Sigma^i$$
    - **Chiusura Positiva (Positive Closure) $\Sigma^+$:** L'insieme di tutte le stringhe sull'alfabeto $\Sigma$ ad esclusione della stringa vuota [LinguaggiI.pdf]: $$\Sigma^+ = \bigcup_{i=1}^{\infty} \Sigma^i = \Sigma^* \setminus {\epsilon}$$

### 2.2 Teoria dei Linguaggi e Grammatiche Generative

- **Definizione di Linguaggio (Language):** Un linguaggio $L$ su un alfabeto $\Sigma$ è un sottoinsieme di $\Sigma^_$ ($L \subseteq \Sigma^_$) [LinguaggiI.pdf].
    - _Esempi (slide):_ $L_1$ = insieme delle stringhe su $\Sigma_1$ che contengono la sottostringa "fool"; $L_2$ = insieme delle stringhe su $\Sigma_2$ che rappresentano un numero binario divisibile per 7 ($={111, 10001, 10101,\dots}$); $L_3$ = insieme delle stringhe su $\Sigma_3$ dove ogni '(' è seguita esattamente da 2 occorrenze di ')' ($={\epsilon, ), )), ()), )()), \dots}$); $L_4$ = numeri binari corrispondenti a un numero primo ($={10,11,101,111,1011,1101,\dots}$); $L_5$ = insieme delle parole legali inglesi; $L_6$ = insieme dei programmi C legali [LinguaggiI.pdf].
- **Operazioni sui linguaggi:** Poiché i linguaggi sono insiemi, ereditano le operazioni standard della teoria degli insiemi (Unione $A \cup B$, Intersezione $A \cap B$, Differenza $A \setminus B$ quando $B\subseteq A$, Complemento $\bar{A} = \Sigma^* \setminus A$) [LinguaggiI.pdf]. Sono definite inoltre:
    - **Concatenazione di linguaggi:** $AB = {ab \mid a \in A \land b \in B}$; esempio: ${0,1}{1,2}={01,02,11,12}$ [LinguaggiI.pdf].
    - **Chiusura di Kleene $L^*$ e chiusura positiva $L^+$:** $$L^* = \bigcup_{i=0}^{\infty} L^i, \quad \text{dove } L^0 = {\epsilon} \qquad\qquad L^+ = \bigcup_{i=1}^{\infty} L^i$$ [LinguaggiI.pdf]. Nota: il linguaggio vuoto $\emptyset \neq {\epsilon}$ (il linguaggio contenente solo la stringa vuota) [LinguaggiI.pdf].
    - _Ulteriori esempi (slide):_ l'insieme delle stringhe con $n$ occorrenze di 1 seguite da $n$ occorrenze di 0 (${\epsilon, 01, 0011, 000111,\dots}$); l'insieme delle stringhe con un numero uguale di occorrenze di 0 e 1 (${\epsilon,01,10,0011,0101,1001,\dots}$) [LinguaggiI.pdf].
- **Il problema fondamentale (slide "Problems"):** data una stringa $w$, appartiene al linguaggio $L$? Due approcci: generare tutte le parole di $L$ e verificare se $w$ è tra queste, oppure disporre di un modo per _riconoscere_ quando una parola appartiene a $L$ [LinguaggiI.pdf].
- **L'approccio generativo — Grammatiche:** partendo da un simbolo iniziale, usando le regole di riscrittura delle produzioni, si genera l'insieme di tutte le stringhe appartenenti al linguaggio [LinguaggiI.pdf].
- **Definizione di Grammatica:** Una grammatica $G$ è definita formalmente come una quadrupla: $$G = (\Sigma, N, S, P)$$ dove $\Sigma$ è l'alfabeto dei simboli terminali, $N$ è l'insieme dei simboli non terminali, $S \in N$ è il simbolo non terminale iniziale (starting symbol) e $P$ è l'insieme finito di regole di produzione (rewriting rules) della forma $U \rightarrow V$, con $U \in (\Sigma \cup N)^+$ e $V \in (\Sigma \cup N)^*$ [LinguaggiI.pdf].
- **Derivazioni e linguaggio generato:** una stringa $w \in \Sigma^*$ è generata da $G$ se esiste una derivazione che parte da $S$ e, riscrivendo ripetutamente tramite le produzioni di $P$, produce $w$. Il linguaggio generato da $G$, denotato $L(G)$, è l'insieme di tutte le stringhe derivabili usando $G$ [LinguaggiI.pdf].
- **Esempio guida (slide, grammatica banale):** $G=({a},{S},S,P)$ con $P = {S\to\epsilon,\ S\to a,\ S\to aS}$ genera $L(G)={a^n\mid n\ge0}$ [LinguaggiI.pdf].
- **Esempio guida — linguaggio con numero pari di 1 (slide):** $L_1$ = insieme delle stringhe con un numero pari di 1. Generata dalla grammatica $({0,1},{S,T},S,P)$ con:
    
    ```
    S → ε | 0S | 1TT → 0T | 1S
    ```
    
    Una stringa appartiene a $L_1$ se e solo se può essere generata da questa grammatica [LinguaggiI.pdf].
- **Esempio di derivazione (slide):** la stringa `01010` appartiene a $L_1$? Si trova la derivazione: $$S \to 0S \to 01T \to 010T \to 0101S \to 01010S \to 01010$$ [LinguaggiI.pdf].

### 2.3 La Gerarchia di Chomsky e Complessità

La Gerarchia di Chomsky classifica le grammatiche in quattro classi (Tipi) in base alle restrizioni applicate alla forma delle produzioni $U \rightarrow V$ (con $U \in (\Sigma \cup N)^+$ e $V \in (\Sigma \cup N)^*$) [LinguaggiI.pdf]. Una lingua è "di un tipo" se e solo se ammette una grammatica di quel tipo:

1. **Tipo 0 (Unrestricted / Phrase-Structure):** Nessuna restrizione sulle produzioni. Riconosciute dalle **Macchine di Turing** [LinguaggiI.pdf].
2. **Tipo 1 (Context-Sensitive):** vedi §2.11bis per la forma esatta e un esempio completo. Riconosciute dagli **automi a spazio limitato (Linear Bounded Automata, LBA)** [LinguaggiI.pdf].
3. **Tipo 2 (Context-Free):** Regole della forma $A \rightarrow V$ con $A \in N$ (la parte sinistra deve essere un singolo non-terminale). Riconosciute dagli **Automi a Pila (Pushdown Automata - PDA)** [LinguaggiI.pdf].
4. **Tipo 3 (Regular):** Regole della forma $A \rightarrow aB$ oppure $A \rightarrow a$ (Grammatiche Regolari Destre). Riconosciute dagli **Automi a Stati Finiti (FSA)** [LinguaggiI.pdf].

#### Tabella di Decidibilità e Complessità dei Problemi d'Esame:

- **Membership ($w \in L(G)$?):** Decidibile in tempo polinomiale ($P$) per i linguaggi Regolari e Context-Free. Decidibile in spazio polinomiale ($PSPACE$) per i Context-Sensitive. Non decidibile ($U$ — Undecidable) per il Tipo 0 [LinguaggiI.pdf].
- **Emptiness ($L(G) = \emptyset$?):** Decidibile in tempo polinomiale ($P$) per Regolari e Context-Free. Non decidibile ($U$) per i Tipi 1 e 0 [LinguaggiI.pdf].
- **Equivalenza/Inclusione ($L(G_1) \subseteq L(G_2)$?):** Decidibile in $PSPACE$ per i linguaggi regolari. Non decidibile ($U$) per tutti gli altri livelli della gerarchia [LinguaggiI.pdf].

#### Esempi della Gerarchia (slide "Examples of Language Hierarchy")

La potenza espressiva cresce strettamente: $\text{regular} \subset \text{context-free} \subset \text{context-sensitive} \subset \text{phrase-structure}$ [LinguaggiI.pdf]:

- $L_1 = {$stringhe su ${0,1}$ con un numero pari di 1$}$ è **regolare** [LinguaggiI.pdf].
- $L_2 = {a^nb^n \mid n\in\mathbb{N}}$ è **context-free ma non regolare** (dimostrato col Pumping Lemma regolare, §2.8) [LinguaggiI.pdf].
- $L_3 = {a^nb^nc^n \mid n\in\mathbb{N}}$ è **context-sensitive ma non context-free** (dimostrato col Pumping Lemma per CF, §2.10) [LinguaggiI.pdf].

#### Relazione fra Linguaggi e Automi

Un linguaggio è regolare $\iff$ accettato da un automa a stati finiti; context-free $\iff$ accettato da un automa a pila (PDA); context-sensitive $\iff$ accettato da un automa a spazio lineare limitato (Linear Bounded Automaton); phrase-structure $\iff$ accettato da una Macchina di Turing [LinguaggiI.pdf].

### 2.4 Automi a Stati Finiti e Cinque Formalismi Equivalenti

I cinque formalismi equivalenti per rappresentare e riconoscere un linguaggio regolare sono:

1. **Grammatiche Regolari (RG)** [LinguaggiI.pdf].
2. **Automi a Stati Finiti Deterministici (DFA)** [LinguaggiI.pdf].
3. **Automi a Stati Finiti Non Deterministici (NFA)** [LinguaggiI.pdf].
4. **Automi a Stati Finiti Non Deterministici con $\epsilon$-transizioni ($\epsilon$-NFA)** [LinguaggiI.pdf].
5. **Espressioni Regolari (RE)** [LinguaggiI.pdf].

- **Definizione di Grammatica Regolare Destra (Right Regular Grammar):** Una grammatica in cui ogni produzione ha la forma $A \rightarrow aB$ o $A \rightarrow a$ (con $A, B \in N$ e $a \in \Sigma$). Solo per il simbolo iniziale è ammessa la produzione $S \rightarrow \epsilon$ [LinguaggiI.pdf].
    - _Esempio (slide):_ $G=({a,b},{S,B},S,P)$ con $P={S\to aS\mid aB,\ B\to bB\mid b}$ genera $L(G)={a^nb^m\mid n,m>0}$ [LinguaggiI.pdf].
- **Definizione Formale di DFA:** Un Automa a Stati Finiti Deterministico $M$ è una quintupla: $$M = (Q, \Sigma, \delta, q_0, F)$$ dove $Q$ è un insieme finito di stati, $\Sigma$ è l'alfabeto di input, $\delta: Q \times \Sigma \rightarrow Q$ è la funzione di transizione deterministica, $q_0 \in Q$ è lo stato iniziale, $F \subseteq Q$ è l'insieme degli stati finali o accettanti [LinguaggiI.pdf]. La funzione estesa alle stringhe $\hat{\delta}: Q \times \Sigma^* \rightarrow Q$ è definita per induzione: $$\hat{\delta}(q, \epsilon) = q, \quad \hat{\delta}(q, wa) = \delta(\hat{\delta}(q, w), a)$$ Una stringa $x$ è accettata se $\hat{\delta}(q_0, x) \in F$, e $L(M)={x\in\Sigma^*\mid\hat\delta(q_0,x)\in F}$ [LinguaggiI.pdf].
- **Definizione Formale di NFA:** Un Automa a Stati Finiti Non Deterministico ammette transizioni multiple per lo stesso simbolo. Si differenzia dal DFA unicamente per la funzione di transizione, che restituisce un insieme di stati: $$\delta: Q \times \Sigma \rightarrow \mathcal{P}(Q)$$ [LinguaggiI.pdf]. Una stringa $w$ è accettata se l'insieme di stati raggiungibili interseca gli stati accettanti: $\hat{\delta}(q_0, w) \cap F \neq \emptyset$, cioè $L(M)={x\in\Sigma^*\mid\hat\delta(q_0,x)\cap F\neq\emptyset}$ [LinguaggiI.pdf]. Un fatto centrale (slide): **gli NFA non espandono la classe dei linguaggi accettabili** rispetto ai DFA [LinguaggiI.pdf].

### 2.5 Algoritmi di Trasformazione Costruttiva

- **Da Grammatiche Regolari a NFA (Theorem 1):** Dato $RG = (\Sigma, N, S, P)$, si costruisce l'equivalente $NFA = (N \cup {F_{new}}, \Sigma, \delta, S, F_{NFA})$ in cui:
    1. Se $A \rightarrow a \in P \Rightarrow \delta(A,a) \ni F_{new}$ [LinguaggiI.pdf].
    2. Se $A \rightarrow aB \in P \Rightarrow \delta(A,a) \ni B$ [LinguaggiI.pdf].
    3. $F_{NFA} = {F_{new}} \cup {S}$ se $S \rightarrow \epsilon \in P$, altrimenti $F_{NFA} = {F_{new}}$ [LinguaggiI.pdf].
- **Da NFA a Grammatiche Regolari (Theorem 2):** Dato $NFA = (Q, \Sigma, \delta, q_0, F)$, si costruisce l'equivalente $RG = (\Sigma, Q', q_0', P)$:
    1. **Transizioni:** se $B \in \delta(A, a)$, si aggiunge $A \rightarrow aB$ a $P$.
    2. **Stati finali:** se $B \in F$, si aggiunge anche $A \rightarrow a$ a $P$.
    3. **Stringa vuota:** se $q_0 \in F$ (cioè $\epsilon \in L$), si introduce un nuovo simbolo iniziale $q$ ($Q'=Q\cup{q}$), si aggiungono $q\to q_0\mid\epsilon$, e $q_0'=q$; altrimenti $Q'=Q$ e $q_0'=q_0$ [LinguaggiI.pdf].
- **Da NFA a DFA (Subset Construction):** Dato $M_N = (Q_N, \Sigma, \delta_N, q_0, F_N)$, si costruisce $M_D = (Q_D, \Sigma, \delta_D, q_D, F_D)$:
    1. $Q_D = \mathcal{P}(Q_N)$ [LinguaggiI.pdf].
    2. $q_D = {q_0}$ [LinguaggiI.pdf].
    3. $\delta_D(P, a) = \bigcup_{p \in P} \delta_N(p, a)$ per ciascun $P \in Q_D$, $a\in\Sigma$ [LinguaggiI.pdf].
    4. $F_D = {P \in Q_D \mid P \cap F_N \neq \emptyset}$ [LinguaggiI.pdf].
    5. Si eliminano tutti i macro-stati non raggiungibili a partire da $q_D$ [LinguaggiI.pdf].
- **$\epsilon$-NFA ed eliminazione transizioni:**
    - Un $\epsilon$-NFA consente transizioni spontanee sulla stringa vuota $\epsilon$; formalmente $\delta:Q\times(\Sigma\cup{\epsilon})\to\mathcal P(Q)$ [LinguaggiI.pdf].
    - **$\epsilon$-closure:** l'insieme di tutti gli stati raggiungibili da $q$ (incluso $q$ stesso) effettuando esclusivamente zero o più transizioni su $\epsilon$; si estende a insiemi di stati come $\epsilon\text{-closure}(P)=\bigcup_{p\in P}\epsilon\text{-closure}(p)$ [LinguaggiI.pdf].
    - La funzione estesa è $\hat\delta(q,\epsilon)=\epsilon\text{-closure}(q)$, $\hat\delta(q,wa)=\bigcup_{p\in\hat\delta(q,w)}\epsilon\text{-closure}(\delta(p,a))$; si noti che in generale $\hat\delta(q,a)\ne\delta(q,a)$ [LinguaggiI.pdf].
    - **Conversione da $\epsilon$-NFA a NFA:** Dato $M = (Q, \Sigma, \delta, q_0, F)$, si costruisce l'NFA equivalente $M' = (Q, \Sigma, \delta', q_0, F')$ ponendo:
        1. $\delta'(q, a) = \hat{\delta}(q, a)$ [LinguaggiI.pdf].
        2. $F' = F \cup {q_0}$ se $\epsilon\text{-closure}(q_0) \cap F \neq \emptyset$, altrimenti $F' = F$ [LinguaggiI.pdf].

#### Esempio Svolto di Determinizzazione (slide)

NFA su $\Sigma = {0,1}$ con $F = {q_2}$:

|$\delta_N$|0|1|
|---|---|---|
|$\to q_0$|${q_0}$|${q_0, q_1}$|
|$q_1$|${q_1}$|${q_0, q_2}$|
|$*q_2$|${q_1, q_2}$|${q_0, q_1, q_2}$|

Costruzione dei **soli sottoinsiemi raggiungibili**:

1. $s_0 = {q_0}$: su 0 → ${q_0} = s_0$; su 1 → ${q_0, q_1} = s_1$ (nuovo);
2. $s_1 = {q_0, q_1}$: su 0 → ${q_0} \cup {q_1} = s_1$; su 1 → ${q_0,q_1} \cup {q_0,q_2} = {q_0,q_1,q_2} = s_2$ (nuovo);
3. $s_2 = {q_0, q_1, q_2}$: su 0 e su 1 → $s_2$ (stato pozzo).

|$\delta_D$|0|1|
|---|---|---|
|$\to s_0 = {q_0}$|$s_0$|$s_1$|
|$s_1 = {q_0, q_1}$|$s_1$|$s_2$|
|$*s_2 = {q_0, q_1, q_2}$|$s_2$|$s_2$|

Finali = i macro-stati contenenti $q_2$ (solo $s_2$). Linguaggio riconosciuto: $L = {x \in {0,1}^* \mid x \text{ contiene almeno 2 occorrenze di } 1}$ [LinguaggiI.pdf]. (La tabella completa su $\mathcal{P}(Q_N)$ mostrerebbe che la maggior parte degli stati è irraggiungibile — la slide sottolinea esplicitamente questo punto come motivazione per costruire solo i sottoinsiemi effettivamente raggiungibili [LinguaggiI.pdf].)

#### Esempio Svolto: da $\epsilon$-NFA a NFA

$\epsilon$-NFA $M=({q_0,q_1,q_2,q_3,q_4},{0,1,\epsilon},\delta,q_0,{q_1,q_2,q_3})$ (slide): da $q_0$ si diramano transizioni $\epsilon$ verso $q_1$ e $q_3$, oltre a una transizione $\epsilon$ interna; $q_1\xrightarrow{0}q_1$; $q_2\xrightarrow{1}q_2$; $q_3\xrightarrow{0}q_4$; $q_4\xrightarrow{1}q_3$ [LinguaggiI.pdf]. Applicando la conversione (§2.5): la matrice di transizione dell'NFA equivalente $M'$ risulta

|$\delta'$|0|1|
|---|---|---|
|$q_0$|${q_1,q_4}$|${q_2}$|
|$q_1$|${q_1}$|$\emptyset$|
|$q_2$|$\emptyset$|${q_2}$|
|$q_3$|${q_4}$|$\emptyset$|
|$q_4$|$\emptyset$|${q_3}$|

con $F' = F \cup {q_0} = {q_0,q_1,q_2,q_3}$, poiché $\epsilon\text{-closure}(q_0)={q_0,q_1,q_3}$ interseca $F={q_1,q_2,q_3}$ [LinguaggiI.pdf].

### 2.6 Espressioni Regolari (RE) e Ulteriori Conversioni

- **Definizione induttiva di RE (slide):** dato un alfabeto finito $\Sigma$, sono espressioni regolari: $\emptyset$ (denota l'insieme vuoto), $\epsilon$ (denota ${\epsilon}$), ogni $a\in\Sigma$ (denota ${a}$). Se $r,s$ sono RE che denotano gli insiemi $R,S$, allora $(r+s)$, $(rs)$ e $r^_$ denotano rispettivamente $R\cup S$, $RS$ e $R^_$. $L(r)$ indica il linguaggio denotato da $r$ [LinguaggiI.pdf].
    
- **Esempi di RE (slide):**
    
    - $a\mid b^_$ denota ${\epsilon,\text{"a"},\text{"b"},\text{"bb"},\dots}$ — attenzione: qui l'unione lega più debolmente della concatenazione/Kleene, quindi è $a \mid (b^_)$, non $(a\mid b)^*$ [LinguaggiI.pdf].
    - $(a+b)^*$ denota l'insieme con $\epsilon$ e tutte le stringhe formate da "a" e "b" [LinguaggiI.pdf].
    - $ab^*(c+\epsilon)$ denota l'insieme delle stringhe che iniziano con "a", poi zero o più "b", e infine opzionalmente una "c" [LinguaggiI.pdf].
    - $(0+(1(01^_0)^_1))^_$ e $(0^_+1^_+(01)^_)$ sono esempi ulteriori; quest'ultimo denota il linguaggio ${0,11,110,1001,1100,1111,\dots}$ [LinguaggiI.pdf].
- **Da RE a $\epsilon$-NFA (Thompson's Inductive Construction, slide):**
    
    - _Casi base:_ per $\emptyset$ (automa senza transizioni accettanti), per $\epsilon$ (due stati uniti da una transizione $\epsilon$), per $a\in\Sigma$ (due stati uniti da una transizione $a$) [LinguaggiI.pdf].
    - _Unione $R=S+T$:_ un nuovo stato iniziale e un nuovo stato finale, connessi in parallelo agli automi di $S$ e $T$ tramite transizioni $\epsilon$ [LinguaggiI.pdf].
    - _Concatenazione $R=ST$:_ si collega lo stato finale dell'automa di $S$ allo stato iniziale dell'automa di $T$ [LinguaggiI.pdf].
    - _Chiusura di Kleene $R=S^_$:* si introduce un nuovo stato iniziale/finale con un ciclo di transizioni $\epsilon$ che permette di ripetere l'automa di $S$ un numero arbitrario di volte, incluso zero [LinguaggiI.pdf].
    - **Esempio svolto — conversione di $R=(ab+a)^*$ (slide):** si procede per passi, costruendo dapprima gli automi elementari per $a$ e $b$, poi $ab$ (concatenazione), poi $ab+a$ (unione con l'automa di $a$), infine $(ab+a)^*$ applicando la costruzione della chiusura di Kleene attorno all'intero automa di $ab+a$ [LinguaggiI.pdf].
- **Da DFA a RE (State Elimination Method, Theorem 3):** per ogni DFA $D$ esiste una RE $r$ tale che $L(D)=L(r)$. Si eliminano progressivamente gli stati intermedi (né iniziali né finali) dell'automa, riscrivendo le etichette degli archi come espressioni regolari. Data la figura con stato da eliminare $s$, stati residui $q_1,\dots,q_k$ (con archi entranti $R_{i1},\dots,R_{ik}$ verso $s$) e $p_1,\dots,p_m$ (con archi uscenti $Q_1,\dots,Q_k$ da $s$), un self-loop $S$ su $s$, e archi diretti preesistenti $R_{ij}$ da $q_i$ a $p_j$, la nuova etichetta è: $$R_{ij} ; := ; R_{ij} + Q_i, S^{*}, P_j$$ Il processo si ripete eliminando uno stato intermedio per volta [LinguaggiI.pdf].
    
    - **Caso speciale — un solo stato finale coincidente con l'iniziale:** se, dopo l'eliminazione di tutti gli stati intermedi, resta un solo stato che è sia iniziale sia finale, con un self-loop etichettato $R$, l'espressione regolare cercata è semplicemente $R^*$ [LinguaggiI.pdf].
    - **Caso speciale — un solo stato finale diverso dall'iniziale:** con stato iniziale $S$ e stato finale diverso $T$, e archi rimasti etichettati $R$ (self-loop su $S$), $S$ (arco $S\to T$), $U$ (self-loop su $T$), $T$ (arco $T\to S$), l'automa si descrive come: $$(R+SU^*T)^_SU^_$$ [LinguaggiI.pdf].
    - **Caso generale — più stati finali:** con uno stato iniziale e $n$ stati finali $s_1,\dots,s_n$, si ripetono i passi precedenti per ciascun $s_i$ rendendo temporaneamente non finale ogni altro stato finale, ottenendo $n$ espressioni regolari distinte $R_1,\dots,R_n$; l'espressione regolare finale cercata è la loro unione: $$R_1 + R_2 + \dots + R_n$$ [LinguaggiI.pdf].
- **Esempio Svolto 1 — DFA con 3 stati (slide "DFA→RE Example"):** automa con stato iniziale 3, stato intermedio 1, stato finale 2 (etichette $0,1$ sugli archi secondo lo schema della slide). Eliminando lo stato intermedio si ottiene prima la forma con archi $0{+}10$ (self-loop sul nuovo stato iniziale) e $11$, poi $0{+}1$ sul residuo; l'espressione regolare finale sintetizzata è: $$(0+10)^_,11,(0+1)^_$$ [LinguaggiI.pdf].
    
- **Esempio Svolto 2 — automa che accetta un numero pari di 1 (slide "Another Example"):** automa a 3 stati (1 iniziale, 2, 3), che riconosce le stringhe con un numero pari di occorrenze di 1. Eliminando lo stato 2 si ottiene un automa a 2 stati (1 iniziale/finale, 3 finale) con archi etichettati $0$ (self-loop su 1), $0{+}10^*1$ (self-loop su 3), $10^_1$ (arco $1\to3$). Poiché ci sono **due stati finali** (1 e 3), si applica il caso generale: si ottengono $R_1=0^_$ (rendendo non finale lo stato 3) e $R_2=0^*10^_1(0+10^_1)^_$ (rendendo non finale lo stato 1); l'espressione regolare sintetizzata finale è: $$0^_ + 0^*10^*1(0+10^_1)^_$$ [LinguaggiI.pdf].
    
- **Esercizi di conversione DFA→RE (slide, senza soluzione nelle slide originali):**
    
    1. $Q={q_0,q_1,q_2}$, $q_0$ iniziale, $q_2$ finale, con $\delta(q_0,a){=}q_1$, $\delta(q_0,b){=}q_0$, $\delta(q_1,a){=}q_1$, $\delta(q_1,b){=}q_2$, $\delta(q_2,a){=}q_1$, $\delta(q_2,b){=}q_0$ [LinguaggiI.pdf].
    2. $Q={p_0,p_1,p_2,p_3}$, $p_0$ iniziale e finale, con $\delta(p_0,0){=}p_0$, $\delta(p_0,1){=}p_1$, $\delta(p_1,0){=}p_2$, $\delta(p_1,1){=}p_0$, $\delta(p_2,0){=}p_1$, $\delta(p_2,1){=}p_2$, $\delta(p_3,0){=}p_3$, $\delta(p_3,1){=}p_3$ [LinguaggiI.pdf].
    
    > **Nota metodologica:** questi due esercizi sono posti nelle slide senza soluzione fornita; non risolverli qui per rispettare la loro natura di esercizio d'auto-verifica, coerentemente con l'impostazione generale della dispensa quando la fonte lascia un esercizio aperto.
    

### 2.7 Algoritmo di Minimizzazione del DFA

Consente di trovare il DFA minimo equivalente riducendo il numero di stati. Si basa sul concetto di stati indistinguibili [LinguaggiI.pdf].

- **Algoritmo Pairwise DISTINCT-Table:**
    
    1. **Inizializzazione:** si crea una tabella triangolare inferiore `DISTINCT` per tutte le coppie di stati $(p,q)$ con $p\ne q$, inizialmente vuota.
    2. **Passo base:** se $p$ è finale e $q$ non lo è (o viceversa), $DISTINCT[p,q]=\epsilon$ [LinguaggiI.pdf].
    3. **Passo induttivo:** si itera finché non si verifica più alcun cambiamento; per ogni coppia $(p,q)$ con cella ancora vuota e ogni $a\in\Sigma$: se $DISTINCT[\delta(p,a),\delta(q,a)]$ non è vuota, allora $DISTINCT[p,q]=a$ [LinguaggiI.pdf].
    4. **Fusione:** le coppie rimaste con cella vuota sono indistinguibili (equivalenti) e vengono fuse in un unico stato del DFA minimo [LinguaggiI.pdf].
    
    - **Complessità:** $O(k\cdot n^2)$, con $n=|Q|$, $k=|\Sigma|$ [LinguaggiI.pdf].
- **Algoritmo di Hopcroft:** esiste un algoritmo più complesso, basato sulla partizione progressiva, con complessità ottima $O(k\cdot n\log n)$; l'algoritmo di riferimento per gli esercizi d'esame resta però quello pairwise sopra descritto [LinguaggiI.pdf].

#### Esempio Svolto "Very Simple" (slide: DFA per $(a|b)^+$)

DFA con $s_0$ iniziale (non finale) e $s_1,s_2$ finali, entrambi raggiungibili da $s_0$ su $a$ o $b$:

1. **Passo base:** $DISTINCT[s_0,s_1]=\epsilon$, $DISTINCT[s_0,s_2]=\epsilon$ (finale vs non finale).
2. **Loop principale:** nessuna coppia a cella vuota ha transizioni verso celle già marcate ⇒ nessun cambiamento.
3. **Fusione:** $DISTINCT[s_1,s_2]$ resta vuota ⇒ $s_1\equiv s_2$: si fondono in un unico stato (con self-loop su $a,b$); il DFA minimo ha **2 stati** [LinguaggiI.pdf].

#### "More Complex Example" e Sfida d'Esame (slide)

Oltre all'esempio "very simple" sopra, la slide presenta un secondo esempio più articolato ("More Complex Example"), risolto seguendo lo stesso schema: (1) si marcano con $\epsilon$ tutte le coppie stato-finale/stato-non-finale; (2) alla prima iterazione del loop principale si propagano le prime distinzioni indotte dalle transizioni verso coppie già marcate; (3) a una seconda iterazione si propagano ulteriori distinzioni derivate; (4) una terza iterazione non produce più cambiamenti (le celle rimaste vuote sono le coppie equivalenti); si combinano infine gli stati equivalenti per ottenere il DFA minimizzato [LinguaggiI.pdf]. Lo schema generale — passo base, iterazione fino al punto fisso, poi fusione — è identico indipendentemente dalla dimensione dell'automa.

**Esercizi di minimizzazione (slide, senza soluzione nelle slide originali):**

1. Automa a 8 stati ${A,\dots,H}$ con transizioni su ${0,1}$: $A{\to}(B,A)$, $B{\to}(A,C)$, $C{\to}(D,B)$, $D{\to}(D,A)$, $E{\to}(D,F)$, $F{\to}(G,E)$, $G{\to}(F,G)$, $H{\to}(G,H)$ [LinguaggiI.pdf].
    
2. Automa a 9 stati ${A,\dots,I}$ con transizioni su ${0,1}$: $A{\to}(B,E)$, $B{\to}(C,F)$, $C{\to}(D,H)$, $D{\to}(E,H)$, $E{\to}(F,I)$, $F{\to}(G,B)$, $G{\to}(H,B)$, $H{\to}(I,C)$, $I{\to}(A,E)$ [LinguaggiI.pdf].
    
    > **Nota metodologica:** anche questi esercizi restano aperti nelle slide originali; sono qui riportati per completezza come materiale di autoverifica, senza soluzione risolta.
    

### 2.8 Proprietà di Chiusura e Limiti dei Linguaggi Regolari

- **Proprietà di Chiusura:** i linguaggi regolari sono chiusi rispetto a Unione, Concatenazione, Kleene Closure, Complementazione, Intersezione e Differenza [LinguaggiI.pdf].
    
- **Pumping Lemma per i Linguaggi Regolari:** se $L$ è un linguaggio regolare infinito, esiste un intero $k$ (costante di pompaggio) tale che ogni stringa $z\in L$ con $|z|\ge k$ può essere decomposta in tre sottostringhe $z=uvw$ che soddisfano [LinguaggiI.pdf]:
    
    1. $|uv|\le k$
    2. $|v|>0$
    3. $\forall i\ge0: uv^iw\in L$
- **Uso in forma negativa:** per dimostrare che $L={a^nb^n\mid n\in\mathbb N}$ non è regolare, si prende $z=a^kb^k\in L$ [LinguaggiI.pdf]. Ogni scomposizione $z=uvw$ con $|uv|\le k$ forza $v$ a essere composta esclusivamente da simboli `a` [LinguaggiI.pdf]. Pompando con $i=2$, $uv^2w=a^{k+|v|}b^k$ contiene più `a` che `b`, non appartiene a $L$: contraddizione, quindi $L$ non è regolare [LinguaggiI.pdf].
    
- **Esercizi (slide, senza soluzione fornita nelle slide originali):** dimostrare che non sono regolari:
    
    1. $L_1={0^n1^m\mid n\le m}$
    2. $L_2={0^n\mid n\text{ è una potenza di }2}$
    3. $L_3={w^{2n}\mid w\in{0,1}^*,\ n=|w|}$
    
    [LinguaggiI.pdf]. (Notazione della slide: $w^{2n}$ indica la stringa $w$ ripetuta, con esponente pari alla lunghezza di $w$ moltiplicata per 2 — coerentemente con lo stile "esponente = ripetizione" già usato per $a^n$, $b^n$ altrove nella fonte.)
    

### 2.9 Automi a Pila (Pushdown Automata)

- **Struttura:** controllo a stati finiti + nastro di input + **pila**; la testa legge la cima ed esegue _push_, _pop_, _empty_ [LinguaggiI.pdf].
    
- **Definizione:** $M = (Q, \Sigma, R, \delta, q_0, Z_0, F)$ con $R$ alfabeto dei simboli di pila, $Z_0 \in R$ simbolo iniziale sulla pila, e $$\delta : Q \times (\Sigma \cup {\epsilon}) \times R \to \mathcal{P}(Q \times R^*)$$ [LinguaggiI.pdf].
    
- **Descrizioni istantanee:** triple $(q, w, \gamma)$ — stato corrente, input residuo, contenuto della pila; un passo: $$(q_0, aw, Z\eta) \vdash (q_1, w, \gamma\eta) \quad \text{se} \quad (q_1, \gamma) \in \delta(q_0, a, Z)$$ [LinguaggiI.pdf].
    
- **Linguaggio accettato:** per **stati finali** $F$, oppure per **pila vuota** (con $F = \emptyset$) [LinguaggiI.pdf].
    
- **Esempio Svolto 1 — $L={x,c,x^R \mid x \in {a,b}^*}$ (slide):** riconosciuto **per pila vuota** da $M = ({q_0, q_1}, {a,b,c}, {Z,A,B}, \delta, q_0, Z, \emptyset)$:
    
    |$\delta$|$a$|$b$|$c$|
    |---|---|---|---|
    |$q_0, Z$|$(q_0, ZA)$|$(q_0, ZB)$|$(q_1, \epsilon)$|
    |$q_1, Z$|$(q_1, Z)$|$(q_1, Z)$|—|
    |$q_1, A$|$(q_1, \epsilon)$|$(q_1, Z)$|$(q_1, Z)$|
    |$q_1, B$|$(q_1, Z)$|$(q_1, \epsilon)$|$(q_1, Z)$|
    
    (celle non specificate riempibili in modo da forzare il rigetto) [LinguaggiI.pdf].
    
    **Traccia di `abcba`:**
    
    ```
    (q0, abcba, Z)  ⊢  (q0, bcba, ZA)   [δ(q0,a,Z)=(q0,ZA): push A]
                    ⊢  (q0, cba,  ZBA)  [δ(q0,b,Z)=(q0,ZB): push B]
                    ⊢  (q1, ba,   BA)   [δ(q0,c,Z)=(q1,ε):  pop Z, cambio stato]
                    ⊢  (q1, a,    A)    [δ(q1,b,B)=(q1,ε):  pop B]
                    ⊢  (q1, ε,    ε)    [δ(q1,a,A)=(q1,ε):  pop A]
    ```
    
    Input consumato **e** pila vuota ⇒ accettato [LinguaggiI.pdf]. La sintassi dei linguaggi di programmazione è progettata con marcatori (`if`, `while`, `then`, …) proprio perché il parsing sia realizzabile con un PDA **deterministico** [LinguaggiI.pdf].
    
- **Esempio Svolto 2 — palindromi $L={ww^R\mid w\in{a,b}^*}$ (slide "Example", distinto dal precedente):** automa $M$ con $Q={q_0,q_1}$, $\Sigma={a,b}$, $R={Z,A,B}$, riconosciuto anch'esso **per pila vuota**, ma con una relazione di transizione diversa dall'esempio precedente — qui il push avviene su $q_0$ per ogni simbolo letto (senza bisogno del marcatore `c` di separazione), e il "cambio fase" da accumulo a confronto è **non deterministico** (può avvenire su un qualunque simbolo di input, anziché su un marcatore esplicito):
    
    |$q_0$|$\epsilon$|$a$|$b$|
    |---|---|---|---|
    |$Z$|—|$(q_0,AZ)$|$(q_0,BZ)$|
    |$A$|$(q_1,\epsilon)$|$(q_0,AA)$|$(q_0,BA)$|
    |$B$|$(q_1,\epsilon)$|$(q_0,AB)$|$(q_0,BB)$|
    
    |$q_1$|$a$|$b$|
    |---|---|---|
    |$Z$|—|—|
    |$A$|$(q_1,\epsilon)$|—|
    |$B$|—|$(q_1,\epsilon)$|
    
    [LinguaggiI.pdf]. **Esercizio associato (slide, senza soluzione fornita):** scrivere le derivazioni necessarie per riconoscere la stringa `abbba` [LinguaggiI.pdf].
    
    - **Nota di correttezza (slide, enunciato senza dimostrazione):** vale il fatto generale — se $L=L(M)$ con $M$ PDA per pila vuota, allora esiste un PDA $M'$ equivalente per stati finali (e viceversa) [LinguaggiI.pdf].
- **Esercizi di design PDA (slide, senza soluzione fornita nelle slide originali):** progettare un PDA che riconosca:
    
    1. ${w\in{0,1}^* \mid$ ogni prefisso di $w$ ha più 0 che 1$}$
    2. ${w\in{0,1}^* \mid w$ ha un numero uguale di 0 e di 1$}$
    
    [LinguaggiI.pdf].
    

### 2.10 Pumping Lemma per i Linguaggi Context-Free

- **Enunciato:** se $L$ è context-free, esiste $k \in \mathbb{N}$ tale che per ogni $z \in L$ con $|z| \ge k$ esiste una scomposizione $z = u,v,w,x,y$ con:
    
    1. $|vwx| \le k$
    2. $|vx| > 0$
    3. $\forall i \ge 0: ; u,v^i w,x^i y \in L$
    
    [LinguaggiI.pdf].
    
- **Uso in forma negativa:** se per ogni $k$ esiste $z \in L$, $|z| \ge k$, tale che **nessuna** scomposizione soddisfa le tre condizioni, allora $L$ non è context-free [LinguaggiI.pdf].
    
- **Esempio svolto:** $L = {a^n b^n c^n \mid n \in \mathbb{N}}$ non è CF. Sia $z = a^k b^k c^k$. Poiché $|vwx| \le k$, $v$ e $x$ insieme coprono al più **due blocchi adiacenti** di lettere; pompando con $i \neq 0$ si alterano al più due dei tre esponenti (es. $a^k b^{k+i} c^{k+j}$ con $i + j \neq 0$), e la stringa ottenuta non appartiene a $L$. Contraddizione ⇒ $L$ non è CF [LinguaggiI.pdf]. ∎
    
- **Esercizi (slide, senza soluzione fornita):** dire se sono context-free:
    
    1. ${0^n1^{3n}\mid n\ge0}$ _(nella fonte originale l'esponente appare come "0n13n"; si interpreta come $0^n1^{3n}$, coerentemente con la notazione "esponente=ripetizione" usata altrove — si segnala l'ambiguità della trascrizione OCR)_
    2. ${0^n1^{kn}\mid n\ge0 \text{ e } k\ge0}$
    3. ${a^ib^jc^k\mid i=j \text{ o } j=k}$
    4. ${a^ib^jc^k\mid k\ne i+j}$
    5. ${w\in{a,b}^*\mid w\ne vv}$
    
    [LinguaggiI.pdf].
    
- **Discussione dell'ultimo esercizio (slide, con soluzione schematica fornita nella fonte):** per ${w\mid w\ne vv}$ — se $|w|$ è dispari, allora banalmente $w\in L$ (non può essere $vv$ per nessun $v$); altrimenti (se $|w|$ è pari) occorre dimostrare l'esistenza di una grammatica generatrice. La slide fornisce lo schema: $$L = {a^Nb^M \mid N\ne M} \cup {\dots}$$ con produzioni suggerite $A\to a\mid aAa\mid aAb\mid bAa\mid bAb$, $B\to b\mid aBa\mid aBb\mid bBa\mid bBb$, $S\to A\mid B\mid BA\mid AB\mid\epsilon$ [LinguaggiI.pdf]. _(Lo schema è riportato così come appare nella fonte; la sua derivazione completa non è sviluppata nella slide originale.)_
    
- **Proprietà dei linguaggi CF:** chiusi rispetto a unione, concatenazione e Kleene closure. Il complemento di un linguaggio CF **non è sempre** CF. I linguaggi CF **non sono chiusi** rispetto all'intersezione. Decidibilità: emptiness, non-emptiness, finiteness, infiniteness, membership sono tutte decidibili per i linguaggi CF [LinguaggiI.pdf].
    

### 2.11 Grammatiche Context-Free: Definizione Formale, Parse Tree ed Esempio Guidato

_(Sezione integrata: presente nel testo sorgente ma assente dalla stesura precedente del capitolo — il contenuto pratico del parsing CF è sviluppato al Cap. 4, ma la definizione formale e l'esempio del parse tree appartengono qui, alla trattazione dei fondamenti dei linguaggi.)_

- **Definizione di Grammatica Context-Free:** $(\Sigma, N, S, P)$ è una grammatica dove ogni produzione ha la forma $U\to V$ con $U\in N$ (un singolo non-terminale) e $V\in(\Sigma\cup N)^+$; solo per il simbolo iniziale $S$ è ammessa $S\to\epsilon$ [LinguaggiI.pdf].
- **Esempio guida — espressioni booleane (slide):** $G=({E},{or,and,not,(,),0,1},P,E)$ con produzioni:
    
    ```
    E → 0E → 1E → (E or E)E → (E and E)E → (not E)
    ```
    
    $G$ genera le possibili espressioni booleane [LinguaggiI.pdf].
- **Definizione di Parse Tree:** data una grammatica $(\Sigma,N,S,P)$, il parse tree è la rappresentazione a grafo di una derivazione, definita come segue [LinguaggiI.pdf]:
    - ogni vertice ha un'etichetta in $\Sigma\cup N\cup{\epsilon}$;
    - l'etichetta della radice e di ogni vertice interno appartiene a $N$;
    - se un vertice etichettato $A$ ha $k$ figli etichettati $X_1,\dots,X_k$, allora la produzione $A\to X_1\dots X_k$ appartiene a $P$;
    - se un vertice è etichettato $\epsilon$, allora è una foglia ed è figlio unico.
- **Esempio guidato — derivazione di `((0 or 1) and (not 0))` (slide):** applicando la grammatica sopra, la stringa `((0 or 1) and (not 0))` è generata dalla derivazione $E\Rightarrow(E\ and\ E)\Rightarrow((E\ or\ E)\ and\ E)\Rightarrow((0\ or\ E)\ and\ E)\Rightarrow((0\ or\ 1)\ and\ E)\Rightarrow((0\ or\ 1)\ and\ (not\ E))\Rightarrow((0\ or\ 1)\ and\ (not\ 0))$, il cui parse tree ha radice $E$ etichettata dalla produzione $E\to(E\ and\ E)$, il cui figlio sinistro (etichettato $E$) espande $E\to(E\ or\ E)$ generando le foglie `0` e `1`, e il cui figlio destro (etichettato $E$) espande $E\to(not\ E)$ generando la foglia `0` [LinguaggiI.pdf].
- **Grammatiche equivalenti:** due grammatiche $G_1$ e $G_2$ sono equivalenti se $L(G_1)=L(G_2)$ [LinguaggiI.pdf].
- **Esempio — $\Sigma^*$ è sempre un linguaggio CF (slide):** con $\Sigma={s_1,\dots,s_n}$, la grammatica $S\to\epsilon\mid s_1S\mid\dots\mid s_nS$ genera $\Sigma^*$ [LinguaggiI.pdf].
- **Esempio — ${0^n1^n\mid n\ge0}$ (slide):** la grammatica $S\to ASB\mid\epsilon$, $A\to0$, $B\to1$ genera questo linguaggio (dimostrabile per induzione su $n$) [LinguaggiI.pdf].
- **Esempio — palindromi su ${0,1}$ (slide):** la grammatica $S\to\epsilon\mid0\mid1\mid0S0\mid1S1$ genera esattamente le stringhe palindrome su ${0,1}$ (es. `0110`, `010` sono palindrome; `0101`, `01001` non lo sono). La dimostrazione di correttezza procede in due direzioni: (1) se $x$ è palindroma allora $S\Rightarrow^*x$, per induzione sulla lunghezza $|x|$; (2) se esiste una derivazione $S\Rightarrow^*x$ allora $x$ è palindroma, anch'essa per induzione sulla lunghezza della derivazione [LinguaggiI.pdf].

### 2.12 Grammatiche Context-Sensitive: Esempio Completo

_(Sezione integrata: assente dalla stesura precedente, che si limitava a definire il Tipo 1 senza esempio.)_

- **Definizione (Type 1, slide):** una Grammatica Context-Sensitive ha produzioni della forma $U\to V$ con il solo vincolo $|U|\le|V|$ (la parte destra non può essere più corta della sinistra) [LinguaggiI.pdf].
- **Perché servono (slide):** esistono insiemi ricorsivi che non sono generabili da alcuna grammatica context-free. In particolare, ${a^ib^ic^i\mid i\ge1}$ non è context-free (dimostrato al §2.10 tramite il Pumping Lemma per CF); si dimostra ora che tale linguaggio **è** invece generabile da una grammatica di Tipo 1 [LinguaggiI.pdf].
- **Esempio svolto — grammatica di Tipo 1 per ${a^ib^ic^i\mid i\ge1}$ (slide):**
    
    ```
    S  → aSBC | aBCCB → BCbB → bbbC → bccC → ccaB → ab
    ```
    
    Questa grammatica genera esattamente il linguaggio ${a^ib^ic^i\mid i\ge1}$ [LinguaggiI.pdf]. Intuizione sul funzionamento: le prime produzioni ($S\to aSBC\mid aBC$) generano un numero uguale di simboli ausiliari $a$, $B$, $C$ in blocchi non ancora ordinati; la produzione $CB\to BC$ permette di "riordinare" i simboli ausiliari $B$ e $C$ scambiandoli di posizione finché non si raggiunge la forma $a^i B^i C^i$; le produzioni rimanenti (`bB→bb`, `bC→bc`, `cC→cc`, `aB→ab`) convertono progressivamente, da sinistra a destra, ciascun simbolo ausiliario $B$ in `b` e $C$ in `c`, preservando a ogni passo la lunghezza non decrescente richiesta dal vincolo $|U|\le|V|$ del Tipo 1 [LinguaggiI.pdf].

### 2.13 Chomsky's Hierarchy — Riepilogo Grafico

La gerarchia di Chomsky si rappresenta come quattro insiemi annidati (dal più ristretto al più ampio): Regular (Type 3) $\subset$ Context-Free (Type 2) $\subset$ Context-Sensitive (Type 1) $\subset$ Unrestricted/Phrase-Structure (Type 0) [LinguaggiI.pdf]. Ogni livello aggiunge potere espressivo al costo di una complessità computazionale via via crescente per i problemi di membership, emptiness ed equivalenza (tabella riassuntiva in §2.3) [LinguaggiI.pdf].<a id="cap3"></a>
<a id="cap3"></a>

<a id="cap3"></a>
## CAPITOLO 3: Analisi Lessicale (Lexing)

**Source:** _Lexer.pdf_ (33 slide)

> **Nota di revisione:** questo capitolo è stato ricontrollato per intero contro il testo OCR completo delle 33 slide di `Lexer.pdf`. La versione precedente copriva correttamente il nucleo (definizioni, pipeline a 5 fasi, ambiguità lessicali, i due casi di studio sui registri ILOC, rollback ed eccezioni al modello DFA), ma mancavano: la tabella di confronto Scanning/Parsing, l'esempio della grammatica regolare per identificatori riscritta come RE, il catalogo di espressioni regolari per token comuni (identificatori, interi, decimali, reali, complessi), l'elenco dei generatori di scanner reali, e — soprattutto — l'intera distinzione tra le **tre strategie di implementazione** dello scanner (table-driven, direct-coded, hand-coded) con la tecnica di _character classification_. È stato inoltre integrato l'esercizio d'esame finale (lexer a mano per espressioni di assegnamento), risolto con una traccia completa.

### 3.1 Il Ruolo dello Scanner nella Pipeline del Front-End

- **Compito del Front-End (slide "The Front End"):** il front-end si occupa del linguaggio di input: esegue un test di appartenenza (il codice appartiene al linguaggio sorgente?); verifica se il programma è ben formato semanticamente; costruisce una versione IR del codice per il resto del compilatore. Il front-end si occupa quindi sia della forma (sintassi) sia del significato (semantica) [Lexer.pdf, Slide 2].
    
- **Perché separare Scanner e Parser? (slide "The Front End" #2):**
    
    1. **Semplicità del design:** lo scanner classifica le parole, il parser costruisce derivazioni grammaticali; il parsing è più difficile e più lento. La separazione semplifica l'implementazione — gli scanner sono semplici, e uno scanner efficiente porta a un parser più veloce e più piccolo [Lexer.pdf, Slide 3].
    2. Un **token** è una coppia $\langle$parte del discorso, lessema$\rangle$ [Lexer.pdf, Slide 3].
    3. **Lo scanner è l'unica fase di compilazione che processa ogni singolo carattere dell'input** [Lexer.pdf, Slide 3].
- **Tabella di confronto Scanning vs Parsing (slide "Our setting: the Front End"):**
    
    ||**Scanning**|**Parsing**|
    |---|---|---|
    |Specificare la sintassi|Espressioni regolari|Grammatiche context-free|
    |Implementare il riconoscitore|Automa a stati finiti deterministico (DFA)|Automa a pila (push-down automaton)|
    |Eseguire il lavoro|Azioni sulle transizioni dell'automa|(analogamente, azioni sulle transizioni/riduzioni)|
    
    [Lexer.pdf, Slide 4]. Questa tabella riassume in modo compatto il parallelismo strutturale tra le due fasi, che verrà approfondito nel Cap. 4 per il parsing.
    

### 3.2 Definizioni Formali

- **Analisi Lessicale (Lexical Analysis):** riguarda le parole del vocabolario di un linguaggio (in opposizione alla grammatica, cioè la corretta costruzione delle frasi). Un **Analizzatore Lessicale** (lexer, scanner, o tokenizer) divide il programma di input, visto come flusso di caratteri, in una sequenza di **token** [Lexer.pdf, Slide 5].
- **Token:** le "parole" del linguaggio di programmazione (parole chiave, numeri, commenti, parentesi, punto e virgola). I token sono classi di input concreto, chiamato **lessema** (lexeme) [Lexer.pdf, Slide 5].
- **Ruolo unico dello scanner (slide "Lexical analysis"):** l'analisi lessicale è la primissima fase nella progettazione del compilatore, l'unica che analizza l'intero codice sorgente carattere per carattere. Un **lessema** è una sequenza di caratteri inclusa nel programma sorgente secondo il pattern di matching di un token. L'analizzatore lessicale aiuta a identificare i token nella symbol table. Una sequenza di caratteri che non è possibile scandire in alcun token valido è un **errore lessicale** [Lexer.pdf, Slide 7].
- **Costruire un Analizzatore Lessicale (slide "Constructing a Lexical Analyser"):** due strategie — _a mano_, identificando i lessemi nell'input e restituendo i token; oppure _automaticamente_, tramite un generatore di analizzatori lessicali, che compila le specifiche dei lessemi in codice (l'analizzatore lessicale stesso). L'analisi lessicale decide se i singoli token sono ben formati; questo può essere espresso da un **linguaggio regolare** [Lexer.pdf, Slide 8].

### 3.3 Grammatiche Regolari come Espressioni Regolari: l'Esempio degli Identificatori

- **La sintassi di un linguaggio di programmazione può essere espressa da una grammatica regolare (slide):** esempio — la seguente grammatica genera tutti gli identificatori legali:
    
    ```
    S → aT | … | zT | AT | … | ZTT → ε | 0T | … | 9T | S
    ```
    
    che può essere espressa più elegantemente tramite un'espressione regolare: $$(a|\dots|z|A|\dots|Z)\ (a|\dots|z|A|\dots|Z|0|\dots|9)^*$$ [Lexer.pdf, Slide 10]. Questo esempio rende esplicito, con un caso concreto, il **Teorema 2** del Cap. 2 (§2.5): ogni grammatica regolare destra ammette un automa/una RE equivalente, e viceversa — qui applicato al caso pratico più comune nella progettazione di uno scanner.

### 3.4 Espressioni Regolari per Token Comuni

- **Identificatori (slide "Examples of Regular Expressions"):**
    
    ```
    Letter     → (a|b|c|…|z|A|B|C|…|Z)Digit      → (0|1|2|…|9)Identifier → (Letter | _) (Letter | Digit | _)*
    ```
    
    (i simboli in blu nella slide indicano terminali — caratteri nel flusso di input) [Lexer.pdf, Slide 11].
- **Numeri (slide "Examples of Regular Expressions"):**
    
    ```
    Integer → (+|-|ε) (0 | (1|2|3|…|9)(Digit*))Decimal → Integer . Digit*Real    → (Integer | Decimal) E (+|-|ε) Digit*     (esistono altre varianti molto più complesse)Complex → (Real, Real)
    ```
    
    [Lexer.pdf, Slide 11]. **In pratica queste espressioni possono diventare molto più complesse** di quanto mostrato qui: la slide lo segnala esplicitamente come avvertenza [Lexer.pdf, Slide 11].

### 3.5 Pipeline di Costruzione di uno Scanner Automatizzato

Per convertire una specifica in codice, si seguono questi passi (slide "Automating Scanner Construction"):

1. Scrivere le RE per il linguaggio di input [Lexer.pdf, Slide 20].
2. Costruire un $\epsilon$-NFA che collezioni tutti gli NFA per le RE [Lexer.pdf, Slide 20].
3. Costruire un NFA corrispondente all'$\epsilon$-NFA (eliminazione delle $\epsilon$-transizioni) [Lexer.pdf, Slide 20].
4. Costruire il DFA che simula l'NFA (subset construction) [Lexer.pdf, Slide 20].
5. Minimizzare sistematicamente il DFA [Lexer.pdf, Slide 20].
6. Tradurlo in codice [Lexer.pdf, Slide 20].

- **Generatori di scanner reali (slide):** Lex e Flex lavorano secondo queste linee, così come re2c, Ragel, ANTLR, JFlex, ocamllex, Alex, …. Gli algoritmi sono ben noti e ben compresi; la questione chiave è l'interfaccia col parser. **"You could build one in a weekend!"** [Lexer.pdf, Slide 20].

### 3.6 Le Tre Strategie di Implementazione dello Scanner

- **Panoramica (slide "Implementing Scanners"):** la costruzione complessiva è RE → $\epsilon$-NFA → NFA → DFA → DFA minimizzato. Per trasformare un DFA in codice si può scegliere tra: **scanner table-driven**, **scanner a codice diretto (direct-coded)**, **scanner scritti a mano (hand-coded)** — tutti e tre simulano comunque lo stesso DFA sottostante [Lexer.pdf, Slide 21].
    
- **Passi comuni a tutte le implementazioni (slide "Common Steps Across Different Implementations"):** leggono ripetutamente il prossimo carattere dell'input e simulano la transizione DFA corrispondente; il processo si ferma quando non c'è transizione uscente dallo stato corrente per quel carattere di input; se lo stato corrente è accettante, lo scanner riconosce la parola e la sua categoria sintattica; se lo stato corrente non è accettante, lo scanner deve determinare se ha superato uno stato finale in qualche punto precedente — se sì, deve fare **rollback** del proprio stato interno e del flusso di input e segnalare successo; se no, deve segnalare fallimento [Lexer.pdf, Slide 22]. Tutte e tre le strategie hanno **costo costante per carattere** (con costanti diverse) più il costo del rollback; differiscono nel modo in cui implementano la tabella di transizione e simulano le operazioni del DFA [Lexer.pdf, Slide 23].
    
- **① Scanner Table-Driven (slide "Table-Driven Scanners"):** finora si è usato uno skeleton semplificato; in pratica lo skeleton è più complesso, e deve gestire: classificazione dei caratteri (per la compressione della tabella), costruzione del lessema, riconoscimento di sottoespressioni. In pratica si combinano tutte le RE in un unico DFA, e si deve riconoscere le singole parole senza incappare nell'EOF [Lexer.pdf, Slide 24]:
    
    ```text
    state ← s0;
    while (state ≠ serror) do
        char  ← NextChar()        // legge il prossimo carattere
        state ← δ(state, char)    // esegue la transizione
    ```
    
    - **Classificazione dei caratteri (Character Classification, slide "Character Classification"):** si raggruppano insieme i caratteri che hanno la stessa azione nel DFA — si combinano le colonne identiche nella tabella di transizione $\delta$; indicizzare $\delta$ per classe (anziché per singolo carattere) **restringe la tabella**:
        
        ```text
        state ← s0;while (state ≠ serror) do    char  ← NextChar()          // legge il prossimo carattere    cat   ← CharCat(char)       // classifica il carattere    state ← δ(state, cat)       // esegue la transizione
        ```
        
        [Lexer.pdf, Slide 25].
    - **Costruzione del lessema (slide "Building the Lexeme"):** lo scanner produce la categoria sintattica (parte del discorso), ma la maggior parte delle applicazioni vuole anche il lessema (la parola) — problema banale: si salvano semplicemente i caratteri via via letti:
        
        ```text
        state ← s0lexeme ← empty stringwhile (state ≠ serror) do    char   ← NextChar()              // legge il prossimo carattere    lexeme ← lexeme + char           // concatena al lessema    cat    ← CharCat(char)           // classifica il carattere    state  ← δ(state, cat)           // esegue la transizione
        ```
        
        [Lexer.pdf, Slide 26].
    - **Riconoscimento di sottoespressioni — Rollback (slide "Recognising subexpressions: RollBack"):** una pila (stack) traccia tutti gli stati attraversati:
        
        ```text
        lexeme ← empty stringwhile (state ≠ serror) do    char ← NextChar();  lexeme ← lexeme + char    push(state);                       // ricorda tutti gli stati attraversati    cat ← CharCat(char);  state ← δ(state, cat)while (state ≠ sa) do                   // sa = ultimo stato finale incontrato    state ← pop();  truncate lexeme;  Rollback();
        ```
        
        [Lexer.pdf, Slide 27]. (Questa è la stessa logica già presentata in dettaglio in §3.9.)
    - **Costo:** per ogni carattere lo scanner table-driven esegue **due lookup in tabella** — uno in `CharCat`, uno in $\delta$ [Lexer.pdf, Slide 30].
- **② Scanner a Codice Diretto (Direct-Coded, slide "Direct-Coded scanners"):** evita il doppio lookup per carattere dello scanner table-driven, traducendo direttamente la struttura degli stati in codice (tipicamente `switch`/`if` annidati anziché tabelle esplicite) — più efficiente a parità di comportamento. Se il test sullo stato è complesso (es. con molti case), il generatore di scanner dovrebbe considerare altri schemi, come la **ricerca binaria** [Lexer.pdf, Slide 30].
    
- **③ Scanner Scritti a Mano (Hand-Coded, slide "What About Hand-Coded Scanners?"):** molti (la maggior parte?) dei compilatori moderni usano scanner scritti a mano. Partire da un DFA semplifica il design e la comprensione — permette di usare vecchi trucchi in stile assembly, e di combinare stati simili. Gli scanner sono divertenti da scrivere: compatti, comprensibili, facili da debuggare [Lexer.pdf, Slide 32].
    
- **Riepilogo delle tre strategie:** tutte e tre simulano lo stesso DFA sottostante e hanno costo asintoticamente costante per carattere; differiscono per il fattore costante e per la manutenibilità/comprensibilità del codice risultante. Un generatore di scanner automatico (Lex, Flex, …) tipicamente produce codice table-driven o direct-coded; molti compilatori di produzione preferiscono comunque scanner hand-coded per motivi di velocità e controllo fine [Lexer.pdf, Slide 21, 30, 32].
    
- **Struttura concreta di uno scanner table-driven per i nomi di registro (slide "A table driven scanner for register names"):** il codice risultante si organizza tipicamente in cinque sezioni: inizializzazione, loop di scansione, rollback, sezione finale, stati finali — la stessa struttura concettuale del Cap. 3 §3.8 [Lexer.pdf, Slide 29].
    

### 3.7 Risoluzione delle Ambiguità Lessicali

Durante la scansione possono sorgere conflitti in cui più regole o lessemi corrispondono all'input. Vengono usate due euristiche standard per risolverli deterministicamente:

- **Longest Match (Maximal Munch):** lo scanner seleziona sempre il lessema più lungo possibile che corrisponde a una regola valida. Ad esempio, la stringa di input `while_var` verrà riconosciuta interamente come un unico identificatore `while_var` anziché come la parola chiave `while` seguita dall'identificatore `_var` [Lexer.pdf].
- **First Fit / Scelta della categoria da una RE ambigua (slide "Choosing a Category from an Ambiguous RE"):** si vuole un DFA unico, quindi si combinano tutte le RE in un solo automa — alcune stringhe possono corrispondere alla RE di più di una categoria sintattica (parole chiave contro identificatori generici). Lo scanner deve scegliere una categoria per gli stati finali ambigui: la risposta classica è **specificare la priorità in base all'ordine delle RE** (si restituisce la prima) [Lexer.pdf, Slide 28]. Esempio della slide: con `Identifier → Letter (Letter|Digit)*` e `key → if | …`, la stringa `ife` viene classificata come **identificatore** (poiché non coincide esattamente con `if`) [Lexer.pdf, Slide 28].

### 3.8 Casi di Studio ed Esempi d'Esame

**Caso di Studio 1 — specifica generica per i registri ILOC (slide "Consider the problem of recognizing ILOC register names").** `Register → r (0|…|9)(0|…|9)*`: permette registri di numero arbitrario, richiede almeno una cifra [Lexer.pdf, Slide 12]. DFA:

```
        r            (0|…|9)
  s0 ───────► s1 ────────► s2 (finale)
```

con transizioni su ogni altro carattere verso lo stato d'errore $s_e$ [Lexer.pdf, Slide 12].

**Comportamento (slide "DFA operation"):** `r17` attraversa $s_0,s_1,s_2$ e viene accettato; `r` attraversa $s_0,s_1$ e fallisce; `0` va direttamente a $s_e$ [Lexer.pdf, Slide 13].

**Skeleton recognizer e tabella (slide "Example"):**

```
Char ← next character;  State ← s0
while (Char ≠ EOF)
    State ← δ(State, Char)
    Char  ← next character
if (State is final) then report success else report failure
```

Costo $O(1)$ per carattere (o per transizione); per essere utile, il DFA deve essere convertito in codice [Lexer.pdf, Slide 14]:

|δ|r|0…9|altri|
|---|---|---|---|
|s0|s1|se|se|
|s1|se|s2|se|
|s2|se|s2|se|
|se|se|se|se|

**Tabella delle azioni α (slide "Example" — aggiunta di azioni alle transizioni):** affiancata a δ, associa a ogni transizione un'azione (tipicamente _catturare il lessema_) [Lexer.pdf, Slide 15]:

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

- **Caso di Studio 2 — Tighter Register Specification (slide "What if we need a tighter specification?"):** Con `r Digit Digit*` si accetta anche `r00000` o `r99999` — lessemi errati se si vogliono limitare i registri a $r_0$–$r_{31}$ [Lexer.pdf, Slide 16]. La RE più stringente: $$Register \rightarrow r \ ( \ (0 \mid 1 \mid 2)(Digit \mid \epsilon) \mid (4 \mid 5 \mid 6 \mid 7 \mid 8 \mid 9) \mid (3 \mid 30 \mid 31) \ )$$ produce un DFA più complesso: più stati, stesso costo per transizione, stessa implementazione di base [Lexer.pdf, Slide 16]. _Nota storica della slide:_ più stati implicano una tabella più grande, un fatto che contava quando i computer avevano 128KB–640KB di RAM; oggi, con smartphone che hanno decine o centinaia di gigabyte di storage e laptop con 16–64GB di RAM, la preoccupazione può sembrare superata [Lexer.pdf, Slide 16].
    
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
    
    [Lexer.pdf, Slide 18].
    
    ##### Tabella delle Azioni $\alpha$ (Tighter Register Specification):
    
    |State|r|0,1|2|3|4-9|other|
    |---|---|---|---|---|---|---|
    |s0|1, start|e|e|e|e|e|
    |s1|e|2, add|2, add|5, add|4, add|e|
    |s2|e|3, add|3, add|3, add|3, add|e, exit|
    |s3, s4, s6|e|e|e|e|e|e, exit|
    |s5|e|6, add|e|e|e|e, exit|
    |se|e|e|e|e|e|e|
    
    [Lexer.pdf, Slide 19]. Questa tabella gira nello **stesso skeleton recognizer** della specifica generica [Lexer.pdf, Slide 18].
    

### 3.9 Rollback e Limiti degli Scanner DFA

- **Rollback (slide, cfr. §3.6):** avanzando lo scanner può superare l'ultimo stato finale; uno **stack degli stati traversati** permette di tornare indietro. Se non esiste alcun stato finale su cui tornare ⇒ **errore lessicale**. Tutte le implementazioni (table-driven, direct-coded, hand-coded) costano O(1) per carattere più il costo del rollback [Lexer.pdf, Slide 22, 23, 27].
- **Eccezioni al modello DFA (slide "Building Scanners"):** tutta questa tecnologia permette di automatizzare la costruzione dello scanner: l'implementatore scrive le espressioni regolari, il generatore di scanner costruisce NFA, DFA, DFA minimo, e produce il codice (table-driven o direct-coded); questo produce in modo affidabile scanner veloci e robusti. Per la maggior parte delle feature linguistiche moderne, questo funziona — si dovrebbe pensarci due volte prima di introdurre una feature che sconfigge uno scanner DFA-based [Lexer.pdf, Slide 31]. Alcune eccezioni: _contextual keywords_ (`async`, `await`, `record` — keyword solo in certi contesti sintattici: richiedono cooperazione lexer/parser, indebolendo lo scanning puramente DFA-based) e sintassi **sensibile all'indentazione** (Python: il lexer traccia i livelli ed emette `INDENT`/`DEDENT`, andando oltre il semplice riconoscimento di linguaggi regolari). Storicamente le feature che rompono la regolarità lessicale non hanno avuto un successo particolare né un'adozione diffusa [Lexer.pdf, Slide 31].

### 3.10 Esercizio Svolto d'Esame: Lexer a Mano per Espressioni di Assegnamento

**Testo dell'esercizio (slide "Exercise"):** scrivere a mano un analizzatore lessicale che tokenizzi un semplice linguaggio di input per assegnamenti come `sum = a1 + 23 - value2`. Identificatori e numeri sono descritti dalle RE [Lexer.pdf, Slide 33]:

- `IDENTIFIER → [a-zA-Z][a-zA-Z0-9]*` (una lettera seguita da lettere o cifre)
- `NUMBER → [0-9]+` (una o più cifre)
- i caratteri di spaziatura (spazio, tab, newline) vanno ignorati

Implementare una funzione `NEXT_TOKEN()` che: (1) salta ogni spaziatura; (2) ispeziona il carattere corrente (lookahead); (3) riconosce il token valido più lungo; (4) consuma i caratteri corrispondenti; (5) restituisce il token identificato. Se si incontra un carattere non valido, si segnala un errore lessicale [Lexer.pdf, Slide 33].

**Esempio di input e output atteso dato dalla slide:** per l'input `x = 10 + y` (nota: la slide riporta letteralmente `x = 10 + y.`, col punto finale — probabile refuso della fonte, ignorato nella traccia sottostante poiché `.` non è un carattere descritto da alcuna RE del linguaggio):

```
IDENTIFIER(x)
ASSIGN
NUMBER(10)
PLUS
IDENTIFIER(y)
EOF
```

[Lexer.pdf, Slide 33].

> **Nota metodologica:** l'implementazione di `NEXT_TOKEN()` e la traccia carattere-per-carattere non sono fornite nella slide originale (che pone solo l'esercizio); sono sviluppate qui applicando rigorosamente il modello a DFA table-driven di §3.6.

**Implementazione di `NEXT_TOKEN()` (skeleton coerente con §3.6):**

```text
NEXT_TOKEN():
    while (current_char is ' ' or '\t' or '\n')     // 1. salta la spaziatura
        current_char ← NextChar()

    if current_char = EOF then return EOF

    if current_char is a letter then                // IDENTIFIER
        lexeme ← empty string
        while (current_char is a letter or a digit)
            lexeme ← lexeme + current_char
            current_char ← NextChar()
        return IDENTIFIER(lexeme)

    else if current_char is a digit then             // NUMBER
        lexeme ← empty string
        while (current_char is a digit)
            lexeme ← lexeme + current_char
            current_char ← NextChar()
        return NUMBER(lexeme)

    else if current_char = '=' then
        current_char ← NextChar();  return ASSIGN
    else if current_char = '+' then
        current_char ← NextChar();  return PLUS
    else if current_char = '-' then
        current_char ← NextChar();  return MINUS
    else
        report lexical error, current_char
```

Questo è precisamente uno scanner **hand-coded** (§3.6, strategia ③): la struttura a `if`/`while` annidati, anziché una tabella $\delta$ esplicita, codifica direttamente il DFA sottostante — combinando i tre automi (IDENTIFIER, NUMBER, simboli singoli) in un'unica funzione tramite lookahead sul primo carattere, esattamente come richiesto dal punto 2–3 della traccia dell'esercizio (ispezionare il lookahead, riconoscere il token più lungo).

**Traccia completa per l'input `x = 10 + y`:**

|Chiamata a `NEXT_TOKEN()`|Caratteri consumati|Token restituito|
|---|---|---|
|1|`x` (lettera; nessuna lettera/cifra successiva — spazio)|`IDENTIFIER(x)`|
|2|(salta spazio) `=` (nessun altro simbolo `=` atteso)|`ASSIGN`|
|3|(salta spazio) `1`,`0` (cifre, poi spazio)|`NUMBER(10)`|
|4|(salta spazio) `+`|`PLUS`|
|5|(salta spazio) `y` (lettera; poi EOF)|`IDENTIFIER(y)`|
|6|(nessun carattere: EOF)|`EOF`|

Sequenza di output: `IDENTIFIER(x) ASSIGN NUMBER(10) PLUS IDENTIFIER(y) EOF` — coincide esattamente con l'output atteso dalla slide [Lexer.pdf, Slide 33]. Si noti che la regola del **longest match** (§3.7) è implicitamente rispettata dal `while` interno di ciascun ramo: lo scanner continua a consumare caratteri finché appartengono alla stessa classe (lettere/cifre per IDENTIFIER, cifre per NUMBER), fermandosi solo al primo carattere che non estende il lessema corrente.<a id="cap4"></a>

<a id="cap4"></a>
## CAPITOLO 4: Parsing Top-Down e Parser LL(1)

**Sources:** _ParsingMio.pdf_ (75 slide) / _TableConstruction.pdf_ (parte LL(1), slide 30)

> **Nota di revisione:** questo capitolo è stato ricontrollato per intero contro il testo OCR completo delle 75 slide di `ParsingMio.pdf`. Il nucleo era già corretto (FIRST/FOLLOW/FIRST⁺, tabella LL(1), skeleton parser, i due esercizi risolti begin-end e S→AB|eDa), ma mancavano interi algoritmi e dimostrazioni operative presenti nella fonte: (1) gli esempi motivazionali completi sui limiti dei linguaggi regolari, (2) la dimostrazione _operativa_ dell'ambiguità tramite due derivazioni concrete per `x-2*y` con parse tree diversi, (3) l'intera traccia di parsing top-down **con backtracking** (compreso un ramo che non termina), (4) l'algoritmo generale per l'eliminazione della ricorsione a sinistra **indiretta** (non solo immediata) con l'esempio svolto G,E,T, (5) il **parser ricorsivo a discesa** con pseudocodice esplicito per l'intera grammatica delle espressioni, (6) l'algoritmo generale di **left factoring** con esempio svolto, (7) la nozione di "ambiguità più profonda" dovuta all'overloading. Tutti questi blocchi sono ora integrati.

### 4.1 Perché i Linguaggi Regolari Non Bastano

- **Non tutti i linguaggi sono regolari (slide "Why Not Use Regular Languages & DFAs?"):** $RL \subset CFL \subset CSL$. Non è possibile costruire DFA per riconoscere linguaggi come [ParsingMio.pdf, Slide 4]:
    
    - $L = {p^kq^k}$
    - $L = {wcw^R \mid w \in \Sigma^*}$
    
    Nessuno dei due è un linguaggio regolare [ParsingMio.pdf, Slide 4].
    
- **Costrutti dei linguaggi di programmazione che richiedono grammatiche più potenti (slide):**
    
    - Parentesi bilanciate con annidamento arbitrario, es. `f(g(h(x)))`: il linguaggio $L={(^n)^n \mid n\ge0}$ non è regolare [ParsingMio.pdf, Slide 4].
    - Blocchi annidati `{...}` [ParsingMio.pdf, Slide 4].
    - Coppie begin-end [ParsingMio.pdf, Slide 4].
    - Argomenti di funzione annidati, es. `f(a, g(b,c), h(d,k(e)))`: la virgola dentro una chiamata annidata deve essere ignorata (non deve essere confusa con un separatore di primo livello) [ParsingMio.pdf, Slide 4].
    - **Corrispondenza del numero di parametri: non è nemmeno context-free!** $L={vv}$ non è regolare (e, come visto al §2.10 con il Pumping Lemma per CF, ${w\mid w\ne vv}$ e varianti collegate non sono nemmeno context-free) [ParsingMio.pdf, Slide 4].

### 4.2 Grammatiche Context-Free, Derivazioni e Ambiguità: Definizioni

- **Definizione di Grammatica Context-Free (CFG):** produzioni della forma $A\to\beta$ con $A\in N$ un singolo non-terminale e $\beta\in(\Sigma\cup N)^+$ (solo per $S$ è ammessa $S\to\epsilon$) [LinguaggiI.pdf; ParsingMio.pdf, Slide 13].
- **Derivazioni, Sentential Form e Parse Tree:**
    - Una **derivazione** è una sequenza di passi di riscrittura $S\Rightarrow\gamma_0\Rightarrow\gamma_1\Rightarrow\dots\Rightarrow\gamma_n\Rightarrow\text{sentenza}$ [ParsingMio.pdf, Slide 7].
    - Ogni $\gamma_i$ è una **forma sentenziale**; se contiene solo terminali è una sentenza di $L(G)$; se contiene uno o più non-terminali resta una forma sentenziale [ParsingMio.pdf, Slide 7].
    - Per ottenere $\gamma_i$ da $\gamma_{i-1}$, si espande un non-terminale $A\in\gamma_{i-1}$ usando $A\to\beta$, sostituendo quella occorrenza di $A$ con $\beta$ [ParsingMio.pdf, Slide 7].
    - **Leftmost derivation:** a ogni passo si espande il **primo** non-terminale (da sinistra) — produce una _left-sentential form_ [ParsingMio.pdf, Slide 6, 7].
    - **Rightmost derivation:** a ogni passo si espande l'**ultimo** non-terminale (da destra) — produce una _right-sentential form_ [ParsingMio.pdf, Slide 6, 7].
    - Queste sono le due derivazioni "sistematiche" di interesse (non ci si cura di derivazioni con ordine casuale) [ParsingMio.pdf, Slide 6].

### 4.3 L'Ambiguità Aritmetica: un Esempio Operativo

Consideriamo la grammatica "più utile del SheepNoise" (slide "A More Useful Grammar Than Sheep Noise"):

```
0. Expr → Expr Op Expr
1.      | number
2.      | id
3. Op   → +
4.      | -
5.      | *
6.      | /
```

[ParsingMio.pdf, Slide 5]. Deriviamo `x – 2 * y` (cioè `<id,x> - <num,2> * <id,y>`) in modo **leftmost**:

|Regola|Forma Sentenziale|
|---|---|
|—|`Expr`|
|0|`Expr Op Expr`|
|2|`<id,x> Op Expr`|
|4|`<id,x> - Expr`|
|0|`<id,x> - Expr Op Expr`|
|1|`<id,x> - <num,2> Op Expr`|
|5|`<id,x> - <num,2> * Expr`|
|2|`<id,x> - <num,2> * <id,y>`|

[ParsingMio.pdf, Slide 5, 8]. Il parse tree corrispondente rappresenta `x – (2 * y)` [ParsingMio.pdf, Slide 9].

**Ora deriviamo la STESSA stringa in modo rightmost:**

|Regola|Forma Sentenziale|
|---|---|
|—|`Expr`|
|0|`Expr Op Expr`|
|2|`Expr Op <id,y>`|
|5|`Expr * <id,y>`|
|0|`Expr Op Expr * <id,y>`|
|1|`Expr Op <num,2> * <id,y>`|
|4|`Expr - <num,2> * <id,y>`|
|2|`<id,x> - <num,2> * <id,y>`|

[ParsingMio.pdf, Slide 8, 10]. **Sorprendentemente, il parse tree di questa derivazione rightmost rappresenta `(x – 2) * y` — un albero diverso dal precedente, con un significato diverso!** [ParsingMio.pdf, Slide 10]. **Questa ambiguità non va bene**: le due derivazioni (leftmost e rightmost) della stessa stringa producono alberi di parsing diversi, che implicano ordini di valutazione diversi [ParsingMio.pdf, Slide 8, 10].

- **La causa del problema (slide "Derivations and Precedence"):** questa grammatica non ha alcuna nozione di **precedenza**, né di ordine di valutazione implicito [ParsingMio.pdf, Slide 11].
- **Ambiguità anche fra due derivazioni leftmost (slide "Ambiguous Grammars" / "The Difference"):** la stessa grammatica ammette **due diverse derivazioni leftmost** per `x-2*y`, a seconda di quale produzione si sceglie al secondo passo (Regola 4, `Expr→Expr-Expr`, vs. Regola 0 seguita da ulteriore espansione): entrambe raggiungono con successo `x-2*y`, ma tramite alberi diversi [ParsingMio.pdf, Slide 14, 15, 16]. **Definizione formale di ambiguità (slide "Ambiguous Grammars — Definitions"):** una grammatica è ambigua se ammette più di una derivazione leftmost per una singola forma sentenziale, oppure più di una derivazione rightmost per una singola forma sentenziale. **Nota sottile:** le derivazioni leftmost e rightmost per una data forma sentenziale possono differire anche in una grammatica **non ambigua** — ma in tal caso devono comunque produrre lo **stesso parse tree** [ParsingMio.pdf, Slide 17].

### 4.4 Rimuovere l'Ambiguità Aritmetica tramite la Precedenza

Per aggiungere la precedenza (slide "Derivations and Precedence"): si crea un non-terminale per ciascun livello di precedenza; si isola la parte corrispondente della grammatica; si forza il parser a riconoscere prima le sotto-espressioni a precedenza più alta. Per le espressioni algebriche: parentesi per prime (livello 1), moltiplicazione e divisione poi (livello 2), sottrazione e addizione per ultime (livello 3) [ParsingMio.pdf, Slide 11].

Aggiungendo la precedenza algebrica standard si ottiene:

```
0. Goal   → Expr
1. Expr   → Expr + Term
2.        | Expr - Term
3.        | Term
4. Term   → Term * Factor
5.        | Term / Factor
6.        | Factor
7. Factor → ( Expr )
8.        | number
9.        | id
```

[ParsingMio.pdf, Slide 12]. Questa grammatica è leggermente più grande — richiede più passi di riscrittura per raggiungere alcuni terminali — ma codifica la precedenza attesa, e **produce lo stesso parse tree sotto derivazione sia leftmost sia rightmost**: la correttezza prevale sulla velocità del parser [ParsingMio.pdf, Slide 12]. _(Nota: una RE non può codificare la precedenza, né le parentesi — entrambe eccedono il potere di un'espressione regolare, motivando ulteriormente il passaggio a una CFG [ParsingMio.pdf, Slide 12].)_

**Derivazione rightmost di `x-2*y` con la grammatica a precedenza (slide "Derivations and Precedence" #2):**

|Regola|Forma Sentenziale|
|---|---|
|—|`Goal`|
|0|`Expr`|
|2|`Expr - Term`|
|4|`Expr - Term * Factor`|
|9|`Expr - Term * <id,y>`|
|6|`Expr - Factor * <id,y>`|
|8|`Expr - <num,2> * <id,y>`|
|3|`Term - <num,2> * <id,y>`|
|6|`Factor - <num,2> * <id,y>`|
|9|`<id,x> - <num,2> * <id,y>`|

Deriva `x – (2 * y)`, con il parse tree corretto — sia la derivazione leftmost sia quella rightmost producono ora **lo stesso** parse tree, perché la grammatica codifica direttamente ed esplicitamente la precedenza desiderata [ParsingMio.pdf, Slide 13].

### 4.5 Il Caso Dangling-Else: Ambiguità e Disambiguazione

- **Esempio classico (slide "Ambiguous Grammars"):**
    
    ```
    Stmt → if Expr then Stmt
         | if Expr then Stmt else Stmt
         | … altre istruzioni …
    ```
    
    Questa ambiguità è **inerente alla grammatica** [ParsingMio.pdf, Slide 17].
    
- **La forma sentenziale `if Expr1 then if Expr2 then Stmt1 else Stmt2` ammette due derivazioni (slide "Ambiguity"):** una che applica prima la produzione 2 poi la 1 (associando `else` all'`if` più esterno), l'altra che applica prima la 1 poi la 2 (associando `else` all'`if` più interno) — **parte del problema è che la struttura costruita dal parser determinerà l'interpretazione del codice, e queste due forme hanno significati diversi!** [ParsingMio.pdf, Slide 18].
    
- **Rimuovere l'ambiguità (slide "Ambiguity"):** occorre riscrivere la grammatica per evitare di generare il problema; si fa corrispondere ogni `else` all'`if` non ancora abbinato più interno (regola di buon senso):
    
    ```
    0. Stmt     → if Expr then Stmt
    1.           | if Expr then WithElse else Stmt
    2.           | Other Statements
    3. WithElse → if Expr then WithElse else WithElse
    4.           | Other Statements
    ```
    
    Con questa grammatica l'esempio ha **una sola** derivazione rightmost [ParsingMio.pdf, Slide 19]. Intuizione: una volta entrati in `WithElse`, non si può più generare un `else` non abbinato; un `if` finale senza `else` può provenire solo dalla regola 0 — la grammatica forza la struttura a corrispondere al significato desiderato [ParsingMio.pdf, Slide 19].
    
- **Traccia della derivazione rightmost risultante (slide "Ambiguity" #4):** per `if Expr1 then if Expr2 then Stmt1 else Stmt2`, questa grammatica ammette **una sola** derivazione rightmost:
    
    |Regola|Forma Sentenziale|
    |---|---|
    |—|`Stmt`|
    |0|`if Expr then Stmt`|
    |1|`if Expr then if Expr then WithElse else Stmt`|
    |2|`if Expr then if Expr then WithElse else S2`|
    |4|`if Expr then if Expr then S1 else S2`|
    |⋯|(altre produzioni per derivare gli `Expr` in `E1`, `E2`)|
    |⋯|`if E1 then if E2 then S1 else S2`|
    
    [ParsingMio.pdf, Slide 20].
    

### 4.6 Ambiguità Più Profonda: Confusione Context-Sensitive

- **Overloading come fonte di ambiguità più profonda (slide "Deeper Ambiguity"):** l'ambiguità di solito si riferisce a confusione nella CFG; l'overloading può creare un'ambiguità più profonda. Esempio: `a = f(17)` — in molti linguaggi Algol-like, `f` potrebbe essere sia una funzione sia una variabile indicizzata (array). Disambiguare questo caso richiede **contesto**: servono i valori delle dichiarazioni; è realmente una questione di **tipo**, non di sintassi context-free; richiede una soluzione extra-grammaticale (non esprimibile in una CFG) — va gestita con un meccanismo diverso, uscendo dalla grammatica anziché usare una grammatica più complessa [ParsingMio.pdf, Slide 21].
- **Ambiguità — la parola finale (slide "Ambiguity - the Final Word"):** l'ambiguità nasce da due fonti distinte: confusione nella sintassi context-free (if-then-else), e confusione che richiede contesto per essere risolta (overloading). Per risolvere l'ambiguità: per rimuovere l'ambiguità context-free, si riscrive la grammatica; per gestire l'ambiguità context-sensitive serve cooperazione — conoscenza di dichiarazioni, tipi, … — accettando un **superset** di $L(G)$ e verificandolo con altri mezzi (analisi context-sensitive, Cap. 6); è un problema di design del linguaggio. **A volte il compilatore accetta esplicitamente una grammatica ambigua**, usando tecniche di parsing che "fanno la cosa giusta" — cioè selezionano sempre la stessa derivazione [ParsingMio.pdf, Slide 22].

### 4.7 Parsing Top-Down: l'Algoritmo Generico con Backtracking

- **Tecniche di parsing (slide "Parsing Techniques"):**
    - **Top-down** (LL(1), recursive descent): parte dalla radice del parse tree e cresce verso le foglie; sceglie una produzione e prova a far corrispondere l'input; una scelta sbagliata può richiedere backtracking; alcune grammatiche sono _backtrack-free_ (parsing predittivo) [ParsingMio.pdf, Slide 23].
    - **Bottom-up** (LR(1), operator precedence): parte dalle foglie e cresce verso la radice; man mano che l'input viene consumato, codifica le possibilità in uno stato interno; parte da uno stato valido per i primi token legali; gestisce una classe più ampia di grammatiche [ParsingMio.pdf, Slide 23].
- **Algoritmo generico di parsing top-down (slide "Top-down Parsing"):** un parser top-down parte dalla radice del parse tree, etichettata col simbolo iniziale della grammatica.
    
    ```text
    Costruire il nodo radice del parse treeRipetere finché la frontiera inferiore del parse tree non corrisponde alla stringa di input:    1. In un nodo etichettato A, selezionare una produzione con A sulla lhs e, per       ciascun simbolo della rhs, costruire il figlio appropriato    2. Quando un simbolo terminale viene aggiunto alla frontiera e non corrisponde       all'input, fare backtrack    3. Trovare il prossimo nodo da espandere (etichetta ∈ NT)
    ```
    
    La chiave è scegliere la produzione giusta al passo 1 — quella scelta dovrebbe essere guidata dalla stringa di input [ParsingMio.pdf, Slide 24].

### 4.8 Esempio Svolto: Parsing con Backtracking di `x – 2 * y`

Applichiamo l'algoritmo generico di §4.7 alla grammatica a precedenza di §4.4, sull'input `x – 2 * y` [ParsingMio.pdf, Slide 25].

**Primo tentativo (slide "Example"):** partendo da `Goal`, si espande fino a `<id,x> + Term` (scegliendo la Regola 1, `Expr→Expr+Term`), e si consuma `x`:

|Regola|Forma Sentenziale|Input|
|---|---|---|
|—|`Goal`|$\uparrow$`x - 2 * y`|
|0|`Expr`|$\uparrow$`x - 2 * y`|
|1|`Expr + Term`|$\uparrow$`x - 2 * y`|
|3|`Term + Term`|$\uparrow$`x - 2 * y`|
|6|`Factor + Term`|$\uparrow$`x - 2 * y`|
|9|`<id,x> + Term`|$\uparrow$`x - 2 * y`|
|→|`<id,x> + Term`|`x` $\uparrow$`- 2 * y`|

Ha funzionato bene, **eccetto che "–" non corrisponde a "+"**: il parser deve fare backtrack fino a qui [ParsingMio.pdf, Slide 27].

**Secondo tentativo — si sceglie la Regola 2 al posto della 1 (slide "Example" #2):**

|Regola|Forma Sentenziale|Input|
|---|---|---|
|—|`Goal`|$\uparrow$`x - 2 * y`|
|0|`Expr`|$\uparrow$`x - 2 * y`|
|2|`Expr - Term`|$\uparrow$`x - 2 * y`|
|3|`Term - Term`|$\uparrow$`x - 2 * y`|
|6|`Factor - Term`|$\uparrow$`x - 2 * y`|
|9|`<id,x> - Term`|$\uparrow$`x - 2 * y`|
|→|`<id,x> - Term`|`x` $\uparrow$`- 2 * y`|
|→|`<id,x> - Term`|`x -` $\uparrow$`2 * y`|

Ora "–" e "–" corrispondono; ora si può espandere `Term` per far corrispondere "2" [ParsingMio.pdf, Slide 28].

**Terzo passo — espansione di `Term` troppo breve (slide "Example" #3):**

|Regola|Forma Sentenziale|Input|
|---|---|---|
|→|`<id,x> - Term`|`x -` $\uparrow$`2 * y`|
|6|`<id,x> - Factor`|`x -` $\uparrow$`2 * y`|
|8|`<id,x> - <num,2>`|`x -` $\uparrow$`2 * y`|
|→|`<id,x> - <num,2>`|`x - 2` $\uparrow$`* y`|

"2" corrisponde a "2" — ma resta altro input e non ci sono più non-terminali da espandere: **l'espansione è terminata troppo presto ⇒ serve backtrack** [ParsingMio.pdf, Slide 29].

**Quarto tentativo — successo (slide "Example" #4):** si riespande `Term` con la Regola 4 (`Term→Term*Factor`) invece della Regola 6:

|Regola|Forma Sentenziale|Input|
|---|---|---|
|→|`<id,x> - Term`|`x -` $\uparrow$`2 * y`|
|4|`<id,x> - Term * Factor`|`x -` $\uparrow$`2 * y`|
|6|`<id,x> - Factor * Factor`|`x -` $\uparrow$`2 * y`|
|8|`<id,x> - <num,2> * Factor`|`x -` $\uparrow$`2 * y`|
|→|`<id,x> - <num,2> * Factor`|`x - 2` $\uparrow$`* y`|
|→|`<id,x> - <num,2> * Factor`|`x - 2 *` $\uparrow$`y`|
|9|`<id,x> - <num,2> * <id,y>`|`x - 2 *` $\uparrow$`y`|
|→|`<id,x> - <num,2> * <id,y>`|`x - 2 * y`$\uparrow$|

Questa volta si corrisponde e si consuma **tutto** l'input ⇒ **successo!** [ParsingMio.pdf, Slide 30]. **Il punto:** il parser deve fare la scelta giusta quando espande un non-terminale; le scelte sbagliate portano a sforzo sprecato [ParsingMio.pdf, Slide 30].

**Un ramo pericoloso — non-terminazione (slide "Example" #5):** altre scelte di espansione sono possibili; una di queste **non termina**:

|Regola|Forma Sentenziale|Input|
|---|---|---|
|—|`Goal`|$\uparrow$`x - 2 * y`|
|0|`Expr`|$\uparrow$`x - 2 * y`|
|1|`Expr + Term`|$\uparrow$`x - 2 * y`|
|1|`Expr + Term + Term`|$\uparrow$`x - 2 * y`|
|1|`Expr + Term + Term + Term`|$\uparrow$`x - 2 * y`|
|1|e così via…|$\uparrow$`x - 2 * y`|

Questa espansione **non consuma alcun input**: una scelta di espansione sbagliata porta alla non-terminazione — una proprietà pessima per un parser (e per un compilatore in generale) [ParsingMio.pdf, Slide 31].

### 4.9 Ricorsione a Sinistra: Eliminazione Immediata e Generale (Indiretta)

- **Definizione formale (slide "Left Recursion"):** una grammatica è ricorsiva a sinistra se $\exists A\in N$ tale che esiste una derivazione $A\Rightarrow^+A\alpha$, per qualche stringa $\alpha\in(N\cup\Sigma)^+$. La nostra classica grammatica delle espressioni è ricorsiva a sinistra — questo può portare a non-terminazione in un parser top-down. In un parser top-down, ogni ricorsione deve essere ricorsione **destra**; vogliamo convertire la ricorsione sinistra in ricorsione destra. **La non-terminazione è sempre una proprietà pessima in un compilatore** [ParsingMio.pdf, Slide 32].
    
- **Eliminazione della ricorsione sinistra immediata (slide "Eliminating Left Recursion"):** dato un frammento di grammatica della forma $Fee\to Fee,\alpha \mid \beta$ (dove né $\alpha$ né $\beta$ iniziano con $Fee$), si riscrive come: $$Fee \to \beta,Fie \qquad Fie \to \alpha,Fie \mid \epsilon$$ dove $Fie$ è un nuovo non-terminale. La nuova grammatica definisce lo **stesso linguaggio** della vecchia, usando solo ricorsione destra [ParsingMio.pdf, Slide 33].
    
- **Applicazione alla grammatica delle espressioni (slide "Eliminating Left Recursion" #2):** la grammatica delle espressioni contiene due casi di ricorsione sinistra (in `Expr` e in `Term`); applicando la trasformazione: $$Expr\to Term,Expr' \qquad Expr'\to{+},Term,Expr'\mid{-},Term,Expr'\mid\epsilon$$ $$Term\to Factor,Term' \qquad Term'\to{*},Factor,Term'\mid{/},Factor,Term'\mid\epsilon$$ Questi frammenti usano solo ricorsione destra [ParsingMio.pdf, Slide 34]. **Nota sulla associatività (slide, con cautela):** la ricorsione destra spesso implica associatività destra; tuttavia, sostituendo questi frammenti nella grammatica completa (§4.4), il risultato — pur essendo strutturalmente ricorsivo a destra — **resta left-associative come l'originale** dal punto di vista del linguaggio riconosciuto: la trasformazione naïve produce una grammatica corretta ma "non intuitiva" nella sua struttura [ParsingMio.pdf, Slide 34, 35]. _(Attenzione, nota metodologica: se in seguito si aggiungono azioni semantiche sintetizzate durante il parsing — es. per costruire un AST — occorre prestare attenzione a preservare esplicitamente l'associatività sinistra semantica, poiché la struttura sintattica destrorsa da sola non lo garantisce automaticamente in presenza di azioni naive.)_ Un parser top-down termina con questa grammatica trasformata, ma potrebbe comunque dover fare backtrack usandola tal quale, senza ulteriore fattorizzazione predittiva [ParsingMio.pdf, Slide 35].
    
- **Il problema più generale — ricorsione sinistra indiretta (slide "Eliminating Left Recursion" #3):** la trasformazione immediata elimina solo la ricorsione sinistra diretta. Cosa succede con la ricorsione sinistra indiretta più generale (es. $A\to B\gamma$, $B\to A\delta$)? **Algoritmo generale:**
    
    ```text
    ordinare i non-terminali in una sequenza A1, A2, …, An
    for i ← 1 to n
        for s ← 1 to i-1
            sostituire ogni produzione Ai → As γ con Ai → δ1γ | δ2γ | … | δkγ,
                dove As → δ1 | δ2 | … | δk sono tutte le produzioni correnti per As
        eliminare ogni ricorsione sinistra immediata su Ai
            usando la trasformazione diretta (sopra)
    ```
    
    Questo presuppone che la grammatica iniziale non abbia cicli ($A_i\Rightarrow^+A_i$) né produzioni $\epsilon$ [ParsingMio.pdf, Slide 36].
    
- **Come funziona l'algoritmo (slide "Eliminating Left Recursion" #4):**
    
    1. Si impone un ordine arbitrario sui non-terminali.
    2. Il loop esterno scorre i non-terminali in ordine.
    3. Il loop interno garantisce che una produzione che espande $A_i$ non contenga alcun non-terminale $A_s$ nella sua rhs, per $s<i$.
    4. L'ultimo passo del loop esterno converte ogni ricorsione diretta su $A_i$ in ricorsione destra usando la trasformazione già vista.
    5. I nuovi non-terminali sono aggiunti in fondo all'ordine e non hanno ricorsione sinistra.
    
    **Invariante:** all'inizio della $i$-esima iterazione del loop esterno, per ogni $k<i$, nessuna produzione che espande $A_k$ contiene un non-terminale $A_s$ nella sua rhs, per $s<k$ [ParsingMio.pdf, Slide 37].
    
- **Esempio Svolto — ordine $G,E,T$ (slide "Example"):**
    
    ![[Pasted image 20260907111522.png]]
    
    Grammatica finale: $G\to E$; $E\to TE'$; $E'\to{+}TE'\mid\epsilon$; $T\to id,T'$; $T'\to E'{*}T,T'\mid\epsilon$ [ParsingMio.pdf, Slide 38]. Si noti come il passo 3 introduca temporaneamente una nuova ricorsione sinistra immediata su $T$ (tramite la sostituzione), risolta poi al passo 4 — questo è il meccanismo generale con cui l'algoritmo gestisce le dipendenze indirette tra non-terminali.
    

### 4.10 Parsing Predittivo e Grammatiche LL(k)

- **Come scegliere la produzione "giusta" (slide "Picking the Right Production"):** se sceglie la produzione sbagliata, un parser top-down può fare backtrack (§4.8). L'alternativa è guardare avanti nell'input (_lookahead_) e usare il contesto per scegliere correttamente. Quanto lookahead serve? In generale, una quantità arbitrariamente grande — si userebbero l'algoritmo di Cocke-Younger-Kasami (CYK) o l'algoritmo di Earley. Fortunatamente, ampie sottoclassi di CFG possono essere parsate con lookahead limitato, e la maggior parte dei costrutti dei linguaggi di programmazione ricade in queste sottoclassi. Tra le sottoclassi interessanti: le grammatiche **LL(1)** e **LR(1)** [ParsingMio.pdf, Slide 39].
- **Grammatiche LL(k) (slide):** una grammatica LL è una CFG che può essere parsata da un parser LL, che analizza l'input da sinistra a destra (**L**eft-to-right) e costruisce una derivazione **L**eftmost. Un linguaggio che ammette una grammatica LL è detto linguaggio LL. Per un $k$ fissato, LL($k$) è una grammatica LL che può predire la produzione corretta da applicare con un lookahead di al più $k$ simboli: $$LL(0) \subset LL(1) \subset LL(2) \subset \dots \subset LL(*)$$ [ParsingMio.pdf, Slide 40, 42].
- **Idea base del parsing predittivo (slide "Predictive Parsing"):** dato $A\to\alpha\mid\beta$, il parser dovrebbe poter scegliere (tra $\alpha$ e $\beta$) la produzione giusta per espandere $A$ nel parse tree, a ogni passo [ParsingMio.pdf, Slide 41, 43].
- **Insieme FIRST (slide):** per un rhs $\alpha\in(N\cup\Sigma)^*$, FIRST($\alpha$) è l'insieme dei terminali che compaiono come primo simbolo in una qualche stringa derivata da $\alpha$: $x\in\text{FIRST}(\alpha) \iff \alpha\Rightarrow^*x\gamma$ per qualche $\gamma$ [ParsingMio.pdf, Slide 43, 54].
- **La proprietà LL(1) (slide):** se $A\to\alpha$ e $A\to\beta$ compaiono entrambe nella grammatica, vorremmo $\text{FIRST}(\alpha)\cap\text{FIRST}(\beta)=\emptyset$ — questo permetterebbe al parser di fare la scelta corretta con un lookahead di esattamente un simbolo [ParsingMio.pdf, Slide 43]. **Questo è quasi corretto** — le produzioni $\epsilon$ complicano la definizione [ParsingMio.pdf, Slide 44].
- **Il problema delle produzioni $\epsilon$ e FIRST⁺ (slide):** se $A\to\alpha$ e $A\to\beta$ ed $\epsilon\in\text{FIRST}(\alpha)$, occorre garantire che anche $\text{FIRST}(\beta)$ sia disgiunto da FOLLOW($A$), dove FOLLOW($A$) è l'insieme dei terminali che possono seguire immediatamente $A$ in una forma sentenziale. Si definisce: $$\text{FIRST}^+(A\to\alpha) = \begin{cases}\text{FIRST}(\alpha)\cup\text{FOLLOW}(A) & \text{se }\epsilon\in\text{FIRST}(\alpha)\ \text{FIRST}(\alpha) & \text{altrimenti}\end{cases}$$ Una grammatica è LL(1) se e solo se $A\to\alpha$ e $A\to\beta$ implica $\text{FIRST}^+(A\to\alpha)\cap\text{FIRST}^+(A\to\beta)=\emptyset$ [ParsingMio.pdf, Slide 44].
- **Codice predittivo generico (slide "Predictive Parsing" #3):** data $A\to\beta_1\mid\beta_2\mid\beta_3$ con $\text{FIRST}^+(A\to\beta_i)\cap\text{FIRST}^+(A\to\beta_j)=\emptyset$ per $i\ne j$:
    
    ```text
    /* trova una A */
    if (parola_corrente ∈ FIRST(A→β1))      trova un β1 e restituisci vero
    else if (parola_corrente ∈ FIRST(A→β2)) trova un β2 e restituisci vero
    else if (parola_corrente ∈ FIRST(A→β3)) trova un β3 e restituisci vero
    else segnala un errore e restituisci falso
    ```
    
    (naturalmente "trovare un $\beta_i$" richiede più dettaglio — una procedura per ciascun non-terminale) [ParsingMio.pdf, Slide 45]. Le grammatiche con la proprietà LL(1) sono dette **grammatiche predittive**, perché il parser può "predire" l'espansione corretta a ogni punto del parsing; i parser che sfruttano questa proprietà sono detti **parser predittivi**. Un tipo di parser predittivo è il **parser ricorsivo a discesa** [ParsingMio.pdf, Slide 45].

### 4.11 Calcolo Formale di FIRST e FOLLOW: le Regole Generali

- **Regole per il calcolo di FIRST(X) (slide "Computing FIRST Sets"):**
    - Per ogni terminale $X$: $\text{FIRST}(X)={X}$.
    - Per ogni non-terminale $X$, se $X\to Y_1Y_2\dots Y_n$ è una produzione: $\text{FIRST}(Y_1)\subseteq\text{FIRST}(X)$; inoltre, se $Y_1,\dots,Y_k$ sono nullificabili ($Y_i\Rightarrow^*\epsilon$), allora anche $\text{FIRST}(Y_{k+1})\subseteq\text{FIRST}(X)$ [ParsingMio.pdf, Slide 55]. (Ci si interessa a FIRST(X) solo per i non-terminali; per i terminali è banale. Per determinare FIRST($A$) occorre ispezionare tutte le produzioni che hanno $A$ sulla sinistra [ParsingMio.pdf, Slide 56].)
- **Regole per il calcolo di FOLLOW(X) (slide "Computing FOLLOW Sets"):**
    - Se $S$ è il simbolo iniziale, \$$\in\text{FOLLOW}(S)$.
    - Se $A\to\alpha B\beta$ è una produzione, $\text{FIRST}(\beta)\subseteq\text{FOLLOW}(B)$.
    - Se $A\to\alpha B$ è una produzione, oppure $A\to\alpha B\beta$ con $\beta$ nullificabile, allora $\text{FOLLOW}(A)\subseteq\text{FOLLOW}(B)$ [ParsingMio.pdf, Slide 60]. (Ci si interessa a FOLLOW(X) solo per i non-terminali; per determinare FOLLOW($A$) occorre ispezionare tutte le produzioni che hanno $A$ sulla destra [ParsingMio.pdf, Slide 61].)
- **Nota metodologica:** l'esempio completo di calcolo di FIRST/FOLLOW passo-passo su una grammatica $E,E',T,T',F$ — con la catena di ragionamento esplicita ("$E$ compare a sinistra in una sola produzione $E\to TE'$; quindi $\text{FIRST}(T)\subseteq\text{FIRST}(E)$; inoltre $T$ non è nullificabile; quindi $\text{FIRST}(E)=\text{FIRST}(T)$", e così via) [ParsingMio.pdf, Slide 57–66] — è la **stessa identica grammatica** già trattata come "Caso di Studio Svolto: la Grammatica delle Espressioni Classica" al §4.15 di questa dispensa (con `number`/`id`/parentesi al posto delle sole variabili $F$): si rimanda a quella sezione per la tabella FIRST/FOLLOW/FIRST⁺ completa e la tabella di parsing risultante, che coincidono.

### 4.12 Recursive Descent Parsing: il Parser Ricorsivo a Discesa

- **Idea (slide "Recursive Descent Parsing"):** data la grammatica delle espressioni dopo la trasformazione (eliminazione della ricorsione sinistra, §4.9): 
	```
		1.  Goal    → Expr
		
		2.  Expr    → Term Expr'
		
		3.  Expr'   → + Term Expr'
		4.          | - Term Expr'
		5.          | ε
		
		6.  Term    → Factor Term'
		
		7.  Term'   → * Factor Term'
		8.          | / Factor Term'
		9.          | ε
		
		10.  Factor  → ( Expr )
		11.         | number
		12.         | id
	```
	
	questa grammatica produce un parser con **sei routine mutuamente ricorsive**: `Goal`, `Expr`, `EPrime`, `Term`, `TPrime`, `Factor` — ciascuna riconosce un non-terminale o un terminale. Il termine "discesa" (_descent_) si riferisce alla direzione in cui viene costruito il parse tree [ParsingMio.pdf, Slide 46].
- **Implementazione procedurale (slide "Recursive Descent Parsing (Procedural)"):**
    
    ```text
    Goal()    token ← next_token();    if (Expr() = true & token = EOF)        then procedi al prossimo passo di compilazione;        else            segnala errore di sintassi;            return false;Expr()    if (Term() = false)        then return false;        else return Eprime();
    ```
    
    [ParsingMio.pdf, Slide 47].
- **`Factor()` (slide "Recursive Descent Parsing II"):**
    ```text
	    Factor()
	    if (token = Number) then
	        token ← next_token();
	        return true;
	
	    else if (token = Identifier) then
	        token ← next_token();
	        return true;
	
	    else if (token = Lparen) then
	        token ← next_token();
	
	        if (Expr() = true and token = Rparen) then
	            token ← next_token();
	            return true;
	        end if;
	
	    end if;
	
	    // Cercava Number, Identifier o "(".
	    // È stato trovato un token diverso, oppure
	    // Expr() o ")" è mancante dopo "(".
	    segnala errore di sintassi;
	    return false;
    ```
    
    `EPrime`, `Term` e `TPrime` seguono le stesse linee di base [ParsingMio.pdf, Slide 48]. Questa è l'implementazione **manuale** (hand-coded) del parsing predittivo, complementare all'approccio table-driven di §4.14–4.16: entrambe realizzano lo stesso algoritmo LL(1), ma la prima lo codifica direttamente come struttura di chiamate a funzione, la seconda lo interpreta a partire da una tabella esplicita.

### 4.13 Left Factoring: l'Algoritmo Generale e un Esempio Svolto

- **Cosa fare se la grammatica non è LL(1)? (slide "What If My Grammar Is Not LL(1)?"):** si può trasformare una grammatica non-LL(1) in una LL(1)? In generale la risposta è no, ma **a volte sì**. Si assuma una grammatica $G$ con produzioni $A\to\alpha\beta_1$ e $A\to\alpha\beta_2$: se $\alpha$ deriva qualcosa di diverso da $\epsilon$, allora $\text{FIRST}^+(A\to\alpha\beta_1)\cap\text{FIRST}^+(A\to\alpha\beta_2)\ne\emptyset$ e la grammatica non è LL(1). Se si estrae il prefisso comune $\alpha$ in una produzione separata, si può rendere la grammatica LL(1): $$A\to\alpha A', \qquad A'\to\beta_1, \qquad A'\to\beta_2$$ Ora, se $\text{FIRST}^+(A'\to\beta_1)\cap\text{FIRST}^+(A'\to\beta_2)=\emptyset$, $G$ potrebbe essere LL(1) [ParsingMio.pdf, Slide 50].
- **Algoritmo generale di Left Factoring (slide "Left Factoring"):** 
    ```text
		Per ogni non-terminale A:
		
		    trova il prefisso α più lungo comune a due o più alternative di A;
		
		    if α ≠ ε then
		
		        sostituisci tutte le produzioni
		
		            A → α β₁
		              | α β₂
		              | α β₃
		              | ...
		              | α βₙ
		              | γ
		
		        con
		
		            A  → α A'
		              | γ
		
		            A' → β₁
		               | β₂
		               | β₃
		               | ...
		               | βₙ
		
		    end if;
		
		Ripeti finché nessun non-terminale ha alternative nel lato destro
		che condividono un prefisso comune.
    ```
    
    Questa trasformazione rende LL(1) alcune grammatiche. **Esistono linguaggi per cui non esiste alcuna grammatica LL(1)** [ParsingMio.pdf, Slide 51].
- **Esempio Svolto (slide "Left Factoring Example"):** si consideri una semplice grammatica delle espressioni right-recursive:
    
    ```
		1.  Goal    → Expr
		
		2.  Expr    → Term + Expr
		3.          | Term - Expr
		4.          | Term
		
		5.  Term    → Factor * Term
		6.          | Factor / Term
		7.          | Factor
		
		8.  Factor  → number
		9.          | id

    ```
    
    [ParsingMio.pdf, Slide 52]. Sia in `Expr` (alternative 1,2,3 condividono il prefisso `Term`) sia in `Term` (alternative 4,5,6 condividono il prefisso `Factor`) c'è un prefisso comune. **Dopo il Left Factoring:**
    
    ```
		1. Goal    → Expr
		
		2.  Expr    → Term Expr'
		
		3.  Expr'   → + Expr
		4.          | - Expr
		5.          | ε
		
		6.  Term    → Factor Term'
		
		7.  Term'   → * Term
		8.          | / Term
		9.          | ε
		
		10.  Factor  → number
		11.         | id
    ```
    
    [ParsingMio.pdf, Slide 53]. **Confronto con l'eliminazione della ricorsione sinistra (§4.9):** si noti la somiglianza strutturale con l'esito della rimozione della ricorsione sinistra — in entrambi i casi si introduce un nuovo non-terminale "primato" ($Expr'$, $Term'$) — ma qui il problema di partenza era una grammatica già priva di ricorsione sinistra (è _right_-recursive), bensì afflitta da **prefissi comuni** fra alternative dello stesso non-terminale; le due trasformazioni (eliminazione ricorsione sinistra e left factoring) risolvono quindi due patologie distinte che possono entrambe violare la condizione LL(1), pur producendo forme finali strutturalmente simili.

### 4.14 Costruzione della Tabella di Parsing LL(1)

- **Proprietà LL(1):** una grammatica è LL(1) se e solo se, per ogni coppia di produzioni distinte dello stesso non-terminale $A \rightarrow \alpha$ e $A \rightarrow \beta$, si ha $\text{FIRST}^+(A \rightarrow \alpha) \cap \text{FIRST}^+(A \rightarrow \beta) = \emptyset$ [ParsingMio.pdf, Slide 44].
    
- **Algoritmo di Riempimento della Tabella (slide "Building Top-down Parsers" — "Filling in TABLE[X,y]"):** per $X\in N$, $y\in\Sigma$:
    
    1. l'entry è la regola $X\to\beta$ se $y\in\text{FIRST}^+(X\to\beta)$;
    2. l'entry è "errore" se la regola 1 non definisce alcuna produzione.
    
    Se una qualsiasi entry ha più di una regola, $G$ non è LL(1). Questo algoritmo è detto **algoritmo di costruzione della tabella LL(1)** [ParsingMio.pdf, Slide 74].
    

### 4.15 Caso di Studio Svolto: la Grammatica delle Espressioni Classica

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

**FIRST (slide, calcolati "dal basso"):** `FIRST(F) = FIRST(T) = FIRST(E) = FIRST(Goal) = {(, id, num}` (F non nullificabile); `FIRST(E') = {+, -, ε}`; `FIRST(T') = {*, /, ε}` [ParsingMio.pdf, Slide 57–59].

**FOLLOW (slide, passo-passo):**

- `FOLLOW(E) = {$, )}` (start symbol; E compare in `F → (E)`);
- `FOLLOW(E') = FOLLOW(E) = {$, )}` (E' è ultimo in `E → T E'` e in `E' → + T E'`);
- `FOLLOW(T) = FIRST(E')\{ε} ∪ FOLLOW(E) ∪ FOLLOW(E') = {+, -, $, )}` (E' nullificabile);
- `FOLLOW(T') = FOLLOW(T) = {+, -, $, )}`;
- `FOLLOW(F) = FIRST(T')\{ε} ∪ FOLLOW(T) ∪ FOLLOW(T') = {*, /, +, -, $, )}` (T' nullificabile).

[ParsingMio.pdf, Slide 62–66].

**Tabella di parsing LL(1) (slide):**

|NT \ T|+|−|*|/|id|num|(|)|$|
|---|---|---|---|---|---|---|---|---|---|
|**Goal**|||||0|0|0|||
|**Expr**|||||1|1|1|||
|**Expr'**|2|3||||||4|4|
|**Term**|||||5|5|5|||
|**Term'**|8|8|6|7||||8|8|
|**Factor**|||||10|9|11|||

[ParsingMio.pdf, Slide 67, 70, 71]. Nessuna cella contiene più di una produzione ⇒ **grammatica LL(1)**.

### 4.16 Skeleton Parser LL(1) (table-driven)

```
word ← NextWord()
push $ onto Stack                    // la pila traccia la frontiera del parse tree
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

[ParsingMio.pdf, Slide 73].

#### ✴️ Esercizio d'Esame: La grammatica begin-end (svolto)

Grammatica esatta della slide finale di _TableConstruction.pdf_ ("Construct the table for descendent parser…") [TableConstruction.pdf, Slide 30]:

1. $P \rightarrow begin\ L\ end$
2. $L \rightarrow ST$
3. $T \rightarrow ST \mid \epsilon$
4. $S \rightarrow id := E; \mid read(id); \mid write(E);$
5. $E \rightarrow FG$
6. $G \rightarrow + FG \mid \epsilon$
7. $F \rightarrow (E) \mid id$

> **Nota metodologica:** questa soluzione non è presente nelle slide (che pongono l'esercizio senza risolverlo); è stata sviluppata in questa dispensa applicando rigorosamente gli algoritmi FIRST/FOLLOW/FIRST⁺ del §4.10-4.11, a partire dalla grammatica esatta trascritta dalla slide.

**Calcolo di FIRST (risalendo dai non-terminali "foglia" $F$, $G$):**

|Simbolo|FIRST|
|---|---|
|$F$|${ (,\ id }$ ($F$ non nullificabile)|
|$G$|${ +,\ \epsilon }$|
|$E$|$\text{FIRST}(F) = { (,\ id }$ ($E \rightarrow FG$, $F$ non nullificabile ⇒ $G$ non contribuisce)|
|$S$|${ id,\ read,\ write }$ (le tre alternative iniziano con terminali distinti)|
|$T$|$\text{FIRST}(S) \cup {\epsilon} = { id,\ read,\ write,\ \epsilon }$|
|$L$|$\text{FIRST}(S) = { id,\ read,\ write }$ ($S$ non nullificabile in $L \rightarrow ST$)|
|$P$|${ begin }$|

**Calcolo di FOLLOW:**

- $\text{FOLLOW}(P) = { $ }$ (simbolo iniziale).
- $\text{FOLLOW}(L) \supseteq \text{FIRST}(end) = {end}$, da $P \rightarrow begin\ L\ end$ ⇒ $\text{FOLLOW}(L) = {end}$.
- $\text{FOLLOW}(T)$: $T$ è ultimo simbolo in $L \rightarrow ST$ ⇒ $\text{FOLLOW}(T) \supseteq \text{FOLLOW}(L) = {end}$; $T$ è ultimo anche in $T \rightarrow ST$ (auto-ricorsiva, nessuna informazione nuova) ⇒ $\text{FOLLOW}(T) = {end}$.
- $\text{FOLLOW}(S)$: in $L \rightarrow S,T$, $S$ è seguito da $T$: $\text{FOLLOW}(S) \supseteq \text{FIRST}(T)\setminus{\epsilon} = {id, read, write}$; poiché $T$ è nullificabile, $\text{FOLLOW}(S) \supseteq \text{FOLLOW}(L) = {end}$. Stesso ragionamento per $T \rightarrow S,T$. Quindi $\text{FOLLOW}(S) = { id,\ read,\ write,\ end }$.
- $\text{FOLLOW}(E)$: $E$ compare in $S \rightarrow id := E;$ (seguito da `;`), in $S \rightarrow write(E);$ (seguito da `)`) e in $F \rightarrow (E)$ (seguito da `)`) ⇒ $\text{FOLLOW}(E) = { ;,\ ) }$.
- $\text{FOLLOW}(G)$: $G$ è ultimo in $E \rightarrow FG$ ⇒ $\text{FOLLOW}(G) \supseteq \text{FOLLOW}(E) = {;, )}$; $G$ è ultimo anche in $G \rightarrow +FG$ (nessuna informazione nuova) ⇒ $\text{FOLLOW}(G) = { ;,\ ) }$.
- $\text{FOLLOW}(F)$: in $E \rightarrow FG$, $F$ è seguito da $G$: $\text{FOLLOW}(F) \supseteq \text{FIRST}(G)\setminus{\epsilon} = {+}$; poiché $G$ è nullificabile, $\text{FOLLOW}(F) \supseteq \text{FOLLOW}(E) = {;, )}$. Stesso da $G \rightarrow +FG$. Quindi $\text{FOLLOW}(F) = { +,\ ;,\ ) }$.

**FIRST⁺ per ogni produzione e verifica LL(1):**

|#|Produzione|FIRST⁺|
|---|---|---|
|1|$P \rightarrow begin\ L\ end$|${begin}$|
|2|$L \rightarrow ST$|${id, read, write}$|
|3|$T \rightarrow ST$|${id, read, write}$|
|4|$T \rightarrow \epsilon$|$\text{FOLLOW}(T) = {end}$|
|5|$S \rightarrow id := E;$|${id}$|
|6|$S \rightarrow read(id);$|${read}$|
|7|$S \rightarrow write(E);$|${write}$|
|8|$E \rightarrow FG$|${(, id}$|
|9|$G \rightarrow +FG$|${+}$|
|10|$G \rightarrow \epsilon$|$\text{FOLLOW}(G) = {;, )}$|
|11|$F \rightarrow (E)$|${(}$|
|12|$F \rightarrow id$|${id}$|

Per $T$ (produzioni 3, 4): ${id,read,write} \cap {end} = \emptyset$. Per $G$ (produzioni 9, 10): ${+} \cap {;,)} = \emptyset$. Nessun'altra coppia di produzioni condivide lo stesso non-terminale a sinistra ⇒ **grammatica LL(1)**.

**Tabella di parsing $M[A,t]$:**

|NT \ T|begin|id|read|write|(|)|+|;|end|
|---|---|---|---|---|---|---|---|---|---|
|**P**|1|||||||||
|**L**||2|2|2||||||
|**T**||3|3|3|||||4|
|**S**||5|6|7||||||
|**E**||8|||8|||||
|**G**||||||10|9|10||
|**F**||12|||11|||||

**Traccia di parsing per `begin write ( id + id ) ; end` (skeleton parser di §4.16):**

|Pila (top a sinistra)|Input residuo|Regola / Azione|
|---|---|---|
|`P $`|`begin write ( id + id ) ; end $`|$M[P,begin]$: prod. 1 → push `begin L end`|
|`begin L end $`|`begin write ( id + id ) ; end $`|match `begin`|
|`L end $`|`write ( id + id ) ; end $`|$M[L,write]$: prod. 2 → push `S T`|
|`S T end $`|`write ( id + id ) ; end $`|$M[S,write]$: prod. 7 → push `write ( E ) ;`|
|`write ( E ) ; T end $`|`write ( id + id ) ; end $`|match `write`|
|`( E ) ; T end $`|`( id + id ) ; end $`|match `(`|
|`E ) ; T end $`|`id + id ) ; end $`|$M[E,id]$: prod. 8 → push `F G`|
|`F G ) ; T end $`|`id + id ) ; end $`|$M[F,id]$: prod. 12 → push `id`|
|`id G ) ; T end $`|`id + id ) ; end $`|match `id`|
|`G ) ; T end $`|`+ id ) ; end $`|$M[G,+]$: prod. 9 → push `+ F G`|
|`+ F G ) ; T end $`|`+ id ) ; end $`|match `+`|
|`F G ) ; T end $`|`id ) ; end $`|$M[F,id]$: prod. 12 → push `id`|
|`id G ) ; T end $`|`id ) ; end $`|match `id`|
|`G ) ; T end $`|`) ; end $`|$M[G,)]$: prod. 10 (ε) → pop, nessun push|
|`) ; T end $`|`) ; end $`|match `)`|
|`; T end $`|`; end $`|match `;`|
|`T end $`|`end $`|$M[T,end]$: prod. 4 (ε) → pop, nessun push|
|`end $`|`end $`|match `end`|
|`$`|`$`|**successo**|

#### ✴️ Esercizio d'Esame: seconda grammatica LL(1) (svolto)

Grammatica esatta della slide finale di _ParsingMio.pdf_ [ParsingMio.pdf, Slide 75]:

```
S → AB | eDa
A → ab | c
B → dC
C → eC | g
D → fD | g
```

> **Nota metodologica:** anche in questo caso la soluzione non è presente nelle slide (l'esercizio è posto senza risoluzione). **Osservazione correttiva:** a differenza della grammatica begin-end, questa grammatica **non contiene alcuna produzione $\epsilon$** — nessun simbolo è nullificabile. L'esempio è utile per esercitare il calcolo di FIRST/FOLLOW su una grammatica interamente non nullificabile, con alternative lessicalmente disgiunte.

**FIRST:**

- $\text{FIRST}(D) = {f, g}$ ($D \rightarrow fD \mid g$)
- $\text{FIRST}(C) = {e, g}$ ($C \rightarrow eC \mid g$)
- $\text{FIRST}(B) = {d}$ ($B \rightarrow dC$)
- $\text{FIRST}(A) = {a, c}$ ($A \rightarrow ab \mid c$)
- $\text{FIRST}(S) = \text{FIRST}(A) \cup {e} = {a, c, e}$ ($S \rightarrow AB \mid eDa$)

**FOLLOW:**

- $\text{FOLLOW}(S) = {\$}$ (simbolo iniziale).
- $\text{FOLLOW}(A)$: da $S \rightarrow AB$, $A$ seguito da $B$, $B$ non nullificabile ⇒ $\text{FOLLOW}(A) = \text{FIRST}(B) = {d}$.
- $\text{FOLLOW}(B)$: da $S \rightarrow AB$, $B$ ultimo simbolo ⇒ $\text{FOLLOW}(B) = \text{FOLLOW}(S) = {\$}$.
- $\text{FOLLOW}(D)$: da $S \rightarrow eDa$, $D$ seguito da `a` ⇒ $\text{FOLLOW}(D) \supseteq {a}$; da $D \rightarrow fD$, $D$ ultimo simbolo (auto-ricorsiva, nessuna informazione nuova) ⇒ $\text{FOLLOW}(D) = {a}$.
- $\text{FOLLOW}(C)$: da $B \rightarrow dC$, $C$ ultimo simbolo ⇒ $\text{FOLLOW}(C) \supseteq \text{FOLLOW}(B) = {\$}$; da $C \rightarrow eC$, nessuna informazione nuova ⇒ $\text{FOLLOW}(C) = {\$}$.

**FIRST⁺ e verifica LL(1)** (nessuna produzione è nullificabile, quindi $\text{FIRST}^+(A\rightarrow\beta)=\text{FIRST}(\beta)$ direttamente):

|#|Produzione|FIRST⁺|
|---|---|---|
|1|$S \rightarrow AB$|${a, c}$|
|2|$S \rightarrow eDa$|${e}$|
|3|$A \rightarrow ab$|${a}$|
|4|$A \rightarrow c$|${c}$|
|5|$B \rightarrow dC$|${d}$|
|6|$C \rightarrow eC$|${e}$|
|7|$C \rightarrow g$|${g}$|
|8|$D \rightarrow fD$|${f}$|
|9|$D \rightarrow g$|${g}$|

Per $S$: ${a,c} \cap {e} = \emptyset$. Per $A$: ${a}\cap{c}=\emptyset$. Per $C$: ${e}\cap{g}=\emptyset$. Per $D$: ${f}\cap{g}=\emptyset$ ⇒ **grammatica LL(1)**.

**Tabella di parsing $M[A,t]$:**

|NT \ T|a|b|c|d|e|f|g|
|---|---|---|---|---|---|---|---|
|**S**|1||1||2|||
|**A**|3||4|||||
|**B**||||5||||
|**C**|||||6||7|
|**D**||||||8|9|

**Traccia di parsing per `abdg` (= $a,b,d,g$):** $S \Rightarrow AB \Rightarrow abB \Rightarrow abdC \Rightarrow abdg$.

|Pila|Input residuo|Regola / Azione|
|---|---|---|
|`S $`|`a b d g $`|$M[S,a]$: prod.1 → push `A B`|
|`A B $`|`a b d g $`|$M[A,a]$: prod.3 → push `a b`|
|`a b B $`|`a b d g $`|match `a`|
|`b B $`|`b d g $`|match `b`|
|`B $`|`d g $`|$M[B,d]$: prod.5 → push `d C`|
|`d C $`|`d g $`|match `d`|
|`C $`|`g $`|$M[C,g]$: prod.7 → push `g`|
|`g $`|`g $`|match `g`|
|`$`|`$`|**successo**|

<a id="cap5"></a>
## CAPITOLO 5: Parsing Bottom-Up e Tabelle LR(1)
**Sources:** *Bottom_up_Parsing.pdf* (verificato integralmente) / *TableConstruction.pdf*

### 5.1 Il Principio dello Shift-Reduce e il Problema dell'Handle
> **Nota di revisione:** questa sezione è stata riscritta e ricontrollata parola per parola contro il testo integrale di `Bottom_up_Parsing.pdf`, ora disponibile. Le citazioni con numeri di slide generici/segnaposto della stesura precedente sono state sostituite con riferimenti al titolo esatto della slide sorgente (il file non espone una numerazione di pagina nel testo estratto). È stato inoltre corretto un errore concettuale: la "pila semantica a 4 azioni" descritta in precedenza usava già la nozione di *stato* e le tabelle ACTION/GOTO — che nella progressione reale delle slide vengono introdotte solo **più avanti**, come soluzione al problema qui presentato. La versione stateless (senza stati) è quella dell'algoritmo shift-reduce "ingenuo".

*   **Richiamo su derivazioni e forme sentenziali (slide "Bottom-up Parsing (recap of definitions)"):** una derivazione è una sequenza di passi di riscrittura $S \Rightarrow \gamma_0 \Rightarrow \gamma_1 \Rightarrow \dots \Rightarrow \gamma_n \Rightarrow w$; ogni $\gamma_i$ è una **forma sentenziale** (*sentential form*); se $\gamma$ contiene solo terminali è una **frase** di $L(G)$. Espandendo sempre il **primo** non-terminale si ottiene una **derivazione leftmost** (che produce una *left-sentential form*); espandendo sempre l'**ultimo** si ottiene una **derivazione rightmost** (che produce una *right-sentential form*). **I parser bottom-up costruiscono una derivazione rightmost, ma al contrario** (dall'ultimo passo al primo) [Bottom_up_Parsing.pdf, slide "Bottom-up Parsing (recap of definitions)"].
*   **Riduzione (slide "Bottom-up Parsing"):** per ridurre $\gamma_i$ a $\gamma_{i-1}$ si trova un rhs $\beta$ che compare in $\gamma_i$ e lo si sostituisce con il corrispondente lhs $A$ (data la produzione $A\rightarrow\beta$); poiché ogni sostituzione di $\beta$ con $A$ **restringe** la frontiera superiore dell'albero (che ha un solo simbolo invece di $|\beta|$), l'operazione si chiama **reduction** [Bottom_up_Parsing.pdf, slide "Bottom-up Parsing"]. In termini di albero di parsing, il bottom-up procede dalle foglie verso la radice: i nodi senza genitore in un albero parziale ne formano la *frontiera superiore*.
*   **Esempio guida (slide "Bottom-up Parsing" / "Finding Reductions" / "Leftmost reductions for rightmost derivations"):** con la grammatica
    ```
    0. Goal → a A B e
    1. A    → A b c
    2.      | b
    3. B    → d
    ```
    e la stringa di input `abbcde`, la sequenza delle forme sentenziali (dalla stringa fino a `Goal`) con la produzione e la **posizione** (indice del simbolo più a destra del rhs coinvolto) usate a ogni passo è:

| Forma sentenziale | Produzione                 | Posizione |
| ----------------- | -------------------------- | --------- |
| `abbcde`          | 2 ($A\rightarrow b$)       | 2         |
| `aAbcde`          | 1 ($A\rightarrow Abc$)     | 4         |
| `aAde`            | 3 ($B\rightarrow d$)       | 3         |
| `aABe`            | 0 ($Goal\rightarrow aABe$) | 4         |
| `Goal`            | —                          | —         |

Per ricostruire una derivazione rightmost procedendo bottom-up bisogna quindi cercare, a ogni passo, **la sottostringa più a sinistra** che corrisponde al lato destro di una produzione **e che occorre in quel punto della derivazione rightmost** [Bottom_up_Parsing.pdf, slide "Finding Reductions" / "Leftmost reductions for rightmost derivations"].
*   **Definizione formale di Handle (manico) (slide "Finding Reductions (Handles)"):** un *handle* di una forma sentenziale destra $\gamma$ è una coppia $\langle A \rightarrow \beta, k \rangle$ dove $A \rightarrow \beta \in P$ e $k$ è la posizione in $\gamma$ del simbolo **più a destra** di $\beta$. Se $\langle A\rightarrow\beta,k\rangle$ è un handle, sostituire $\beta$ in posizione $k$ con $A$ produce la forma sentenziale destra da cui $\gamma$ deriva nella derivazione rightmost [Bottom_up_Parsing.pdf, slide "Finding Reductions (Handles)"].
    *   **Attenzione (slide, esempio d'errore comune):** un semplice *match* testuale con un rhs **non basta** a trovare l'handle corretto — per la stringa `abbcde` sopra, il primo `b` (posizione 2) è l'handle, **non** il `d` che pure compare come rhs della produzione $B\rightarrow d$: solo `b` occorre correttamente al primo passo della derivazione rightmost inversa [Bottom_up_Parsing.pdf, slide "Finding Reductions (Handles)", nota "For this string is b not d!!"].
    *   **Proprietà (slide):** poiché $\gamma$ è una forma right-sentential, la sottostringa a **destra** di un handle contiene **solo simboli terminali** [Bottom_up_Parsing.pdf, slide "Finding Reductions (Handles)"].
*   **Teorema (unicità dell'handle, slide "Handles Are Unique"):** se $G$ è non ambigua, ogni forma sentenziale destra ha un handle unico. *Dimostrazione (schema della slide):* (1) $G$ non ambigua ⇒ derivazione rightmost unica; (2) ⇒ esiste un'unica produzione $A\rightarrow\beta$ applicata per derivare $\gamma_i$ da $\gamma_{i-1}$; (3) ⇒ un'unica posizione $k$ alla quale $A\rightarrow\beta$ è applicata; (4) ⇒ un'unica coppia $\langle A\rightarrow\beta,k\rangle$. Se sappiamo trovare gli handle, possiamo costruire una derivazione [Bottom_up_Parsing.pdf, slide "Handles Are Unique"].

*   **Shift-Reduce Parsing — la versione "ingenua", senza stati (slide "Shift-reduce Parsing" / "Bottom-up Parser"):** un parser shift-reduce è un automa a pila con **quattro azioni**:
    1.  **Shift:** la prossima parola viene spinta (push) sulla pila.
    2.  **Reduce:** l'estremità destra dell'handle è in cima alla pila; si localizza l'estremità sinistra dell'handle all'interno della pila, si esegue il pop dell'handle e si spinge (push) il lhs corrispondente. Una reduce consiste quindi in $|rhs|$ pop e 1 push.
    3.  **Accept:** termina il parsing e segnala successo.
    4.  **Error:** invoca una routine di segnalazione/recupero dell'errore.

    [Bottom_up_Parsing.pdf, slide "Shift-reduce Parsing"]. **Il problema aperto (slide):** *"But how does the parser know when to shift and when to reduce?"* — la regola operativa di base è: si continua a fare shift finché non si ha un handle in cima alla pila [Bottom_up_Parsing.pdf, slide "Shift-reduce Parsing"].

    Un semplice parser shift-reduce **stateless** che implementa questa idea (slide "Bottom-up Parser"):
    ```text
    push $
    token ← next_token()
    repeat until (top of stack = S and token = EOF)
        if the top of the stack is a handle A → β
        then                               // reduce β a A
            pop |β| symbols off the stack
            push A onto the stack
        else if (token ≠ EOF)
        then                               // shift
            push token
            token ← next_token()
        else                               // serve shift, ma input esaurito
            report an error
    ```
    [Bottom_up_Parsing.pdf, slide "Bottom-up Parser"].
    
	![[Pasted image 20260906174625.png|489]]
    
    **Difetto grave di questo algoritmo (slide):** se il parser non trova mai un handle, continua semplicemente a fare shift, consumando **tutto** l'input prima di segnalare l'errore — un comportamento tutt'altro che desiderabile per la localizzazione degli errori [Bottom_up_Parsing.pdf, slide "Bottom-up Parser", nota "This parser reads all input before reporting an error"]. Inoltre, decidere "è la cima della pila un handle?" è, così formulato, un problema apparentemente oracolare: la slide osserva esplicitamente che *"while the process of finding the next reduction appears to be almost oracular, it can be automated in an efficient way for a large class of grammars"* [Bottom_up_Parsing.pdf, slide "Finding Reductions"]. È esattamente per risolvere questo problema — riconoscere un handle in tempo costante, senza generare esplicitamente derivazioni alternative — che si introducono gli **item LR** e gli **stati** del parser (§5.2): la LR(1) usa per questo il contesto sinistro completo, codificato in uno stato, più **1 simbolo di lookahead** oltre l'handle [Bottom_up_Parsing.pdf, slide "An Important Lesson about Handles" / "LR(1) Parsers"].

*   **Definizione di grammatica LR(1) (slide "LR(1) Parsers"):** una grammatica è LR(1) se, data una derivazione rightmost $S\Rightarrow\gamma_0\Rightarrow\dots\Rightarrow\gamma_n\Rightarrow w$, per ogni $\gamma_i$ è possibile (1) isolare l'handle e (2) determinare la produzione con cui ridurre, osservando **al più 1 simbolo oltre l'estremità destra dell'handle**. "LR(1)" sta per: scansione dell'input da sinistra a destra (**L**eft-to-right), costruzione di una derivazione **R**ightmost (in ordine inverso), **1** simbolo di lookahead [Bottom_up_Parsing.pdf, slide "LR(1) Parsers"]. Il contesto sinistro aggiuntivo codificato negli stati è precisamente il motivo per cui **le grammatiche LR(1) esprimono un superinsieme delle grammatiche LL(1)** [Bottom_up_Parsing.pdf, slide "LR(1) Parsers"] — coerentemente con il diagramma di Venn della slide introduttiva, che colloca $RG \subset LL(1) \subset LR(1) \subset CFG$ [Bottom_up_Parsing.pdf, slide "Bottom-up parser handle a larger class of grammars"].
### 5.2 Gli Item LR e gli Algoritmi di Chiusura
*   **Definizione di Item LR(1):** Un item LR(1) è una coppia ordinata:
    $$[A \rightarrow \beta \bullet \gamma, a]$$
    dove $A \rightarrow \beta\gamma$ è una produzione e $a \in T \cup \{\$\}$ è un simbolo terminale di lookahead [TableConstruction.pdf, Slide 12, 6.1].
    *   Il punto $\bullet$ indica lo stato di avanzamento del parser: ciò che si trova a sinistra è stato riconosciuto, ciò che è a destra è atteso [TableConstruction.pdf, Slide 12, 6.1].
    *   L'item $[A \rightarrow \beta \bullet, a]$ indica che il parser ha riconosciuto l'intera riga destra $\beta$ e deve ridurre a $A$, ma solo se il simbolo di lookahead corrente è esattamente $a$ [TableConstruction.pdf, Slide 12, 6.1].
*   **Algoritmo di Punto Fisso CLOSURE(I):**
    Consente di completare un insieme di item includendo tutte le possibili produzioni attese.
    
	![[Pasted image 20260906175233.png|483]]
    
    ![[Pasted image 20260906180134.png|483]]
    
    ![[Pasted image 20260906180738.png]]
    
    [TableConstruction.pdf, Slide 15, 6.2].
*   **Algoritmo GOTO(I, X):**
    La funzione è definita formalmente come la chiusura dell'insieme di tutti gli item ottenuti "spostando" il punto ($\bullet$) oltre il simbolo $X$
    $$\text{GOTO}(I, X) = \text{CLOSURE}(\{ [A \rightarrow \beta X \bullet \gamma, a] \mid [A \rightarrow \beta \bullet X \gamma, a] \in I \})$$
    ![[Pasted image 20260906180300.png]]
    
    ![[Pasted image 20260906181334.png|525]]
    
    [TableConstruction.pdf, Slide 15, 6.2].
*   **Collezione Canonica degli Insiemi di Item LR(1):**
    Si costruisce l'insieme di tutti gli stati dell'automa del parser calcolando la chiusura dello stato iniziale aumentato $[S' \rightarrow \bullet S, \$]$ e applicando ripetutamente GOTO su ciascun simbolo grammaticale fino al raggiungimento del punto fisso [TableConstruction.pdf, Slide 15].
    
    ![[Pasted image 20260906180346.png|513]]

### 5.3 Riempimento delle Tabelle ACTION e GOTO
*   **Regole di Popolamento delle Tabelle:**
    Per ciascuno stato $i$ (corrispondente all'insieme di item $I_i$):
    *   Se $[A \rightarrow \beta \bullet a \gamma, b] \in I_i$ e $\text{GOTO}(I_i, a) = I_j$ (con $a$ terminale), allora imposta $\text{ACTION}[i, a] = \text{Shift } j$ [TableConstruction.pdf, Slide 15].
    *   Se $[A \rightarrow \beta \bullet, a] \in I_i$, imposta $\text{ACTION}[i, a] = \text{Reduce } A \rightarrow \beta$ (escluso il caso di $S'$) [TableConstruction.pdf, Slide 15].
    *   Se $[S' \rightarrow S \bullet, \$] \in I_i$, imposta $\text{ACTION}[i, \$] = \text{Accept}$ [TableConstruction.pdf, Slide 15].
    *   Se $\text{GOTO}(I_i, A) = I_j$ (con $A$ non-terminale), imposta $\text{GOTO}[i, A] = j$ [TableConstruction.pdf, Slide 15].
    * ![[Pasted image 20260906180553.png]]
      
*   **Risoluzione dei Conflitti:**
    *   **Conflitto Shift/Reduce:** Si verifica se una cella contiene sia un'azione di shift sia una di reduce. Viene tipicamente risolto assegnando priorità allo shift (come nel caso del dangling-else) [TableConstruction.pdf, Slide 22, 6.3].
    *   **Conflitto Reduce/Reduce:** Si verifica se una cella contiene due diverse riduzioni accettabili sullo stesso lookahead. Indica che la grammatica è ambigua e deve essere modificata strutturalmente [TableConstruction.pdf, Slide 22, 6.3].
*   **Lo Skeleton Parser LR(1) (pseudocodice, slide "LR(1) Skeleton Parser"):** una volta costruite ACTION e GOTO, il parser vero e proprio è un semplice automa a pila, molto più snello della versione "ingenua" senza stati vista in §5.1 — la pila ora memorizza **coppie** $(simbolo, stato)$:
    ```text
    stack.push($);
    stack.push(s0);                // stato iniziale
    token = scanner.next_token();
    loop forever {
        s = stack.top();           // legge la cima della pila
        if ( ACTION[s,token] == "reduce A→β" ) then {
            stack.popnum(2*|β|);   // pop di 2*|β| simboli (coppie simbolo,stato)
            s = stack.top();
            stack.push(A);                    // push del non-terminale A
            stack.push(GOTO[s,A]);            // push del nuovo stato
        }
        else if ( ACTION[s,token] == "shift si" ) then {
            stack.push(token); stack.push(si);
            token ← scanner.next_token();
        }
        else if ( ACTION[s,token] == "accept" & token == EOF )
            then break;
        else throw a syntax error;
    }
    report success;
    ```
    
    Il parser si appoggia a uno stack e a uno scanner e usa due tabelle, ACTION (stato × parola → azione) e GOTO (stato × non-terminale → stato); rileva gli errori per fallimento degli altri tre casi [Bottom_up_Parsing.pdf, slide "LR(1) Skeleton Parser"]. 
    
    A differenza del parser stateless di §5.1, qui la decisione "shift o reduce?" è immediata: si consulta semplicemente $\text{ACTION}[s,token]$ — è proprio l'introduzione dello **stato** (che codifica tutto il contesto sinistro rilevante) a eliminare il problema "oracolare" del riconoscimento dell'handle.

### 5.4 Tracce d'Esame Svolte
#### Esempio 0: parsing shift-reduce di `x - 2 * y` (slide "Example" / "Back to x - 2 * y")
Grammatica classica left-recursive (`Goal → Expr`; `Expr → Expr + Term | Expr - Term | Term`; `Term → Term * Factor | Term / Factor | Factor`; `Factor → number | id | ( Expr )`), input `id - num * id` [Bottom_up_Parsing.pdf, slide "Example" (grammatica) e "Back to x - 2 * y" (traccia)]:

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
Consideriamo la grammatica formale dei belati di una pecora [Bottom_up_Parsing.pdf, slide "LR(1) Parsers (parse tables)"]:
1.  $Goal \rightarrow SheepNoise$
2.  $SheepNoise \rightarrow SheepNoise\ baa$
3.  $SheepNoise \rightarrow baa$

L'automa a pila bottom-up utilizza le seguenti tabelle d'azione e di transizione costruite dalle slide [Bottom_up_Parsing.pdf, slide "LR(1) Parsers (parse tables)"]:

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
Questo tracciamento descrive passo-passo la pila del parser, l'input rimanente e l'azione intrapresa [Bottom_up_Parsing.pdf, slide "Example Parse 1"]:
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
Questo tracciamento mostra la gestione dei belati ripetuti [Bottom_up_Parsing.pdf, slide "Example Parse 2"]:
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

#### Esempio 2: Grammatica dei Lookahead Critici (esercizio d'esame, svolto)
Grammatica esatta della slide "Exercise" finale di *TableConstruction.pdf* [TableConstruction.pdf, Slide 27]:
```
Start → S
S     → A a
A     → B C
      | B C f
B     → b
C     → c
```
Numerando le produzioni: **(0)** $Start\rightarrow S$, **(1)** $S\rightarrow Aa$, **(2)** $A\rightarrow BC$, **(3)** $A\rightarrow BCf$, **(4)** $B\rightarrow b$, **(5)** $C\rightarrow c$. Il simbolo aumentato è già $Start$ (come per SheepNoise, non serve introdurre un ulteriore $S'$); lo stato iniziale parte da $[Start \rightarrow \bullet S, \$]$.

> **Nota metodologica:** questa soluzione non è presente nelle slide (che pongono l'esercizio in tre punti — a, b, c — più la richiesta di parsing di `bcfa`/`bca`, senza fornire risposta); è stata sviluppata in questa dispensa applicando rigorosamente CLOSURE e GOTO come definiti in §5.2.

**(a) Costruzione della collezione canonica.**

$\text{FIRST}(B)=\{b\}$, $\text{FIRST}(C)=\{c\}$, $\text{FIRST}(A)=\{b\}$, $\text{FIRST}(S)=\{b\}$.

$s_0 = \text{Closure}(\{[Start\rightarrow\bullet S,\$]\})$:
```
[Start → • S, $]
[S → • A a, $]              (chiusura su S: δ=ε dopo S, lookahead = $)
[A → • B C, a]              (chiusura su A: δ=a dopo A, lookahead ∈ FIRST(a)={a})
[A → • B C f, a]            (idem, seconda alternativa di A)
[B → • b, c]                (chiusura su B: δ=C nella prima; δ=Cf nella seconda; in entrambi i casi lookahead ∈ FIRST(C·resto)={c})
```
$s_0$ ha 5 item; nessun item con • davanti a $C$ (compare solo dopo aver ridotto $B$).

Transizioni da $s_0$:
*   $\text{goto}(s_0,S) = \{[Start\rightarrow S\bullet,\$]\} = s_1$ (stato di accept)
*   $\text{goto}(s_0,A) = \{[S\rightarrow A\bullet a,\$]\} = s_2$
*   $\text{goto}(s_0,B)$: sposto il punto in $[A\rightarrow B\bullet C,a]$, $[A\rightarrow B\bullet Cf,a]$; chiusura aggiunge $[C\rightarrow\bullet c,a]$ (da $A\rightarrow B\bullet C,a$: δ=ε, lookahead $a$) e $[C\rightarrow\bullet c,f]$ (da $A\rightarrow B\bullet Cf,a$: δ=f, lookahead $f$) $= s_3$
*   $\text{goto}(s_0,b) = \{[B\rightarrow b\bullet,c]\} = s_4$ (stato di reduce)

$s_2 = \{[S\rightarrow A\bullet a,\$]\}$: $\text{goto}(s_2,a) = \{[S\rightarrow Aa\bullet,\$]\} = s_5$ (reduce).

$s_3 = \{[A\rightarrow B\bullet C,a],\ [A\rightarrow B\bullet Cf,a],\ [C\rightarrow\bullet c,a],\ [C\rightarrow\bullet c,f]\}$:
*   $\text{goto}(s_3,C) = \{[A\rightarrow BC\bullet,a],\ [A\rightarrow BC\bullet f,a]\} = s_6$
*   $\text{goto}(s_3,c) = \{[C\rightarrow c\bullet,a],\ [C\rightarrow c\bullet,f]\} = s_7$ (reduce su $a$ o $f$)

$s_4 = \{[B\rightarrow b\bullet,c]\}$: nessuna transizione (reduce puro).

$s_5 = \{[S\rightarrow Aa\bullet,\$]\}$: nessuna transizione (reduce puro).

$s_6 = \{[A\rightarrow BC\bullet,a],\ [A\rightarrow BC\bullet f,a]\}$: $\text{goto}(s_6,f) = \{[A\rightarrow BCf\bullet,a]\} = s_8$ (reduce).

**Osservazione cruciale:** $s_6$ contiene *simultaneamente* l'item $[A\rightarrow BC\bullet,a]$ (dot a fine produzione ⇒ riduzione candidata sul lookahead $a$) e l'item $[A\rightarrow BC\bullet f,a]$ (dot prima del terminale $f$ ⇒ shift candidato su $f$). In una costruzione **LR(0)** (senza lookahead) questo sarebbe un conflitto shift/reduce irrisolvibile; in **LR(1)** le due azioni sono innescate da simboli di input diversi — reduce solo se il prossimo simbolo è $a$, shift solo se è $f$ — quindi **non c'è conflitto**.

$s_7 = \{[C\rightarrow c\bullet,a],\ [C\rightarrow c\bullet,f]\}$: nessuna transizione (reduce puro, su $a$ o su $f$).

$s_8 = \{[A\rightarrow BCf\bullet,a]\}$: nessuna transizione (reduce puro).

La collezione canonica ha **9 stati** ($s_0$–$s_8$); non emergono ulteriori collassi di stati oltre a quelli già impliciti nella chiusura di $s_3$ (il singolo stato $s_3$ produce già entrambe le lookahead $a,f$ per $C\rightarrow\bullet c$, quindi non c'è uno stato duplicato da unificare).

**(b) Tabelle ACTION e GOTO:**

| Stato | ACTION `a` | ACTION `b` | ACTION `c` | ACTION `f` | ACTION `$` | GOTO `S` | GOTO `A` | GOTO `B` | GOTO `C` |
|---|---|---|---|---|---|---|---|---|---|
| $s_0$ | | shift $s_4$ | | | | $s_1$ | $s_2$ | $s_3$ | |
| $s_1$ | | | | | **accept** | | | | |
| $s_2$ | shift $s_5$ | | | | | | | | |
| $s_3$ | | | shift $s_7$ | | | | | | $s_6$ |
| $s_4$ | | | reduce (4) $B\rightarrow b$ | | | | | | |
| $s_5$ | | | | | reduce (1) $S\rightarrow Aa$ | | | | |
| $s_6$ | reduce (2) $A\rightarrow BC$ | | | shift $s_8$ | | | | | |
| $s_7$ | reduce (5) $C\rightarrow c$ | | | reduce (5) $C\rightarrow c$ | | | | | |
| $s_8$ | reduce (3) $A\rightarrow BCf$ | | | | | | | | |

Ogni cella contiene **al più un'azione** ⇒ **la grammatica è LR(1)** (risposta al punto (c) della slide), pur non essendo LR(0)/SLR(1): senza il lookahead, lo stato $s_6$ mostrerebbe un conflitto shift/reduce fra $[A\rightarrow BC\bullet]$ e $[A\rightarrow BC\bullet f]$, risolto qui unicamente grazie alla capacità dell'LR(1) di propagare lookahead diversi ($a$ vs $f$) sui due item.

**(d) Traccia di parsing di `bcfa`:**

| Passo | Pila | Input residuo | Lookahead | Azione |
|---|---|---|---|---|
| 0 | $s_0$ | `b c f a $` | `b` | shift → $s_4$ |
| 1 | $s_0\,b\,s_4$ | `c f a $` | `c` | reduce (4) $B\rightarrow b$; pop `b,s_4`; GOTO$(s_0,B)=s_3$; push `B,s_3` |
| 2 | $s_0\,B\,s_3$ | `c f a $` | `c` | shift → $s_7$ |
| 3 | $s_0\,B\,s_3\,c\,s_7$ | `f a $` | `f` | reduce (5) $C\rightarrow c$; pop `c,s_7`; GOTO$(s_3,C)=s_6$; push `C,s_6` |
| 4 | $s_0\,B\,s_3\,C\,s_6$ | `f a $` | `f` | shift → $s_8$ |
| 5 | $s_0\,B\,s_3\,C\,s_6\,f\,s_8$ | `a $` | `a` | reduce (3) $A\rightarrow BCf$; pop 3 coppie (`f,s_8`;`C,s_6`;`B,s_3`); GOTO$(s_0,A)=s_2$; push `A,s_2` |
| 6 | $s_0\,A\,s_2$ | `a $` | `a` | shift → $s_5$ |
| 7 | $s_0\,A\,s_2\,a\,s_5$ | `$` | `$` | reduce (1) $S\rightarrow Aa$; pop `a,s_5`;`A,s_2`; GOTO$(s_0,S)=s_1$; push `S,s_1` |
| 8 | $s_0\,S\,s_1$ | `$` | `$` | **accept** |

`bcfa` viene accettata: 3 shift, 4 reduce, 1 accept.

**Traccia di parsing di `bca`:**

| Passo | Pila | Input residuo | Lookahead | Azione |
|---|---|---|---|---|
| 0 | $s_0$ | `b c a $` | `b` | shift → $s_4$ |
| 1 | $s_0\,b\,s_4$ | `c a $` | `c` | reduce (4) $B\rightarrow b$; GOTO$(s_0,B)=s_3$; push `B,s_3` |
| 2 | $s_0\,B\,s_3$ | `c a $` | `c` | shift → $s_7$ |
| 3 | $s_0\,B\,s_3\,c\,s_7$ | `a $` | `a` | reduce (5) $C\rightarrow c$; GOTO$(s_3,C)=s_6$; push `C,s_6` |
| 4 | $s_0\,B\,s_3\,C\,s_6$ | `a $` | `a` | **reduce (2)** $A\rightarrow BC$ (non shift! lookahead `a` ≠ `f`); pop 2 coppie (`C,s_6`;`B,s_3`); GOTO$(s_0,A)=s_2$; push `A,s_2` |
| 5 | $s_0\,A\,s_2$ | `a $` | `a` | shift → $s_5$ |
| 6 | $s_0\,A\,s_2\,a\,s_5$ | `$` | `$` | reduce (1) $S\rightarrow Aa$; GOTO$(s_0,S)=s_1$; push `S,s_1` |
| 7 | $s_0\,S\,s_1$ | `$` | `$` | **accept** |

`bca` viene accettata anch'essa: 2 shift, 4 reduce, 1 accept. Il passo 4 è quello pedagogicamente rilevante: nello stesso stato $s_6$, un lookahead `a` innesca la riduzione $A\rightarrow BC$ mentre un lookahead `f` (come nella traccia di `bcfa`, passo 4) innesca invece lo shift verso $A\rightarrow BCf$ — la dimostrazione concreta del perché questa grammatica richiede LR(1) e non è gestibile da un automa LR(0)/SLR(1).


### 5.5 Confronto LR(k) vs LL(k) (slide)
*   **LR(k):** ogni riduzione è individuabile con il contesto sinistro **completo**, la frase da ridurre e i $k$ terminali alla sua destra.
*   **LL(k):** la produzione va scelta con il contesto sinistro e i prossimi $k$ terminali, *prima* di aver riconosciuto il corpo.

⇒ LR(k) esamina più contesto; esistono grammatiche LR(0) che non sono LL(k) per alcun $k$ (Knuth 1971; Lewis–Rosenkrantz–Stearns 1976).

| | Vantaggi | Svantaggi |
|---|---|---|
| Top-down / LL(1) | veloce, buona località, semplice, buona diagnosi d'errore | hand-coded, alta manutenzione, associatività a destra |
| LR(1) | veloce, linguaggi deterministici, automatizzabile, associatività a sinistra | working set grandi, messaggi d'errore poveri, tabelle grandi |

<a id="cap6"></a>
<a id="cap6"></a>
## CAPITOLO 6: Analisi Semantica e Sintassi Yacc

**Source:** *ContextsensitiveAnalysisv.pdf*

> **Nota di revisione:** questo capitolo è stato ricontrollato per intero contro il testo integrale di `ContextsensitiveAnalysisv.pdf`. Sono state aggiunte tre precisazioni assenti nella stesura precedente (§6.1, §6.2, §6.3), un collegamento esplicito tra il problema del *load tracking* e la sua soluzione ad-hoc (§6.4/§6.6), un secondo esempio Yacc di type inference su un dominio di tipi distinto (§6.5bis), e la chiusura sul bilancio vantaggi/svantaggi dell'approccio ad-hoc (§6.6, slide "Reality").

### 6.1 Analisi Sensibile al Contesto (Oltre la Sintassi)

- **Limiti delle Grammatiche Context-Free:** una CFG non può, da sola, stabilire se un identificatore è dichiarato prima dell'uso, se il numero di argomenti di una chiamata coincide con l'arità dichiarata, se un'espressione è type-consistent, dove va memorizzato un valore (registro, locale, globale, heap, static), o se due puntatori riferiscono la stessa locazione di memoria [ContextsensitiveAnalysisv.pdf, Slide 3–4]. Queste domande **dipendono da valori, non da parti del discorso**, coinvolgono **informazione non locale** e possono richiedere **computazione** [ContextsensitiveAnalysisv.pdf, Slide 5].
- **Analisi dei sei errori semantici d'esame:**
```c
    fie(int a, int b, int c, int d) { ... }
    fee() {
        int f[3], g[0], h, i, j, k;
        char *p;
        fie(h, i, "ab", j, k);      // Errori 1 e 2
        k = f * i + j;              // Errore 3
        h = g[17];                  // Errore 4
        printf("%s, %s\n", p, q);   // Errore 5
        p = 10;                     // Errore 6
    }
``` 

- **Errore 1 (Wrong number of arguments):** `fie` è dichiarata con 4 parametri formali ma chiamata con 5 argomenti [ContextsensitiveAnalysisv.pdf, Slide 10].
- **Errore 2 (Type mismatch):** la costante stringa `"ab"` è passata dove è atteso un `int` [ContextsensitiveAnalysisv.pdf, Slide 10].
- **Errore 3 (Invalid dimension usage):** l'array `f` (dichiarato `int f[3]`) è usato come scalare in `f * i` [ContextsensitiveAnalysisv.pdf, Slide 10].
- **Errore 4 (Array out of bounds):** accesso a `g[17]` mentre `g` è dichiarato `g[0]` [ContextsensitiveAnalysisv.pdf, Slide 10].
- **Errore 5 (Undeclared variable):** `q` è usata in `printf` ma mai dichiarata [ContextsensitiveAnalysisv.pdf, Slide 10].
- **Errore 6 (Incompatible assignment):** l'intero `10` è assegnato al puntatore `char *p` [ContextsensitiveAnalysisv.pdf, Slide 10].

Tutti questi errori sono **"deeper than syntax"**, al di fuori del potere espressivo di una CFG [ContextsensitiveAnalysisv.pdf, Slide 6]. Per rispondere a queste domande si usano metodi formali (grammatiche sensibili al contesto, grammatiche attribuite) oppure tecniche ad-hoc (symbol table, codice d'azione); **in pratica dominano le tecniche ad-hoc** [ContextsensitiveAnalysisv.pdf, Slide 7].

**Quando avviene l'analisi context-sensitive?** Queste analisi vengono tipicamente eseguite o **insieme al parsing** (azioni innestate nelle produzioni, eseguite a ogni riduzione o regola sintattica) oppure in un **post-pass** che attraversa la IR già prodotta dal parser [ContextsensitiveAnalysisv.pdf, slide "When?"]. Questa distinzione anticipa la scelta pratica che il capitolo svilupperà: il corso presenterà prima il formalismo delle grammatiche attribuite (per chiarire i problemi in modo rigoroso), per poi mostrare come la pratica reale preferisca la traduzione ad-hoc innestata nel parsing [ContextsensitiveAnalysisv.pdf, slide "Beyond Syntax — Telling the story"].

### 6.2 Grammatiche Attribuite (Attribute Grammars)

Una grammatica attribuita è una CFG aumentata con regole che calcolano valori: ogni simbolo del parse tree ha un insieme di attributi con nome, e ogni attributo è definito **funzionalmente** da regole che possono riferire solo attributi **locali alla stessa produzione** [ContextsensitiveAnalysisv.pdf, Slide 15].

- **Attributi Sintetizzati (Synthesized):** usano valori dei figli e di costanti; formano le _S-attributed grammars_; si valutano in un'unica passata bottom-up ottimo accoppiamento con il parsing LR [ContextsensitiveAnalysisv.pdf, Slide 15, 32].
- **Attributi Ereditati (Inherited):** usano valori del genitore, di costanti o di fratelli; ritenuti più "naturali" ma **non facilmente calcolabili durante il parsing** [ContextsensitiveAnalysisv.pdf, Slide 15, 32].

#### Esempio guida: valore di numeri binari con segno

Grammatica (`Number → Sign List`; `List → List Bit | Bit`; `Bit → 0 | 1`; `Sign → + | −`), che genera numeri binari con segno come `-10010` o `+00101` [ContextsensitiveAnalysisv.pdf, Slide 9]. Attributi: `Number.val` (synth.), `Sign.neg` (synth.), `List.pos, List.val` (pos ered., val synth.), `Bit.pos, Bit.val` (pos ered., val synth.) [ContextsensitiveAnalysisv.pdf, Slide 12].

**Regole di attribuzione corrette** [ContextsensitiveAnalysisv.pdf, Slide 13]:

```
Number → Sign List     List.pos ← 0
                       if Sign.neg
                          then Number.val ← − List.val
                          else Number.val ← List.val

Sign → +               Sign.neg ← false
Sign → −               Sign.neg ← true

List0 → List1 Bit      List1.pos ← List0.pos + 1
                       Bit.pos  ← List0.pos
                       List0.val ← List1.val + Bit.val

List → Bit             Bit.pos ← List.pos
                       List.val ← Bit.val

Bit → 0                Bit.val ← 0
Bit → 1                Bit.val ← 2^Bit.pos
```

**Valutazione di "−101"** [ContextsensitiveAnalysisv.pdf, Slide 14, 18–21]: `Sign.neg = true`; `List(pos 0).val = 5`; `List(pos 1).val = 4`; `List(pos 2).val = 4`; `Bit(pos 2)='1' → val 4`; `Bit(pos 1)='0' → val 0`; `Bit(pos 0)='1' → val 1`; `Number.val = −5`. Un ordine di valutazione coerente col grafo delle dipendenze (regola di Knuth: attributi indipendenti prima, poi gli altri man mano disponibili): `List.pos → Sign.neg → Bit.pos → Bit.val → List.val → Number.val` [ContextsensitiveAnalysisv.pdf, Slide 16]. Regole + parse tree implicano un **grafo delle dipendenze**, che deve essere **aciclico** i metodi dinamici lo ordinano a runtime, i metodi rule-based analizzano le regole per trovare un buon ordine, i metodi _oblivious_ ignorano la struttura del grafo [ContextsensitiveAnalysisv.pdf, Slide 22].

**N.B. metodologico:** attributi associati ai nodi del parse tree; le regole sono assegnazioni di valori associate alle produzioni; ogni attributo è definito una sola volta, usando informazione locale; regole e parse tree definiscono un grafo delle dipendenze che deve essere non-circolare. Questo produce una specifica funzionale di alto livello — serve poi un **evaluator** per la grammatica attribuita: **una AG è una specifica per il calcolo, non un algoritmo** [ContextsensitiveAnalysisv.pdf, slide "The Rules of the Game"]. Questa distinzione è centrale: il resto del capitolo mostra prima come tale specifica possa essere realizzata (evaluator dinamici, rule-based, oblivious), poi perché in pratica si preferisca abbandonarla in favore di azioni ad-hoc innestate nel parser (§6.6).

### 6.3 Circolarità nelle Grammatiche Attribuite

Una grammatica attribuita produce valori **determinati** solo se il suo grafo delle dipendenze è aciclico per ogni istanza generata; una grammatica **circolare**, al contrario, non ammette affatto un valore ben definito per l'attributo coinvolto — non si tratta soltanto di un limite degli algoritmi di valutazione, che semplicemente falliscono nel tentativo di eseguire un calcolo privo di senso. Da qui la scelta, quando possibile, di lavorare con grammatiche **provabilmente non circolari** [ContextsensitiveAnalysisv.pdf, slide "Circularity — The Point"].

- **Il problema:** una AG è circolare se le sue regole inducono dipendenze cicliche tra attributi per qualche albero. Le grammatiche circolari producono **valori indeterminati**: i valutatori algoritmici falliscono [ContextsensitiveAnalysisv.pdf, Slide 23, 30].
- **Test SNC (Strongly Non-Circular):** il test di circolarità generale è intrinsecamente esponenziale; la classe delle grammatiche **Strongly Non-Circular** è la più ampia classe testabile in tempo polinomiale fallire il test SNC non è conclusivo (condizione solo sufficiente) [ContextsensitiveAnalysisv.pdf, Slide 23].

**Esempio di grammatica circolare** (corretto, con la regola di inizializzazione mancante nella versione precedente) [ContextsensitiveAnalysisv.pdf, Slide 24]:

```
Number → List           List.a ← 0

List0 → List1 Bit       List1.a ← List0.a + 1
                        List0.b ← List1.b
                        List1.c ← List1.b + Bit.val

List0 → Bit             List0.b ← List0.a + List0.c + Bit.val

Bit → 0                 Bit.val ← 0
Bit → 1                 Bit.val ← 1
```

Il ciclo emerge quando `List1` si espande a sua volta in `Bit` (caso base): la regola della produzione genitrice impone `List1.c ← List1.b + Bit.val`, mentre la regola del caso base impone `List1.b ← List1.a + List1.c + Bit.val` cioè **`List1.b` dipende da `List1.c` che dipende da `List1.b`** [ContextsensitiveAnalysisv.pdf, Slide 27–29].

Come conseguenza pratica, molti sistemi di valutazione **scoprono la circolarità dinamicamente** (a runtime, durante la valutazione), il che è una proprietà indesiderabile per un compilatore: si preferisce quindi restringersi, quando fattibile, a schemi provabilmente non circolari, così da rendere la valutazione più semplice e prevedibile [ContextsensitiveAnalysisv.pdf, slide "Circularity"].

### 6.4 Un secondo esempio: costo di un basic block

Grammatica per un basic block, usata per stimare il numero di cicli macchina [ContextsensitiveAnalysisv.pdf, Slide 33]:

```
1  Block0 → Block1 Assign
2         | Assign
3  Assign0 → Ident = Expr ;
4  Expr0  → Expr1 + Term
5         | Expr1 - Term
6         | Term
7  Term0  → Term1 * Factor
8         | Term1 / Factor
9         | Factor
10 Factor → ( Expr )
11        | Number
12        | Ident
```

Regole (tutte **sintetizzate**, valori che fluiscono da rhs a lhs) [ContextsensitiveAnalysisv.pdf, Slide 34]:

```
1  Block0.cost ← Block1.cost + Assign.cost
2  Block0.cost ← Assign.cost
3  Assign.cost ← COST(store) + Expr.cost
4  Expr0.cost ← Expr1.cost + COST(add) + Term.cost
5  Expr0.cost ← Expr1.cost + COST(sub) + Term.cost
6  Expr0.cost ← Term.cost
7  Term0.cost ← Term1.cost + COST(mult) + Factor.cost
8  Term0.cost ← Term1.cost + COST(div) + Factor.cost
9  Term0.cost ← Factor.cost
10 Factor.cost ← Expr.cost
11 Factor.cost ← COST(loadI)
12 Factor.cost ← COST(load)
```

Essendo una **S-attributed grammar**, si valuta bottom-up in una singola passata, ben accoppiata al parsing shift/reduce [ContextsensitiveAnalysisv.pdf, Slide 35]. Un miglioramento realistico (caricare un valore una sola volta per blocco, non a ogni uso) richiederebbe due attributi ereditati **before/after** (insiemi di nomi già caricati) propagati lungo tutto l'albero informazione **non locale**, che moltiplica rapidamente le "regole di copia" e i requisiti di spazio [ContextsensitiveAnalysisv.pdf, Slide 36–41].

Questo stesso problema di *load tracking* — evitare ricariche ridondanti nello stesso blocco — verrà ripreso in §6.6 con una soluzione ad-hoc radicalmente più semplice: una tabella hash **globale** `Table[i].loaded`, aggiornata direttamente dalle azioni associate alle riduzioni, senza alcuna necessità di attributi ereditati o di regole di copia [ContextsensitiveAnalysisv.pdf, slide "Reworking the Example (with load tracking)"]. Il confronto tra la versione con attributi before/after e la versione con tabella globale è di per sé la miglior illustrazione del perché, in pratica, si preferisca abbandonare l'approccio funzionale puro.

### 6.5 Un terzo esempio: inferenza dei tipi

Assumendo che `name` e `num` abbiano già un attributo `type`, e date tabelle di conversione $\mathcal{F}_+,\mathcal{F}_-,\mathcal{F}_\times,\mathcal{F}_\div$ (es. `integer + double → double`, `double + complex → illegal`) [ContextsensitiveAnalysisv.pdf, Slide 43–44]:

```
Expr0 → Expr1 + Term    Expr0.type ← F+(Expr1.type, Term.type)
      | Expr1 - Term    Expr0.type ← F-(Expr1.type, Term.type)
      | Term             Expr0.type ← Term.type
Term0 → Term1 Factor    Term0.type ← F×(Term1.type, Factor.type)
      | Term1 Factor    Term0.type ← F÷(Term1.type, Factor.type)
      | Factor           Term0.type ← Factor.type
Factor → (Expr)          Factor.type ← Expr.type
       | num             num.type già definito
       | name             name.type già definito
```

Anche qui: per popolare `name.type`/`num.type` servirebbe propagare informazione di dichiarazione attraverso l'intero albero di nuovo molte regole di copia [ContextsensitiveAnalysisv.pdf, Slide 45–47].

#### 6.5bis Esempio Yacc equivalente: assegnazione dei tipi nei nodi d'espressione

La stessa inferenza di tipo può essere realizzata con azioni Yacc invece che con regole di attribuzione pure, assumendo tabelle di conversione $F_+,F_-,F_\times,F_\div$ analoghe — qui su un dominio di tipi distinto, `Int16, Int32, Float, Double`, per mostrare che la tecnica non dipende dal dominio scelto [ContextsensitiveAnalysisv.pdf, slide "Example — Assigning Types in Expression Nodes"]:

```yacc
1  Goal   → Expr           $$ = $1;
2  Expr   → Expr + Term    $$ = F+($1,$3);
3         | Expr - Term    $$ = F-($1,$3);
4         | Term            $$ = $1;
5  Term   → Term * Factor  $$ = Fx($1,$3);
6         | Term / Factor  $$ = F÷($1,$3);
7         | Factor          $$ = $1;
8  Factor → ( Expr )       $$ = $2;
9         | number         $$ = type of num;
10        | ident          $$ = type of ident;
```

Anche qui si assume che le foglie `number`/`ident` abbiano **già** un attributo `type` popolato da una fase precedente [ContextsensitiveAnalysisv.pdf, slide "Example — Assigning Types in Expression Nodes"]. Frammento della tabella $F_\times$ di riferimento:

| $\times$ | Int16 | Int32 | Float | Double |
|---|---|---|---|---|
| Int16 | Int16 | Int32 | Float | Double |
| Int32 | Int32 | Int32 | Float | Double |
| Float | Float | Float | Float | Double |
| Double | Double | Double | Double | Double |

Questo esempio dimostra che la traduzione ad-hoc **non stravolge** la struttura delle regole di una AG S-attributed: sostituisce solo la notazione simbolica (`Expr.type`, `Term.type`, …) con `$$`/`$n`, mantenendo intatta la logica bottom-up. È esattamente il ponte concettuale verso §6.6.

### 6.6 Traduzione Guidata dalla Sintassi Ad-Hoc (SDT) e Yacc

Le grammatiche attribuite gestiscono bene flussi locali e monodirezionali, ma l'informazione non locale richiede molte regole di copia, che aumentano il carico cognitivo e lo spazio occupato [ContextsensitiveAnalysisv.pdf, Slide 48]. La soluzione realistica: abbandonare l'approccio funzionale puro e usare un **repository centrale** (symbol table) che le azioni possono leggere/scrivere liberamente [ContextsensitiveAnalysisv.pdf, Slide 49–50].

- **Sintassi Yacc:** azioni in C associate a ogni produzione, eseguite a ogni riduzione [ContextsensitiveAnalysisv.pdf, Slide 25, 51].
    - **`$$`** = attributo del non terminale a sinistra (LHS).
    - **`$1, $2, …, $n`** = valori dei simboli a destra (RHS), contati da sinistra.
- **Pila semantica parallela:** il parser LR mantiene una pila semantica in parallelo alla pila degli stati [ContextsensitiveAnalysisv.pdf, Slide 25, 55].

**Esempio — costruzione dell'AST:**

```yacc
Goal   : Expr           { $$ = $1; }
Expr   : Expr '+' Term  { $$ = MakeAddNode($1, $3); }
       | Expr '-' Term  { $$ = MakeSubNode($1, $3); }
       | Term            { $$ = $1; }
Term   : Term '*' Factor { $$ = MakeMulNode($1, $3); }
       | Term '/' Factor { $$ = MakeDivNode($1, $3); }
       | Factor          { $$ = $1; }
Factor : '(' Expr ')'   { $$ = $2; }
       | number          { $$ = MakeNumNode(token); }
       | ident           { $$ = MakeIdNode(token); }
```

[ContextsensitiveAnalysisv.pdf, Slide 52–53].

**Emissione di ILOC:** con `NextRegister()`, `Emit(op,r1,r2,r3)`, `EmitLoad(id,r) = loadAI rarp,@id,r` e `Emit(loadI,n,r)`, la traduzione di `a×2 + a×2×b` genera [ContextsensitiveAnalysisv.pdf, Slide 56–59]:

```
loadAI rarp, @a, r0 ;  loadI 2, r1 ;  mult r0, r1, r2 ;
loadAI rarp, @a, r3 ;  loadI 2, r4 ;  mult r3, r4, r5 ;
loadAI rarp, @b, r6 ;  mult r5, r6, r7 ;  add r2, r7, r8
```

**Reworking dell'esempio del costo di blocco (senza load tracking):** riscrivendo l'esempio di §6.4 in stile ad-hoc, la variabile `cost` diventa **globale**, accumulata a ogni riduzione [ContextsensitiveAnalysisv.pdf, slide "Reworking the Example"]:

```
Block0 → Block1 Assign     (nessuna azione: cost è già cumulativo)
Assign0 → Ident = Expr ;   cost ← cost + COST(store)
Expr0  → Expr1 + Term      cost ← cost + COST(add)
Expr0  → Expr1 - Term      cost ← cost + COST(sub)
Term0  → Term1 * Factor    cost ← cost + COST(mult)
Term0  → Term1 / Factor    cost ← cost + COST(div)
Factor → Number            cost ← cost + COST(loadI)
```

Questa versione appare più semplice della AG corrispondente, ma lascia un dettaglio mancante: **l'inizializzazione di `cost`** [ContextsensitiveAnalysisv.pdf, slide "Reworking the Example", nota "One missing detail: initializing cost"].

**Reworking dell'esempio con load tracking (la soluzione reale al problema di §6.4):**

```
0   Start → Init Block
.5  Init  → ε              cost ← 0
1   Block0 → Block1 Assign
...
```
```
12  Factor → Ident         i ← hash(Ident);
                            if (Table[i].loaded = false)
                               then {
                                  cost ← cost + COST(load)
                                  Table[i].loaded ← true
                               }
```

- **Prima che il parser possa raggiungere `Block`, deve ridurre `Init`.**
- **La riduzione di `Init` azzera `cost`.**

Si è **spezzata la produzione** per creare una riduzione intermedia — al solo scopo di agganciarvi un'azione: questo trucco è usato frequentemente [ContextsensitiveAnalysisv.pdf, slide "Reworking the Example (with load tracking)"]. Si osservi il contrasto con l'approccio ad attributi ereditati before/after di §6.4: qui basta una tabella hash globale (`Table[i].loaded`), aggiornata e consultata direttamente dalle azioni, **senza alcuna regola di copia**.

**Integrazione nel parser LR:** la pila memorizza **3 elementi per simbolo** (simbolo, attributo `$$`, stato); a ogni reduce si poppano $3\cdot|\beta|$ elementi e una grande `case` sul numero di produzione calcola `$$`; `$n` si mappa sulla locazione di pila $top - 3(n-1) - 1$. Rispetto allo skeleton LR(1) di base di §5.3 — che impila **2** elementi per simbolo (token e stato) — l'estensione per il supporto alle azioni Yacc porta questo numero a **3** (token, `$$`, stato). Costo: lieve aumento di tempo di parsing e di spazio sulla pila [ContextsensitiveAnalysisv.pdf, Slide 63–65].

**Bilancio della tecnica ad-hoc (slide "Reality"):** nella pratica **la maggior parte dei parser reali** adotta proprio questo stile ad-hoc di analisi context-sensitive [ContextsensitiveAnalysisv.pdf, slide "Reality"]. *Vantaggi:* risolve i limiti strutturali del paradigma delle grammatiche attribuite (non-località, regole di copia); è efficiente e flessibile. *Svantaggi:* il programmatore scrive il codice delle azioni con poco supporto dal formalismo, e deve gestire direttamente tutti i dettagli implementativi (pila semantica, naming degli attributi, ordine di valutazione) [ContextsensitiveAnalysisv.pdf, slide "Reality"].

### 6.7 Rappresentazioni Intermedie (cenno)

Come nota di raccordo verso il Capitolo 9, le IR si dividono in tre categorie [ContextsensitiveAnalysisv.pdf, Slide 66]:

- **Strutturali** (grafiche, es. AST) — usate spesso nei source-to-source translator, tendono a essere grandi.
- **Lineari** (pseudo-codice per macchina astratta, es. codice a tre indirizzi come ILOC, o stack-machine code) — strutture dati semplici, facili da riordinare.
- **Ibride** — combinazione di grafi e codice lineare.

L'AST **elimina i nodi non terminali** mantenendo la struttura essenziale del parse tree [ContextsensitiveAnalysisv.pdf, Slide 67].

### 6.8 Esercizio

Write a grammar that generate all binary numbers multiple than 4. Assume we are interested in knowing whether the representation contain a even number of 0 or an odd one. 
• Design a attribute grammar to compute the information we are interested in • Design a ad-hoc directed translation solving the same problem 
• Construct the evaluation for the string 110100 

#### 1. Grammar Design

A binary number is a multiple of 4 if and only if its two least significant bits are `00` (i.e., the binary string ends with the suffix `00`).

We can design a Context-Free Grammar (CFG) where:

- **\(S\)** is the start symbol (the complete binary string).
- **\(L\)** is a list of arbitrary binary digits representing the prefix before the suffix `00`.
- **\(B\)** is a single binary bit (`0` or `1`).

##### **Productions:**

1. $(S \rightarrow L\ \mathbf{0}\ \mathbf{0})$
2. $(L_0 \rightarrow L_1\ B)$
3. $(L \rightarrow \epsilon)$
4. $(B \rightarrow \mathbf{0})$
5. $(B \rightarrow \mathbf{1})$

This grammar generates all valid multiple-of-4 binary strings (e.g., `00` for 0, `100` for 4, `1000` for 8, `1100` for 12, etc.).
#### 2. Attribute Grammar (AG) Design

To compute whether the representation contains an **even** or **odd** number of `0`s, we define a synthesized attribute **`parity`** for each non-terminal, taking values in $({\text{even}, \text{odd}})$ [ContextsensitiveAnalysisv.pdf, Slide 15].

Let's define the addition operator $(\oplus)$ over this domain as:

- $(\text{even} \oplus \text{even} = \text{even})$
- $(\text{even} \oplus \text{odd} = \text{odd})$
- $(\text{odd} \oplus \text{even} = \text{odd})$
- $(\text{odd} \oplus \text{odd} = \text{even})$

##### **Attribution Rules:**

- **Rule 1:** $(S \rightarrow L\ \mathbf{0}\ \mathbf{0}) [\text{S.parity} \leftarrow \text{L.parity}]$ _(Since the two trailing `0`s always contribute an even amount to the parity $((\text{L.parity} \oplus \text{odd} \oplus \text{odd} = \text{L.parity} \oplus \text{even} = \text{L.parity}))$, the total parity of \(S) is identical to the parity of (L))_.
- **Rule 2:** $(L_0 \rightarrow L_1\ B)$ $[\text{L}_0\text{.parity} \leftarrow \text{L}_1\text{.parity} \oplus \text{B.parity}]$
- **Rule 3:** $(L \rightarrow \epsilon) \; [\text{L.parity} \leftarrow \text{even}]$
- **Rule 4:** $(B \rightarrow \mathbf{0}) \; [\text{B.parity} \leftarrow \text{odd}]$
- **Rule 5:** $(B \rightarrow \mathbf{1}) [\text{B.parity} \leftarrow \text{even}]$
#### 3. Ad-Hoc Syntax-Directed Translation (SDT)

Using **Yacc-like actions**, we can represent `even` as `0` and `odd` as `1`, performing addition modulo 2 (`% 2`) within the semantic stack [ContextsensitiveAnalysisv.pdf, Slide 29, 31, 32].

##### **Yacc Semantic Rules:**

1. $(S \rightarrow L \mathbf{0} \mathbf{0}) \; [{ \$\$ = \$1; }]$
2. $(L_0 \rightarrow L_1 B) \; [{ \$\$ = (\$1 + \$2) \pmod 2}]$
3. $(L \rightarrow \epsilon) \; [{ \$\$ = 0;}]$
4. $(B \rightarrow \mathbf{0}) \; [{ \$\$ = 1;}]$
5. $(B \rightarrow \mathbf{1}) \; [{ \$\$ = 0;}]$

#### 4. Constructing the Evaluation for the String `110100`

The suffix `00` matches the root rule $(S \rightarrow L\ \mathbf{0}\ \mathbf{0})$, while the prefix $(L)$ is evaluated on `1101`.

##### **Step-by-Step Bottom-Up Attribute Evaluation:**

1. **Prefix Initialization ($L_5 \rightarrow \epsilon$):**
    
    - $L_5.\text{parity} = \text{even}$ (value = `0`)
        
2. **First Digit ($B_1 \rightarrow \mathbf{1}$):**
    
    - $B_1.\text{parity} = \text{even}$ (value = `0`)
        
    - $L_4 \rightarrow L_5\ B_1 \Rightarrow L_4.\text{parity} = \text{even} \oplus \text{even} = \text{even}$  
        (value = `(0 + 0) % 2 = 0`)
        
3. **Second Digit ($B_2 \rightarrow \mathbf{1}$):**
    
    - $B_2.\text{parity} = \text{even}$ (value = `0`)
        
    - $L_3 \rightarrow L_4\ B_2 \Rightarrow L_3.\text{parity} = \text{even} \oplus \text{even} = \text{even}$  
        (value = `(0 + 0) % 2 = 0`)
        
4. **Third Digit ($B_3 \rightarrow \mathbf{0}$):**
    
    - $B_3.\text{parity} = \text{odd}$ (value = `1`)
        
    - $L_2 \rightarrow L_3\ B_3 \Rightarrow L_2.\text{parity} = \text{even} \oplus \text{odd} = \text{odd}$  
        (value = `(0 + 1) % 2 = 1`)
        
5. **Fourth Digit ($B_4 \rightarrow \mathbf{1}$):**
    
    - $B_4.\text{parity} = \text{even}$ (value = `0`)
        
    - $L_1 \rightarrow L_2\ B_4 \Rightarrow L_1.\text{parity} = \text{odd} \oplus \text{even} = \text{odd}$  
        (value = `(1 + 0) % 2 = 1`)
        
6. **Full Number ($S \rightarrow L_1\ \mathbf{0}\ \mathbf{0}$):**
    
    - $S.\text{parity} = L_1.\text{parity} = \mathbf{odd}$ (value = `1`)

##### **Attributed Parse Tree Visualization:**

```
               S (parity = odd, $$ = 1)
              /  |  \
             /   0   0
            /
        L1 (parity = odd, $$ = 1)
       /  \
      /    B4 (parity = even, $$ = 0) --> 1
     /
  L2 (parity = odd, $$ = 1)
 /  \
/    B3 (parity = odd, $$ = 1) --> 0
|
L3 (parity = even, $$ = 0)
| \
|  B2 (parity = even, $$ = 0) --> 1
|
L4 (parity = even, $$ = 0)
| \
|  B1 (parity = even, $$ = 0) --> 1
|
L5 (parity = even, $$ = 0) --> epsilon
```

**Conclusion:** The string `110100` contains exactly **three** `0`s. Both translation schemes correctly evaluate to `odd` (or `1`), verifying the soundness and consistency of the implementations [ContextsensitiveAnalysisv.pdf, Slide 15, 29].
<a id="cap7"></a>
<a id="cap7"></a>
## CAPITOLO 7: Ottimizzazione del Codice (Middle-End)

**Source:** _OptimizationI.pdf_

### 7.1 Ruolo dell'Ottimizzatore e Struttura a Passate

- L'ottimizzatore riceve in input l'IR generata dal Front-End, la analizza per derivare conoscenza sul comportamento a run-time (_static analysis_: data-flow analysis, pointer disambiguation, …) e la riscrive in una forma "migliore" — non necessariamente più veloce in assoluto, ma migliore secondo una metrica (velocità, dimensione del codice, spazio dati, consumo energetico) [OptimizationI.pdf].
    
- **Requisiti rigorosi per le trasformazioni:**
    
    1. **Safety:** non può alterare il risultato di un programma d'esecuzione corretto [OptimizationI.pdf].
    2. **Profitability:** deve essere applicata solo quando ci si attende un beneficio [OptimizationI.pdf].
- ⚠️ **Nota concettuale (dalla slide):** "Nothing 'optimal' about optimization" — le dimostrazioni di ottimalità per le trasformazioni assumono condizioni restrittive e non realistiche; il termine "ottimizzazione" è quindi convenzionale, non una garanzia di risultato ottimo [OptimizationI.pdf].
    
- **Trasformazioni tipiche (elenco completo dalla slide):** scoprire e propagare valori costanti; spostare una computazione in un punto meno frequentemente eseguito; specializzare una computazione in base al contesto; scoprire ed eliminare una computazione ridondante; rimuovere codice inutile o irraggiungibile [OptimizationI.pdf]. Nella sezione 7.3 si dettagliano le istanze più comuni di queste categorie (constant folding, copy propagation, LICM, DCE).
    
- **Contesto storico:** fino ai primi anni '80 l'ottimizzazione era considerata una funzionalità da aggiungere al compilatore solo dopo che le altre parti funzionavano correttamente (compilatori per il debug vs. compilatori ottimizzanti); con l'avvento dei processori RISC la richiesta di supporto da parte del compilatore è cresciuta sensibilmente [OptimizationI.pdf].
    
- **Definizione di Ridondanza:** un'espressione $x+y$ è ridondante se e solo se, lungo **ogni** cammino dall'ingresso della procedura, essa è già stata valutata e i suoi sotto-operandi ($x$ e $y$) non sono stati ridefiniti nel frattempo [OptimizationI.pdf]. Se il compilatore prova che un'espressione è ridondante, può preservare il risultato della valutazione precedente e sostituire la valutazione corrente con un riferimento. Il problema si scompone in due parti: (1) provare che $x+y$ è ridondante, o _available_; (2) riscrivere il codice per eliminare la valutazione ridondante. Una tecnica che risolve entrambe è la **value numbering** [OptimizationI.pdf].
    
- **Definizione formale (Control-Flow Graph, CFG):** un CFG è un grafo $G = (N, E)$ dove i nodi rappresentano i _basic block_ (sequenze di lunghezza massimale di codice rettilineo) e gli archi rappresentano i possibili salti/branch tra blocchi; è la base della maggior parte delle analisi e trasformazioni del compilatore [OptimizationI.pdf, slide "Terminology — Control-flow graph (CFG)"]. Esempio di riferimento usato nel resto del capitolo: $N=\{A,B,C,D,E,F,G\}$, $E=\{(A,B),(A,C),(B,G),(C,D),(C,E),(D,F),(E,F),(F,E)\}$, $|N|=7,\ |E|=8$, con il seguente contenuto concreto dei blocchi [OptimizationI.pdf, slide "Terminology — Control-flow graph (CFG)"]:
    ```
    A: m ← a + b        C: q ← a + b        E: e ← a + 17
       n ← a + b            r ← c + d            t ← c + d
    B: p ← c + d        D: e ← b + 18            u ← e + f
       r ← c + d            s ← a + b        F: v ← a + b
    G: y ← a + b            u ← e + f            w ← c + d
       z ← c + d                                 x ← e + f
    ```

> **Nota di revisione:** questo capitolo è stato confrontato con il testo integrale di `OptimizationI.pdf` (slide "This lecture begins the material from Chapter 8 of EaC"). Sono stati aggiunti il contenuto esatto dei blocchi del CFG guida (sopra), corretto un errore nell'elenco dei blocchi in cui l'espressione `a+b` viene ricalcolata (§7.4, mancava il blocco D) e aggiunta una nota sui fattori di complessità pratici della LVN (§7.2).
    
- **Nota terminologica su "scope" (slide "Scope of Optimization"):** in scanning e parsing, la parola "scope" indicava la regione di codice in cui una variabile è visibile; in ottimizzazione, "scope" indica invece la regione di codice soggetta ad analisi e trasformazione. Le due nozioni sono in qualche modo correlate, ma la connessione non è necessariamente intuitiva; scope diversi introducono sfide e opportunità diverse [OptimizationI.pdf, slide "Scope of Optimization"].
- **Classificazione degli ambiti (scope) di ottimizzazione:**
    
    1. **Locale:** opera interamente entro un singolo basic block; le proprietà del blocco permettono ottimizzazioni forti [OptimizationI.pdf].
    2. **Regionale:** opera su una regione del CFG che contiene più blocchi — loop, alberi, cammini, extended basic block — aprendo nuove opportunità rispetto al caso locale [OptimizationI.pdf].
    3. **Whole procedure / Intraprocedurale:** opera sull'intero CFG di una procedura [OptimizationI.pdf].
    4. **Whole program / Interprocedurale:** opera su tutto o parte del _call graph_ (più procedure); deve gestire il binding call/return e dei parametri [OptimizationI.pdf].

### 7.2 Tecniche di Ottimizzazione Locale

- **Local Value Numbering (LVN) — idea chiave:** assegnare un identificatore $V(e)$ a ogni identificatore, costante o espressione, con la proprietà $V(e_1) = V(e_2)$ **se e solo se** $e_1$ ed $e_2$ hanno sempre lo stesso valore per ogni possibile operando; l'hashing sui value number rende l'operazione efficiente [OptimizationI.pdf]. Algoritmo classico, attribuito a Balke (1968) o Ershov (1954) [OptimizationI.pdf].
    
- **Esempio guida — estensione del live range (register pressure):**
    
    ```iloc
    a <- b + c
    b <- a - d
    c <- b + c
    d <- a - d   // Ottimizzato tramite LVN in: d <- b
    ```
    
    |Originale|Con VN|Riscritto|
    |---|---|---|
    |`a ← b + c`|`a³ ← b¹ + c²`|`a ← b + c`|
    |`b ← a - d`|`b⁵ ← a³ - d⁴`|`b ← a - d`|
    |`c ← b + c`|`c⁶ ← b⁵ + c²`|`c ← b + c`|
    |`d ← a - d`|`d⁵ ← a³ - d⁴`|**`d ← b`**|
    
    Il codice riscritto gira più velocemente ma **estende la vitalità di $b$** fino alla riga 4 (senza l'ottimizzazione, $b$ morirebbe subito dopo la riga 3): l'aumento di pressione sui registri può indurre l'allocatore a effettuare _spill_, e poiché l'ottimizzatore non può prevedere il comportamento dell'allocatore, **assume comunque che evitare la ridondanza sia vantaggioso** [OptimizationI.pdf].
    
- **Ridondanza senza identità testuale (esempio mancante, ora integrato):**
    
    ```iloc
    a <- b * c
    d <- b
    e <- d * c
    ```
    
    Dopo la copia `d ← b`, l'espressione `e ← d * c` è **semanticamente ridondante** rispetto ad `a ← b * c` (poiché $d$ e $b$ denotano lo stesso valore), ma **non è testualmente identica** a `b * c`. Riconoscere questa ridondanza richiede di ragionare sui _valori_ piuttosto che sul testo delle espressioni — è esattamente il problema che motiva la value numbering, ed è "più complesso di quanto sembri a prima vista" [OptimizationI.pdf].
    
- **Edge case: il ruolo del naming (slide):**
    
    |Originale|Con VN|Riscritto|
    |---|---|---|
    |`a ← x + y`|`a³ ← x¹ + y²`|`a³ ← x¹ + y²`|
    |`b ← x + y`|`b³ ← x¹ + y²`|`b³ ← a³`|
    |`a ← 17`|`a⁴ ← 17`|`a⁴ ← 17`|
    |`c ← x + y`|`c³ ← x¹ + y²`|`c³ ← a³` **(oops!)**|
    
    L'ultima riscrittura è **sbagliata**: `a` è stata ridefinita (`a⁴ ← 17`) prima della terza occorrenza di `x+y`, quindi `c³ ← a³` referenzia il valore sbagliato. Opzioni di correzione: (a) mantenere una mappatura esplicita VN→nome corrente (usare `c³ ← b³`); oppure (b) **renaming alla SSA**, assegnando un nome unico a ogni valore ($a_0^3, b_0^3, a_1^4, c_0^3$, …), dopo il quale la riscrittura funziona correttamente e $a_0^3$ risulta "disponibile" senza ambiguità [OptimizationI.pdf]. Una mappatura pratica per riconciliare i nomi SSA con quelli originali: $a_1{\to}a,\ b_0{\to}b,\ c_0{\to}c,\ a_0{\to}t$ [OptimizationI.pdf].
    
    Con gli **assegnamenti indiretti** (`*p ← 0`) il compilatore non isola una singola locazione di memoria (**riferimento ambiguo**): serve _pointer analysis_ per restringere l'insieme di variabili a cui `p` può riferirsi, altrimenti bisogna invalidare in modo conservativo [OptimizationI.pdf].
    
- **Estensioni semplici alla Value Numbering [OptimizationI.pdf]:**
    
    - _Operazioni commutative:_ $a \times b$ e $b \times a$ devono ricevere lo stesso value number — si impone un **ordine canonico** sugli operandi.
    - _Constant folding:_ si aggiunge un bit che registra quando un valore è costante; si valutano le costanti a tempo di compilazione; si sostituisce l'operazione con il caricamento del valore immediato.
    - _Identità algebriche:_ $x+0,\ x-0,\ x\times1,\ x\div1,\ x-x,\ x\times0,\ x\div x,\ x\lor0,\ x\land x,\ \max(x,x),\ \min(y,y), \dots$ — vanno organizzate in un albero di decisione specifico per operatore; il risultato viene sostituito col VN dell'input.
- **Algoritmo LVN completo (recap, slide):** per ogni $T_i \leftarrow L_i\ Op_i\ R_i$, $i=0,\dots,n-1$:
    
    1. Ottieni i value number $V_1, V_2$ di $L_i, R_i$ da lookup in hash;
    2. Se $L_i$ e $R_i$ sono entrambi costanti → **constant folding**: valuta $L_i\ Op_i\ R_i$, assegnalo a $T_i$, marca $T_i$ come costante;
    3. Se $L_i\ Op_i\ R_i$ combacia con un'**identità algebrica** → sostituisci con una copia/assegnamento;
    4. Se $Op_i$ commuta e $V_1 > V_2$ → scambia $V_1$ e $V_2$ (**commutatività**);
    5. Costruisci la chiave hash $\langle V_1, Op_i, V_2\rangle$: se già presente in tabella → sostituisci l'operazione con una copia in $T_i$ e marca $T_i$ col VN esistente; altrimenti → inserisci un nuovo VN in tabella per quella chiave e marca $T_i$ con esso [OptimizationI.pdf].
    
    Se l'hashing si comporta bene, l'algoritmo gira in **tempo lineare** [OptimizationI.pdf].

- **Fattori pratici di complessità e velocità (slide "Complexity & Speed Issues"):** anche a parità di algoritmo, l'efficienza reale dipende da alcune scelte implementative: il recupero dei value number degli operandi può avvenire per ricerca lineare o tramite hash; il lookup della chiave $\langle op, VN(o_1), VN(o_2)\rangle$ può a sua volta essere lineare o hashed; il *copy folding* richiede di propagare il VN del risultato; le operazioni commutative richiedono di scegliere tra un doppio hashing (uno per ciascun ordine degli operandi) oppure l'ordinamento preventivo degli operandi (soluzione adottata in §7.2, passo 4) [OptimizationI.pdf, slide "Local Value Numbering — Complexity & Speed Issues"].
    

### 7.3 Ottimizzazioni Tipiche

- **Constant Folding:** valuta a tempo di compilazione operazioni tra costanti note (es. `2 + 3` → `5`) [OptimizationI.pdf].
- **Copy Propagation:** sostituisce gli usi successivi di `x` con `y`, dato un assegnamento di copia `x <- y`, eliminando l'istruzione di copia.
- **Loop-Invariant Code Motion (LICM):** sposta fuori dal ciclo (nel _pre-header_) computazioni i cui operandi non cambiano tra le iterazioni.
- **Dead Code Elimination (DCE):** elimina istruzioni che calcolano valori mai usati lungo alcun cammino successivo del CFG.

### 7.4 Oltre il Blocco: EBB e Loop Unrolling

- **CFG d'esempio:** blocchi $A\dots G$ con $N=\{A,B,C,D,E,F,G\}$, $E=\{(A,B),(A,C),(B,G),(C,D),(C,E),(D,F),(E,F),(F,E)\}$, $|N|=7$, $|E|=8$, con il contenuto concreto riportato in §7.1 [OptimizationI.pdf, slide "Local Value Numbering"].
    > **⚠️ Correzione (errore nella stesura precedente):** applicata un blocco alla volta, la LVN trova **solo due** ridondanze, entrambe *interne al proprio blocco*: `n←a+b` in A (duplica `m←a+b` nello stesso blocco) e `r←c+d` in B (duplica `p←c+d` nello stesso blocco). **Tutto il resto è una "missed opportunity"**, non una ridondanza trovata da LVN: in C, `q←a+b` e `r←c+d` non sono ridondanti *tra loro* (sono espressioni diverse), ma duplicano rispettivamente `a+b` calcolato in A e `c+d` calcolato in B — LVN non se ne accorge perché il duplicato si trova in un blocco diverso. Allo stesso modo sono "perse" da LVN: `s←a+b` in D (duplica A), `t←c+d` in E (duplica B), `v,w,x` in F (duplicano A/B/D-E), `y,z` in G (duplicano A/B). La slide etichetta esplicitamente questa situazione "missed opportunities (need stronger methods)" [OptimizationI.pdf, slide "Local Value Numbering"] — è esattamente il limite che motiva l'introduzione della Superlocal Value Numbering (EBB) discussa di seguito.
    
- **Extended Basic Block (EBB):** insieme massimale di blocchi $B_1,\dots,B_n$ dove ogni $B_i$ ($i>1$) ha **esattamente un predecessore, interno all'EBB stesso** [OptimizationI.pdf]. Nell'esempio ${A,B,C,D,E}$ è un EBB con 3 cammini: $(A,B)$, $(A,C,D)$, $(A,C,E)$; ${F}$ e ${G}$ sono EBB degeneri [OptimizationI.pdf].
    
- **Superlocal Value Numbering:** applica LVN ai cammini dell'EBB, riusando i risultati degli antenati per evitare di ri-analizzare $A$ e $C$ (non aiuta però su $F$ o $G$, che non fanno parte dell'EBB) [OptimizationI.pdf]. Per efficienza si usa una **hash table scoped**, con la sequenza di scope $A,\ AB,\ A,\ AC,\ ACD,\ AC,\ ACE,\ F,\ G$: la tabella di $A$ inizializza quelle di $B$ e $C$, evitando duplicazioni [OptimizationI.pdf]. Serve inoltre una mappatura **VN→nome** per gestire i **kill** (ridefinizioni di un nome): la mappa va ripristinata all'uscita dallo scope — complicazione, non costo asintotico aggiuntivo. Per semplificare il problema conviene usare nomi unici per ogni definizione, cioè lo **spazio dei nomi SSA** [OptimizationI.pdf].
    
- **Loop unrolling:**
    
    1. _Completo_ (bounds fissi, poche iterazioni): il loop diventa codice rettilineo, eliminando somme/test/branch — sempre sicuro se i bound sono corretti [OptimizationI.pdf].
    2. _Per fattore_ (es. 4): `do i=1 to 100 by 4: a(i); a(i+1); a(i+2); a(i+3) end` — riduce test e branch del 25% con minor crescita di codice rispetto all'unrolling completo [OptimizationI.pdf].
    3. _Bounds ignoti — guard loop:_ loop principale `do while (i+3 < n) …; i ← i+4 end` seguito da un loop di coda `do while (i < n) …; i ← i+1 end`, generalizzabile a bound e fattori arbitrari [OptimizationI.pdf].
    4. _Unroll-and-rename:_ per `a(i) = a(i) + b(i) + b(i-1)`, l'unroll by 2 con renaming (`t1 ← b(i+1)` al posto di `t1 ← t2`) elimina le copie di fine iterazione, che erano solo un artefatto di naming [OptimizationI.pdf].
    
    ⚠️ **Rischi:** crescita del codice; maggiore domanda di registri; se gli spill risultanti generano più traffico di memoria del beneficio ottenuto, l'ottimizzazione è controproducente [OptimizationI.pdf].
<a id="cap8"></a>
## CAPITOLO 8: Il Framework Dataflow
**Sources:** *Data-FlowFirst.pdf / Data-Flow2.pdf*

### 8.1 Fondamenti Matematici dell'Analisi del Flusso di Dati
*   L'analisi dataflow raccoglie informazioni statiche sul comportamento a runtime del programma risolvendo sistemi di equazioni ricorsive sul Control Flow Graph (CFG) [Data-FlowFirst.pdf, Slide 12; Data-Flow2.pdf, Slide 12].
*   **Teoria dei Reticoli (Lattices):** Ciascuna analisi modella le proprietà come elementi di un reticolo parzialmente ordinato (CPO).
    *   L'operatore di combinazione dei rami è il **Join Semilattice ($\sqcup$)** o il **Meet Semilattice ($\sqcap$)**, che definisce il limite superiore/inferiore comune [Data-Flow2.pdf, Slide 12, 43].
    *   **Teorema di Kleene (Fixed Point):** Garantisce che, se la funzione di trasferimento associata alle equazioni di flusso è monotona su un dominio finito con elementi di minimo e massimo ($\perp$ e $\top$), l'algoritmo iterativo convergerà necessariamente e in modo stabile verso un unico punto fisso stabile [Data-Flow2.pdf, Slide 12, 43]. Il fondamento formale completo di questa affermazione — dominio CPO, ordine componente per componente, monotonia, esempio numerico d'iterazione — è sviluppato per intero al §8.1bis qui sotto.

### 8.1bis Fondamento Formale del Punto Fisso: dal CFG al Dominio CPO
**Sources:** *Data-FlowFirst.pdf / Data-Flow2.pdf* (sezione verificata riga per riga contro il testo integrale delle due PDF fornite in sessione)

Questa sezione integra il paragrafo precedente con il trattamento formale completo, presente nelle slide, della costruzione del dominio su cui si risolve il sistema di equazioni dataflow, usando la Liveness Analysis come esempio guida end-to-end.

*   **Cos'è la dataflow analysis (slide "What is Dataflow Analysis: general idea"):** una tecnica di analisi statica che traccia come l'informazione fluisce nel programma; opera su una rappresentazione a grafo (tipicamente il CFG); calcola proprietà del programma (live variables, constant propagation, reaching definitions); associa informazione a nodi (punti di programma) o ad archi; ha due direzioni principali — forward (l'informazione fluisce nella direzione d'esecuzione) e backward (l'informazione risale la direzione d'esecuzione). Analisi diverse condividono lo stesso framework computazionale sottostante.
*   **Struttura comune (slide "Common Structure of Dataflow Analyses"):**
    *   *Equazioni di flusso:* per ogni nodo, $IN[n]$ = merge dell'informazione dei predecessori (o successori); $OUT[n]$ = funzione di trasferimento applicata a $IN[n]$.
    *   *Funzione di trasferimento:* modella l'effetto di ogni statement, spesso espressa via gen/kill.
    *   *Operatore di merge:* combina l'informazione da più cammini — $\cup$ (unione) per le analisi *may*; $\cap$ (intersezione) per le analisi *must*.
    *   *Computazione:* soluzione iterativa fino al punto fisso.
*   **May vs Must (slide):** *May* (possibile) — la proprietà può valere su alcuni cammini d'esecuzione (es. reaching definitions, live variables). *Must* (definitiva) — la proprietà vale su tutti i cammini (es. available expressions, definite assignment).
*   **Control Flow Graph (slide):** i comandi del programma sono codificati da nodi in un CFG; se un comando $S$ può essere direttamente seguito da un comando $T$, il CFG deve includere un arco diretto dal nodo che codifica $S$ al nodo che codifica $T$. Esempio guida ripreso nell'intero capitolo (fattoriale-like): `1: input n; 2: m:=1; 3: while n>1 do 4: m:=m*n; 5: n:=n-1; 6: output m;`.

#### Liveness: dalla definizione informale alla formalizzazione
*   **Motivazione (slide "Liveness or Live Variables Analysis"):** il codice sorgente va tradotto in una IR (codice a tre indirizzi) con un numero potenzialmente illimitato di registri, ma il programma verrà eseguito su un processore con un numero finito (e piccolo) di registri fisici. Due variabili $a$ e $b$ possono condividere lo stesso registro fisico quando non sono mai "vive" simultaneamente.
*   **Definizione (slide "Live Variables Analysis"):** una variabile $X$ è viva all'uscita di un comando $C$ se memorizza un valore che sarà effettivamente usato in futuro come R-value, senza un uso precedente come L-value. Una variabile non viva all'uscita di $C$ è detta **morta** (informazione usabile per la dead code elimination). **Questa è una proprietà indecidibile** in generale — da qui la necessità di un'approssimazione statica conservativa.
*   **Esempio guida completo (slide, sul CFG del fattoriale):** 
	```text
	1) a := 0;
	
	2) b := a + 1;
	
	3) c := c + b;
	
	4) a := b * 2;
	
	5) a < N;
	
	6) return c;
	```
  
  si traccia a mano il live range di `b` — l'ultimo uso di `b` come r-value è nel comando 4; `b` è quindi vivo lungo l'arco $3\to4$; il comando 3 non assegna `b`, quindi `b` è vivo anche lungo $2\to3$; il comando 2 assegna `b`, quindi il valore di `b` lungo $1\to2$ non sarà più usato. Il live range di `b` è dunque $\{2\to3,\ 3\to4\}$. Analogamente si traccia `a` (vivo lungo $4\to5$, $5\to2$, $1\to2$; morto lungo $2\to3$, $3\to4$) e `c` (vivo lungo **ogni** arco: il compilatore può dedurne che, se `c` è locale, viene usata senza inizializzazione precedente — un warning). **Conseguenza pratica:** poiché `a` e `b` non sono mai vivi simultaneamente lungo lo stesso arco, **due registri bastano**: si può sostituire il nome `a` e il nome `b` con un'unica variabile `ab`, ottenendo un risparmio di un registro senza alterare la semantica.
*   **Notazione formale su predecessori/successori (slide "We need a way to compute live variables"):** $pre[n]$ e $post[n]$ denotano rispettivamente i nodi predecessori e successori di $n$. $def[n]$ = variabili definite (assegnate come L-value) nel nodo $n$; $use[n]$ = variabili usate (lette come R-value) nel nodo $n$. Esempio dalla slide: $def[3]=\{c\}$, $use[3]=\{b,c\}$, $def[5]=\emptyset$, $use[5]=\{a\}$.
*   **Formalizzazione della proprietà (slide "Formalization of the property"):** una variabile $x$ è viva lungo un arco $e\to f$ se esiste un cammino di esecuzione reale $P$ da $e$ a un nodo $n$ tale che: (1) $e\to f$ è il primo arco di $P$; (2) $x\in use[n]$; (3) per ogni nodo $n'\neq e,n$ in $P$, $x\notin def[n']$. Una variabile $x$ è **live-out** in $n$ se è viva lungo almeno un arco uscente da $n$; è **live-in** in $n$ se è viva lungo un qualsiasi arco entrante in $n$.
*   **Le tre regole della soluzione approssimata (slide "Computing an approximation of Liveness property" / "Computing Liveness"):**
    1.  Se $x\in use[n]$ allora $x$ è live-in in $n$: $in[n]\supseteq use[n]$.
    2.  Se $x$ è live-out in $n$ e $x\notin def[n]$, allora $x$ è anche live-in in $n$: $in[n]\supseteq out[n]-def[n]$.
    3.  Se $x$ è live-in in un nodo $m$, allora $x$ è live-out per ogni nodo $n$ tale che $m\in post[n]$ (per definizione — la slide lo osserva come "clearly correct by definition").
*   **Le equazioni dataflow risultanti (slide "Dataflow Equations"):**
    $$in[n] = use[n] \cup (out[n] - def[n]) \qquad out[n] = \bigcup_{m\in post[n]} in[m]$$
*   **Correttezza dell'analisi (slide "Correctness of the analysis of Liveness"):** questa definizione è **corretta** (sound): se $x$ è concretamente live-in (live-out) in $n$, allora l'analisi statica lo rileva, cioè
    $$in[n]\supseteq live\text{-}in[n] \qquad out[n]\supseteq live\text{-}out[n]$$
    nessuna variabile effettivamente viva viene mai trascurata. La dimostrazione ricalca lo schema di correttezza usato dal Dragon Book per Available Expressions (slide "Correctness in Dragon Book", riquadro "Why the Available-Expressions Algorithm Works"): l'unica ragione per cui un'espressione $x+y$ risulta non disponibile in un punto è (1) uccisa in un blocco perché $x$ o $y$ vengono ridefinite senza un successivo ricalcolo di $x+y$ — nel qual caso, la prima volta che si applica la funzione di trasferimento, $x+y$ viene rimossa da $OUT[B]$ — oppure (2) mai calcolata lungo un cammino, nel qual caso, per induzione sulla lunghezza del cammino, $x+y$ risulta rimossa da tutti gli $IN$/$OUT$ lungo quel cammino. Poiché l'intersezione è l'operatore di meet per questa classe di analisi, ogni ragione di non-disponibilità si propaga in avanti lungo **tutti** i cammini possibili. Lo stesso argomento, dualizzato (unione al posto di intersezione, propagazione all'indietro), garantisce la correttezza della Liveness.
*   **⚠️ Approssimazione — cammini infeasible (slide "Computing Liveness — Liveness analysis is approximate"):** l'analisi assume che **ogni cammino del CFG sia un cammino d'esecuzione fattibile**, ipotesi in generale falsa. Esempio esplicito delle slide: nel CFG con `a:=b*b; c:=a+b; if (c>=b) then return c else return a`, l'analisi determina che `a` è live-in nel nodo 5 (`return a`), quindi live-out nel nodo 3 — ma nessun cammino reale da 3 a 5 esiste, poiché la condizione `b+b*b<b` è sempre falsa; dunque `a` non è realmente viva all'uscita di 3. L'analisi resta comunque **sound** (sovrastima, mai sottostima), al prezzo di un'imprecisione accettata in cambio della decidibilità del problema.

#### La teoria del punto fisso: da "come risolvere le equazioni" a Kleene
*   **Il problema aperto (slide "How can we compute a solution to 1 and 2?"):** bisogna calcolare, per ogni nodo, gli insiemi $in[n]$/$out[n]$ che soddisfano contemporaneamente le due equazioni — un **punto fisso**. Ma come garantire che tali punti fissi esistano? *Dipende dal dominio e dalla funzione!*
*   **Cosa serve (slide "What do we need?"):** occorre fissare (1) un dominio che sia un **CPO continuo** $(D,\sqsubseteq)$, e (2) una funzione $f:D\to D$; a quel punto si può applicare il **Teorema di Kleene**.
*   **Caso particolare — domini finiti (slide "On finite sets"):**
    *   Se un poset $(D,\sqsubseteq)$ è **finito**, allora è automaticamente un CPO.
    *   Se un poset $(D,\sqsubseteq)$ è finito **e** $f:D\to D$ è **monotona**, allora $f$ è automaticamente **continua**.

    Questo è precisamente il caso della liveness analysis: il dominio è costruito su un insieme finito di variabili e un CFG con un numero finito di nodi, quindi basta dimostrare la monotonia della funzione di trasferimento per ottenere gratuitamente la continuità e, con essa, l'esistenza del punto fisso per Kleene.
*   **Costruzione esplicita del dominio (slide "Which is our domain?"):**
    *   Sia **Vars** l'insieme finito delle variabili che occorrono nel programma $P$ da analizzare; tutti i sottoinsiemi possibili sono $\mathcal{P}(\text{Vars})$.
    *   Per ogni nodo servono un insieme $in$ e un insieme $out$: la coppia vive in $\mathcal{P}(\text{Vars})\times\mathcal{P}(\text{Vars})$.
    *   Se il CFG ha $N$ nodi, il dominio complessivo è
        $$\big(\mathcal{P}(\text{Vars})\times\mathcal{P}(\text{Vars})\big)^N$$
        cioè $N$-uple di coppie di sottoinsiemi di Vars.
    *   **L'ordine** $\sqsubseteq^{2N}$ è definito componente per componente:
        $$\langle in_1^1,out_1^1,\dots,in_N^1,out_N^1\rangle \sqsubseteq^{2N} \langle in_1^2,out_1^2,\dots,in_N^2,out_N^2\rangle \iff \forall i,\ in_i^1\subseteq in_i^2 \ \text{e}\ out_i^1\subseteq out_i^2$$
*   **Esempio concreto del reticolo (slide "Example"):** con $\text{Vars}=\{a,b\}$, $N=2$ (CFG a due nodi `1: a:=0; 2: b:=a+1;`), il dominio $\langle(\mathcal{P}(\text{Vars})\times\mathcal{P}(\text{Vars}))^2,\sqsubseteq^4\rangle$ è un reticolo finito: il diagramma di Hasse della slide mostra il **bottom** $\langle\emptyset\emptyset\emptyset\emptyset\rangle$ risalendo attraverso i singoletti (es. $\langle\{a\}\emptyset\emptyset\emptyset\rangle$), le coppie, fino al **top** $\langle\{a,b\}\{a,b\}\{a,b\}\{a,b\}\rangle$. Essendo finito, è automaticamente un **CPO con bottom** (il bottom essendo la $N$-upla di coppie di insiemi vuoti).
*   **La funzione Live come trasformatore sul dominio (slide "Which is our function?"):** si definisce la mappa
    $$\text{Live}: \big(\mathcal{P}(\text{Vars})\times\mathcal{P}(\text{Vars})\big)^N \to \big(\mathcal{P}(\text{Vars})\times\mathcal{P}(\text{Vars})\big)^N$$
    $$\text{Live}(\langle in_1,out_1,\dots,in_N,out_N\rangle) = \Big\langle use[1]\cup(out_1-def[1]),\ \bigcup_{m\in post[1]} in_m,\ \dots,\ use[N]\cup(out_N-def[N]),\ \bigcup_{m\in post[N]} in_m \Big\rangle$$
    cioè l'applicazione simultanea delle due equazioni di flusso a ogni nodo, vista come **un'unica funzione** sull'intero dominio prodotto.
*   **Esempio numerico di iterazione (slide, sul CFG `1: a:=0; 2: b:=a+1;` con $def(1)=\{a\}$, $use(1)=\emptyset$, $def(2)=\{b\}$, $use(2)=\{a\}$):**
    $$\text{Live}(\langle\emptyset\emptyset\emptyset\emptyset\rangle) = \langle\emptyset\emptyset\{a\}\emptyset\rangle$$
    $$\text{Live}(\langle\emptyset\emptyset\{a\}\emptyset\rangle) = \langle\emptyset\{a\}\{a\}\emptyset\rangle$$
    $$\text{Live}(\langle\emptyset\{a\}\{a\}\emptyset\rangle) = \langle\emptyset\{a\}\{a\}\emptyset\rangle \quad \text{(punto fisso raggiunto)}$$
    Si osservi che, partendo dal bottom $\langle\emptyset\emptyset\emptyset\emptyset\rangle$ e iterando Live ripetutamente, la successione è **crescente** nell'ordine $\sqsubseteq^{2N}$ e converge in un numero finito di passi — l'istanza concreta del Teorema di Kleene applicato a questo dominio.
*   **Monotonia della funzione Live (slide "Note that Live is monotone!"):** la funzione Live è costruita interamente da unioni, differenze insiemistiche rispetto a insiemi *fissi* ($def,use$) e unioni su insiemi di indici fissi ($post[n]$) — operazioni che preservano l'inclusione insiemistica componente per componente. Di conseguenza Live è **monotona** rispetto a $\sqsubseteq^{2N}$; essendo il dominio finito, per la proprietà enunciata sopra ("On finite sets") Live è automaticamente **continua**, e il Teorema di Kleene garantisce l'esistenza del **minimo punto fisso**, calcolabile iterando Live a partire dal bottom fino a convergenza — esattamente l'algoritmo iterativo presentato nell'esercizio di liveness già svolto al §8.5 (3 sweep backward fino alla convergenza sul CFG del fattoriale a 6 nodi).

**Collegamento con il resto del Capitolo 8:** questo apparato formale — dominio $\mathcal{P}(\text{Vars})^{2N}$, ordine componente per componente, funzione di trasferimento monotona su dominio finito, convergenza per Teorema di Kleene — è esattamente il fondamento matematico invocato in modo sintetico al §8.1 ("Teorema di Kleene (Fixed Point)"): ogni istanza delle quattro analisi del catalogo di §8.2 (Reaching Definitions, Available Expressions, Live Variables, Very Busy Expressions) è un'istanza dello stesso schema — cambiano soltanto l'operatore di merge ($\cup$ per le *may*, $\cap$ per le *must*) e la direzione (forward/backward), ma la garanzia di terminazione e correttezza discende sempre dalla stessa coppia di fatti: dominio finito + funzione di trasferimento monotona.

### 8.2 Classificazione del Framework Unificato
Ciascuna analisi del flusso di dati viene categorizzata in modo univoco sulla base di due caratteristiche geometriche e insiemistiche fondamentali [Data-Flow2.pdf, Slide 18, 12.1]:

1.  **Direzione (Direction):**
    *   **Forward (In avanti):** L'informazione si propaga seguendo la direzione d'esecuzione del codice (dagli ingressi dei blocchi verso le uscite) [Data-Flow2.pdf, Slide 18, 12.1].
    *   **Backward (All'indietro):** L'informazione risale la corrente d'esecuzione, partendo dall'uscita del programma verso i blocchi d'ingresso [Data-Flow2.pdf, Slide 18, 12.1].
2.  **Operatore di Merge (Combinazione):**
    *   **May (Possibile / Unione $\cup$):** La proprietà vale se è vera lungo *almeno uno* dei cammini che convergono nel punto. Si associa all'operazione insiemistica di unione [Data-Flow2.pdf, Slide 18, 12.1].
    *   **Must (Definito / Intersezione $\cap$):** La proprietà deve valere *su tutti* i cammini d'esecuzione che giungono al punto. Si associa all'operazione di intersezione [Data-Flow2.pdf, Slide 18, 12.1].

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
		* $$in[n] = use[n] \cup (out[n] \setminus def[n])$$
		- $$out[n] = \bigcup_{m \in post[n]} in[m]$$
	- ![[Pasted image 20260907191733.png|515]] 
	  
	  [Data-FlowFirst.pdf, Slide 12; Data-Flow2.pdf, Slide 12, 11.1].
*   **Reaching Definitions:**
    * *Classificazione:* Forward + May (Unione) [Data-Flow2.pdf, Slide 18, 12.1].
    * *Scopo:* Trovare quali definizioni (assegnamenti a variabili) attive arrivano a un dato punto d'esecuzione senza essere sovrascritte.
	* *Equazioni di flusso:*
		* $$kill_{RD}[p] = \{(x,q) \mid q \in Points \land \{x\} = def[q]\} \quad \text{se } \{x\} = def[p]$$
		* $$gen_{RD}[p] = \{(x,p)\} \quad \text{se } \{x\} = def[p]$$
		- $$RD_{entry}(p) = \begin{cases} \iota = \{(x,?) \;|\; x \in Vars \} & \text{se } p \text{ è il blocco iniziale} \\ \bigcup_{q \in pre[p]} RD_{exit}(q) & \text{altrimenti} \end{cases}$$
		- $$RD_{exit}(p) = (RD_{entry}(p) \setminus kill_{RD}[p]) \cup gen_{RD}[p]$$
	- ![[Pasted image 20260907191530.png|506]]
	  
*   **Available Expressions (AE):**
	*   *Classificazione:* Forward + Must (Intersezione) [Data-Flow2.pdf, Slide 18, 44, 12.1].
	*   *Scopo:* Identificare se un'espressione matematica è già stata calcolata lungo tutti i percorsi precedenti ed è ancora valida (consente l'eliminazione delle sottoespressioni comuni - CSE) [Data-Flow2.pdf, Slide 18, 44, 12.1].
	*   *Equazioni:*
	* Un'espressione $e \in E$ viene uccisa nel blocco $p$ se una qualsiasi delle sue variabili componenti viene modificata ( ridefinita tramite assegnamento) dal comando in $p$
	  $$kill_{AE}([x := e']_p) = \{ e \in E \mid x \in vars(e) \}$$
	- An expression $e \in E$ is generated in a program point $p$ ($e \in gen_{AE}(p)$) if e is evaluated in $p$ and no variable occurring in $e$ is modified in $p$.
	  $$gen_{AE}([x := e]_p) = \{e\} \quad \text{se } x \notin vars(e)$$
	  $$gen_{AE}([x := e]_p) = \emptyset \quad \text{se } x \in vars(e)$$
	  $$gen_{AE}([e_1 > e_2]_p) = expr(\{e_1, e_2\})$$
	  _dove_ $expr(S)$ _estrae solo gli elementi di_ $S$ _che sono effettivamente sottoespressioni_
	- **Ingresso del blocco (**$AE_{entry}[p]$**):** $$AE_{entry}[p] = \begin{cases} \emptyset & \text{se } p \text{ è il blocco iniziale} \\ \bigcap_{q \in pre[p]} AE_{exit}[q] & \text{altrimenti} \end{cases}$$
	- **Uscita del blocco (**$AE_{exit}[p]$**):** $$AE_{exit}[p] = (AE_{entry}[p] \setminus kill_{AE}[p]) \cup gen_{AE}[p]$$
	- ![[Pasted image 20260907213902.png|473]]
	  
	  [Data-Flow2.pdf, Slide 43].
*   **Very Busy Expressions (VBE):**
    *   *Classificazione:* Backward + Must (Intersezione) [Data-Flow2.pdf, Slide 18, 44, 45, 12.1].
    *   *Scopo:* Individuare se un'espressione verrà sicuramente calcolata in futuro a prescindere dal ramo d'esecuzione scelto, consentendo di anticiparne il calcolo (expression hoisting) per risparmiare spazio [Data-Flow2.pdf, Slide 44, 45].
    *   *Equazioni di flusso:*
        - **All'uscita del blocco (**$VB_{exit}[p]$**):** $$VB_{exit}[p] = \begin{cases} \emptyset & \text{se } p \text{ è un nodo finale} \\ \bigcap_{q \in post[p]} VB_{entry}[q] & \text{altrimenti} \end{cases}$$
        - **All'ingresso del blocco (**$VB_{entry}[p]$**):** $$VB_{entry}[p] = (VB_{exit}[p] \setminus kill_{VB}[p]) \cup gen_{VB}[p]$$
       - $kill_{VB}[p]$**:** Un'espressione viene uccisa se una qualsiasi delle sue variabili componenti viene definita (ridefinita) in $p$. L'insieme di uccisione è identico a quello delle Available Expressions ($kill_{VB} = kill_{AE}$)
	   - $gen_{VB}[p]$**:** Un'espressione viene generata se viene valutata in $p$.
	     **Differenza fondamentale con AE (**$gen_{VB} \neq gen_{AE}$**):** In un assegnamento come `x := x + 1`, l'espressione `x + 1` viene considerata generata per la VBE (poiché deve essere fisicamente valutata a runtime). Nelle Available Expressions, invece, l'assegnamento alla variabile `x` (che fa parte dell'espressione stessa) ne annulla la generazione a causa del _kill_ simultaneo, rendendola non disponibile.
   - 
     
     ![[Pasted image 20260908020940.png|439]]

### 8.4 La Regola d'Oro dell'Inizializzazione
La stabilità e la correttezza matematica del calcolo del punto fisso dipendono strettamente dall'inizializzazione corretta dei set all'inizio delle iterazioni [Data-Flow2.pdf, Slide 22, 12.2]:
*   **Nei sistemi May (unione $\cup$):** Tutti i set `IN` e `OUT` (ad eccezione dei blocchi di ingresso) devono essere inizializzati al **set vuoto ($\emptyset$)**. In questo modo, l'algoritmo risale dal basso verso l'alto (least fixed point) [Data-Flow2.pdf, Slide 22, 12.2].
*   **Nei sistemi Must (intersezione $\cap$):** Tutti i set devono essere inizializzati al **set universale ($\mathcal{U}$)**. Se si inizializzasse erroneamente al set vuoto, l'operazione di intersezione iniziale con l'insieme vuoto continuerebbe a produrre il vuoto ad ogni passo ("avvelenamento da intersezione"), facendo collassare l'intero sistema a $\emptyset$ [Data-Flow2.pdf, Slide 22, 12.2].
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

Programma fattoriale: `1: input n; 2: m := 1; 3: n > 1 ?; 4: m := m*n; 5: n := n-1; 6: output m`, archi $1 \to 2 \to 3$, $3 \to 4 \to 5 \to 3$ (back-edge), $3 \to 6$.

**gen/kill (slide, corretto):**

|$p$|$kill_{RD}[p]$|$gen_{RD}[p]$|
|---|---|---|
|1|$\emptyset$|$\emptyset$|
|2|(m,?)(m,2)(m,4)|(m,2)|
|3|$\emptyset$|$\emptyset$|
|4|(m,?)(m,2)(m,4)|(m,4)|
|5|(n,?)(n,5)|(n,5)|
|6|$\emptyset$|$\emptyset$|

_Nota:_ il nodo 1 (`input n;`) **non** compare come punto di generazione/kill nella specifica delle slide: la definizione di $n$ è tracciata solo tramite il valore di boundary $\iota={(x,?)\mid x\in Vars}$ e la successiva ridefinizione al nodo 5. Inoltre, per costruzione, $kill_{RD}[p]={(x,q)\mid q\in Points \wedge {x}=def[q]}$ quando ${x}=def[p]$: cioè il kill di una variabile coincide _sempre_ con l'intero insieme delle coppie $(x,q)$ per **tutti** i punti in cui quella variabile è definita nel programma (non solo il punto corrente) — per questo $kill_{RD}(2)=kill_{RD}(4)={(m,?),(m,2),(m,4)}$: entrambi i nodi che assegnano `m` uccidono l'intero insieme delle definizioni di `m`.

**Equazioni (forward, may):** $RDentry(p) = \iota = {(x,?) \mid x \in Vars}$ se $p$ è iniziale, altrimenti $\bigcup {RDexit(q) \mid q \in pre[p]}$; $\quad RDexit(p) = (RDentry(p) - kill_{RD}[p]) \cup gen_{RD}[p]$.

**Iterazione 1 (slide):**

```
RDentry(1)={(n,?),(m,?)}   RDexit(1)={(n,?),(m,?)}     ← invariato: kill(1)=gen(1)=∅
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

La slide segnala esplicitamente **"fix point!"** subito dopo questa seconda iterazione (nessun ulteriore passo esplicito è mostrato): confrontando i valori con quelli che si otterrebbero ricalcolando le equazioni una terza volta, nessun insieme cambia ⇒ **punto fisso raggiunto in 2 iterazioni** (least fixed point, partenza da $\bot=\emptyset$ per tutti gli insiemi tranne il nodo iniziale).

**Lettura (slide):** in $RDentry(3)$ coesistono $(m,2)$ e $(m,4)$ ⇒ $m$ **non è costante** nel loop; $(n,?)$ non muore mai ⇒ $n$ _potrebbe_ essere usato non inizializzato (warning). **Applicazione — loop-invariant code motion:** se per ogni $y \in vars(exp)$ le definizioni che raggiungono l'entry del loop coincidono con quelle che raggiungono il punto $n$, allora `x := exp` può essere issato **prima** del loop (slide: `x = y+z` con `y:=3; z:=5` fuori dal for ⇒ hoisted).
<a id="cap9"></a>
## CAPITOLO 9: Astrazione delle Procedure e Gestione della Memoria
**Source:** *TheProcedureAbstraction.pdf*

### 9.1 Le Tre Astrazioni delle Procedure
La procedura è l'astrazione fondamentale per rendere gestibili e modulari i software di grandi dimensioni [TheProcedureAbstraction.pdf, Slide 152]. Offre tre astrazioni principali:
1.  **Control Abstraction**:** Consente un unico punto di ingresso e uscita ordinato, con passaggio controllato dei parametri e gestione del flusso di ritorno [TheProcedureAbstraction.pdf, Slide 154, 155].
2.  **Clean Name Space:** Ogni procedura eredita uno spazio di nomi isolato. Le variabili locali sono visibili solo all'interno del proprio blocco d'esecuzione, e lo *shadowing* permette di oscurare variabili omonime dichiarate negli scope esterni [TheProcedureAbstraction.pdf, Slide 154].
3.  **External Interface:** Permette a parti distinte del software di essere scritte, compilate in anticipo ed ottimizzate in modo indipendente, venendo poi unite durante la fase di collegamento (*linking*) [TheProcedureAbstraction.pdf, Slide 154].

*   **Perché le procedure sono centrali (slide "Conceptual Overview"):** offrono information hiding, spazi di nomi distinti e separabili, interfacce uniformi. L'hardware sottostante supporta ben poco di queste astrazioni (capisce bit, byte, interi, reali e indirizzi, ma non entry/exit, interfacce, meccanismi call/return oltre il semplice trasferimento di controllo, spazi di nomi o scope annidati): parte del lavoro del compilatore è costruire queste astrazioni sopra l'hardware ("il compilatore mantiene fede alle bugie raccontate ai programmatori"), e parte è renderle efficienti (ruolo della code optimization) [TheProcedureAbstraction.pdf, slide "Conceptual Overview" / "The Procedure (More Abstract View)"].
*   **Compile-time vs run-time (slide "Run Time versus Compile Time"):** le sequenze di linkage (e il codice del corpo della procedura) **eseguono** a runtime; il codice per la linkage viene però **emesso** a compile time; la convenzione di linkage stessa è progettata molto prima di entrambi questi momenti — un punto spesso fonte di confusione.
*   **Il compilatore deve decidere quasi tutto (slide "Practical Overview"):** la locazione per ogni valore (nominato e non), il metodo per calcolare ogni risultato (es. come tradurre uno statement `case`), e cosa avviene a compile-time rispetto a runtime. Tutte queste decisioni emergono in modo centrale nell'implementazione delle procedure.

### 9.1bis Lexical vs Dynamic Scoping
*   **Il problema dello scoping (slide "The Problem"):** dato un punto $p$ nel programma, quale dichiarazione di `x` è quella corrente? A runtime, dove si trova il valore di `x` da usare? Mentre il parser entra ed esce dagli scope, come elimina `x`? Il compilatore deve **modellare lo spazio dei nomi** tramite symbol table con scoping lessicale [TheProcedureAbstraction.pdf, slide "The Problem"].
*   **Perché introdurre lo scoping lessicale (slide "The Procedure as a Name Space"):** fornisce un meccanismo a compile-time per legare le variabili "libere"; semplifica le regole di naming e risolve i conflitti; consente al programmatore di introdurre nomi "locali" con libertà.
*   **Lexical scoping:** ogni variabile libera è legata alla dichiarazione del suo nome **lessicalmente più vicina** all'uso; la dichiarazione proviene sempre da uno scope che racchiude il riferimento [TheProcedureAbstraction.pdf, slide "Lexical vs Dynamical scoping"].
*   **Dynamic scoping:** una variabile libera è legata alla variabile omonima creata **più di recente a runtime** (es. LISP, o come possibilità in Common LISP) [TheProcedureAbstraction.pdf, slide "Lexical vs Dynamical scoping"].
*   **Esempi di scoping per linguaggio (slide "The Procedure as a Name Space"):** C ha scope globale, static, locale e di blocco (in stile Fortran) — i blocchi possono essere annidati, le procedure no; Scheme ha scope globale, a livello di procedura, e annidato (`let`).
*   **Esempio guida (slide "Example with lexical scoping"):** la procedura annidata
    ```
    procedure p { int a,b,c
      procedure q { int v,b,x,w
        procedure r { int x,y,z; ... }
        procedure s { int x,a,v; ... }
        ... r ... s
      }
      ... q ...
    }
    ```
    si traduce nei blocchi lessicali `B0{a,b,c} ⊃ B1{v,b,x,w} ⊃ B2{x,y,z}` e `B1 ⊃ B3{x,a,v}`: la `b` dichiarata in B1 **oscura** la `b` di B0 all'interno di B1 (e dei blocchi da esso contenuti); le variabili `x,a,v` dichiarate in B3 oscurano gli omonimi di B0/B1 e non sono visibili al di fuori di B3.

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
    | return address                | | indirizzo di ripresa del chiamante
    | access link                  | | supporto all'accesso non-locale
    | caller's ARP                 | | ripristino dell'AR del chiamante
    | local variables (+ spill)    | | variabili locali e registri scaricati
    +------------------------------+ ▼
    ```
*   **Dove vivono le variabili? (slide "Where Do All These Variables Go?")**
    *   **Automatic & Local:** mantenute nell'AR della procedura o in un registro; lifetime coincide con quella dell'invocazione della procedura.
    *   **Static:** a livello di procedura, un'area di storage etichettata col nome della procedura; a livello di file, etichettata col nome del file; lifetime = intera esecuzione.
    *   **Global:** una o più aree dati globali nominate; lifetime = intera esecuzione.
*   **Organizzazione classica dello spazio d'indirizzamento (slide "Placing Run-time Data Structures"):** un unico spazio logico di indirizzi contiguo `Code | Static & Global | Stack → ← Heap`, con stack e heap che crescono l'uno verso l'altro per una migliore utilizzazione dello spazio disponibile. Codice, dati statici e globali hanno dimensione nota (etichette simboliche nel codice); stack e heap crescono e si riducono nel tempo; si tratta comunque di uno spazio di indirizzi **virtuale**, mappato dall'hardware reale (cache L1/L2, core del processore) in modo trasparente rispetto alla correttezza — la struttura della cache incide sulle prestazioni, non sulla correttezza [TheProcedureAbstraction.pdf, slide "How Does This Really Work?"].
*   **AR e ricorsione — modello semplicistico e sua estensione (slide "Where Do Local Variables Live?"):** un'allocazione ingenua assegnerebbe un'area dati per ciascuno scope distinto; ma con la ricorsione serve un'area dati per ogni **invocazione** di uno scope (l'AR). Nello schema più diffuso, un solo AR per istanza di procedura ospita tutti gli scope della procedura (che possono condividere spazio); la relazione tra scope interni a una singola procedura è **statica**, cioè nota a compile-time.

### 9.2bis Storage per Blocchi entro una Singola Procedura e Dati a Lunghezza Variabile
*   **Dati a lunghezza fissa (slide "Storage for Blocks within a Single Procedure"):** possono sempre risiedere a un offset costante dall'inizio della procedura. Riprendendo l'esempio di §9.1bis (`B0{a,b,c} ⊃ B1{v,b,x,w} ⊃ B2{x,y,z}`, `B1 ⊃ B3{x,a,v}`): la `a` di livello 0 è sempre il primo elemento (byte 0 dell'area dati a lunghezza fissa); la `x` di livello 1 (in B1) è sempre il sesto elemento (byte 20); la `x` di livello 2 (in B2) è sempre l'ottavo elemento (byte 28). **Domanda aperta della slide:** dove va la `a` dichiarata nel *secondo* blocco di livello 2 (B3)? — la disposizione lineare `a b c | v b x w | x y z | x a v` mostra che ogni blocco fratello (B2 e B3, entrambi a livello 2 ma non annidati l'uno nell'altro) riceve comunque un'area contigua propria all'interno dell'area dati a lunghezza fissa complessiva della procedura.
*   **Symbol table con scoping lessicale (slide "Lexically-scoped Symbol Tables"):** idea di alto livello — si crea una nuova tabella per ogni scope e le si concatena per la ricerca (lookup). Nell'esempio con procedure annidate `p ⊃ q ⊃ r` (e `q ⊃ s`), ogni tabella (r, q, p) punta alla tabella dello scope lessicalmente racchiudente, formando una catena risalibile durante la risoluzione dei nomi.
*   **Dati a lunghezza variabile (slide "Variable-length Data"):** per gli **array**, se la dimensione è nota a tempo di compilazione, si colloca l'array nell'area dati a lunghezza fissa. Se la dimensione è **variabile** (es. `int v(a)` con `a` non costante), si memorizza un **descrittore** nell'area fissa, con un puntatore all'area a lunghezza variabile. L'**area a lunghezza variabile** viene allocata **alla fine** dell'area a lunghezza fissa del blocco in cui è dichiarata (includendo tutti i blocchi contenuti). Esempio slide: con `B0{a,b} ⊃ B1{v(a),b,x} ⊃ B2{x,y(8)}`, il layout finale è `[a b v b x x | y(8) | v(a)]` — prima tutta l'area fissa di tutti i blocchi (inclusi i descrittori), poi le aree a lunghezza variabile in ordine.

### 9.3 Indirizzamento e Risoluzione dei Nomi Non Locali
*   **Coordinate Statiche $\langle level, offset \rangle$:**
    A tempo di compilazione, ogni variabile è identificata univocamente da una coppia:
    *   `level`: Il livello lessicale di annidamento in cui la variabile è dichiarata [TheProcedureAbstraction.pdf, Slide 156].
    *   `offset`: Lo scostamento fisso e noto dall'inizio del record d'attivazione [TheProcedureAbstraction.pdf, Slide 156].
    Il codice successivo userà la coordinata statica per generare indirizzi e riferimenti; il `level` è funzione della tabella in cui `x` viene trovata (memorizzato nella entry di ciascun `x`); l'`offset` deve essere assegnato e memorizzato nella symbol table, deciso e noto a compile-time, e usato per generare codice che esegue a runtime [TheProcedureAbstraction.pdf, slide "Translating Local Names"].
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
    *   **Tabella completa di generazione codice (slide "Establishing Addressability — Using Access Links"):** assumendo livello lessicale corrente 2, access link a `ARP − 4`, ARP in $r_0$:

        | Coordinata Statica | Codice Generato |
        |---|---|
        | $\langle 2,8\rangle$ | `loadAI r0, 8 ⇒ r10` |
        | $\langle 1,12\rangle$ | `loadAI r0, -4 ⇒ r1` ; `loadAI r1, 12 ⇒ r10` |
        | $\langle 0,16\rangle$ | `loadAI r0, -4 ⇒ r1` ; `loadAI r1, -4 ⇒ r1` ; `loadAI r1, 16 ⇒ r10` |

        Il costo di accesso **varia con il livello** (una `loadAI` in più per ogni salto della catena); tutti gli accessi sono comunque relativi all'ARP corrente ($r_0$) [TheProcedureAbstraction.pdf, slide "Establishing Addressability — Using Access Links"].
    *   **Manutenzione degli access link (slide "Maintaining access link")** — chiamante a livello $p$, chiamato definito a livello $q$:
        *   $q = p+1$ (il chiamato è annidato nel chiamante): il link del chiamato è l'**ARP corrente**;
        *   $q = p$: il chiamato **copia** l'access link del chiamante;
        *   $q < p$: risalire la catena fino all'ARP di livello $q-1$ e usarlo come link.

        Il costo di manutenzione è proporzionale alla distanza lessicale.
*   **Display:**
    Un array globale di puntatori, allocato in memoria o registri, in cui l'elemento all'indice $i$ contiene l'indirizzo dell'AR corrente attivo per il livello lessicale $i$ [TheProcedureAbstraction.pdf, Slide 22, 162].
    *   *Vantaggi:* L'accesso a qualsiasi variabile non locale richiede un costo fisso costante ($O(1)$) indipendentemente dal livello di annidamento [TheProcedureAbstraction.pdf, Slide 162].
    *   *Svantaggi:* Richiede la manutenzione dell'array globale ad ogni chiamata e ritorno e l'occupazione di un registro fisso dedicato [TheProcedureAbstraction.pdf, Slide 162].
    *   **Esempio Display (slide)** — livello corrente 2, display all'etichetta `_disp`, celle da 4 byte; accesso a $\langle 1, 12 \rangle$:
        ```iloc
        loadI  _disp => r1      // indirizzo del display
        loadAI r1, 4  => r1     // ARP del livello 1   (4 × level)
        loadAI r1, 12 => r10    // variabile
        ```
        Accesso a **costo costante**; manutenzione: all'ingresso al livello $j$ salvare il vecchio $Display[j]$ nell'AR (*saved ptr.*) e scriverci l'ARP; all'uscita ripristinarlo. Contro: l'indirizzo del display consuma un registro.
    *   **Tabella completa di generazione codice (slide "Establishing Addressability — Using a Display"):** assumendo livello corrente 2, display all'etichetta `_disp`, indirizzo desiderato $=\_disp + 4\times level$:

        | Coordinata Statica | Codice Generato |
        |---|---|
        | $\langle 2,8\rangle$ | `loadAI r0, 8 ⇒ r10` |
        | $\langle 1,12\rangle$ | `loadI _disp ⇒ r1` ; `loadAI r1, 4 ⇒ r1` ; `loadAI r1, 12 ⇒ r10` |
        | $\langle 0,16\rangle$ | `loadI _disp ⇒ r1` ; `loadAI r1, 0 ⇒ r1` ; `loadAI r1, 16 ⇒ r10` |

        I costi di accesso sono **fissi** indipendentemente dal livello; l'indirizzo del display può però consumare un registro dedicato [TheProcedureAbstraction.pdf, slide "Establishing Addressability — Using a Display"].
    *   **Manutenzione del Display (slide "Maintaining Display"):** all'ingresso nel livello $j$ si salva il vecchio contenuto di `Display[j]` in un campo dedicato dell'AR (**saved ptr.**) e vi si scrive l'ARP corrente; all'uscita dal livello $j$ si ripristina il valore salvato.
*   **⚠️ Catena statica ≠ catena delle chiamate — esempio completo (slide "The static and call chain do not coincide!"):**

	![[Pasted image 20260908171022.png|479]]

	la **call history a runtime** è `Main → p2 → q2 → r2 → p1`, ma la **catena statica** (nesting lessicale) resta `Main → p2 → q2 → r2` — quando `r2` chiama `p1`, l'antenato lessicale di `p1` è `Main`, non `r2`: il link di accesso (o la voce di display) usato da `p1` fa riferimento all'ARP di `Main`, completamente scavalcando la catena dinamica delle chiamate. Questo è l'esempio concreto per cui, in generale, **l'antenato lessicale non coincide con il chiamante**.
*   **Confronto finale Access Links vs Display (slide "Establishing Addressability — Access Links Versus Display"):** entrambi aggiungono un qualche overhead a ogni chiamata. Gli access link hanno costo variabile col livello di riferimento — l'overhead è incorso solo su riferimenti e chiamate, e se gli AR sopravvivono alla procedura gli access link continuano comunque a funzionare correttamente. Il display ha costo fisso per ogni riferimento — riferimenti e chiamate devono caricare l'indirizzo del display (tipicamente un registro dedicato); la scelta migliore dipende dal rapporto tra accessi non-locali e chiamate. Per entrambi gli schemi, il compilatore deve comunque inserire codice in ogni chiamata e ritorno di procedura.
*   **Procedure Linkage (Sequenze d'Invocazione):**
    La creazione e distruzione dell'ambiente d'esecuzione dell'AR è regolata da convenzioni di chiamata concordate (*linkage convention*) suddivise in:
    1.  *Pre-call (Chiamante):* Alloca lo spazio per i parametri, valuta le espressioni dei parametri, salva l'indirizzo di ritorno e i registri *caller-saved* volatili.
    2.  *Prologue (Chiamato):* Completa l'allestimento dell'AR, aggiorna l'ARP, alloca le variabili locali, inizializza i dati e salva i registri *callee-saved* non volatili [TheProcedureAbstraction.pdf, Slide 12].
    3.  *Epilogue (Chiamato):* Inserisce il valore di ritorno, ripristina i registri salvati nel prologo e carica l'indirizzo di ritorno.
    4.  *Post-return (Chiamante):* Dealloca l'AR del chiamato, legge il valore di ritorno e ripristina i propri registri.
    (Il dettaglio operativo completo di ciascuna delle quattro fasi è sviluppato in §9.5.)
*   **Allocazione dell'AR: Stack vs Heap:**
    *   *Stack (Pila):* Se la vita dell'AR coincide strettamente con l'invocazione (LIFO, classico in C o Pascal), gli AR sono gestiti sulla pila di sistema per massima efficienza [TheProcedureAbstraction.pdf, Slide 158].
    *   *Heap (Sottofondo):* Se le variabili locali o la procedura stessa possono "sopravvivere" al termine della routine (come nel caso delle *closures* con variabili catturate in ML o Rust), gli Activation Record non possono essere deallocati e devono essere mantenuti nello heap [TheProcedureAbstraction.pdf, Slide 158].

### 9.4 Creazione/Distruzione degli AR e Convenzioni di Salvataggio Registri
*   **Collaborazione caller/callee (slide "Creating and Destroying Activation Records"):** tutte e tre le astrazioni della procedura lasciano stato nell'AR. Creare e inizializzare l'AR (preservando il mondo del chiamante) tocca alla chiamata di procedura; smantellare l'ambiente (ripristinando il mondo del chiamante) tocca al ritorno. Il chiamante conosce da solo alcune informazioni necessarie: indirizzo di ritorno, valori dei parametri, accesso ad altri scope; il chiamato conosce da solo il resto: dimensione dell'area dati locale, registri che userà. La loro collaborazione prende la forma di una **linkage convention**.
*   **Procedure Linkages come convenzione di sistema (slide "Procedure Linkages"):** a tempo di compilazione il chiamato può non essere disponibile per l'ispezione (chiamate diverse possono trovarsi in diverse unità di compilazione), quindi tutte le chiamate devono usare lo stesso protocollo. Il compilatore deve usare una sequenza standard di operazioni, che applica le astrazioni di controllo e dei dati e divide la responsabilità fra chiamante e chiamato — di norma un accordo a livello dell'intero sistema, per garantire l'interoperabilità.
*   **Chi salva i registri? (slide "Saving Registers")** Si dividono convenzionalmente i registri in tre insiemi:
    *   **Caller-saved:** il chiamante li usa per valori *short-lived* attraverso la chiamata — il chiamante sa quali valori sono vivi attraverso la call.
    *   **Callee-saved:** il chiamato li usa solo *dopo* aver riempito i registri caller-saved — il chiamato sa quali registri userà.
    *   **Riservati alla linkage convention:** ARP, indirizzo di ritorno (se in registro), ecc.
    In ogni caso, sono salvati in una delle due AR (chiamante o chiamato).
*   **Struttura standard della linkage (slide "Procedure Linkages — Standard Procedure Linkage"):** ogni procedura ha un **prologo** standard e un **epilogo** standard; ogni chiamata comporta una sequenza di **pre-call** e una di **post-return**. Queste ultime due sono completamente predicibili dal punto di chiamata, poiché dipendono dal numero e dal tipo dei parametri attuali.

### 9.5 Le Quattro Fasi della Procedure Linkage in Dettaglio
*(Integra e sviluppa in dettaglio operativo l'elenco sintetico già introdotto in §9.3)*

*   **Pre-call (chiamante) — dettagli (slide "Procedure Linkages — Pre-call Sequence"):** inizia ad allestire l'ambiente di base del chiamato e valuta i parametri formali.
    1. Alloca spazio per l'AR del chiamato.
    2. Valuta ciascun parametro e ne memorizza valore o indirizzo.
    3. Salva l'indirizzo di ritorno: l'ARP del chiamante nell'AR del chiamato.
    4. Se si usano access link: trova l'antenato lessicale appropriato e lo copia nell'AR del chiamato.
    5. Salva gli eventuali registri *caller-saved* (nello spazio dell'AR del chiamante).
    6. Salta all'indirizzo del prologo del chiamato.
*   **Prologue (chiamato) — dettagli (slide "Procedure Linkages — Prolog Code"):** completa l'allestimento dell'ambiente del chiamato e preserva le parti dell'ambiente del chiamante che verranno disturbate.
    1. Preserva gli eventuali registri *callee-saved*.
    2. Se si usa il display: salva la voce del display per il livello lessicale corrente, poi vi memorizza l'ARP corrente.
    3. Alloca spazio per i dati locali.
    4. Gestisce eventuali inizializzazioni di variabili locali.
*   **Epilogue (chiamato) — dettagli (slide "Procedure Linkages — Epilog Code"):** conclude gli affari del chiamato e inizia a ripristinare l'ambiente del chiamante.
    1. Memorizza il valore di ritorno.
    2. Ripristina i registri *callee-saved*.
    3. Libera lo spazio dati locale, se necessario.
    4. Carica l'indirizzo di ritorno dall'AR.
    5. Ripristina l'ARP del chiamante.
    6. Salta all'indirizzo di ritorno.
*   **Post-return (chiamante) — dettagli (slide "Procedure Linkages — Post-return Sequence"):** disfa le azioni della sequenza di pre-call e rimette ogni valore al proprio posto.
    1. Libera l'AR del chiamato.
    2. Ripristina gli eventuali registri caller-saved.
    3. Ripristina i parametri call-by-reference nei registri, se necessario; copia indietro i parametri call-by-value/result.
    4. Riprende l'esecuzione dopo la chiamata.

### 9.6 Comunicazione tra Procedure: Passaggio dei Parametri
*(slide "Communicating Between Procedures")* La maggior parte dei linguaggi fornisce un meccanismo di passaggio dei parametri: l'espressione usata al call site diventa una variabile nel chiamato. Due meccanismi di binding comuni:
*   **Call-by-reference:** passa un puntatore al parametro attuale; richiede uno slot nell'AR per l'indirizzo; più nomi possono condividere lo stesso indirizzo.
*   **Call-by-value:** passa una copia del valore al momento della chiamata; richiede uno slot nell'AR; ogni nome ottiene una locazione univoca (può comunque avere lo stesso valore). Gli array sono tipicamente passati per riferimento, non per valore.

### 9.7 Dove Vivono gli Activation Record: Regole per Famiglia di Linguaggio
*(slide "How is it realised? It depends on where the AR are…")* La realizzazione concreta della linkage dipende da dove risiedono gli AR:
*   **AR sulla pila (Algol-60 rules):** facile da estendere (basta avanzare il top-of-stack). Chiamante e chiamato condividono la responsabilità: il chiamante può inserire (push) parametri, spazio registri, slot valore di ritorno, indirizzo di ritorno, informazioni di addressability e il proprio ARP; il chiamato può inserire lo spazio per le variabili locali (fisse e a lunghezza variabile).
*   **AR nello heap (ML rules):** difficile da estendere. Opzioni possibili: il chiamante passa tutto in registri e il chiamato alloca e riempie l'AR; oppure si memorizzano parametri, indirizzo di ritorno, ecc. nell'AR del **chiamante**; oppure si memorizza la dimensione dell'AR del chiamato in una costante statica.
*   **Senza ricorsione (Fortran 66 & 77 rules):** gli activation record possono essere **statici**, allocati una volta per tutte a tempo di compilazione.
*   **Activation Record Basics — vista riassuntiva (slide "Remember This Drawing?"):** l'AR (con ARP che punta al blocco parametri/registri/valore di ritorno/indirizzo di ritorno/addressability/ARP del chiamante/variabili locali) rimane lo schema unificante indipendentemente da dove, fisicamente, l'AR viene collocato (stack, heap, o area statica).

### 9.8 Riepilogo (Recap)
*(slide "Recap")*

| Categoria | Lifetime | Dove vive |
|---|---|---|
| **Automatic** | coincide con l'attivazione della procedura | AR (activation record) |
| **Static** | può durare quanto l'intera esecuzione | area dati statica nominata |
| **Dynamic** | sotto controllo del programma, non nota a compile-time | heap |

Per gli elementi a lunghezza variabile: si colloca un descrittore nella locazione "naturale" (area dati a lunghezza fissa) e si alloca l'elemento vero e proprio alla fine dell'AR oppure nello heap.

Rappresentare le variabili tramite coordinate statiche $\langle level, offset\rangle$ richiede quindi di: (a) mappare, **a runtime**, il livello lessicale in un indirizzo base dell'area dati; (b) emettere, **a tempo di compilazione**, il codice che esegue quella mappatura — è esattamente il problema risolto in modo duale da access link (costo variabile col livello, nessun registro dedicato permanente) e display (costo costante, un registro dedicato all'indirizzo del display).

<a id="cap10"></a>
## CAPITOLO 10: Generazione del Codice (Instruction Selection, Code Shape, Array, Stringhe, Controllo di Flusso)

**Source:** _IntroCodeGeneration.pdf_ (68 slide, Cooper & Torczon — Engineering a Compiler, cap. 7)

> **Nota di revisione:** questo capitolo è stato interamente riscritto ed espanso confrontandolo slide per slide con il testo integrale OCR di `IntroCodeGeneration.pdf` (68 slide). La versione precedente copriva solo 4 sotto-sezioni (§10.1–10.4 originali, corrispondenti a poco più di un quarto del materiale sorgente); mancavano interamente: modelli di memoria, ambiguità dei valori, gestione dell'assegnamento come operatore, l'intera sezione sugli array (indirizzamento, false zero, layout multi-dimensionale, dope vector, range checking), l'ottimizzazione degli accessi array nei loop (LICM e operator strength reduction), la rappresentazione delle stringhe, e la rappresentazione di valori booleani/relazionali. Queste sezioni sono ora integrate qui per intero. La numerazione interna delle sotto-sezioni sostituisce integralmente quella della versione precedente.

### 10.1 Struttura del Back-End e Modelli di Memoria

- **Il back-end come "collo di bottiglia" del compilatore (slide "Structure of a Compiler"):** un compilatore è, in sostanza, molta roba veloce seguita da alcuni problemi difficili — la parte difficile risiede prevalentemente nella generazione del codice e nell'ottimizzazione. Per i sistemi multicore serve gestire parallelismo e condivisione; per le prestazioni su singolo core, allocazione e scheduling sono critici [IntroCodeGeneration.pdf, slide "Structure of a Compiler"]. Le tre fasi del back-end e le rispettive complessità computazionali:

| Fase                    | Complessità            | Input                    | Output                   |
| ----------------------- | ---------------------- | ------------------------ | ------------------------ |
| fvInstruction Selection | $O(n)$                 | IR con registri $\infty$ | IR con registri $\infty$ |
| Instruction Scheduling  | o veloce o NP-Completo | IR con registri $\infty$ | IR con registri $\infty$ |
| Register Allocation     | NP-Completo            | IR con registri $\infty$ | codice con $k$ registri  |

(Front-end/scanner-parser: $O(n\log n)$ a esponenziale nel caso peggiore per l'analisi sintattica generale, ma tipicamente lineare) [IntroCodeGeneration.pdf, slide "Structure of a Compiler"].    
- **Il modello assunto dal corso (slide "Structure of a Compiler" #2):** la selezione delle istruzioni è considerata relativamente semplice (un problema già risolto negli anni '80); allocazione e scheduling sono le fasi complesse; il posizionamento delle operazioni non è ancora un problema critico — si assume un unico insieme di registri unificato [IntroCodeGeneration.pdf, slide "Structure of a Compiler" (2)].
    
- **Il ruolo della IR (slide "What about the IR?"):** si assume una IR di basso livello, RISC-like, come ILOC, con un numero di registri "sufficiente". ILOC è stato progettato appositamente per questo scopo, con: branch, compare e label; tag di memoria; gerarchia di load e store; predisposizione per più operazioni per ciclo [IntroCodeGeneration.pdf, slide "What about the IR?"].
    
- **Ruolo dell'ottimizzatore rispetto al front-end (slide "Analysis & Optimization"):** la traduzione prodotta dal front-end considera gli statement uno alla volta, man mano che vengono incontrati; questa IR iniziale codifica strategie implementative generali, valide in qualunque contesto circostante. A runtime il codice verrà eseguito in un contesto più vincolato e prevedibile: l'ottimizzatore analizza la forma IR del codice per scoprire fatti sul contesto e li usa per riscrivere (trasformare) il codice, in modo che calcoli la stessa risposta ma in modo più efficiente [IntroCodeGeneration.pdf, slide "Analysis & Optimization"].
    
- **Compiti del back-end (slide "The Back End"):** il back-end del compilatore attraversa la forma IR ed emette il codice per la macchina target: (1) seleziona le operazioni della macchina target per implementare ciascuna operazione IR (**instruction selection**); (2) sceglie un ordine in cui le operazioni verranno eseguite in modo efficiente (**instruction scheduling**); (3) decide quali valori risiederanno in registro e quali in memoria (**register allocation**) [IntroCodeGeneration.pdf, slide "The Back End"].
    
- **I due modelli di memoria (slide "Memory Models"):**
    
    - **Register-to-register model:** mantiene tutti i valori che possono legalmente essere immagazzinati in un registro dentro un registro; ignora i limiti hardware sul numero di registri disponibili; il back-end del compilatore deve inserire esplicitamente `load` e `store`. Usa **registri virtuali**!
    - **Memory-to-memory model:** mantiene tutti i valori in memoria; promuove i valori a registro solo immediatamente prima del loro uso; il back-end del compilatore può rimuovere `load` e `store`.
    - I compilatori per macchine RISC usano tipicamente il modello register-to-register, perché è più facile determinare quando i registri sono usati [IntroCodeGeneration.pdf, slide "Memory Models"].
- **Le tre definizioni operative (slide "Definitions"):**
    
    - **Instruction selection:** mappa la IR in codice assembly; assume un modello di memoria e una code shape fissati; combina operazioni, usando i modi di indirizzamento (istruzioni con modalità registro+offset o registro-a-registro).
    - **Instruction scheduling:** riordina le operazioni per nascondere le latenze; assume un programma fissato (un insieme di operazioni); cambia la domanda di registri.
    - **Register allocation:** decide quali valori risiederanno in registro; cambia la mappatura di storage, e può aggiungere condivisioni spurie (_false sharing_); si occupa del posizionamento dei dati e delle operazioni di memoria.
    
    Questi tre problemi sono **strettamente accoppiati** e richiedono analisi statica [IntroCodeGeneration.pdf, slide "Definitions"].
    

### 10.2 Il Concetto di "Code Shape"

- **Definizione (slide "Code Shape (Chapter 7)"):** il compilatore deve scegliere fra molte alternative implementative per ciascun costrutto su un dato processore; queste scelte hanno un impatto forte e diretto sulla qualità del codice finale prodotto. La _code shape_ è il prodotto finale di molte decisioni, grandi e piccole. **Impatto:** la code shape ha un forte impatto sul comportamento del codice compilato e sulla capacità dell'ottimizzatore e del back-end di migliorarlo ulteriormente; la code shape può codificare fatti importanti, oppure nasconderli [IntroCodeGeneration.pdf, slide "Code Shape (Chapter 7)"].
    
- **Esempio guida — lo statement `case` su un valore carattere (slide "Code Shape" #1):**
    
    1. **Cascata di if-then-else:** il costo dipende da dove si trova effettivamente il case cercato — $O(256)$.
    2. **Ricerca binaria:** richiede un insieme denso di condizioni da cercare — costo uniforme $O(\log 256)$.
    3. **Jump table:** cerca l'indirizzo in una tabella e salta a esso — si scambia spazio dati per velocità — costo uniforme (costante).
    
    Tutte queste sono implementazioni legali (e ragionevoli) dello statement switch; **le prestazioni dipendono dall'ordine dei case!** [IntroCodeGeneration.pdf, slide "Code Shape" #1].
    
- **Quale implementazione scegliere per lo switch? (slide "Which implementation for switch?"):** quella migliore per un particolare statement switch dipende da molti fattori, come: il numero di case e le loro frequenze relative di esecuzione; la conoscenza della struttura di costo del branching sul processore. Anche quando il compilatore non ha informazione sufficiente per scegliere, **deve comunque scegliere** una strategia implementativa: nessuna quantità di trasformazione può convertire un'implementazione in un'altra [IntroCodeGeneration.pdf, slide "Which implementation for switch?"].
    
- **Esempio guida — l'operazione ternaria $x+y+z$ (slide "Code Shape: the ternary operation x+y+z"):** ci sono diversi modi di implementare $x+y+z$, sfruttando la commutatività e l'associatività dell'addizione sugli interi:
    
    - $(x+y)+z$: `x+y → t1; t1+z → t2`
    - $(x+z)+y$: `x+z → t1; t1+y → t2`
    - $(y+z)+x$: `y+z → t1; t1+x → t2`
    
    _Cosa succede se il compilatore sa che $x$ è la costante 2 e $z$ è la costante 3?_ Il compilatore dovrebbe rilevare che $2+3$ è calcolabile e ripiegare (_fold_) il risultato nel codice. _Cosa succede se $y+z$ viene valutato prima altrove nel programma?_ La forma "migliore" per $x+y+z$ dipende dalla conoscenza contestuale — possono esserci diverse opzioni in conflitto tra loro [IntroCodeGeneration.pdf, slide "Code Shape: the ternary operation x+y+z"].
    
- **Perché non fidarsi semplicemente di ottimizzatore e back-end? (slide "Code Shape" #2):** ottimizzatore e back-end approssimano le risposte a molti problemi difficili; le singole passate del compilatore devono girare velocemente; spesso conviene codificare informazione utile direttamente nella IR — la forma di un'espressione o di una struttura di controllo, un valore mantenuto in registro piuttosto che in memoria. Derivare tale informazione può essere costoso, quando possibile; registrarla esplicitamente nella IR è spesso più facile ed economico [IntroCodeGeneration.pdf, slide "Code Shape" #2].
    

### 10.3 Postorder Treewalk Evaluator: Generazione del Codice per le Espressioni

- **Come generare codice ILOC (slide "How to generate ILOC code"):** la forma a tre indirizzi permette al compilatore di nominare il risultato di ogni operazione e preservarlo per un riuso successivo; il compilatore usa sempre un nuovo registro, lasciando all'allocatore il compito di ridurli. Per generare il codice per un'espressione banale $a+b$, il compilatore emette codice che garantisce che i valori di $a$ e $b$ siano in registro. Se $a$ è memorizzato in memoria all'offset `@a` nel record di attivazione corrente (AR), il codice è:
    
    ```iloc
    loadI @a       ⇒ r1
    loadAO rarp,r1 ⇒ ra
    ```
    
    [IntroCodeGeneration.pdf, slide "How to generate ILOC code"].
- **L'idea del postorder treewalk (slide "Generating Code for Expressions"):** si assume un AST come input e ILOC come output; si usa un _valutatore treewalk in postordine_: visita e valuta i figli, poi emette il codice per l'operazione stessa, e restituisce il registro col risultato. La complessità dell'indirizzamento dei nomi viene sepolta in routine chiamate `base()`, `offset()` e `val()`. Funziona per espressioni semplici ed è facilmente estendibile ad altri operatori [IntroCodeGeneration.pdf, slide "Generating Code for Expressions"]:
    ```text
	expr(node) {
		register result, t1, t2;

		switch (type(node)) {
		
			case *, /, +, -:
				t1 <- expr(leftChild(node));
				t2 <- expr(rightChild(node));
		
				result <- NextRegister();
		
				emit(
					op(node),
					t1,
					t2,
					result
				);
				break;
		
			case IDENTIFIER:
				// Recupera il puntatore al record di attivazione
				// contenente l'identificatore.
				t1 <- base(node);
		
				// Carica l'offset dell'identificatore.
				t2 <- NextRegister();
				emit(
					loadI,
					offset(node),
					none,
					t2
				);
		
				// Carica il valore memorizzato all'indirizzo base + offset.
				result <- NextRegister();
				emit(
					loadAO,
					t1,
					t2,
					result
				);
				break;
		
			case NUMBER:
				result <- NextRegister();
		
				// Carica il valore costante.
				emit(
					loadI,
					val(node),
					none,
					result
				);
				break;
		}

    return result;
}
	```
    
- **Traccia completa per `x + y` (slide "Generating Code for Expressions (a naive translation)" #1):** con contatore di registri a 0, per l'albero `+(x,y)`:
    
    ```text
		espr("x"):
		    rarp ← ptr AR di x
		
		    r1 ← NextRegister();
		    loadI @x ⇒ r1
		
		    r2 ← NextRegister();
		    loadA0 rarp, r1 ⇒ r2
		
		
		espr("y"):
		    rarp ← ptr AR di y
		
		    r3 ← NextRegister();
		    loadI @y ⇒ r3
		
		    r4 ← NextRegister();
		    loadA0 rarp, r3 ⇒ r4
		
		
		r5 ← NextRegister();
		Emit(add, r2, r4, r5):
		
		add r2, r4 ⇒ r5
    ```
    
    [IntroCodeGeneration.pdf, slide "Generating Code for Expressions (a naive translation)" #1].
- **Traccia completa per `x + z×y` (slide "Generating Code for Expressions (a naive translation)" #2):** per l'albero `+(x, ×(z,y))`, visitando prima il figlio sinistro (`x`) e poi il destro (`z×y`):
    
    ```text
	espr("x"):
	    r1 ← NextRegister();
	    loadI @x ⇒ r1
	    r2 ← NextRegister();
	    loadA0 rarp, r1 ⇒ r2
	
	espr("z"):
	    r3 ← NextRegister();
	    loadI @z ⇒ r3
	    r4 ← NextRegister();
	    loadA0 rarp, r3 ⇒ r4
	
	espr("y"):
	    r5 ← NextRegister();
	    loadI @y ⇒ r5
	    r6 ← NextRegister();
	    loadA0 rarp, r5 ⇒ r6
	
	r7 ← NextRegister();
	Emit(mul, r4, r6, r7):
	mult r4, r6 ⇒ r7
	r8 ← NextRegister();
	Emit(add, r2, r7, r8):
	add r2, r7 ⇒ r8
    ```
    
    [IntroCodeGeneration.pdf, slide "Generating Code for Expressions (a naive translation)" #2].
- **Effetti della code shape sulla domanda di registri (slide "Effects of code shape on the demand of registers"):** le decisioni di code shape incorporate nel generatore di codice a treewalk hanno un effetto diretto sulla domanda di registri — il codice naive sopra usa **8 registri** oltre a `rarp`; l'allocatore di registri (fase successiva della compilazione) può ridurre la domanda a **3 registri + rarp**:
    
    ```iloc
	loadI   @x        ⇒ r1
	loadA0  rarp, r1  ⇒ r1
	
	loadI   @z        ⇒ r2
	loadA0  rarp, r2  ⇒ r2
	
	loadI   @y        ⇒ r3
	loadA0  rarp, r3  ⇒ r3
	
	mult    r2, r3    ⇒ r2
	add     r1, r2    ⇒ r2
    ```
    
    [IntroCodeGeneration.pdf, slide "Effects of code shape on the demand of registers"].
- **La regola generale — quale figlio valutare per primo (slide, esempio senza titolo dopo "Effects..."):** confrontando due ordini di valutazione per lo stesso albero `x + z×y`, valutare prima `z×y` e poi `x` produce, dopo l'allocazione dei registri, una sequenza che usa **3 registri** in tutto:
    
    ```iloc
    load   @z        ⇒ r1loadA0 rarp,r1   ⇒ r1load   @y        ⇒ r2loadA0 rarp,r2   ⇒ r2mult   r1,r2     ⇒ r1load   @x        ⇒ r2loadA0 rarp,r2   ⇒ r2add    r2,r1     ⇒ r1
    ```
    
    **Regola generale: valutare per primo il figlio con maggiore domanda di registri.** Questa è precisamente una decisione di **code shape** [IntroCodeGeneration.pdf, slide sull'esempio "The best solution: alternate right and left children"].

### 10.4 Estensioni del Treewalk: Valori in Registro, Parametri, Valori Ambigui

- **Domande aperte sull'algoritmo semplice (slide "Some observations"):** cosa succede se l'IDENTIFIER è già in un registro? è in un'area dati globale? è un valore parametro (per valore o per riferimento)? [IntroCodeGeneration.pdf, slide "Some observations"].
- **Estensione del caso IDENTIFIER (slide "Extending the Simple Treewalk Algorithm" #1):**
    - _Valori già in un registro:_ se il valore è già in un registro, si restituisce direttamente il nome del registro; se non lo è, si carica come prima, ma si registra il fatto — occorre scegliere i nomi in modo da evitare di creare dipendenze spurie (_false dependences_).
    - _Valori parametro:_ **call-by-value** ⇒ può essere gestito come se fosse una variabile locale, come prima; **call-by-reference** ⇒ richiede un'indirezione extra (3 istruzioni) — il valore potrebbe non poter restare in un registro attraverso un assegnamento (vedi §10.5).
    - _Chiamate a funzione dentro un'espressione:_ si genera la sequenza di chiamata e si carica il valore di ritorno — questo **limita severamente** la capacità del compilatore di riordinare le operazioni [IntroCodeGeneration.pdf, slide "Extending the Simple Treewalk Algorithm" #1].
- **Mantenere i valori in registro: il problema dell'ambiguità (slide "Keeping values in registers"):** in un modello di memoria register-to-register, il compilatore cerca di assegnare quanti più valori possibile a registri virtuali; l'allocatore mapperà poi l'insieme di registri virtuali su registri fisici, inserendo gli spill. **Tuttavia**, il compilatore può mantenere un valore in registro solo per un **valore non ambiguo**: un valore è non ambiguo se può essere acceduto con un solo nome [IntroCodeGeneration.pdf, slide "Keeping values in registers"].
- **Il problema dei valori ambigui (slide "The problem with ambiguous values"):** si considerino `a` e `b` ambigui e il codice:
    
    ```
    a := m+n;b := 13;c := a+b;
    ```
    
    Se `a` e `b` si riferiscono alla stessa locazione, `c` ottiene il valore `26`; altrimenti `c` ottiene `m+n+13`. Il compilatore **non può** mantenere `a` in un registro durante l'assegnamento di `b`, a meno di dimostrare che gli insiemi di locazioni a cui i due nomi si riferiscono sono disgiunti — un'analisi che può essere costosa (**sharing analysis**) [IntroCodeGeneration.pdf, slide "The problem with ambiguous values"].
- **Da dove nascono i valori ambigui? (slide "Where do ambiguous values arise?"):** i valori ambigui possono nascere in diversi modi: valori memorizzati in una variabile basata su puntatore; parametri formali call-by-reference; molti compilatori trattano i valori degli elementi di array come ambigui, perché non possono stabilire se due riferimenti `A[i,j]` e `A[n,m]` si riferiscano alla stessa locazione — per sicurezza il compilatore deve considerare quei valori come ambigui [IntroCodeGeneration.pdf, slide "Where do ambiguous values arise?"].

### 10.5 Operatori Misti, Ordine di Valutazione e Gestione dell'Assegnamento

- **Estensione ad altri operatori (slide "Extending the Simple Treewalk Algorithm" #2):** si valutano gli operandi, poi si esegue l'operazione; operazioni complesse (funzioni esponenziali e trigonometriche) possono trasformarsi in chiamate a libreria. **Espressioni a tipo misto:** si inserisce codice di conversione secondo necessità, da una tabella di conversione; la maggior parte dei linguaggi ha tabelle di conversione simmetriche e razionali. Se il tipo non può essere inferito a tempo di compilazione, il compilatore deve inserire codice per controlli a runtime che verifichino i casi illegali [IntroCodeGeneration.pdf, slide "Extending the Simple Treewalk Algorithm" #2].
- **Ordine di valutazione (slide "Extending the Simple Treewalk Algorithm" #3):** si può usare commutatività e associatività per migliorare il codice per gli interi: per riconoscere che un valore è già stato calcolato ($a+b = b+a$), o per riconoscere che si possono calcolare sottoespressioni comuni (es. in `a+b+d` e `c+a+b` — cosa che non accade se si valuta sempre rigorosamente da sinistra a destra). **Non si dovrebbero riordinare le espressioni in virgola mobile!** Il sottoinsieme dei reali rappresentato su un calcolatore non preserva l'associatività: per `a-b-c` il risultato può dipendere dall'ordine di valutazione [IntroCodeGeneration.pdf, slide "Extending the Simple Treewalk Algorithm" #3].
- **Gestione dell'assegnamento come operatore (slide "Handling Assignment (just another operator)"):** per `lhs ← rhs`, la strategia è: valutare `rhs` a un valore (un rvalue); valutare `lhs` a una locazione (un lvalue) — se l'lvalue è un registro, si fa una `move` del rhs; se è un indirizzo, si fa una `store` del rhs. Se rvalue e lvalue hanno tipi diversi: si valuta l'rvalue al suo tipo "naturale", poi si converte quel valore al tipo di `*lvalue`. **Gli scalari non ambigui vanno in registro; gli scalari ambigui o gli aggregati vanno in memoria** [IntroCodeGeneration.pdf, slide "Handling Assignment (just another operator)"].
- **Assegnamento con tipo del rhs sconosciuto a compile-time (slide "Handling Assignment" #2):** è una proprietà del linguaggio e del programma specifico. Per la type-safety, il compilatore deve inserire un controllo a runtime (alcuni linguaggi e implementazioni ignorano la sicurezza — una cattiva idea); si aggiunge un campo tag ai dati per contenere l'informazione di tipo, controllato esplicitamente a runtime. Il codice per l'assegnamento diventa più complesso:
    
    ```text
	evaluate rhs 
	if type(lhs) ≠ rhs.tag 
	    then 
	    convert rhs to type(lhs) or signal a run-time error l
	hs ← rhs
    ```
    
    La scelta tra conversione ed eccezione a runtime dipende dai dettagli del linguaggio e del sistema dei tipi; è **molto più complesso** del controllo statico, e i costi ricadono a runtime anziché a compile-time [IntroCodeGeneration.pdf, slide "Handling Assignment" #2].
- **Type-checking a tempo di compilazione (slide "Handling Assignment" #3):** l'obiettivo è eliminare la necessità sia di tag sia di controlli a runtime, determinando a compile-time il tipo di ciascuna sottoespressione, e usando un controllo runtime solo quando il compilatore non può determinare i tipi. Strategia di ottimizzazione: se il compilatore conosce il tipo, sposta il controllo a compile-time; a meno che i tag non servano per il garbage collector, li elimina; se un controllo è necessario, prova a sovrapporlo con altra computazione. Si può progettare il linguaggio in modo che tutti i controlli siano statici [IntroCodeGeneration.pdf, slide "Handling Assignment" #3].
- **Riepilogo (slide "Code Generation for Expressions" — Summary):** il treewalk semplice produce codice ragionevole se si esegue prima la sottoespressione più esigente; si può implementare il treewalk esplicitamente, con una grammatica attribuita o una traduzione ad-hoc guidata dalla sintassi (§6.6). Si gestisce l'assegnamento come un operatore, inserendo conversioni secondo le regole specifiche del linguaggio; se il controllo a compile-time è impossibile, si controllano i tag a runtime [IntroCodeGeneration.pdf, slide "Code Generation for Expressions"].

### 10.6 Generazione del Codice per gli Array

- **Calcolo dell'indirizzo di un array monodimensionale (slide "Computing an Array Address of an array A[low:high]"):** dato `A[i]` con array dichiarato `A[low:high]`: $$\text{addr}(A[i]) = {@}A + (i - low) \times \text{sizeof}(A[i])$$ In generale: $\text{base}(A) + (i - low) \times \text{sizeof}(A[i])$. A seconda di come `A` è dichiarato, `@A` può essere un offset dall'ARP, un offset da un'etichetta globale, o un indirizzo arbitrario — i primi due sono costanti a tempo di compilazione. `sizeof` è quasi sempre una potenza di 2, nota a compile-time ⇒ si usa uno shift per velocità [IntroCodeGeneration.pdf, slide "Computing an Array Address of an array A[low:high]"].
    
- **Il "false zero" (slide "Computing an Array Address A[low:high]" / "The False Zero"):** se il compilatore conosce `low`, può ripiegare la sottrazione direttamente in `@A`, definendo: $${@}_0 = {@}A - (low \times w), \qquad w = \text{sizeof}(A[i])$$ L'indirizzo diventa allora ${@}A_0 + (i \times w)$ invece di ${@}A + (i-low)\times w$. Con `A[2..7]` e `w` tale che uno shift di 2 bit equivale a moltiplicare per $w$, il confronto di codice è (slide "The False Zero"):
    
    ```iloc
    ; calcolo con @A                    ; calcolo con @A0
    loadI   @A       ⇒ r@A              loadI   @A0      ⇒ r@A0
    subI    ri, 2    ⇒ r1               lshiftI ri, 2    ⇒ r1
    lshiftI r1, 2    ⇒ r2               loadA0  r@A0,r1  ⇒ rv
    loadA0  r@A,r2   ⇒ rv
    ```
    
    Usare il false zero **risparmia un'istruzione** (`subI`) a ogni accesso — la tecnica è redditizia quando l'array viene acceduto molte volte, ad esempio dentro un ciclo [IntroCodeGeneration.pdf, slide "The False Zero"].
    
- **Array multi-dimensionali: schemi di storage (slide "How does the compiler handle A[i,j]?"):** prima di tutto occorre concordare uno schema di memorizzazione:
    
    - **Row-major order** (la maggior parte dei linguaggi): memorizza come sequenza di righe consecutive; il subscript più a destra varia più rapidamente: `A[1,1], A[1,2], A[1,3], A[2,1], …`.
    - **Column-major order** (Fortran): memorizza come sequenza di colonne; il subscript più a sinistra varia più rapidamente: `A[1,1], A[2,1], A[1,2], …`.
    - **Indirection vectors** (Java): un vettore di puntatori a puntatori a … a valori; occupa molto più spazio, scambia indirezione per aritmetica, e non è amenable all'analisi [IntroCodeGeneration.pdf, slide "How does the compiler handle A[i,j]?"].
    
    Queste tre rappresentazioni hanno un comportamento di cache **distinto e diverso** [IntroCodeGeneration.pdf, slide "The Concept" / "Laying Out Arrays"].
    
- **Costo apparente e formule per due dimensioni (slide "Computing an Array Address" / "This stuff looks expensive!"):** per `A[i1,i2]`:
    
    - Row-major, due dimensioni: ${@}A + ((i_1-low_1)\times(high_2-low_2+1) + i_2-low_2) \times w$
    - Column-major, due dimensioni: ${@}A + ((i_2-low_2)\times(high_1-low_1+1) + i_1-low_1) \times w$
    - Indirection vectors, due dimensioni: `*(A[i1])[i2]`, dove `A[i1]` è a sua volta un riferimento ad array 1-D
    
    dove $w = \text{sizeof}(A[1,1])$ [IntroCodeGeneration.pdf, slide "Computing an Array Address"].
    
- **Ottimizzazione dell'indirizzo per `A[i,j]` in row-major (slide "Optimizing Address Calculation for A[i,j]"):** partendo da $${@}A + (i-low_1)\times(high_2-low_2+1)\times w + (j-low_2)\times w$$ si fattorizza in $${@}A + i\times(high_2-low_2+1)\times w + j\times w - (low_1\times(high_2-low_2+1)\times w) - (low_2\times w)$$ Se $low_i$, $high_i$ e $w$ sono noti, l'ultimo termine è una costante. Definendo $${@}A_0 = {@}A - (low_1\times(high_2-low_2+1)\times w) - (low_2\times w), \qquad len_2 = (high_2-low_2+1)$$ l'espressione dell'indirizzo diventa $${@}A_0 + (i\times len_2 + j)\times w$$ Se `@A` è noto, `@A0` è una costante nota, e $i \times len_2 + j$ è calcolabile con operazioni interamente a tempo di esecuzione ma su termini a costo ridotto [IntroCodeGeneration.pdf, slide "Optimizing Address Calculation for A[i,j]"].
    
- **Array come parametri attuali (slide "Array References"):** per array interi passati come parametri call-by-reference, serve l'informazione sulle dimensioni ⇒ si costruisce un **dope vector**; i suoi valori vengono memorizzati nella sequenza di chiamata; si passa l'indirizzo del dope vector nello slot del parametro; si genera il polinomio d'indirizzo completo a ogni riferimento. Miglioramenti possibili: scegliere il polinomio d'indirizzo basato sul false zero; pre-calcolare i termini fissi nella sequenza di prologo. Per il call-by-value: la maggior parte dei linguaggi passa gli array per riferimento — è una questione di design del linguaggio [IntroCodeGeneration.pdf, slide "Array References"]. Il **dope vector** stesso incorpora tipicamente i "false zero" già discussi, per rendere efficiente il calcolo dell'indirizzo anche quando i bound non sono noti a compile-time [IntroCodeGeneration.pdf, slide "The Dope vector"].
    
- **Range checking (slide "Range checking"):** un programma che referenzia elementi di array fuori dai limiti dichiarati non è ben formato. Alcuni linguaggi (come Java) richiedono che gli accessi fuori dai limiti siano rilevati e segnalati; in altri linguaggi i compilatori hanno incluso meccanismi per rilevare e segnalare questi accessi. Il modo semplice è introdurre un controllo a runtime che verifichi che il valore dell'indice cada nell'intervallo dell'array, usando l'informazione sui bound presente nel dope vector; alternativamente il compilatore dovrebbe dimostrare che un dato riferimento **non può** generare un accesso fuori dai limiti — **costoso!** [IntroCodeGeneration.pdf, slide "Range checking"].
    
- **Perché il calcolo degli indirizzi array conta così tanto (slide "Array Address Calculations"):** è una fonte primaria di overhead. Le applicazioni scientifiche fanno un uso estensivo di array e strutture array-like (algebra lineare computazionale, densa e sparsa); anche le applicazioni non scientifiche usano ampiamente gli array come rappresentazione di altre strutture dati (hash table, matrici di adiacenza, tabelle, strutture). I calcoli sugli array tendono a iterare su di essi: i loop eseguono più spesso del codice fuori dai loop, quindi i calcoli d'indirizzo array dentro i loop fanno una differenza enorme nell'efficienza di molte applicazioni compilate. Ridurre l'overhead del calcolo d'indirizzo array è stato un obiettivo primario dell'ottimizzazione fin dagli anni '50 [IntroCodeGeneration.pdf, slide "Array Address Calculations"].
    

### 10.7 Ottimizzazione degli Accessi Array nei Loop: LICM e Operator Strength Reduction

Esempio guida usato in tutta la sezione (slide "Example: Array Address Calculations in a Loop"), con `A`, `B` array conformabili floating-point in **column-major order**:

```fortran
DO J = 1, N
    A[I,J] = A[I,J] + B[I,J]
END DO
```

- **Versione naïve (slide "Example: Array Address Calculations in a Loop" #1):** l'indirizzo viene ricalcolato per intero **due volte** a ogni iterazione:
    
    ```text
    DO J = 1, N    
	    R1 = @A0 + (J × len1 + I) × w    
	    R2 = @B0 + (J × len1 + I) × w    
	    MEM(R1) = MEM(R1) + MEM(R2)
    END DO
    ```
    
    (`len1` = numero di righe, poiché siamo in column-major order) [IntroCodeGeneration.pdf, slide "Example: Array Address Calculations in a Loop" #1].
- **Loop-Invariant Code Motion (slide "Loop-invariant code motion"):** i calcoli comuni (quelli che non dipendono da `J`) vengono spostati **fuori** dal loop:
    
    ```text
    R1 = I × w
    c  = len1 × w  ! costante a tempo di compilazione
    R2 = @A0 + R1
    R3 = @B0 + R1
    DO J = 1, N
	    a  = J × c    
	    R4 = R2 + a    
	    R5 = R3 + a    
	    MEM(R4) = MEM(R4) + MEM(R5)
    END DO
    ```
    
    [IntroCodeGeneration.pdf, slide "Loop-invariant code motion"].
- **Operator Strength Reduction (§10.4.2 in EaC, slide "Operator Strength Reduction"):** la moltiplicazione `J × c` all'interno del loop viene convertita in una somma incrementale — `J` diventa a questo punto pura contabilità (_bookkeeping_):
    
    ```text
    R1 = I × w
    c  = len1 × w    ! costante a tempo di compilazione
    R2 = @A0 + R1
    R3 = @B0 + R1
    DO J = 1, N    
	    R2 = R2 + c    
	    R3 = R3 + c    
	    MEM(R2) = MEM(R2) + MEM(R3)
    END DO
    ```
    
    Da 2 calcoli d'indirizzo completi per iterazione (versione naïve, con moltiplicazioni) si arriva a due semplici addizioni per iterazione — una trasformazione progressiva che illustra concretamente come LICM e strength reduction cooperino per eliminare overhead ridondante dagli accessi array in loop [IntroCodeGeneration.pdf, slide "Operator Strength Reduction (§ 10.4.2 in EaC)"].

### 10.8 Rappresentazione e Manipolazione delle Stringhe

- **Le stringhe come caso a parte (slide "Representing and Manipulating Strings" #1):** le stringhe di caratteri differiscono da scalari, array e strutture; il supporto linguistico varia: in C la maggior parte delle manipolazioni avviene tramite chiamate a routine di libreria; altri linguaggi forniscono meccanismi di prima classe per specificare sottostringhe o concatenarle. L'unità fondamentale è il carattere — tipicamente 1 o 2 byte — e l'ISA target può (o non può) supportare operazioni a grana carattere. Le operazioni su stringa possono essere costose: le vecchie architetture CISC fornivano supporto esteso per la manipolazione di stringhe; le architetture RISC moderne si affidano al compilatore per codificare queste operazioni complesse usando un insieme di operazioni più semplici [IntroCodeGeneration.pdf, slide "Representing and Manipulating Strings" #1].
    
- **Due rappresentazioni comuni (slide "Representing and Manipulating Strings" #2):** per la stringa `"a string"`:
    
    - **Campo di lunghezza esplicito:** un intero che precede i dati contiene la lunghezza (il campo lunghezza può occupare più spazio del terminatore).
    - **Terminazione nulla:** un carattere speciale (`\0`) segna la fine della stringa.
    
    È una questione di design del linguaggio. Ciascuna rappresentazione ha vantaggi e svantaggi propri; sfortunatamente, la terminazione nulla è quasi considerata la norma — un retaggio del design di C, ormai radicato nei design di sistemi operativi e API [IntroCodeGeneration.pdf, slide "Representing and Manipulating Strings" #2, #3].
    
- **Assegnamento di un singolo carattere (slide "Manipulating Strings" #1):**
    
    - _Con operazioni a livello di carattere:_ si calcola l'indirizzo del rhs e si carica il carattere; si calcola l'indirizzo del lhs e si memorizza il carattere.
    - _Con sole operazioni a livello di parola_ (>1 carattere per parola): si calcola l'indirizzo della parola contenente il rhs e la si carica; si sposta il carattere nella posizione di destinazione all'interno della parola; si calcola l'indirizzo della parola contenente il lhs e la si carica; si maschera fuori il carattere corrente e si maschera dentro il nuovo carattere; si memorizza indietro la parola del lhs [IntroCodeGeneration.pdf, slide "Manipulating Strings" #1] (esempio: `a[1]=b[2]`).
- **Assegnamento multi-carattere (slide "Manipulating Strings" #2):** due strategie: (1) avvolgere un loop attorno al codice per un singolo carattere; oppure (2) lavorare fino a un caso allineato-a-parola, ripetere spostamenti di parole intere, e gestire un eventuale caso finale a parola parziale — con operazioni a livello di carattere o con sole operazioni a livello di parola [IntroCodeGeneration.pdf, slide "Manipulating Strings" #2].
    
- **Concatenazione (slide "Manipulating Strings" #3):** la concatenazione di stringhe è un calcolo di lunghezza seguito da una coppia di assegnamenti dell'intera stringa — tocca ogni carattere; possono esserci problemi di lunghezza (overflow del buffer di destinazione) [IntroCodeGeneration.pdf, slide "Manipulating Strings" #3].
    
- **Calcolo della lunghezza (slide "Manipulating Strings" #4):** la rappresentazione scelta determina il costo del calcolo della lunghezza (immediato con campo esplicito, lineare con terminazione nulla). Il calcolo della lunghezza emerge anche in altri contesti: assegnamento di stringa intera o sottostringa; assegnamento controllato (per prevenire buffer overflow); concatenazione; valutazione di un parametro attuale call-by-value [IntroCodeGeneration.pdf, slide "Manipulating Strings" #4].
    

### 10.9 Valori Booleani e Relazionali

- **Come rappresentarli (slide "Boolean & Relational Values" #1):** l'implementazione di espressioni booleane, relazionali e dei costrutti di controllo di flusso varia ampiamente con l'ISA. La risposta dipende dalla macchina target. Due approcci classici: **rappresentazione numerica (esplicita)** e **rappresentazione posizionale (implicita)**. La scelta migliore dipende sia dal contesto sia dall'ISA — alcuni casi funzionano meglio con la prima rappresentazione, altri con la seconda [IntroCodeGeneration.pdf, slide "Boolean & Relational Values" #1].
- **Grammatica per riconoscere espressioni booleane e relazionali (slide "Boolean & Relational Expressions"):**
    
    ```
	Expr     → Expr ∨ AndTerm
	         | AndTerm
	
	AndTerm  → AndTerm ∧ RelExpr
	         | RelExpr
	
	RelExpr  → RelExpr < NumExpr
	         | RelExpr ≤ NumExpr
	         | RelExpr = NumExpr
	         | RelExpr ≠ NumExpr
	         | RelExpr ≥ NumExpr
	         | RelExpr > NumExpr
	         | NumExpr
	
	NumExpr  → NumExpr + Term
	         | NumExpr - Term
	         | Term
	
	Term     → Term × Value
	         | Term ÷ Value
	         | Value
	
	Value    → ¬ Factor
	         | Factor
	
	Factor   → ( Expr )
	         | number
    ```
    
    [IntroCodeGeneration.pdf, slide "Boolean & Relational Expressions"].
- **Rappresentazione numerica (slide "Boolean & Relational Values" #2):** si assegnano valori numerici a TRUE e FALSE; si usano le operazioni hardware AND, OR e NOT; si usa un confronto per ottenere un booleano da una relazionale. Se la macchina target supporta operazioni booleane che calcolano il risultato booleano direttamente: `cmp_LT rx,ry → r1` con `r1=True` se `rx<ry`, `r1=False` altrimenti [IntroCodeGeneration.pdf, slide "Boolean & Relational Values" #2].
- **Condition code (slide "Boolean & Relational Values" #3):** se la macchina target usa un condition code invece di operazioni booleane come `cmp_LT`, occorre usare un branch condizionale per interpretare il risultato del confronto. Se la macchina target calcola un codice risultato del confronto e serve memorizzare il risultato dell'operazione booleana:
    
    ```iloc
    cmp r1,r2 ⇒ cc     ; imposta cc col codice per LT,LE,EQ,GE,GT,NE
    cbr_LT cc l2,l3    ; PC=l2 se cc=LT, PC=l3 altrimenti
    ```
    
    [IntroCodeGeneration.pdf, slide "Boolean & Relational Values" #3].
	- **Rappresentazione posizionale (slide "Boolean & Relational Values" #4):** l'esempio precedente in realtà codifica il risultato nel condition code stesso (`cc`, o `r2` in altre varianti). Se il risultato viene usato per controllare un'operazione, potrebbe non essere necessario scriverlo esplicitamente da nessuna parte — questa è precisamente la **codifica posizionale** [IntroCodeGeneration.pdf, slide "Boolean & Relational Values" #4].
	  ![[Pasted image 20260908181708.png]]
	  
- **Variazioni architetturali — conditional move e predicazione (slide "Other Architectural Variations"):** entrambe le tecniche semplificano il codice evitando i branch:
    ![[Pasted image 20260908181836.png]]
    
    Entrambe le versioni evitano i branch; entrambe sono più corte del codice con condition code o confronto booleano. **Sono equivalenti al codice iniziale? Non sempre!** Sono migliori? Dipende: conta la dimensione del codice o il tempo di esecuzione? [IntroCodeGeneration.pdf, slide "Other Architectural Variations"].
- **Esempio comparativo — `x ← a<b ∧ c<d` (slide "Boolean & Relational Values" #5, #6):** 
  
  ![[Pasted image 20260908182000.png|455]]
  
  qui il confronto booleano produce codice molto migliore rispetto al condition code [IntroCodeGeneration.pdf, slide "Boolean & Relational Values" #5]; anche il conditional move aiuta in questo caso, ma risulta **peggiore** del confronto booleano puro. **Il succo:** contesto e hardware determinano la scelta appropriata — non esiste una tecnica universalmente migliore [IntroCodeGeneration.pdf, slide "Boolean & Relational Values" #6].

### 10.10 Generazione del Codice per il Controllo di Flusso

- **If-then-else (slide "Control Flow" #1):** si segue il modello di valutazione di relazionali e booleani con i branch. **Branching contro predicazione:**
    - _Frequenza di esecuzione:_ una distribuzione ineguale tra i rami ⇒ conviene fare il necessario per velocizzare il caso comune (favorendo il branching).
    - _Quantità di codice in ciascun ramo:_ quantità ineguali significano che la predicazione può sprecare issue slot.
    - _Flusso di controllo interno al costrutto:_ qualunque attività di branching dentro il costrutto complica i predicati e rende i branch più attraenti [IntroCodeGeneration.pdf, slide "Control Flow" #1].
- **Short-circuit evaluation (slide "Short-circuit Evaluation"):** ottimizza la valutazione di espressioni booleane (valutazione lazy) — una volta determinato il valore, si salta il resto della valutazione. Per `if (x or y and z) then …`: se `x` è vero, non serve valutare `y` o `z` — si salta direttamente alla clausola "then". Su un PDP-11 o un VAX, lo short-circuiting risparmiava tempo; le architetture moderne possono favorire la valutazione dell'espressione completa, poiché le crescenti latenze di branch rendono costoso il percorso a corto circuito, mentre conditional move e predicazione possono rendere più economico il percorso completo. **Passato:** i compilatori analizzavano il codice per inserire corti circuiti. **Futuro:** i compilatori analizzano il codice per dimostrare la legalità della valutazione completa laddove il linguaggio specifica uno short-circuit [IntroCodeGeneration.pdf, slide "Short-circuit Evaluation"].
- **Loop (slide "Control Flow" #2 / "Implementing Loops"):** si valuta la condizione prima del loop (se necessario — **pre-test**); si esegue il corpo del loop; si valuta la condizione dopo il loop (**post-test**); si effettua un branch di ritorno alla cima (se necessario). `while`, `for`, `do` e `until` si adattano tutti a questo modello base: Pre-test → Loop body → Post-test → Next block [IntroCodeGeneration.pdf, slide "Control Flow" #2]. Esempio concreto per `for (i=1; i<100; i++) { loop body }`: si genera un blocco di inizializzazione, un pre-test, il corpo, e il salto di ritorno al pre-test, seguito dallo statement successivo [IntroCodeGeneration.pdf, slide "Implementing Loops"].
  
  ![[Pasted image 20260908182313.png|443]]

### 10.11 Case (Switch) Statements: le Tre Strategie di Ricerca

- **Il modello concettuale a 4 parti (slide "Case (switch) Statements" / "Case Statements"):**
    
    1. Valutare l'espressione di controllo.
    2. Effettuare il branch verso il case selezionato.
    3. Eseguire il codice per quel case.
    4. Effettuare il branch verso lo statement successivo al case (uso di `break`).
    
    Le parti 1, 3 e 4 sono ben comprese; **la parte 2 è la chiave**: serve un metodo efficiente per localizzare il codice designato. Molti compilatori forniscono diversi schemi di ricerca, ciascuno migliore in casi diversi [IntroCodeGeneration.pdf, slide "Case (switch) Statements" / "Case Statements"].
    
- **Le tre strategie (slide "Case Statements"):**
    
    1. **Linear Search:** costrutti if-then-else annidati (nested); adatta a un numero ridotto di case.
       - ![[Pasted image 20260908182404.png]]
    2. **Ricerca binaria:** si costruisce una tabella delle espressioni di case e la si cerca con ricerca binaria — richiede un insieme denso di condizioni.
       - ![[Pasted image 20260908182435.png]]
    1. **Calcolo diretto dell'indirizzo (jump table):** richiede un insieme di case denso; effettua il lookup dell'indirizzo in una tabella e vi salta direttamente — costo $O(1)$.
       - ![[Pasted image 20260908182507.png]]
    
    [IntroCodeGeneration.pdf, slide "Case Statements", "Linear Search", "Binary Search", "Direct Address Computation"]. Questa classificazione ricalca esattamente quella già introdotta come esempio guida in §10.2 (il case su un valore carattere), qui formalizzata nelle sue quattro fasi comuni e nelle tre tecniche di ricerca applicabili alla fase 2.
## CAPITOLO 11 — Allocazione dei Registri

**Fonti:** _RegisterAlloc1.pdf_ (Local Register Allocation), _RegisterAlloc2.pdf_ (Global Register Allocation via Graph Coloring)

---

### 11.0 Collocazione nel Back-End e complessità del problema

L'allocatore dei registri riceve in ingresso codice quasi completamente compilato — già scandito, parsato, verificato, ottimizzato e tradotto in codice macchina target, eventualmente già schedulato — e con un numero **teoricamente illimitato** di registri virtuali (o pseudo-registri); restituisce codice equivalente che utilizzi al più $k$ registri fisici, inserendo se necessario `load`/`store` di spill _(RegisterAlloc1, sezione "Register Allocation" / "Background issues")_.

**Proprietà critiche richieste a un allocatore** _(RegisterAlloc1, "Register Allocation")_:

1. Produrre codice **corretto** che usi non più di $k$ registri.
2. Minimizzare il lavoro aggiunto da `load`/`store` di spill.
3. Minimizzare lo spazio usato per i valori scaricati in memoria.
4. Operare in modo efficiente: $O(n)$, $O(n\log_2 n)$, al più $O(n^2)$ — **mai** $O(2^n)$.

⚠️ **Nota di notazione**: la letteratura sull'allocazione dei registri usa sistematicamente $k$ per indicare il numero di registri disponibili sulla macchina target.

#### Allocazione vs Assegnamento (distinzione formale)

_(RegisterAlloc1, "Allocation versus assignment")_

- **Allocazione (Allocation):** decidere **quali** valori risiedano in un registro in un dato punto del programma.
- **Assegnamento (Assignment):** scegliere **quale registro fisico specifico** usare per ciascun valore allocato.

Questa distinzione è spesso persa in letteratura, ma il compilatore deve eseguire entrambe le fasi.

#### Tabella di complessità computazionale

_(RegisterAlloc1, "Register Allocation" — riepilogo complessità)_

|             | **Allocazione**                                                                                                                                                            | **Assegnamento**                                                                                                 |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Locale**  | **O(n)** nel caso semplificato (un solo blocco, una sola dimensione dei registri, costo di spill uniforme); **NP-completo** nel caso generale con vincoli/costi aggiuntivi | **O(n)** con un solo tipo/dimensione di registro; **NP-completo** nel caso con più classi/dimensioni di registri |
| **Globale** | **NP-completo**, già con un solo registro; resta **NP-completo** anche con \(k\) registri                                                                                  | **NP-completo**                                                                                                  |
Una volta ridotta la domanda di registri (allocazione), l'assegnamento può essere risolto in tempo polinomiale su una macchina con un solo tipo di registro _(RegisterAlloc1, "Allocation vs. Assignment")_.

#### Register Classes

_(RegisterAlloc1, "Register Classes")_ Le architetture distinguono tipicamente più classi di registri: general purpose (interi e indirizzi), floating-point (singola/doppia precisione), e talvolta condition code, predicate register o branch target register.

- Se il compilatore usa classi distinte per dati di tipo diverso, può allocare ciascuna classe **indipendentemente**, semplificando il problema.
- Se le classi si sovrappongono (es. registri floating-point a singola e doppia precisione che condividono lo stesso banco fisico), l'allocazione deve trattarle insieme, aumentando la complessità.

#### Modelli di gestione della memoria

- **Register-to-register model:** l'Instruction Selection assume registri virtuali illimitati; il codice prodotto **non è legale** finché l'allocatore non lo riscrive con un numero finito di registri fisici, inserendo gli spill necessari.
- **Memory-to-memory model:** il codice è **già legale** prima dell'allocazione (tutti i valori risiedono in memoria); l'allocatore agisce come una passata di ottimizzazione che promuove temporaneamente variabili nei registri. Con questo modello l'allocatore ha meno conoscenza a disposizione, il che ne può limitare l'efficacia.

---

### 11.1 Allocazione Locale

#### 11.1.1 Basic Block e MAXLIVE

_(RegisterAlloc1, "Local Register Allocation")_

- **Definizione (Basic Block):** segmento di lunghezza massima di codice _straight-line_ (privo di diramazioni). Se un'istruzione del blocco esegue, eseguono tutte, ed eseguono in ordine totale — proprietà che rende i basic block il terreno più semplice e più forte su cui dimostrare risultati di ottimizzazione.
- "**Locale**" (in contrapposizione a _regionale_ o _globale_) significa che la trasformazione opera all'interno di un singolo basic block. L'allocazione locale produce un buon uso dei registri **dentro** il blocco, ma può generare inefficienze ai **confini tra blocchi**.
- **Live range locali = intervalli $[i,j]$** nel blocco: un valore è vivo dalla sua definizione all'ultimo uso; una seconda definizione apre un nuovo live range.
- **MAXLIVE** = massimo, su tutte le istruzioni del blocco, del numero di pseudo-registri simultaneamente vivi. Se $\text{MAXLIVE} \le k$, l'allocazione è diretta (nessuno spill necessario); se $\text{MAXLIVE} > k$, occorre riservare $F$ registri per lo spill (tipicamente $F=2$: uno per l'indirizzo, uno per il dato).
- I live set si calcolano **a ritroso** sul blocco: si parte da `live = ∅` e a ogni istruzione si rimuove il _target_ e si aggiungono gli _operandi_. In ILOC la freccia `⇒` separa usi da definizioni; **eccezione**: `store` **usa** tutti i propri operandi di registro (compreso quello a destra della freccia, che qui è un indirizzo, non una definizione).

**Esempio svolto (traccia completa da $a - (2b)$):**

```
loadI   1028    ⇒ r1    // {r1}
load    r1      ⇒ r2    // {r1 r2}
mult    r1, r2  ⇒ r3    // {r1 r2 r3}
load    x       ⇒ r4    // {r1 r2 r3 r4}  ← MAXLIVE = 4
sub     r4, r2  ⇒ r5    // {r1  r3  r5}
load    z       ⇒ r6    // {r1  r3  r5 r6}
mult    r5, r6  ⇒ r7    // {r1  r3      r7}
sub     r7, r3  ⇒ r8    // {r1          r8}
store   r8      ⇒ r1    // { }   (r1 è un USE, non una definizione)
```

Il codice usa deliberatamente `1028` sia come costante sia (indirettamente) come indirizzo per creare un live range lungo a fini pedagogici: l'allocatore non deve "capire" il calcolo, deve solo preservarlo.

#### 11.1.2 Allocatore Top-Down (frequency count)

_(RegisterAlloc1, "Top-down Allocator")_ **Idea:** i valori più usati devono risiedere in registro; si riservano $r$ registri per lo spilling.

**Algoritmo:**

1. Contare le occorrenze di ogni registro virtuale nel blocco.
2. Ordinare i registri in base al conteggio.
3. Allocare i primi $k-r$ valori (per frequenza) ai registri fisici.
4. Riscrivere il codice: i valori esclusi vengono spostati in memoria, inserendo `load`/`store` di spill.

**Esempio con $k=3$ (di cui 2 riservati per gli operandi, quindi si spilla 1 valore):** poiché `r1` compare più spesso di `r3`, si spilla `r3`:

```
loadI   1028    ⇒ r1
load    r1      ⇒ r2
mult    r1, r2  ⇒ r3
store   r3      ⇒ 16     // spill di r3
load    x       ⇒ r4
sub     r4, r2  ⇒ r5
load    z       ⇒ r6
mult    r5, r6  ⇒ r7
load    16      ⇒ r3     // restore di r3
sub     r7, r3  ⇒ r8
store   r8      ⇒ r1
```

`r3` diventa così **due live range minimi** che si sovrappongono a meno valori (al più 3 vivi in ogni punto). Il codice è più lento ma **corretto** su 3 registri — _correctness is a virtue_.

**Debolezza:** un registro fisico è dedicato a un virtuale per **l'intero blocco** — se un valore ha vita breve ma è ad alta priorità, "blocca" il registro anche quando non serve.

**Nota sul caso limite:** se $k - r < |\text{valori}| < k$, poiché il problema sottostante è NP-completo, l'allocatore può controllare esplicitamente questa situazione, adottare una strategia più complessa, oppure accettare l'approssimazione.

#### 11.1.3 Allocatore Bottom-Up (distance to next use)

_(RegisterAlloc1, "Bottom-up Allocator")_ **Idea:** _load on demand_; si concentra sulla sostituzione più che sull'allocazione a priori, e tratta tutti i valori in modo uniforme.

**Algoritmo (non ottimale):**

1. Iniziare con l'insieme dei registri vuoto.
2. Caricare i valori "su richiesta" (al momento dell'uso).
3. Quando non c'è un registro libero, liberarne uno: si spilla il valore il cui **prossimo uso è più lontano nel futuro**, preferendo i valori _clean_ (costanti o già in memoria, che non richiedono `store`) ai _dirty_ (che vanno riscritti).

**Esempio con $k=3$:** all'istruzione `load x ⇒ r4` tutti i registri sono occupati; il prossimo uso di `r1` (il `store` finale) è il più lontano ⇒ si spilla `r1`:

```
loadI   1028    ⇒ r1
load    r1      ⇒ r2
mult    r1, r2  ⇒ r3
store   r1      ⇒ 20     // spill di r1
load    x       ⇒ r4
sub     r4, r2  ⇒ r5
load    z       ⇒ r6
mult    r5, r6  ⇒ r7
sub     r7, r3  ⇒ r8
load    20      ⇒ r1     // restore di r1
store   r8      ⇒ r1
```

Anche qui al più 3 valori sono vivi in ogni punto.

#### 11.1.4 Dal locale al regionale: perché serve l'allocazione globale

_(RegisterAlloc1, "From local algorithms to regional algorithms")_ Estendere gli algoritmi locali al caso regionale/globale può essere difficile. Esempio: se un blocco $B_1$ definisce `x ← r1` e un blocco $B_3$ definisce `x ← r3`, e i blocchi successori $B_2$ ($r2 ← x$) e $B_4$ ($r4 ← x$) confluiscono su percorsi diversi, non esiste in generale un assegnamento di registri coerente su tutti i cammini: per l'arco $B_1 \to B_4$ si potrebbe sostituire il load con una semplice `move` (`r4 ← r1`), ma nessuna possibilità esiste per l'arco "incrociato" $B_3 \to B_2$ con lo stesso registro. **L'unica soluzione corretta in generale è scaricare `x` in memoria alla fine di entrambi i blocchi predecessori** — ciò motiva il passaggio a un'allocazione globale che ragioni sull'intero grafo di flusso.

---

### 11.2 Allocazione Globale: cosa la rende difficile

_(RegisterAlloc2, "What Makes Global Register Allocation Hard?")_ Un caso apparentemente semplice — `store r4 ⇒ x` seguito da `load x ⇒ r1` nello stesso blocco — è in realtà un problema di **assegnamento**, non di allocazione: se `x` fosse tenuto nel registro giusto, si potrebbe sostituire la coppia store-load con una `move`. Il problema diventa "duro" quando:

- un blocco ha **più predecessori** nel CFG (es. `store r4 ⇒ x` in un ramo, `store r5 ⇒ x` in un altro, `load x ⇒ r1` nel blocco successore): bisogna garantire che i valori giusti siano nei registri giusti in **ciascun** predecessore;
- in presenza di **cicli**, un blocco può essere predecessore di sé stesso, aggiungendo ulteriori vincoli.

L'approccio globale abbandona la distinzione locale/regionale e adotta uno schema sistematico che approssima una buona allocazione su tutta la procedura. A differenza del caso locale — dove ogni riferimento esegue esattamente una volta per esecuzione del blocco, e il costo di uno spill è quindi uniforme — nel caso globale **il costo di uno spill dipende da dove avviene**: gli allocatori globali annotano ogni riferimento con una frequenza di esecuzione stimata, derivata da analisi statica (es. euristiche su cicli) o da dati di profiling.

#### 11.2.1 Digressione: colorazione di grafi

_(RegisterAlloc2, "Graph Coloring (A Background Digression)")_ **Definizione (k-colorabilità):** un grafo $G$ è **k-colorabile** se e solo se i suoi nodi possono essere etichettati con interi $1,\dots,k$ in modo che nessun arco di $G$ connetta due nodi con la stessa etichetta. Ogni colore può essere mappato su un registro fisico distinto.

#### 11.2.2 Grafo di Interferenza

_(RegisterAlloc2, "Building the Interference Graph")_

- **Definizione (Interferenza):** due valori **interferiscono** se esiste un'operazione in cui entrambi sono simultaneamente vivi. Se $x$ e $y$ interferiscono, non possono occupare lo stesso registro.
- **Grafo di Interferenza** $G_I = (N_I, E_I)$: i nodi rappresentano _live range_ (valori); un arco $\langle x,y\rangle \in E_I$ esiste se e solo se $x$ e $y$ interferiscono.
- Una $k$-colorazione di $G_I$ corrisponde esattamente a un'allocazione su $k$ registri.
- A differenza del caso locale (dove il grafo d'interferenza è un grafo d'intervalli), nel caso globale $G_I$ **non** è un grafo d'intervalli, e calcolare LIVE è più complesso.

**Costruzione del grafo (procedura in 3 punti):**

![[Pasted image 20260908184548.png|493]]

1. **Scoprire i live range:**
    - Costruire la forma **SSA** della procedura.
    - A ogni $\phi$-function, unire gli argomenti in un unico live range (gli argomenti della stessa $\phi$-function devono essere fusi insieme).
    - Rinominare il codice in termini di questi nuovi live range.
2. **Calcolare gli insiemi LIVE sui live range**, per ciascun blocco, risolvendo un sistema di equazioni a punto fisso: $$LV_\bullet(l) = \bigcup { LV_o(l') \mid l' \in post(l) }$$ $$LV_o(l) = (LV_\bullet(l) \setminus def(B)) \cup use(B)$$ dove $LV_o(l)$ sono le variabili vive **prima** del blocco $l$, e $LV_\bullet(l)$ le variabili vive **all'uscita** di $l$; $def([x{:=}a]^l)={x}$, $use([x{:=}a]^l)=FV(a)$ (le variabili libere di $a$).
3. **Costruire il grafo con una scansione lineare all'indietro di ogni blocco:** per ogni live range $LR_i$ si crea un nodo $n_i$; per ogni blocco $b$, si inizializza `LiveNow ← LiveOut(b)`, e per ogni operazione $op_i: LR_a, LR_b \Rightarrow LR_c$ (in ordine **inverso**, da $op_n$ a $op_1$): si aggiunge l'arco $(LR_c, LR_i)$ per ogni $LR_i \in \text{LiveNow}$; si rimuove $LR_c$ da LiveNow; si aggiungono $LR_a$ e $LR_b$ a LiveNow.

**Esempio svolto:** CFG con $B_0 \to {B_1, B_2} \to B_3$, in cui:

- $B_0$: `LR_a ← …`
- $B_1$: `LR_b ← …; … ← LR_b; LR_d ← …`
- $B_2$: `LR_c ← …; …; LR_d ← LR_c`
- $B_3$: `… ← LR_a; … ← LR_d`

Propagando LiveOut all'indietro: $\text{LiveOut}(B_1) = \text{LiveOut}(B_2) = {LR_a, LR_d}$, $\text{LiveOut}(B_0) = {LR_a}$. Scansionando ogni blocco in ordine inverso e aggiungendo archi come sopra, si ottiene il grafo di interferenza con archi $\langle LR_a, LR_d\rangle$, $\langle LR_a, LR_b\rangle$, $\langle LR_a, LR_c\rangle$ (nessun arco tra $LR_b$ e $LR_c$, che non sono mai vivi insieme).

#### 11.2.3 Stima del costo di spill

_(RegisterAlloc2, "Account for Execution Frequency")_ Il compilatore annota ogni blocco con un conteggio di esecuzione stimato, derivato da dati di profiling o da euristiche fisse (es.: un ciclo esegue convenzionalmente 10 volte; un `if-then-else` imprevedibile divide per 2 la frequenza a ogni ramo). Il costo di spillare un singolo riferimento è dato dal costo dell'operazione di indirizzo più l'operazione di memoria, moltiplicato per la frequenza stimata del blocco; per ogni live range si somma il costo di tutti i suoi riferimenti.

---

### 11.3 La Pipeline di Chaitin e di Chaitin-Briggs

⚠️ **Attenzione:** l'algoritmo di **Chaitin** (1981/82) e la sua estensione di **Chaitin-Briggs** (1989) sono **due varianti distinte** dello stesso schema, che differiscono in un punto cruciale (fase di Simplify/Spill). Vengono qui presentate separatamente.

#### 11.3.1 Le 5 fasi comuni della pipeline

1. **Build:** costruisce il CFG, esegue l'analisi di liveness (via SSA come descritto in 11.2.2) e costruisce il grafo di interferenza $G_I$.
2. **Coalesce:** elimina le copie non necessarie (`x ← y`) fondendo i nodi di $x$ e $y$ se non interferiscono (dettagli in 11.5).
3. **Spill Cost:** stima il costo di spill di ciascun nodo, pesando maggiormente i riferimenti nei cicli annidati (11.2.3).
4. **Simplify / Select:** — qui **Chaitin** e **Chaitin-Briggs** si differenziano, vedi sotto.

#### 11.3.2 Algoritmo di Chaitin (1981)

_(RegisterAlloc2, "Chaitin's Algorithm")_

1. **Finché** esistono vertici con grado $< k$ in $G_I$: scegliere un vertice $n$ con $n° < k$, metterlo sullo stack, e rimuoverlo (con i suoi archi) da $G_I$. Questo abbassa il grado dei vicini di $n$.
2. **Se** $G_I$ è non vuoto (tutti i vertici rimasti hanno grado $\ge k$): scegliere un vertice $n$ (con un'euristica di costo) e **spillare immediatamente** il live range associato a $n$; rimuoverlo da $G_I$ e metterlo nella "spill list". Se questo fa scendere qualche vertice sotto grado $k$, tornare al passo 1; altrimenti ripetere il passo 2.
3. Se la spill list non è vuota: inserire il codice di spill, **ricostruire** il grafo di interferenza e ritentare l'allocazione da capo.
4. Altrimenti: estrarre successivamente i vertici dallo stack e colorarli con il colore più basso non usato da alcun vicino.

**Limite:** un nodo destinato allo spill viene scartato **subito** dal grafo, senza mai tentare di colorarlo — anche se in fase di _select_ un colore sarebbe potuto essere disponibile.

#### 11.3.3 Algoritmo di Chaitin-Briggs (1989) — Spill Ottimistico

_(RegisterAlloc2, "Chaitin-Briggs Algorithm")_ **Osservazione chiave (Briggs):** il grado è solo un **limite superiore lasco** sulla colorabilità — un nodo può avere $k+2$ vicini che usano complessivamente meno di $k$ colori, quindi essere colorabile comunque.

1. **Finché** esistono vertici con grado $< k$ in $G_I$: push sullo stack e rimozione, come in Chaitin.
2. **Se** $G_I$ è non vuoto: scegliere un vertice $n$ (euristica di costo/grado), ma invece di spillarlo subito **spingerlo comunque sullo stack** e rimuoverlo da $G_I$ ("spill ottimistico"). Se questo abbassa qualche grado sotto $k$, tornare al passo 1; altrimenti ripetere il passo 2.
3. Estrarre i vertici dallo stack in ordine e colorarli col colore più basso libero. **Se** un nodo (anche uno spinto come candidato spill) non trova colore disponibile: **solo allora** si sceglie un vertice non colorato da spillare realmente, si inserisce il codice di spill e si riparte dal passo 1.

**Differenza cruciale con Chaitin:** il candidato allo spill non viene scartato a priori — viene comunque colorato se possibile al momento del pop dallo stack.

#### 11.3.4 Esempi svolti

![[Pasted image 20260908185323.png]]

**(a) Chaitin, $k=3$.** Grafo su ${1,\dots,5}$ con archi ${1\text{-}2, 1\text{-}3, 2\text{-}4, 2\text{-}5, 3\text{-}4, 3\text{-}5, 4\text{-}5}$; gradi: $1{:}2$, $2{:}3$, $3{:}3$, $4{:}3$, $5{:}3$ — solo il nodo 1 ha grado $<3$.

1. push 1 (grado $2<3$); la rimozione abbassa a 2 i gradi di 2 e 3.
2. push 2; ora **tutti** i rimanenti hanno grado $<3$.
3. push 4, push 3; resta solo 5 (grado 0) ⇒ push 5.
4. pop 5 → colore 1; pop 3 (vicini 1,4,5: solo 5 colorato) → colore 2; pop 4 (vicini 2,3,5: colori 1,2 usati) → colore 3; pop 2 → colore 2; pop 1 → colore 1.

Colorazione valida su 3 registri, **senza alcuno spill**.

![[Pasted image 20260908185446.png]]

**(b) Briggs — optimistic coloring, $k=2$.** Grafo a diamante: archi $1\text{-}2, 2\text{-}4, 4\text{-}3, 3\text{-}1$; **tutti** i nodi hanno grado esattamente 2 ⇒ nessun nodo con grado $<2$: **Chaitin spillerebbe immediatamente** un nodo qualsiasi. Briggs pusha comunque un nodo, diciamo 1; la rimozione porta 2 e 3 a grado 1; push 3; ora 2 e 4 hanno grado $<2$; push 2, push 4. In fase di select: pop 4 → colore 1; pop 2 → colore 2; pop 3 → colore 2 (il vicino 4 ha colore 1); pop 1 → i vicini 2 e 3 usano entrambi colore 2 ⇒ **il colore 1 è disponibile!** 2-colorazione trovata, **zero spill**: proprio il caso che dimostra come il grado sia solo un limite superiore lasco.

---

### 11.4 Allocazione Globale Top-Down

_(RegisterAlloc2, "Top-Down Coloring")_ Approccio alternativo a Chaitin-Briggs (bottom-up):

1. Assegnare a ogni live range un rango basato sul risparmio di tempo di esecuzione stimato (analogo al costo di spill).
2. Separare i live range in **constrained** (con $\ge k$ vicini in $G_I$) e **unconstrained** (con $<k$ vicini).
3. Colorare per primi i live range _constrained_, in ordine di rango decrescente; poi gli _unconstrained_ (che, rimossi i precedenti, spesso "diventano" a loro volta non vincolati).

**Gestione degli spill:** se il top-down incontra un live range non colorabile, lo spilla — poiché tutti i live range già colorati avevano rango superiore, si spilla sempre il nodo corrente, evitando così i costi di un backtracking completo; il compilatore potrebbe in linea di principio "decolorare" scelte precedenti, ma per evitarne il costo tipicamente non lo fa.

Non esiste un modo chiaro per stabilire a priori se l'approccio top-down o quello bottom-up (Chaitin-Briggs) produca risultati migliori su un dato programma.

---

### 11.5 Coalescing delle copie

_(RegisterAlloc2, "Coalescing Copies I/II/III", "Safe Coalescing")_ Per una copia `i2i LR1 ⇒ LR2`, se $\langle LR_1, LR_2\rangle \notin E_I$ (sorgente e destinazione **non interferiscono mai** — proprietà sempre vera per una pura copia, anche se i loro live range si sovrappongono nel tempo), si possono fondere i due live range in un unico nodo $LR_{ab}$ ed **eliminare l'operazione di copia**.

**Vantaggi:**

- elimina l'istruzione di copia;
- riduce il grado di ogni live range che interferiva con **entrambi** $LR_a$ e $LR_b$ (poiché ora conta come un solo vicino anziché due).

⚠️ **Precisazione (correzione rispetto alla versione precedente del capitolo):** il grado del nodo fuso $LR_{ab}$ **non** è in generale la somma $deg(LR_a)+deg(LR_b)$: fondere due live range **non può aumentare** il grado dei loro vicini comuni (un vicino che interferiva con entrambi ora ha un solo arco verso $LR_{ab}$ anziché due). Tuttavia il grado di $LR_{ab}$ stesso può comunque **crescere** rispetto a $\max(deg(LR_a), deg(LR_b))$, perché somma i vicini _distinti_ di $LR_a$ e $LR_b$: il grafo risultante può quindi diventare più difficile da colorare. Inoltre l'**ordine** di coalescenza conta — fondere due live range può precludere altre fusioni potenzialmente più vantaggiose.

**Coalescing sicuro (_safe coalescing_):** l'allocatore scandisce ogni blocco ed esamina ogni operazione di copia `i2i LR1 ⇒ LR2`; se $LR_1$ e $LR_2$ non interferiscono, li combina, elimina la copia e aggiorna il grafo di interferenza. Sono state sviluppate diverse euristiche per decidere quando il coalescing è "sicuro", cioè quando è garantito che non trasformi un grafo $k$-colorabile in uno che non lo è; con tali euristiche è possibile alternare passi di _simplify_ e passi di _safe coalescing_, eliminando molte operazioni di move superflue.

---

### 11.6 Pipeline completa (Chaitin-Briggs, bottom-up)

_(RegisterAlloc2, "Chaitin-Briggs Allocator (Bottom-up Coloring)")_

```
renumber   →  Costruisce SSA, calcola i live range, rinomina
build      →  Costruisce il grafo di interferenza
coalesce   →  Elimina copie superflue: LRx→LRy, ⟨LRx,LRy⟩∉GI ⇒ fondi LRx e LRy
spillcosts →  Stima il costo di spill di ogni live range
simplify   →  while N non vuoto:
                 if ∃ n con n° < k: push n sullo stack
                 else: scegli n da (eventualmente) spillare, push n, rimuovi n da GI
select     →  while stack non vuoto:
                 pop n, inserisci n in GI, prova a colorarlo
                 se non colorabile → spill
spill      →  Inserisce load/store per le definizioni e gli usi non colorati,
              poi ricomincia dal punto "build"
```

**Punti di forza e debolezze del Chaitin-Briggs (bottom-up globale):**

- ✅ grafo di interferenza preciso; forte meccanismo di coalescing; buona gestione dell'assegnamento; esecuzione ragionevolmente rapida.
- ❌ tende a "sovra-spillare" nei casi difficili; il grafo di interferenza non ha "geografia" (non distingue _dove_ nel programma un nodo è vivo); quando spilla un live range, lo spilla **ovunque** nel programma, anche dove non servirebbe.

Ulteriori miglioramenti sono possibili ma con ritorni via via più marginali.

---

### 11.7 Allocazione Globale Approssimata: Linear Scan

_(RegisterAlloc2, "Linear Scan Allocation")_ Gli allocatori basati su colorazione sono spesso considerati troppo costosi per ambienti **JIT**, dove la compilazione avviene a runtime. Il _linear scan_ usa un grafo di interferenza **approssimato** e una variante dell'algoritmo locale bottom-up.

- **Definizione (Live Interval):** $[i,j]$ è l'intervallo di vita per la variabile $v$ se non esiste un'istruzione numerata $j' > j$ in cui $v$ è viva, e non esiste un'istruzione numerata $i' < i$ in cui $v$ è viva. È un'**approssimazione conservativa** del live range reale: possono esistere sotto-intervalli $[i,j]$ in cui $v$ non è effettivamente viva (l'intervallo la sovrastima). L'intervallo banale per qualunque variabile è $[1,N]$.
- Si considera la procedura come una **lista lineare** di operazioni; un live range diventa un intervallo $(x,y)$ su questa lista, il che sovrastima le vere interferenze.

**Algoritmo (pseudocodice):**

```
LinearScanRegisterAllocation
    active ← {}
    foreach live interval i, in order of increasing start point
        ExpireOldIntervals(i)
        if length(active) = R then
            SpillAtInterval(i)
        else
            register[i] ← a register removed from pool of free registers
            add i to active, sorted by increasing end point

ExpireOldIntervals(i)
    foreach interval j in active, in order of increasing end point
        if endpoint[j] ≥ startpoint[i] then
            return
        remove j from active
        add register[j] to pool of free registers

SpillAtInterval(i)
    spill ← last interval in active
    if endpoint[spill] > endpoint[i] then
        register[i] ← register[spill]
        location[spill] ← new stack location
        remove spill from active
        add i to active, sorted by increasing end point
    else
        location[i] ← new stack location
```

Gli intervalli di vita sono ordinati per punto di inizio crescente; la lista `active` contiene gli intervalli che si sovrappongono al punto corrente e hanno già un registro assegnato, ordinata per punto di fine crescente.

**Esempio svolto** (5 live range $a,b,c,d,e$, 2 registri $R1,R2$):

|Live ranges|a|b|c|d|e|
|---|---|---|---|---|---|
|**Allocazione**|R1|R2|_(spill)_|R1|R2|

Quando `c` inizia, sia `R1` (occupato da `a`) sia `R2` (occupato da `b`) sono attivi e nessuno dei due termina prima: `c` viene **spillato**. Successivamente, alla scadenza di `a` e `b`, i registri si liberano per `d` ed `e`.

**Confronto:** l'algoritmo è rapido e produce allocazioni ragionevoli, ma — essendo basato su un grafo approssimato — è meno preciso di Chaitin-Briggs e può sovra-spillare rispetto a un'analisi di liveness esatta.

---

### 11.8 Approccio Ibrido

_(RegisterAlloc2, "Hybrid Approach?")_ **Osservazione:** molte procedure sono piccole e non generano mai spill; poche procedure sono effettivamente difficili da allocare.

**Possibile strategia:**

1. Provare prima il **linear scan** (economico, spesso sufficiente).
2. Se il linear scan genera spill, ricorrere a un allocatore _heavyweight_ (Chaitin-Briggs, basato su SSA, o altro), usando l'algoritmo costoso solo quando quello economico fallisce.

Questo non velocizza la compilazione nel caso complesso, ma può compensare sulla maggioranza delle compilazioni semplici. (Nota storica: il compilatore server di Sun HotSpot utilizza un allocatore Chaitin-Briggs completo.)

---

### 11.9 Static Single Assignment (SSA) e Register Allocation

- **Principio cardine:** in forma SSA ogni variabile è **definita esattamente una volta** nel testo del programma; ogni nome si riferisce alla variabile in un punto specifico del programma, ed SSA codifica sia il flusso di controllo sia il flusso dei valori.
- **$\phi$-functions:** nei punti di confluenza (join) del CFG in cui percorsi diversi portano definizioni diverse per la stessa variabile originaria, si inserisce una funzione $x_3 \leftarrow \phi(x_1, x_2)$ che seleziona il valore corretto in base al cammino di provenienza effettivo a runtime.

**Esempio (ciclo `while`):**

```
Originale                       Forma SSA
x ← …                           x0 ← …
y ← …                           y0 ← …
while (x < k)                   if (x0 >= k) goto next
    x ← x + 1                   loop: x1 ← φ(x0,x2)
    y ← y + x                          y1 ← φ(y0,y2)
                                       x2 ← x1 + 1
                                       y2 ← y1 + x2
                                 if (x2 < k) goto loop
                                 next: …
```

La forma SSA è il prerequisito per la costruzione precisa dei live range descritta in 11.2.2 (unione degli argomenti delle $\phi$-function), e semplifica molte analisi di ottimizzazione (value numbering globale, propagazione di costanti), riducendo di conseguenza la complessità pratica dell'allocazione dei registri.

---

### 11.10 Riepilogo dei conflitti/edge case del capitolo

| Situazione                                                                          | Conseguenza                                                                                 | Soluzione                                                                                                                                 |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| $\text{MAXLIVE} > k$ nel caso locale                                                | servono $F$ registri riservati                                                              | spill (top-down: per frequenza; bottom-up: per distanza al prossimo uso)                                                                  |
| valore vivo all'uscita di più blocchi predecessori con un solo registro disponibile | nessun assegnamento locale coerente su tutti i cammini                                      | store di `x` alla fine di **tutti** i predecessori coinvolti (motiva l'allocazione globale)                                               |
| nodo con grado $\ge k$ in fase di simplify (Chaitin)                                | spill immediato, nessuna possibilità di colorare in seguito                                 | —                                                                                                                                           |
| nodo con grado $\ge k$ in fase di simplify (Chaitin-Briggs)                         | push ottimistico sullo stack                                                                | può comunque ricevere un colore al pop, se i vicini usano $<k$ colori                                                                     |
| coalescing di due live range che condividono vicini                                 | il grado dei vicini comuni **non aumenta**                                                  | il grado del nodo fuso può comunque crescere e rendere il grafo più difficile da colorare → si richiedono euristiche di _safe coalescing_ |
| linear scan: intervallo che si sovrappone a tutti i registri attivi                 | spill del live range con fine più lontana tra quelli attivi (o del nuovo, se termina prima) | `SpillAtInterval`                                                                                                                           |

<a id="cap12"></a>
## CAPITOLO 12: Monografia rustc (L'Architettura del Compilatore Rust)
**Sources:** *COMP-01...06-RUST_COMPILATION.pdf*

> Capitolo di ripasso estratto dalla dispensa di Compilation Techniques (0073A), per la preparazione dell'esame sulla parte Rust del corso.

### 12.1 Storia, Motivazioni e Sistema Demand-Driven

*   **Breve storia (slide):** lo sviluppo di Rust iniziò nel 2006 a opera di Graydon Hoare presso Mozilla. Nel 2010 si passò dal compilatore iniziale scritto in OCaml a un compilatore **self-hosting** scritto in Rust stesso, `rustc`, che riuscì a compilare se stesso nel 2011. Il **bootstrapping** viene tuttora usato per generare le nuove versioni del compilatore; `rustc` usa **LLVM** come back-end [COMP-01_RUST_COMPILATION.pdf, Slide 3].
*   **Obiettivi e sintassi di Rust (slide):** Rust è un linguaggio di programmazione di sistema general-purpose focalizzato sulla sicurezza (in particolare sulla concorrenza sicura), che supporta sia il paradigma funzionale sia quello imperativo. L'obiettivo principale è garantire sicurezza **senza penalizzare l'efficienza**. La sintassi concreta è simile a C/C++ (blocchi, if-else, while, for), con `match` per il pattern matching; quasi ogni parte del corpo di una funzione è un'espressione (incluso `if-else`); non richiede alcun runtime (garbage collector, tipizzazione/binding dinamici, …) e offre più controllo sull'allocazione/distruzione della memoria [COMP-01_RUST_COMPILATION.pdf, Slide 4].
*   **Panoramica delle garanzie (slide "Rust overview"):**
    *   *Prestazioni, come in C:* Rust compila in codice oggetto per prestazioni bare-metal.
    *   *Ma con sicurezza della memoria:* niente puntatori null, niente dangling pointer, niente double free, niente data race, niente iterator invalidation; accessi ad array fuori dai limiti non consentiti (una garanzia che C++26 introdurrà solo in seguito).
    *   *Con basso overhead:* le regole di sicurezza della memoria sono verificate perlopiù staticamente; l'astrazione di gestione della memoria è **a costo zero** (nessun garbage collector a runtime).
    *   *Tramite:* un sistema di tipi avanzato; i concetti di ownership, borrowing e lifetime per prevenire corruzioni di memoria (basati su RAII).
    *   *Ma a un costo:* un costo cognitivo per il programmatore, che deve ragionare più a fondo sulle regole d'uso di memoria e riferimenti mentre scrive il codice [COMP-01_RUST_COMPILATION.pdf, Slide 5].
*   **RAII (Resource Acquisition Is Initialization):** l'idioma per cui l'allocazione di una risorsa avviene durante l'inizializzazione dell'oggetto (nel costruttore), mentre il rilascio avviene durante la distruzione dell'oggetto (nel distruttore). Popolare nel C++ moderno: i piccoli oggetti si allocano preferibilmente sullo stack; le risorse grandi risiedono sullo heap (o altrove) mentre sono possedute da un oggetto sullo stack, che si occupa di rilasciarle nel proprio distruttore. L'oggetto è legato allo scope (funzione, blocco) in cui è dichiarato: quando lo scope si chiude, l'oggetto viene recuperato insieme a ogni risorsa posseduta. Ogni risorsa ha un unico proprietario [COMP-01_RUST_COMPILATION.pdf, Slide 6].
*   **Sistema di Ownership:** Rust supporta il RAII in modo rigoroso tramite un sistema di ownership basato sui concetti di ownership e borrowing, riassumibile in tre regole:
    *   **[O1]** Ogni valore è posseduto da una variabile, identificata da un nome o path.
    *   **[O2]** Ogni valore ha al più un proprietario alla volta.
    *   **[O3]** Quando il proprietario esce dallo scope, il valore viene recuperato/distrutto/"droppato" [COMP-01_RUST_COMPILATION.pdf, Slide 7].
*   **Semantica di move nell'assegnamento (slide):** per default, un assegnamento tra variabili ha semantica **move**: l'ownership passa dal lato destro al lato sinistro (per [O2]). Esempio: `let x = Box::new(3); let _y = x; println!("x = {}", x);` produce un **errore** (`x` non è più valido dopo il move); al contrario, per i tipi primitivi e per i tipi che implementano il trait `Copy`, l'assegnamento ha semantica **copy**: `let x = 3; let _y = x; println!("x = {:?}", x);` è **corretto**, poiché [O2] resta soddisfatto grazie alla creazione di un nuovo valore [COMP-01_RUST_COMPILATION.pdf, Slide 8].
*   **Semantica di move nel passaggio di parametri (slide):** lo stesso vale per il passaggio di parametri e il ritorno da funzione: ogni valore passato a una funzione viene recuperato al ritorno, quando i parametri formali escono di scope; solo il valore restituito può sopravvivere (si usano tuple per restituire più valori). Esempio: `fn foo<T>(z: T) -> T { z }` — chiamare `foo(x)` con `x: Box<i32>` e poi usare ancora `x` produce errore, a meno di riassegnare il risultato (`x = foo(x)`) oppure di usare un tipo `Copy` [COMP-01_RUST_COMPILATION.pdf, Slide 9].
*   **Borrowing:** le regole di ownership sono troppo restrittive da sole; una risorsa può essere **presa in prestito** dal proprietario (via assegnamento o passaggio di parametro). Per garantire la sicurezza della memoria, le regole di borrowing assicurano che **ALIASING e MUTABILITY non possano coesistere**. I valori possono essere passati per riferimento immutabile (`x = &y`), per riferimento mutabile (`x = &mut y`), o per valore (`x = y`) [COMP-01_RUST_COMPILATION.pdf, Slide 10].
*   **Lifetimes:** un lifetime è un costrutto usato dal borrow checker per garantire la validità delle regole di ownership/borrowing. I lifetime sono associati a ogni singola ownership e borrowing: un lifetime inizia quando l'ownership comincia e termina quando il valore viene mosso o distrutto; per un prestito, termina nel punto in cui il valore preso in prestito è usato per l'ultima volta. I lifetime sono per lo più inferiti; a volte devono essere resi espliciti con la stessa sintassi dei generics. Usando i lifetime, il compilatore verifica che (il proprietario di) ogni variabile/riferimento preso in prestito abbia un lifetime più lungo di chi prende in prestito [B4, B5] [COMP-01_RUST_COMPILATION.pdf, Slide 13].
*   **Perché `rustc` è interessante (slide):** è open source e aperto ai contributi; argomenti classici come CFG, liveness, dataflow, vincoli e punti fissi sono visibili direttamente **come semantica del linguaggio**, non confinati soltanto a fasi di ottimizzazione opzionali; il design del compilatore adotta diverse scelte implementative non convenzionali (es. le query) [COMP-01_RUST_COMPILATION.pdf, Slide 17].
*   **Il Sistema di Compilazione Demand-Driven:** a differenza delle architetture tradizionali basate su passate sequenziali e immutabili, `rustc` è strutturato come un **sistema basato su query** (*demand-driven system*) [COMP-01_RUST_COMPILATION.pdf, Slide 18].
    *   **Funzionamento:** `rustc` non esegue una sequenza fissa di passate; ogni informazione (es. il tipo di una funzione, il suo MIR, il risultato del suo borrow-checking) è calcolata da una **query** che può dipendere da altre query (es. `type_of(def_id)`, `optimized_mir(def_id)`, `mir_borrowck(def_id)`). Quando il compilatore necessita di un'informazione, invoca la query corrispondente, che a sua volta assicura ricorsivamente che tutte le sue dipendenze siano calcolate [COMP-01_RUST_COMPILATION.pdf, Slide 18].
    *   **Compilazione Incrementale:** i risultati delle query sono **memoizzati**; se la stessa informazione viene richiesta di nuovo, può essere riusata senza ricalcolo. Quando il codice sorgente cambia, solo le query i cui input sono cambiati — e quelle che ne dipendono — devono essere ricalcolate [COMP-01_RUST_COMPILATION.pdf, Slide 18].
    *   **Modularità:** questo rende la compilazione più efficiente e scalabile su grandi progetti, offrendo al contempo una struttura pulita e modulare per l'implementazione del compilatore [COMP-01_RUST_COMPILATION.pdf, Slide 18].

### 12.2 Il Front-End e i Quattro Livelli di Rappresentazione Intermedia (IR)

*   **Il Front-End (slide):** `rustc` usa uno scanner (lexer) di basso livello standard che traduce il sorgente in token (`rustc-lexer`), invocato da un lexer di livello più alto usato dal parser; il **parser ricorsivo a discesa** `rustc-parse` genera l'AST [COMP-01_RUST_COMPILATION.pdf, Slide 19].
*   **Dal Front-End al Middle-End (slide):** dopo l'espansione delle macro e la name resolution, `rustc` abbassa (*lowers*) l'AST a **HIR**, un albero sintattico più regolare usato da molte analisi di front-end; vengono poi aggiunte le informazioni tipizzate a livello di corpo funzione, ottenendo il **THIR** [COMP-01_RUST_COMPILATION.pdf, Slide 20].
*   **Il Middle-End (slide):** l'AST del THIR viene tradotto nel CFG del **MIR**, dove flusso di controllo, temporanei, place e drop diventano espliciti. Questa è l'IR su cui viene eseguito il Borrow Checker. Il MIR viene ulteriormente ottimizzato prima dell'abbassamento a LLVM IR. Il back-end consuma il MIR verificato e preparato, crea istanze monomorfizzate concrete, e delega l'ottimizzazione di basso livello a LLVM [COMP-01_RUST_COMPILATION.pdf, Slide 21].
*   **Perché un solo AST non basta? (slide "Why an AST Alone Is Not Enough?"):**
    *   **Troppo sintattico:** un AST rispecchia la sintassi del programmatore: espressioni annidate, zucchero sintattico e forme di superficie oscurano l'ordine di valutazione e gli archi del flusso di controllo.
    *   **Desugaring ripetuto:** senza una IR centrale, ogni fase successiva dovrebbe riscoprire o reimplementare gli stessi desugaring e la stessa semantica locale.
    *   **Ragionamento sul CFG difficile:** il borrow checking necessita di punti fine-grained nel programma e di archi tra essi, scomodi da esprimere direttamente su un AST.
    *   **Forma eseguibile:** il MIR è più vicino a un modello eseguibile: blocchi, statement, terminatori, place, operandi e temporanei espliciti [COMP-01_RUST_COMPILATION.pdf, Slide 22].
*   **HIR (High-Level IR) in dettaglio (slide):**
    *   **Post-espansione:** l'HIR è costruito dopo il parsing, l'espansione delle macro e la name resolution, quindi molti nomi e forme sintattiche sono già risolti.
    *   **Ancora leggibile:** resta vicino al programma del programmatore, il che lo rende adatto ai controlli di front-end e alla diagnostica.
    *   **Parte dello zucchero rimossa:** alcuni costrutti di superficie sono già normalizzati (es. parte dello zucchero orientato ai loop è rappresentato in forme più regolari).
    *   **Non è la IR del borrow check:** l'HIR è utile, ma resta troppo di alto livello per il ragionamento puntuale e dettagliato richiesto dal borrow checking sul MIR [COMP-01_RUST_COMPILATION.pdf, Slide 24].
*   **THIR (Typed HIR) in dettaglio (slide):**
    *   **IR locale al corpo:** il THIR è prodotto per i singoli corpi ed è intenzionalmente temporaneo; `rustc` non mantiene ogni corpo THIR globalmente per sempre.
    *   **Pienamente tipizzato:** rende esplicite le scelte dipendenti dal tipo, incluse le regolazioni (*adjustments*) come autoref, autoderef, coercizioni, e le chiamate overloaded.
    *   **Ponte per l'abbassamento:** il costruttore del MIR consuma il THIR, non l'HIR grezzo, perché il THIR espone già decisioni semantiche importanti.
    *   **Ruolo concettuale:** il THIR è il punto in cui si può osservare lo spostamento dalla sintassi di superficie verso i fatti operazionali necessari alla costruzione del CFG [COMP-01_RUST_COMPILATION.pdf, Slide 25].
*   **MIR (Mid-Level IR) come CFG tipizzato, in dettaglio (slide):**
    *   **Blocchi base:** il MIR organizza una funzione in blocchi base, ciascuno terminato da un terminatore (`return`, `goto`, `switch`, `call`, `unwind`).
    *   **Place e operandi:** una *place* denota una locazione di storage (un locale, un campo, un dereference, una posizione indicizzata); gli operandi sono valori copiati, mossi, o costanti.
    *   **Return place:** il risultato della funzione è un locale distinto, di norma stampato come `_0`; argomenti e temporanei sono stampati come `_1`, `_2`, ecc.
    *   **Ruolo centrale:** il MIR è usato per l'analisi di sicurezza, le trasformazioni, la preparazione delle ottimizzazioni, la valutazione delle costanti (CTFE) e la generazione di codice finale [COMP-01_RUST_COMPILATION.pdf, Slide 27].
*   **MIR Dialects and Phases — i tre "dialetti" del MIR (slide):** la stessa struttura dati sottostante del MIR attraversa fasi con contratti semantici diversi:
    *   **MIR Built:** il MIR iniziale è costruito dal THIR e contiene ancora costrutti orientati all'analisi e annotazioni a livello sorgente.
    *   **MIR Analysis:** il borrow checking, le NLL, l'analisi dei move, i controlli d'inizializzazione e il ragionamento dataflow operano su questo MIR di analisi.
    *   **MIR Runtime:** dopo il borrowck, la pulizia e l'elaborazione (drop elaboration) rimuovono gli artefatti necessari alla verifica ma non all'esecuzione a runtime.
    *   **Stessa struttura, nuovo contratto:** le strutture dati MIR sottostanti sono correlate tra le fasi, ma le promesse semantiche attese da ciascuno stadio del compilatore cambiano [COMP-01_RUST_COMPILATION.pdf, Slide 28].
*   **Da MIR a LLVM IR: cosa sopravvive? (slide):**
    *   **Sopravvive:** flusso di controllo, chiamate, load, store, operazioni aritmetiche, layout, e funzioni monomorfizzate concrete sopravvivono in forme orientate al backend.
    *   **Non sopravvive direttamente:** lifetime e ownership non sono valori a runtime di prima classe nel codice generato — servono a validare il programma prima dell'abbassamento.
    *   **La pulizia conta:** la pulizia post-borrowck rimuove gli artefatti utili solo alla verifica e prepara un dialetto MIR "runtime" adatto a trasformazioni e codegen.
    *   **Il confine con LLVM:** LLVM riceve una IR di livello più basso, dove il ragionamento di sicurezza specifico di Rust ha già giustificato molte assunzioni [COMP-02_RUST_COMPILATION.pdf, Slide 5].
*   **Comandi per ispezionare le IR (slide):** `cargo rustc -- -Z unpretty=hir-tree` (dump dell'HIR, richiede nightly); `cargo rustc -- -Z unpretty=thir-tree` (dump del THIR); `rustc -Z dump-mir=all` (dump del MIR a più stadi); `rustc --emit=mir` e `rustc --emit=llvm-ir` (artefatti di backend, confrontabili per vedere cosa scompare prima di LLVM) [COMP-02_RUST_COMPILATION.pdf, Slide 4].

### 12.3 Desugaring

Il "desugaring" è la trasformazione di costrutti sintattici di alto livello (zucchero sintattico) in forme più elementari ed esplicite, distribuita lungo le varie fasi di abbassamento verso il MIR [COMP-02_RUST_COMPILATION.pdf, Slide 6]:
*   **Desugaring precoce (early):** avviene durante l'abbassamento a HIR (es. i cicli `for`).
*   **Desugaring tardivo (late):** avviene durante la costruzione del THIR (chiamate a metodo, autoderef, autoref, operatori).
*   **Costruzione del MIR:** rimuove interamente l'annidamento delle espressioni.

**Perché serve (slide "Syntactic sugar in Rust"):** Rust contiene molto zucchero sintattico, che nasconde informazioni importanti anche ai fini del borrow-checking. Esempi: desugaring delle chiamate a metodo, dei cicli `for`, dell'overloading degli operatori, dell'operatore `?`, di `if let`/`while let`, dell'auto-ref/deref, delle closure (struct + trait `Fn`/`FnMut`/`FnOnce`), dell'indicizzazione `v[i]` (trait `Index`), del `return` implicito (espressione di coda) [COMP-02_RUST_COMPILATION.pdf, Slide 7].

#### Tabella dei desugaring principali (slide)

| Sorgente                                                 | Forma desugarata                                                                                                                                             |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `for x in v { println!("{}", x); }`                      | `{ let mut iter = IntoIterator::into_iter(v); loop { match iter.next() { Some(x) => { println!("{}", x); } None => break, } } }`                             |
| `let x = foo()?;`                                        | `let x = match foo() { Ok(v) => v, Err(e) => return Err(From::from(e)), };`                                                                                  |
| `let x = opt?;` (su `Option`)                            | `let x = match opt { Some(v) => v, None => return None, };`                                                                                                  |
| `v.push(10);`                                            | `Vec::push(&mut v, 10);`                                                                                                                                     |
| `x.foo()`                                                | `Foo::foo(&x)` oppure `Foo::foo(&mut x)` oppure `Foo::foo(&*x)`, a seconda della modalità di ricezione richiesta                                             |
| `if let Some(x) = opt { println!("{}", x); }`            | `match opt { Some(x) => { println!("{}", x); } _ => {} }`                                                                                                    |
| `while let Some(x) = iter.next() { println!("{}", x); }` | `loop { match iter.next() { Some(x) => { println!("{}", x); } None => break, } }`                                                                            |
| `v[i]` (lettura)                                         | `*std::ops::Index::index(&v, i)`                                                                                                                             |
| `v[i] = 10;`                                             | `*std::ops::IndexMut::index_mut(&mut v, i) = 10;`                                                                                                            |
| `fn f() -> i32 { 3 }` (return implicito)                 | `fn f() -> i32 { return 3; }` (espressione di coda)                                                                                                          |
| `let f = \|x\| x + 1;` (closure)                         | `struct Closure; impl Fn(i32) -> i32 for Closure { extern "rust-call" fn call(&self, (x,): (i32,)) -> i32 { x + 1 } } let f = Closure;`                      |
| `let y = 10; let f = \|x\| x + y;` (cattura)             | `struct Closure { y: i32 } impl Fn(i32) -> i32 for Closure { extern "rust-call" fn call(&self, (x,): (i32,)) -> i32 { x + self.y } } let f = Closure { y };` |

[COMP-02_RUST_COMPILATION.pdf, Slide 8, 9, 10]

**Note metodologiche sul desugaring (slide):**
*   La sintassi a metodo è puro zucchero: il compilatore inserisce `&`, `&mut`, il dereference (`*`) e la risoluzione dei trait necessari [COMP-02_RUST_COMPILATION.pdf, Slide 8].
*   Il desugaring interno di `rustc` per le closure produce sintassi **non legale** in Rust scritto a mano: l'inferenza di cattura e la selezione del trait non sono esprimibili direttamente dal codice del programmatore [COMP-02_RUST_COMPILATION.pdf, Slide 10].
*   Perché è importante per la compilazione: senza rendere esplicite queste trasformazioni in una IR dedicata, ogni analisi successiva (type checking, borrow checking) dovrebbe re-implementare autonomamente la decodifica dello zucchero sintattico.

### 12.4 Esempio Guidato: Traduzione di un'Istruzione Condizionale

Analizziamo come l'istruzione condizionale Rust `let z = if x > 0 { x + 1 } else { 0 };` viene progressivamente ridotta lungo le quattro IR [COMP-01_RUST_COMPILATION.pdf, Slide 23, 26, 29]:
*   **Livello AST:** Struttura ad albero gerarchica che preserva le espressioni annidate del blocco `Stmt::Local` contenente l'espressione condizionale `Expr::If` con i rami `then` e `else` intatti. Il risultato di ogni blocco è **implicito** (l'ultima espressione di ciascun ramo ne diventa l'inizializzatore) [COMP-01_RUST_COMPILATION.pdf, Slide 23]:
    ```rust
    // AST-like view
    Stmt::Local {
        pat: Pat::Ident("z"),
        init: Expr::If {
            cond: Expr::Binary(Gt, Path("x"), Lit(0)),
            then: Block(Expr::Binary(Add, Path("x"), Lit(1))),
            else_: Block(Expr::Lit(0))
        }
    }
    ```
*   **Livello HIR & THIR:** La struttura ad albero rimane simile, ma vengono annotate esplicitamente le informazioni tipizzate locali: viene registrato che `z`, `x` e le costanti `0` e `1` hanno tipo `i32`, e che l'espressione di confronto condizionale ha tipo `bool`. Il THIR registra anche le regolazioni (*adjustments*) e i significati tipizzati degli operatori prima della costruzione del MIR [COMP-01_RUST_COMPILATION.pdf, Slide 26]:
    ```rust
    // HIR-like view
    let z: i32 = if (x > 0) { x + 1 } else { 0 };
    // THIR-like view, typed and normalized
    LocalDecl z: i32
    Init = ExprKind::If {
        cond: ExprKind::Binary(Gt, x:i32, 0_i32): bool,
        then: ExprKind::Binary(Add, x:i32, 1_i32): i32,
        else: 0_i32
    }
    // No CFG yet, but typed body facts are explicit.
    ```
*   **Livello MIR (CFG):** La singola riga di assegnamento viene riscritta ed esplosa in un grafo del flusso di controllo esplicito **a forma di diamante**, in cui la condizione e il calcolo del ramo sono memorizzati in temporanei nominati (`_t0`, `_t1`), e ciascun ramo scrive nella stessa place di destinazione, così che l'inizializzazione possa essere verificata in modo path-sensitive [COMP-01_RUST_COMPILATION.pdf, Slide 29]:
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
        _z = move _t1;
        goto -> bb3;
    }
    bb2: {
        _z = const 0_i32;
        goto -> bb3;
    }
    bb3: { /* z initialized here */ }
    ```
    Questa forma è adatta a liveness, definite assignment, borrow checking e abbassamento successivo [COMP-01_RUST_COMPILATION.pdf, Slide 29].

### 12.5 Struttura Dati, Query e Visitor Pattern sul MIR

*   **Concetti chiave del MIR (slide "MIR: key characteristics and concepts"):**
    *   È basato su un control-flow graph, e non ha espressioni annidate; tutti i tipi nel MIR sono pienamente espliciti (costruiti dal THIR).
    *   **Blocchi base:** unità del CFG, composte da *statement* (azioni con un solo successore) e un **terminatore** (azione con potenzialmente più successori, sempre in fondo al blocco).
    *   **Locals:** argomenti di funzione, variabili locali e temporanei, indicati come `_1`, `_2`, …; `_0` è il locale speciale che rappresenta il valore di ritorno.
    *   **Places:** espressioni che identificano una locazione in memoria, come `_1` oppure `_1.f`.
    *   **Rvalues:** espressioni che producono un valore; i loro **operandi** possono essere una costante (es. `22`) oppure una place (es. `_1`) [COMP-02_RUST_COMPILATION.pdf, Slide 12].
*   **Esempio di MIR di una funzione (slide):**
    ```rust
    fn main() {
        let mut vec = Vec::new();
        vec.push(1);
        vec.push(2);
    }
    // optimized MIR
    fn main() -> () {
        let mut _0: ();
        let mut _1: std::vec::Vec<i32>;
        let _2: ();
        let mut _3: &mut std::vec::Vec<i32>;
        let _4: ();
        let mut _5: &mut std::vec::Vec<i32>;
        scope 1 { debug vec => _1; }
        bb0: { _1 = Vec::<i32>::new() -> [return: bb1, unwind continue]; }
        bb1: { _3 = &mut _1; _2 = Vec::<i32>::push(move _3, const 1_i32) -> [return: bb2, unwind: bb5]; }
        bb2: { _5 = &mut _1; _4 = Vec::<i32>::push(move _5, const 2_i32) -> [return: bb3, unwind: bb5]; }
        bb3: { drop(_1) -> [return: bb4, unwind continue]; }
        bb4: { return; }
        bb5 (cleanup): { drop(_1) -> [return: bb6, unwind terminate(cleanup)]; }
        bb6 (cleanup): { resume; }
    }
    ```
    I locali non hanno nome (tranne l'annotazione di debug `vec => _1`); il MIR registra esplicitamente se i valori sono copiati o mossi (informazione necessaria al ragionamento sull'ownership); il CFG espone cammini che le analisi successive possono attraversare con tecniche di dataflow standard. Si notino i blocchi `(cleanup)` — il percorso alternativo eseguito in caso di *unwind* (svolgimento dello stack durante un panic), che garantisce comunque il drop di `_1` [COMP-02_RUST_COMPILATION.pdf, Slide 13].
*   **MIR Data Types (slide):** i tipi dati del MIR sono definiti nel modulo `compiler/rustc_middle/src/mir/`:
    *   Il tipo dati principale è **`Body`**.
    *   I blocchi base sono memorizzati nel campo `Body::basic_blocks`, un vettore di strutture `BasicBlockData`; non si referenzia mai un blocco direttamente, ma si passa un valore `BasicBlock` (un indice *newtype* in quel vettore).
    *   Gli statement sono rappresentati dal tipo `Statement`; i terminatori dal tipo `Terminator`.
    *   I locali sono rappresentati da un tipo indice *newtype* `Local`; i dati di una variabile locale si trovano nel vettore `Body::local_decls`. Esiste la costante speciale **`RETURN_PLACE`** che identifica il locale speciale rappresentante il valore di ritorno.
    *   Le place sono identificate dalla struct `Place`, con due campi: la variabile locale di base (es. `_1`) e le **proiezioni** (*projections*), rappresentate dal tipo *newtype* `ProjectionElem`, che "proiettano" fuori da una place base — es. `_1.f` è una proiezione con `f` come elemento di proiezione e `_1` come path di base; `*_1` è anch'essa una proiezione, con `*` rappresentato da `ProjectionElem::Deref`.
    *   Gli rvalue sono rappresentati dall'enum `Rvalue`; gli operandi dall'enum `Operand` [COMP-02_RUST_COMPILATION.pdf, Slide 14].
*   **MIR Queries and Passes (slide):** per ottenere il MIR di una funzione si usa la query `optimized_mir` (tipicamente usata dal codegen) oppure `mir_for_ctfe` (tipicamente usata per la valutazione a tempo di compilazione, CTFE); per un "promoted" si usa `promoted_mir`. Queste restituiscono il MIR finale, ottimizzato. Per i def-id esterni (di altri crate) il MIR è ottenuto dai metadati del crate esterno; per i def-id locali, la query costruisce il MIR ottimizzato richiedendo una pipeline di query a monte, ciascuna delle quali contiene una serie di *pass* [COMP-02_RUST_COMPILATION.pdf, Slide 15]. Per produrre il MIR ottimizzato di un dato def-id, si attraversano diverse suite di pass, ciascuna raggruppata da una query, che rappresenta un punto intermedio utile per accedere al dialetto MIR per il type checking o altri scopi [COMP-02_RUST_COMPILATION.pdf, Slide 16]:
    *   `mir_built(D)` — fornisce il MIR iniziale appena costruito;
    *   `mir_const(D)` — applica semplici pass di trasformazione per preparare il MIR alla qualificazione delle costanti;
    *   `mir_promoted(D)` — estrae i temporanei "promuovibili" in MIR body separati, e prepara il MIR al borrow checking;
    *   `mir_drops_elaborated_and_const_checked(D)` — esegue il borrow checking, esegue i pass di trasformazione principali (come la drop elaboration) e prepara il MIR all'ottimizzazione;
    *   `optimized_mir(D)` — esegue tutte le ottimizzazioni abilitate e raggiunge lo stato finale.
*   **MIR Promotion (slide):** un MIR "promosso" è un frammento di MIR estratto dal corpo di una funzione ed elevato a un corpo MIR separato, simile a una costante, così da poter essere valutato a tempo di compilazione o trattato come avente lifetime `'static`. Durante la costruzione del MIR, il compilatore identifica espressioni pure, costanti e prive di effetti collaterali (es. literal array, riferimenti a dati costanti); invece di lasciarle inline nel MIR della funzione, le promuove in un corpo MIR separato (una "costante promossa") e sostituisce l'espressione originale con un riferimento a quel valore promosso [COMP-02_RUST_COMPILATION.pdf, Slide 17]:
    ```rust
    fn f() -> &'static [i32; 3] { &[1, 2, 3] }
    // Senza promozione, l'array sarebbe un temporaneo dentro f. Con la promozione:
    // Promoted[0]:  _0 = [1, 2, 3]; return;
    // fn f():       _0 = &'static Promoted[0]; return;
    ```
*   **MIR Construction (slide):** la query `mir_built` provoca l'abbassamento dal THIR di corpi di funzione/closure, inizializzatori di item `static`/`const`, inizializzatori di discriminanti di `enum`, e altro ancora. Per prima cosa crea variabili locali per ogni argomento e per ogni binding specificato, oltre ad accessi ai campi che leggono i valori dagli argomenti e li scrivono nelle variabili di binding. Infine, innesca una chiamata ricorsiva a una funzione che genera il MIR per il corpo (un'espressione `Block`) e ne scrive il risultato nella `RETURN_PLACE` [COMP-02_RUST_COMPILATION.pdf, Slide 18].
*   **MIR Visitor (slide):** il visitor del MIR è uno strumento comodo per attraversare il MIR, sia per cercare cose sia per modificarle — usato dalle analisi di dataflow. `rustc` supporta il **pattern Visitor** con trait appositi definiti nel modulo `middle::mir::visit`: `Visitor` (opera su un `&Mir` e restituisce riferimenti condivisi) e `MutVisitor` (opera su un `&mut Mir` e restituisce riferimenti mutabili) [COMP-02_RUST_COMPILATION.pdf, Slide 20]. Nel pattern Visitor generico: la struttura dati può essere composta da diversi tipi di componenti (`ConcreteElement`); ciascun componente implementa un metodo `accept(Visitor)`; il Visitor definisce un metodo `visit` per ciascun tipo; la logica di navigazione risiede nel Visitor; a ogni passo il metodo `visit` corretto è selezionato per overloading [COMP-02_RUST_COMPILATION.pdf, Slide 21]. Per implementare un visitor si crea un tipo che "trattiene" lo stato necessario durante l'elaborazione del MIR e si implementa per esso il trait `Visitor` o `MutVisitor`; il modulo `middle::mir::traversal` contiene funzioni utili per attraversare il CFG del MIR in ordini standard diversi (pre-order, reverse post-order, ecc.) [COMP-02_RUST_COMPILATION.pdf, Slide 22].

### 12.6 Il Framework di Dataflow Analysis su MIR

L'analisi di dataflow sul MIR è ampiamente usata da `rustc`, ad esempio per: trovare variabili non inizializzate, determinare quali variabili sono vive attraverso uno statement `yield` di un generatore, calcolare quali place sono prese in prestito in un dato punto del CFG [COMP-02_RUST_COMPILATION.pdf, Slide 23].
*   **Il trait `Analysis`:** un'analisi di dataflow è definita dal trait `Analysis`, che oltre al tipo dello stato di dataflow definisce il valore iniziale di quello stato all'ingresso di ciascun blocco e la **direzione** dell'analisi (forward o backward). Il dominio dell'analisi deve essere un reticolo (più precisamente, un **join-semilattice**) con un operatore di join ben definito (si veda il modulo `lattice` e il trait `JoinSemiLattice`) — esattamente il framework matematico introdotto in astratto nel Cap. 8 (si veda anche §8.1bis per il fondamento formale CPO/Kleene) [COMP-02_RUST_COMPILATION.pdf, Slide 23].
*   **Funzioni di trasferimento ed "effects" (slide):** il framework di dataflow di `rustc` consente a ciascuno statement (e terminatore) all'interno di un blocco base di definire la propria funzione di trasferimento, chiamata **effect**. Ogni effect viene applicato in successione secondo l'ordine di dataflow, e insieme definiscono la funzione di trasferimento dell'intero blocco base. È anche possibile definire un effect per particolari archi in uscita di alcuni terminatori. Gli statement possono inoltre essere dotati di **"before" effect**: applicati immediatamente prima dell'effect "primario", indipendentemente dalla direzione dell'analisi — cioè un'analisi backward applica prima il "before" effect e poi l'effect primario nel calcolare la funzione di trasferimento del blocco, esattamente come farebbe un'analisi forward. Le varianti "before" sono utili, ad esempio, quando l'effetto del lato destro di un'assegnazione deve essere considerato separatamente da quello del lato sinistro [COMP-02_RUST_COMPILATION.pdf, Slide 24].
*   **Ispezionare i risultati (slide):** dopo aver costruito un'analisi, si invoca `iterate_to_fixpoint`, che restituisce una struttura `Results` contenente lo stato di dataflow al punto fisso in ingresso a ciascun blocco. Se serve lo stato solo in pochi punti (es. a ogni terminatore `Drop`), si usa un `ResultsCursor`; se serve lo stato a ogni locazione, un `ResultsVisitor` è più efficiente [COMP-02_RUST_COMPILATION.pdf, Slide 25]. Esempio con `ResultsVisitor` (ispeziona lo stato al punto fisso per ogni locazione in ogni blocco, in ordine RPO) e con `ResultsCursor` (ispeziona lo stato immediatamente prima di ogni terminatore `Drop`) [COMP-02_RUST_COMPILATION.pdf, Slide 26]:
    ```rust
    // ResultsVisitor
    let results = MyAnalysis::new().iterate_to_fixpoint(tcx, body, None);
    results.visit_with(body, &mut my_visitor);

    // ResultsCursor
    let mut results = MyAnalysis::new().iterate_to_fixpoint(tcx, body, None)
        .into_results_cursor(body);
    for (bb, block) in body.basic_blocks().iter_enumerated() {
        if let TerminatorKind::Drop { .. } = block.terminator().kind {
            results.seek_before_primary_effect(body.terminator_loc(bb));
            let state = results.get();
            println!("state before drop: {:#?}", state);
        }
    }
    ```
    `rustc` può anche produrre diagrammi Graphviz per visualizzare lo stato di dataflow completo in ingresso e in uscita da ciascun blocco [COMP-02_RUST_COMPILATION.pdf, Slide 27].

### 12.7 Drop Elaboration

In Rust, la gestione della memoria si basa sulla deallocazione deterministica automatica di ciascuna risorsa non appena il suo proprietario esce dallo scope d'esecuzione (regola RAII, §12.1). La **Drop Elaboration** è la fase del compilatore che rispecchia questa semantica a livello di MIR.

*   **Drop dinamici (slide "Dynamic drops"):** quando viene costruito il MIR, i terminatori `Drop` e `DropAndReplace` rappresentano punti in cui un drop *può* verificarsi; in questa fase, la loro presenza non garantisce ancora che un distruttore verrà eseguito. Bisogna tener traccia di **se** una variabile è inizializzata dinamicamente [COMP-02_RUST_COMPILATION.pdf, Slide 28]:
    ```rust
    let mut y = vec![];
    {
        let x = vec![1, 2, 3];
        if std::process::id() % 2 == 0 {
            y = x;  // move condizionale di `x` in `y`
        }
    } // `x` esce di scope qui. Va droppata?
    ```
    Quando una variabile o un temporaneo inizializzato esce di scope, il suo distruttore viene eseguito (viene "droppato"); anche l'assegnamento esegue il distruttore del proprio operando sinistro, se inizializzato. Se una variabile è stata parzialmente inizializzata, vengono droppati solo i suoi campi inizializzati. Se una variabile è inizializzata o no è noto **solo a runtime** [COMP-02_RUST_COMPILATION.pdf, Slide 28].
*   **Drop obligations (slide):** quando una variabile locale diventa inizializzata, essa stabilisce un insieme di **"obblighi di drop"** (*drop obligations*): un insieme di path strutturali (es. una variabile locale `a`, o un path a un campo `b.f.y`) che devono essere droppati. Gli obblighi di drop per una variabile locale `x` di tipo struct `T` sono calcolati analizzando la struttura di `T`: se `T` stesso implementa `Drop`, allora `x` è un obbligo di drop; se `T` non implementa `Drop`, l'insieme degli obblighi di drop è l'unione degli obblighi di drop dei campi di `T`. Quando un path strutturale viene mosso (e diventa quindi non inizializzato), ogni obbligo di drop per quel path o per i suoi discendenti (`path.f`, `path.f.g.h`, ecc.) viene rilasciato. Quando una variabile locale esce di scope (`Drop`), o quando un path strutturale viene sovrascritto tramite assegnamento (`DropAndReplace`), si controllano gli eventuali obblighi di drop per quella variabile o path: a meno che l'obbligo non sia già stato rilasciato, viene chiamata la relativa implementazione di `Drop`. Per i tipi `enum`, devono essere droppati solo i campi corrispondenti alla variante "attiva": si controlla prima il discriminante per determinare la variante attiva, e tutti gli obblighi di drop delle varianti diverse da quella attiva vengono ignorati [COMP-02_RUST_COMPILATION.pdf, Slide 29].
*   **Il processo di Drop Elaboration (slide):** un modello valido per queste regole consiste nel mantenere un flag booleano (un **"drop flag"**) per ogni path strutturale usato in un qualsiasi punto della funzione. Questo flag viene impostato quando il path viene inizializzato ed è azzerato quando il path viene mosso. Quando si verifica un `Drop`, si controllano i flag di ogni obbligo associato al target del `Drop` e si chiama l'implementazione `Drop` associata per quelli ancora applicabili. Questo processo — la trasformazione del MIR appena costruito, con i suoi terminatori `Drop`/`DropAndReplace` imprecisi, in uno con drop flag — è noto come **drop elaboration**. Quando uno statement MIR fa sì che una variabile diventi inizializzata (o non inizializzata), la drop elaboration inserisce codice che imposta (o azzera) il drop flag corrispondente; avvolge inoltre i terminatori `Drop` in condizionali che verificano i drop flag appena inseriti. Una volta completato questo processo, i terminatori `Drop` nel MIR corrispondono a una chiamata alla "drop glue" (o "drop shim") per il tipo della place droppata: la drop glue di un tipo chiama l'implementazione `Drop` per quel tipo (se esiste), e poi richiama ricorsivamente la drop glue per tutti i campi di quel tipo [COMP-02_RUST_COMPILATION.pdf, Slide 30].
*   **Ottimizzazioni della drop elaboration in `rustc` (slide):** alcune ottimizzazioni possibili: solo i path che sono target di un `Drop` (o hanno tale target come prefisso) necessitano di drop flag; alcune variabili sono note per essere inizializzate (o non inizializzate) quando vengono droppate, e non necessitano di flag; se un insieme di path viene droppato o mosso solo tramite un prefisso condiviso, quei path possono condividere un singolo drop flag. Un sottoinsieme di queste ottimizzazioni è implementato in `rustc` [COMP-02_RUST_COMPILATION.pdf, Slide 31].
*   **Le quattro categorie di Drop (slide):** la drop elaboration designa ogni `Drop` nel MIR appena costruito come uno dei seguenti quattro tipi:
    *   **Static:** il target è sempre inizializzato.
    *   **Dead:** il target è sempre non inizializzato.
    *   **Conditional:** il target è o interamente inizializzato o interamente non inizializzato (mai parzialmente).
    *   **Open:** il target può essere parzialmente inizializzato.

    Per questa classificazione si usa una coppia di analisi di dataflow, **`MaybeInitializedPlaces`** e **`MaybeUninitializedPlaces`**. Se una place risulta in una ma non nell'altra, allora è noto a tempo di compilazione se è `Dead` o `Static`: non serve alcun flag per il target, e il terminatore `Drop` viene rimosso (caso `Dead`) o preservato (caso `Static`). Per i drop `Conditional`, viene generato un drop flag per il target [COMP-02_RUST_COMPILATION.pdf, Slide 31].
*   **Open Drops (slide):** concretamente, nella costruzione del MIR e nelle prime fasi di analisi, un `drop(x)` può essere "aperto" (*open*) nel senso che il compilatore sa che `x` deve essere droppata, ma non ha ancora completamente elaborato **come** quel drop debba avvenire. Questo include: se `x` ha un'implementazione `Drop` personalizzata; se `x` è parzialmente inizializzata o parzialmente mossa; quali campi di `x` devono ancora essere droppati; e in quale ordine i drop annidati devono avvenire. Più avanti nella pipeline, durante la drop elaboration, questi drop aperti vengono trasformati in sequenze pienamente esplicite di operazioni di drop (talvolta chiamate drop "chiuse"), dove tutti i cammini di flusso di controllo sono resi espliciti, tutti i drop campo-per-campo sono inseriti, e i drop condizionali (dipendenti dai move) sono gestiti con precisione [COMP-02_RUST_COMPILATION.pdf, Slide 32].

### 12.8 Il MIR Borrow Checker e i Non-Lexical Lifetimes (NLL)

#### 12.8.1 Il Borrow Checking come Analisi di Programma
*   **Dominio:** il checker ragiona su place, move path, prestiti (*loans*), stati d'inizializzazione, e regioni in locazioni di un CFG MIR.
*   **Vincoli:** il type checking sul MIR genera vincoli di regione, mentre le analisi di move e borrow producono fatti sui punti del programma.
*   **Dataflow:** le classiche idee gen/kill e di punto fisso appaiono nel calcolo dell'inizializzazione, della liveness, e della validità dei prestiti.
*   **Diagnostica:** il risultato non è solo accetta/rifiuta; il compilatore riporta i fatti agli span del sorgente per spiegare perché un prestito o un move non è valido [COMP-04_RUST_COMPILATION.pdf, Slide 4].

#### 12.8.2 Le Fasi Principali del MIR Borrow Checker (query `mir_borrowck`)
1.  **Punto di ingresso:** il borrow checker è implementato in `rustc_borrowck` ed è invocato come query sul MIR.
2.  **Duplicazione e preparazione del MIR:** viene creata una copia locale del MIR, che verrà mutata in-place per allegarvi informazioni di regione.
3.  **Region variable initialization:** `replace_regions_in_mir` sostituisce tutte le annotazioni di lifetime con variabili di inferenza fresche.
4.  **Analisi di dataflow (mosse e inizializzazione):** le analisi calcolano quando i valori sono mossi, inizializzati, o invalidati lungo il CFG.
5.  **Seconda type-check sul MIR:** un type checker a livello MIR deriva i vincoli tra regioni (lifetime).
6.  **Region inference (risoluzione dei vincoli):** calcola l'insieme dei punti del CFG in cui ogni lifetime deve valere, tramite inferenza in stile a punto fisso.
7.  **Borrow set / prestiti in scope:** determina quali prestiti sono attivi a ogni punto del CFG.
8.  **Passata di validazione finale (segnalazione errori):** una seconda traversata controlla ogni operazione (es. `*a + 1`) contro: stato d'inizializzazione, regole di borrowing, vincoli di mutabilità [COMP-04_RUST_COMPILATION.pdf, Slide 5].

#### 12.8.3 Il MIR Type Check
Una componente chiave del borrow check è il MIR type-check, che attraversa il MIR ed esegue un "type check" completo. Durante questo controllo emergono anche i vincoli di regione applicabili al programma, così come i *type test* (obblighi speciali sui tipi che coinvolgono regioni); il controllo sostituisce tutte le regioni nel corpo con nuove regioni non vincolate. Sebbene il MIR sia costruito a partire dal THIR — già interamente type-checked — `rustc` esegue comunque un type check sul MIR perché il processo di abbassamento non è banalmente *type-preserving* e introduce nuovi costrutti e invarianti che devono essere validati indipendentemente. Durante la transizione da THIR a MIR il compilatore esegue desugaring, introduce temporanei, riordina la valutazione, inserisce operazioni implicite (borrow, move, drop) e semplifica le espressioni in un CFG: queste trasformazioni possono esporre incoerenze o richiedere garanzie aggiuntive non controllate esplicitamente a livello THIR. Il MIR type check garantisce quindi che tutte queste operazioni abbassate siano internamente coerenti, che operandi e place abbiano i tipi corretti, e che gli invarianti richiesti dalle fasi successive (borrow checking, ottimizzazioni, codegen) siano rispettati: agisce come un passo di validazione difensiva — il THIR garantisce la correttezza del programma a livello sorgente, mentre il type checking sul MIR garantisce la correttezza della trasformazione del compilatore verso il MIR [COMP-03_RUST_COMPILATION.pdf, Slide 27, 28].

**Perché il MIR type check è eseguito dopo la move analysis (slide):** `rustc` esegue il type check sul MIR **dopo** l'analisi dei move perché il type checker MIR necessita di informazioni prodotte da quest'ultima. Il suo scopo principale nel borrow checking è generare vincoli precisi di regione/lifetime, e tali vincoli dipendono dal sapere: quali place sono ancora inizializzate; quali move sono avvenuti; quali path sono legalmente movibili; e quali locali/place sono effettivamente rilevanti per l'analisi dei prestiti. L'ordinamento delle fasi è quindi determinato dalle dipendenze tra le analisi [COMP-06_RUST_COMPILATION.pdf, Slide 26].

#### 12.8.4 Regioni e Lifetime: la Distinzione Concettuale
Nella terminologia di `rustc`, una **regione** è la rappresentazione interna del compilatore per un lifetime, usata durante il type checking e il borrow checking. Una regione denota un insieme di punti del programma (o di scope nel CFG) in cui un riferimento è considerato valido. Invece di pensare ai lifetime come scope puramente sintattici, il compilatore li modella come regioni che possono essere confrontate, vincolate (es. una regione deve sopravvivere a un'altra) e inferite tramite un'analisi in stile dataflow. La relazione è che "lifetime" è il concetto rivolto all'utente, mentre "regione" è il modello semantico e analitico del compilatore per quel concetto. Quando si scrive un'annotazione di lifetime come `'a`, il compilatore la traduce in variabili di regione e vincoli (es. `'a: 'b` diventa "la regione `'a` sopravvive alla regione `'b`"). Con i Non-Lexical Lifetime (NLL), queste regioni non sono più legate a blocchi lessicali ma corrispondono a insiemi precisi di punti del CFG, calcolati tramite risoluzione di vincoli. I lifetime nel linguaggio sono quindi essenzialmente nomi o astrazioni sopra le regioni, mentre le regioni sono gli oggetti concreti manipolati dal borrow checker [COMP-03_RUST_COMPILATION.pdf, Slide 29].

#### 12.8.5 Region Inference (NLL): Panoramica e Meccanismo
*   **Due fasi principali:** `replace_regions_in_mir` (prepara il MIR per l'inferenza) e `compute_regions` (risolve le variabili di regione/lifetime) [COMP-03_RUST_COMPILATION.pdf, Slide 30].
*   **Passo 1 — Identificare le regioni universali:** si estraggono le regioni libere dalla firma della funzione (es. `'a`, `'static`), che rappresentano i lifetime visibili dal chiamante.
*   **Passo 2 — Sostituire le regioni con variabili:** tutte le regioni del MIR diventano variabili di inferenza fresche, scartando l'informazione lessicale sui lifetime e abilitando così l'analisi control-flow-sensitive (NLL).
*   **Passo 3 — Generare i vincoli (MIR type check):** un type checker specializzato produce vincoli di outlives (`'a: 'b`), **vincoli di liveness**, e **member constraint** (che sorgono da `impl Trait`).
*   **Passo 4 — Risolvere i vincoli (region inference):** si costruisce un `RegionInferenceContext` e si calcolano i valori delle regioni tramite propagazione di vincoli / risoluzione a punto fisso [COMP-03_RUST_COMPILATION.pdf, Slide 30; COMP-04_RUST_COMPILATION.pdf, Slide 7, 8].
*   **Rappresentazione delle regioni:** le regioni sono insiemi di punti del programma; ogni regione è l'insieme delle locazioni CFG in cui è valida. Gli elementi di una regione includono locazioni MIR (punti del programma), `end('a)` (il lifetime si estende nel contesto del chiamante), `end('static)` (per il resto del programma), e segnaposto per regioni ignote. Per efficienza, sono memorizzate come bitset indicizzati da `RegionElementIndex` [COMP-03_RUST_COMPILATION.pdf, Slide 31].
*   **Come funziona l'inferenza — inizializzazione dalla liveness:** ogni regione parte con i punti del CFG in cui è usata (questi vengono dai vincoli di liveness). **Propagazione dei vincoli:** per ogni vincolo di outlives `'a: 'b`: $'a \leftarrow 'a \cup 'b \cup \{end('b)\}$, ripetuto fino al punto fisso (`propagate_constraints`). Le regioni **crescono monotonicamente** — i loro valori sono insiemi, e la propagazione è un dataflow basato su unione [COMP-03_RUST_COMPILATION.pdf, Slide 33; COMP-04_RUST_COMPILATION.pdf, Slide 10].
*   **`RegionInferenceContext` (dati centrali, slide):** contiene tutti gli input dell'inferenza: `constraints` (relazioni di outlives), `liveness_constraints` (seed iniziali), `universal_regions` (lifetime liberi), `universal_region_relations` (limiti noti, es. da `where` clause), `type_tests` (vincoli da controllare dopo l'inferenza). Il processo di risoluzione (`solve()`) esegue: `propagate_constraints` → `check_type_tests` → `check_universal_regions` [COMP-03_RUST_COMPILATION.pdf, Slide 35].
*   **Cicli di vincoli di outlives e SCC:** i vincoli di outlives (`'a: 'b`) sono rappresentati come un grafo diretto in cui le regioni sono nodi e i vincoli sono archi. I cicli in questo grafo indicano regioni che devono essere uguali, quindi il compilatore calcola le **componenti fortemente connesse (SCC)** per raggruppare tali regioni; ogni SCC è trattata come una singola unità con un unico valore condiviso, migliorando l'efficienza. Dopo aver collassato i cicli in SCC, il compilatore lavora su un grafo ridotto di SCC, che è sempre un **DAG**; i vincoli tra regioni diventano vincoli tra SCC, abilitando una propagazione efficiente e priva di dipendenze potenzialmente cicliche [COMP-04_RUST_COMPILATION.pdf, Slide 11].

#### 12.8.6 Vincoli di Regione: Esempi
**Esempi di vincoli generati (slide):**
```rust
fn f<'a>(x: &'a u32) -> u32 { let y = x; *y }
```
Il prestito/riferimento memorizzato in `y` è vivo nel punto in cui `*y` è usato (**vincolo di liveness**). Per l'assegnazione, il compilatore introduce una regione inferita, diciamo `'0`, per `y`: `x : &'a u32`, `y : &'0 u32`; affinché l'assegnamento sia valido serve `&'a u32 <: &'0 u32`, il che implica il **vincolo di outlives** `'a : '0` [COMP-04_RUST_COMPILATION.pdf, Slide 9].

**Tipi di vincoli raccolti dal type checker MIR (slide):** vincoli di liveness (`R live at E`); vincoli di outlives (`R1: R2`, che sorgono da subtyping); *member constraint* (`member R_m of [R_c...]`, che sorgono da `impl Trait`). Il type checker MIR raccoglie anche i **type test**, da controllare dopo la region inference [COMP-04_RUST_COMPILATION.pdf, Slide 8].

#### 12.8.7 Type Tests
Durante il MIR type checking, `rustc` genera vincoli e **type test**: obblighi speciali sui tipi che coinvolgono regioni. Il solutore di region inference calcola una soluzione (una mappatura da variabili di regione a insiemi di punti del programma); dopo che la soluzione è calcolata, `rustc` controlla tutti i type test memorizzati contro quella soluzione. Vengono usati quando codificare un vincolo direttamente nel solutore sarebbe troppo complesso o inefficiente, oppure quando è più pulito controllarlo dopo aver conosciuto le regioni finali [COMP-04_RUST_COMPILATION.pdf, Slide 12].

**Cosa verificano (slide):** un type test tipicamente verifica che un tipo sia ben formato rispetto ai lifetime inferiti. Esempi concettuali: un tipo riferimento `&'r T` è valido solo se `'r` contiene tutti i punti in cui il riferimento è usato; un vincolo generico come `T:'a` richiede che tutti i riferimenti dentro `T` vivano abbastanza da soddisfare `'a`; le relazioni di subtyping tra tipi che coinvolgono lifetime sono rispettate. Sono essenzialmente controlli di *well-formedness*/subtyping su tipi che dipendono da regioni [COMP-04_RUST_COMPILATION.pdf, Slide 13].

**Perché non codificarli nel solutore (slide):** perché il solutore lavora su un dominio relativamente semplice (insiemi di punti, vincoli di outlives, ecc.), mentre la struttura dei tipi può essere complessa (tipi annidati, proiezioni, generics): includere tutto ciò nel calcolo a punto fisso lo complicherebbe e rallenterebbe [COMP-04_RUST_COMPILATION.pdf, Slide 14].

**Tabella di esempi (slide):**

| Codice Rust | Type test generato | Spiegazione |
|---|---|---|
| `fn f<'a, T>(x: &'a T) { let y: &'a T = x; }` | `T: 'a` | `&'a T` è ben formato solo se il tipo referente `T` è valido per almeno `'a` — **soddisfatto** |
| `fn f<'a, T>(x: T) { let r: &'a T; }` | `T: 'a` | Anche se `r` è solo una dichiarazione locale, il tipo annotato `&'a T` impone un obbligo di well-formedness su `T` — **non soddisfatto** |
| `fn f<'a, T>(x: &'a [T]) { let y: &'a [T] = x; }` | `[T]: 'a`, riducibile a `T: 'a` | Un riferimento a slice con lifetime `'a` richiede che il tipo degli elementi dello slice sia valido per `'a` — **soddisfatto** |
| `struct S<T>(T); fn f<'a, T>(x: &'a S<T>) {}` | `S<T>: 'a`, che richiede `T: 'a` | Il riferimento `&'a S<T>` richiede che l'intero tipo referente `S<T>` sopravviva a `'a`; strutturalmente ciò dipende da `T` |

[COMP-04_RUST_COMPILATION.pdf, Slide 15]

**Esempio di type test semplice dal tipo di ritorno (slide):**
```rust
fn f<'a,'b>(x: &'a u32) -> &'b u32 { x }
```
Restituire `x` dove è atteso `&'b u32` richiede `&'a u32 <: &'b u32`, quindi il compilatore genera il type test `'a: 'b`. Questo non è usato come vincolo di outlives, ma viene solo **controllato** dopo la region inference — di conseguenza la compilazione fallisce (nessun `where 'a: 'b` è dichiarato) [COMP-04_RUST_COMPILATION.pdf, Slide 16].

#### 12.8.8 Universal Regions e Controllo delle Regioni "Troppo Grandi"
Le **regioni universali** si riferiscono ai lifetime dichiarati dall'utente, come i parametri di lifetime (`'a`, `'b`) e `'static`. Sono universalmente quantificate: il compilatore deve garantire che la funzione sia corretta per **tutte** le possibili istanziazioni di questi lifetime (soddisfacendo i vincoli dichiarati). Internamente, tutti i lifetime sono rappresentati come variabili di regione: le regioni universali occupano un sottoinsieme fisso di queste variabili, mentre le regioni esistenziali rappresentano variabili di inferenza. Durante la region inference, a ogni regione viene assegnato un insieme contenente punti del flusso di controllo e marcatori speciali come `end('a)`, che indicano l'estensione di un lifetime. Dopo la propagazione, il compilatore esegue un controllo di coerenza: se il valore inferito di una regione universale `'a` include `end('b)`, allora la relazione `'a:'b` deve essere già stata dichiarata esplicitamente; altrimenti si tratta di una violazione della firma della funzione e risulta in un errore a tempo di compilazione. Questo garantisce che le relazioni di lifetime inferite non eccedano quanto promesso dai bound della funzione [COMP-04_RUST_COMPILATION.pdf, Slide 17]:
```rust
fn f<'a,'b>(x: &'a i32) -> &'b i32 { x } // NO
fn f<'a,'b>(x: &'a i32) -> &'b i32 where 'a: 'b { x } // OK
```

#### 12.8.9 Esempio Svolto: NLL, Accettazione vs Rifiuto per Liveness
**Caso accettato — la liveness termina all'ultimo uso (slide):** il prestito condiviso `r` è vivo solo fino al suo ultimo uso; dopo quel punto la regione di `r` termina, quindi può iniziare il prestito mutabile. Poiché le regioni non si sovrappongono, il programma è accettato [COMP-04_RUST_COMPILATION.pdf, Slide 19]:
```rust
fn f() {
    let mut x = 10;
    let r = &x;
    println!("{}", r);   // ultimo uso di r
    let m = &mut x;      // 'r termina qui, 'm inizia
    *m += 1;
}
// 'r = { punti fino all'ultimo uso di r }
// 'm = { punti da &mut x a *m += 1 }
```

**Caso rifiutato — la liveness si sovrappone al prestito mutabile (slide):** qui `r` è ancora vivo alla `println!` dopo che `m` è stato creato, quindi il prestito condiviso e quello mutabile si sovrappongono, violando le regole di borrowing; il programma è rigettato [COMP-04_RUST_COMPILATION.pdf, Slide 20]:
```rust
fn f() {
    let mut x = 10;
    let r = &x;
    let m = &mut x;
    println!("{}", r);   // r è ancora vivo qui, dopo la creazione di m!
    *m += 1;
}
// 'r vivo a println!("{}", r);  'm vivo a *m += 1;
```

#### 12.8.10 Two-Phase Borrows: Esempio Numerico Completo
I two-phase borrow sono una forma speciale di prestito mutabile che si comporta temporaneamente come un prestito condiviso, per supportare pattern come `vec.push(vec.len())`. Sono introdotti solo in casi impliciti specifici (es. chiamate a metodo con ricevitore `&mut`, re-borrow in argomenti, operatori di assegnamento composto). Sono implementati come temporanei con due punti chiave: un **punto di prenotazione** (*reservation*), dove inizia il comportamento simile a un prestito condiviso, e un **punto di attivazione** (*activation*), dove diventa un prestito mutabile pieno. Vengono trattati come prestiti mutabili ma con regole rilassate prima dell'attivazione [COMP-04_RUST_COMPILATION.pdf, Slide 21].

**Esempio numerico (slide):**
```rust
fn push_len(v: &mut Vec<i32>) { v.push(v.len() as i32); }
// Conceptual THIR, simplified:
// Vec::push(&mut *v, (Vec::len(&*v)) as i32)
fn push_len(_1: &mut Vec<i32>) -> () {
    let mut _0: ();
    let mut _2: &mut Vec<i32>;
    let mut _3: &Vec<i32>;
    let mut _4: usize;
    let mut _5: i32;
    bb0: {
        [p1] _2 = &mut (*_1);   // prenotazione del prestito mutabile
        [p2] _3 = &(*_1);       // prestito condiviso per len()
        [p3] _4 = Vec::<i32>::len(move _3);
        [p4] _5 = move _4 as i32 (IntToInt);
        [p5] _0 = Vec::<i32>::push(move _2, move _5);
        return;
    }
}
```
Regioni fresche: `_2: &'r_mut mut Vec<i32>`, `_3: &'r_shr Vec<i32>`. Soluzione delle regioni: `'r_shr = {p2, p3}`, `'r_mut = {p1, p2, p3, p4, p5}`, ma `'r_mut` è **a due fasi**: prenotazione a `p1`, attivazione a `p5`. Quindi, tra `p1` e `p5`, il prestito mutabile è solo *prenotato*, e l'uso del prestito condiviso a `p3` è legale [COMP-04_RUST_COMPILATION.pdf, Slide 22]. Senza il meccanismo a due fasi, il prestito mutabile a `p1` (che copre l'intero intervallo `p1`–`p5`) si sovrapporrebbe al prestito condiviso a `p2`–`p3`, violando [B2] e rigettando un pattern d'uso perfettamente sicuro.

#### 12.8.11 Move Analysis Completa

**Vista unificata (slide "Tracking Moves and Initialization"):** il borrow checker traccia un insieme di "place inizializzate": l'assegnamento aggiunge all'insieme, il move rimuove dall'insieme. Move e inizializzazione sono, dal punto di vista del compilatore, la **stessa analisi** — entrambe sono semplicemente transizioni di stato in un dataflow [COMP-03_RUST_COMPILATION.pdf, Slide 17]:
```rust
fn foo() {
    let a: Vec<u32>;                 // a non è ancora inizializzata
    a = vec![22];                    // a è inizializzata qui
    std::mem::drop(a);               // a è mossa qui
    let l = a.len();                 // a non è più inizializzata qui → ERRORE
}
```

**Move path (slide):** i move path corrispondono approssimativamente a place MIR ottimizzate; ciascuno è memorizzato come `MovePathIndex` per efficienza. Sono costruiti percorrendo il MIR (`MoveData::gather_moves`), registrando dove ogni place è inizializzata e mossa. Sono **esclusi** dal tracciamento gli elementi di array (`foo[1]`) e i dereference di prestiti (`*foo`), per ridurre l'overhead dell'analisi. I move path formano una **struttura ad albero** gerarchica (es. `a → a.b → a.b.c`), consentendo query su genitori/figli e un'analisi efficiente dei move parziali [COMP-03_RUST_COMPILATION.pdf, Slide 19].

**Move Analysis come dataflow (slide):** problema di dataflow **forward**. Dominio: $IN[n], OUT[n] \subseteq MovePaths$; $IN[n]$ = path inizializzati prima dello statement $n$; $OUT[n]$ = path inizializzati dopo. Equazioni standard: $OUT[n] = GEN[n] \cup (IN[n] - KILL[n])$, $IN[n] = \bigcup OUT[p]$ sui predecessori $p$ [COMP-03_RUST_COMPILATION.pdf, Slide 21]. Interpretazione: $GEN[n]$ (inizializzazioni) sono gli assegnamenti (`a = ...` aggiunge `a` all'insieme inizializzato); $KILL[n]$ (move) sono i move (`let b = a;`, `drop(a);` rimuovono `a` dall'insieme inizializzato) [COMP-03_RUST_COMPILATION.pdf, Slide 22].

**Esempio svolto — caso scalare (slide):**
```rust
let a: Vec<u32>;
a = vec![22];
drop(a);
let l = a.len(); // ERRORE
```

| Punto | IN | GEN | KILL | OUT |
|---|---|---|---|---|
| entry | ∅ | ∅ | ∅ | ∅ |
| `a = ...` | ∅ | {a} | ∅ | {a} |
| `drop(a)` | {a} | ∅ | {a} | ∅ |
| `a.len()` | ∅ | — | — | **ERRORE** |

`a ∉ IN` ⇒ *use of uninitialized value* [COMP-03_RUST_COMPILATION.pdf, Slide 23].

**Regola d'oro:** lo spostamento (*move*) di una variabile padre invalida (uccide) tutti i suoi campi figli; lo spostamento di un singolo campo figlio non uccide i fratelli, consentendo un ragionamento preciso a livello di singola componente (*partial-move reasoning*) [COMP-03_RUST_COMPILATION.pdf, Slide 24, 25].

**Esempio 1 — field-sensitive, move del padre (slide):**
```rust
let a: (Vec<u32>, Vec<u32>) = (vec![1,2,3], vec![4,5,6]);
let b = a;
```

| Statement | GEN           | KILL          |
| --------- | ------------- | ------------- |
| init `a`  | {a, a.0, a.1} | ∅             |
| `b = a`   | {b}           | {a, a.0, a.1} |

Risultato: inizializzati = {b} — muovere il padre `a` uccide **tutti** i figli [COMP-03_RUST_COMPILATION.pdf, Slide 24].

**Esempio 2 — field-sensitive, move di un figlio (slide):**
```rust
let a: (Vec<u32>, Vec<u32>) = (vec![1,2,3], vec![4,5,6]);
let b = a.0;
```

| Statement | GEN           | KILL  |
| --------- | ------------- | ----- |
| init `a`  | {a, a.0, a.1} | ∅     |
| `b = a.0` | {b}           | {a.0} |

Risultato: inizializzati = {a, a.1, b} — `a.0` è morto, ma `a.1` è ancora valido: muovere un figlio **non** uccide i fratelli [COMP-03_RUST_COMPILATION.pdf, Slide 25].

**Esempio 3 — errore di move parziale (slide):**
```rust
let a: (Vec<u32>, Vec<u32>) = (vec![1,2,3], vec![4,5,6]);
let b = a.0;
let c = a;   // ERRORE: use of partially moved value a
```

| Statement | IN            | GEN           | KILL          |
| --------- | ------------- | ------------- | ------------- |
| init `a`  | ∅             | {a, a.0, a.1} | ∅             |
| `b = a.0` | {a, a.0, a.1} | {b}           | {a.0}         |
| `c = a`   | {a, a.1, b}   | {c}           | {a, a.0, a.1} |

[COMP-03_RUST_COMPILATION.pdf, Slide 26]

#### 12.8.12 Il Quadro d'Insieme: Due Analisi, un Solo Framework
Il borrow checking di Rust consiste in **due analisi di dataflow interagenti** sul MIR: (1) Move/Initialization Analysis (ownership) e (2) Region Inference / NLL (lifetime). Entrambe sono basate sul CFG, **monotone**, e risolte tramite iterazione a punto fisso [COMP-03_RUST_COMPILATION.pdf, Slide 36].

**Struttura di dataflow condivisa (slide):**

| Aspetto | Move Analysis | Region Inference (NLL) |
|---|---|---|
| Dominio | insieme di move path | insieme di elementi di regione |
| Direzione | forward | forward (propagazione) |
| Reticolo | powerset | powerset |
| Transfer | GEN/KILL | unione tramite vincoli |
| Significato | "è inizializzato?" | "la regione è valida qui?" |
| Punto fisso | sì | sì |

Equazioni: Move Analysis — $OUT[n] = GEN[n] \cup (IN[n] - KILL[n])$, $IN[n] = \bigcup OUT[p]$; Region Inference — $R_a = LIVENESS_a \cup \bigcup \{R_b \cup end(b) \mid a{:}b\}$, a partire dai seed di liveness, propagando tramite i vincoli di outlives [COMP-03_RUST_COMPILATION.pdf, Slide 37]. A livello di grafo su cui si opera: la move analysis lavora sul CFG MIR, mentre la region inference lavora sul **DAG delle SCC** del grafo (Regioni, Outlives) [COMP-04_RUST_COMPILATION.pdf, Slide 18].

**Differenze e interazione (slide):** la move analysis **può rimuovere** informazione (i kill); la region inference **solo aggiunge** informazione (gli insiemi crescono monotonicamente). Dove interagiscono — ragionamento combinato: la move analysis dice `drop(x) ⇒ x non inizializzata`; la region inference dice `la regione r deve essere valida nel punto d'uso`; il **conflitto** emerge quando la regione dice "valido" mentre la move analysis dice "il valore non c'è più" [COMP-03_RUST_COMPILATION.pdf, Slide 38]:
```rust
let x = vec![1];
let r = &x;
drop(x);
*r; // errore: x è stata droppata mentre r è ancora "vivo" per la regione
```

#### 12.8.13 Esempio Svolto: Dangling Reference
```rust
fn bad() -> &i32 { let x = 10; &x }
```
MIR: `_1 = const 10;   _0 = &'r1 _1;   return` con `_0 : &'r0 i32`. Dall'assegnamento discende il vincolo **`'r1 : 'r0`** ("`'r1` outlives `'r0`": il prestito deve vivere almeno quanto il ritorno). Inferenza sui punti $[p_1]\,_1 = 10$, $[p_2]\,_0 = \&'r1\_1$, $[p_3]$ return: $'r1 = \{p_2, p_3\}$, $'r0 = \{p_3, \text{contesto del chiamante}\}$ ⇒ $'r1$ non copre tutti i punti di $'r0$ ⇒ **errore**. ⚠️ L'errore **non è locale al borrow**: emerge globalmente dopo la region inference (vincoli + CFG + drop ⇒ sistema insoddisfabile) [COMP-03_RUST_COMPILATION.pdf, Slide 15, 16].

#### 12.8.14 Le Regole di Ownership e Borrowing (riepilogo)
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
Sintesi: **alias XOR mutation**. Esempi:
```rust
let mut s = String::from("example");
let r1 = &mut s; let r2 = &mut s;   // NON compila — viola [B1]
let r1 = &s;     let r2 = &mut s;   // NON compila — viola [B2]
let r1 = &s;     let r2 = &s;       // OK — [B3]
```

### 12.9 Closure Capture Inference
Le closure Rust vengono compilate trasformandole in struct che memorizzano le variabili catturate. Il compilatore deve: identificare quali variabili dello scope circostante la closure usa (gli **upvar**); determinare come ciascuna è usata (letta, modificata, o consumata); decidere di conseguenza la modalità di cattura (per riferimento condiviso `&T`, per riferimento mutabile `&mut T`, o per valore/move). Questa analisi permette anche a `rustc` di inferire quale trait di closure la closure implementa: `Fn` (solo letture), `FnMut` (muta), `FnOnce` (consuma valori) [COMP-04_RUST_COMPILATION.pdf, Slide 23]. L'inferenza di cattura avviene durante la fase di type checking, specificamente nello stadio di type-checking dell'HIR — dopo il parsing e l'abbassamento a HIR, durante l'inferenza di tipo e la preparazione al borrow checking [COMP-04_RUST_COMPILATION.pdf, Slide 24].

Le closure sono desugarate in struct + implementazione di trait (si veda anche §12.3): `rustc` inferisce la modalità partendo da un borrow immutabile e rilassandola al bisogno — sola lettura ⇒ `&T` (**Fn**); mutazione ⇒ `&mut T` (**FnMut**); consumo (es. `drop`) ⇒ by value (**FnOnce**) [COMP-04_RUST_COMPILATION.pdf, Slide 25, 29].

**Meccanismo (slide):** un *upvar* è una variabile della funzione circostante che una closure cattura (una "variabile libera"). Il compilatore le identifica con un'analisi interna (`upvars_mentioned`). `euv::ExprUseVisitor` cammina il corpo della closure invocando le callback del trait **`Delegate`** (`consume`, `borrow`, `mutate`), ciascuna con un `cmt` (*Category, Mutability, Type*) che descrive origine, locazione e mutabilità della variabile. `InferBorrowKind` implementa questo trait e registra la modalità finale (`ByValue` / `ByRef{ImmBorrow, UniqueImmBorrow, MutBorrow}`) [COMP-04_RUST_COMPILATION.pdf, Slide 29, 30, 31].

**Esempi MIR (slide):**
```rust
// Lettura sola: fn invoke(f: impl Fn()) { f(); }  main: let x=10; invoke(|| println!("Hi {}", x));
bb0: { _1 = const 10_i32; _4 = &_1; _3 = closure { x: move _4 }; /* Fn */ }

// Mutazione: fn invoke(mut f: impl FnMut()) { f(); }  main: let mut x=10; invoke(|| { x += 10; ... });
bb0: { _1 = const 10_i32; _4 = &mut _1; _3 = closure { x: move _4 }; /* FnMut */ }

// Consumo: fn invoke(f: impl FnOnce()) { f(); }  main: let x=vec![21]; invoke(|| { drop(x); });
bb2: { _4 = closure { x: move _1 }; /* FnOnce, move di x */ }
```
[COMP-04_RUST_COMPILATION.pdf, Slide 26, 27, 28]

### 12.10 Ottimizzazioni MIR e Backend di Codegen

*   **Dal MIR ai binari (slide):** dopo il borrow checking sul MIR, il back-end di `rustc` esegue diversi passi per produrre l'output eseguibile. Sono supportati diversi backend: **LLVM IR** (tipicamente usato, stabile, pronto per ulteriori ottimizzazioni), **Cranelift IR** (più sperimentale), e **GCC IR** (IR interna del compilatore) [COMP-05_RUST_COMPILATION.pdf, Slide 4].
*   **Cranelift (slide):** un backend di codegen veloce, sicuro, relativamente semplice e innovativo. Prende in ingresso una IR generata da un qualche front-end e la compila in codice macchina eseguibile. Cranelift IR è anch'essa una IR da compilatore con blocchi base, valori in stile SSA e flusso di controllo, ma progettata per compilazione rapida e un'architettura di backend più semplice; l'obiettivo del backend Cranelift è particolarmente adatto per le build di debug/locali; il suo uso più comune è come compilatore per WebAssembly [COMP-05_RUST_COMPILATION.pdf, Slide 5].
*   **Fasi principali del codegen (slide):**
    1.  Pulizia post-borrowck: rimuove dal MIR tutte le informazioni usate per l'analisi ma non necessarie al codegen.
    2.  Preparazione del MIR "runtime" (inclusa la Drop Elaboration).
    3.  Ottimizzazioni MIR, ancora su codice generico.
    4.  **Monomorphization collection:** identifica tutti i tipi concreti che sono istanze di un tipo generico, per cui la monomorfizzazione deve essere eseguita.
    5.  Abbassamento (*lowering*) del MIR a una IR di codegen, per ciascun tipo concreto raccolto.
    6.  Backend di codegen: esegue una serie di pass di ottimizzazione, genera codice eseguibile e collega insieme un binario eseguibile.

    La complessità del codegen deriva da: supporto per più backend di codegen (il codice di codegen è generico rispetto all'implementazione del backend, con diversi livelli di astrazione); il codegen avviene in modo asincrono in un altro thread per prestazioni — il codegen effettivo è svolto da una libreria di terze parti (uno dei tre backend) [COMP-05_RUST_COMPILATION.pdf, Slide 6].
*   **Ottimizzazioni MIR (slide):** migliorano il MIR prima della generazione di codice del backend. Eseguite dopo il borrow checking, producono un MIR più pulito ed efficiente prima dell'abbassamento alla IR target — migliorano sia le prestazioni a runtime sia la velocità di compilazione (un MIR migliore produce codice macchina migliore e riduce il lavoro di ottimizzazione richiesto successivamente, es. da LLVM). Sono efficaci perché il MIR è ancora **generico**: le ottimizzazioni MIR avvengono prima della monomorfizzazione, quindi la versione migliorata è riusata per tutte le istanziazioni concrete di quella funzione o tipo generico. L'ottimizzazione MIR è implementata come sequenza di pass: alcuni sono obbligatori, alcuni validano solo invarianti o eseguono controlli, alcuni sono abilitati solo nelle build ottimizzate/release. Ottimizzazioni MIR tipiche semplificano e ripuliscono il CFG: propagazione di costanti, eliminazione di codice morto, propagazione di copie, semplificazione del CFG, e inlining. La query **`optimized_mir`** guida il processo [COMP-05_RUST_COMPILATION.pdf, Slide 7].
*   **Definire i pass di ottimizzazione (slide):** la funzione `run_optimization_passes` definisce la lista dei pass da eseguire e il loro ordine, in un array di pass; ciascun pass in tale array è una struct che implementa il trait `MirPass` (l'array è un array di trait object `&dyn MirPass`); tipicamente un pass è implementato in un proprio modulo del crate `rustc_mir_transform`. Esempi di pass: `CleanupPostBorrowck` (rimuove informazioni utili solo alle analisi, non al codegen); `ConstProp` (propagazione di costanti); il sistema è facilmente estensibile con nuovi pass di ottimizzazione [COMP-05_RUST_COMPILATION.pdf, Slide 8].
*   **Livello di ottimizzazione (slide):** `rustc main.rs -C opt-level=X` con `X` in `[0,1,2,3,s,z]`: `0` = nessuna ottimizzazione (compilazione veloce, buona per il debug); `1` = ottimizzazioni di base; `2` = build ottimizzata standard; `3` = ottimizzazioni aggressive; `s` = ottimizza per la dimensione del binario; `z` = ottimizza ancora di più per la dimensione. `cargo build` usa il livello 0; `cargo build --release` usa il livello 3 [COMP-05_RUST_COMPILATION.pdf, Slide 9].

### 12.11 Monomorfizzazione, Mono Item Collection e Codegen Units

*   **Implementazioni del polimorfismo universale a confronto (slide):**

| Linguaggio | Meccanismo di bound | Idea principale d'implementazione | Trade-off principale |
|---|---|---|---|
| Haskell | Type class | Dictionary passing + polimorfismo parametrico | Codice compatto, chiamate indirette a meno di ottimizzazione |
| Java | Interfacce / bound | Type erasure | Compatto, meno specificità di tipo a runtime, indirezione |
| C++ | Template / concept | Monomorfizzazione | Veloce/specializzato, code bloat |
| C# | Interfacce / vincoli | Generics reificati, ibrido shared/specialized | Più informazione di tipo a runtime, tipi valore efficienti |
[COMP-05_RUST_COMPILATION.pdf, Slide 10]
*   **Monomorfizzazione in Rust (slide):** Rust ha ampio supporto per i tipi generici, con polimorfismo universale esplicito e vincolato; i bound sono espressi tramite Trait. Rust **monomorfizza** tutti i tipi generici: il compilatore genera una copia distinta del codice di una funzione generica per ciascun tipo concreto necessario. La monomorfizzazione è il primo passo nel back-end del compilatore Rust: il MIR generico viene istanziato prima della generazione di codice. Stesso trade-off del C++: veloce/specializzato, ma con crescita del codice [COMP-05_RUST_COMPILATION.pdf, Slide 11].
*   **Collection (slide):** per ogni entità generica il compilatore deve raccogliere tutti i tipi concreti che la istanziano; il codice che esegue questa raccolta si chiama **monomorphization collector**, eseguito appena prima dell'abbassamento del MIR e del codegen. `rustc_codegen_ssa::base::codegen_crate` invoca la query `collect_and_partition_mono_items`, che esegue la raccolta di monomorfizzazione e poi la partiziona in codegen unit [COMP-05_RUST_COMPILATION.pdf, Slide 12].
*   **Mono item collection in dettaglio (modulo `rustc_monomorphize`, slide):** la raccolta dei mono item determina tutto ciò che deve generare codice di backend. Il collettore trova tutti gli item che produrranno artefatti LLVM/backend: funzioni, metodi, closure, `static`, e drop glue; deve anche scoprire ogni istanza monomorfizzata concreta di codice generico, inclusi i generics importati da altri crate. Un "mono item" rappresenta un artefatto di backend (qualcosa che diventa una funzione o un oggetto globale nella IR generata). I mono item dipendono l'uno dall'altro (es. una funzione che ne chiama un'altra), formando un **grafo diretto dei mono item**. L'algoritmo di raccolta lavora in due fasi: (1) trova le radici del grafo attraversando l'HIR del crate e raccogliendo gli item pubblici/non generici; (2) a partire da quelle radici, ispeziona ricorsivamente il MIR per scoprire tutti i mono item usati e le loro istanziazioni di tipo concrete [COMP-05_RUST_COMPILATION.pdf, Slide 13].
*   **Da dove emergono gli usi (slide):** gli usi sono scoperti dal MIR, non solo dalle chiamate esplicite. Gli archi nel grafo dei mono item sorgono da: chiamate a funzione/metodo, presa di riferimenti a funzioni, generazione di drop glue, cast di *unsizing* di trait-object (che richiedono vtable), e funzioni generiche/inline cross-crate. Rust supporta strategie di raccolta sia **lazy** sia **eager**: la raccolta lazy istanzia solo gli item effettivamente usati, minimizzando il codice generato; la raccolta eager istanzia più item in modo proattivo (utile per la compilazione incrementale e un comportamento di ricompilazione stabile) [COMP-05_RUST_COMPILATION.pdf, Slide 14]:
    ```rust
    fn print_val<T: Display>(x: T) { println!("{}", x); }
    fn call_fn(f: &dyn Fn(i32), x: i32) { f(x); }
    fn main() {
        let print_i32 = print_val::<i32>;
        call_fn(&print_i32, 0);
    }
    ```
    Il collettore valuta anche le costanti e traccia i "mentioned item": per evitare errori di compilazione dipendenti dalle ottimizzazioni, `rustc` traccia non solo gli item effettivamente usati dopo l'ottimizzazione, ma anche gli item che appaiono sintatticamente nel MIR ("mentioned items"), garantendo che i fallimenti di valutazione costante siano riportati in modo coerente anche se il codice morto viene poi ottimizzato via [COMP-05_RUST_COMPILATION.pdf, Slide 14].
*   **Codegen Units — CGU (slide):** la collezione di mono item generata dal monomorfizzatore viene partizionata in **Codegen Unit (CGU)** dal partizionatore. Una CGU è un insieme di coppie (mono-item, linkage) che diventa **un modulo LLVM**; il partizionatore decide quali funzioni, `static`, closure e monomorfizzazioni finiscono in quale CGU. Il partizionamento è cruciale per le prestazioni della compilazione incrementale: LLVM ricompila e ottimizza interi moduli, non singole funzioni — se una CGU cambia, l'intero modulo LLVM deve essere ricostruito e ri-ottimizzato da capo. Trade-off: molte piccole CGU ⇒ ricompilazione minima dopo modifiche, build incrementali più veloci, eseguibili più lenti (ottimizzazioni interprocedurali e inlining non possibili); poche grandi CGU ⇒ migliore ottimizzazione e inlining di LLVM, eseguibili più veloci [COMP-05_RUST_COMPILATION.pdf, Slide 16].
*   **Euristica basata sui moduli sorgente (slide):** il partizionatore bilancia questi obiettivi in competizione tramite un'euristica basata sui moduli sorgente: per ciascun modulo sorgente, `rustc` crea una CGU per il codice non-generico stabile e una CGU per le istanze monomorfizzate generiche volatili — isolando i cambiamenti causati da istanziazioni generiche e riducendo la ricompilazione non necessaria. I riferimenti generici sono particolarmente problematici per la compilazione incrementale: aggiungere o rimuovere un riferimento a una funzione generica può creare o eliminare istanze monomorfizzate, forzando la ricompilazione anche quando il corpo della funzione generica stessa non è cambiato. L'inlining influenza fortemente le decisioni di partizionamento: LLVM può fare inlining solo quando il corpo del chiamato è disponibile all'interno dello stesso modulo LLVM, quindi il partizionatore duplica le funzioni idonee tra CGU quando necessario — `rustc` tratta principalmente le funzioni marcate `#[inline]` come candidate per l'inlining cross-CGU [COMP-05_RUST_COMPILATION.pdf, Slide 17].
*   **Abbassamento del MIR a una IR di Codegen (slide):** dopo la raccolta dei mono item, `rustc` abbassa il MIR a una IR di backend (di norma LLVM IR, sebbene siano supportati anche Cranelift e GCC). La monomorfizzazione avviene durante questo processo di abbassamento; il codegen inizia in `codegen_crate` e raggiunge `codegen_mir`. La logica di abbassamento è divisa per costrutto MIR, con moduli diversi che gestiscono elementi diversi: `block` → blocchi base e terminatori (specialmente chiamate di funzione e unwind); `statement` → statement MIR; `operand` → operandi; `place` → riferimenti a memoria/place; `rvalue` → computazioni e valori temporanei [COMP-05_RUST_COMPILATION.pdf, Slide 18]. Semplici pass di analisi vengono eseguiti prima della traduzione: `rustc` esegue analisi leggere per produrre una LLVM IR più pulita — ad esempio rileva variabili in stile SSA così da poterle emettere direttamente in forma SSA invece di affidarsi interamente a ottimizzazioni LLVM come `mem2reg`. I blocchi base del MIR di norma mappano direttamente su blocchi base LLVM (sebbene operazioni come asserzioni, intrinsics, o chiamate complesse possano espandersi in più blocchi base LLVM); la generazione di codice specifica per LLVM usa intrinsics (operazioni built-in speciali di LLVM) e l'interfaccia builder [COMP-05_RUST_COMPILATION.pdf, Slide 19].

### 12.12 Il Sistema dei Tipi di Rust e il Type Checking

*   **Caratteristiche del sistema dei tipi (slide):** nominale; sostrutturale (affine); tipi di dato algebrici (`struct`, `enum`) con pattern matching; generics parametrici su tipi, costanti e lifetime; trait con funzioni, tipi e costanti associate; `impl Trait` per parametri anonimi e tipi di ritorno astratti; coercizioni fortemente limitate [COMP-06_RUST_COMPILATION.pdf, Slide 16]:
    ```rust
    struct ArrayRef<'a, T, const N: usize> { data: &'a [T; N] }
    ```
*   **Azioni del Type Checking (tabelle, slide):**

| Azione | Scopo |
|---|---|
| Controllo delle espressioni | Assicura la correttezza di tipo delle operazioni (compatibilità dell'assegnamento, tipi degli operandi, tipi di ritorno, coerenza dei rami) |
| Risoluzione dei metodi | Trova i metodi chiamabili (cerca in impl inherenti e di trait, catene di autoderef/autoref, valida il tipo del receiver) |
| Controllo degli obblighi di trait | Valida gli obblighi di trait (es. `T: Clone`, tutti gli obblighi impliciti, clausole `where`, supertrait) |
| Correttezza degli argomenti generici | Controlla argomenti di tipo/const/lifetime (arità, vincoli, tipi di const, well-formedness) |
| Controllo delle coercizioni | Valida conversioni implicite (`&mut T → &T`, array-to-slice, deref coercion, unsizing coercion) |
| Controllo dei pattern | Verifica match/destrutturazione (validità dei costruttori, tipi dei binding, supporto all'esaustività, coerenza delle varianti enum) |
| Controllo delle firme | Valida le interfacce di fn/closure (tipi dei parametri, tipi di ritorno, coerenza ABI, trait di chiamata delle closure `Fn`/`FnMut`/`FnOnce`) |
| Risoluzione degli operatori | Tipizzazione basata su trait degli operatori (`a + b` diventa `Add::add(a, b)`: esistenza del trait, compatibilità degli operandi, tipo del risultato) |
| Autoderef/autoref | Inserisce riferimenti/deref impliciti (`x.len()` può diventare `(*(*x)).len()`: legalità della catena di deref, inserimento del borrow, correttezza della mutabilità) |
| Controllo di well-formedness | Assicura tipi legali (`struct S<T: Copy> { x: T }`: bound, legalità ricorsiva, regole di varianza, sizedness, precondizioni di object safety) |
| Controllo di costruzione degli ADT | Valida enum/struct (`Some(3)` o `Point{x:1,y:2}`: esistenza dei campi, visibilità, tipi dei campi, arità) |
 [COMP-06_RUST_COMPILATION.pdf, Slide 17, 18, 19, 20]

### 12.13 Type Inference in rustc

*   **Panoramica (slide):** l'inferenza di tipo di Rust è un sistema multi-dominio di generazione di vincoli + risoluzione di vincoli su: tipi, lifetime (regioni), obblighi di trait, proiezioni, e const generics. Si basa sull'algoritmo standard di Hindley-Milner (HM), esteso in vari modi per gestire subtyping, region inference, e tipi higher-ranked [COMP-06_RUST_COMPILATION.pdf, Slide 20].
*   **Tabella delle azioni di inferenza (slide):**

| Azione di Inferenza | Scopo | Esempio | Vincolo |
|---|---|---|---|
| Inferenza variabile locale | Inferisce il tipo di una variabile | `let x = 3;` | `x: ?T1`; `?T1 = IntVar` (da `3`); `IntVar = i32` (fallback) |
| Inferenza tipo di ritorno | Inferisce il tipo del risultato | `fn f() { 3 }` | `return_type = body_type` |
| Inferenza argomenti generici | Inferisce parametri generici | `let v = Vec::new(); v.push(3);` | `v: Vec<?T1>`; `?T1 = i32` (dalla chiamata) |
| Inferenza parametri/risultato closure | Inferisce param/risultato closure | `let f = \|x\| x + 1;` | `x: ?T1`; `?T1: Add<i32>`; risultato `?T2 = i32` |
| Inferenza receiver di metodo | Inferisce la struttura del receiver | `x.push(3)` | `x: ?T1`; `?T1 = Vec<?T2>` (lookup metodo); `?T2 = i32` |
| Inferenza di riferimento | Inferisce il tipo del prestito | `let r = &x;` | `r: &'?R i32`; `region(x) ⊇ '?R` |
| Inferenza di lifetime | Inferisce l'estensione della regione | `let r = &x; println!("{}", r);` | `borrow_point ∈ '?R`; `use_point ∈ '?R` |
| Inferenza di reborrow | Restringe i prestiti annidati | `let y = &*x;` (con `x: &'a mut i32`) | `y: &'?R i32`; `'?R ⊆ 'a` |
| Inferenza obblighi di trait | Inferisce trait richiesti | `x.clone()` | `x: ?T1`; `?T: Clone` |
| Inferenza tipo associato | Risolve proiezioni | `Iterator::Item` | `<?T1 as Iterator>::Item = ?T2` |
| Unificazione dei rami | Unifica i tipi dei rami `match` | `let y = if cond {3} else {4};` | `arm1_type = ?T = arm2_type` |
| Inferenza array | Inferisce tipo/lunghezza elementi | `let a = [1,2,3];` | `a: [i32; 3]`; stesso tipo, lunghezza fissa |
| Inferenza HRTB | Inferisce lifetime higher-ranked | `for<'a> fn(&'a i32)` | variabili di regione legate, universi, placeholder |
| Inferenza subtyping/outlives | Inferisce contenimento di lifetime | `let x: &'static i32 = y;` | `y: &'?R i32`; `'?R: 'static` |

[COMP-06_RUST_COMPILATION.pdf, Slide 21, 22, 23]
*   **Vincoli di tipo generati (slide):**

| Tipo di vincolo | Significato |
|---|---|
| Uguaglianza | `?T = i32` |
| Subtyping | `'a : 'b` |
| Obblighi di trait | `?T : Clone` |
| Uguaglianza di proiezione | `<T as Trait>::Assoc = U` |
| Contenimento di regione | `'?R ⊆ 'a` |
| Uguaglianza di const | `?N = 4` |

[COMP-06_RUST_COMPILATION.pdf, Slide 24]

### 12.14 Unificazione del Primo Ordine e l'Algoritmo di Martelli–Montanari
*   **Unificazione del primo ordine (definizione formale, slide):** dato un insieme finito $G = \{s_1 \doteq t_1, \dots, s_n \doteq t_n\}$ di equazioni potenziali, l'algoritmo applica regole per trasformarlo in una **sostituzione**, cioè un insieme equivalente di equazioni della forma $\{x_1 \doteq u_1, \dots, x_m \doteq u_m\}$ dove $x_1, \dots, x_m$ sono variabili distinte e $u_1, \dots, u_m$ sono termini che non contengono nessuna delle $x_i$. Se non esiste soluzione, l'algoritmo termina con $\bot$. $G\{x \mapsto t\}$ denota l'operazione di sostituire tutte le occorrenze della variabile $x$ nel problema $G$ con il termine $t$. I simboli costanti sono considerati simboli funzionali con arità zero [COMP-06_RUST_COMPILATION.pdf, Slide 28].
*   **Algoritmo di Martelli–Montanari (1976–82, slide):** l'algoritmo calcola il **most general unifier**, cioè una sostituzione $S$ tale che $S(s_i) = S(t_i)$ per ogni $s_i \doteq t_i \in G$. Se non esiste soluzione, l'algoritmo termina con $\bot$ [COMP-06_RUST_COMPILATION.pdf, Slide 29]. `rustc` applica questo algoritmo formale per risolvere i sistemi di equazioni di vincolo sui tipi estratti dal codice [COMP-06_RUST_COMPILATION.pdf, Slide 12, 15.5 (vecchia numerazione)].
*   **Algoritmi di inferenza di tipo — panoramica (slide):** il sistema di tipi Hindley-Milner è alla base dell'inferenza; l'**Algoritmo W** è il più usato, ma non l'unico: è adatto a linguaggi puri, con effetti collaterali limitati all'introduzione di nuove variabili. L'**Algoritmo J** usa più effetti collaterali ed è più efficiente. L'**unificazione lazy** raccoglie tutti i vincoli visitando l'AST, per poi applicare l'unificazione in un secondo momento [COMP-06_RUST_COMPILATION.pdf, Slide 27].

### 12.15 Linting e Diagnostica degli Errori

*   **Cos'è un lint (slide):** in generale, un "lint" è uno strumento per migliorare il codice sorgente. `rustc` contiene numerosi lint, eseguiti durante la compilazione; possono produrre un warning, un errore, o nulla, a seconda della configurazione [COMP-06_RUST_COMPILATION.pdf, Slide 4].
*   **Lint vs diagnostiche fisse (slide):** alcuni messaggi sono emessi tramite lint, il cui livello è controllabile dall'utente; la maggior parte delle diagnostiche sono invece "hard-coded" e non regolabili. Di solito è ovvio se una diagnostica debba essere "fissa" o un lint, ma esistono zone grigie. Esempi: gli errori del borrow checker sono diagnostiche fisse (l'utente non può silenziare il borrow checker); il codice morto (*dead code*) è un lint (renderlo un errore fisso renderebbe il refactoring molto doloroso); i lint "future-incompatible" sono silenziabili ma verranno eventualmente trasformati in errori fissi [COMP-06_RUST_COMPILATION.pdf, Slide 5].
*   **Livelli dei lint:** `allow` (non fa nulla) → `expect` (verifica che un lint specifico venga emesso, sopprimendolo se emesso, warning se **non** emesso — utile in debug o prima di eliminare un lint) → `warn` (produce un warning, la compilazione prosegue) → `force-warn` (come `warn`, ma il livello non è modificabile) → `deny` (produce un errore) → `forbid` (come `deny`, ma il livello non è modificabile). Ogni lint ha un livello di default, e il compilatore ha un livello di warning di default [COMP-06_RUST_COMPILATION.pdf, Slide 6, 7].
*   **Configurazione:** flag `-A/-W/--force-warn/-D/-F` per trasformare uno o più lint nel livello desiderato; attributi (`#![warn(missing_docs)]` a livello di crate/modulo, `#[allow(unused_mut, reason = "…")]` con motivazione mostrata all'emissione); `rustc --cap-lints LEVEL` imposta il "livello di cap" — il massimo livello per tutti i lint (usato da Cargo quando compila le dipendenze, passando `--cap-lints allow`, così i loro warning non inquinano il build) [COMP-06_RUST_COMPILATION.pdf, Slide 8, 9, 10, 11].
*   **Lint group (slide):** `rustc` ha il concetto di gruppo di lint, per attivare più warning tramite un unico nome — es. `nonstandard-style` imposta insieme `non-camel-case-types`, `non-snake-case`, `non-upper-case-globals`. Gruppi principali: `warnings` (tutti i lint impostati per emettere warning); `deprecated-safe` (funzioni erroneamente marcate `safe` in passato); `future-incompatible` (codice con problemi di compatibilità futura); `keyword-idents` (identificatori che diventeranno keyword in edizioni successive); `nonstandard-style` (violazioni delle convenzioni di naming); `refining-impl-trait`; `unused` (cose dichiarate ma non usate, o sintassi in eccesso) [COMP-06_RUST_COMPILATION.pdf, Slide 12].
*   **Quando vengono eseguiti i lint — cinque momenti distinti (tabella, slide):**

| Tipo | Momento | Informazione disponibile | Uso tipico |
|---|---|---|---|
| Pre-expansion | Prima dell'espansione delle macro | AST grezzo, contesto limitato | compatibilità di edizione e casi sensibili alle macro, come `keyword_idents` |
| Early lint | Dopo l'espansione delle macro, prima dell'abbassamento | AST risolto, ma i tipi non sono ancora completi | lint puramente sintattici, come `unused_parens` |
| Late lint | Verso la fine dell'analisi, sull'HIR | HIR, tipi e semantica più ricca | controlli idiomatici o semantici, come `non_snake_case` o `invalid_value` |
| MIR / inline | Dentro il MIR, il borrowck o percorsi di codice specifici | stato specializzato del sottosistema | `arithmetic_overflow`, `unused_mut`, lint complessi di future-compat |
| Driver / tool lint | Registrazione esterna, esecuzione nelle stesse fasi di cui sopra | dipende dal pass registrato | Clippy e strumenti personalizzati via `register_lints` e `rustc_driver` |

I lint girano in fasi di compilazione diverse a seconda del loro significato; molti lint sono raggruppati in pass eseguiti con un unico visitor, altri sono collocati dove servono nel codice [COMP-06_RUST_COMPILATION.pdf, Slide 13].
*   **Clippy (slide):** è la collezione ufficiale di lint di Rust — un ampio insieme di analisi statiche aggiuntive costruite sopra `rustc`, che aiutano gli sviluppatori a scrivere codice Rust più idiomatico, corretto, efficiente e manutenibile. Concettualmente: `rustc` verifica se il programma è Rust **valido**; Clippy verifica se è **buon** Rust. Clippy si integra direttamente nell'infrastruttura del compilatore, piuttosto che operare come parser o analizzatore separato: usa la stessa architettura di linting di `rustc`, registrando pass di lint personalizzati tramite il driver del compilatore ed eseguendoli dentro la normale pipeline di lint [COMP-06_RUST_COMPILATION.pdf, Slide 14].

### 12.16 Type Inference in uHaskell (Algorithm W)

`uHaskell` è un sottoinsieme di Haskell usato per spiegare l'inferenza di tipo senza considerare l'overloading (sia Haskell sia ML hanno overloading, qui non considerato) [COMP-06_RUST_COMPILATION.pdf, Slide 34]:
```
<decl> ::= <name> <pat> = <exp>
<pat>  ::= Id | (<pat>, <pat>) | <pat> : <pat> | []
<exp>  ::= Int | Bool | [] | Id | (<exp>) | <exp> <op> <exp> | <exp> <exp>
         | (<exp>, <exp>) | if <exp> then <exp> else <exp>
```

**Algoritmo di Type Inference (slide "Type Inference Algorithm"):** (1) analizza il programma per costruire il parse tree; (2) assegna variabili di tipo ai nodi dell'albero; (3) genera vincoli — dall'ambiente (costanti, operatori built-in, funzioni note) e dalla forma del parse tree (nodi di applicazione e astrazione); (4) risolve i vincoli tramite unificazione; (5) determina i tipi delle dichiarazioni top-level [COMP-06_RUST_COMPILATION.pdf, Slide 36].

*   **Vincoli dai nodi di applicazione (slide):** per l'applicazione `f x`: il tipo di `f` ($t_0$) deve essere dominio → codominio; il dominio deve essere il tipo dell'argomento `x` ($t_1$); il codominio deve essere il risultato dell'applicazione ($t_2$). Vincolo: $t_0 = t_1 \to t_2$ [COMP-06_RUST_COMPILATION.pdf, Slide 39].
*   **Vincoli dalle astrazioni (slide):** per la dichiarazione `f x = e`: il tipo di `f` ($t_0$) deve essere dominio → codominio; il dominio è il tipo della variabile astratta `x` ($t_1$); il codominio è il tipo del corpo `e` ($t_2$). Vincolo: $t_0 = t_1 \to t_2$ [COMP-06_RUST_COMPILATION.pdf, Slide 40].

**Esempio svolto `f x = 2 + x`:** il tipo di `+` è `Int → Int → Int` (con overloading sarebbe `Num a => a → a → a`); `2` ha tipo `Int`; poiché `+` è applicato a `x`, serve `x :: Int`; dunque `f x = 2 + x` ha tipo `Int → Int` [COMP-06_RUST_COMPILATION.pdf, Slide 35]. Vincoli generati: $t_0 = t_1 \to t_6$, $t_4 = t_1 \to t_6$, $t_2 = t_3 \to t_4$, $t_2 = Int \to Int \to Int$, $t_3 = Int$; risolvendo per unificazione: $t_3 = Int$, $t_4 = Int \to Int$, $t_1 = Int$, $t_6 = Int$ ⇒ **`f :: Int → Int`** [COMP-06_RUST_COMPILATION.pdf, Slide 41, 42, 43].

**Tipi polimorfi — esempio `f g = g 2`:** vincoli $t_0 = t_1 \to t_4$, $t_1 = t_3 \to t_4$, $t_3 = Int$; risolvendo: $t_0 = (Int \to t_4) \to t_4$, $t_1 = Int \to t_4$, $t_3 = Int$ ⇒ **`f :: (Int → t₄) → t₄`**, con $t_4$ variabile **non vincolata** che diventa polimorfa [COMP-06_RUST_COMPILATION.pdf, Slide 44–48]. Uso di funzioni polimorfe: `add x = 2 + x` (`add :: Int -> Int`) applicata come `f add` dà `4 :: Int`; `isEven x = mod (x, 2) == 0` (`isEven :: Int -> Bool`) applicata come `f isEven` dà `True :: Bool` [COMP-06_RUST_COMPILATION.pdf, Slide 49].

**Datatypes e clausole multiple (slide):** le funzioni possono avere più clausole; l'inferenza inferisce un tipo separato per ciascuna clausola, poi le combina imponendo il vincolo che tutte le clausole abbiano lo stesso tipo; le chiamate ricorsive hanno lo stesso tipo della definizione. Esempio:
```haskell
length [] = 0
length (x:rest) = 1 + (length rest)
```
Vincoli: $t_0 = t_3 \to t_{10}$, $t_3 = t_2$, $t_3 = [t_1]$, $t_6 = t_9 \to t_{10}$, $t_4 = t_5 \to t_6$, $t_4 = Int \to Int \to Int$, $t_5 = Int$, $t_0 = t_2 \to t_9$; risolvendo ⇒ $t_0 = [t_1] \to Int$ ⇒ **`length :: [t₁] → Int`** [COMP-06_RUST_COMPILATION.pdf, Slide 50–54].

### 12.17 Altri Argomenti Correlati a Rust

*   **RustBelt (slide):** un lavoro di ricerca (*RustBelt: Securing the Foundations of the Rust Programming Language*) che fornisce la prima dimostrazione formale (meccanicamente verificata) di sicurezza per un linguaggio che rappresenta un sottoinsieme realistico di Rust. Rust estende il proprio type system ownership-based tramite librerie che internamente usano funzionalità `unsafe`; la dimostrazione è estensibile — per ogni nuova libreria Rust che usa funzionalità `unsafe`, si può stabilire quale condizione di verifica deve soddisfare affinché sia considerata un'estensione sicura del linguaggio. Il lavoro applica questa verifica ad alcune delle librerie più importanti dell'ecosistema Rust [COMP-06_RUST_COMPILATION.pdf, Slide 31].
*   **Polonius (slide):** una proposta di nuovo borrow checker, estensione conservativa dell'approccio NLL, basata su un formalismo *alias-based*. Il cambiamento principale: le regioni sono insiemi di **prestiti** (*loans*), non insiemi di punti del programma — un tipo come `&'a i32` con questo approccio significa che `'a` corrisponde a un insieme di espressioni di prestito (`&x` o `&mut v`); invalidare i termini di uno qualsiasi dei prestiti in `'a` invaliderebbe il riferimento `r` [COMP-06_RUST_COMPILATION.pdf, Slide 32].
*   **Studio empirico sui bug specifici di Rust in `rustc` (slide):** uno studio (J. ACM, Vol. 37, No. 4, Agosto 2025) analizza i bug di `rustc` dovuti a caratteristiche uniche di Rust (trait solving, borrow checking, ottimizzazioni specifiche), basato su issue e fix segnalati tra il 2022 e il 2024, con revisione manuale di 301 issue valide. Risultati principali: (1) i bug di `rustc` derivano principalmente dal sistema di tipi e dal modello dei lifetime, con errori frequenti nei moduli HIR e MIR a causa della complessità di checker e ottimizzazioni; (2) i test case che rivelano bug coinvolgono spesso feature instabili, usi avanzati di trait, annotazioni di lifetime, API standard, e specifici livelli di ottimizzazione; (3) sia programmi validi sia invalidi possono innescare bug, e gli strumenti di testing esistenti faticano a rilevare errori non-crash, sottolineando la necessità di ulteriori progressi nel testing di `rustc` [COMP-06_RUST_COMPILATION.pdf, Slide 33].

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