# Rust Compilation — Domande e Risposte per l'esame orale (versione approfondita)

> Versione ampliata del documento originale, integrata con i contenuti puntuali dei lucidi del corso (COMP-26 RUST #1–#6): pipeline rustc, MIR, drop elaboration, borrow checker, region inference, two-phase borrows, closure capture inference, monomorphization, codegen units, linting, type system, type inference e Hindley-Milner/uHaskell.

---

# 0. Storia e obiettivi di Rust e di rustc

### 0.1 Da dove nasce Rust?

Lo sviluppo è iniziato nel 2006 a opera di **Graydon Hoare** presso Mozilla. Nel 2010 il compilatore, inizialmente scritto in OCaml, è stato riscritto in Rust stesso (**self-hosting**): `rustc` è riuscito a compilare se stesso nel 2011. Da allora si usa il **bootstrapping** per generare le nuove versioni del compilatore. `rustc` usa **LLVM** come backend principale.

### 0.2 Quali sono gli obiettivi di design di Rust?

Rust è un linguaggio general-purpose per programmazione di sistema, con focus sulla **safety** (in particolare la _safe concurrency_), che supporta sia il paradigma funzionale sia quello imperativo. L'obiettivo principale è garantire la sicurezza **senza penalizzare l'efficienza**. La sintassi concreta è simile a C/C++ (blocchi, if-else, while, for, match per il pattern matching); quasi ogni parte del corpo di una funzione è un'espressione (incluso l'if-else). Rust non richiede alcun runtime (niente GC, niente dynamic typing/binding), offrendo più controllo sull'allocazione/distruzione della memoria.

### 0.3 Quali garanzie di sicurezza offre Rust, e a quale costo?

Come C, Rust compila verso codice oggetto per prestazioni "bare-metal", ma garantisce memory safety:

- nessun puntatore nullo;
- nessun dangling pointer;
- nessun double free;
- nessuna data race;
- nessuna iterator invalidation;
- accessi fuori dai limiti di un array non ammessi.

Il tutto con **basso overhead**: le regole di memory safety sono verificate perlopiù _staticamente_, e l'astrazione nella gestione della memoria è "a costo zero" (niente garbage collector). Il meccanismo è basato su un **sistema di tipi avanzato** e sui concetti di ownership, borrowing e lifetime (basati su RAII). Il costo è **cognitivo**: il programmatore deve ragionare più esplicitamente sulle regole d'uso di memoria e riferimenti.

---

# 1. RAII, Ownership e Borrowing

### 1.1 Che cos'è RAII e come lo eredita Rust?

_Resource Acquisition Is Initialization_: l'allocazione di una risorsa avviene durante l'inizializzazione dell'oggetto (dal costruttore), la deallocazione avviene durante la distruzione dell'oggetto (dal distruttore). È popolare in C++: piccoli oggetti sullo stack, risorse grandi sull'heap possedute da un oggetto sullo stack che le rilascia nel proprio distruttore. L'oggetto è legato allo scope in cui è dichiarato: quando lo scope si chiude, l'oggetto (e ogni risorsa posseduta) viene recuperato. **Ogni risorsa ha un unico proprietario.**

Rust possiede un sistema di ownership che supporta RAII in modo **stretto**, basato sui concetti di ownership e borrowing.

### 1.2 Quali sono le tre regole di Ownership (O1–O3)?

- **[O1]** Ogni valore è posseduto da una variabile, identificata da un nome o un path;
- **[O2]** Ogni valore ha al più un proprietario alla volta;
- **[O3]** Quando il proprietario esce dallo scope, il valore viene recuperato/distrutto/"dropped".

### 1.3 Come funziona la move semantics dell'assegnamento?

Per default, un assegnamento fra variabili ha semantica di **move**: la ownership passa dal RHS al LHS (per soddisfare [O2]):

```rust
fn main() {
    let x = Box::new(3);
    let _y = x;
    println!("x = {}", x); // errore: x è stato mosso
}
```

Per i tipi primitivi e i tipi che implementano il trait `Copy`, l'assegnamento ha invece semantica di **copia**; [O2] resta soddisfatto perché viene creato un nuovo valore:

```rust
fn main() {
    let x = 3;
    let _y = x;
    println!("x = {:?}", x); // OK, i32 è Copy
}
```

Nota: anche `Option<T>` con `T: Copy` (es. `Option<i32>`) mantiene la semantica corretta senza errori.

### 1.4 Come funziona la move semantics nel passaggio parametri e nel return?

Vale lo stesso principio: ogni valore passato a una funzione viene recuperato quando la funzione ritorna, perché il parametro formale esce dallo scope. Solo il valore restituito (eventualmente in una tupla, per restituirne più di uno) può sopravvivere:

```rust
fn foo<T>(z: T) -> T { z } // identità polimorfa

fn main(){
    let x = Box::new(3);
    let _y = foo(x);
    println!("x == {}", x); // errore: x è stato mosso in foo
}

fn main(){
    let mut x = Box::new(3);
    x = foo(x); // il valore ritorna e viene riassegnato a x
    println!("x == {}", x); // OK
}
```

### 1.5 Perché servono le regole di Borrowing?

Le regole di ownership sono troppo restrittive. Una risorsa può essere **presa in prestito** (borrowed) dal proprio proprietario, tramite assegnamento o passaggio parametri. Per garantire la memory safety, le regole di borrowing impongono che **aliasing e mutabilità non possano coesistere**. I valori possono essere passati:

- per riferimento immutabile (`x = &y`);
- per riferimento mutabile (`x = &mut y`);
- per valore (`x = y`).

### 1.6 Quali sono le cinque regole di Borrowing (B1–B5)?

- **[B1]** Al più un riferimento mutabile a una risorsa può esistere in un dato momento;
- **[B2]** Se esiste un riferimento mutabile, non possono esistere riferimenti immutabili;
- **[B3]** Se non esiste un riferimento mutabile, possono esistere più riferimenti immutabili alla stessa risorsa.

Durante il borrowing, l'ownership è ridotta o sospesa:

- **[B4]** Il proprietario non può liberare o mutare la propria risorsa mentre è presa in prestito immutabilmente;
- **[B5]** Il proprietario non può nemmeno leggere la propria risorsa mentre è presa in prestito mutabilmente.

Questo insieme di regole è spesso riassunto come **"Alias XOR Mutation"**.

### 1.7 Esempi di violazione/rispetto delle regole di borrowing

```rust
let mut s = String::from("example");
let r1 = &mut s;
let r2 = &mut s;
println!("{} {}", r1, r2); // NON compila: viola [B1]

let mut s = String::from("example");
let r1 = &s;
let r2 = &mut s;
println!("{} {}", r1, r2); // NON compila: viola [B2]

let s = String::from("example");
let r1 = &s;
let r2 = &s;
println!("{} {}", r1, r2); // OK per [B3]
```

### 1.8 Che cos'è una lifetime?

Una **lifetime** è un costrutto che il borrow checker usa per garantire la validità delle regole di ownership/borrowing sopra. È associata a ogni singola ownership e a ogni singolo borrowing:

- una lifetime **inizia** quando l'ownership comincia, e **finisce** quando il valore è mosso/distrutto;
- per i prestiti, finisce nel punto in cui il valore preso in prestito è usato l'ultima volta.

Le lifetime sono per lo più **inferite**; a volte devono essere rese esplicite con la stessa sintassi dei generics. Usando le lifetime, il compilatore verifica la validità delle regole di ownership/borrowing garantendo in particolare che (il proprietario di) ogni variabile/riferimento preso in prestito abbia una lifetime più lunga di quella di chi prende in prestito [B4, B5].

---

# 2. Perché servono più IR: dal front-end alla LLVM IR

### 2.1 Qual è l'architettura classica LLVM, e perché non basta a Rust?

Nell'architettura LLVM classica, l'analisi statica (es. type checking) avviene nel front-end tipicamente sull'AST, mentre le analisi dataflow e le ottimizzazioni avvengono sulla LLVM IR, tipicamente su un control-flow graph. Il problema è che la **LLVM IR è troppo low-level per il borrow checker di Rust**.

### 2.2 Perché il borrow checking non è "semplice alias analysis su codice machine-like"?

Perché è un'analisi di sicurezza **flow-sensitive** a livello di linguaggio, che ragiona su concetti come:

- places e projections (`x`, `x.0`, `*p`, `v[i]`);
- move e partial move;
- prestiti condivisi vs mutabili;
- vincoli di region/lifetime;
- semantica dei drop;
- controllo di flusso desugarato ma ancora tipato secondo le regole di Rust.

Un esempio tipico che richiede questo ragionamento fine è:

```rust
fn push_len(v: &mut Vec<i32>) {
    v.push(v.len() as i32);
}
```

Per questo `rustc` necessita di IR intermedie prima di generare la LLVM IR.

### 2.3 Perché rustc è un caso di studio interessante indipendentemente da Rust?

Perché è open source e aperto ai contributi, e perché temi "classici" della teoria dei compilatori — CFG, liveness, dataflow, constraint, punti fissi — sono visibili direttamente **come semantica del linguaggio**, non solo come fasi opzionali di ottimizzazione. Il design ha inoltre scelte implementative non convenzionali, come il **sistema a query**.

---

# 3. Il Query System di rustc

### 3.1 Come organizza rustc le proprie analisi?

Le query sono l'astrazione centrale che struttura il compilatore come **sistema demand-driven**: `rustc` non è eseguito come una sequenza fissa di passate. Ogni informazione (es. il tipo di una funzione, il suo MIR, il risultato del borrow-checking) è calcolata da una query che può dipendere da altre query. Quando il compilatore necessita di un'informazione, invoca la query corrispondente, che ricorsivamente assicura che tutte le sue dipendenze siano calcolate.

### 3.2 Perché il query system è importante?

- I risultati delle query sono **memoizzati**: se la stessa informazione viene richiesta di nuovo, può essere riusata senza ricalcolo;
- quando il codice sorgente cambia, solo le query i cui input sono cambiati — e quelle che ne dipendono — devono essere ricalcolate;
- questo rende la compilazione più efficiente e scalabile su progetti grandi, offrendo al contempo una struttura modulare pulita per l'implementazione del compilatore (**caching + incremental compilation**).

---

# 4. Front-end e Middle-end: AST → HIR → THIR → MIR

### 4.1 Che cos'è il front-end di rustc?

- Un lexer standard low-level (sorgente → token): `rustc-lexer`;
- un lexer di livello più alto invocato dal parser;
- un **recursive descent parser** (`rustc-parse`) che genera l'AST.

### 4.2 Che cosa avviene dal front-end al middle-end?

Dopo la macro expansion e la name resolution, `rustc` abbassa (lowers) l'AST a **HIR**, un albero sintattico più regolare usato da molte analisi front-end. A livello di corpo funzione vengono poi aggiunte informazioni tipate, ottenendo il **THIR**.

### 4.3 Che cosa avviene nel middle-end?

Il THIR viene tradotto nel **MIR**, un control-flow graph dove controllo di flusso, temporanei, places e drop diventano espliciti. Questa è l'IR su cui viene eseguito il **borrow checker**. Il MIR è ulteriormente ottimizzato prima dell'abbassamento a LLVM IR. Il backend consuma MIR verificato e preparato, crea istanze concrete monomorfizzate e delega l'ottimizzazione low-level a LLVM.

### 4.4 Perché un solo AST non basta?

- **Troppo sintattico**: un AST rispecchia la sintassi utente — espressioni annidate, zucchero sintattico e forme source-level oscurano l'ordine di valutazione e gli archi di controllo di flusso;
- **desugaring ripetuto**: senza un'IR centrale, ogni passata successiva dovrebbe riscoprire o reimplementare le stesse regole di desugaring e semantica locale;
- **CFG difficile da ragionare**: il borrow checking necessita di punti fine-grained del programma e archi fra essi; questi sono scomodi da esprimere direttamente su un AST;
- **forma eseguibile**: il MIR è più vicino a un modello eseguibile: blocchi, statement, terminator, places, operandi e temporanei espliciti.

### 4.5 Esempio completo: traduzione di uno statement attraverso le fasi

Consideriamo l'istruzione Rust:

```rust
let z = if x > 0 { x + 1 } else { 0 };
```

**AST** — struttura ad albero che preserva l'annidamento delle espressioni; il risultato del blocco è implicito (l'ultima espressione di ciascun ramo diventa l'inizializzatore):

```text
Stmt::Local {
  pat: Pat::Ident("z"),
  init: Expr::If {
    cond: Expr::Binary(Gt, Path("x"), Lit(0)),
    then: Block(Expr::Binary(Add, Path("x"), Lit(1))),
    else_: Block(Expr::Lit(0))
  }
}
```

**HIR** — ancora vicino alla sintassi, ma ha attraversato un lowering front-end importante:

```text
let z: i32 = if (x > 0) { x + 1 } else { 0 };
```

**THIR** — l'inizializzatore e ciascun ramo hanno tipo `i32` noto; la condizione ha tipo `bool`; THIR registra adjustment e significati tipati degli operatori prima della costruzione del MIR:

```text
LocalDecl z: i32
Init = ExprKind::If {
  cond: ExprKind::Binary(Gt, x:i32, 0_i32): bool,
  then: ExprKind::Binary(Add, x:i32, 1_i32): i32,
  else: 0_i32
}
// Nessun CFG ancora, ma i fatti tipati sul corpo sono espliciti.
```

**MIR** — l'espressione singola diventa un CFG a "diamante" esplicito; condizione e calcolo del ramo sono salvati in temporanei con nome; ciascun ramo scrive nella stessa place di destinazione, così l'inizializzazione può essere verificata path-sensitively:

```text
let mut _z: i32;
let mut _t0: bool;
let mut _t1: i32;

bb0: { _t0 = Gt(copy _x, const 0_i32);
       switchInt(copy _t0) -> [0: bb2, otherwise: bb1]; }
bb1: { _t1 = Add(copy _x, const 1_i32);
       _z = move _t1;
       goto -> bb3; }
bb2: { _z = const 0_i32; goto -> bb3; }
bb3: { /* z inizializzata qui */ }
```

Questa forma è adatta a liveness, definite assignment, borrow checking e lowering.

### 4.6 Che cos'è l'HIR nel dettaglio?

**High-level Intermediate Representation**. È costruito _dopo_ parsing, macro expansion e name resolution, quindi molti nomi e forme sintattiche sono già risolti. Resta vicino al programma del programmatore, il che lo rende adatto a check e diagnostica front-end. Alcuni costrutti superficiali possono già essere normalizzati (es. parte dello zucchero sui loop è rappresentata in forme più regolari). Non è però l'IR del borrow-check: è ancora troppo alto livello per il ragionamento puntuale dettagliato richiesto dal MIR borrow checking.

### 4.7 Che cos'è il THIR nel dettaglio?

**Typed HIR**, prodotto per i corpi di funzione ed è intenzionalmente temporaneo: `rustc` non mantiene ogni corpo THIR globalmente per sempre. È completamente tipato: rende espliciti gli adjustment dipendenti dal tipo, inclusi autoref, autoderef, coercizioni e chiamate overloaded. È il "ponte" di lowering: il costruttore del MIR consuma THIR piuttosto che l'HIR grezzo, perché il THIR espone già decisioni semantiche importanti. Concettualmente è il punto in cui si vede lo spostamento dalla sintassi superficiale verso i fatti operazionali necessari alla costruzione del CFG.

### 4.8 Perché serve comunque il MIR type check se il THIR è già tipato?

Perché nella trasformazione THIR → MIR vengono introdotti nuovi costrutti, temporanei, prestiti impliciti, move, drop, ordine di valutazione esplicito e controllo di flusso: il MIR type checking resta necessario anche se il THIR era già tipato (approfondito in Sezione 8).

---

# 5. Desugaring

### 5.1 Dove avviene il desugaring nella pipeline?

Le varie fasi di abbassamento verso il MIR eseguono diversi tipi di desugaring:

- **early desugaring** (es. i cicli `for`) avviene durante l'HIR lowering;
- **late desugaring** (chiamate a metodo, autoderef, autoref, operatori) avviene durante la costruzione del THIR;
- la **costruzione del MIR** rimuove del tutto l'annidamento delle espressioni.

### 5.2 Quali sono le principali forme di zucchero sintattico in Rust?

Rust ha molto zucchero sintattico, che nasconde informazioni importanti anche per il borrow-checking. Esempi:

- Method Call Desugaring;
- for-loop Desugaring;
- Operator Overloading;
- operatore `?` → match su `Result`/`Option`;
- `if let` → `match`;
- `while let` → `loop` + `match`;
- auto-ref/auto-deref;
- Closure → struct + trait (`Fn`, `FnMut`, `FnOnce`);
- indicizzazione `v[i]` → trait `Index`/`IndexMut`;
- return implicito → tail expression.

### 5.3 Tabella completa di esempi di desugaring

|Sorgente|Desugarato|
|---|---|
|`for x in v { println!("{}", x); }`|`{ let mut iter = IntoIterator::into_iter(v); loop { match iter.next() { Some(x) => { println!("{}", x); } None => break, } } }`|
|`let x = foo()?;`|`let x = match foo() { Ok(v) => v, Err(e) => return Err(From::from(e)), };`|
|`let x = opt?;`|`let x = match opt { Some(v) => v, None => return None, };`|
|`v.push(10);`|`Vec::push(&mut v, 10);`|
|`x.foo()`|`Foo::foo(&x)` / `Foo::foo(&mut x)` / `Foo::foo(&*x)` (a seconda della firma di `foo`)|
|`if let Some(x) = opt { println!("{}", x); }`|`match opt { Some(x) => { println!("{}", x); } _ => {} }`|
|`while let Some(x) = iter.next() { println!("{}", x); }`|`loop { match iter.next() { Some(x) => { println!("{}", x); } None => break, } }`|
|`v[i]` (lettura)|`*std::ops::Index::index(&v, i)`|
|`v[i] = 10;`|`*std::ops::IndexMut::index_mut(&mut v, i) = 10;`|
|`fn f() -> i32 { 3 }`|`fn f() -> i32 { return 3; }` (tail expression)|

Ricordando le definizioni standard:

```rust
enum Result<T, E> { Ok(T), Err(E) }
enum Option<T> { None, Some(T) }
```

La sintassi a metodo è pura sintassi zuccherata: il compilatore inserisce `&`, `&mut`, deref (`*`) e la risoluzione del trait.

### 5.4 Come vengono desugarate le closure?

```rust
let f = |x| x + 1; // closure
```

diventa concettualmente:

```rust
struct Closure;
impl Fn(i32) -> i32 for Closure {
    extern "rust-call" fn call(&self, (x,): (i32,)) -> i32 {
        x + 1
    }
}
let f = Closure;
```

Con cattura di variabile:

```rust
let y = 10;
let f = |x| x + y; // cattura di variabile
```

diventa:

```rust
struct Closure { y: i32 }
impl Fn(i32) -> i32 for Closure {
    extern "rust-call" fn call(&self, (x,): (i32,)) -> i32 {
        x + self.y
    }
}
let f = Closure { y };
```

**Importante**: il risultato di questo desugaring interno non è codice Rust legale scrivibile dall'utente: l'inferenza delle catture e la selezione del trait non sono esprimibili direttamente da codice sorgente scritto a mano.

### 5.5 Perché il desugaring è importante?

Permette al compilatore di lavorare con un insieme più piccolo di costrutti fondamentali. Avviene a più livelli (HIR lowering, THIR construction, ed emerge esplicitamente nel MIR). Il lowering può introdurre temporanei, borrow impliciti, move, drop, ordine di valutazione esplicito e controllo di flusso — per questo il MIR type checking resta comunque necessario anche se il THIR era già tipato.

---

# 6. MIR: struttura e concetti chiave

### 6.1 Quali sono i benefici storici dell'introduzione del MIR (aprile 2016)?

- compilazione più veloce;
- esecuzione più veloce;
- borrow checking più preciso — **NLL** (Non-Lexical Lifetimes).

### 6.2 Quali sono le caratteristiche chiave del MIR?

- È basato su un **control-flow graph**;
- **non ha espressioni annidate**;
- tutti i tipi nel MIR sono completamente espliciti (costruiti a partire dal THIR);
- **basic block**: unità del CFG, composte da:
    - **statement**: azioni con un solo successore;
    - **terminator**: azioni con potenzialmente più successori; sempre alla fine di un blocco;
- **local**: argomenti di funzione, variabili locali e temporanei, come `_1`, `_2`; `_0` è la variabile locale speciale per il valore di ritorno;
- **place**: espressioni che identificano una locazione in memoria, come `_1` oppure `_1.f`;
- **rvalue**: espressioni che producono un valore;
    - **operand**: gli argomenti di un rvalue, che possono essere una costante (es. `22`) o una place (es. `_1`).

### 6.3 Esempio completo di MIR ottimizzato

```rust
fn main() {
    let mut vec = Vec::new();
    vec.push(1);
    vec.push(2);
}
```

```text
// optimized MIR
fn main() -> () {
    let mut _0: ();
    let mut _1: std::vec::Vec<i32>;
    let _2: ();
    let mut _3: &mut std::vec::Vec<i32>;
    let _4: ();
    let mut _5: &mut std::vec::Vec<i32>;
    scope 1 {
        debug vec => _1;
    }

    bb0: {
        _1 = Vec::<i32>::new() -> [return: bb1, unwind continue];
    }
    bb1: {
        _3 = &mut _1;
        _2 = Vec::<i32>::push(move _3, const 1_i32) -> [return: bb2, unwind: bb5];
    }
    bb2: {
        _5 = &mut _1;
        _4 = Vec::<i32>::push(move _5, const 2_i32) -> [return: bb3, unwind: bb5];
    }
    bb3: {
        drop(_1) -> [return: bb4, unwind continue];
    }
    bb4: {
        return;
    }
    bb5 (cleanup): {
        drop(_1) -> [return: bb6, unwind terminate(cleanup)];
    }
    bb6 (cleanup): {
        resume;
    }
}
```

Da notare: i local sono senza nome (`_1`, `_2`, …), `_0` è il return value; le annotazioni `debug` mantengono i nomi delle variabili utente; il MIR registra se i valori sono copiati o mossi (`move`/`copy`), informazione necessaria per il ragionamento sull'ownership; il CFG espone i percorsi che le analisi successive possono attraversare con tecniche dataflow standard.

### 6.4 Quali sono i tipi dati del MIR in rustc?

Definiti nel modulo `compiler/rustc_middle/src/mir/`:

- il tipo dati principale è `Body`;
- i **basic block** sono salvati nel campo `Body::basic_blocks`, un vettore di `BasicBlockData`; nessuno referenzia mai un basic block direttamente, ma si passano valori `BasicBlock`, indici newtype in questo vettore;
- gli **statement** sono rappresentati dal tipo `Statement`;
- i **terminator** dal tipo `Terminator`;
- i **local** sono rappresentati da un tipo indice newtype `Local`; i dati di una variabile locale si trovano nel vettore `Body::local_decls`; esiste la costante speciale `RETURN_PLACE` che identifica il "local" speciale che rappresenta il valore di ritorno;
- le **place** sono identificate dalla struct `Place`, con campi:
    - la variabile locale di base (es. `_1`);
    - le **projections**, ossia campi o altre operazioni che "proiettano fuori" da una place di base, rappresentate dal tipo newtype `ProjectionElem` — ad es. `_1.f` è una projection con `f` come elemento di projection e `_1` come path di base; `*_1` è anch'essa una projection, con `*` rappresentato dall'elemento `ProjectionElem::Deref`;
- gli **rvalue** sono rappresentati dall'enum `Rvalue`;
- gli **operand** sono rappresentati dall'enum `Operand`.

### 6.5 Quali sono i "dialetti" e le fasi del MIR?

- **MIR Built**: il MIR iniziale è costruito dal THIR e contiene ancora costrutti orientati all'analisi e annotazioni source-level;
- **MIR Analysis**: borrow checking, NLL, move analysis, controlli di inizializzazione e ragionamento dataflow operano sul MIR di analisi;
- **MIR Runtime**: dopo il borrowck, cleanup ed elaboration rimuovono gli artefatti necessari al checking ma non all'esecuzione runtime;
- **stessa struttura, nuovo contratto**: le strutture dati MIR sottostanti sono correlate fra le fasi, ma le promesse semantiche attese da ciascuna fase del compilatore cambiano.

### 6.6 Quali query servono a ottenere il MIR?

- per una funzione: la query `optimized_mir` (tipicamente usata dal codegen) oppure `mir_for_ctfe` (tipicamente usata per la valutazione a compile time, CTFE);
- per un "promoted": la query `promoted_mir`.

Queste restituiscono il MIR finale, ottimizzato. Per i def-id esterni (di altri crate), il MIR è ottenuto dai metadati dell'altro crate. Per i def-id locali, la query costruisce il MIR ottimizzato richiedendo una pipeline di query upstream; ogni query contiene una serie di passate.

### 6.7 Qual è la pipeline completa delle query MIR?

- `mir_built(D)` — dà il MIR iniziale appena costruito;
- `mir_const(D)` — applica alcune semplici passate di trasformazione per rendere il MIR pronto per la const qualification;
- `mir_promoted(D)` — estrae i temporanei promuovibili in corpi MIR separati, e rende il MIR pronto per il borrow checking;
- `mir_drops_elaborated_and_const_checked(D)` — esegue il borrow checking, esegue le maggiori passate di trasformazione (come la drop elaboration) e rende il MIR pronto per l'ottimizzazione;
- `optimized_mir(D)` — esegue tutte le ottimizzazioni abilitate e raggiunge lo stato finale.

### 6.8 Che cos'è un "promoted" MIR?

Un pezzo di MIR estratto dal corpo di una funzione e sollevato in un corpo MIR separato, simile a una costante, così da poter essere valutato a compile time o trattato come avente lifetime `'static`. Durante la costruzione del MIR, il compilatore identifica espressioni pure, costanti e prive di effetti collaterali (es. array literal, riferimenti a dati costanti); invece di lasciarle inline nel MIR della funzione, le promuove in un corpo MIR separato (una **costante promossa**), e sostituisce l'espressione originale con un riferimento a quel valore promosso.

```rust
fn f() -> &'static [i32; 3] {
    &[1, 2, 3]
}
```

diventa concettualmente:

```text
Promoted[0]:
    _0 = [1, 2, 3];
    return;

fn f():
    _0 = &'static Promoted[0];
    return;
```

Senza promozione l'array sarebbe un temporaneo interno a `f`; con la promozione il compilatore lo trasforma in un corpo separato referenziato.

### 6.9 Cosa fa concretamente la costruzione del MIR (`mir_built`)?

La query `mir_built` provoca l'abbassamento dal THIR di corpi di funzione e closure, inizializzatori di item `static`/`const`, inizializzatori di discriminanti di enum e altro. Per prima cosa crea variabili locali per ogni argomento e per ogni binding specificato, e accessi a campo che leggono i campi dall'argomento e scrivono il valore nella variabile di binding. Infine attiva una chiamata ricorsiva a una funzione che genera il MIR per il corpo (un'espressione `Block`) e scrive il risultato nella `RETURN_PLACE`.

---

# 7. Il MIR Visitor

### 7.1 A cosa serve?

Il MIR visitor è uno strumento comodo per attraversare sistematicamente il MIR, sia per cercare cose sia per apportare modifiche; è usato dalle analisi dataflow. `rustc` supporta il pattern Visitor con trait appositi definiti nel modulo `middle::mir::visit`:

- `Visitor` (opera su un `&Mir` e restituisce riferimenti condivisi);
- `MutVisitor` (opera su un `&mut Mir` e restituisce riferimenti mutabili).

### 7.2 Come si implementa un visitor?

Si crea un tipo che rappresenta il proprio visitor (tipicamente tiene lo stato necessario durante l'elaborazione del MIR) e si implementa per esso il trait `Visitor` o `MutVisitor`:

```rust
struct MyVisitor<...> { tcx: TyCtxt<'tcx>, ... }

impl<'tcx> MutVisitor<'tcx> for MyVisitor {
    fn visit_foo(&mut self, ...) {
        ...
        self.super_foo(...);
    }
}
```

Inoltre il modulo `middle::mir::traversal` contiene funzioni utili per attraversare il CFG del MIR in ordini standard diversi (es. pre-order, reverse post-order, e altri).

---

# 8. MIR Dataflow Analysis (framework generale)

### 8.1 Dove viene usata la dataflow analysis in rustc?

È usata pervasivamente: per trovare variabili non inizializzate, determinare quali variabili sono live attraverso uno statement `yield` di un generatore, calcolare quali `Place` sono prese in prestito in un dato punto del CFG.

### 8.2 Come è strutturato il framework?

Una dataflow analysis è definita dal trait `Analysis`. Oltre al tipo dello stato dataflow, questo trait definisce il valore iniziale di quello stato all'ingresso di ogni blocco, e la **direzione** dell'analisi (forward o backward). Il **dominio** dell'analisi deve essere un **reticolo** (più precisamente un _join-semilattice_) con un operatore di join ben definito (vedi il modulo `lattice` e il trait `JoinSemiLattice`).

### 8.3 Che cosa sono le "effect" (transfer function)?

Il framework dataflow permette a ogni statement (e terminator) all'interno di un basic block di definire la propria transfer function; queste transfer function sono chiamate **effect**. Ciascun effetto viene applicato successivamente nell'ordine dataflow, e insieme definiscono la transfer function per l'intero basic block. È anche possibile definire un effetto per particolari archi uscenti di alcuni terminator.

Gli statement possono anche essere equipaggiati con **"before" effect**:

- i "before" effect sono applicati immediatamente prima dell'effetto non prefissato, indipendentemente dalla direzione dell'analisi: un'analisi backward applicherà il "before" effect e poi l'effetto "primario" quando calcola la transfer function per un basic block, esattamente come farebbe un'analisi forward;
- le varianti "before" sono utili, ad esempio, quando l'effetto della parte destra (right-hand side) di uno statement di assegnamento deve essere considerato separatamente da quello della parte sinistra.

### 8.4 Come si ispezionano i risultati di una dataflow analysis?

Dopo aver costruito un'analisi, si invoca `iterate_to_fixpoint`, che restituisce un `Results` contenente lo stato dataflow al punto fisso all'ingresso di ogni blocco. Da un `Results`, si può ispezionare lo stato dataflow al punto fisso in qualunque punto del CFG:

- se serve lo stato solo in pochi punti (es. a ogni terminator `Drop`), si usa un `ResultsCursor`;
- se serve lo stato a _ogni_ punto, un `ResultsVisitor` è più efficiente.

```rust
// Uso di un ResultsVisitor
let mut my_visitor = MyVisitor::new();
let results = MyAnalysis::new().iterate_to_fixpoint(tcx, body, None);
results.visit_with(body, &mut my_visitor);

// Uso di un ResultsCursor
let mut results = MyAnalysis::new()
    .iterate_to_fixpoint(tcx, body, None)
    .into_results_cursor(body);
// ispeziona lo stato al punto fisso immediatamente prima di ogni terminator `Drop`
for (bb, block) in body.basic_blocks().iter_enumerated() {
    if let TerminatorKind::Drop { .. } = block.terminator().kind {
        results.seek_before_primary_effect(body.terminator_loc(bb));
        let state = results.get();
        println!("state before drop: {:#?}", state);
    }
}
```

Il framework offre anche diagrammi **Graphviz** per ispezionare visivamente lo stato dataflow (mostrando lo stato completo all'ingresso e all'uscita di ogni blocco).

---

# 9. Drop Elaboration

### 9.1 Perché non basta un semplice terminator Drop?

Quando viene costruito il MIR, i terminator `Drop` e `DropAndReplace` rappresentano punti dove i drop _possono_ verificarsi; tuttavia, in questa fase, la loro presenza non garantisce che un distruttore verrà effettivamente eseguito. Occorre tenere traccia di **se una variabile è inizializzata dinamicamente**:

```rust
let mut y = vec![];
{
    let x = vec![1, 2, 3];
    if std::process::id() % 2 == 0 {
        y = x; // move condizionale di `x` in `y`
    }
} // `x` esce dallo scope qui. Va droppato?
```

Quando una variabile o un temporaneo inizializzato esce dallo scope, il suo distruttore viene eseguito (viene "droppato"). Anche l'assegnamento esegue il distruttore del proprio operando sinistro, se inizializzato. Se una variabile è stata parzialmente inizializzata, solo i suoi campi inizializzati vengono droppati. **Se una variabile è inizializzata o meno è noto solo a runtime.**

### 9.2 Che cosa sono i "drop obligation"?

Quando una variabile locale diventa inizializzata, stabilisce un insieme di **drop obligation**: un insieme di path strutturali (es. una locale `a`, o un path a un campo `b.f.y`) che devono essere droppati.

- Le drop obligation per una variabile locale `x` di tipo struct `T` sono calcolate analizzando la struttura di `T`. Se `T` stesso implementa `Drop`, allora `x` è una drop obligation. Se `T` non implementa `Drop`, l'insieme delle drop obligation è l'unione delle drop obligation dei campi di `T`.
- Quando un path strutturale viene mosso (e diventa quindi non inizializzato), qualunque drop obligation per quel path o i suoi discendenti (`path.f`, `path.f.g.h`, ecc.) vengono rilasciate.
- Quando una variabile locale esce dallo scope (`Drop`), o quando un path strutturale viene sovrascritto tramite assegnamento (`DropAndReplace`), si controllano le drop obligation per quella variabile/path.
- A meno che l'obligation non sia stata rilasciata a quel punto, l'implementazione `Drop` associata viene chiamata. Per i tipi enum, vanno droppati solo i campi corrispondenti alla variante "attiva": si controlla il discriminante per determinare la variante attiva; le drop obligation delle altre varianti sono ignorate.

### 9.3 Che cos'è un "drop flag" e cos'è la drop elaboration?

Un modello valido per queste regole è mantenere un **flag booleano** (un "drop flag") per ogni path strutturale usato in qualche punto della funzione. Questo flag viene impostato quando il path è inizializzato, e azzerato quando il path viene mosso. Quando avviene un `Drop`, si controllano i flag per ogni obligation associata al target del `Drop` e si chiama l'implementazione `Drop` associata per quelle ancora applicabili.

Questo processo — trasformare il MIR appena costruito, con i suoi terminator `Drop`/`DropAndReplace` imprecisi, in uno con drop flag — è noto come **drop elaboration**.

- Quando uno statement MIR causa l'inizializzazione (o la de-inizializzazione) di una variabile, la drop elaboration inserisce codice che imposta (o azzera) il drop flag per quella variabile.
- Avvolge i terminator `Drop` in condizionali che controllano i drop flag appena inseriti.
- Una volta completato, i terminator `Drop` nel MIR corrispondono a una chiamata al **"drop glue"** (o "drop shim") per il tipo della place droppata. Il drop glue per un tipo chiama l'implementazione `Drop` per quel tipo (se esiste), e poi chiama ricorsivamente il drop glue per tutti i campi di quel tipo.

### 9.4 Quali ottimizzazioni applica rustc nella drop elaboration?

- solo i path che sono target di un `Drop` (o che hanno il target come prefisso) necessitano di drop flag;
- alcune variabili sono note come inizializzate (o non inizializzate) quando vengono droppate: queste non necessitano di drop flag;
- se un insieme di path sono droppati o mossi solo tramite un prefisso condiviso, questi path possono condividere un singolo drop flag.

Un sottoinsieme di queste ottimizzazioni è implementato in `rustc`. La drop elaboration designa ogni `Drop` nel MIR appena costruito con uno di quattro tipi:

- **Static**: il target è sempre inizializzato;
- **Dead**: il target è sempre non inizializzato;
- **Conditional**: il target è interamente inizializzato oppure interamente non inizializzato (non parzialmente);
- **Open**: il target può essere parzialmente inizializzato.

Per determinarlo, usa una coppia di analisi dataflow: `MaybeInitializedPlaces` e `MaybeUninitializedPlaces`. Se una place è in una ma non nell'altra, è noto a compile-time se è `Dead` o `Static`: il target non necessita di un flag, e il terminator `Drop` viene rimosso (`Dead`) o preservato (`Static`). Per i drop `Conditional`, viene generato un drop flag per il target.

### 9.5 Che cos'è un "Open Drop"?

Concretamente, nelle fasi di costruzione del MIR e di analisi iniziale, un `drop(x)` può essere "open" nel senso che il compilatore sa che `x` deve essere droppato, ma non ha ancora completamente elaborato _come_ avvenga il drop. Questo include: se `x` ha un'implementazione `Drop` personalizzata, se `x` è parzialmente inizializzato o parzialmente mosso, quali campi di `x` devono ancora essere droppati, e in quale ordine devono avvenire i drop annidati.

Più avanti nella pipeline, durante la drop elaboration, questi open drop vengono trasformati in sequenze completamente esplicite di operazioni di drop (a volte chiamate drop "closed"), dove tutti i percorsi di controllo di flusso sono resi espliciti, tutti i drop field-wise vengono inseriti, e i drop condizionali (dipendenti dai move) sono gestiti precisamente.

**Perché esiste questa separazione**: consente al compilatore di mantenere il MIR più semplice durante le analisi iniziali (borrow checking, dataflow) e solo successivamente espandere i drop nella loro forma low-level completa necessaria per l'esecuzione corretta. Un Open Drop è essenzialmente un placeholder per la semantica di distruzione, che viene raffinato in operazioni concrete nelle passate MIR successive.

---

# 10. Il Borrow Checker sul MIR

### 10.1 Che cosa verifica il borrow checker, oltre a ownership e borrowing?

Il borrow checker di Rust è responsabile di far rispettare le regole di Ownership e Borrowing, più: **tutte le variabili sono inizializzate prima di essere usate**.

### 10.2 Perché il borrow checking sul MIR (e non sull'HIR) è vantaggioso?

Un'implementazione più vecchia operava sull'HIR. Fare il borrow checking sul MIR ha diversi vantaggi:

- il MIR è molto meno complesso dell'HIR; il radicale desugaring aiuta a prevenire bug nel borrow checker;
- soprattutto, usare il MIR abilita le **"non-lexical lifetimes"** (NLL), che sono region derivate dal control-flow graph.

### 10.3 Il borrow checking come program analysis

- **Dominio**: il checker ragiona su places, move path, loan, stati di inizializzazione e region in locazioni di un CFG MIR;
- **Vincoli**: il type checking sul MIR genera vincoli di region, mentre le analisi di move e borrow producono fatti sui punti del programma;
- **Dataflow**: le classiche idee di gen/kill e punto fisso appaiono nel calcolo di inizializzazione, liveness e validità dei loan;
- **Diagnostica**: il risultato non è solo accetta/rifiuta; il compilatore mappa i fatti a spans del sorgente per spiegare perché un borrow o un move non è valido.

### 10.4 Quali sono le fasi (dettagliate) del MIR Borrow Checker?

1. **Entry point**: la query `mir_borrowck`; il borrow checker è implementato in `rustc_borrowck` ed è invocato come query sul MIR.
2. **Duplicazione e preparazione del MIR**: viene creata una copia locale del MIR, che sarà mutata in place per attaccarvi le informazioni di region.
3. **Inizializzazione delle variabili di region**: `replace_regions_in_mir` sostituisce tutte le annotazioni di lifetime con variabili di inferenza fresche.
4. **Analisi dataflow (move e initialization)**: le analisi calcolano quando i valori sono mossi, inizializzati o invalidati attraverso il CFG.
5. **Secondo type checking sul MIR**: un type check a livello MIR deriva vincoli fra region (lifetime).
6. **Region inference (risoluzione dei vincoli)**: calcola l'insieme dei punti del CFG in cui ogni lifetime deve valere, tramite inferenza fixpoint-style.
7. **Insiemi di borrow / borrow in scope**: determina quali borrow sono attivi in ogni punto del programma nel control-flow graph.
8. **Passata finale di validazione (error reporting)**: un secondo attraversamento controlla le operazioni (es. `*a + 1`) rispetto a stato di inizializzazione, regole di borrowing e vincoli di mutabilità.

### 10.5 Esempio completo (1): funzione semplice senza errori

```rust
fn example(a: &mut i32) -> i32 {
    let x = *a;
    *a = x + 1;
    x
}
```

MIR semplificato iniziale:

```text
fn example(_1: &mut i32) -> i32 {
    let mut _0: i32; // return
    let mut _2: i32; // x
    bb0: {
        _2 = (*_1);      // lettura tramite il borrow
        (*_1) = _2 + 1;  // scrittura tramite il borrow
        _0 = _2;
        return;
    }
}
```

**Fasi 1–2 (region variable + preparazione)**: tutte le lifetime nel MIR sono sostituite con variabili di region fresche, ad es. `_1: &mut i32` diventa `_1: &'r1 mut i32`. Queste `'r1, 'r2, …` sono incognite da risolvere in seguito; il MIR è ora annotato ma non ancora validato.

**Fase 3 (dataflow su move/initialization)**: si calcola dove le variabili sono inizializzate, dove i valori sono mossi, dove diventano invalidi (analisi dataflow classica sul CFG, simile alla liveness). In questo esempio: `_2` è inizializzata a `_2 = (*_1)`; `_1` è usata ma non mossa; nessuna lettura da non inizializzato.

**Fasi 4–5 (vincoli + region inference)**. Generazione dei vincoli dalle operazioni MIR: `_2 = (*_1)` richiede che `'r1` sia valida in quel punto del programma; `(*_1) = _2 + 1` richiede che `'r1` sia ancora valida, senza borrow in conflitto. Risoluzione: `'r1 = {bb0 entry … bb0 exit}` — la lifetime deve coprire tutti gli usi di `_1`. Analisi CFG-based, fixpoint-style, come nei framework dataflow.

**Fasi 6–7 (borrow in scope + verifica finale)**. Ad ogni punto del programma si calcola, ad es., `IN[bb0]: { mut borrow of _1 }`, dicendoci quali riferimenti sono attivi e quali vincoli di aliasing devono valere (concettualmente simile ai live set, ma per i borrow). Si valida quindi ogni statement MIR, ad es. per `(*_1) = _2 + 1`: `_1` è inizializzata? SÌ. `_1` è presa in prestito mutabilmente più di una volta? NO. Ci sono borrow immutabili in conflitto? NO. ⇒ **OK**.

### 10.6 Esempio completo (2): dangling reference rifiutato

```rust
fn bad() -> &i32 {
    let x = 10; // allocato sullo stack
    &x
}
```

MIR semplificato:

```text
fn bad() -> &i32 {
    let mut _0: &i32; // return place
    let mut _1: i32;  // x
    bb0: {
        _1 = const 10;
        _0 = &_1; // borrow di una locale
        return;
    }
}
```

**Fasi 1–2**: lifetime sostituite con region fresche, incluse region aggiuntive per i borrow: `_0: &i32` → `_0: &'r0 i32`; `_0 = &_1` → `_0 = &'r1 _1`.

**Fase 4 (constraint generation)**: dall'assegnamento `_0 = &'r1 _1` viene generato il vincolo `'r1 : 'r0` ("`'r1` sopravvive almeno quanto `'r0`" — il borrow deve vivere almeno quanto il return).

**Fase 5 (region inference)**: si numerano i punti `bb0: [p1] _1 = 10; [p2] _0 = &_1; [p3] return`. Si ricava `'r1 = {p2, p3}` (regola di scope: `x` esce di scope dopo `p3`), mentre `'r0 = {p3, contesto del chiamante}`. Il vincolo `'r1 : 'r0` richiede che tutti i punti di `'r0` appartengano a `'r1`, il che è **falso** (il contesto del chiamante non è in `'r1`, perché `x` è locale e non sopravvive al ritorno). **Nota**: l'errore non è rilevato localmente al borrow, ma globalmente, dopo la region inference: vincoli + CFG + drop ⇒ insoddisfacibile.

### 10.7 Perché move e initialization sono "la stessa analisi"?

Il borrow checker tiene traccia di un insieme di "place inizializzate": l'assegnamento aggiunge all'insieme, il move rimuove dall'insieme. Dal punto di vista del compilatore, entrambi sono semplicemente transizioni di stato in un'unica analisi dataflow. Una variabile diventa inizializzata dopo l'assegnamento, ma un move (es. `drop(a)` o `b = a`) la rende di nuovo non inizializzata, causando errori sugli usi successivi. La granularità è quella dei **"move path"**, non delle variabili: si traccia a livello di `a`, `a.0`, `a.b.c`, permettendo un ragionamento fine sui partial move.

```rust
fn foo() {
    let a: Vec<u32>;
    // a non è ancora inizializzata
    a = vec![22];
    // a è inizializzata qui
    std::mem::drop(a); // a viene mossa qui
    // a non è più inizializzata qui
    let l = a.len(); //~ ERRORE
}
```

### 10.8 Che cosa sono i "move path" nel dettaglio?

I move path sono approssimativamente le **MIR Place** (ottimizzate). Ogni move path rappresenta una locazione di memoria ed è salvato come `MovePathIndex` per efficienza.

- **Costruzione**: i move path sono costruiti attraversando il MIR (`MoveData::gather_moves`), registrando dove ogni place è inizializzata o mossa.
- **Move path illegali esclusi**: non viene creato tracciamento per elementi di array (`foo[1]`) né per borrow dereferenziati (`*foo`), riducendo l'overhead dell'analisi.
- **Struttura ad albero**: i move path formano un albero gerarchico (es. `a → a.b → a.b.c`), permettendo query su genitori/figli e un'analisi efficiente dei partial move.

```rust
fn foo() {
    let a: (Vec<u32>, Vec<u32>) = (vec![22], vec![44]);
    // a.0 e a.1 sono entrambi inizializzati
    let b = a.0; // muove a.0
    // a.0 non è inizializzato, ma a.1 lo è ancora
    let c = a.0; // ERRORE
    let d = a.1; // OK
}
```

---

# 11. Move Analysis come Dataflow Analysis

### 11.1 Come si formalizza la move/initialization analysis come dataflow?

È un problema dataflow **forward**. Dominio: `IN[n], OUT[n] ⊆ MovePaths`, dove ogni elemento è un move path (es. `a`, `a.0`, `a.b.c`). Significato: `IN[n]` = inizializzato prima dello statement `n`; `OUT[n]` = inizializzato dopo lo statement `n`. Equazioni dataflow standard:

```text
OUT[n] = GEN[n] ∪ (IN[n] − KILL[n])
IN[n]  = ⋃ OUT[p]   per tutti i predecessori p
```

### 11.2 Che cosa sono GEN e KILL in questo contesto?

- **GEN[n]** (inizializzazioni): gli assegnamenti (`a = ...`) aggiungono `a` all'insieme inizializzato;
- **KILL[n]** (move): i move (`let b = a; drop(a);`) rimuovono `a` dall'insieme inizializzato.

### 11.3 Esempio (caso scalare)

```rust
let a: Vec<u32>;
a = vec![22];
drop(a);
let l = a.len(); // ERRORE
```

|Program Point|IN|GEN|KILL|OUT|
|---|---|---|---|---|
|entry|∅|∅|∅|∅|
|`a = ...`|∅|{a}|∅|{a}|
|`drop(a)`|{a}|∅|{a}|∅|
|`a.len()`|∅|—|—|ERRORE|

`a ∉ IN` ⇒ uso di un valore non inizializzato.

### 11.4 Esempio field-sensitive (1): move del padre

```rust
let a: (Vec<u32>, Vec<u32>) = (vec![1,2,3], vec![4,5,6]);
let b = a;
```

Move path: `{a, a.0, a.1, b}`.

|Statement|GEN|KILL|
|---|---|---|
|`init a`|{a, a.0, a.1}|∅|
|`b = a`|{b}|{a, a.0, a.1}|

Risultato: `Initialized = {b}`. **Muovere un padre "uccide" tutti i figli.**

### 11.5 Esempio field-sensitive (2): move di un solo campo

```rust
let a: (Vec<u32>, Vec<u32>) = (vec![1,2,3], vec![4,5,6]);
let b = a.0;
```

Move path: `{a, a.0, a.1, b}`.

|Statement|GEN|KILL|
|---|---|---|
|`init a`|{a, a.0, a.1}|∅|
|`b = a.0`|{b}|{a.0}|

Risultato: `Initialized = {a, a.1, b}`. `a.0` è morto, ma `a.1` è ancora valido: **muovere un figlio non uccide i fratelli.**

### 11.6 Esempio field-sensitive (3): partial move con errore

```rust
let a: (Vec<u32>, Vec<u32>) = (vec![1,2,3], vec![4,5,6]);
let b = a.0;
let c = a; // ERRORE: uso di un valore parzialmente mosso
```

Move path: `{a, a.0, a.1, b, c}`.

|Statement|IN|GEN|KILL|
|---|---|---|---|
|`init a`|∅|{a, a.0, a.1}|∅|
|`b = a.0`|{a, a.0, a.1}|{b}|{a.0}|
|`c = a`|{a, a.1, b}|{c}|{a, a.0, a.1}|

Errore: uso di un valore `a` parzialmente mosso (`a.0` era già mosso, quindi `a` non è interamente inizializzata).

---

# 12. Il MIR Type Check

### 12.1 Che cosa fa, esattamente?

È un componente chiave del borrow check: attraversa il MIR ed esegue un "type check" completo. Durante questo type check, scopre anche i **vincoli di region** che si applicano al programma, così come i **type test** (obligation speciali riguardanti tipi che coinvolgono region), e sostituisce tutte le region nel corpo con nuove region non vincolate.

### 12.2 Perché serve, se il THIR era già completamente tipato?

Anche se il MIR è costruito dal THIR — già completamente type-checked — `rustc` esegue comunque un MIR type check perché il processo di lowering **non è banalmente type-preserving** e introduce nuovi costrutti e invarianti che devono essere validati indipendentemente. Durante la transizione THIR → MIR il compilatore esegue desugaring, introduce temporanei, riordina la valutazione, inserisce operazioni implicite (come borrow, move e drop) e semplifica le espressioni in un control-flow graph. Queste trasformazioni possono esporre inconsistenze o richiedere garanzie aggiuntive che non erano esplicitamente controllate a livello THIR.

Il MIR type check garantisce quindi che tutte queste operazioni abbassate siano internamente consistenti, che operandi e place abbiano i tipi corretti, e che gli invarianti richiesti dalle fasi successive (borrow checking, ottimizzazioni, codegen) siano rispettati. In altre parole, agisce come un passo di validazione difensiva: il THIR garantisce la correttezza del programma a livello sorgente, mentre il MIR type checking garantisce la correttezza della trasformazione del compilatore stesso verso il MIR.

### 12.3 Perché il MIR type check viene eseguito dopo la move analysis?

Perché il MIR type checker necessita delle informazioni prodotte dalla move analysis. Il suo scopo principale, all'interno del borrow checking, è generare vincoli precisi di region/lifetime, e questi vincoli dipendono dal sapere: quali place sono ancora inizializzate, quali move sono avvenuti, quali path è legale muovere, e quali local/place sono effettivamente rilevanti per l'analisi di borrow. L'ordinamento delle fasi è quindi guidato dalle dipendenze fra le analisi.

---

# 13. Region, Lifetime e Region Inference (NLL)

### 13.1 Qual è la relazione fra "lifetime" e "region"?

Nella terminologia di `rustc`, una **region** è la rappresentazione interna del compilatore per una lifetime, usata durante type checking e borrow checking. Una region denota un insieme di punti del programma (o scope nel CFG) in cui un riferimento è considerato valido. Invece di pensare le lifetime come scope puramente sintattici, il compilatore le modella come region che possono essere confrontate, vincolate (es. una region deve sopravvivere a un'altra) e inferite tramite un'analisi dataflow-like. La lifetime è quindi il concetto user-facing, mentre la region è il modello semantico/analitico interno del compilatore. Quando si scrive `'a`, il compilatore la traduce in una variabile di region e vincoli (es. `'a: 'b` diventa "la region `'a` sopravvive alla region `'b`"). Con le **NLL**, queste region non sono più legate a blocchi lessicali, ma corrispondono a insiemi precisi di punti del CFG, calcolati tramite risoluzione di vincoli.

### 13.2 Che cosa significa NLL?

**Non-Lexical Lifetimes**: la validità di un borrow può terminare nel punto della sua ultima utilizzazione effettiva, invece di coincidere necessariamente con la fine dello scope lessicale.

### 13.3 Esempio di NLL accettato

```rust
fn f() {
    let mut x = 10;
    let r = &x;
    println!("{}", r);
    let m = &mut x;
    *m += 1;
}
```

Il borrow condiviso `r` è live solo fino al suo ultimo uso: `'r = { punti fino all'ultimo uso di r }`. Dopo quel punto la region di `r` termina, così il borrow mutabile può cominciare: `'m = { punti da &mut x fino a *m += 1 }`. Poiché queste region non si sovrappongono, il programma è accettato.

### 13.4 Esempio di NLL rifiutato

```rust
fn f() {
    let mut x = 10;
    let r = &x;
    let m = &mut x;
    println!("{}", r); // r ancora vivo qui!
    *m += 1;
}
```

Qui `r` è ancora live al `println!` successivo alla creazione di `m`. Il compilatore vede che il borrow condiviso e quello mutabile si sovrappongono. Ciò viola le regole di borrowing, quindi il programma è **rifiutato**.

### 13.5 Quali sono le quattro fasi principali della region inference (NLL)?

1. **Identificare le universal region**: estrarre le region libere dalla firma della funzione (es. `'a`, `'static`), che rappresentano le lifetime visibili al chiamante;
2. **Sostituire le region con variabili**: tutte le region del MIR diventano variabili di inferenza fresche, scartando l'informazione di lifetime lessicale ⇒ abilita l'analisi control-flow-sensitive (NLL);
3. **Generare i vincoli** (MIR type check): il type checker specializzato per il MIR produce vincoli di outlives (`'a: 'b`), vincoli di liveness e type test;
4. **Risolvere i vincoli** (region inference): si costruisce un `RegionInferenceContext` e si calcolano i valori delle region tramite propagazione dei vincoli / risoluzione fixpoint.

Dopo l'inferenza si eseguono i controlli d'errore: verifica dei type test e controllo delle universal region ("too big").

### 13.6 Come sono rappresentate le region?

Le region sono **insiemi di punti del programma**: ogni region è un insieme di locazioni del CFG in cui è valida. Gli elementi di una region includono: locazioni MIR (punti del programma); `end('a)` (la lifetime si estende nel chiamante); `end('static)` (il resto del programma); placeholder per region sconosciute. Per efficienza, sono implementate come **bitset** indicizzati da `RegionElementIndex`.

### 13.7 Quali tipi di vincolo guidano l'inferenza?

- **Outlives constraint** (`'a: 'b`): `'a` deve includere tutto ciò che è in `'b`; generati dal MIR type checker;
- **Liveness constraint**: una region deve essere valida ovunque venga usata;
- **Member constraint**: nascono da `impl Trait` (`member R_m of [R_c...]`).

Il MIR type checker raccoglie inoltre i **type test**, da verificare dopo la region inference.

### 13.8 Esempi di generazione dei vincoli

```rust
fn f<'a>(x: &'a u32) -> u32 {
    let y = x;
    *y
}
```

- **Vincolo di liveness semplice**: il borrow/riferimento salvato in `y` è live nel punto in cui `*y` viene usato.
- **Vincolo di outlives dall'assegnamento**: il compilatore introduce una region inferita, diciamo `'0`, per `y`: `x : &'a u32`, `y : &'0 u32`; per la validità dell'assegnamento serve `&'a u32 <: &'0 u32`, il che implica `'a : '0`.

### 13.9 Come funziona la propagazione dei vincoli?

- **Inizializzazione dalla liveness**: ogni region parte dai punti del CFG in cui è usata (dai vincoli di liveness);
- **Propagazione**: per ogni vincolo di outlives `'a: 'b`:

```text
'a ← 'a ∪ 'b ∪ {end('b)}
```

ripetuta fino al punto fisso (`propagate_constraints`);

- **crescita monotona**: i valori delle region sono insiemi che crescono; la propagazione è un dataflow union-based.

### 13.10 Perché servono le SCC (Strongly Connected Components)?

I vincoli di outlives (`'a: 'b`) sono rappresentati come un grafo diretto dove le region sono nodi e i vincoli sono archi. I cicli in questo grafo indicano region che devono essere uguali, quindi il compilatore calcola le **componenti fortemente connesse (SCC)** per raggrupparle insieme. Ogni SCC è trattata come una singola unità con un unico valore condiviso, migliorando l'efficienza. Dopo aver collassato i cicli in SCC, il compilatore lavora su un grafo ridotto di SCC, che è sempre un **DAG**. I vincoli fra region diventano vincoli fra SCC, permettendo una propagazione efficiente ed evitando dipendenze potenzialmente cicliche.

### 13.11 Che cosa sono i "type test" e perché sono separati dal solver?

Durante il MIR type checking, `rustc` genera vincoli e **type test**: obligation speciali riguardanti tipi che coinvolgono region. Il solver della region inference calcola una soluzione (una mappa da variabili di region a insiemi di punti del programma). Dopo che la soluzione è calcolata, `rustc` verifica tutti i type test salvati contro quella soluzione. Sono usati quando codificare un vincolo direttamente nel solver sarebbe troppo complesso o inefficiente, oppure quando è più pulito verificarlo dopo aver conosciuto le region finali.

Un type test verifica tipicamente che un tipo sia **well-formed** rispetto alle lifetime inferite:

|Codice Rust|Type test generato|Spiegazione|
|---|---|---|
|`fn f<'a, T>(x: &'a T) { let y: &'a T = x; }`|`T: 'a`|Il tipo `&'a T` è well-formed solo se il tipo referenziato `T` è valido per almeno `'a`. _Soddisfatto._|
|`fn f<'a, T>(x: T) { let r: &'a T; }`|`T: 'a`|Anche se `r` è solo una dichiarazione locale, il tipo annotato `&'a T` impone un'obligation di well-formedness su `T`. _Non soddisfatto._|
|`fn f<'a, T>(x: &'a [T]) { let y: &'a [T] = x; }`|`[T]: 'a`, riducibile/verificabile come `T: 'a`|Un riferimento a slice con lifetime `'a` richiede che il tipo degli elementi sia valido per `'a`. _Soddisfatto._|
|`struct S<T>(T); fn f<'a, T>(x: &'a S<T>) {}`|`S<T>: 'a`, che richiede `T: 'a`|Il riferimento `&'a S<T>` richiede che l'intero tipo referenziato `S<T>` sopravviva a `'a`; strutturalmente questo dipende da `T`.|

Esempio semplice dal tipo di ritorno:

```rust
fn f<'a,'b>(x: &'a u32) -> &'b u32 { x }
```

Restituire `x` dove è atteso `&'b u32` richiede `&'a u32 <: &'b u32`, quindi il compilatore genera il type test `'a: 'b`. Questo non viene usato come vincolo di outlives, ma solo verificato dopo la region inference — dunque la compilazione **fallisce**.

### 13.12 Perché non incorporare i type test direttamente nel solver?

Perché il solver delle region opera su un dominio relativamente semplice: insiemi di punti e vincoli di outlives. I tipi Rust possono invece essere arbitrariamente complessi: generics, tipi annidati, projection. Incorporare tutta questa complessità nel calcolo del punto fisso lo complicherebbe e lo rallenterebbe.

### 13.13 Che cosa sono le "universal region" e il controllo "too big"?

Le universal region si riferiscono a lifetime dichiarate dall'utente, come i parametri di lifetime (`'a`, `'b`) e `'static`. Sono **universalmente quantificate**: il compilatore deve garantire che la funzione sia corretta per **tutte** le possibili istanziazioni di queste lifetime (che soddisfino i vincoli dichiarati). Internamente, tutte le lifetime sono rappresentate come variabili di region: le universal region occupano un sottoinsieme fisso di queste variabili, mentre le region esistenziali rappresentano variabili di inferenza.

Durante la region inference, a ogni region viene assegnato un insieme contenente punti di controllo di flusso e marcatori speciali come `end('a)` che indicano l'estensione di una lifetime. Dopo la propagazione, il compilatore esegue un controllo di consistenza: se il valore inferito di una universal region `'a` include `end('b)`, allora la relazione `'a: 'b` deve essere stata dichiarata esplicitamente. In caso contrario, questo indica una violazione della firma della funzione e produce un errore di compilazione ("too big" check):

```rust
fn f<'a,'b>(x: &'a i32) -> &'b i32 { x } // NO: 'a contiene end('b) senza vincolo dichiarato

fn f<'a,'b>(x: &'a i32) -> &'b i32
where 'a: 'b
{ x } // OK
```

Questo garantisce che le relazioni di lifetime inferite non eccedano quelle promesse dai bound della funzione.

### 13.14 Che cos'è il `RegionInferenceContext`?

È la struttura dati centrale che contiene tutti gli input dell'inferenza:

- `constraints` → relazioni di outlives;
- `liveness_constraints` → i "semi" iniziali;
- `universal_regions` → le lifetime libere;
- `universal_region_relations` → i bound noti (es. le clausole `where`);
- `type_tests` → i vincoli da verificare dopo.

Il processo di risoluzione `solve()` esegue: `propagate_constraints` → `check_type_tests` → `check_universal_regions`.

### 13.15 Big Picture: due analisi, un solo framework

Il borrow checking di Rust è composto da **due analisi dataflow interagenti** sul MIR:

1. Move / Initialization Analysis (ownership);
2. Region Inference / NLL (lifetime).

Entrambe sono: basate sul CFG, monotone, risolte tramite iterazione al punto fisso.

|Aspetto|Move Analysis|Region Inference (NLL)|
|---|---|---|
|Dominio|Insieme di move path|Insieme di elementi di region|
|Direzione|Forward|Forward (propagazione)|
|Reticolo|Powerset|Powerset|
|Transfer|GEN/KILL|Unione tramite vincoli|
|Significato|"è inizializzato?"|"la region è valida qui?"|
|Punto fisso|Sì|Sì|

Equazioni riassuntive:

```text
OUT[n] = GEN[n] ∪ (IN[n] − KILL[n])       (move analysis)
IN[n]  = ⋃ OUT[p]

R_a = LIVENESS_a ∪ ⋃ { R_b ∪ end(b) | a: b }   (region inference)
```

Una differenza importante: la move analysis lavora sul CFG del MIR, mentre la region inference lavora sul **DAG delle SCC** del grafo (Region, Outlives).

### 13.16 Differenze e interazione fra le due analisi

- la **move analysis** può _rimuovere_ informazione (kill);
- la **region inference** _solo aggiunge_ informazione (gli insiemi crescono).

Dove interagiscono: la move analysis dice `drop(x) ⇒ x non inizializzato`; la region inference dice `r deve essere valida all'uso`. Un conflitto emerge quando la region dice "valido" ma la move analysis dice "il valore non c'è più":

```rust
let x = vec![1];
let r = &x;
drop(x);
*r; // errore
```

---

# 14. Two-phase borrows

### 14.1 Che cosa sono?

Una forma speciale di **mutable borrow** che si comporta temporaneamente come un borrow condiviso, per permettere pattern come `vec.push(vec.len())`. Sono introdotti solo in casi impliciti specifici (es. chiamate a metodo con receiver `&mut`, reborrow negli argomenti, e operatori di assegnamento composto). Implementati come temporanei con due punti chiave:

- un **punto di reservation**, dove inizia il comportamento "shared-like";
- un **punto di activation**, dove diventa un borrow mutabile a pieno titolo.

Sono trattati come mutable borrow ma con regole rilassate prima dell'attivazione.

### 14.2 Esempio completo con region e MIR

```rust
fn push_len(v: &mut Vec<i32>) {
    v.push(v.len() as i32);
}
```

Concettualmente il THIR desugarato è:

```text
Vec::push(&mut *v, (Vec::len(&*v)) as i32)
```

Con region fresche `_2: &'r_mut mut Vec<i32>` e `_3: &'r_shr Vec<i32>`, la soluzione delle region è:

```text
'r_shr = { p2, p3 }
'r_mut = { p1, p2, p3, p4, p5 }
```

ma `'r_mut` è **two-phase**: reservation a `p1`, activation a `p5`. Quindi fra `p1` e `p5` il borrow mutabile è solo _riservato_, e l'uso del borrow condiviso a `p3` è legale.

MIR corrispondente:

```text
fn push_len(_1: &mut Vec<i32>) -> () {
    let mut _0: ();
    let mut _2: &mut Vec<i32>;
    let mut _3: &Vec<i32>;
    let mut _4: usize;
    let mut _5: i32;
    bb0: {
        [p1] _2 = &mut (*_1);   // reservation del borrow mutabile
        [p2] _3 = &(*_1);       // borrow condiviso per len()
        [p3] _4 = Vec::<i32>::len(move _3);
        [p4] _5 = move _4 as i32 (IntToInt);
        [p5] _0 = Vec::<i32>::push(move _2, move _5); // activation
        return;
    }
}
```

Senza il meccanismo two-phase, il borrow mutabile `_2` sarebbe considerato attivo già a `p1`, rendendo illegale il borrow condiviso `_3` a `p2` (violazione di [B2]).

### 14.3 Perché servono?

Per permettere pattern naturali dove una chiamata richiede un receiver mutabile ma gli argomenti devono temporaneamente usare lo stesso valore tramite un borrow condiviso. `vec.push(vec.len())` è l'esempio classico: il borrow mutabile viene prima **prenotato** (reservation) e solo successivamente **attivato** (activation).

---

# 15. Closure Capture Inference

### 15.1 Che cosa deve determinare il compilatore per una closure?

Le closure Rust sono compilate trasformandole in struct che salvano le variabili catturate. Il compilatore deve:

- identificare quali variabili dell'ambiente circostante la closure usa (gli **upvar**);
- determinare come ciascuna è usata (letta, modificata o consumata);
- in base a questo, decidere la modalità di cattura: per riferimento condiviso (`&T`), per riferimento mutabile (`&mut T`), oppure per valore (move).

Questa analisi permette anche a `rustc` di inferire quale trait di closure la closure implementa: `Fn` (solo lettura), `FnMut` (muta), `FnOnce` (consuma valori).

### 15.2 Quando avviene questa inferenza?

Durante la fase di **type checking**, specificamente nello stadio di type-checking dell'**HIR**. Più precisamente: avviene dopo il parsing e l'abbassamento a HIR, durante l'inferenza di tipo e la preparazione al borrow checking.

### 15.3 Tre esempi completi di variable capture con relativo MIR

**Solo lettura (Fn)**:

```rust
fn invoke(f: impl Fn()) { // anche FnMut(), FnOnce()
    f();
}
fn main() {
    let x: i32 = 10;
    invoke(|| println!("Hi {}", x)); // la closure legge solo x
    println!("Value of x after return {}", x);
}
```

MIR (parziale):

```text
bb0: {
    _1 = const 10_i32;
    _4 = &_1;
    _3 = {closure@immut.rs:13:12: 13:14} { x: move _4 }; // struct con init
    _2 = invoke::<{closure@immut.rs:13:12: 13:14}>(move _3) -> [return: bb1, unwind continue];
}
```

**Mutazione (FnMut)**:

```rust
fn invoke(mut f: impl FnMut()) { // anche FnOnce()
    f();
}
fn main() {
    let mut x: i32 = 10;
    invoke(|| {
        x += 10; // la closure muta x
        println!("Hi {}", x)
    });
    println!("Value of x after return {}", x);
}
```

MIR (parziale):

```text
bb0: {
    _1 = const 10_i32;
    _4 = &mut _1;
    _3 = {closure@mut.rs:7:12: 7:14} { x: move _4 };
    _2 = invoke::<{closure@mut.rs:7:12: 7:14}>(move _3) -> [return: bb1, unwind continue];
}
```

**Move (FnOnce)**:

```rust
fn invoke(f: impl FnOnce()) { // errore con Fn() o FnMut()
    f();
}
fn main() {
    let x = vec![21];
    invoke(|| {
        drop(x); // rende x inutilizzabile in seguito
    });
    // println!("Value of x after return {:?}", x); // non compilerebbe
}
```

MIR (parziale):

```text
bb2: {
    _4 = {closure@drop.rs:7:12: 7:14} { x: move _1 }; // move di x
    _3 = invoke::<{closure@drop.rs:7:12: 7:14}>(move _4) -> [return: bb3, unwind continue];
}
```

### 15.4 Che cos'è un upvar e come funziona l'inferenza incrementale?

Un **upvar** è una variabile della funzione circostante catturata da una closure (una "variabile libera"). Il compilatore le identifica con un'analisi interna (`upvars_mentioned`). Le closure differiscono dalle funzioni normali perché catturano e prendono in prestito questi upvar dal loro ambiente.

`rustc` inferisce come ciascun upvar è catturato partendo da un **borrow immutabile** e rilassandolo se necessario:

- rimane immutabile se solo letto;
- diventa mutabile se modificato;
- diventa move se consumato (es. droppato).

In base a questo, la closure implementa il trait appropriato: `Fn` → borrow immutabile; `FnMut` → borrow mutabile; `FnOnce` → semantica move.

### 15.5 Come funziona il meccanismo Visitor/Delegate?

`upvar.rs` definisce `euv::ExprUseVisitor`, che attraversa il sorgente della closure e invoca una callback per ogni upvar che viene preso in prestito, mutato o mosso:

```rust
fn main() {
    let mut x = vec![21];
    let _cl = || {
        let y = x[0];   // 1. shared borrow
        x[0] += 1;      // 2. mutable borrow
    };
}
```

In questo esempio il visitor viene chiamato due volte, per le righe marcate 1 e 2, una volta per un borrow condiviso e una per un borrow mutabile (e ci dice anche _cosa_ è stato preso in prestito). Le callback sono definite implementando il trait `Delegate`.

`InferBorrowKind` implementa il trait `Delegate` e traccia come ciascun upvar viene catturato:

- `ByValue` (mosso);
- `ByRef` (preso in prestito), con i tipi: `ImmBorrow`, `UniqueImmBorrow`, `MutBorrow`.

Le callback chiave sono: `consume` → la variabile è mossa; `borrow` → la variabile è presa in prestito; `mutate` → la variabile è modificata. Ogni callback riceve un `cmt` (Category, Mutability, Type) che descrive origine, locazione e mutabilità della variabile. In base a queste callback, il compilatore aggiusta il borrow kind e registra la modalità di cattura finale per ogni closure.

---

# 16. MIR Optimization

### 16.1 Quando e perché il MIR viene ottimizzato?

Dopo il borrow checking e prima della monomorphization/codegen, ossia mentre il MIR è ancora **generico**. Le ottimizzazioni MIR migliorano il MIR prima della generazione di codice nel backend, migliorando sia le prestazioni runtime sia la velocità di compilazione: un MIR migliore produce codice macchina migliore e riduce il lavoro di ottimizzazione richiesto in seguito (es. da LLVM).

**Perché prima della monomorphization**: le ottimizzazioni sono efficaci proprio perché il MIR è ancora generico — avvengono prima della monomorphization, quindi la versione migliorata viene riusata per tutte le istanziazioni concrete di quella funzione o tipo generico. Questo evita di ripetere lo stesso lavoro per ogni versione specializzata.

### 16.2 Come sono organizzate le passate?

L'ottimizzazione MIR è implementata come una sequenza di **passate**: alcune sono obbligatorie, alcune servono solo a validare invarianti o eseguire controlli, alcune sono abilitate solo nelle build ottimizzate/release. Le tipiche ottimizzazioni MIR semplificano e ripuliscono il control-flow graph: constant propagation, dead-code elimination, copy propagation, CFG simplification e inlining. La query `optimized_mir` guida il processo.

La funzione `run_optimization_passes` definisce l'elenco delle passate e il loro ordine: contiene un array di passate, ognuna delle quali è una struct che implementa il trait `MirPass` (l'array è un array di trait object `&dyn MirPass`). Tipicamente una passata è implementata nel proprio modulo del crate `rustc_mir_transform`.

Esempi di passate:

- `CleanupPostBorrowck`: rimuove alcune informazioni necessarie solo per l'analisi, non per il codegen;
- `ConstProp`: esegue constant propagation.

Il sistema è facilmente estensibile con nuove passate di ottimizzazione.

### 16.3 Livelli di ottimizzazione

```bash
rustc main.rs -C opt-level=X
```

con `X` in `[0, 1, 2, 3, s, z]`:

- `0` → nessuna ottimizzazione (compilazione veloce, buono per debug);
- `1` → ottimizzazioni di base;
- `2` → build ottimizzata standard;
- `3` → ottimizzazioni aggressive;
- `s` → ottimizza per la dimensione del binario;
- `z` → ottimizza ancora di più per la dimensione.

`cargo build` usa il livello `0`; `cargo build --release` usa il livello `3`.

---

# 17. Monomorfizzazione e implementazioni dei generics

### 17.1 Come implementano i generics i diversi linguaggi? (confronto)

|Linguaggio|Meccanismo dei bound|Idea implementativa principale|Trade-off principale|
|---|---|---|---|
|Haskell|Type classes|Dictionary passing + polimorfismo parametrico|Codice compatto, chiamate indirette a meno di ottimizzazione|
|Java|Interfacce / bound|Type erasure|Compatto, meno specificità di tipo a runtime, indirezione|
|C++|Template / concept|Monomorphization|Veloce/specializzato, code bloat|
|C#|Interfacce / vincoli|Generics reificati, ibrido shared/specializzato|Più informazione di tipo a runtime, value type efficienti|

### 17.2 Come implementa i generics Rust?

Rust ha ampio supporto per i tipi generici, con **polimorfismo universale esplicito vincolato**: i bound sono espressi tramite Trait. Rust **monomorfizza** tutti i tipi generici: il compilatore genera una copia diversa del codice di una funzione generica per ogni tipo concreto necessario. La monomorphization è il **primo passo del backend**: il MIR generico viene istanziato prima della generazione di codice. Vale lo stesso trade-off del C++: veloce/specializzato, ma con code bloat.

### 17.3 Come funziona la Mono Item Collection?

Per ogni cosa generica il compilatore deve raccogliere tutti i tipi concreti che la istanziano: questo compito è svolto dal **monomorphization collector**, eseguito appena prima del MIR lowering e del codegen. `rustc_codegen_ssa::base::codegen_crate` invoca la query `collect_and_partition_mono_items`, che esegue la mono item collection e poi la partiziona in codegen unit.

- Un **mono item** rappresenta un artefatto che deve generare codice backend: funzione, metodo, closure, static, drop glue. Deve essere scoperta anche ogni istanza monomorfizzata concreta di codice generico, inclusi i generics importati da altri crate.
- Un mono item corrisponde a qualcosa che diventa una funzione o un oggetto globale nella IR generata. I mono item dipendono l'uno dall'altro (es. una funzione che ne chiama un'altra), formando un **grafo di mono item diretto**.
- L'algoritmo di collezione lavora in due fasi:
    1. trova i **graph root** attraversando l'HIR del crate e raccogliendo gli item pubblici/non generici;
    2. a partire da quelle radici, ispeziona ricorsivamente il MIR per scoprire tutti i mono item usati e le loro istanziazioni concrete di tipo.

### 17.4 Da cosa nascono gli archi del mono item graph?

Non solo dalle chiamate esplicite di funzione. Nascono anche da: chiamate a funzione/metodo; riferimenti a funzioni; generazione del drop glue; cast di unsizing verso trait object (che richiedono vtable); funzioni generiche cross-crate/inline.

```rust
fn print_val<T: Display>(x: T) {
    println!("{}", x);
}
fn call_fn(f: &dyn Fn(i32), x: i32) {
    f(x);
}
fn main() {
    let print_i32 = print_val::<i32>;
    call_fn(&print_i32, 0);
}
```

### 17.5 Lazy vs eager collection

- **Lazy collection**: istanzia solo gli item effettivamente usati, minimizzando il codice generato;
- **Eager collection**: istanzia più item in modo proattivo, utile per l'incremental compilation e per un comportamento di ricompilazione più stabile.

### 17.6 Perché rustc tiene traccia anche dei "mentioned item"?

Il collector valuta anche le costanti e traccia i "mentioned item": non solo gli item effettivamente usati dopo l'ottimizzazione, ma anche quelli che appaiono sintatticamente nel MIR. Questo garantisce che i fallimenti di valutazione a compile-time (const evaluation) vengano riportati in modo consistente anche se il codice morto viene successivamente eliminato dall'ottimizzazione — così il risultato della compilazione non dipende dalle ottimizzazioni applicate.

### 17.7 Che cosa sono le Codegen Unit (CGU) e qual è il loro trade-off?

Una **CGU** è un insieme di coppie (mono-item, linkage) che diventa un unico modulo LLVM. Il partitioner decide quali funzioni, static, closure e monomorfizzazioni vanno in quale CGU. Il partizionamento è cruciale per le prestazioni della compilazione incrementale: **LLVM ricompila e ottimizza interi moduli**, non singole funzioni — se una codegen unit cambia, l'intero modulo LLVM deve essere ricostruito e ri-ottimizzato da zero.

Trade-off:

- **molte CGU piccole** → minima ricompilazione dopo un cambiamento, build incrementali più veloci, eseguibili potenzialmente più lenti (ottimizzazioni inter-procedurali e inlining non possibili tra moduli diversi);
- **poche CGU grandi** → migliore ottimizzazione LLVM e più inlining, eseguibili potenzialmente più veloci, ricompilazione più costosa.

Il partitioner bilancia questi obiettivi contrastanti con un'euristica basata sui moduli a livello sorgente: per ogni modulo sorgente, `rustc` crea una CGU per il codice non-generico stabile, e una CGU per le istanze monomorfizzate generiche volatili — isolando i cambiamenti causati dalle istanziazioni generiche e riducendo la ricompilazione non necessaria.

**Perché i generics complicano l'incremental compilation**: aggiungere o rimuovere un riferimento a una funzione generica può creare o eliminare istanze monomorfizzate, forzando la ricompilazione anche quando il corpo della funzione generica stessa non è cambiato.

**Perché l'inlining influenza il partizionamento**: LLVM può fare inlining solo quando il corpo del callee è disponibile nello stesso modulo LLVM; per questo il partitioner duplica funzioni eleggibili fra CGU quando necessario. `rustc` tratta principalmente le funzioni marcate `#[inline]` come candidate per l'inlining cross-CGU.

### 17.8 Come avviene il lowering da MIR a codegen IR?

Dopo la mono item collection, `rustc` abbassa il MIR in una IR di backend — di solito LLVM IR, sebbene siano supportati anche Cranelift e GCC. La monomorphization avviene durante questo processo di lowering. La generazione di codice comincia in `codegen_crate` e raggiunge `codegen_mir`. La logica di lowering è divisa per costrutto MIR, con moduli diversi che gestiscono elementi diversi:

- `block` → basic block e terminator (specialmente chiamate a funzione e unwinding);
- `statement` → statement MIR;
- `operand` → operandi;
- `place` → riferimenti a memoria/place;
- `rvalue` → calcoli e valori temporanei.

Prima della traduzione vengono eseguite passate di analisi leggere: `rustc` rileva variabili "SSA-like" così da poterle emettere direttamente in forma SSA invece di affidarsi interamente a ottimizzazioni LLVM come `mem2reg`. I basic block MIR di solito mappano direttamente a basic block LLVM, sebbene alcuni costrutti (assertion, intrinsic, chiamate complesse, gestione dell'unwinding) possano espandersi in più basic block LLVM.

### 17.9 Quali backend supporta rustc, dopo il borrow checking?

```text
borrow checked MIR
      ↓
cleanup
      ↓
runtime MIR preparation (incl. Drop elaboration)
      ↓
MIR optimization (codice ancora generico)
      ↓
monomorphization collection
      ↓
codegen IR (per ogni tipo concreto collezionato)
      ↓
backend (LLVM / Cranelift / GCC)
      ↓
machine code + linking
```

- **LLVM IR** è il percorso tipico, stabile e pronto per ulteriori ottimizzazioni;
- **Cranelift** è più sperimentale: un backend veloce, sicuro e relativamente semplice, che compila una IR (con basic block, valori SSA-like, controllo di flusso, ecc.) verso codice macchina eseguibile; obiettivo particolarmente interessante per build di debug/locali; l'uso più comune è come compilatore per WebAssembly;
- **GCC IR** è una IR interna del compilatore GCC.

La complessità del codegen deriva da: supporto per backend multipli (il codice di codegen è generico rispetto all'implementazione di backend, con più livelli di astrazione) e dal fatto che il codegen avviene **in modo asincrono**, su un altro thread, per prestazioni (l'effettiva generazione di codice è delegata a una libreria di terze parti, uno dei tre backend).

---

# 18. Linting e diagnostica degli errori

### 18.1 Che cos'è un "lint" in rustc?

Nel software, un "lint" è uno strumento usato per migliorare il codice sorgente. `rustc` contiene numerosi lint: durante la compilazione esegue anche i lint. Questi possono produrre un warning, un errore o niente, a seconda della configurazione.

```rust
fn main() {
    let x = 5;
}
```

```text
$ rustc main.rs
warning: unused variable: `x`
--> main.rs:2:9
|
2 | let x = 5;
| ^
|
= note: `#[warn(unused_variables)]` on by default
= note: to avoid this warning, consider using `_x` instead
```

### 18.2 Lint vs diagnostica fissa

Alcuni messaggi sono emessi tramite lint, dove l'utente può controllarne il livello; la maggior parte delle diagnostiche è invece hard-coded, e l'utente non può controllarne il livello. Di solito è ovvio se una diagnostica debba essere "fissa" o un lint, ma esistono zone grigie:

- **errori del borrow checker**: sono errori fissi; l'utente non può regolare il livello per silenziare il borrow checker;
- **dead code**: è un lint; anche se l'utente probabilmente non vuole codice morto nel proprio crate, renderlo un errore rigido renderebbe il refactoring e lo sviluppo molto dolorosi;
- **lint future-incompatible**: sono lint silenziabili; vengono emessi warning che saranno eventualmente trasformati in errori fissi (hard).

### 18.3 I livelli dei lint

`rustc` divide i lint in sei livelli:

1. `allow` → non fa nulla;
2. `expect` → verifica che un lint specifico venga emesso;
3. `warn` → produce un warning, la compilazione procede (es. variabile non usata);
4. `force-warn` → come `warn`, ma il livello non può essere cambiato;
5. `deny` → produce un errore;
6. `forbid` → come `deny`, ma il livello non può essere cambiato.

Ogni lint ha un livello di default, e il compilatore ha un livello di warning di default.

### 18.4 Che cos'è il livello `expect`?

Permette di verificare che un lint specifico venga effettivamente emesso (es. in fase di debug, o prima di eliminare un lint): sopprime il lint atteso se viene emesso, ed emette un warning se non viene emesso.

```rust
fn main() {
    #[expect(unused_variables)] // attributo esterno
    // il lint `unused_variables` viene emesso:
    let unused = "Everyone ignores me"; // non stampa nulla

    #[expect(unused_variables)] // il lint `unused_variables` non viene emesso:
    let used = "I'm useful"; // aspettativa non soddisfatta -> warning
    println!("The `used` value is equal to: {:?}", used);
}
```

```text
warning: this lint expectation is unfulfilled
--> src/main.rs:7:14
|
7 | #[expect(unused_variables)]
| ^^^^^^^^^^^^^^^^
|
= note: `#[warn(unfulfilled_lint_expectations)]` on by default
```

### 18.5 Come si configurano i livelli dei lint?

Tramite flag del compilatore: `-A`, `-W`, `--force-warn`, `-D` e `-F` permettono di trasformare uno o più lint rispettivamente in `allow`, `warn`, `force-warn`, `deny` o `forbid`:

```bash
$ rustc lib.rs --crate-type=lib -D missing-docs # di solito allow
error: missing documentation for crate
error: missing documentation for a function
error: aborting due to 2 previous errors
```

Oppure tramite attributi nel codice:

```rust
#![warn(missing_docs)] // attributo interno
pub fn foo() {}
```

È anche possibile specificare più attributi e un parametro `reason` (mostrato quando il lint viene emesso):

```rust
#![warn(missing_docs)]
#![deny(unused_variables)]
pub fn foo() {}

use std::path::PathBuf;
pub fn get_path() -> PathBuf {
    #[allow(unused_mut, reason = "this is only modified on some platforms")]
    let mut file_name = PathBuf::from("git");
    #[cfg(target_os = "windows")] // attributo di compilazione condizionale
    file_name.set_extension("exe");
    file_name
}
```

### 18.6 Che cos'è il "capping" dei lint?

```bash
rustc --cap-lints LEVEL
```

imposta il "lint cap level": il livello massimo per tutti i lint. È la feature usata da Cargo quando compila le dipendenze: passa `--cap-lints allow`, così eventuali warning delle dipendenze non "inquinano" l'output della build.

### 18.7 Che cosa sono i "lint group"?

`rustc` ha il concetto di gruppo di lint, dove si possono attivare più warning attraverso un solo nome. Ad esempio il gruppo `nonstandard-style` imposta insieme `non-camel-case-types`, `non-snake-case` e `non-upper-case-globals`. Altri gruppi principali: `warnings` (tutti i lint impostati a warning), `deprecated-safe`, `future-incompatible`, `keyword-idents`, `nonstandard-style`, `refining-impl-trait`, `unused`.

### 18.8 In quali momenti della compilazione girano i lint?

|Tipo|Momento|Informazione disponibile|Uso tipico|
|---|---|---|---|
|Pre-expansion|Prima della macro expansion|AST grezzo, contesto limitato|compatibilità con edition e casi sensibili alle macro, es. `keyword_idents`|
|Early lint|Dopo macro expansion, prima del lowering|AST risolto, tipi non ancora completi|lint puramente sintattici, es. `unused_parens`|
|Late lint|Verso la fine dell'analisi, sull'HIR|HIR, tipi e semantica più ricca|check idiomatici o semantici, es. `non_snake_case` o `invalid_value`|
|MIR / inline|Dentro il MIR, borrowck o specifici percorsi di codice|stato specializzato del sottosistema|`arithmetic_overflow`, `unused_mut`, lint future-compat complessi|
|Driver / tool lint|Registrazione esterna, esecuzione nelle stesse fasi di cui sopra|dipende dalla passata registrata|Clippy e strumenti custom via `register_lints` e `rustc_driver`|

I lint girano in fasi diverse a seconda del loro significato. Molti sono raggruppati in passate eseguite con un unico visitor; altri sono collocati dove necessario nel codice.

### 18.9 Che cos'è Clippy?

Il linter ufficiale di Rust: un ampio insieme di analisi statiche aggiuntive ("lint") costruite sopra `rustc`, che aiutano a scrivere codice Rust più idiomatico, corretto, efficiente e mantenibile. Concettualmente: `rustc` verifica se il tuo programma è Rust _valido_; Clippy verifica se il tuo Rust è **buon** Rust. Clippy si integra direttamente nell'infrastruttura del compilatore, piuttosto che operare come parser/analizzatore separato: usa la stessa architettura di linting di `rustc`, registrando passate di lint custom tramite il compiler driver ed eseguendole dentro la normale pipeline di lint.

---

# 19. Il sistema di tipi di Rust, type checking e type inference

### 19.1 Quali sono le caratteristiche del sistema di tipi di Rust?

- **Nominale**;
- **sostrutturale (affine)**;
- Algebraic Data Type (struct, enum), con pattern matching;
- generics parametrici su tipi, costanti e lifetime;
- trait con funzioni associate, tipi associati e costanti;
- `impl Trait` per parametri anonimi e tipi di ritorno astratti;
- coercizioni fortemente ristrette.

```rust
struct ArrayRef<'a, T, const N: usize> {
    data: &'a [T; N],
}
```

### 19.2 Quali azioni compie il type checking in rustc?

|Azione|Scopo|
|---|---|
|Expression checking|Garantisce la correttezza di tipo delle operazioni (compatibilità di assegnamento, tipi degli operandi, tipi di ritorno, consistenza dei rami)|
|Method resolution|Trova i metodi chiamabili (cerca fra impl inerenti, impl di trait, catene di autoderef/autoref, valida il tipo del receiver)|
|Trait obligation checking|Valida le obligation di trait (`T: Clone`, tutte le obligation implicite, clausole where, supertrait) — es. `fn f<T: Clone>(x: T) { x.clone(); }`|
|Generic argument correctness|Verifica gli argomenti di tipo/const/lifetime (arità, vincoli, tipi di const, well-formedness) — es. `Array::<i32, 4>`|
|Coercion checking|Valida le conversioni implicite (`&mut T → &T`, array-to-slice, deref coercion, unsizing coercion)|
|Pattern checking|Verifica match/destructuring (validità dei costruttori, tipi dei binding, supporto all'esaustività, consistenza delle varianti enum)|
|Signature checking|Valida le interfacce di funzioni/closure (tipi dei parametri, tipo di ritorno, consistenza ABI, closure call trait `Fn`/`FnMut`/`FnOnce`)|
|Operator resolution|Tipizzazione basata sui trait per gli operatori (`a + b` diventa `Add::add(a, b)`)|
|Autoderef/autoref|Inserisce ref/deref impliciti (`x.len()` può diventare `(*(*x)).len()`; legalità della catena di deref, inserimento del borrow, correttezza della mutabilità)|
|Well-formedness checking|Garantisce che i tipi siano legali (bound, legalità ricorsiva, regole di varianza, sizedness, precondizioni di object safety) — es. `struct S<T: Copy> { x: T }`|
|ADT construction checking|Valida la costruzione di enum/struct (esistenza dei campi, visibilità, tipi dei campi, arità) — es. `Some(3)` o `Point{x:1,y:2}`|

### 19.3 Su quali basi teoriche si fonda il type inference di rustc?

Il type inference di Rust è un sistema **multi-dominio** di generazione e risoluzione di vincoli, su: tipi, lifetime (region), obligation di trait, projection, const generics. Si basa sull'algoritmo standard di **Hindley-Milner** (HM), esteso in vari modi per accomodare subtyping, region inference e tipi higher-ranked.

### 19.4 Quali azioni di inferenza compie rustc? (tabella completa)

|Azione di inferenza|Scopo|Esempio|Vincolo generato|
|---|---|---|---|
|Local variable inference|Inferisce il tipo delle variabili|`let x = 3;`|`x: ?T1` (fresca) → `?T1 = IntVar` (da `3`) → `IntVar = i32` (fallback)|
|Return type inference|Inferisce il tipo di ritorno|`fn f() { 3 }`|`return_type = body_type`|
|Generic argument inference|Inferisce i parametri generici|`let v = Vec::new(); v.push(3);`|`v: Vec<?T1>` → `?T1 = i32` (dalla chiamata a metodo) → `v: Vec<i32>`|
|Closure parameter/result inference|Inferisce parametri/risultati di closure|`let f = \|x\| x + 1;`|`x: ?T1`, `result: ?T2`, `?T1: Add<i32>` (overload), `Add::Output(?T1, i32) = ?T2` → soluzione tipica `?T1 = i32`, `?T2 = i32`|
|Method receiver inference|Inferisce la struttura del receiver|`x.push(3)`|`x: ?T1` → `?T1 = Vec<?T2>` (method lookup) → `?T2 = i32` (argomento) → `?T1 = Vec<i32>`|
|Reference inference|Inferisce il tipo di un borrow|`let r = &x;` (con `x: i32`)|`r: &'?R i32`, con `'?R` region fresca; `region(x) ⊇ '?R`|
|Lifetime inference|Inferisce l'estensione di una region|`let r = &x; println!("{}", r);`|`borrow_point ∈ '?R`, `use_point ∈ '?R`|
|Reborrow inference|Restringe i borrow annidati|`let y = &*x;` (con `x: &'a mut i32`)|`y: &'?R i32`, `'?R ⊆ 'a` (il reborrow non può sopravvivere al borrow originale)|
|Trait obligation inference|Inferisce i trait richiesti|`x.clone()`|`x: ?T1`, `?T1: Clone`|
|Associated type inference|Risolve le projection|`Iterator::Item` (con `?T1: Iterator`)|`<?T1 as Iterator>::Item = ?T2`|
|Branch unification|Unifica il tipo dei rami di match|`let y = if cond {3} else {4};`|`arm1_type = ?T`, `arm2_type = ?T`|
|Array inference|Inferisce tipi/lunghezze degli elementi|`let a = [1,2,3];`|`a: [i32; 3]`, tutti gli elementi dello stesso tipo, lunghezza fissa|
|HRTB inference|Inferisce lifetime higher-ranked|`for<'a> fn(&'a i32)`|variabili di region legate, universi, region placeholder — `∀'a . valid(fn(&'a i32))`|
|Subtyping/outlives inference|Inferisce il contenimento delle lifetime|`let x: &'static i32 = y;`|`y: &'?R i32`, `'?R: 'static`|

### 19.5 Tabella dei tipi di vincolo generati

|Tipo di vincolo|Significato|
|---|---|
|Equality|`?T = i32`|
|Subtyping|`'a : 'b`|
|Trait obligations|`?T : Clone`|
|Projection equality|`<T as Trait>::Assoc = U`|
|Region containment|`'?R ⊆ 'a`|
|Const equality|`?N = 4`|

### 19.6 Quali sono gli algoritmi di inferenza citati (oltre HM standard)?

- **Algoritmo W**: il più usato, ma non l'unico. È adatto a linguaggi puri, dove gli effetti collaterali sono limitati alla creazione di nuove variabili;
- **Algoritmo J**: usa più effetti collaterali, più efficiente;
- **Lazy unification**: raccoglie tutti i vincoli visitando l'AST, e applica l'unificazione solo alla fine.

### 19.7 Che cos'è la first-order unification, formalmente?

Dato un insieme finito `G = { s1 ≐ t1, ..., sn ≐ tn }` di potenziali equazioni, l'algoritmo applica regole per trasformarlo in una **sostituzione**, cioè un insieme equivalente di equazioni della forma `{ x1 ≐ u1, ..., xm ≐ um }` dove `x1, ..., xm` sono variabili distinte e `u1, ..., um` sono termini che non contengono nessuna delle `xi`. Se non esiste soluzione, l'algoritmo termina con `⊥`. `G{x ↦ t}` denota l'operazione di sostituire tutte le occorrenze della variabile `x` nel problema `G` con il termine `t`. I simboli costanti sono considerati simboli di funzione con arità zero.

### 19.8 Che cos'è l'algoritmo di Martelli–Montanari (1976–82)?

Calcola il **most general unifier** (mgu), cioè una sostituzione `S` tale che `S(s_i) = S(t_i)` per ogni `s_i ≐ t_i` in `G`. Se non esiste soluzione, l'algoritmo termina con `⊥`. (È lo stesso principio alla base della risoluzione dei vincoli `?T = i32` incontrati nel type inference: HM riduce l'inferenza a un problema di unificazione del primo ordine su termini di tipo.)

---

# 20. uHaskell: type inference con Hindley-Milner passo-passo

### 20.1 Che cos'è uHaskell?

Un sottoinsieme di Haskell usato per spiegare il type inference. Sia Haskell che ML hanno overloading, ma nella trattazione base l'overloading viene ignorato:

```text
<decl> ::= <name> <pat> = <exp>
<pat>  ::= Id | (<pat>, <pat>) | <pat> : <pat> | []
<exp>  ::= Int | Bool | [] | Id | (<exp>)
         | <exp> <op> <exp>
         | <exp> <exp> | (<exp>, <exp>)
         | if <exp> then <exp> else <exp>
```

### 20.2 Idea di base: come si inferisce il tipo di `f x = 2 + x`?

`+` ha tipo `Int → Int → Int` (con overloading sarebbe `Num a => a → a → a`); `2` ha tipo `Int`. Poiché applichiamo `+` a `x`, serve `x :: Int`. Quindi `f x = 2 + x` ha tipo `Int → Int`.

### 20.3 Quali sono i passi dell'algoritmo di type inference?

1. Parsing del programma per costruire il parse tree;
2. assegnazione di variabili di tipo ai nodi dell'albero;
3. generazione dei vincoli:
    - dall'ambiente: costanti (`2`), operatori built-in (`+`), funzioni note (`tail`);
    - dalla forma del parse tree: es. nodi di applicazione e astrazione;
4. risoluzione dei vincoli tramite **unificazione**;
5. determinazione dei tipi delle dichiarazioni top-level.

### 20.4 Esempio completo: `f x = 2 + x`

**Passo 1 — Parse**: si costruisce il parse tree; nodi binari `@` rappresentano l'applicazione, un nodo ternario `Fun` rappresenta la definizione di funzione; gli operatori infissi sono convertiti in applicazione di funzione curried durante il parsing: `2 + x` → `(+) 2 x`.

**Passo 2 — Assegna variabili di tipo**: alle variabili viene assegnato lo stesso tipo della loro occorrenza di binding.

**Passo 3 — Genera vincoli**. Dai nodi di applicazione (`f x`): il tipo di `f` (`t_0`) deve essere dominio → codominio; il dominio è il tipo dell'argomento `x` (`t_1`); il codominio è il risultato dell'applicazione (`t_2`); vincolo: `t_0 = t_1 -> t_2`. Dai nodi di astrazione/dichiarazione (`f x = e`): il tipo di `f` (`t_0`) deve essere dominio → codominio; il dominio è il tipo della variabile astratta `x` (`t_1`); il codominio è il tipo del corpo `e` (`t_2`); vincolo: `t_0 = t_1 -> t_2`.

Per `f x = 2 + x`, l'insieme completo di vincoli generati è:

```text
t_0 = t_1 -> t_6
t_4 = t_1 -> t_6
t_2 = t_3 -> t_4
t_2 = Int -> Int -> Int
t_3 = Int
```

**Passo 4 — Risolvi i vincoli** (unificazione progressiva):

```text
t_2 = t_3 -> t_4  e  t_2 = Int -> Int -> Int, t_3 = Int
⟹ t_3 -> t_4 = Int -> (Int -> Int)  ⟹  t_4 = Int -> Int

t_4 = t_1 -> t_6  e  t_4 = Int -> Int
⟹ t_1 -> t_6 = Int -> Int  ⟹  t_1 = Int,  t_6 = Int

t_0 = t_1 -> t_6  ⟹  t_0 = Int -> Int
```

**Passo 5 — Tipo della dichiarazione**:

```text
f x = 2 + x
> f :: Int -> Int
```

### 20.5 Esempio completo: inferenza di un tipo polimorfo — `f g = g 2`

**Passi 1–2**: si costruisce il parse tree e si assegnano le variabili di tipo.

**Passo 3 — Genera vincoli**:

```text
t_0 = t_1 -> t_4
t_1 = t_3 -> t_4
t_3 = Int
```

**Passo 4 — Risolvi**:

```text
t_1 = t_3 -> t_4 = Int -> t_4
t_0 = t_1 -> t_4 = (Int -> t_4) -> t_4
```

**Passo 5 — Tipo finale**: le variabili di tipo non vincolate diventano **tipi polimorfi**:

```text
f g = g 2
> f :: (Int -> t_4) -> t_4
```

### 20.6 Come si usano funzioni polimorfe come `f g = g 2`?

```text
add x = 2 + x
> add :: Int -> Int
f add
> 4 :: Int

isEven x = mod (x, 2) == 0
> isEven :: Int -> Bool
f isEven
> True :: Bool
```

`f` può essere applicata a qualunque funzione `g :: Int -> t_4`, istanziando `t_4` in modo diverso a ogni chiamata: è questo il senso del polimorfismo parametrico ottenuto tramite generalizzazione delle variabili di tipo non vincolate.

### 20.7 Come si gestiscono tipi di dato e funzioni con più clausole (es. ricorsione su liste)?

Le funzioni possono avere più clausole. Nel type inference: si inferisce un tipo separato per ciascuna clausola; si combinano aggiungendo il vincolo che tutte le clausole abbiano lo stesso tipo; per le chiamate ricorsive, la funzione ha lo stesso tipo della propria definizione.

```rust
length [] = 0
length (x:rest) = 1 + (length rest)
```

**Passo 1 — Parse tree** per la clausola `length (x:rest) = 1 + (length rest)`.

**Passo 2 — Assegna variabili di tipo.**

**Passo 3 — Genera vincoli**:

```text
t_0 = t_3 -> t_10
t_3 = t_2
t_3 = [t_1]
t_6 = t_9 -> t_10
t_4 = t_5 -> t_6
t_4 = Int -> Int -> Int
t_5 = Int
t_0 = t_2 -> t_9
```

**Passo 4 — Risolvi**: combinando `t_3 = [t_1]` con `t_3 = t_2` e `t_0 = t_2 -> t_9` insieme al resto della catena di vincoli, si arriva a:

```text
t_0 = [t_1] -> Int
```

ossia (combinando con la clausola base `length [] = 0`, che vincola il tipo di ritorno a `Int` e il dominio a una lista generica) il tipo finale:

```text
length :: [t_1] -> Int
```

coerentemente con l'idea che `length` accetta una lista di un tipo qualunque e restituisce un intero.

---

# 21. Altri argomenti: fondazioni formali, Polonius, bug reali

### 21.1 Che cos'è RustBelt?

Un lavoro (POPL 2018) che fornisce la **prima prova formale (machine-checked) di safety** per un linguaggio che rappresenta un sottoinsieme realistico di Rust. Motivazione: nessuna delle garanzie di sicurezza di Rust era stata formalmente dimostrata, e c'è ragione di dubitare che valgano sempre, perché Rust impiega un sistema di tipi ownership-based forte ma poi ne estende il potere espressivo tramite librerie che usano internamente feature `unsafe`. La prova è **estensibile**: per ogni nuova libreria Rust che usa feature `unsafe`, si può dire quale condizione di verifica deve soddisfare per essere considerata un'estensione sicura del linguaggio. Gli autori hanno svolto questa verifica per alcune delle librerie più importanti usate nell'ecosistema Rust. (Riferimento: RustBelt, POPL18, https://plv.mpi-sws.org/rustbelt/popl18/)

### 21.2 Che cos'è Polonius?

Una formulazione **alias-based** del borrow checker, estensione conservativa del borrow checker NLL. Lo spostamento principale in questo nuovo approccio è che, per un tipo come `&'a i32`, il significato di `'a` cambia:

- nel sistema descritto dall'RFC NLL, `'a` — chiamata **lifetime** — corrispondeva in ultima analisi a una porzione del programma sorgente o del control-flow graph;
- in questa proposta, `'a` — chiamata **region** — corrisponde invece a un **insieme di loan** (prestiti), cioè un insieme di espressioni di borrow, come `&x` o `&mut v`. L'idea è che se un riferimento `r` ha tipo `&'a i32`, invalidare i termini di uno qualunque dei loan in `'a` invaliderebbe `r`.

(Riferimento: "An alias-based formulation of the borrow checker", https://smallcultfollowing.com/babysteps/blog/2018/04/27/)

### 21.3 Che cosa dice lo studio empirico sui bug di rustc?

"An Empirical Study of Rust-Specific Bugs in the rustc Compiler" (J. ACM, Vol. 37, No. 4, Agosto 2025) studia bug di `rustc` dovuti a feature specifiche di Rust — trait solving, borrow checking, ottimizzazioni specifiche — basandosi su issue e fix riportati fra il 2022 e il 2024, con revisione manuale di 301 issue valide. Risultati principali:

1. i bug di `rustc` nascono principalmente dal sistema di tipi e dal modello delle lifetime di Rust, con errori frequenti nei moduli HIR e MIR dovuti alla complessità dei checker e delle ottimizzazioni;
2. i test case che rivelano bug spesso coinvolgono feature instabili, usi avanzati dei trait, annotazioni di lifetime, API standard e specifici livelli di ottimizzazione;
3. sia programmi validi sia invalidi possono innescare bug, ma gli strumenti di testing esistenti faticano a rilevare errori "non-crash" (senza panic/crash immediato), sottolineando la necessità di ulteriori progressi nel testing di `rustc`.

---

# 22. Domande di collegamento (sintesi)

### 22.1 Perché il MIR è centrale nella compilazione di Rust?

Perché costituisce il punto in cui molte proprietà fondamentali diventano esplicite:

```text
ownership → move analysis → initialization → borrowing → regions
   → borrow checking → optimization → monomorphization → code generation
```

Il MIR è quindi il punto di incontro fra analisi semantiche e generazione del codice.

### 22.2 Qual è la relazione fra move analysis e region inference?

Entrambe sono analisi di dataflow/punto fisso, forward, su reticoli powerset. La move analysis lavora sui **move path** (con transfer GEN/KILL, può rimuovere informazione); la region inference lavora sugli **elementi di region** (con transfer di sola unione via vincoli, può solo aggiungere informazione). Entrambe propagano informazione attraverso una struttura di controllo/dipendenza — CFG per la move analysis, DAG delle SCC per la region inference — fino al raggiungimento di un punto fisso. Interagiscono quando un move rende una place non inizializzata mentre una region ne richiede ancora la validità.

### 22.3 Qual è la relazione fra borrow checking e code generation?

Il borrow checker deve terminare con successo prima che il compilatore consideri il programma valido. Solo dopo il borrow checking il compilatore procede con: cleanup del MIR → ottimizzazione → monomorphization → generazione di codice. Le ottimizzazioni successive lavorano quindi su un programma già verificato rispetto alle proprietà di ownership e borrowing.

### 22.4 Perché la monomorphization viene fatta dopo le ottimizzazioni MIR?

Perché ottimizzare il MIR generico permette di riusare il risultato per più istanze concrete, riducendo lavoro duplicato e sfruttando il fatto che il MIR è ancora parametrico.

### 22.5 Qual è il rapporto fra closure capture inference e borrow checker?

La closure capture inference determina **come** una closure usa le variabili esterne (read → `&T`, mutate → `&mut T`, consume → move). Queste informazioni diventano poi parte della rappresentazione (il campo della struct-closure e il suo tipo di borrow) che il compilatore deve rispettare durante le successive analisi di ownership e borrowing, incluse le regole dei two-phase borrow quando la cattura avviene in contesti di chiamata a metodo.

---

# 23. Le 25 domande più importanti da sapere perfettamente

1. Che cos'è il MIR e perché è necessario?
2. Qual è la pipeline AST → HIR → THIR → MIR (con l'esempio del `let z = if ...` )?
3. Che cosa sono Place, Rvalue, Operand, Local, `RETURN_PLACE`, basic block, terminator?
4. Qual è la pipeline delle query MIR (`mir_built` → `mir_const` → `mir_promoted` → `mir_drops_elaborated_and_const_checked` → `optimized_mir`)?
5. Che cos'è la drop elaboration e a cosa servono i drop flag?
6. Quali sono i quattro tipi di Drop (Static, Dead, Conditional, Open)?
7. Perché il MIR type check è necessario anche dopo il THIR, e perché va dopo la move analysis?
8. Come funziona `mir_borrowck` e quali sono le sue 7-8 fasi?
9. Che cos'è la move analysis come dataflow (GEN/KILL, equazioni)?
10. Che cosa sono i move path e come gestiscono i partial move?
11. Che cosa sono lifetime e region, e qual è la loro relazione?
12. Che cosa significa NLL, con un esempio accettato e uno rifiutato?
13. Come funziona la region inference (le 4 fasi, propagazione `'a ← 'a ∪ 'b ∪ {end('b)}`)?
14. Che cosa sono i vincoli di liveness, outlives e member?
15. Perché servono le SCC e il DAG nella region inference?
16. Che cosa sono i type test e perché vengono verificati separatamente dal solver?
17. Che cos'è il controllo "too big" sulle universal region?
18. Che cosa sono i two-phase borrow (reservation/activation) e perché servono?
19. Come funziona la closure capture inference (`ExprUseVisitor`, `Delegate`, `InferBorrowKind`)?
20. Qual è la differenza fra `Fn`, `FnMut` e `FnOnce`?
21. Che cos'è `optimized_mir` e come funzionano i `MirPass`?
22. Che cos'è la monomorphization, e come si confronta con Haskell/Java/C++/C#?
23. Che cos'è la mono item collection (lazy vs eager, mentioned items)?
24. Che cosa sono le Codegen Unit e qual è il loro trade-off?
25. Come funziona il type inference di Rust (Hindley-Milner, Algorithm W, unificazione di Martelli-Montanari) — sapere rifare a mano l'esempio uHaskell `f x = 2 + x`.

---

# 24. Mappa mentale finale

```text
                         RUST SOURCE
                              │
                              ▼
                         AST → HIR
                    (macro expansion,
                     name resolution,
                     early desugaring)
                              │
                              ▼
                             THIR
                    (late desugaring:
                     autoref/deref,
                     operatori, chiamate
                     overloaded)
                   ┌──────────┴──────────┐
                   │                     │
             type checking        closure capture inference
                   │                     │
                   └──────────┬──────────┘
                              ▼
                        MIR (Built)
             ┌────────────────┼─────────────────┐
             │                │                 │
             ▼                ▼                 ▼
        Move Analysis    Region Inference    Borrow set /
       (move paths,       (liveness, outlives, borrows in scope
        GEN/KILL,          member constraints;
        forward dataflow)  SCC → DAG;
             │             propagate_constraints;
             │             type tests; "too big" check)
             │                │                 │
             └────────────────┼─────────────────┘
                              ▼
                    MIR Type Check (2°)
                              │
                              ▼
                       Borrow Checking
                        (mir_borrowck)
                              │
                              ▼
                     Drop Elaboration
               (drop obligations, drop flags,
                Static/Dead/Conditional/Open)
                              │
                              ▼
                MIR Runtime + MIR Optimization
                   (optimized_mir, MirPass:
                    CleanupPostBorrowck, ConstProp, ...)
                              │
                              ▼
                Mono Item Collection
          (graph roots, lazy/eager, mentioned items)
                              │
                              ▼
                     Monomorphization
                              │
                              ▼
              Codegen Units (partitioning,
                inlining vs incremental trade-off)
                              │
                              ▼
                Lowering → Codegen IR
                    ┌─────────┼─────────┐
                    │         │         │
                  LLVM    Cranelift    GCC
                    │
                    ▼
              Machine Code + Linking
                    │
                    ▼
                 Executable
```

## Concetto chiave da ricordare

> Rust parte da una rappresentazione sintattica (AST), passa progressivamente a rappresentazioni sempre più semantiche (HIR, poi THIR completamente tipato), arriva al MIR — un CFG tipato ed esplicito — per rendere espliciti controllo di flusso, temporanei, move, borrow, drop e lifetime. Su questo MIR il borrow checker esegue due analisi dataflow intrecciate al punto fisso (move/initialization analysis e region inference NLL, quest'ultima risolta su un DAG di componenti fortemente connesse), verificate da un secondo type check MIR e da type test posticipati. Solo dopo aver validato il programma, il compilatore elabora i drop dinamici, ottimizza il MIR ancora generico, lo monomorfizza per ogni istanziazione concreta, lo partiziona in codegen unit e lo abbassa infine a una IR di backend (tipicamente LLVM) per produrre codice macchina.