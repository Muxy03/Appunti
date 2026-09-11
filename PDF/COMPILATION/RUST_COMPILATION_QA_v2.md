# Rust Compilation — Domande e Risposte (v2, ampliata e verificata su COMP01–COMP06RUST_COMPILATION.pdf)

> Nota di revisione: questa versione integra e verifica la precedente stesura contro le sei dispense ufficiali del corso (COMP01–COMP06). Sono state corrette imprecisioni, aggiunti riferimenti puntuali alle slide, e completate intere sezioni assenti nella prima stesura: backend e codegen (Cranelift/GCC), ottimizzazioni MIR, monomorfizzazione e Codegen Units, two-phase borrows con traccia completa, closure capture inference con Delegate/ExprUseVisitor, Strongly Connected Components nel grafo delle outlives constraints, type tests, lints e Clippy, il sistema dei tipi di Rust, il type checking, il type inference (con Hindley-Milner, Algorithm W, unificazione di Martelli-Montanari) e gli esempi completi di inferenza in uHaskell. Ogni risposta è ricondotta al file e, dove utile, allo slide di provenienza.

---

# PARTE I — COMP01: Introduzione, Ownership/Borrowing, Perché servono più IR

## 1. Perché Rust è interessante dal punto di vista della compilazione?

Rust è interessante perché ownership e borrowing **non sono meccanismi runtime**, ma concetti statici che devono essere imposti dal compilatore (COMP01, slide 2). Il compilatore rustc genera codice tramite il framework **LLVM**, ma le analisi tipiche su LLVM IR non bastano: LLVM IR è **troppo basso livello** per esprimere ownership e borrowing. Per questo rustc introduce IR aggiuntive — **HIR, THIR, MIR** — prima di arrivare a LLVM IR (COMP01, slide 2).

Un'osservazione più ampia (COMP01, slide 17): rustc è interessante anche perché argomenti "classici" della teoria dei compilatori — CFG, liveness, dataflow, constraint, punti fissi — non compaiono solo in fasi di ottimizzazione opzionali, ma **sono parte della semantica stessa del linguaggio** (cioè servono a decidere se un programma è legale, non solo a ottimizzarlo). Inoltre rustc adotta scelte implementative non convenzionali, come il sistema delle **query**.

---

## 2. Cenni storici su Rust e rustc

* Sviluppo iniziato nel 2006 da **Graydon Hoare** presso Mozilla.
* Nel 2010 il compilatore, inizialmente scritto in OCaml, viene riscritto per diventare **self-hosting**: rustc scritto in Rust. Nel 2011 rustc riesce a compilare se stesso.
* Il **bootstrapping** viene usato per generare nuove versioni del compilatore.
* rustc utilizza **LLVM** come backend (COMP01, slide 3).

---

## 3. Quali sono gli obiettivi e le caratteristiche principali di Rust?

Rust è un linguaggio general-purpose per system programming, focalizzato sulla **safety**, in particolare sulla **safe concurrency**, e supporta sia il paradigma funzionale sia quello imperativo (COMP01, slide 4). L'obiettivo principale è garantire sicurezza **senza penalizzare l'efficienza**.

Caratteristiche sintattiche (slide 4):
* sintassi concreta simile a C/C++ (blocchi, `if-else`, `while`, `for`), con `match` per il pattern matching;
* quasi ogni parte del corpo di una funzione è un'espressione (incluso `if-else`);
* nessun runtime richiesto (niente GC, niente typing/binding dinamico);
* maggiore controllo su allocazione/distruzione della memoria.

Dal punto di vista delle garanzie (COMP01, slide 5), Rust offre:
* **prestazioni** paragonabili a C (compilazione a codice oggetto "bare-metal");
* **memory safety**: niente puntatori null, niente dangling pointer, niente double free, niente data race, niente iterator invalidation, niente accessi fuori dai limiti degli array (proprietà che arriverà in C++26);
* **basso overhead**: le regole di memory safety sono verificate perlopiù **staticamente**, con **zero-cost abstraction** nella gestione della memoria (nessun garbage collector);
* il tutto ottenuto tramite un sistema di tipi avanzato e i concetti di ownership, borrowing e lifetime, basati su **RAII**.

Il prezzo da pagare è un **costo cognitivo** maggiore per il programmatore, che deve ragionare più esplicitamente sulle regole d'uso di memoria e riferimenti.

---

## 4. Che cos'è RAII?

**RAII (Resource Acquisition Is Initialization)** è l'idioma per cui l'allocazione di una risorsa avviene durante l'inizializzazione dell'oggetto (dal costruttore), mentre il rilascio avviene durante la distruzione dell'oggetto (dal distruttore) (COMP01, slide 6).

* Popolare nel C++ moderno: piccoli oggetti sullo stack, risorse grandi sull'heap ma possedute da un oggetto sullo stack, che le rilascia nel proprio distruttore.
* L'oggetto è legato allo **scope** (funzione, blocco) in cui è dichiarato; quando lo scope si chiude, l'oggetto viene distrutto insieme a ogni risorsa posseduta.
* Ogni risorsa ha un **unico proprietario**.

---

## 5. Che cos'è il sistema di ownership di Rust?

Rust ha un sistema di ownership che supporta RAII in modo rigoroso, basato sui concetti di **ownership** e **borrowing** (COMP01, slide 7). Le tre regole formali (numerazione ufficiale delle slide):

* **[O1]** Ogni valore è posseduto da una variabile, identificata da un nome o un *path*;
* **[O2]** Ogni valore ha al massimo un *owner* alla volta;
* **[O3]** Quando l'owner esce dallo scope, il valore viene recuperato/distrutto/"droppato".

---

## 6. Come funziona la move semantics dell'assegnamento?

Per default, un assegnamento fra variabili ha **semantica di move**: la ownership passa dal membro destro a quello sinistro, per rispettare [O2] (COMP01, slide 8):

```rust
fn main() {
    let x = Box::new(3);
    let _y = x; // underscore per evitare warning 'unused'
    println!("x = {}", x); // errore!
}
```

Per i tipi che implementano il trait **`Copy`** (tipi primitivi e altri), l'assegnamento ha invece **semantica di copia**: [O2] resta soddisfatta perché viene creato un nuovo valore:

```rust
fn main() {
    let x = 3;
    let _y = x;
    println!("x = {:?}", x); // OK
}
```

Da notare (slide 8) che anche `Option<T>` con `T: Copy` (es. `Option::Some(3)`) segue la semantica di copia se implementa `Copy`.

---

## 7. Come funziona la move semantics nel passaggio di parametri e nel return?

Vale lo stesso principio dell'assegnamento: qualunque valore passato a una funzione viene recuperato/distrutto quando la funzione ritorna, poiché il parametro formale esce di scope. Solo il valore di ritorno può "sopravvivere" (COMP01, slide 9):

```rust
fn foo<T>(z: T) -> T { // funzione identità polimorfa
    z
}

fn main(){
    let x = Box::new(3);
    let _y = foo(x);
    println!("x == {}", x); // errore
}
```

Se si riassegna il risultato alla stessa variabile, il codice torna valido:

```rust
fn main(){
    let mut x = Box::new(3);
    x = foo(x);
    println!("x == {}", x); // OK
}
```

E se `T` implementa `Copy` (es. `i32`), non c'è move e tutto compila normalmente.

---

## 8. Perché esiste il borrowing?

Le regole di ownership pura sarebbero troppo restrittive. Una risorsa può essere **presa in prestito** dal suo proprietario, tramite assegnamento o passaggio di parametro, senza trasferirne la ownership (COMP01, slide 10). Per garantire la memory safety, le regole di borrowing assicurano che **ALIASING e MUTABILITÀ non possano coesistere**.

I valori possono essere passati:
* per riferimento immutabile: `x = &y`;
* per riferimento mutabile: `x = &mut y`;
* per valore: `x = y`.

---

## 9. Quali sono le regole formali del borrowing?

(COMP01, slide 11, numerazione ufficiale)

* **[B1]** Al massimo un riferimento mutabile a una risorsa può esistere in un dato momento;
* **[B2]** Se esiste un riferimento mutabile, non possono esistere riferimenti immutabili;
* **[B3]** Se non esiste un riferimento mutabile, possono coesistere più riferimenti immutabili alla stessa risorsa;
* **[B4]** Il proprietario non può liberare o mutare la propria risorsa mentre è presa in prestito immutabilmente;
* **[B5]** Il proprietario non può nemmeno leggere la propria risorsa mentre è presa in prestito mutabilmente.

Esempi (slide 12):

```rust
let mut s = String::from("example");
let r1 = &mut s;
let r2 = &mut s;
println!("{} {}", r1, r2); // non compila per B1

let mut s = String::from("example");
let r1 = &s;
let r2 = &mut s;
println!("{} {}", r1, r2); // non compila per B2

let s = String::from("example");
let r1 = &s;
let r2 = &s;
println!("{} {}", r1, r2); // OK per B3
```

---

## 10. Che cos'è una lifetime?

Una **lifetime** è il costrutto che il borrow checker utilizza per garantire la validità delle regole precedenti (COMP01, slide 13).

* Le lifetime sono associate a ogni singola operazione di ownership e borrowing.
* Una lifetime inizia quando comincia la ownership, e termina quando il valore viene mosso o distrutto.
* Per i borrow, termina nel punto in cui il valore preso in prestito viene usato per l'ultima volta.
* Le lifetime sono per lo più **inferite**; solo a volte devono essere rese esplicite, con la stessa sintassi dei generics.
* Usando le lifetime, il compilatore verifica la validità delle regole di ownership e borrowing: in particolare garantisce che (il proprietario di) ogni variabile/riferimento preso in prestito abbia una lifetime più lunga di chi la prende in prestito (regole [B4],[B5]).

---

# PARTE II — Perché servono più IR (HIR, THIR, MIR)

## 11. Come è organizzato tradizionalmente un compilatore come LLVM, e perché questo non basta a Rust?

Nell'architettura LLVM, l'analisi statica (es. type checking) avviene tipicamente nel front-end sull'**Abstract Syntax Tree**, mentre le analisi dataflow e le ottimizzazioni avvengono sulla **LLVM IR**, tipicamente su un **Control Flow Graph** (COMP01, slide 14).

Il problema è che la LLVM IR è **troppo low-level per il borrow checker di Rust** (COMP01, slide 15). Il borrow checking non è semplicemente "alias analysis su codice simil-macchina": è un'analisi di sicurezza **language-level e flow-sensitive** su concetti quali:

* *places* e *projections* (`x`, `x.0`, `*p`, `v[i]`);
* moves e *partial moves*;
* borrow condivisi vs mutabili;
* vincoli di regione/lifetime;
* semantica dei drop;
* controllo di flusso desugarizzato ma ancora tipato secondo la semantica Rust.

Esempio guida usato nelle slide per motivare l'esigenza di un IR intermedio:

```rust
fn push_len(v: &mut Vec<i32>) {
    v.push(v.len() as i32);
}
```

Per questo rustc introduce altre IR prima di generare la LLVM IR (slide 15).

---

## 12. Che cos'è il sistema delle Query in rustc?

Le **query** sono l'astrazione centrale con cui rustc è strutturato come sistema **demand-driven** (COMP01, slide 18):

* rustc non è eseguito come una sequenza fissa di passate: ogni informazione (il tipo di una funzione, il suo MIR, il risultato del suo borrow-checking, ecc.) è calcolata da una query che può dipendere da altre query.
* Quando il compilatore necessita di un'informazione, invoca la query corrispondente, che ricorsivamente garantisce che tutte le sue dipendenze siano calcolate.
* Le query abilitano la **compilazione incrementale e cacheable**: i risultati sono *memoized*, quindi se la stessa informazione viene richiesta di nuovo può essere riusata senza ricalcolo.
* Quando il codice sorgente cambia, solo le query i cui input sono cambiati — e quelle che dipendono da esse — devono essere ricalcolate.
* Questo rende la compilazione più efficiente e scalabile per progetti grandi, offrendo anche una struttura modulare pulita per l'implementazione del compilatore.

---

## 13. Qual è la pipeline generale del front-end e middle-end di rustc?

**Front-end** (COMP01, slide 19):
* un lexer di basso livello (sorgente → token): `rustc-lexer`;
* un lexer di livello più alto invocato dal parser;
* un **recursive descent parser** (`rustc-parse`) che genera l'**AST**.

**Da front-end a middle-end** (slide 20):
* dopo macro expansion e name resolution, rustc abbassa (*lowers*) il programma in **HIR**, un albero sintattico più regolare, usato da molte analisi front-end;
* vengono poi aggiunte informazioni tipate a livello di corpo (*body-level*), ottenendo il **THIR**.

**Middle-end** (slide 21):
* l'AST del THIR viene tradotto nel **CFG del MIR**, dove controllo di flusso, temporanei, places e drop diventano espliciti;
* questa è l'IR su cui viene eseguito il **Borrow Checker**;
* il MIR viene ulteriormente ottimizzato prima dell'abbassamento a LLVM IR;
* il backend consuma un MIR verificato e preparato, crea istanze concrete monomorfizzate, e delega alla LLVM le ottimizzazioni di basso livello.

---

## 14. Perché un solo AST non basta?

(COMP01, slide 22)

* **Troppo sintattico**: un AST rispecchia la sintassi dell'utente — espressioni annidate, zucchero sintattico, forme source-level — oscurando l'ordine di valutazione e gli archi di controllo di flusso.
* **Desugaring ripetuto**: senza un'IR centrale, ogni passata successiva dovrebbe riscoprire o reimplementare gli stessi desugaring e la stessa semantica locale.
* **Ragionamento sul CFG difficile**: il borrow checking necessita di punti fine-grained nel programma e di archi fra di essi; sono scomodi da esprimere direttamente su un AST.
* **Forma eseguibile**: il MIR è più vicino a un modello eseguibile: basic block, statement, terminator, place, operand, temporanei espliciti.

---

## 15. Esempio di traduzione dello statement `let z = if x > 0 { x + 1 } else { 0 };` — vista AST

(COMP01, slide 23)

```rust
// Rust source inside a function
let z = if x > 0 { x + 1 } else { 0 };
```

```text
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

Osservazioni delle slide:
* lo statement lega `z` al valore prodotto da un'espressione `if`;
* l'AST è ad albero e preserva la struttura annidata dell'espressione;
* il risultato del blocco è implicito: l'ultima espressione di ciascun ramo diventa l'inizializzatore;
* le fasi successive devono esporre tipi e controllo di flusso in modo più diretto.

---

## 16. Che cos'è l'HIR e cosa lo distingue dall'AST?

**HIR (High-Level Intermediate Representation)**, COMP01 slide 24:

* **Post-espansione**: l'HIR è costruito dopo parsing, macro expansion e name resolution, quindi molti nomi e forme sintattiche sono già risolti.
* **Ancora leggibile**: resta vicino al programma del programmatore, il che lo rende adatto a controlli e diagnostica front-end.
* **Parte dello zucchero già rimosso**: alcuni costrutti superficiali sono già normalizzati (per esempio parte dello zucchero relativo ai loop è già rappresentata in forme più regolari).
* **Non è l'IR del borrow-check**: l'HIR è utile, ma resta troppo alto livello per il ragionamento puntuale (*pointwise*) richiesto dal borrow checking sul MIR.

---

## 17. Che cos'è il THIR?

**THIR: Typed HIR for Function Bodies** (COMP01, slide 25):

* **IR body-local**: il THIR è prodotto per i corpi delle funzioni ed è intenzionalmente temporaneo; rustc non conserva ogni corpo THIR globalmente per sempre.
* **Completamente tipato**: rende esplicite le decisioni type-dependent, inclusi aggiustamenti come autoref, autoderef, coercions e chiamate overloaded.
* **Ponte per l'abbassamento**: il MIR builder consuma il THIR piuttosto che l'HIR grezzo, perché il THIR espone già decisioni semantiche importanti.
* **Ruolo concettuale**: il THIR è il ponte dove si vede lo spostamento dalla sintassi superficiale verso i fatti operativi necessari alla costruzione del CFG.

---

## 18. Esempio di traduzione HIR → THIR

(COMP01, slide 26)

```text
// let z = if x > 0 { x + 1 } else { 0 };
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

Osservazioni: l'HIR è ancora vicino alla sintassi ma ha già subito un importante abbassamento front-end; si sa che l'inizializzatore e ciascun ramo hanno tipo `i32`, e che la condizione ha tipo `bool`. Il THIR registra gli aggiustamenti e i significati tipati degli operatori prima della costruzione del MIR. Non c'è ancora un CFG, ma i fatti tipati sul corpo sono già espliciti.

---

## 19. Che cos'è il MIR come CFG tipato?

**MIR: Mid-Level IR as a Typed CFG** (COMP01, slide 27):

* **Basic block**: il MIR organizza una funzione in basic block, ciascuno terminato da un **terminator** come `return`, `goto`, `switch`, `call` o `unwind`.
* **Places e operands**: una *place* denota una locazione di memoria (un locale, un campo, una dereference o un accesso indicizzato); gli *operands* sono valori copiati, mossi, o costanti.
* **Return place**: il risultato della funzione è un locale speciale, tipicamente stampato come `_0`; argomenti e temporanei sono stampati come `_1`, `_2`, ecc.
* **Ruolo centrale**: il MIR è usato per l'analisi di sicurezza, le trasformazioni, la preparazione delle ottimizzazioni, la valutazione delle costanti (const evaluation) e la generazione di codice finale.

---

## 20. Quali sono i "dialetti" (fasi) del MIR?

**MIR Dialects and Phases** (COMP01, slide 28):

* **MIR Built**: il MIR iniziale costruito dal THIR, contiene ancora costrutti orientati all'analisi e annotazioni source-level.
* **MIR Analysis**: borrow checking, NLL, move analysis, controlli di inizializzazione e ragionamento dataflow operano su questo MIR "da analisi".
* **MIR Runtime**: dopo il borrowck, cleanup ed elaboration rimuovono gli artefatti necessari alla verifica ma non all'esecuzione runtime.
* **Stessa struttura, nuovo contratto**: le strutture dati MIR sottostanti sono correlate fra le fasi, ma le promesse semantiche attese da ciascuno stadio del compilatore cambiano.

---

## 21. Esempio completo: traduzione MIR di `let z = if x > 0 { x + 1 } else { 0 };`

(COMP01, slide 29)

```text
//MIR-like of: let z = if x > 0 { x + 1 } else { 0 };
let mut _z: i32;
let mut _t0: bool;
let mut _t1: i32;

bb0: { _t0 = Gt(copy _x, const 0_i32);
       switchInt(copy _t0) -> [0: bb2, otherwise: bb1]; }
bb1: { _t1 = Add(copy _x, const 1_i32);
       _z = move _t1;
       goto -> bb3; }
bb2: { _z = const 0_i32; goto -> bb3; }
bb3: { /* z initialized here */ }
```

Osservazioni: la singola espressione diventa un esplicito grafo di controllo "a diamante"; la condizione e il calcolo dei rami sono memorizzati in temporanei con nome; ciascun ramo scrive nella stessa place di destinazione, così l'inizializzazione può essere verificata in modo path-sensitive. Questa forma è adatta a liveness, definite assignment, borrow checking e lowering.

# PARTE III — COMP02: Come si ottengono le IR, Desugaring, MIR interno

## 22. Come si possono ispezionare le varie IR di rustc?

(COMP02, slide 4)

* **HIR dump**: `cargo rustc -- -Z unpretty=hir-tree` mostra l'albero high-level; il flag `-Z` richiede un compilatore *nightly*.
* **THIR dump**: `cargo rustc -- -Z unpretty=thir-tree` espone l'abbassamento tipato del corpo e gli aggiustamenti prima della costruzione del MIR.
* **MIR dump**: `rustc -Z dump-mir=all` emette il MIR in vari stadi, utile per osservare costruzione, analisi e cleanup.
* **Artefatti di backend**: `rustc --emit=mir` e `rustc --emit=llvm-ir` producono artefatti confrontabili per vedere cosa scompare prima di LLVM.

---

## 23. Cosa sopravvive nel passaggio da MIR a LLVM IR, e cosa no?

(COMP02, slide 5)

* **Sopravvive**: controllo di flusso, chiamate, load, store, operazioni aritmetiche, layout, e funzioni concrete monomorfizzate sopravvivono in forme orientate al backend.
* **Non sopravvive direttamente**: lifetime e ownership non sono valori runtime di prima classe nel codice generato. Servono a **validare** il programma prima dell'abbassamento.
* **Il cleanup conta**: il cleanup post-borrowck rimuove gli artefatti utili solo alla verifica e prepara un dialetto MIR "runtime" adatto a trasformazioni e codegen.
* **Confine con LLVM**: LLVM riceve una IR di livello più basso, dove il ragionamento di sicurezza specifico di Rust ha già giustificato molte assunzioni.

---

## 24. Che cos'è il desugaring, e quando avviene?

Il desugaring è la trasformazione dello **zucchero sintattico** in forme più primitive ed esplicite (COMP02, slide 6). Le varie fasi di abbassamento verso il MIR eseguono diversi tipi di desugaring:

* **Early desugaring** (es. i cicli `for`): avviene durante l'abbassamento a HIR.
* **Late desugaring** (method call, autoderef, autoref, operatori): avviene durante la costruzione del THIR.
* **Costruzione del MIR**: rimuove completamente l'annidamento delle espressioni.

Motivazione (slide 7): Rust contiene molto zucchero sintattico, che nasconde informazioni importanti anche per il borrow checking. Esempi di zucchero elencati nelle slide:

* Method Call Desugaring
* for-loop Desugaring
* Operator Overloading
* operatore `?` → `match` su `Result`/`Option`
* `if let` → `match`
* `while let` → `loop` + `match`
* auto-ref/deref
* Closure → struct + trait (`Fn`, `FnMut`, `FnOnce`)
* Indicizzazione `v[i]` → trait `Index`
* return implicito → tail expression

---

## 25. Tabella completa degli esempi di desugaring (slide 8–9)

| Source | Desugared |
|---|---|
| `for x in v { println!("{}", x); }` | `{ let mut iter = IntoIterator::into_iter(v); loop { match iter.next() { Some(x) => { println!("{}", x); } None => break, } } }` |
| `let x = foo()?;` | `let x = match foo() { Ok(v) => v, Err(e) => return Err(From::from(e)), };` |
| `let x = opt?;` | `let x = match opt { Some(v) => v, None => return None, };` |
| `v.push(10);` | `Vec::push(&mut v, 10);` |
| `x.foo()` | `Foo::foo(&x)` / `Foo::foo(&mut x)` / `Foo::foo(&*x)` (a seconda del receiver) |
| `if let Some(x) = opt { println!("{}", x); }` | `match opt { Some(x) => { println!("{}", x); } _ => {} }` |
| `while let Some(x) = iter.next() { println!("{}", x); }` | `loop { match iter.next() { Some(x) => { println!("{}", x); } None => break, } }` |
| `v[i]` (lettura) | `*std::ops::Index::index(&v, i)` |
| `v[i] = 10;` | `*std::ops::IndexMut::index_mut(&mut v, i) = 10;` |
| `fn f() -> i32 { 3 }` (return implicito) | `fn f() -> i32 { return 3; }` (tail expression) |

Le enum coinvolte (slide 8):

```rust
enum Result<T, E> { Ok(T), Err(E) }
enum Option<T> { None, Some(T) }
```

La sintassi metodo è solo zucchero: il compilatore inserisce implicitamente `&`, `&mut`, deref (`*`) e la risoluzione del trait.

---

## 26. Come vengono desugarate le closure? Perché il risultato non è Rust legale?

(COMP02, slide 10)

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
let f = |x| x + y; // variable capturing
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

Nota importante delle slide: questo è **desugaring interno di rustc**. La sintassi risultante non è codice Rust legale (per esempio `extern "rust-call"` e l'implementazione anonima non sono scrivibili direttamente dall'utente): l'inferenza della cattura e la selezione del trait non sono esprimibili direttamente da codice scritto dall'utente.

---

## 27. Quali benefici ha portato l'introduzione del MIR (aprile 2016)?

(COMP02, slide 11): **compilazione più veloce**, **esecuzione più veloce**, **borrow checking più preciso** (grazie alle Non-Lexical Lifetimes, NLL).

---

## 28. Quali sono le caratteristiche chiave del MIR?

(COMP02, slide 12)

* È basato su un **control-flow graph**.
* Non ha espressioni annidate.
* Tutti i tipi nel MIR sono completamente espliciti (costruiti a partire dal THIR).
* **Basic block**: unità del CFG, composte da:
  - **statement**: azioni con un solo successore;
  - **terminator**: azioni con potenzialmente più successori; sempre alla fine di un blocco.
* **Locals**: argomenti della funzione, variabili locali e temporanei, come `_1`, `_2`; il local `_0` è il valore di ritorno.
* **Places**: espressioni che identificano una locazione in memoria, come `_1` o `_1.f`.
* **Rvalues**: espressioni che producono un valore.
  - **Operands**: gli argomenti di una rvalue: possono essere una costante (es. `22`) o una place (es. `_1`).

---

## 29. Esempio completo di MIR ottimizzato di una funzione con `Vec`

(COMP02, slide 13)

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

Osservazioni: i locals sono senza nome, `_0` è il valore di ritorno; le annotazioni `debug` collegano un local al nome sorgente (`vec => _1`); il MIR registra se i valori sono copiati o mossi, informazione necessaria al ragionamento sull'ownership; il CFG espone i cammini che le analisi dataflow successive possono attraversare con tecniche standard.

---

## 30. Dove sono definiti i tipi di dato del MIR in rustc?

(COMP02, slide 14) I tipi dati del MIR sono definiti nel modulo `compiler/rustc_middle/src/mir/`:

* Il tipo principale è **`Body`**.
* I **basic block** sono memorizzati nel campo `Body::basic_blocks`, un vettore di strutture `BasicBlockData`. Nessuno referenzia mai direttamente un basic block: si passano valori `BasicBlock`, indici *newtype* in questo vettore.
* Gli **statement** sono rappresentati dal tipo `Statement`.
* I **terminator** sono rappresentati da `Terminator`.
* I **locals** sono rappresentati da un tipo indice *newtype* `Local`. I dati per una variabile locale si trovano nel vettore `Body::local_decls`. Esiste anche una costante speciale **`RETURN_PLACE`** che identifica il "local" speciale che rappresenta il valore di ritorno.
* Le **place** sono identificate dalla struct `Place`, con pochi campi:
  - la variabile locale di base, come `_1`;
  - le **projections**, cose che "proiettano fuori" da una place base, rappresentate dal tipo *newtype* `ProjectionElem`. Per esempio `_1.f` è una projection con `f` elemento di proiezione e `_1` base path; `*_1` è anch'essa una projection, rappresentata con `ProjectionElem::Deref`.
* Le **rvalue** sono rappresentate dall'enum `Rvalue`.
* Gli **operand** sono rappresentati dall'enum `Operand`.

---

## 31. Come si ottiene il MIR di una funzione? Quali query esistono?

(COMP02, slide 15)

* Per una funzione si usa la query **`optimized_mir`** (tipicamente usata dal codegen) o **`mir_for_ctfe`** (tipicamente usata per la compile-time function evaluation, CTFE). Queste restituiscono il MIR finale ottimizzato.
* Per un valore *promosso* si usa la query **`promoted_mir`**.
* Per i def-id esterni (di altre crate), il MIR è ottenuto dai metadati della crate esterna.
* Per i def-id locali, la query costruisce il MIR ottimizzato richiedendo una pipeline di query "upstream", ciascuna contenente una serie di passate.

---

## 32. Qual è la pipeline completa delle query MIR?

(COMP02, slide 16) Per produrre il MIR ottimizzato per un def-id `D`, si passa attraverso diverse suite di passate, ciascuna raggruppata da una query. Ogni suite contiene passate che eseguono linting, analisi, trasformazione o ottimizzazione. Ogni query rappresenta un punto intermedio utile per accedere al dialetto MIR per il type checking o altri scopi:

* **`mir_built(D)`** — fornisce il MIR iniziale appena costruito;
* **`mir_const(D)`** — applica alcune semplici passate di trasformazione per preparare il MIR alla const qualification;
* **`mir_promoted(D)`** — estrae i temporanei promuovibili in corpi MIR separati, e prepara il MIR al borrow checking;
* **`mir_drops_elaborated_and_const_checked(D)`** — esegue il borrow checking, esegue le principali passate di trasformazione (come la drop elaboration), e prepara il MIR all'ottimizzazione;
* **`optimized_mir(D)`** — esegue tutte le ottimizzazioni abilitate e raggiunge lo stato finale.

---

## 33. Che cos'è la MIR promotion?

Un **MIR promosso** è un pezzo di MIR estratto dal corpo di una funzione e sollevato in un corpo MIR separato, simile a una costante, così da poter essere valutato a compile time o trattato come avente lifetime `'static` (COMP02, slide 17).

Durante la costruzione del MIR, il compilatore identifica espressioni pure, costanti e prive di effetti collaterali (es. letterali di array, riferimenti a dati costanti). Invece di tenerle inline nel MIR della funzione, le promuove in un corpo MIR separato (una **costante promossa**), sostituendo l'espressione originale con un riferimento a quel valore promosso.

Esempio (slide 17):

```rust
fn f() -> &'static [i32; 3] {
    &[1, 2, 3]
}
```

```text
Promoted[0]:
    _0 = [1, 2, 3];
    return;

fn f():
    _0 = &'static Promoted[0];
    return;
```

Senza promozione, l'array sarebbe un temporaneo dentro `f`; con la promozione il compilatore lo trasforma come mostrato sopra.

---

## 34. Cosa fa la query `mir_built`?

(COMP02, slide 18) La query `mir_built` causa l'abbassamento dal THIR di:

* corpi di funzioni e closure;
* inizializzatori di item `static` e `const`;
* inizializzatori di discriminanti di enum;

e altre cose. Prima crea:

* variabili locali per ogni argomento;
* variabili locali per ogni binding specificato;
* accessi ai campi che leggono i valori dagli argomenti e li scrivono nella variabile di binding.

Infine, innesca una chiamata ricorsiva a una funzione che genera il MIR per il corpo (un'espressione `Block`) e scrive il risultato nella **`RETURN_PLACE`**.

---

## 35. Che cos'è il MIR Visitor e a cosa serve?

(COMP02, slide 20) Il **MIR visitor** è uno strumento comodo per attraversare il MIR, sia per cercare cose sia per modificarlo; è usato dalle analisi dataflow. rustc supporta il design pattern Visitor con trait adeguati definiti nel modulo `middle::mir::visit`:

* **`Visitor`** (opera su `&Mir` e restituisce riferimenti condivisi);
* **`MutVisitor`** (opera su `&mut Mir` e restituisce riferimenti mutabili).

---

## 36. Come funziona il design pattern Visitor in generale?

(COMP02, slide 21)

* La struttura dati può essere composta da diversi tipi di componenti (*ConcreteElements*).
* Ogni componente implementa un metodo `accept(Visitor)`.
* Il Visitor definisce un metodo di visita per ciascun tipo.
* La logica di navigazione risiede nel Visitor.
* A ogni passo, il metodo di visita corretto è selezionato per overloading.

Uso pratico in rustc (slide 22): per implementare un visitor si crea un tipo che rappresenta il proprio visitor (tipicamente per "aggrappare" lo stato necessario durante l'elaborazione del MIR), e si implementa per esso il trait `Visitor` o `MutVisitor`:

```rust
struct MyVisitor<...> { tcx: TyCtxt<'tcx>, ... }

impl<'tcx> MutVisitor<'tcx> for MyVisitor {
    fn visit_foo(&mut self, ...) {
        ...
        self.super_foo(...);
    }
}
```

Oltre al visitor, il modulo `middle::mir::traversal` contiene funzioni utili per attraversare il CFG del MIR in diversi ordini standard (es. pre-order, reverse post-order, ecc.).

---

## 37. Come è definita un'analisi dataflow in rustc (trait `Analysis`)?

(COMP02, slide 23) La dataflow analysis sul MIR è ampiamente usata da rustc, per esempio per:

* trovare variabili non inizializzate;
* determinare quali variabili sono vive attraverso uno statement `yield` di un generator;
* calcolare quali *Place* sono prese in prestito (borrowed) in un dato punto del CFG.

Un'analisi dataflow è definita dal trait **`Analysis`**. Oltre al tipo dello stato dataflow, questo trait definisce il valore iniziale dello stato all'entrata di ciascun blocco, e la **direzione** dell'analisi, forward o backward. Il **dominio** dell'analisi deve essere un **lattice** (più precisamente un *join-semilattice*) con un operatore di join ben definito (si vedano il modulo `lattice` e il trait `JoinSemiLattice`).

---

## 38. Che cosa sono gli "effect" nel framework dataflow di rustc?

(COMP02, slide 24) Il framework dataflow consente a ogni statement (e terminator) dentro un basic block di definire la propria funzione di trasferimento:

* le funzioni di trasferimento sono chiamate **effect**;
* ogni effect è applicato in sequenza nell'ordine dataflow, e insieme definiscono la funzione di trasferimento per l'intero basic block;
* è possibile definire un effect anche per specifici archi uscenti (*outgoing edges*) di alcuni terminator.

Gli statement possono anche essere dotati di **"Before" Effect**:

* i "before effect" sono applicati immediatamente prima dell'effect "primario" senza prefisso, a prescindere dalla direzione dell'analisi (un'analisi backward applica comunque il "before effect" e poi l'effect primario, come farebbe un'analisi forward);
* utili in scenari come quando l'effetto della parte destra di un assegnamento va considerato separatamente da quello della parte sinistra.

---

## 39. Come si ispezionano i risultati di un'analisi dataflow?

(COMP02, slide 25) Dopo aver costruito un'analisi, si chiama **`iterate_to_fixpoint`**, che restituisce una struttura **`Results`** contenente lo stato dataflow al punto fisso all'entrata di ciascun blocco.

Una volta ottenuto un `Results`:

* se serve lo stato solo in **pochi punti specifici** (es. prima di ogni terminator `Drop`), si usa un **`ResultsCursor`**;
* se serve lo stato **in ogni punto**, un **`ResultsVisitor`** è più efficiente.

Esempio con `ResultsVisitor` (slide 26):
```rust
// Assuming `MyVisitor` implements `ResultsVisitor<FlowState = MyAnalysis::Domain>`...
let mut my_visitor = MyVisitor::new();
// inspect the fixpoint state for every location within every block in RPO.
let results = MyAnalysis::new()
    .iterate_to_fixpoint(tcx, body, None);
results.visit_with(body, &mut my_visitor);
```

Esempio con `ResultsCursor`:
```rust
let mut results = MyAnalysis::new()
    .iterate_to_fixpoint(tcx, body, None)
    .into_results_cursor(body);

// Inspect the fixpoint state immediately before each `Drop` terminator.
for (bb, block) in body.basic_blocks().iter_enumerated() {
    if let TerminatorKind::Drop { .. } = block.terminator().kind {
        results.seek_before_primary_effect(body.terminator_loc(bb));
        let state = results.get();
        println!("state before drop: {:#?}", state);
    }
}
```

Le slide menzionano anche diagrammi **Graphviz** per ispezionare il dataflow (slide 27): ogni visualizzazione mostra lo stato dataflow completo all'entrata e all'uscita di ciascun blocco.

---

## 40. Perché serve la Drop Elaboration? (Dynamic drops)

(COMP02, slide 28) Quando si costruisce il MIR, i terminator `Drop` e `DropAndReplace` rappresentano punti dove *potrebbero* avvenire dei drop; tuttavia, in questa fase, la loro presenza non garantisce che un distruttore verrà effettivamente eseguito.

Esempio guida (slide 28):
```rust
let mut y = vec![];
{
    let x = vec![1, 2, 3];
    if std::process::id() % 2 == 0 {
        y = x; // conditionally move `x` into `y`
    }
} // `x` goes out of scope here. Should it be dropped?
```

Quando una variabile o un temporaneo inizializzato esce di scope, il suo distruttore viene eseguito (viene "droppato"). Anche l'assegnamento esegue il distruttore del proprio operando sinistro, se inizializzato. Se una variabile è stata parzialmente inizializzata, solo i suoi campi inizializzati vengono droppati. **Se una variabile è inizializzata o no si sa solo a runtime.**

---

## 41. Che cosa sono le "drop obligations"?

(COMP02, slide 29)

* Quando una variabile locale diventa inizializzata, stabilisce un insieme di **"drop obligations"**: un insieme di path strutturali (es. il local `a`, o un path a un campo `b.f.y`) che devono essere droppati.
* Le drop obligation per una variabile locale `x` di tipo struct `T` sono calcolate analizzando la struttura di `T`. Se `T` stessa implementa `Drop`, allora `x` è una drop obligation. Se `T` non implementa `Drop`, l'insieme delle drop obligation è l'unione delle drop obligation dei campi di `T`.
* Quando un path strutturale viene mosso (e diventa quindi non inizializzato), ogni drop obligation per quel path o i suoi discendenti (`path.f`, `path.f.g.h`, ecc.) viene rilasciata.
* Quando una variabile locale esce di scope (`Drop`), o quando un path strutturale viene sovrascritto tramite assegnamento (`DropAndReplace`), si controllano eventuali drop obligation per quella variabile o quel path.
* A meno che l'obbligazione non sia già stata rilasciata a questo punto, viene chiamata la relativa implementazione `Drop`. Per i tipi enum, devono essere droppati solo i campi corrispondenti alla **"active variant"**: si controlla prima il discriminante per determinare la variante attiva; tutte le drop obligation delle varianti diverse da quella attiva sono ignorate.

---

## 42. Che cos'è un drop flag, e cos'è la drop elaboration?

(COMP02, slide 30) Un modello valido per queste regole è mantenere un **flag booleano** (un "drop flag") per ogni path strutturale usato in un qualunque punto della funzione:

* il flag è impostato quando il path viene inizializzato, ed è azzerato quando il path viene mosso;
* quando avviene un `Drop`, si controllano i flag per ogni obbligazione associata al target del `Drop`, e si chiama la `Drop` impl associata solo per quelle ancora applicabili.

Questo processo — trasformare il MIR appena costruito, con i suoi terminator `Drop` e `DropAndReplace` imprecisi, in uno con drop flag — è noto come **drop elaboration**:

* quando uno statement MIR causa l'inizializzazione (o la deinizializzazione) di una variabile, la drop elaboration inserisce codice che imposta (o azzera) il drop flag per quella variabile;
* avvolge i terminator `Drop` in condizionali che controllano i drop flag appena inseriti.

Una volta completato questo processo, i terminator `Drop` nel MIR corrispondono a una chiamata alla **"drop glue"** (o "drop shim") per il tipo della place droppata. La drop glue di un tipo chiama la sua implementazione `Drop` (se esiste), e poi richiama ricorsivamente la drop glue di tutti i suoi campi.

---

## 43. Quali ottimizzazioni sono applicate alla drop elaboration in rustc?

(COMP02, slide 31) Alcune ottimizzazioni concettuali:

* servono drop flag solo per i path che sono il target di un `Drop` (o che hanno il target come prefisso);
* alcune variabili sono note essere sempre inizializzate (o sempre non inizializzate) quando vengono droppate: non necessitano di drop flag;
* se un insieme di path viene droppato o mosso solo tramite un prefisso condiviso, questi path possono condividere un unico drop flag.

Un sottoinsieme di queste ottimizzazioni è implementato in rustc. La drop elaboration classifica ciascun `Drop` del MIR appena costruito in una delle quattro categorie seguenti:

* **Static**: il target è sempre inizializzato;
* **Dead**: il target è sempre non inizializzato;
* **Conditional**: il target è interamente inizializzato oppure interamente non inizializzato (mai parzialmente);
* **Open**: il target può essere parzialmente inizializzato.

Per determinare la categoria, rustc usa una coppia di analisi dataflow: **`MaybeInitializedPlaces`** e **`MaybeUninitializedPlaces`**. Se una place compare in una ma non nell'altra, allora si sa a compile-time se è Dead o Static: non serve un flag per il target; il terminator `Drop` viene rimosso (Dead) o mantenuto (Static). Per i drop **Conditional** viene generato un drop flag per il target.

---

## 44. Che cosa sono gli "Open Drops"?

(COMP02, slide 32) Concretamente, nella costruzione del MIR e nelle prime fasi di analisi, un `drop(x)` può essere "open" nel senso che:

* il compilatore sa che `x` deve essere droppato;
* ma non ha ancora completamente elaborato **come** avviene quel drop.

Questo include: se `x` ha un'implementazione custom di `Drop`; se `x` è parzialmente inizializzato o parzialmente mosso; quali campi di `x` devono ancora essere droppati; e in quale ordine devono avvenire i drop annidati.

Più avanti nella pipeline, durante la drop elaboration, questi open drop vengono trasformati in sequenze completamente esplicite di operazioni di drop (a volte chiamate drop "closed"), dove:

* tutti i cammini di controllo di flusso sono resi espliciti;
* tutti i drop campo-per-campo sono inseriti;
* i drop condizionali (dipendenti dai move) sono gestiti con precisione.

Perché esiste questa separazione: consente al compilatore di mantenere il MIR più semplice nelle prime analisi (borrow checking, dataflow), ed espandere i drop nella loro forma completa di basso livello, necessaria per la corretta esecuzione, solo in seguito. Un Open Drop è quindi essenzialmente un segnaposto per la semantica di distruzione che viene raffinato in operazioni concrete nelle passate MIR successive.

# PARTE IV — COMP03: Il Borrow Checker sul MIR

## 45. Che cosa verifica il borrow checker, oltre a ownership e borrowing?

Il borrow checker di Rust è responsabile di far rispettare le regole di ownership e borrowing, **più**: che tutte le variabili siano inizializzate prima di essere usate (COMP03, slide 5).

Opera sul **MIR**. Un'implementazione più vecchia operava sull'HIR; fare borrow checking sul MIR ha diversi vantaggi:

* il MIR è molto meno complesso dell'HIR; il desugaring radicale aiuta a prevenire bug nel borrow checker;
* soprattutto, usare il MIR abilita le **"non-lexical lifetimes" (NLL)**, cioè regioni derivate dal control-flow graph.

---

## 46. Come si inquadra il borrow checking come analisi di programma?

(COMP03, slide 6)

* **Dominio**: il checker ragiona su places, move path, *loans* (prestiti), stati di inizializzazione e regioni, in posizioni del CFG del MIR.
* **Vincoli**: il type checking sul MIR genera *region constraint*, mentre le analisi di move e borrow producono fatti sui punti del programma.
* **Dataflow**: idee classiche di gen/kill e punto fisso appaiono nel calcolo di inizializzazione, liveness e validità dei loan.
* **Diagnostica**: il risultato non è solo accetta/rifiuta; il compilatore mappa i fatti sugli span del sorgente per spiegare perché un borrow o un move non è valido.

---

## 47. Quali sono le fasi principali del borrow checker sul MIR?

(COMP03, slide 7 — elenco ufficiale delle 8 fasi)

1. **Entry point**: query `mir_borrowck`. Il borrow checker è implementato in `rustc_borrowck` ed è invocato come query sul MIR.
2. **MIR duplication and preparation**: viene creata una copia locale del MIR, che sarà mutata *in-place* per attaccare le informazioni di regione.
3. **Region variable initialization**: `replace_regions_in_mir` sostituisce tutte le annotazioni di lifetime con variabili di inferenza fresche.
4. **Dataflow analyses (moves and initialization)**: le analisi calcolano dove i valori vengono mossi, inizializzati o invalidati attraverso il CFG.
5. **Second type checking over MIR**: un type check a livello MIR deriva vincoli fra regioni (lifetime).
6. **Region inference (constraint solving)**: calcola l'insieme di punti del CFG in cui ciascuna lifetime deve valere, tramite inferenza stile punto-fisso.
7. **Borrow sets / borrows in scope**: determina quali borrow sono attivi in ciascun punto del programma nel CFG.
8. **Final validation pass (error reporting)**: un secondo attraversamento verifica le operazioni (es. `*a + 1`) rispetto a: stato di inizializzazione, regole di borrowing, vincoli di mutabilità.

---

## 48. Esempio guida (worked example 1): funzione con borrow mutabile

(COMP03, slide 8)

```rust
// Rust
fn example(a: &mut i32) -> i32 {
    let x = *a;
    *a = x + 1;
    x
}
```

```text
// Simplified MIR
fn example(_1: &mut i32) -> i32 {
    let mut _0: i32; // return
    let mut _2: i32; // x
    bb0: {
        _2 = (*_1);     // read through borrow
        (*_1) = _2 + 1; // write through borrow
        _0 = _2;
        return;
    }
}
```

### Fasi 1–2: Region Variables & MIR Preparation

Tutte le lifetime nel MIR sono sostituite con variabili di regione fresche (slide 9):

```text
_1: &mut i32  ⟶  _1: &'r1 mut i32
```

```text
fn example(_1: &'r1 mut i32) -> i32 {
    let mut _0: i32;
    let mut _2: i32;
    bb0: {
        _2 = (*_1);
        (*_1) = _2 + 1;
        _0 = _2;
        return;
    }
}
```

`'r1` è un'incognita che verrà risolta successivamente. Il MIR è ora annotato ma non ancora validato: si passa da lifetime esplicite a variabili da inferire.

### Fase 3: Dataflow (Moves, Initialization)

(slide 10) Si calcola dove le variabili sono inizializzate, dove i valori sono mossi, dove diventano non validi — è la classica dataflow analysis sul CFG (simile alla liveness). In questo esempio: `_2` è inizializzata a `_2 = (*_1)`; `_1` è usata ma non mossa; nessuna lettura di valore non inizializzato.

### Fasi 4–5: Generazione dei vincoli + Region Inference

(slide 11) Generazione dei vincoli dalle operazioni MIR:

* `_2 = (*_1)` → richiede: `'r1` deve essere valida in questo punto del programma;
* `(*_1) = _2 + 1` → richiede: `'r1` ancora valida, nessun borrow in conflitto.

Region inference: si risolvono i vincoli calcolando `'r1 = {bb0 entry … bb0 exit}`. Interpretazione: la lifetime deve coprire tutti gli usi di `_1`. Questa è un'analisi CFG-based, stile punto-fisso (come nei framework dataflow).

### Fasi 6–7: Borrow attivi + verifica finale

(slide 12) In ogni punto del programma si calcola, ad esempio: `IN[bb0]: { mut borrow of _1 }`. Questo dice quali riferimenti sono attivi e quali vincoli di aliasing devono valere — concettualmente simile ai *live set*, ma per i borrow.

Si valida ora ogni statement MIR. Per `(*_1) = _2 + 1`:

* `_1` è inizializzata? **SÌ**
* `_1` è presa in prestito mutabilmente più di una volta? **NO**
* Ci sono borrow immutabili in conflitto? **NO**
* ✔ OK

---

## 49. Esempio guida (worked example 2): dangling reference — traccia completa

(COMP03, slide 13) Il classico caso di riferimento dangling (come in C/C++):

```rust
fn bad() -> &i32 {
    let x = 10; // allocated on stack
    &x
}
```

```text
// Simplified MIR
fn bad() -> &i32 {
    let mut _0: &i32; // return place
    let mut _1: i32;  // x
    bb0: {
        _1 = const 10;
        _0 = &_1; // borrow of local
        return;
    }
}
```

### Fasi 1–2: Region Variables & MIR Preparation

(slide 14) Le lifetime nel MIR sono sostituite da variabili di regione fresche, incluse variabili aggiuntive per i borrow:

```text
_0: &i32  ⟶  _0: &'r0 i32
_1: i32
_0 = &_1  ⟶  _0 = &'r1 _1
```

```text
fn bad() -> &i32 {
    let mut _0: &'r0 i32; // return place
    let mut _1: i32;      // x
    bb0: {
        _1 = const 10;
        _0 = &'r1 _1;     // borrow of local
        return;
    }
}
```

### Fase 4: Generazione dei vincoli

(slide 15) Dall'assegnamento `_0 = &'r1 _1` viene generato il vincolo:

```text
'r1 : 'r0    ("'r1 outlives 'r0")
```

cioè il borrow deve vivere almeno quanto il valore di ritorno.

### Fase 5: Region Inference (CFG-based)

(slide 16) Si calcola dove le regioni sono valide:

```text
bb0:
[p1] _1 = 10
[p2] _0 = &_1
[p3] return

'r1 = {p2, p3}                // scope rule
'r0 = {p3, caller context}
```

**Fallimento del vincolo**: `'r1 : 'r0` richiede che tutti i punti di `'r0` appartengano a `'r1`, il che è **falso** (il contesto del chiamante non appartiene a `'r1`, che finisce con il ritorno della funzione).

Nota fondamentale delle slide: **l'errore non viene rilevato localmente nel punto del borrow, ma globalmente dopo l'inferenza delle regioni**:

```text
constraints + CFG + drops ⇒ unsatisfiable
```

---

## 50. Come vengono tracciati moves e inizializzazione nel borrow checker?

(COMP03, slide 17–18)

* **Vista unificata**: inizializzazione = stato della ownership. Il borrow checker tiene traccia di un insieme di "place inizializzate": l'assegnamento aggiunge all'insieme, il move rimuove dall'insieme.
* **Moves e inizializzazione sono la stessa analisi**: dal punto di vista del compilatore, sono solo transizioni di stato in un'analisi dataflow.
* **Esempio di comportamento**: una variabile diventa inizializzata dopo un assegnamento, ma un move (es. `drop(a)` o `b = a`) la rende di nuovo non inizializzata, causando errori sugli usi successivi.
* **Granularità: "move path", non variabili**: il tracciamento avviene a livello di *move path* (es. `a`, `a.0`, `a.b.c`), permettendo un ragionamento fine-grained sui *partial move*.

Esempio (slide 18):
```rust
fn foo() {
    let a: Vec<u32>;
    // a is not initialized yet
    a = vec![22];
    // a is initialized here
    std::mem::drop(a); // a is moved here
    // a is no longer initialized here
    let l = a.len(); //~ ERROR
}
```

---

## 51. Che cosa sono i move path e come sono costruiti?

(COMP03, slide 19–20)

* **Move path ≈ MIR Place (ottimizzate)**: ogni move path rappresenta una locazione di memoria ed è memorizzato come `MovePathIndex` per efficienza.
* **Fase di costruzione**: i move path sono costruiti attraversando il MIR (`MoveData::gather_moves`), registrando dove ciascuna place è inizializzata e mossa.
* **Move path illegali sono esclusi**: nessun tracciamento è creato per elementi di array (`foo[1]`) e borrow dereferenziati (`*foo`) — questo riduce l'overhead dell'analisi.
* **Struttura ad albero**: i move path formano un albero gerarchico (es. `a → a.b → a.b.c`), permettendo query su genitori/figli e un'analisi efficiente dei partial move.

Esempio (slide 20):
```rust
fn foo() {
    let a: (Vec<u32>, Vec<u32>) = (vec![22], vec![44]);
    // a.0 and a.1 are both initialized
    let b = a.0; // moves a.0
    // a.0 is not initialized, but a.1 still is
    let c = a.0; // ERROR
    let d = a.1; // OK
}
```

---

## 52. Come si formalizza la Move Analysis come dataflow forward?

(COMP03, slide 21)

* **Dominio**: `IN[n], OUT[n] ⊆ MovePaths`; ogni elemento è un move path (es. `a`, `a.0`, `a.b.c`).
* **Significato**: `IN[n]`: path inizializzati prima dello statement `n`; `OUT[n]`: path inizializzati dopo lo statement `n`.
* **Equazioni dataflow forward standard**:

```text
OUT[n] = GEN[n] ∪ (IN[n] − KILL[n])
IN[n]  = ⋃ OUT[p]   per ogni predecessore p
```

Interpretazione in Rust (slide 22): `GEN[n]` (inizializzazioni) — gli assegnamenti tipo `a = ...` aggiungono `a` all'insieme inizializzato. `KILL[n]` (move) — i move tipo `let b = a; drop(a);` rimuovono `a` dall'insieme inizializzato.

---

## 53. Esempio numerico: caso scalare

(COMP03, slide 23)

```rust
let a: Vec<u32>;
a = vec![22];
drop(a);
let l = a.len(); // ERROR
```

| Program Point | IN | GEN | KILL | OUT |
|---|---|---|---|---|
| entry | ∅ | ∅ | ∅ | ∅ |
| `a = ...` | ∅ | {a} | ∅ | {a} |
| `drop(a)` | {a} | ∅ | {a} | ∅ |
| `a.len()` | ∅ | — | — | **ERROR** |

`a ∉ IN` → uso di valore non inizializzato.

---

## 54. Esempi numerici: caso field-sensitive (move path composti)

**Caso 1 — move dell'intera tupla** (COMP03, slide 24):
```rust
let a: (Vec<u32>, Vec<u32>) = (vec![1,2,3], vec![4,5,6]);
let b = a;
```

| Statement | GEN | KILL |
|---|---|---|
| `init a` | `{a, a.0, a.1}` | ∅ |
| `b = a` | `{b}` | `{a, a.0, a.1}` |

Move path: `{a, a.0, a.1, b}`. Risultato: inizializzati = `{b}`. **Muovere un genitore uccide tutti i figli.**

**Caso 2 — move di un solo campo** (slide 25):
```rust
let a: (Vec<u32>, Vec<u32>) = (vec![1,2,3], vec![4,5,6]);
let b = a.0;
```

| Statement | GEN | KILL |
|---|---|---|
| `init a` | `{a, a.0, a.1}` | ∅ |
| `b = a.0` | `{b}` | `{a.0}` |

Move path: `{a, a.0, a.1, b}`. Risultato: inizializzati = `{a, a.1, b}` — `a.0` è morto, ma `a.1` è ancora valido. **Muovere un figlio NON uccide i fratelli.**

**Caso 3 — errore: move parziale seguito da move totale** (slide 26):
```rust
let a: (Vec<u32>, Vec<u32>) = (vec![1,2,3], vec![4,5,6]);
let b = a.0;
let c = a; // ERROR: use of partially moved value a
```

| Statement | IN | GEN | KILL |
|---|---|---|---|
| `init a` | ∅ | `{a, a.0, a.1}` | ∅ |
| `b = a.0` | `{a, a.0, a.1}` | `{b}` | `{a.0}` |
| `c = a` | `{a, a.1, b}` | `{c}` | `{a, a.0, a.1}` |

Move path: `{a, a.0, a.1, b, c}`. Errore: uso di un valore parzialmente mosso `a`.

---

## 55. Perché serve un secondo type check a livello di MIR se il THIR è già tipato?

(COMP03, slide 27–28)

* Il **MIR type-check** è una componente chiave del borrow check: attraversa il MIR ed esegue un "type check" completo, e durante questo passaggio scopre anche i vincoli di regione applicabili al programma, sostituendo tutte le regioni del corpo con regioni fresche non vincolate.
* Anche se il MIR è costruito a partire dal THIR — già completamente type-checked — rustc esegue comunque un MIR type check perché il processo di abbassamento **non è banalmente type-preserving**: introduce nuovi costrutti e invarianti che devono essere validati indipendentemente.
* Durante la transizione THIR → MIR il compilatore esegue desugaring, introduce temporanei, riordina la valutazione, inserisce operazioni implicite (borrow, move, drop), e semplifica le espressioni in un CFG. Queste trasformazioni possono esporre inconsistenze o richiedere garanzie aggiuntive non esplicitamente verificate a livello THIR.
* Il MIR type check garantisce che tutte queste operazioni abbassate siano internamente coerenti, che operandi e place abbiano i tipi corretti, e che le invarianti richieste dalle fasi successive (borrow checking, ottimizzazioni, codegen) siano rispettate.
* In altre parole, agisce come un passo di **validazione difensiva**: il THIR garantisce la correttezza del programma a livello sorgente, mentre il MIR type checking garantisce la correttezza della trasformazione del compilatore stesso verso il MIR.

---

## 56. Qual è la differenza fra "lifetime" e "region" nel gergo di rustc?

(COMP03, slide 29)

* Una **region** è la rappresentazione interna del compilatore per una lifetime, usata durante type checking e borrow checking.
* Una region denota un insieme di punti del programma (o scope nel CFG) in cui un riferimento è considerato valido. Invece di pensare alle lifetime come scope puramente sintattici, il compilatore le modella come regioni che possono essere confrontate, vincolate (es. una regione deve *outlive* un'altra) e inferite tramite un'analisi stile dataflow.
* "Lifetime" è il concetto rivolto all'utente; "region" è il modello semantico e analitico interno del compilatore.
* Quando si scrive un'annotazione di lifetime come `'a`, il compilatore la traduce in variabili di regione e vincoli (es. `'a: 'b` diventa "la regione `'a` outlive la regione `'b`").
* Con le NLL, queste regioni non sono più legate a blocchi lessicali, ma corrispondono a insiemi precisi di punti del CFG, calcolati tramite risoluzione di vincoli.
* Quindi le lifetime nel linguaggio sono essenzialmente nomi/astrazioni su regioni, mentre le regioni sono gli oggetti concreti manipolati dal borrow checker.

---

## 57. Panoramica della Region Inference (NLL)

(COMP03, slide 30–33 — vista introduttiva, dettagliata poi in COMP04)

* **Due fasi principali**: `replace_regions_in_mir` (prepara il MIR per l'inferenza) e `compute_regions` (risolve le variabili di regione/lifetime).
* **Step 1 — Identificazione delle universal regions**: si estraggono le regioni libere dalla firma della funzione (es. `'a`, `'static`), che rappresentano le lifetime visibili dal chiamante.
* **Step 2 — Sostituzione delle regioni con variabili**: tutte le regioni del MIR diventano variabili di inferenza fresche; questo scarta l'informazione di lifetime lessicale ed abilita l'analisi control-flow-sensitive (NLL).
* **Step 3 — Generazione dei vincoli (MIR type check)**: il type checker MIR specializzato produce *outlives constraint* (`'a: 'b`) e altre relazioni fra regioni.
* **Step 4 — Risoluzione dei vincoli (region inference)**: si costruisce un `RegionInferenceContext` e si calcolano i valori delle regioni tramite propagazione dei vincoli / risoluzione a punto fisso.

**Rappresentazione delle regioni** (slide 31): una regione è un insieme di punti del programma — ogni regione è l'insieme delle locazioni CFG in cui è valida. Gli elementi di regione includono: locazioni MIR (punti del programma), `end('a)` (la lifetime si estende nel chiamante), `end('static)` (il resto del programma), e placeholder per regioni sconosciute. Implementazione efficiente: le regioni sono memorizzate come **bitset**, indicizzate da `RegionElementIndex`.

**Vincoli che guidano l'inferenza** (slide 32): *outlives constraint* (`'a: 'b` → `'a` deve includere tutto ciò che è in `'b`, generati dal type checker MIR) e *liveness constraint* (la regione deve essere valida ovunque venga usata).

**Come funziona** (slide 33):
* **Inizializzazione da liveness**: ogni regione parte dai punti del CFG in cui è usata (dalle liveness constraint);
* **Propagazione dei vincoli**: per ogni outlives constraint `'a: 'b`: `'a ← 'a ∪ 'b ∪ {end('b)}`, ripetuto fino al punto fisso (`propagate_constraints`);
* **Le regioni crescono monotonicamente**: i valori delle regioni sono insiemi di elementi; la propagazione è un dataflow union-based.

---

## 58. Grande quadro: Move Analysis e Region Inference come due facce dello stesso framework

(COMP03, slide 36–38)

Il borrow checking di Rust = due analisi dataflow che interagiscono sul MIR:

1. **Move / Initialization Analysis** (ownership);
2. **Region Inference (NLL)** (lifetime).

Entrambe sono: basate sul CFG, monotone, risolte tramite iterazione a punto fisso.

**Struttura dataflow condivisa** (slide 37):

| Aspetto | Move Analysis | Region Inference (NLL) |
|---|---|---|
| Dominio | insieme di move path | insieme di elementi di regione |
| Direzione | forward | forward (propagazione) |
| Lattice | powerset | powerset |
| Transfer | GEN/KILL | union tramite vincoli |
| Significato | "è inizializzato?" | "la regione è valida qui?" |
| Fixpoint | sì | sì |

Equazioni riassuntive:
```text
OUT[n] = GEN[n] ∪ (IN[n] − KILL[n])
IN[n]  = ⋃ OUT[p]
GEN = assignments ;  KILL = moves

R_a = LIVENESS_a ∪ ⋃ { R_b ∪ end(b) | a: b }
```

**Differenze e interazione** (slide 38):

* la **move analysis** può *rimuovere* informazione (kill);
* la **region inference** *aggiunge solo* informazione (le regioni crescono);
* dove interagiscono: la move analysis dice `drop(x) ⇒ x non inizializzato`; la region inference dice `r deve essere valida qui`; il conflitto nasce quando la regione dice "valido" ma la move analysis dice "il valore non c'è più":

```rust
let x = vec![1];
let r = &x;
drop(x);
*r; // error
```

# PARTE V — COMP04: Region Inference dettagliata, Two-Phase Borrows, Closure Capture Inference

## 59. Quali tipi di vincoli raccoglie il MIR type checker prima della region inference?

(COMP04, slide 8) Prima della region inference, i vincoli sono raccolti dal MIR type checker. Tipi di vincoli:

* **liveness constraint** (`R live at E`);
* **outlives constraint** (`R1: R2`), che nascono dal subtyping;
* **member constraint** (`member R_m of [R_c...]`), che nascono da `impl Trait`.

Il MIR type checker raccoglie anche i **type test**, da verificare dopo la region inference.

---

## 60. Esempi di generazione di vincoli: liveness e outlives da subtyping

(COMP04, slide 9)

**Liveness constraint semplice**:
```rust
fn f<'a>(x: &'a u32) -> u32 {
    let y = x;
    *y
}
```
Il borrow/riferimento memorizzato in `y` è vivo (*live*) nel punto in cui `*y` è usato.

**Outlives constraint da assegnamento**: il compilatore introduce una regione inferita, diciamo `'0`, per `y`:

```text
x : &'a u32
y : &'0 u32
```

Perché l'assegnamento sia valido serve la relazione di sottotipizzazione:

```text
&'a u32 <: &'0 u32
```

il che implica `'a : '0`.

---

## 61. Come vengono trattati i cicli fra outlives constraint? (SCC)

(COMP04, slide 11) Le outlives constraint (`'a: 'b`) sono rappresentate come un **grafo diretto** in cui le regioni sono nodi e i vincoli sono archi.

* I **cicli** in questo grafo indicano regioni che devono essere uguali, perciò il compilatore calcola le **componenti fortemente connesse (SCC)** per raggruppare tali regioni.
* Ciascuna SCC viene trattata come un'unica unità con un valore condiviso, migliorando l'efficienza.
* Dopo aver collassato i cicli in SCC, il compilatore lavora su un grafo ridotto di SCC, che è **sempre un DAG**.
* I vincoli fra regioni diventano vincoli fra SCC, abilitando una propagazione efficiente: le dipendenze potenzialmente cicliche sono evitate.

---

## 62. Che cosa sono i "type test" e perché non sono codificati direttamente nel solver?

(COMP04, slide 12–15)

Durante il MIR type checking, rustc genera vincoli e **type test**, obbligazioni speciali su tipi che coinvolgono regioni. Il solver della region inference calcola una soluzione (una mappa da variabili di regione a insiemi di punti del programma). Dopo che la soluzione è stata calcolata, rustc controlla tutti i type test memorizzati contro quella soluzione.

Vengono usati quando:
* codificare direttamente il vincolo nel solver sarebbe troppo complesso o inefficiente;
* oppure è più pulito verificarlo dopo aver conosciuto le regioni finali.

**Cosa verificano concettualmente** (slide 13): un type test tipicamente verifica che un tipo sia *well-formed* rispetto alle lifetime inferite. Esempi:
* un tipo riferimento `&'r T` è valido solo se `'r` contiene tutti i punti in cui il riferimento è usato;
* un vincolo generico come `T: 'a` richiede che tutti i riferimenti dentro `T` vivano abbastanza da soddisfare `'a`;
* le relazioni di sottotipizzazione fra tipi che coinvolgono lifetime sono rispettate.

Sono quindi essenzialmente controlli di *well-formedness* / *subtyping* su tipi che dipendono dalle regioni.

**Perché non incorporarli nel solver** (slide 14): il solver lavora su un dominio relativamente semplice (insiemi di punti, outlives constraint, ecc.), mentre la struttura dei tipi può essere complessa (tipi annidati, projections, generics); incorporare tutto ciò nel calcolo a punto fisso complicherebbe e rallenterebbe l'inferenza.

**Tabella di esempi** (slide 15):

| Codice Rust | Type test generato | Spiegazione |
|---|---|---|
| `fn f<'a, T>(x: &'a T) { let y: &'a T = x; }` | `T: 'a` | `&'a T` è well-formed solo se il referente `T` è valido per almeno `'a`. **Soddisfatto**. |
| `fn f<'a, T>(x: T) { let r: &'a T; }` | `T: 'a` | Anche se `r` è solo una dichiarazione locale, il tipo annotato `&'a T` impone comunque un obbligo di well-formedness su `T`. **Non soddisfatto**. |
| `fn f<'a, T>(x: &'a [T]) { let y: &'a [T] = x; }` | `[T]: 'a` (riducibile a `T: 'a`) | Un riferimento a slice con lifetime `'a` richiede che il tipo elemento della slice sia valido per `'a`. **Soddisfatto**. |
| `struct S<T>(T); fn f<'a, T>(x: &'a S<T>) {}` | `S<T>: 'a` (richiede `T: 'a`) | Il riferimento `&'a S<T>` richiede che l'intero tipo referente `S<T>` outlive `'a`; strutturalmente ciò dipende da `T`. |

---

## 63. Esempio: type test generato dal tipo di ritorno

(COMP04, slide 16)

```rust
fn f<'a,'b>(x: &'a u32) -> &'b u32 {
    x
}
```

Ritornare `x` dove è atteso `&'b u32` richiede: `&'a u32 <: &'b u32`. Il compilatore genera dunque il type test: `'a: 'b`. Questo **non** è usato come outlives constraint durante la propagazione, ma è solo controllato dopo la region inference. Poiché non è dichiarato alcun vincolo `'a: 'b` nella firma, **la compilazione fallisce**.

---

## 64. Che cosa sono le Universal Regions e come funziona il controllo di consistenza finale?

(COMP04, slide 17)

* Le **universal regions** si riferiscono alle lifetime dichiarate dall'utente, come i parametri di lifetime (`'a`, `'b`) e `'static`.
* Sono **universalmente quantificate**: il compilatore deve garantire che la funzione sia corretta per **tutte** le possibili istanziazioni di queste lifetime (che soddisfino i vincoli dichiarati).
* Internamente, tutte le lifetime sono rappresentate come variabili di regione: le universal region occupano un sottoinsieme fisso di queste variabili; le regioni **esistenziali** rappresentano variabili di inferenza.
* Durante la region inference, a ciascuna regione viene assegnato un insieme che contiene punti di controllo di flusso e marcatori speciali come `end('a)`, che indicano l'estensione di una lifetime.
* Dopo la propagazione, il compilatore esegue un **controllo di consistenza**: se il valore inferito di una universal region `'a` include `end('b)`, allora la relazione `'a: 'b` deve essere stata **esplicitamente dichiarata**.
* Se non lo è, questo indica una violazione della firma della funzione e produce un errore di compilazione.
* Questo garantisce che le relazioni di lifetime inferite non eccedano quelle promesse dai bound della funzione.

---

## 65. Struttura dati `RegionInferenceContext`

(COMP04, slide 4–5 e già visto in COMP03 slide 35, ribadito) Contiene:

* `constraints` → le relazioni outlives;
* `liveness_constraints` → i semi iniziali;
* `universal_regions` → le lifetime libere;
* `universal_region_relations` → i bound noti (es. clausole `where`);
* `type_tests` → i vincoli da verificare dopo la soluzione.

Processo di risoluzione (`solve()`):
```text
solve():
  propagate_constraints
  → check_type_tests
  → check_universal_regions
```

---

## 66. Esempio: liveness che termina all'ultimo uso — perché il codice viene accettato

(COMP04, slide 19)

```rust
fn f() {
    let mut x = 10;
    let r = &x;
    println!("{}", r);
    let m = &mut x;
    *m += 1;
}
```

Il borrow condiviso `r` è vivo solo fino al suo ultimo uso:
```text
'r live at println!("{}", r)
'r = { points up to last use of r }
'm = { points from &mut x to *m += 1 }
```

Dopo quel punto, la regione di `r` termina, quindi il borrow mutabile può iniziare. Poiché queste regioni non si sovrappongono, il programma è **accettato**.

---

## 67. Esempio contrapposto: rifiutato perché la liveness si sovrappone al borrow mutabile

(COMP04, slide 20)

```rust
fn f() {
    let mut x = 10;
    let r = &x;
    let m = &mut x;
    println!("{}", r);
    *m += 1;
}
```

Qui `r` è ancora vivo al `println!` **dopo** che `m` è stato creato:
```text
'r live at println!("{}", r)
'm live at *m += 1
```

Il borrow condiviso e quello mutabile si sovrappongono. Questo viola le regole di borrowing, quindi il programma è **rifiutato**.

---

## 68. Che cosa sono i Two-phase Borrows?

(COMP04, slide 21) Sono una forma speciale di borrow mutabile che si comporta temporaneamente come un borrow condiviso, per permettere pattern come `vec.push(vec.len())`.

* Sono introdotti solo in casi impliciti specifici (chiamate a metodo con receiver `&mut`, *reborrow* negli argomenti, operatori di assegnamento composti).
* Sono implementati come temporanei con due punti chiave:
  - un **punto di riserva** (*reservation point*), dove inizia il comportamento "simil-condiviso";
  - un **punto di attivazione** (*activation point*), dove diventa un borrow mutabile a tutti gli effetti.
* Sono trattati come borrow mutabili ma con regole rilassate prima dell'attivazione.

### Traccia completa: `vec.push(vec.len() as i32)`

(COMP04, slide 22)

```rust
fn push_len(v: &mut Vec<i32>) {
    v.push(v.len() as i32);
}
```

```text
// Conceptual THIR, simplified
Vec::push(&mut *v, (Vec::len(&*v)) as i32)
```

```text
// MIR
fn push_len(_1: &mut Vec<i32>) -> () {
    let mut _0: ();
    let mut _2: &mut Vec<i32>;
    let mut _3: &Vec<i32>;
    let mut _4: usize;
    let mut _5: i32;

    bb0: {
        [p1] _2 = &mut (*_1);   // reservation of mutable borrow
        [p2] _3 = &(*_1);       // shared borrow for len()
        [p3] _4 = Vec::<i32>::len(move _3);
        [p4] _5 = move _4 as i32 (IntToInt);
        [p5] _0 = Vec::<i32>::push(move _2, move _5);
        return;
    }
}
```

Regioni fresche:
```text
_2: &'r_mut mut Vec<i32>
_3: &'r_shr Vec<i32>
```

Soluzione delle regioni:
```text
'r_shr = { p2, p3 }
'r_mut = { p1, p2, p3, p4, p5 }
```

Ma `'r_mut` è **two-phase**:
* riserva: `p1`
* attivazione: `p5`

Quindi tra `p1` e `p5` il borrow mutabile è solo **riservato**, e l'uso del borrow condiviso in `p3` (il `len()`) è legale — senza il meccanismo two-phase, questo violerebbe [B2]/[B1] perché coesisterebbero un borrow mutabile e uno condiviso sulla stessa risorsa.

---

## 69. Che cos'è la Closure Capture Inference?

(COMP04, slide 23) Le closure di Rust sono compilate trasformandole in struct che memorizzano le variabili catturate. Il compilatore deve:

* identificare quali variabili dell'ambiente circostante la closure utilizza;
* determinare come ciascuna è usata (letta, modificata, o consumata);
* in base a ciò, decidere la **modalità di cattura**: per riferimento condiviso (`&T`), per riferimento mutabile (`&mut T`), o per valore (*move*).

Questa analisi permette anche a rustc di inferire quale trait di closure implementa la closure:
* **`Fn`** (solo letture);
* **`FnMut`** (muta);
* **`FnOnce`** (consuma valori).

**Quando avviene** (slide 24): l'inferenza della cattura avviene durante la fase di type checking, specificamente nello stadio di type-checking sull'HIR — dopo il parsing e l'abbassamento a HIR, durante l'inferenza dei tipi e la preparazione al borrow checking.

Vedi anche la sezione 26 sopra (COMP02) per il desugaring delle closure in struct + trait.

---

## 70. Tre esempi di MIR per la cattura di variabili: read-only, mutate, move

**Cattura in sola lettura** (COMP04, slide 26):

```rust
fn invoke(f: impl Fn()) { // anche FnMut(), FnOnce()
    f();
}
fn main() {
    let x: i32 = 10;
    invoke(|| println!("Hi {}", x)); // The closure just reads x.
    println!("Value of x after return {}", x);
}
```

```text
bb0: {
    _1 = const 10_i32;
    _4 = &_1;
    _3 = {closure@immut.rs:13:12: 13:14} { x: move _4 }; // struct with init
    _2 = invoke::<{closure@immut.rs:13:12: 13:14}>(move _3) -> [return: bb1, unwind continue];
}
```

Nota: `x` è catturata per **riferimento condiviso** (`&_1`).

**Cattura con mutazione** (slide 27):

```rust
fn invoke(mut f: impl FnMut()) { // anche FnOnce()
    f();
}
fn main() {
    let mut x: i32 = 10;
    invoke(|| {
        x += 10; // The closure mutates the value of x
        println!("Hi {}", x)
    });
    println!("Value of x after return {}", x);
}
```

```text
bb0: {
    _1 = const 10_i32;
    _4 = &mut _1;
    _3 = {closure@mut.rs:7:12: 7:14} { x: move _4 };
    _2 = invoke::<{closure@mut.rs:7:12: 7:14}>(move _3) -> [return: bb1, unwind continue];
}
```

Nota: `x` è catturata per **riferimento mutabile** (`&mut _1`).

**Cattura per move** (slide 28):

```rust
fn invoke(f: impl FnOnce()) { // errore con Fn() o FnMut()
    f();
}
fn main() {
    let x = vec![21];
    invoke(|| {
        drop(x); // Makes x unusable after the fact.
    });
    // println!("Value of x after return {:?}", x); // non compilerebbe
}
```

```text
bb2: {
    _4 = {closure@drop.rs:7:12: 7:14} { x: move _1 }; // move di x
    _3 = invoke::<{closure@drop.rs:7:12: 7:14}>(move _4) -> [return: bb3, unwind continue];
}
```

Nota: `x` è mossa per **valore** dentro la struct della closure.

---

## 71. Come vengono inferite le modalità di cattura internamente? Upvar, ExprUseVisitor, Delegate

(COMP04, slide 29–32)

* Un **upvar** è una variabile della funzione circostante che una closure cattura (una "variabile libera"). Il compilatore le identifica con un'analisi interna (`upvars_mentioned`).
* Le closure differiscono dalle funzioni normali perché catturano e prendono in prestito questi upvar dal loro ambiente.
* rustc inferisce come ciascun upvar è catturato partendo da un borrow immutabile e **rilassandolo** se necessario:
  - resta immutabile se solo letto;
  - diventa mutabile se modificato;
  - diventa *move* se consumato (es. droppato).
* In base a ciò, la closure implementa il trait appropriato: `Fn` → borrow immutabile; `FnMut` → borrow mutabile; `FnOnce` → semantica di move.

**Il Visitor per l'inferenza della cattura** (slide 30): il modulo `upvar.rs` definisce **`euv::ExprUseVisitor`**, che attraversa il sorgente della closure e invoca una callback per ogni upvar che viene preso in prestito, mutato o mosso. Esempio:

```rust
fn main() {
    let mut x = vec![21];
    let _cl = || {
        let y = x[0];  // 1.
        x[0] += 1;     // 2.
    };
}
```

In questo esempio il visitor viene chiamato due volte, per le righe marcate 1 e 2: una per un borrow condiviso, un'altra per un borrow mutabile; dirà anche cosa è stato preso in prestito. Le callback sono definite implementando il trait **`Delegate`**.

**Meccanismo interno** (slide 31): il compilatore usa un sistema di callback (trait `Delegate`) per analizzare come le closure usano le variabili. `InferBorrowKind` implementa questo trait e tiene traccia di come ciascun upvar è catturato:

* `ByValue` (mosso);
* `ByRef` (preso in prestito), con tipi: `ImmBorrow`, `UniqueImmBorrow`, `MutBorrow`.

Callback chiave:
* `consume` → la variabile viene mossa;
* `borrow` → la variabile viene presa in prestito;
* `mutate` → la variabile viene modificata.

Ogni callback riceve un **cmt** (*Category, Mutability, Type*) che descrive origine, posizione e mutabilità della variabile. In base a queste callback, il compilatore aggiusta il tipo di borrow e registra la modalità di cattura finale per ciascuna closure.

**Riassunto** (slide 32): Rust inferisce come le closure catturano le variabili tramite un'analisi statica del loro uso. Le variabili dell'ambiente circostante, chiamate *upvar*, sono identificate e inizialmente assunte come prese in prestito immutabilmente. Man mano che il compilatore analizza come ciascun upvar è usato — letto, mutato o consumato — rilassa progressivamente questa assunzione verso il borrow mutabile o il move, se necessario. Questo processo è implementato tramite un meccanismo basato su callback (`Delegate`), dove operazioni come `borrow`, `mutate` e `consume` aggiornano la modalità di cattura inferita usando informazioni contestuali (`cmt`). Il compilatore registra la modalità di cattura finale per ciascun upvar (per riferimento o per valore, con specifici tipi di borrow), e da qui determina quale trait di closure (`Fn`, `FnMut`, o `FnOnce`) la closure può implementare.

---

## 72. Struttura dataflow condivisa (ripresa e completata da COMP04)

(COMP04, slide 18) Ribadendo la tabella già vista in COMP03, con una precisazione aggiuntiva:

| Aspetto | Move Analysis | Region Inference (NLL) |
|---|---|---|
| Dominio | insieme di move path | insieme di elementi di regione |
| Direzione | forward | forward (propagazione) |
| Lattice | powerset | powerset |
| Transfer | GEN/KILL | union tramite vincoli |
| Significato | "è inizializzato?" | "la regione è valida qui?" |
| Fixpoint | sì | sì |

* la **Move Analysis** opera sul **CFG del MIR**;
* la **Region Inference** opera sul **DAG delle SCC** del grafo (Regioni, Outlives) — si veda la sezione 61.

Le ultime due fasi del borrow checker restano: **Borrow sets / borrows in scope** (determina quali borrow sono attivi in ciascun punto del programma nel CFG) e la **Final validation pass** (controlla ogni operazione rispetto a stato di inizializzazione, regole di borrowing, vincoli di mutabilità).

# PARTE VI — COMP05: Verso la generazione di codice

## 73. Cosa succede dopo il borrow checking, da MIR ai binari?

(COMP05, slide 4) Dopo il borrow checking sul MIR, il backend di rustc esegue diversi passi per produrre l'output (codice eseguibile). Sono supportati diversi backend:

* **LLVM IR** (tipicamente);
* **Cranelift IR**;
* **GCC IR**.

LLVM IR è stabile e pronta per ulteriori ottimizzazioni; Cranelift è più sperimentale; GCC IR è una IR interna del compilatore GCC.

---

## 74. Che cos'è Cranelift come backend di codegen per Rust?

(COMP05, slide 5)

* Cranelift è un backend di compilazione veloce, sicuro, relativamente semplice e innovativo.
* Prende una rappresentazione intermedia di un programma generata da un qualche front-end e la compila a codice macchina eseguibile.
* Anche Cranelift IR è una IR da compilatore con basic block, valori simil-SSA, controllo di flusso, ecc., ma è progettata per **compilazione veloce** e un'architettura di backend più semplice.
* L'obiettivo del backend Cranelift è particolarmente attraente per build di **debug/locali**.
* Il suo uso più comune è come compilatore per **WebAssembly**.

---

## 75. Quali sono le fasi principali del codegen?

(COMP05, slide 6)

1. **Cleanup dopo il borrow checking**, che rimuove dal MIR tutte le informazioni usate per l'analisi ma non necessarie al codegen.
2. **Preparazione del MIR runtime** (inclusa la **drop elaboration**).
3. **Ottimizzazioni sul MIR**, ancora su codice generico.
4. **Monomorphization collection**: identificazione di tutti i tipi concreti che sono istanze di un tipo generico per cui va eseguita la monomorfizzazione.
5. **Lowering del MIR a una codegen IR** per ciascun tipo concreto raccolto.
6. **Codegen backend**, che esegue una serie di passate di ottimizzazione, genera codice eseguibile e collega insieme un binario eseguibile.

La complessità del codegen è dovuta a:
* supporto per **più backend di codegen**: il codice di codegen è generico rispetto all'implementazione del backend, con diversi livelli di astrazione;
* il codegen avviene **asincronamente in un altro thread**, per performance.

Il codegen vero e proprio è eseguito da una libreria di terze parti (uno dei tre backend).

---

## 76. Perché e come vengono eseguite le ottimizzazioni sul MIR?

(COMP05, slide 7)

* Le ottimizzazioni MIR migliorano il MIR prima della generazione di codice del backend, eseguite dopo il borrow checking, producendo un MIR più pulito ed efficiente prima dell'abbassamento alla IR target.
* Migliorano sia le prestazioni runtime sia la velocità di compilazione: un MIR migliore porta a codice macchina generato migliore e riduce il lavoro di ottimizzazione richiesto in seguito (es. da LLVM).
* Le ottimizzazioni sono efficaci proprio perché il MIR è **ancora generico**: le ottimizzazioni MIR avvengono prima della monomorfizzazione, quindi la versione migliorata è riusata per **tutte** le istanziazioni concrete di quella funzione o tipo generico.
* L'ottimizzazione MIR è implementata come una sequenza di **passate**: alcune obbligatorie, alcune servono solo a validare invarianti o eseguire controlli, alcune sono abilitate solo nelle build ottimizzate/release.
* Ottimizzazioni tipiche: **constant propagation**, **dead-code elimination**, **copy propagation**, **semplificazione del CFG**, e **inlining**.
* La query **`optimized_mir`** guida il processo.

---

## 77. Come si definiscono le passate di ottimizzazione MIR?

(COMP05, slide 8) La funzione `run_optimization_passes` definisce la lista delle passate da eseguire e il loro ordine:

* contiene un array di passate da eseguire;
* ogni passata nell'array è una struct che implementa il trait **`MirPass`**; l'array è un array di trait object `&dyn MirPass`. Tipicamente, una passata è implementata nel proprio modulo della crate `rustc_mir_transform`.

Esempi di passate:
* **`CleanupPostBorrowck`**: rimuove parte delle informazioni necessarie solo alle analisi, non al codegen;
* **`ConstProp`**: esegue *constant propagation*.

È facilmente estensibile con nuove passate di ottimizzazione (vedi la rustc-dev-guide, sezione "Quickstart for adding a new optimization").

---

## 78. Quali sono i livelli di ottimizzazione (`opt-level`)?

(COMP05, slide 9)

```text
rustc main.rs -C opt-level=X
```
con `X` uno tra `[0, 1, 2, 3, s, z]`:

* **0** → nessuna ottimizzazione (compilazione veloce, buono per il debugging);
* **1** → ottimizzazioni di base;
* **2** → build ottimizzata standard;
* **3** → ottimizzazioni aggressive;
* **s** → ottimizza per dimensione del binario;
* **z** → ottimizza ancora di più per la dimensione.

`cargo build` → livello **0**; `cargo build --release` → livello **3**.

---

## 79. Come implementano i generics i vari linguaggi, e come si posiziona Rust?

(COMP05, slide 10 — tabella completa)

| Linguaggio | Meccanismo di bound | Idea principale di implementazione | Trade-off principale |
|---|---|---|---|
| Haskell | Type classes | Dictionary passing + polimorfismo parametrico | Codice compatto, chiamate indirette a meno di ottimizzazioni |
| Java | Interfacce / bound | Type erasure | Compatto, meno specificità di tipo a runtime, indirezione |
| C++ | Templates / concepts | Monomorfizzazione | Veloce/specializzato, code bloat |
| C# | Interfacce / vincoli | Generics *reified*, ibrido shared/specialized | Più informazione di tipo a runtime, efficiente sui tipi valore |

---

## 80. Come funziona la monomorfizzazione in Rust?

(COMP05, slide 11)

* Rust ha un ampio supporto per i tipi generici, supportando il polimorfismo universale esplicito con bound (*bounded explicit universal polymorphism*).
* I bound sono espressi tramite **Trait**.
* Rust **monomorfizza** tutti i tipi generici: il compilatore genera una copia diversa del codice di una funzione generica per ciascun tipo concreto necessario.
* La monomorfizzazione è il **primo passo del backend** del compilatore Rust: il MIR generico viene istanziato prima della generazione di codice.
* Stesso trade-off del C++: **veloce/specializzato**, ma **code bloat**.

---

## 81. Come funziona la Mono Item Collection?

(COMP05, slide 12–14)

* Per ogni cosa generica, il compilatore deve raccogliere tutti i tipi concreti che la istanziano. Il codice che esegue questa raccolta è chiamato il **monomorphization collector**.
* Il collector viene eseguito **subito prima** del lowering del MIR e del codegen.
* `rustc_codegen_ssa::base::codegen_crate` chiama la query `collect_and_partition_mono_items`, che esegue la raccolta di monomorfizzazione e poi partiziona il risultato in **codegen unit**.

**Mono item collection** (modulo `rustc_monomorphize`, slide 13):

* La raccolta dei mono item determina tutto ciò che deve generare codice backend. Il collector trova tutti gli item che produrranno artefatti LLVM/backend: funzioni, metodi, closure, static e *drop glue*. Deve anche scoprire ogni istanza concreta monomorfizzata di codice generico, incluse le generiche importate da altre crate.
* Un **"mono item"** rappresenta un artefatto di backend: corrisponde a qualcosa che diventa una funzione o un oggetto globale nella IR generata. I mono item dipendono l'uno dall'altro (es. una funzione che ne chiama un'altra), formando un **grafo diretto dei mono item**.
* L'algoritmo di raccolta lavora in due fasi:
  1. trovare le **radici del grafo** attraversando l'HIR della crate e raccogliendo gli item pubblici/non-generici;
  2. a partire da quelle radici, ispezionare ricorsivamente il MIR per scoprire tutti i mono item usati e le loro istanziazioni concrete di tipo.

**Mono item collection (2)** (slide 14): gli usi sono scoperti dal MIR, non solo dalle chiamate esplicite. Gli archi nel grafo dei mono item nascono da: chiamate a funzioni/metodi; prendere riferimenti a funzioni; generazione della *drop glue*; cast di *unsizing* di trait object (che richiedono vtable); funzioni generiche/inlined cross-crate.

Esempio:
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

Rust supporta strategie di raccolta sia **lazy** che **eager**:
* **collezione lazy**: istanzia solo gli item effettivamente usati, minimizzando il codice generato;
* **collezione eager**: istanzia più item in modo proattivo (utile per compilazione incrementale e comportamento di ricompilazione stabile).

Infine, il collector valuta anche le costanti e traccia i "mentioned items": per evitare errori di compilazione dipendenti dal livello di ottimizzazione, rustc traccia non solo gli item effettivamente usati dopo l'ottimizzazione, ma anche quelli che appaiono sintatticamente nel MIR ("mentioned items"). Questo garantisce che i fallimenti di const evaluation siano riportati in modo consistente anche se il codice morto viene poi eliminato dalle ottimizzazioni.

---

## 82. Che cosa sono le Codegen Unit (CGU) e come vengono partizionate?

(COMP05, slide 16–17)

* La collezione dei mono item generata dal monomorfizzatore è partizionata in **codegen unit (CGU)** dal *partitioner*.
* Una CGU è un insieme di coppie (mono-item, linkage) che diventa un unico modulo LLVM. Il partitioner decide quali funzioni, static, closure e monomorfizzazioni vanno in quale CGU.
* Il partizionamento è cruciale per le prestazioni della **compilazione incrementale**.
* LLVM ricompila e ottimizza interi moduli, non singole funzioni: se una CGU cambia, l'intero modulo LLVM va ricostruito e riottimizzato da zero.
* Trade-off fra velocità di ricompilazione incrementale e prestazioni runtime:
  - **molte CGU piccole** → ricompilazione minima dopo un cambiamento, build incrementali più veloci, ma eseguibili più lenti (ottimizzazioni inter-procedurali e inlining non possibili fra CGU);
  - **poche CGU grandi** → migliore ottimizzazione LLVM e inlining, eseguibili più veloci.

**Come bilancia il partitioner** (slide 17): rustc usa un'euristica basata sui **moduli a livello sorgente**. Per ciascun modulo sorgente, rustc crea:
* una CGU per il codice non-generico stabile;
* una CGU per le istanze generiche monomorfizzate "volatili".

Questo isola i cambiamenti causati dalle istanziazioni generiche e riduce la ricompilazione non necessaria. I riferimenti a funzioni generiche sono particolarmente problematici per la compilazione incrementale: aggiungere o rimuovere un riferimento a una funzione generica può creare o eliminare istanze monomorfizzate, forzando la ricompilazione anche se il corpo della funzione generica stessa non è cambiato.

L'inlining influisce fortemente sulle decisioni di partizionamento: LLVM può fare inlining solo se il corpo del *callee* è disponibile nello stesso modulo LLVM. Perciò il partitioner **duplica** le funzioni idonee fra più CGU quando necessario. rustc tratta principalmente le funzioni marcate `#[inline]` come candidate per l'inlining cross-CGU.

---

## 83. Come avviene il lowering dal MIR a una codegen IR?

(COMP05, slide 18–19)

* Dopo la mono item collection, rustc abbassa il MIR in una IR di backend (di solito LLVM IR, ma sono supportati anche Cranelift e GCC).
* La monomorfizzazione avviene durante questo processo di lowering.
* La generazione di codice inizia in `codegen_crate` e arriva a `codegen_mir`.
* La logica di lowering è divisa per costrutti MIR: moduli diversi gestiscono elementi diversi:
  - `block` → basic block e terminator (specialmente chiamate a funzione e unwinding);
  - `statement` → statement MIR;
  - `operand` → operandi;
  - `place` → riferimenti a memoria/place;
  - `rvalue` → calcoli e valori temporanei.

**Lowering (2)** (slide 19):
* prima della traduzione girano semplici passate di analisi: rustc esegue analisi leggere per produrre LLVM IR più pulita, per esempio rilevando variabili "simil-SSA" così da poterle emettere direttamente in forma SSA invece di affidarsi interamente a ottimizzazioni LLVM come `mem2reg`;
* i basic block MIR di solito mappano direttamente su basic block LLVM: la maggior parte dei blocchi MIR diventa un singolo blocco LLVM, sebbene operazioni come assert, intrinsics o chiamate complesse possano espandersi in più blocchi LLVM;
* la generazione di codice specifica LLVM usa **intrinsics** (operazioni built-in speciali di LLVM) e l'interfaccia builder.

# PARTE VII — COMP06: Linting, Sistema dei Tipi, Type Checking, Type Inference

## 84. Che cos'è un "lint" in rustc?

(COMP06, slide 4) In generale, un **lint** è uno strumento usato per migliorare il codice sorgente. rustc contiene numerosi lint: durante la compilazione, li esegue. Questi possono produrre un *warning*, un errore, o niente affatto, a seconda della configurazione.

Esempio:
```text
$ cat main.rs
fn main() {
    let x = 5;
}
$ rustc main.rs
warning: unused variable: `x`
 --> main.rs:2:9
  |
2 |     let x = 5;
  |         ^
  |
  = note: `#[warn(unused_variables)]` on by default
  = note: to avoid this warning, consider using `_x` instead
```

---

## 85. Qual è la differenza fra lint e diagnostiche fisse?

(COMP06, slide 5)

* Alcuni messaggi sono emessi tramite lint, il cui livello è controllabile dall'utente. La maggior parte delle diagnostiche è invece **hard-coded**, e l'utente non può regolarne il livello.
* Di solito è ovvio se una diagnostica dovrebbe essere "fissa" o un lint, ma esistono zone grigie.

Esempi:
* **Errori del borrow checker**: sono errori fissi. L'utente non può regolare il livello di queste diagnostiche per silenziare il borrow checker.
* **Codice morto (dead code)**: è un lint. Sebbene l'utente probabilmente non voglia codice morto nella propria crate, renderlo un errore rigido renderebbe il refactoring e lo sviluppo molto doloroso.
* **Lint "future-incompatible"**: sono lint silenziabili. Vengono emessi warning, che eventualmente diventeranno errori fissi (hard).

---

## 86. Quali sono i livelli dei lint?

(COMP06, slide 6) In rustc, i lint sono divisi in **sei livelli**:

1. **allow** → non fa nulla;
2. **expect** → (vedi sotto);
3. **warn** → produce un warning, la compilazione procede (es. variabile inutilizzata);
4. **force-warn** → come `warn`, ma il livello non può essere cambiato;
5. **deny** → produce un errore;
6. **forbid** → come `deny`, ma il livello non può essere cambiato.

Ogni lint ha un livello di default, e il compilatore ha un livello di warning di default.

---

## 87. Che cos'è il livello `expect`?

(COMP06, slide 7) Permette di verificare che un lint specifico venga effettivamente emesso (es. in debugging, o prima di eliminare un lint):

* sopprime il lint atteso se viene effettivamente emesso;
* emette un warning se **non** viene emesso.

```rust
fn main() {
    #[expect(unused_variables)] // outer attribute
    // `unused_variables` lint emitted:
    let unused = "Everyone ignores me"; // prints nothing

    #[expect(unused_variables)] // `unused_variables` lint is not emitted:
    let used = "I'm useful"; // expectation not fulfilled -> warning
    println!("The `used` value is equal to: {:?}", used);
}
```
```text
warning: this lint expectation is unfulfilled
 --> src/main.rs:7:14
  |
7 |     #[expect(unused_variables)]
  |              ^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unfulfilled_lint_expectations)]` on by default
```

---

## 88. Come si configurano i livelli di warning (flag e attributi)?

(COMP06, slide 8–10)

**Via flag del compilatore**: i flag `-A`, `-W`, `--force-warn`, `-D`, `-F` permettono di trasformare uno o più lint nei livelli allow, warning, force-warn, deny, o forbid rispettivamente:

```text
$ rustc lib.rs --crate-type=lib -D missing-docs // usually allow
error: missing documentation for crate
error: missing documentation for a function
error: aborting due to 2 previous errors
```

**Via attributi** (inner attribute a livello di crate):
```rust
#![warn(missing_docs)] // inner attribute
pub fn foo() {}
```

**Attributi multipli e parametro `reason`**: il parametro `reason` è mostrato quando il lint viene emesso:
```rust
#![warn(missing_docs)]
#![deny(unused_variables)]
pub fn foo() {}

use std::path::PathBuf;
pub fn get_path() -> PathBuf {
    #[allow(unused_mut, reason = "this is only modified on some platforms")]
    let mut file_name = PathBuf::from("git");
    #[cfg(target_os = "windows")] // conditional compilation attribute
    file_name.set_extension("exe");
    file_name
}
```

---

## 89. Che cos'è il "capping" dei lint?

(COMP06, slide 11)

```text
rustc --cap-lints LEVEL
```
imposta il "lint cap level": il livello **massimo** per tutti i lint.

```rust
fn main() {
    100u8 << 10; // dovrebbe emettere #[deny(exceeding_bitshifts)]
}
```
```text
$ rustc lib.rs --cap-lints warn
warning: bitshift exceeds the type's number of bits
warning: this expression will panic at run-time
```

Questa funzionalità è usata da Cargo quando compila le dipendenze: passa `--cap-lints allow`, così se hanno warning, non "inquinano" l'output della build.

---

## 90. Che cosa sono i "lint group"?

(COMP06, slide 12) rustc ha il concetto di **lint group**, dove si possono attivare più warning tramite un solo nome. Per esempio, il gruppo `nonstandard-style` imposta insieme `non-camel-case-types`, `non-snake-case`, e `non-upper-case-globals`. Quindi questi sono equivalenti:

```text
$ rustc -D nonstandard-style
$ rustc -D non-camel-case-types -D non-snake-case -D non-upper-case-globals
```

Gruppi principali:
* **warnings**: tutti i lint impostati a emettere warning;
* **deprecated-safe**: lint per funzioni erroneamente marcate `safe` in passato;
* **future-incompatible**: lint che rilevano codice con problemi di compatibilità futura;
* **keyword-idents**: lint che rilevano identificatori che diventeranno parole chiave in edizioni future;
* **nonstandard-style**: violazioni delle convenzioni standard di naming;
* **refining-impl-trait**: rileva il raffinamento dei tipi di ritorno `impl Trait` da parte delle implementazioni di trait;
* **unused**: lint che rilevano cose dichiarate ma non usate, o sintassi in eccesso.

---

## 91. In quali momenti della compilazione vengono eseguiti i lint?

(COMP06, slide 13 — tabella completa)

| Tipo | Momento | Informazione disponibile | Uso tipico |
|---|---|---|---|
| Pre-expansion | Prima della macro expansion | AST grezzo, contesto limitato | compatibilità di edizione e casi sensibili alle macro, come `keyword_idents` |
| Early lint | Dopo macro expansion, prima del lowering | AST risolto, ma tipi non completati | lint puramente sintattici, come `unused_parens` |
| Late lint | Verso la fine dell'analisi sull'HIR | HIR, tipi e semantica più ricca | controlli idiomatici o semantici, come `non_snake_case` o `invalid_value` (valore non inizializzato, richiede i tipi) |
| MIR / inline | Dentro il MIR, borrowck o percorsi di codice specifici | stato specializzato del sottosistema | `arithmetic_overflow`, `unused_mut`, lint complessi future-compat |
| Driver / tool lint | Registrazione esterna, esecuzione nelle stesse fasi di cui sopra | dipende dalla passata registrata | Clippy e strumenti custom via `register_lints` e `rustc_driver` |

I lint girano in diverse fasi di compilazione, a seconda del loro significato. Molti lint sono raggruppati in *passes*, eseguite con un unico visitor; altri sono posizionati dove servono nel codice.

---

## 92. Che cos'è Clippy?

(COMP06, slide 14)

* **Clippy** è il linter ufficiale di Rust: un ampio insieme di analisi statiche aggiuntive ("lint") costruite sopra rustc, per aiutare gli sviluppatori a scrivere codice Rust più idiomatico, corretto, efficiente e manutenibile.
* Concettualmente: **rustc** verifica se il tuo programma è Rust valido; **Clippy** verifica se il tuo Rust è **buon** Rust.
* Clippy si integra direttamente nell'infrastruttura del compilatore, piuttosto che operare come parser/analizzatore separato.
* Clippy usa la stessa architettura di linting di rustc stesso: registra passate di lint personalizzate tramite il compiler driver e le esegue dentro la normale pipeline di linting.

---

## 93. Quali sono le caratteristiche del sistema dei tipi di Rust?

(COMP06, slide 16)

* **Nominale**;
* **Substrutturale** (affine);
* **Algebraic Data Type** (`struct`, `enum`), con **pattern matching**;
* **Generics parametrici** su tipi, costanti (`const` generics) e lifetime;
* **Trait** con funzioni associate, tipi associati e costanti associate;
* `impl Trait` per parametri anonimi e tipi di ritorno astratti;
* **Coercizioni** fortemente ristrette.

Esempio (slide 16):
```rust
struct ArrayRef<'a, T, const N: usize> {
    data: &'a [T; N],
}
```

---

## 94. Quali azioni compone il Type Checking in rustc?

(COMP06, slide 17–19 — tabella completa in tre parti)

**Parte 1**:

| Azione | Scopo |
|---|---|
| Expression checking | Garantire che le operazioni siano type-correct (compatibilità dell'assegnamento, tipi degli operandi degli operatori, tipi di ritorno, consistenza dei rami) |
| Method resolution | Trovare i metodi chiamabili (ricerca in inherent impl, trait impl, catene di autoderef/autoref, validazione del tipo del receiver) |
| Trait obligation checking | Validare le obbligazioni di trait (`T: Clone`, tutte le obbligazioni implicate, clausole `where`, supertrait) — es. `fn f<T: Clone>(x: T) { x.clone(); }` |
| Generic argument correctness | Verificare argomenti di tipo/const/lifetime (arità, vincoli, tipi delle const, well-formedness) — es. `Array::<i32, 4>` |

**Parte 2**:

| Azione | Scopo |
|---|---|
| Coercion checking | Validare le conversioni implicite (`&mut T → &T`, array-a-slice, deref coercion, unsizing coercion) |
| Pattern checking | Verificare match/destrutturazione (validità del costruttore, tipi dei binding, supporto all'esaustività, consistenza delle varianti enum) — es. `match x { Some(v) => ..., None => ... }` |
| Signature checking | Validare le interfacce di funzioni/closure (tipi dei parametri, tipi di ritorno, consistenza dell'ABI, trait di chiamata delle closure `Fn`, `FnMut`, `FnOnce`) |
| Operator resolution | Tipizzazione degli operatori basata su trait — es. `a + b` diventa `Add::add(a, b)` (esistenza del trait, compatibilità degli operandi, tipo del risultato) |

**Parte 3**:

| Azione | Scopo |
|---|---|
| Autoderef/autoref | Inserire ref/deref impliciti (legalità della catena di deref, inserimento del borrow, correttezza della mutabilità) — es. `x.len()` può diventare `(*(*x)).len()` |
| Well-formedness checking | Garantire che i tipi siano legali (bound, legalità ricorsiva, regole di varianza, sizedness, precondizioni di object safety) — es. `struct S<T: Copy> { x: T }` |
| ADT construction checking | Validare enum/struct (esistenza del campo, visibilità, tipi dei campi, arità) — es. `Some(3)` o `Point{x:1,y:2}` |

---

## 95. Che cos'è il Type Inference in rustc, in generale?

(COMP06, slide 20) L'inferenza dei tipi in Rust è un sistema di generazione di vincoli + risoluzione di vincoli **multi-dominio**, su:

* tipi;
* lifetime (regioni);
* obbligazioni di trait;
* projections;
* const generics.

L'inferenza dei tipi è basata sull'algoritmo standard di **Hindley-Milner (HM)**, esteso in vari modi per accomodare subtyping, region inference, e tipi *higher-ranked*.

---

## 96. Tabella completa delle azioni di inferenza dei tipi

(COMP06, slide 21–23 — tre tabelle)

**Parte 1**:

| Azione di inferenza | Scopo | Esempio | Vincolo |
|---|---|---|---|
| Local variable inference | Inferire il tipo delle variabili | `let x = 3;` | `x: ?T1` (fresca), `?T1 = IntVar` (dal 3), `IntVar = i32` (fallback); `IntVar → i32`, `FloatVar → f64` |
| Return type inference | Inferire il tipo di risultato della funzione | `fn f() { 3 }` | `return_type = body_type` |
| Generic argument inference | Inferire i parametri generici | `let v = Vec::new(); v.push(3);` | `v: Vec<?T1>`, `?T1 = i32` (dalla chiamata al metodo), `v: Vec<i32>` |
| Closure parameter and result inference | Inferire parametri/risultati della closure | `let f = \|x\| x + 1;` | `x: ?T1`, `result: ?T2`, `?T1: Add<i32>` (overloading), `Add::Output(?T1, i32) = ?T2`, tipicamente `?T1 = i32`, `?T2 = i32` |

**Parte 2**:

| Azione di inferenza | Scopo | Esempio | Vincolo |
|---|---|---|---|
| Method receiver inference | Inferire la struttura del receiver | `x.push(3)` | `x: ?T1` (fresca), `?T1 = Vec<?T2>` (method lookup), `?T2 = i32` (argomento), `?T1 = Vec<i32>` |
| Reference inference | Inferire il tipo del borrow | `let r = &x;` (con `x: i32`) | `r: &'?R i32`, `'?R` fresca, `region(x) ⊇ '?R` — `x` deve outlive il borrow |
| Lifetime inference | Inferire l'estensione della regione | `let r = &x; println!("{}", r);` | `borrow_point ∈ '?R`, `use_point ∈ '?R` |
| Reborrow inference | Restringere i borrow annidati | `let y = &*x;` (con `x: &'a mut i32`) | `y: &'?R i32`, `'?R ⊆ 'a` — il reborrow non può outlive il borrow originale |

**Parte 3**:

| Azione di inferenza | Scopo | Esempio | Vincolo |
|---|---|---|---|
| Trait obligation inference | Inferire i trait richiesti | `x.clone()` | `x: ?T1`, `?T: Clone` |
| Associated type inference | Risolvere le projections | `Iterator::Item` | se `?T1: Iterator`, allora `<?T1 as Iterator>::Item = ?T2` |
| Branch unification (match-arm) | Unificare i tipi dei rami | `let y = if cond {3} else {4};` | `arm1_type = ?T`, `arm2_type = ?T` |
| Array inference | Inferire tipo/lunghezza degli elementi | `let a = [1,2,3];` | `a: [i32; 3]`, tutti gli elementi dello stesso tipo, lunghezza fissa |
| Higher-ranked lifetime (HRTB) inference | Inferire lifetime higher-ranked | `for<'a> fn(&'a i32)` | variabili di regione bound, universi, regioni placeholder: `∀'a. valid(fn(&'a i32))` |
| Subtyping/outlives inference | Inferire il contenimento fra lifetime | `let x: &'static i32 = y;` | `y: &'?R i32`, `'?R : 'static` |

**Tabella dei vincoli di tipo generati** (slide 24):

| Tipo di vincolo | Significato |
|---|---|
| Equality | `?T = i32` |
| Subtyping | `'a: 'b` |
| Trait obligations | `?T: Clone` |
| Projection equality | `<T as Trait>::Assoc = U` |
| Region containment | `'?R ⊆ 'a` |
| Const equality | `?N = 4` |

---

## 97. Perché il MIR type check viene eseguito dopo la move analysis?

(COMP06, slide 26)

* Rust esegue il MIR type check **dopo** la move analysis perché il type checker del MIR necessita di informazioni prodotte dalla move analysis.
* Il suo scopo principale, dentro il borrow checking, è generare vincoli precisi di regione/lifetime, e quei vincoli dipendono dal sapere:
  - quali place sono ancora inizializzate;
  - quali move sono avvenuti;
  - quali path sono legali da cui muovere;
  - quali locali/place sono effettivamente rilevanti per l'analisi di borrow.
* L'ordinamento è quindi guidato dalle dipendenze fra le analisi.

---

## 98. Quali algoritmi di inferenza dei tipi esistono, oltre ad Algorithm W?

(COMP06, slide 27) Sistema di riferimento: **Hindley-Milner**. **Algorithm W** è il più usato, ma non l'unico:

* è buono per linguaggi puri, con effetti collaterali limitati a nuove variabili;
* **Algorithm J**: usa più effetti collaterali, più efficiente;
* **Lazy unification**: raccoglie tutti i vincoli visitando l'AST, poi applica l'unificazione.

---

## 99. Che cos'è la First-Order Unification (definizione formale)?

(COMP06, slide 28) Dato un insieme finito $G = \{s_1 \doteq t_1, \ldots, s_n \doteq t_n\}$ di potenziali equazioni, l'algoritmo applica regole per trasformarlo in una **sostituzione**, cioè un insieme equivalente di equazioni della forma $\{x_1 \doteq u_1, \ldots, x_m \doteq u_m\}$ dove $x_1, \ldots, x_m$ sono variabili distinte e $u_1, \ldots, u_m$ sono termini che non contengono nessuna delle $x_i$.

* Se non c'è soluzione, l'algoritmo termina con $\bot$.
* $G\{x \mapsto t\}$ denota l'operazione di sostituire tutte le occorrenze della variabile $x$ nel problema $G$ con il termine $t$.
* I simboli costanti sono considerati simboli di funzione con arità zero.

---

## 100. Che cos'è l'algoritmo di Martelli–Montanari?

(COMP06, slide 29) L'algoritmo di **Martelli–Montanari (1976–82)** calcola il **most general unifier**, cioè una sostituzione $S$ tale che $S(s_i) = S(t_i)$ per ogni $s_i \doteq t_i$ in $G$. Se non c'è soluzione, l'algoritmo termina con $\bot$.

> Nota didattica di raccordo (già presente nel materiale di `LinguaggiI.pdf` per la parte di parsing/unificazione generale): le regole di trasformazione classiche di Martelli-Montanari includono *delete* ($t \doteq t \Rightarrow \emptyset$), *decompose* ($f(s_1,\ldots,s_n) \doteq f(t_1,\ldots,t_n) \Rightarrow \{s_1 \doteq t_1, \ldots, s_n \doteq t_n\}$), *conflict* (simboli di testa diversi $\Rightarrow \bot$), *swap* ($t \doteq x \Rightarrow x \doteq t$ se $t$ non è una variabile), e *eliminate/occur-check* ($x \doteq t \Rightarrow$ sostituzione, purché $x$ non occorra in $t$, altrimenti $\bot$).

---

## 101. Quali altri filoni di ricerca collegati a Rust sono citati nel corso?

(COMP06, slide 30–33)

* **Semantica formale del linguaggio: RustBelt** (https://plv.mpi-sws.org/rustbelt/popl18/). RustBelt fornisce la prima prova formale (e verificata meccanicamente) di sicurezza per un linguaggio che rappresenta un sottoinsieme realistico di Rust. Motivazione: nessuna delle garanzie di sicurezza di Rust era stata formalmente dimostrata, e Rust estende il potere espressivo del suo type system ownership-based tramite librerie che internamente usano funzionalità `unsafe`. Il lavoro fornisce una prova estensibile: per ogni nuova libreria Rust che usa funzionalità `unsafe`, si può stabilire quale condizione di verifica deve soddisfare per essere considerata un'estensione sicura del linguaggio; questa verifica è stata condotta per alcune delle librerie più importanti usate nell'ecosistema Rust.

* **Polonius: una formulazione alias-based del borrow checker** (https://smallcultfollowing.com/babysteps/blog/2018/04/27/an-alias-based-formulation-of-the-borrow-checker/). È un'estensione conservativa del borrow checker NLL, in cui **le regioni sono insiemi di *loan*** (non più insiemi di punti del programma). Il cambio concettuale principale: per un tipo come `&'a i32`, il significato di `'a` cambia — nel sistema NLL descritto nella RFC, una lifetime corrispondeva in ultima analisi a una porzione del programma sorgente o del control-flow graph; in questa proposta, una **region** corrisponde invece a un insieme di *loan* — cioè un insieme di espressioni di borrow, come `&x` o `&mut v`. L'idea è che se un riferimento `r` ha tipo `&'a i32`, invalidare i termini di uno qualsiasi dei loan in `'a` invaliderebbe `r`.

* **Studio empirico dei bug in rustc**: *"An Empirical Study of Rust-Specific Bugs in the rustc Compiler"* (J. ACM, Vol. 37, No. 4, Agosto 2025). Studio dei bug di rustc dovuti a caratteristiche specifiche di Rust, incluse la risoluzione dei trait, il borrow checking, e ottimizzazioni specifiche. Basato su issue e fix riportati fra il 2022 e il 2024, con una revisione manuale di **301 issue valide**. Risultati principali:
  1. i bug di rustc nascono principalmente dal sistema dei tipi di Rust e dal modello delle lifetime, con errori frequenti nei moduli HIR e MIR a causa di checker e ottimizzazioni complesse;
  2. i test case che rivelano bug coinvolgono spesso feature instabili, usi avanzati di trait, annotazioni di lifetime, API standard, e specifici livelli di ottimizzazione;
  3. sia programmi validi sia invalidi possono innescare bug, e gli strumenti di test esistenti faticano a rilevare errori non-crash, sottolineando la necessità di ulteriori progressi nel testing di rustc.

---

## 102. Che cos'è uHaskell e a cosa serve nel corso?

(COMP06, slide 34) **uHaskell** è un sottoinsieme di Haskell usato per spiegare l'inferenza dei tipi. Sia Haskell sia ML hanno *overloading*, ma per semplicità l'overloading non viene considerato in questi esempi.

Grammatica di uHaskell (slide 34):
```text
<decl> ::= <name> <pat> = <exp>
<pat>  ::= Id | (<pat>, <pat>) | <pat> : <pat> | []
<exp>  ::= Int | Bool | [] | Id | (<exp>)
         | <exp> <op> <exp>
         | <exp> <exp> | (<exp>, <exp>)
         | if <exp> then <exp> else <exp>
```

---

## 103. Qual è l'idea di base dell'inferenza dei tipi (esempio introduttivo)?

(COMP06, slide 35)

```haskell
f x = 2 + x -- a simple declaration
> f :: Int -> Int
```

Ragionamento: `+` ha tipo `Int -> Int -> Int` (con overloading sarebbe `Num a => a -> a -> a`); `2` ha tipo `Int`. Poiché si applica `+` a `x`, serve `x :: Int`. Quindi `f x = 2 + x` ha tipo `Int -> Int`.

---

## 104. Qual è l'algoritmo generale di inferenza dei tipi in uHaskell?

(COMP06, slide 36)

1. Effettuare il parsing del programma per costruire il **parse tree**.
2. Assegnare **variabili di tipo** ai nodi dell'albero.
3. Generare i **vincoli**:
   * dall'ambiente: costanti (`2`), operatori built-in (`+`), funzioni note (`tail`);
   * dalla forma del parse tree: es. nodi di applicazione e astrazione.
4. Risolvere i vincoli tramite **unificazione**.
5. Determinare i tipi delle dichiarazioni top-level.

---

## 105. Esempio completo svolto 1: `f x = 2 + x`

(COMP06, slide 37–43)

**Passo 1 — Parse**: il testo del programma viene analizzato per costruire il parse tree di `f x = 2 + x`; i nodi binari `@` rappresentano l'applicazione, un nodo ternario `Fun` rappresenta la definizione di funzione. Gli operatori infissi sono convertiti in applicazione di funzione curried durante il parsing: `2 + x` diventa `(+) 2 x`.

**Passo 2 — Assegnazione delle variabili di tipo**: le variabili ricevono lo stesso tipo della loro occorrenza di binding.

**Passo 3 — Vincoli dai nodi di applicazione**: per l'applicazione (di `f` a `x`):
* il tipo di `f` (`t_0` nella figura) deve essere dominio → codominio;
* il dominio di `f` deve essere il tipo dell'argomento `x` (`t_1`);
* il codominio di `f` deve essere il risultato dell'applicazione (`t_2`);
* vincolo: `t_0 = t_1 -> t_2`.

**Vincoli dalle astrazioni** (dichiarazione di funzione `f x = e`):
* il tipo di `f` (`t_0`) deve essere dominio → codominio;
* il dominio è il tipo della variabile astratta `x` (`t_1`);
* il codominio è il tipo del corpo della funzione `e` (`t_2`);
* vincolo: `t_0 = t_1 -> t_2`.

**Passo 3 (completo) — Insieme dei vincoli per `f x = 2 + x`**:
```text
t_0 = t_1 -> t_6
t_4 = t_1 -> t_6
t_2 = t_3 -> t_4
t_2 = Int -> Int -> Int
t_3 = Int
```

**Passo 4 — Risoluzione tramite unificazione** (traccia passo-passo dalle slide):
```text
t_3 -> t_4 = Int -> (Int -> Int)   [da t_2 = Int -> Int -> Int e t_2 = t_3 -> t_4]
  ⇒ t_3 = Int                        (già noto)
  ⇒ t_4 = Int -> Int

t_1 -> t_6 = Int -> Int             [da t_4 = t_1 -> t_6 e t_4 = Int -> Int]
  ⇒ t_1 = Int
  ⇒ t_6 = Int

t_0 = t_1 -> t_6 = Int -> Int
```

**Passo 5 — Tipo finale della dichiarazione**:
```text
t_0 = Int -> Int
t_1 = Int
t_6 = Int
t_4 = Int -> Int
t_2 = Int -> Int -> Int
t_3 = Int

f x = 2 + x
> f :: Int -> Int
```

---

## 106. Esempio completo svolto 2 (tipi polimorfi): `f g = g 2`

(COMP06, slide 44–48)

```haskell
f g = g 2
> f :: (Int -> t_4) -> t_4
```

**Passo 1** — Costruzione del parse tree.
**Passo 2** — Assegnazione delle variabili di tipo.
**Passo 3** — Generazione dei vincoli:
```text
t_0 = t_1 -> t_4
t_1 = t_3 -> t_4
t_3 = Int
```

**Passo 4** — Risoluzione dei vincoli:
```text
t_0 = (Int -> t_4) -> t_4
t_1 = Int -> t_4
t_3 = Int
```

**Passo 5** — Determinazione del tipo della dichiarazione top-level: le variabili di tipo **non vincolate** diventano **tipi polimorfi**:
```text
f g = g 2
> f :: (Int -> t_4) -> t_4
```

**Uso di funzioni polimorfe** (slide 49): possibili applicazioni:
```haskell
add x = 2 + x
> add :: Int -> Int
f add
> 4 :: Int

isEven x = mod (x, 2) == 0
> isEven :: Int -> Bool
f isEven
> True :: Bool
```
(qui `t_4` viene istanziato a `Int` nel primo caso e a `Bool` nel secondo, mostrando il polimorfismo di `f`.)

---

## 107. Esempio completo svolto 3 (tipi dati/ricorsione): `length (x:rest) = 1 + (length rest)`

(COMP06, slide 50–54)

Premessa (slide 50): le funzioni possono avere clausole multiple. Per l'inferenza dei tipi:
* si inferisce un tipo separato per ciascuna clausola;
* si combinano aggiungendo il vincolo che tutte le clausole abbiano lo **stesso tipo**;
* per le chiamate ricorsive: la funzione ha lo stesso tipo della propria definizione.

```haskell
length [] = 0
length (x:rest) = 1 + (length rest)
```

**Passo 1** — Costruzione del parse tree per la seconda clausola `length (x:rest) = 1 + (length rest)`.
**Passo 2** — Assegnazione delle variabili di tipo ai nodi.
**Passo 3** — Generazione dei vincoli:
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

**Passo 4** — Risoluzione dei vincoli:
```text
t_0 = [t_1] -> Int
```

(qui `t_3 = [t_1]` rappresenta il tipo lista di `x:rest`, e la catena di unificazioni porta a concludere che `length` ha tipo `[t_1] -> Int`, cioè `length :: [a] -> Int`, coerentemente con la prima clausola `length [] = 0`.)

# PARTE VIII — Domande trasversali "da professore" e sintesi finale

## 108. Perché non fare direttamente il borrow checking sull'AST?

Perché l'AST rappresenta principalmente la sintassi. Il borrow checker deve invece conoscere controllo di flusso, temporanei, moves, borrows, drops, places, punti del programma. Il MIR esplicita queste informazioni e riduce enormemente la complessità del problema (cfr. COMP01 slide 22 e COMP03 slide 5).

## 109. Perché non fare direttamente il borrow checking sull'LLVM IR?

Perché LLVM IR è troppo basso livello e ha già perso molti concetti semantici di Rust. Il borrow checker deve ragionare su ownership, borrowing, places, moves, partial moves, regions, drops — concetti che devono essere verificati **prima** di arrivare a LLVM (COMP01 slide 15).

## 110. Perché il MIR non contiene semplicemente il codice Rust originale?

Perché il suo scopo non è rappresentare fedelmente la sintassi, ma una forma più vicina al comportamento operativo: espressioni annidate → temporanei → basic block → terminator → places/operand. Questo rende possibili analisi precise come borrow checking e dataflow (COMP01 slide 22, 27).

## 111. Perché il borrow checker può essere considerato una dataflow analysis?

Perché calcola informazioni associate ai punti del CFG e le propaga lungo gli archi: path inizializzati, borrow attivi, variabili vive, regioni. Le informazioni vengono combinate e propagate fino a un punto fisso (COMP03 slide 6, 36–38).

## 112. Perché il compilatore deve fare sia Move Analysis sia Region Inference?

Sono due aspetti diversi della sicurezza: la Move Analysis determina "il valore esiste ancora?", la Region Inference determina "la reference è ancora valida?". Esempio (COMP04 slide 38):

```rust
let x = vec![1];
let r = &x;
drop(x);
*r; // error
```

La regione può indicare che `r` dovrebbe essere ancora valida, ma la Move Analysis segnala che `x` è stato mosso/distrutto. La combinazione delle due informazioni permette di riconoscere l'errore.

## 113. Perché il borrow checker deve conoscere i Drop?

Perché la distruzione di un valore modifica lo stato di ownership e può invalidare reference e path; inoltre un valore può essere parzialmente inizializzato o parzialmente mosso. Il compilatore deve sapere esattamente quali parti devono essere distrutte e quando — da qui l'importanza di drop obligations, drop flag e drop elaboration (COMP02 slide 28–32).

## 114. Che cosa sopravvive passando da MIR a LLVM IR?

A livello generale sopravvivono le informazioni necessarie all'esecuzione: control flow, calls, load, store, arithmetic, layout, funzioni monomorfizzate. Ownership e lifetime non diventano valori runtime: sono strumenti usati per verificare la correttezza del programma prima del code generation (COMP02 slide 5).

---

# PARTE IX — Le domande essenziali (checklist di ripasso rapido)

Se il tempo per prepararsi è limitato, in ordine di priorità:

1. Perché Rust necessita di HIR, THIR e MIR invece di usare direttamente LLVM IR? (COMP01)
2. Qual è la pipeline AST → HIR → THIR → MIR → LLVM? (COMP01)
3. Perché il borrow checker lavora sul MIR? (COMP03)
4. Che cos'è il MIR e quali sono le sue componenti principali (basic block, statement, terminator, place, rvalue, operand)? (COMP01, COMP02)
5. Che differenza c'è fra Place, Operand e Rvalue? (COMP02)
6. Che cos'è il desugaring e perché è importante per il borrow checker? (COMP02)
7. Come viene desugarato `for`, `?`, una method call, una closure? (COMP02)
8. Come funzionano le query MIR (`mir_built`, `mir_const`, `mir_promoted`, `mir_drops_elaborated_and_const_checked`, `optimized_mir`)? (COMP02)
9. Che cos'è una dataflow analysis in rustc (trait `Analysis`, effect, `iterate_to_fixpoint`)? (COMP02)
10. Come funziona la Move Analysis con GEN/KILL, ed esempi field-sensitive? (COMP03)
11. Che cosa sono i move path e perché servono per i partial move? (COMP03)
12. Perché esiste la Drop Elaboration e cosa sono i drop flag/le 4 categorie di drop? (COMP02)
13. Qual è la differenza fra lifetime e region? (COMP03)
14. Come funziona la Region Inference / NLL (universal regions, SCC, outlives, type test)? (COMP03, COMP04)
15. Come interagiscono Move Analysis e Region Inference nel borrow checker? (COMP03, COMP04)
16. Che cosa sono i Two-Phase Borrows e a cosa servono (`vec.push(vec.len())`)? (COMP04)
17. Come funziona la Closure Capture Inference (upvar, `ExprUseVisitor`, `Delegate`, `Fn`/`FnMut`/`FnOnce`)? (COMP04)
18. Che cos'è la monomorfizzazione, come si differenzia da type erasure/dictionary passing/reified generics? (COMP05)
19. Come funzionano Mono Item Collection e Codegen Units (trade-off incrementalità/inlining)? (COMP05)
20. Quali sono i livelli e i gruppi di lint, e quando girano (pre-expansion/early/late/MIR)? (COMP06)
21. Come funziona l'inferenza dei tipi in rustc (HM esteso, vincoli, tabella delle azioni)? (COMP06)
22. Che cos'è l'unificazione di Martelli-Montanari? (COMP06)
23. Sai svolgere un'inferenza di tipo in uHaskell passo-passo (parse tree → variabili di tipo → vincoli → unificazione → tipo finale), anche nel caso polimorfo? (COMP06)

---

# PARTE X — La risposta "perfetta" alla domanda generale

### "Mi descriva come rustc verifica la sicurezza della memoria, dalla sintassi al codice macchina."

> Rust garantisce la memory safety principalmente attraverso ownership, borrowing e lifetime, che non sono meccanismi runtime ma proprietà verificate staticamente dal compilatore. Rust punta a prestazioni comparabili a C, senza garbage collector, tramite un sistema di tipi avanzato basato su RAII.
>
> Per effettuare queste verifiche rustc non lavora direttamente sull'AST né sull'LLVM IR, che è troppo basso livello per esprimere concetti come places, projections, moves parziali, region/lifetime constraint e semantica dei drop. Dopo parsing (un recursive descent parser), macro expansion e name resolution, il programma viene abbassato in HIR e poi THIR, dove vengono rese esplicite molte informazioni type-dependent (autoref, autoderef, coercions, chiamate overloaded, e — cosa importante — l'inferenza della modalità di cattura delle closure).
>
> Il THIR viene quindi abbassato nel MIR, una rappresentazione tipata basata su un control-flow graph, con basic block, statement, terminator, temporanei e Place. Questo abbassamento comporta un desugaring radicale (for-loop, operatore `?`, `if let`/`while let`, indicizzazione, closure) che rimuove ogni annidamento di espressioni. Il MIR è particolarmente adatto al borrow checking perché rende espliciti controllo di flusso, moves e drop, ed è la base su cui rustc esegue anche numerose dataflow analysis generiche (tramite il trait `Analysis`, gli "effect" e l'iterazione a punto fisso), oltre alla drop elaboration, che trasforma i terminator `Drop`/`DropAndReplace` imprecisi in drop condizionati da drop flag booleani, classificandoli come Static, Dead, Conditional o Open.
>
> Il borrow checker, invocato tramite la query `mir_borrowck`, lavora su una copia del MIR e attraversa otto fasi: preparazione del MIR, sostituzione delle lifetime con variabili di regione fresche (`replace_regions_in_mir`), dataflow di move/inizializzazione (a livello di "move path" gerarchici, per gestire i partial move), un secondo type check a livello di MIR che genera outlives e liveness constraint e type test, la region inference vera e propria (che collassa i cicli del grafo delle outlives constraint in componenti fortemente connesse per ottenere un DAG, e propaga le regioni per unione fino al punto fisso, verificando poi i type test e la coerenza delle universal regions), il calcolo dei borrow attivi in ciascun punto (inclusi i two-phase borrow, che permettono pattern come `v.push(v.len())`), e infine una validazione finale che incrocia inizializzazione, regole di borrowing e mutabilità.
>
> Dopo la verifica, il MIR — ancora generico — viene ottimizzato (constant propagation, dead-code elimination, copy propagation, inlining) mentre è ancora condiviso da tutte le istanziazioni concrete. Solo in seguito interviene la monomorfizzazione: il monomorphization collector individua tutte le istanze concrete necessarie (a partire dagli item pubblici come radici, attraversando ricorsivamente il MIR), che vengono partizionate in Codegen Unit bilanciando ricompilazione incrementale e possibilità di inlining. Ogni istanza viene infine abbassata a una IR di backend — tipicamente LLVM IR, ma anche Cranelift o GCC — dove ownership e lifetime non sopravvivono come valori runtime: hanno già svolto il loro compito di validazione.
>
> In questo modo Rust riesce a garantire proprietà di sicurezza della memoria principalmente a compile time, senza introdurre un garbage collector e mantenendo prestazioni vicine a quelle dei linguaggi system-level.

---

# PARTE XI — Schema mentale finale (completo)

```text
                          RUST SOURCE
                               │
                          rustc-lexer / rustc-parse
                        (recursive descent parser)
                               │
                              AST
                               │
                 macro expansion + name resolution
                               │
                              HIR  ── (early desugaring: for, ecc.)
                               │
                        typed lowering
                               │
                             THIR  ── (late desugaring: method call,
                               │        autoref/deref, operatori, closure)
                     MIR construction (mir_built)
                               │
                              MIR  (CFG tipato: basic block, statement,
                               │    terminator, places, rvalues, operands)
              ┌────────────────┼─────────────────────┐
              │                │                      │
     mir_const/mir_promoted    │              MIR Dataflow Framework
     (promotion, prep.)        │           (trait Analysis, effect,
              │                │            iterate_to_fixpoint)
              └───────┬────────┘
                      ▼
              mir_borrowck (8 fasi)
        ┌─────────────┴─────────────┐
        │                           │
   Move / Init Analysis      Region Inference (NLL)
   (move path, GEN/KILL,     (universal regions, SCC/DAG,
   partial moves)            outlives + liveness constraints,
        │                    type tests)
        └─────────────┬─────────────┘
                       ▼
             Borrow sets + Final Validation
             (two-phase borrows, closure capture)
                       │
                       ▼
             Drop Elaboration (drop flags,
             Static/Dead/Conditional/Open)
                       │
                       ▼
             MIR Optimization (generico:
             const/copy propagation, DCE, inlining)
                       │
                       ▼
        Monomorphization Collector + Codegen Units
             (grafo dei mono item, partizionamento)
                       │
                       ▼
          Lowering a Codegen IR (LLVM / Cranelift / GCC)
                       │
                       ▼
                   MACHINE CODE
```

La frase chiave da ricordare:

> **Il MIR è il punto in cui la sintassi Rust è stata sufficientemente abbassata da permettere al compilatore di trattare ownership, moves, borrows, drops e lifetime come proprietà analizzabili — con le stesse tecniche classiche di dataflow, CFG e punto fisso — sul control-flow graph.**
