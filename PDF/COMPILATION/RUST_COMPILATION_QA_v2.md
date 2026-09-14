# Rust Compilation — Domande e Risposte per l'esame orale

## 1. Obiettivi di Rust e compilazione

### 1.1 Qual è l'obiettivo principale di Rust?

Rust vuole garantire **memory safety**, controllo dell'ownership e gestione sicura della memoria senza affidarsi a un garbage collector.

Il compilatore verifica staticamente proprietà come:

- ownership;
    
- borrowing;
    
- lifetimes;
    
- assenza di use-after-free;
    
- assenza di double free;
    
- correttezza dei move;
    
- compatibilità tra borrow mutabili e immutabili.
    

Una caratteristica fondamentale è che molti errori vengono individuati **a compile time**.

---

### 1.2 Che cos'è RAII?

RAII, _Resource Acquisition Is Initialization_, è il principio secondo cui la durata di una risorsa è associata alla durata di un oggetto.

In Rust questo principio è strettamente collegato all'ownership:

```rust
{
    let v = Vec::new();
}
```

Quando `v` esce dallo scope, il suo `Drop` viene eseguito automaticamente.

---

### 1.3 Perché Rust non ha bisogno di garbage collection?

Perché la gestione della memoria viene determinata principalmente tramite:

- ownership;
    
- borrowing;
    
- lifetimes;
    
- `Drop`.
    

Il compilatore può quindi stabilire staticamente quando una risorsa può essere liberata.

---

# 2. Ownership, Move e Borrowing

### 2.1 Che cos'è l'ownership?

Ogni valore possiede un unico owner.

Quando l'owner esce dal proprio scope, il valore viene distrutto.

---

### 2.2 Che cosa succede durante un move?

Consideriamo:

```rust
let x = String::from("hello");
let y = x;
```

Il valore viene trasferito da `x` a `y`.

Dopo il move:

```rust
println!("{}", x);
```

non è valido.

Il compilatore deve quindi sapere in quali punti del programma una variabile è ancora inizializzata.

---

### 2.3 Che differenza c'è tra Copy e Move?

Un tipo `Copy` viene copiato implicitamente:

```rust
let x = 10;
let y = x;
println!("{}", x);
```

`x` continua a essere utilizzabile.

Un tipo non-`Copy`, come `String`, viene invece trasferito tramite move.

---

### 2.4 Che cos'è un borrow?

Un borrow permette di utilizzare un valore senza trasferirne l'ownership:

```rust
let x = String::from("hello");
let r = &x;
```

Il borrow può essere:

```rust
&T
```

oppure:

```rust
&mut T
```

---

### 2.5 Qual è la regola fondamentale dei borrow?

In generale:

- possono esistere più borrow immutabili contemporaneamente;
    
- oppure un solo borrow mutabile;
    
- non possono coesistere un borrow mutabile e borrow immutabili incompatibili.
    

Il borrow checker verifica queste regole sul MIR.

---

# 3. Dalle sorgenti al codice macchina

### 3.1 Qual è il percorso generale di compilazione di Rust?

Una visione semplificata è:

```text
Source
  ↓
Lexer
  ↓
Parser
  ↓
AST
  ↓
Macro expansion / Name resolution
  ↓
HIR
  ↓
THIR
  ↓
MIR
  ↓
Borrow checking
  ↓
MIR optimization
  ↓
Monomorphization
  ↓
Codegen IR
  ↓
LLVM / Cranelift / GCC
  ↓
Machine code
  ↓
Executable
```

Il percorso attraverso LLVM è quello tipico, ma `rustc` supporta anche altri backend.

---

### 3.2 Perché Rust usa così tante rappresentazioni intermedie?

Perché ogni IR rende più semplice un particolare tipo di analisi.

In particolare:

|IR|Scopo principale|
|---|---|
|AST|rappresentazione sintattica|
|HIR|struttura adatta alle analisi semantiche|
|THIR|struttura tipata|
|MIR|controllo di flusso, ownership, borrow checking|
|LLVM IR|code generation e ottimizzazione|

---

# 4. AST, HIR e THIR

### 4.1 Perché l'AST non è sufficiente per il borrow checker?

L'AST è principalmente sintattico.

Il borrow checker deve invece ragionare su:

- controllo di flusso;
    
- move;
    
- inizializzazione;
    
- borrow;
    
- lifetime;
    
- punti precisi del programma.
    

Il MIR rende queste informazioni molto più esplicite.

---

### 4.2 Che cos'è l'HIR?

HIR significa **High-level Intermediate Representation**.

È una rappresentazione più vicina alla struttura semantica del programma rispetto all'AST.

---

### 4.3 Che cos'è il THIR?

THIR significa **Typed High-level Intermediate Representation**.

Contiene informazioni di tipo più esplicite e rappresenta una forma già fortemente tipata del programma.

---

### 4.4 Perché serve il passaggio THIR → MIR?

Perché il MIR deve trasformare strutture ad alto livello in una rappresentazione basata su:

- basic block;
    
- statement;
    
- terminator;
    
- local;
    
- place;
    
- operand;
    
- rvalue.
    

Il risultato è adatto alle analisi di controllo di flusso e ownership.

---

# 5. Desugaring

### 5.1 Che cos'è il desugaring?

È la trasformazione di una costruzione sintattica ad alto livello in una forma più esplicita.

Per esempio:

```rust
for x in iterator {
    body
}
```

viene concettualmente trasformato in una struttura basata sull'iteratore e su `next()`.

---

### 5.2 Perché il desugaring è importante?

Perché permette al compilatore di lavorare con un insieme più piccolo di costrutti fondamentali.

Il desugaring avviene a più livelli.

Alcune trasformazioni vengono effettuate durante HIR lowering, altre durante THIR construction e altre ancora emergono esplicitamente nel MIR.

---

### 5.3 Quali informazioni possono essere introdotte durante il lowering?

Il lowering può introdurre:

- temporanei;
    
- borrow impliciti;
    
- move;
    
- drop;
    
- ordine di valutazione esplicito;
    
- controllo di flusso.
    

Per questo il MIR type checking è comunque necessario anche se il THIR era già tipato.

---

# 6. MIR

### 6.1 Che cos'è il MIR?

MIR significa **Mid-level Intermediate Representation**.

È una rappresentazione intermedia basata su un control-flow graph, particolarmente adatta alle analisi di:

- ownership;
    
- move;
    
- initialization;
    
- borrow;
    
- lifetime;
    
- drop.
    

---

### 6.2 Che cos'è un basic block?

Un basic block è una sequenza di istruzioni con:

- un punto di ingresso;
    
- un terminatore finale;
    
- nessun salto interno.
    

I terminatori determinano il controllo di flusso verso altri basic block.

---

### 6.3 Che cos'è un terminator?

È un'operazione che termina un basic block e determina il controllo successivo.

Esempi:

- `Goto`;
    
- `SwitchInt`;
    
- `Call`;
    
- `Return`;
    
- `Drop`;
    
- `Assert`.
    

---

### 6.4 Che cos'è una Place nel MIR?

Una `Place` identifica una posizione in memoria.

Può rappresentare, concettualmente:

```text
x
x.field
x[index]
*deref
```

È importante perché il borrow checker deve ragionare non solo sui valori, ma sulle **locazioni** che vengono prese in prestito o modificate.

---

### 6.5 Che cos'è un Rvalue?

Un rvalue descrive la produzione di un valore.

Per esempio:

```rust
x + y
```

può essere rappresentato nel MIR attraverso un'operazione che costruisce il risultato dell'addizione.

---

# 7. Query system di rustc

### 7.1 Come organizza rustc le proprie analisi?

`rustc` utilizza un sistema di **query demand-driven**.

Una query può richiedere il risultato di un'altra query e il compilatore calcola ricorsivamente le dipendenze necessarie.

I risultati vengono memorizzati e possono essere riutilizzati.

---

### 7.2 Perché il query system è importante?

Perché permette:

- caching;
    
- incremental compilation;
    
- calcolo solo delle informazioni necessarie;
    
- gestione delle dipendenze tra fasi del compilatore.
    

---

### 7.3 Quali query sono importanti per il MIR?

Tra le query concettualmente importanti troviamo:

```text
mir_built
optimized_mir
mir_borrowck
```

`mir_borrowck` rappresenta l'ingresso principale al borrow checker.

---

# 8. MIR Visitor

### 8.1 A cosa serve il Visitor del MIR?

Permette di attraversare sistematicamente una rappresentazione MIR senza dover implementare manualmente la visita di ogni componente.

Esistono forme come:

```text
Visitor
MutVisitor
```

per attraversamento rispettivamente in sola lettura o modificabile.

---

### 8.2 Perché il Visitor è utile nelle analisi?

Perché molte analisi devono visitare:

- basic block;
    
- statement;
    
- terminator;
    
- operand;
    
- place;
    
- rvalue.
    

Il Visitor fornisce una struttura uniforme.

---

# 9. Dataflow analysis

### 9.1 Che cos'è una dataflow analysis?

È un'analisi che propagava informazioni lungo il control-flow graph.

Esempi:

- variabili inizializzate;
    
- variabili non inizializzate;
    
- liveness;
    
- loan attivi;
    
- move.
    

---

### 9.2 Che cos'è il modello GEN/KILL?

Una trasformazione può:

- **GEN**: aggiungere informazioni;
    
- **KILL**: rimuovere informazioni.
    

Per esempio, nell'analisi dei move:

```text
x = value
```

può rendere `x` inizializzato.

Un:

```text
move x
```

può invece rendere `x` non più utilizzabile.

---

### 9.3 Che cos'è un fixed point?

L'analisi viene ripetuta finché i risultati non cambiano più.

Concettualmente:

```text
inizializzazione
      ↓
propagazione
      ↓
nuovi risultati
      ↓
propagazione
      ↓
...
      ↓
fixed point
```

---

### 9.4 Qual è il dominio della move analysis?

Il dominio può essere visto come un insieme di **move paths**.

La regione inference utilizza invece un insieme di **region elements**.

I due problemi hanno una struttura matematica molto simile:

||Move analysis|Region inference|
|---|---|---|
|Dominio|move paths|region elements|
|Direzione|forward|forward|
|Lattice|powerset|powerset|
|Transfer|GEN/KILL|propagazione|
|Fixed point|sì|sì|

Questa analogia è esplicitamente evidenziata nelle slide.

---

# 10. Drop Elaboration

### 10.1 Perché serve la Drop Elaboration?

Il compilatore deve sapere **quando è sicuro eseguire un Drop**.

Un valore può essere:

- inizializzato;
    
- parzialmente inizializzato;
    
- spostato;
    
- non inizializzato.
    

Quindi non basta inserire semplicemente un `Drop` alla fine dello scope.

---

### 10.2 Che cos'è un drop obligation?

È l'obbligo strutturale di distruggere una certa parte di un valore quando questa è stata inizializzata.

---

### 10.3 Che cosa sono i drop flags?

Sono informazioni che permettono di sapere dinamicamente se una determinata parte del valore deve essere distrutta.

Questo è importante nei casi di:

- move;
    
- partial move;
    
- inizializzazione condizionale;
    
- enum con varianti diverse.
    

---

### 10.4 Che cos'è il drop glue?

Il **drop glue** è il codice necessario per distruggere correttamente un valore.

Concettualmente:

```text
Drop T
 ↓
distruggi T
 ↓
distruggi ricorsivamente i campi
```

---

# 11. Borrow checker

### 11.1 Qual è l'entry point del borrow checker?

La query:

```text
mir_borrowck
```

nel crate `rustc_borrowck`.

Il borrow checker opera sul MIR.

---

### 11.2 Quali sono le principali fasi del borrow checker?

In forma semplificata:

```text
MIR
 ↓
copia/preparazione
 ↓
replace_regions_in_mir
 ↓
move/init analysis
 ↓
MIR type check
 ↓
region inference
 ↓
borrow set
 ↓
final validation
```

Le slide indicano esplicitamente questa sequenza.

---

### 11.3 Perché viene eseguito un secondo type check sul MIR?

Perché il MIR è stato ottenuto dal THIR tramite un lowering che:

- introduce nuovi costrutti;
    
- introduce temporanei;
    
- esplicita borrow e move;
    
- modifica l'ordine delle operazioni;
    
- introduce invarianti specifiche del MIR.
    

Quindi il passaggio THIR → MIR non è banalmente type-preserving e il MIR deve essere verificato indipendentemente.

---

# 12. Move Analysis

### 12.1 Che cosa deve sapere il compilatore dopo un move?

Deve sapere quali parti del valore non sono più inizializzate/utilizzabili.

Per esempio:

```rust
let x = String::from("hello");
let y = x;
```

dopo il move di `x`, l'analisi deve rappresentare il fatto che `x` non può essere utilizzato normalmente.

---

### 12.2 Che cosa sono i move paths?

Un move path rappresenta una parte di un valore che può essere spostata indipendentemente.

Questo permette di gestire anche i **partial moves**.

---

### 12.3 Che cos'è un partial move?

Per esempio, concettualmente:

```rust
struct S {
    a: String,
    b: String
}
```

può essere possibile spostare `a` senza necessariamente spostare `b`.

Il compilatore deve quindi ragionare a livello di parti del valore.

---

# 13. Lifetime e Region

### 13.1 Lifetime e region sono la stessa cosa?

Non esattamente.

**Lifetime** è il concetto linguistico con cui il programmatore descrive la durata di un riferimento.

**Region** è la rappresentazione interna usata dal compilatore.

---

### 13.2 Come rappresenta rustc una region NLL?

Una region può essere rappresentata come un insieme di **punti del control-flow graph** nei quali il riferimento deve essere valido.

Quindi non coincide necessariamente con uno scope lessicale.

---

### 13.3 Che cosa significa NLL?

NLL significa **Non-Lexical Lifetimes**.

L'idea è che la validità di un borrow possa terminare nel punto della sua ultima utilizzazione effettiva, invece di coincidere necessariamente con la fine dello scope lessicale.

---

### 13.4 Esempio di NLL

```rust
let mut x = 10;

let r = &x;
println!("{}", r);

let m = &mut x;
*m += 1;
```

Il borrow immutabile può terminare dopo l'ultima utilizzazione di `r`.

Quindi il mutable borrow può iniziare successivamente.

---

### 13.5 Quando un programma viene rifiutato?

Se il borrow immutabile è ancora vivo quando viene creato/usato il borrow mutabile:

```rust
let mut x = 10;

let r = &x;
let m = &mut x;

println!("{}", r);
*m += 1;
```

`r` è ancora live durante il suo utilizzo, quindi i due borrow sono incompatibili.

---

# 14. Region inference

### 14.1 Quali sono le fasi della region inference?

Le fasi principali sono:

1. identificare le universal regions;
    
2. sostituire le regioni con variabili di inferenza;
    
3. generare i vincoli;
    
4. risolvere i vincoli;
    
5. verificare type tests e universal regions.
    

---

### 14.2 Che cosa sono le universal regions?

Sono le lifetime visibili nella firma della funzione, per esempio:

```rust
fn f<'a, 'b>(...)
```

e lifetime speciali come:

```rust
'static
```

Sono universalmente quantificate: il compilatore deve garantire che la funzione sia corretta per tutte le istanziazioni ammissibili.

---

### 14.3 Che cosa fa `replace_regions_in_mir`?

Sostituisce le regioni presenti nel MIR con nuove variabili di inferenza.

Questo permette di ignorare temporaneamente le lifetime lessicali e ricostruire la loro durata in modo sensibile al control flow.

---

### 14.4 Quali tipi di constraint vengono generati?

Principalmente:

- **liveness constraints**;
    
- **outlives constraints**;
    
- **member constraints**.
    

Inoltre vengono raccolti i **type tests**.

---

### 14.5 Che cos'è un outlives constraint?

Un vincolo:

```text
'a: 'b
```

significa che `'a` deve vivere almeno quanto `'b`.

---

### 14.6 Che cos'è un liveness constraint?

Indica che una region deve essere valida in determinati punti del CFG.

Per esempio, se:

```rust
*y
```

usa il riferimento `y`, la regione associata a `y` deve contenere quel punto.

---

### 14.7 Come vengono propagate le regioni?

Per un vincolo:

```text
'a: 'b
```

la propagazione può essere vista concettualmente come:

```text
'a ← 'a ∪ 'b ∪ {end('b)}
```

e viene ripetuta fino al fixed point.

---

# 15. SCC e grafo dei vincoli

### 15.1 Come vengono rappresentati i vincoli outlives?

Come un grafo diretto:

```text
region → region
```

dove un arco rappresenta un vincolo di outlives.

---

### 15.2 Perché servono le SCC?

Se il grafo contiene un ciclo:

```text
'a → 'b
 ↑     ↓
 └─────┘
```

le regioni coinvolte devono essere trattate insieme.

Il compilatore calcola quindi le **Strongly Connected Components**.

---

### 15.3 Perché dopo le SCC si ottiene un DAG?

Collassando ogni SCC in un singolo nodo, i cicli vengono eliminati.

Il grafo risultante è un:

```text
DAG
```

e la propagazione dei constraint diventa più efficiente.

---

# 16. Type Tests

### 16.1 Che cos'è un type test?

È un'obbligazione che riguarda la correttezza di un tipo in presenza di region/lifetime.

Il MIR type checker raccoglie questi test durante la generazione dei constraint.

---

### 16.2 Perché i type test vengono verificati dopo la region inference?

Perché il solver delle region lavora principalmente su:

```text
insiemi di punti del CFG
```

mentre i tipi possono essere molto più complessi:

- generics;
    
- tipi annidati;
    
- projections;
    
- riferimenti;
    
- subtyping.
    

Incorporare tutta questa complessità nel solver renderebbe la risoluzione più difficile e meno efficiente.

---

### 16.3 Che cosa verifica tipicamente un type test?

Può verificare che un tipo sia well-formed rispetto alle lifetime inferite.

Per esempio:

```text
T: 'a
```

richiede che i riferimenti contenuti in `T` siano validi abbastanza a lungo per `'a`.

---

# 17. Universal Regions e "too big" check

### 17.1 Perché bisogna controllare le universal regions dopo l'inferenza?

Perché l'inferenza non deve produrre relazioni tra lifetime più forti di quelle consentite dalla firma della funzione.

Per esempio, se l'inferenza implica una relazione tra universal regions che non era dichiarata, il compilatore deve rifiutare il programma.

Questo è il controllo delle regioni "too big".

---

# 18. Two-phase borrows

### 18.1 Che cos'è un two-phase borrow?

È una forma speciale di mutable borrow che ha due fasi:

```text
reservation
     ↓
activation
```

Durante la fase di reservation il borrow ha regole più rilassate, permettendo alcuni pattern altrimenti problematici.

---

### 18.2 Perché servono?

Permettono espressioni come:

```rust
vec.push(vec.len());
```

La chiamata richiede un `&mut Vec`, ma l'argomento usa contemporaneamente `vec` tramite un borrow condiviso.

Il two-phase borrow rende questo pattern valido.

---

### 18.3 Quali sono i due punti fondamentali?

**Reservation point**

```text
&mut vec
```

viene prenotato.

**Activation point**

Il borrow diventa effettivamente un mutable borrow pienamente attivo.

Nel frattempo può essere consentito un borrow condiviso compatibile con le regole dei two-phase borrows.

---

### 18.4 Come appare concettualmente nel MIR?

Il PDF mostra una struttura equivalente a:

```text
_2 = &mut (*_1);   // reservation

_3 = &(*_1);       // shared borrow
_4 = Vec::len(_3);

_0 = Vec::push(_2, _5); // activation
```

Quindi il MIR rende esplicite le diverse fasi del borrow.

---

# 19. Closure

### 19.1 Come vengono rappresentate internamente le closure?

Una closure può essere vista concettualmente come una struct che contiene le variabili catturate.

Per esempio:

```rust
let y = 10;
let f = |x| x + y;
```

può essere pensata come:

```text
struct Closure {
    y: i32
}
```

con un metodo che implementa la chiamata.

Le trasformazioni interne di rustc non sono necessariamente codice Rust legalmente scrivibile dall'utente.

---

### 19.2 Che cosa sono gli upvars?

Gli **upvars** sono le variabili provenienti dall'ambiente esterno che una closure cattura.

Per esempio:

```rust
let x = 10;

let f = || println!("{}", x);
```

`x` è un upvar della closure.

---

### 19.3 Quali modalità di capture esistono?

La closure può catturare una variabile:

- tramite shared reference;
    
- tramite mutable reference;
    
- by value / move.
    

Il compilatore determina automaticamente quale modalità è necessaria.

---

# 20. Fn, FnMut e FnOnce

### 20.1 Qual è la differenza tra Fn, FnMut e FnOnce?

In modo semplificato:

|Trait|Comportamento|
|---|---|
|`Fn`|legge l'ambiente|
|`FnMut`|modifica l'ambiente|
|`FnOnce`|consuma valori dell'ambiente|

---

### 20.2 Esempio di Fn

```rust
let x = 10;

let f = || println!("{}", x);
```

La closure legge `x`.

Il compilatore può quindi catturarlo tramite borrow immutabile e la closure può implementare `Fn`.

---

### 20.3 Esempio di FnMut

```rust
let mut x = 10;

let f = || {
    x += 10;
};
```

La closure modifica `x`.

Serve quindi un mutable borrow e la closure implementa `FnMut`.

---

### 20.4 Esempio di FnOnce

```rust
let x = vec![21];

let f = || {
    drop(x);
};
```

La closure consuma `x`.

Di conseguenza deve poter essere chiamata almeno come `FnOnce`.

---

# 21. Closure Capture Inference

### 21.1 Quando viene fatta la closure capture inference?

Avviene durante il type checking, nello stadio HIR, dopo parsing e lowering a HIR.

---

### 21.2 Come determina rustc la modalità di capture?

Il compilatore parte concettualmente da:

```text
immutable borrow
```

e la rilassa se necessario:

```text
immutable borrow
       ↓
mutable borrow
       ↓
move
```

Quindi:

- se la variabile viene solo letta → immutable borrow;
    
- se viene modificata → mutable borrow;
    
- se viene consumata → move.
    

---

### 21.3 Che cos'è `upvars_mentioned`?

È un'analisi interna che individua le variabili dell'ambiente utilizzate dalla closure.

---

### 21.4 Che cos'è `ExprUseVisitor`?

È un visitor che attraversa il corpo della closure e segnala le operazioni effettuate sugli upvar:

- borrow;
    
- mutate;
    
- consume.
    

---

### 21.5 Che cos'è il `Delegate`?

Il visitor comunica le operazioni sugli upvar attraverso callback definite tramite il `Delegate`.

`InferBorrowKind` implementa questo meccanismo e mantiene traccia del capture kind.

---

### 21.6 Quali capture kind può distinguere `InferBorrowKind`?

Tra quelli indicati nelle slide:

```text
ByValue
ByRef
```

e, nel caso `ByRef`:

```text
ImmBorrow
UniqueImmBorrow
MutBorrow
```

---

# 22. MIR optimization

### 22.1 Quando viene ottimizzato il MIR?

Dopo il borrow checking e prima della monomorphization/code generation.

Questo è importante perché il MIR è ancora **generico**.

---

### 22.2 Perché ottimizzare prima della monomorphization?

Perché una trasformazione effettuata sul MIR generico può essere riutilizzata per tutte le istanze concrete del generic.

Questo evita di ripetere lo stesso lavoro dopo aver generato ogni versione specializzata.

---

### 22.3 Che cos'è `optimized_mir`?

È la query che guida il processo di ottimizzazione del MIR.

---

### 22.4 Che cos'è un `MirPass`?

Ogni pass di trasformazione/analisi del MIR implementa il trait:

```text
MirPass
```

I pass vengono organizzati in una sequenza.

La funzione `run_optimization_passes` definisce l'ordine dei pass.

---

### 22.5 Quali sono alcuni MIR optimization pass?

Tra gli esempi riportati:

- `CleanupPostBorrowck`;
    
- `ConstProp`.
    

Altri tipi di ottimizzazione includono:

- constant propagation;
    
- dead-code elimination;
    
- copy propagation;
    
- CFG simplification;
    
- inlining.
    

---

### 22.6 Quali sono i livelli di ottimizzazione di rustc?

```text
0 → nessuna ottimizzazione
1 → ottimizzazioni di base
2 → ottimizzazione standard
3 → ottimizzazione aggressiva
s → ottimizza per dimensione
z → ottimizza ancora maggiormente per dimensione
```

Si possono impostare con:

```bash
rustc main.rs -C opt-level=3
```

Secondo le slide:

```bash
cargo build
```

usa livello 0, mentre:

```bash
cargo build --release
```

usa livello 3.

---

# 23. Backend e Code Generation

### 23.1 Cosa succede dopo il borrow checking?

Il backend esegue diversi passaggi:

```text
borrow checked MIR
      ↓
cleanup
      ↓
runtime MIR preparation
      ↓
MIR optimization
      ↓
monomorphization
      ↓
codegen IR
      ↓
backend
      ↓
machine code
      ↓
linking
```

---

### 23.2 Quali backend supporta rustc?

Le slide indicano:

- LLVM;
    
- Cranelift;
    
- GCC.
    

LLVM IR è il percorso tipico.

---

### 23.3 Che cos'è Cranelift?

Cranelift è un backend progettato per essere:

- veloce;
    
- relativamente semplice;
    
- adatto a compilazioni rapide.
    

È particolarmente interessante per debug/local builds e ha un utilizzo importante nella compilazione WebAssembly.

---

# 24. Generics e Monomorphization

### 24.1 Come implementa Rust i generics?

Rust utilizza la **monomorphization**.

Un generic viene specializzato per ogni tipo concreto necessario.

Per esempio:

```rust
fn foo<T>(x: T) { ... }
```

può produrre versioni concettualmente equivalenti a:

```text
foo_i32
foo_f64
foo_String
```

se questi sono i tipi realmente utilizzati.

---

### 24.2 Qual è il vantaggio?

Il codice generato è specializzato.

Questo permette:

- performance elevate;
    
- possibilità di ottimizzare conoscendo il tipo concreto;
    
- riduzione dell'indirezione.
    

---

### 24.3 Qual è lo svantaggio?

Il **code bloat**.

Se un generic viene istanziato con molti tipi diversi, possono essere generate molte copie del codice.

Il compromesso è simile a quello dei C++ templates.

---

### 24.4 Quando avviene la monomorphization?

La monomorphization avviene nel backend, prima della code generation finale, quando il MIR generico viene istanziato per i tipi concreti necessari.

---

# 25. Mono Item Collection

### 25.1 Che cos'è un mono item?

Un **mono item** rappresenta un artefatto che deve essere generato dal backend.

Può corrispondere a:

- funzione;
    
- metodo;
    
- closure;
    
- static;
    
- drop glue;
    
- istanza concreta di generic.
    

---

### 25.2 Che cos'è il mono item graph?

I mono item dipendono gli uni dagli altri.

Per esempio:

```text
main
 ↓
foo<i32>
 ↓
bar
```

forma un grafo orientato di dipendenze.

---

### 25.3 Come funziona la mono item collection?

Le slide descrivono due fasi principali:

1. individuazione dei graph roots;
    
2. attraversamento ricorsivo del MIR per trovare i mono item utilizzati e le loro istanziazioni concrete.
    

---

### 25.4 Da cosa possono derivare gli archi del mono item graph?

Non solo da chiamate di funzione.

Possono derivare da:

- function/method calls;
    
- riferimenti a funzioni;
    
- drop glue;
    
- trait-object unsizing;
    
- vtables;
    
- generic cross-crate/inlined functions.
    

---

### 25.5 Qual è la differenza tra lazy ed eager collection?

**Lazy collection**

Genera solo gli elementi effettivamente necessari.

Vantaggio:

```text
meno codice generato
```

**Eager collection**

Raccoglie più elementi preventivamente.

Può essere utile per:

- incremental compilation;
    
- comportamento più stabile delle recompilation.
    

---

### 25.6 Perché rustc tiene traccia anche dei "mentioned items"?

Per evitare che il risultato della compilazione dipenda dalle ottimizzazioni.

Un elemento potrebbe essere eliminato successivamente dal dead-code elimination, ma se era sintatticamente presente nel MIR, alcuni errori di constant evaluation devono comunque essere riportati in maniera consistente.

---

# 26. Codegen Units

### 26.1 Che cos'è una Codegen Unit?

Una **CGU** è un insieme di mono item e informazioni di linkage che viene trasformato in un modulo LLVM.

---

### 26.2 Perché esistono le CGU?

Principalmente per migliorare le performance della compilazione, soprattutto durante la compilazione incrementale.

LLVM ottimizza moduli interi, non singole funzioni.

---

### 26.3 Qual è il trade-off tra molte e poche CGU?

**Molte CGU**

```text
+ recompilation più piccola
+ incremental build più veloce
- meno ottimizzazioni inter-procedurali
- executable potenzialmente peggiore
```

**Poche CGU**

```text
+ migliori ottimizzazioni LLVM
+ più possibilità di inlining
+ executable potenzialmente migliore
- recompilation più costosa
```

---

### 26.4 Perché i generics complicano la compilazione incrementale?

Perché aggiungere o eliminare un riferimento a una funzione generica può creare o eliminare una monomorphized instance.

Quindi può essere necessario ricompilare anche se il corpo della funzione generic non è cambiato.

---

### 26.5 Perché l'inlining influenza le CGU?

LLVM può effettuare l'inlining quando il corpo del callee è disponibile nello stesso modulo.

Per questo il partitioner può duplicare funzioni eleggibili tra CGU.

Le funzioni marcate:

```rust
#[inline]
```

sono particolarmente importanti in questo meccanismo.

---

# 27. Lowering MIR → Codegen IR

### 27.1 Che cosa succede dopo la mono item collection?

Il MIR viene trasformato in una rappresentazione specifica del backend.

Tipicamente:

```text
MIR
 ↓
LLVM IR
```

ma possono essere usati anche Cranelift o GCC.

---

### 27.2 Come vengono trasformati i costrutti MIR?

La traduzione è organizzata in base ai componenti del MIR:

```text
block      → basic blocks / terminators
statement  → statements
operand    → operands
place      → memory/place references
rvalue     → computations
```

---

### 27.3 Come vengono mappati i basic block MIR?

In genere un basic block MIR corrisponde a un basic block LLVM.

Tuttavia un singolo costrutto MIR può espandersi in più basic block LLVM, per esempio a causa di:

- assertions;
    
- intrinsics;
    
- chiamate complesse;
    
- gestione dell'unwinding.
    

---

### 27.4 Che cosa significa che alcune variabili MIR sono "SSA-like"?

Il compilatore può identificare variabili che possono essere emesse direttamente in una forma simile alla SSA.

Questo permette di produrre LLVM IR più pulito senza affidarsi completamente a ottimizzazioni successive come `mem2reg`.

---

# 28. Domande di collegamento

### 28.1 Perché il MIR è centrale nella compilazione di Rust?

Perché costituisce il punto in cui molte proprietà fondamentali diventano esplicite:

```text
ownership
   ↓
move analysis
   ↓
initialization
   ↓
borrowing
   ↓
regions
   ↓
borrow checking
   ↓
optimization
   ↓
code generation
```

Il MIR è quindi il punto di incontro tra analisi semantiche e generazione del codice.

---

### 28.2 Qual è la relazione tra move analysis e region inference?

Entrambe sono analisi di dataflow/fixed point.

La move analysis lavora sui:

```text
move paths
```

mentre la region inference lavora sui:

```text
region elements
```

Entrambe propagano informazioni attraverso una struttura di controllo/dependency fino al raggiungimento di un fixed point.

---

### 28.3 Qual è la relazione tra borrow checking e code generation?

Il borrow checker deve terminare prima che il compilatore possa considerare il programma valido.

Solo dopo il borrow checking il compilatore può procedere con:

```text
MIR cleanup
 ↓
optimization
 ↓
monomorphization
 ↓
code generation
```

Le ottimizzazioni successive lavorano quindi su un programma già verificato rispetto alle proprietà di ownership e borrowing.

---

### 28.4 Perché la monomorphization viene fatta dopo le ottimizzazioni MIR?

Perché ottimizzare il MIR generico permette di riutilizzare il risultato per più istanze concrete.

Questo riduce lavoro duplicato e permette di sfruttare il fatto che il MIR è ancora parametrico.

---

### 28.5 Qual è il rapporto tra closure capture inference e borrow checker?

La closure capture inference determina **come** una closure utilizza le variabili esterne:

```text
read     → &T
mutate   → &mut T
consume  → move
```

Queste informazioni diventano poi parte della rappresentazione che il compilatore deve rispettare durante le successive analisi di ownership e borrowing.

---

# 29. Domande "da professore"

### 29.1 Perché il compilatore esegue il MIR type check se il THIR è già tipato?

**Risposta modello:**

Perché il lowering THIR → MIR non è banalmente type-preserving. Durante la trasformazione vengono introdotti nuovi costrutti, temporanei, borrow, move, drop e specifici invarianti del MIR. Il compilatore deve quindi verificare indipendentemente che il MIR risultante sia corretto e, nello stesso passaggio, generare region constraints e type tests.

---

### 29.2 Perché le lifetime NLL sono rappresentate come punti del CFG?

**Risposta modello:**

Perché la durata effettiva di un borrow dipende dall'utilizzo e dal controllo di flusso, non necessariamente dalla struttura lessicale dello scope. Rappresentare una region come insieme di punti del CFG permette quindi di terminare un borrow alla sua ultima utilizzazione effettiva.

---

### 29.3 Perché servono le SCC nella region inference?

**Risposta modello:**

I vincoli outlives formano un grafo che può contenere cicli. Le regioni appartenenti a un ciclo devono essere trattate insieme. Collassando ogni strongly connected component in un singolo nodo otteniamo un DAG, sul quale la propagazione dei vincoli può essere eseguita efficientemente.

---

### 29.4 Perché i type tests non vengono inseriti direttamente nel region solver?

**Risposta modello:**

Perché il solver delle region opera su un dominio relativamente semplice, costituito da insiemi di punti e vincoli di outlives. I tipi Rust possono invece essere arbitrariamente complessi, con generics, tipi annidati e projections. Separare i type tests permette di mantenere il solver più semplice ed efficiente.

---

### 29.5 Perché Rust usa la monomorphization?

**Risposta modello:**

Per ottenere codice specializzato per ogni tipo concreto utilizzato. Questo permette alte prestazioni e ottimizzazioni specifiche per il tipo, ma può aumentare la dimensione del codice perché vengono generate più copie delle funzioni generic.

---

### 29.6 Perché le Codegen Units sono un compromesso?

**Risposta modello:**

Perché LLVM ottimizza moduli interi. Con molte CGU, una modifica richiede di ricompilare un modulo più piccolo, migliorando la compilazione incrementale. Con poche CGU, invece, LLVM vede più codice insieme e può effettuare migliori ottimizzazioni inter-procedurali e inlining.

---

### 29.7 Perché esistono i two-phase borrows?

**Risposta modello:**

Per consentire alcuni pattern naturali in cui una chiamata richiede un mutable receiver ma gli argomenti devono temporaneamente utilizzare lo stesso valore tramite borrow condiviso. `vec.push(vec.len())` è l'esempio classico. Il mutable borrow viene prima prenotato e solo successivamente attivato.

---

### 29.8 Come fa rustc a capire se una closure è Fn, FnMut o FnOnce?

**Risposta modello:**

Analizza come la closure utilizza gli upvar. Parte concettualmente da un immutable borrow e lo rende più permissivo se necessario: se l'upvar viene solo letto rimane un immutable borrow, se viene modificato diventa mutable borrow, se viene consumato diventa move. Da questo determina il closure trait appropriato: `Fn`, `FnMut` oppure `FnOnce`.

---

# 30. Domande tecniche molto probabili

### 30.1 Che cosa fa `mir_borrowck`?

Avvia il borrow checker sul MIR e coordina:

```text
region replacement
move/init analysis
MIR type checking
region inference
borrow set construction
final validation
```

---

### 30.2 Che cosa fa `optimized_mir`?

Produce il MIR ottimizzato eseguendo una sequenza di `MirPass` dopo il borrow checking.

---

### 30.3 Che cosa fa `collect_and_partition_mono_items`?

Raccoglie gli elementi che devono essere monomorphizzati e li partiziona in Codegen Units.

---

### 30.4 Qual è la differenza tra MIR generico e MIR monomorphized?

Il MIR generico contiene funzioni parametrizzate sui tipi.

Il MIR monomorphized ha invece istanze concrete:

```text
foo<T>
```

diventa concettualmente:

```text
foo<i32>
foo<String>
...
```

solo per le istanze necessarie.

---

### 30.5 Che cosa avviene immediatamente prima della code generation?

In termini semplificati:

```text
MIR optimization
      ↓
mono item collection
      ↓
CGU partitioning
      ↓
MIR lowering
      ↓
LLVM/Cranelift/GCC
      ↓
machine code
```

---

# 31. Le 20 domande più importanti da sapere perfettamente

Se il tempo prima dell'orale è limitato, queste sono quelle che imparerei **a memoria concettuale**:

1. **Che cos'è il MIR e perché è necessario?**
    
2. **Qual è la pipeline AST → HIR → THIR → MIR?**
    
3. **Perché il MIR type check è necessario anche dopo il THIR?**
    
4. **Come funziona `mir_borrowck`?**
    
5. **Che cos'è la move analysis?**
    
6. **Che cosa sono i move paths?**
    
7. **Che cosa sono lifetime e region?**
    
8. **Che cosa significa NLL?**
    
9. **Come funziona la region inference?**
    
10. **Che cosa sono i liveness e outlives constraints?**
    
11. **Perché vengono usate le SCC?**
    
12. **Che cosa sono i type tests e perché vengono verificati separatamente?**
    
13. **Che cosa sono i two-phase borrows?**
    
14. **Come vengono inferite le capture delle closure?**
    
15. **Qual è la differenza tra `Fn`, `FnMut` e `FnOnce`?**
    
16. **Che cos'è `optimized_mir` e come funzionano i `MirPass`?**
    
17. **Che cos'è la monomorphization e perché Rust la utilizza?**
    
18. **Che cos'è la mono item collection?**
    
19. **Che cosa sono le Codegen Units e qual è il loro trade-off?**
    
20. **Come si passa dal MIR a LLVM IR/codice macchina?**
    

---

# 32. Mappa mentale finale

```text
                         RUST SOURCE
                              │
                              ▼
                         AST / HIR
                              │
                              ▼
                             THIR
                              │
                   ┌──────────┴──────────┐
                   │                     │
             type checking        closure inference
                   │                     │
                   └──────────┬──────────┘
                              ▼
                             MIR
                              │
             ┌────────────────┼─────────────────┐
             │                │                 │
             ▼                ▼                 ▼
        Move Analysis    Region Inference    Borrow Analysis
             │                │                 │
             │          constraints             │
             │          SCC → DAG               │
             │                │                 │
             └────────────────┼─────────────────┘
                              ▼
                       Borrow Checking
                              │
                              ▼
                      MIR Optimization
                       optimized_mir
                              │
                              ▼
                    Mono Item Collection
                              │
                              ▼
                     Monomorphization
                              │
                              ▼
                       Codegen Units
                              │
                              ▼
                       Codegen IR
                    ┌─────────┼─────────┐
                    │         │         │
                  LLVM    Cranelift    GCC
                    │
                    ▼
                 Machine Code
                    │
                    ▼
                 Executable
```

## Concetto chiave da ricordare

Il modo migliore per spiegare l'intero capitolo all'orale è presentarlo come una **catena di trasformazioni e analisi**:

> Rust parte da una rappresentazione sintattica, passa progressivamente a rappresentazioni sempre più semantiche, arriva al MIR per rendere espliciti controllo di flusso, move, borrow e lifetime, esegue il borrow checking tramite analisi di dataflow e region inference, quindi ottimizza il MIR, specializza i generics tramite monomorphization e infine lo traduce in una Codegen IR che viene gestita dal backend.

La parte centrale del capitolo è quindi:

```text
MIR
 ↓
Program Analysis
 ↓
Borrow Checking
 ↓
Optimization
 ↓
Monomorphization
 ↓
Code Generation
```

Questa è la struttura concettuale che permette di collegare praticamente tutti gli argomenti dei PDF.