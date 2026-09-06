# Preparazione all'esame orale — CT_Project

> Repository di riferimento: https://github.com/Muxy03/CT_Project  
> Obiettivo: raccogliere in un unico documento le principali domande da orale e risposte modello sul progetto.

---

# Indice

1. Visione generale del progetto
2. Architettura generale
3. MiniImp
   - Lexer
   - Parser e precedenza
   - AST
   - CFG
   - Data-flow analysis
   - Liveness
   - Reaching Definitions
   - Ottimizzazioni
   - Generazione LLVM
4. MiniFun
   - Interprete ed environment
   - Closure e lexical scoping
   - Funzioni ricorsive
   - Type checking con annotazioni
   - Algorithm W
   - Unificazione
   - Occurs check
   - Let-polymorphism
5. Domande trasversali e insidiose
6. Risposta introduttiva consigliata

---

# 1. Visione generale del progetto

## Domanda: Mi descriva il progetto nel suo complesso.

### Risposta

Il progetto è composto da due linguaggi implementati in OCaml: **MiniImp** e **MiniFun**.

MiniImp è un linguaggio imperativo. La sua pipeline comprende:

```text
Codice sorgente
    ↓
Lexer
    ↓
Parser
    ↓
AST
    ↓
Control Flow Graph
    ↓
Data-flow analysis
    ↓
Ottimizzazioni
    ↓
Generazione LLVM IR
    ↓
Compilazione in codice nativo
```

MiniFun è invece un linguaggio funzionale. Per MiniFun vengono affrontati sia l'aspetto dinamico sia quello statico:

```text
Codice sorgente
    ↓
Lexer
    ↓
Parser
    ↓
AST
    ↓
Type checking / Type inference
    ↓
Interpreter
```

In particolare, MiniFun utilizza closure per implementare lo scoping lessicale e comprende sia un type checker con annotazioni esplicite sia un sistema di inferenza dei tipi basato sull'Algorithm W.

---

## Domanda: Qual è la principale differenza tra MiniImp e MiniFun?

### Risposta

MiniImp è un linguaggio imperativo, quindi il programma è principalmente descritto come una sequenza di istruzioni che modificano uno stato.

MiniFun è invece un linguaggio funzionale, nel quale le funzioni sono valori di prima classe e la semantica dell'esecuzione richiede una gestione esplicita degli environment e delle closure.

Dal punto di vista del progetto, MiniImp permette di affrontare soprattutto tecniche tipiche dei compilatori, come CFG, data-flow analysis, ottimizzazioni e generazione di codice. MiniFun permette invece di affrontare concetti come scoping lessicale, closure, ricorsione e sistemi di tipo.

---

# 2. Architettura generale

## Domanda: Perché utilizzare una pipeline lexer → parser → AST?

### Risposta

Questa separazione permette di distinguere chiaramente le diverse responsabilità.

Il lexer trasforma il flusso di caratteri in token.

Il parser verifica che la sequenza di token rispetti la grammatica e costruisce una rappresentazione strutturata del programma.

L'AST elimina i dettagli puramente sintattici e rappresenta direttamente la struttura semantica del programma.

Questa separazione rende più semplice aggiungere successivamente interpreti, type checker, CFG, ottimizzazioni o generatori di codice, perché tutti lavorano su una rappresentazione intermedia ben definita.

---

## Domanda: Perché utilizzare un AST invece di lavorare direttamente sui token?

### Risposta

I token rappresentano ancora una sequenza lineare. Molte operazioni del compilatore richiedono invece di conoscere la struttura gerarchica del programma.

Per esempio, nell'espressione:

```text
a + b * c
```

l'AST rappresenta esplicitamente che la moltiplicazione è un sottoalbero dell'addizione:

```text
      +
     / \
    a   *
       / \
      b   c
```

Questa struttura permette di interpretare, controllare i tipi o generare codice in modo naturale e ricorsivo.

---

# 3. MiniImp — Lexer

## Domanda: Che cosa fa il lexer?

### Risposta

Il lexer riceve il codice sorgente come sequenza di caratteri e lo trasforma in una sequenza di token.

Un token rappresenta una categoria lessicale significativa, come:

- identificatori;
- numeri;
- parole chiave;
- operatori;
- delimitatori;
- parentesi.

Il parser non lavora quindi direttamente sui caratteri, ma su una sequenza più astratta e più facile da elaborare.

---

## Domanda: Perché implementare un lexer manuale?

### Risposta

Un lexer manuale offre controllo diretto sul processo di scansione del sorgente e sulla gestione dei token e degli errori.

In un linguaggio relativamente piccolo, un lexer hand-written può essere semplice da mantenere e permette di gestire in modo esplicito il look-ahead necessario per distinguere token che condividono prefissi.

Per esempio, operatori composti possono richiedere di leggere un carattere aggiuntivo per determinare il token corretto.

---

## Domanda: Che cos'è il look-ahead?

### Risposta

Il look-ahead consiste nel leggere uno o più caratteri successivi prima di decidere definitivamente quale token riconoscere.

È necessario quando due token hanno un prefisso comune.

Per esempio, se un linguaggio contiene sia un operatore formato da un carattere sia un operatore formato da due caratteri con lo stesso primo simbolo, il lexer deve guardare il carattere successivo.

---

# 4. MiniImp — Parser e precedenza

## Domanda: Che tipo di parser è stato utilizzato?

### Risposta

Il parser è un parser **recursive descent**.

La grammatica viene implementata tramite funzioni ricorsive, dove ogni funzione riconosce una determinata categoria sintattica.

Questo approccio è particolarmente adatto a grammatiche semplici e permette di controllare direttamente il parsing e la costruzione dell'AST.

---

## Domanda: Come viene gestita la precedenza degli operatori?

### Risposta

La precedenza viene rappresentata strutturalmente nel parser.

I diversi livelli di precedenza vengono gestiti da funzioni diverse. Un livello con precedenza più bassa chiama quello con precedenza immediatamente più alta.

Concettualmente:

```text
espressione logica
    ↓
confronto
    ↓
somma / sottrazione
    ↓
moltiplicazione
    ↓
operatori unari
    ↓
atomi
```

In questo modo la struttura dell'AST riflette automaticamente la precedenza.

---

## Domanda: Perché gli operatori associativi a sinistra vengono spesso implementati con un ciclo?

### Risposta

Una grammatica left-recursive non è direttamente adatta a un parser recursive descent.

Una regola come:

```text
E → E + T | T
```

porterebbe il parser a richiamare immediatamente `E` senza consumare input, causando ricorsione infinita.

L'associatività a sinistra viene quindi implementata consumando il primo operando e poi, tramite un ciclo, tutte le successive coppie operatore-operando.

Per esempio:

```text
a - b - c
```

viene costruito come:

```text
(a - b) - c
```

---

## Domanda: Come può essere rappresentato il meno unario senza introdurre un nodo AST dedicato?

### Risposta

Il meno unario:

```text
-e
```

può essere trasformato durante il parsing in:

```text
0 - e
```

Questo processo è una forma di **desugaring**.

Il vantaggio è che le fasi successive devono gestire un numero minore di costrutti distinti.

---

## Domanda: Che cos'è il desugaring?

### Risposta

Il desugaring consiste nel trasformare una costruzione sintattica più comoda o più ricca in una costruzione più semplice ma semanticamente equivalente.

L'obiettivo è semplificare le fasi successive, riducendo il numero di casi che interprete, type checker o generatore di codice devono trattare.

---

# 5. MiniImp — Control Flow Graph

## Domanda: Che cos'è un Control Flow Graph?

### Risposta

Un Control Flow Graph, o CFG, è un grafo orientato che rappresenta i possibili flussi di esecuzione di un programma.

I nodi rappresentano istruzioni o blocchi di istruzioni.

Gli archi rappresentano le possibili transizioni del controllo.

È una rappresentazione fondamentale per le analisi di flusso dei dati e per molte ottimizzazioni.

---

## Domanda: Perché il CFG è necessario?

### Risposta

L'ordine testuale delle istruzioni non è sufficiente per comprendere il comportamento di un programma che contiene `if`, `while` o altre costruzioni di controllo.

Il CFG rende espliciti:

- i rami;
- i punti di join;
- i cicli;
- i predecessori;
- i successori.

Queste informazioni sono necessarie per determinare, per esempio, quali definizioni possono raggiungere un punto del programma oppure quali variabili saranno utilizzate in futuro.

---

## Domanda: Perché utilizzare blocchi minimi?

### Risposta

Una possibile scelta progettuale è utilizzare blocchi minimi, cioè rappresentare un'istruzione o una condizione per nodo.

Il vantaggio principale è la precisione delle analisi.

Le informazioni di data-flow sono associate direttamente alle singole istruzioni, senza dover modellare ulteriormente ciò che avviene all'interno di un basic block più grande.

Questa scelta semplifica inoltre il collegamento concettuale tra nodi del CFG e blocchi della successiva generazione di codice.

Lo svantaggio è avere un CFG con più nodi rispetto a una rappresentazione basata su basic block massimali.

---

## Domanda: Qual è il vantaggio di rappresentare ogni comando tramite una coppia `(entry, exit)`?

### Risposta

L'invariante `(entry, exit)` rende composizionale la costruzione del CFG.

Ogni comando, indipendentemente dalla sua complessità, può essere collegato ad altri comandi usando la stessa interfaccia.

Per una sequenza:

```text
c1;
c2
```

si costruiscono:

```text
build(c1) → (entry1, exit1)
build(c2) → (entry2, exit2)
```

e si aggiunge:

```text
exit1 → entry2
```

Il risultato è:

```text
(entry1, exit2)
```

---

## Domanda: Come viene rappresentato un `if` nel CFG?

### Risposta

Un `if` contiene un nodo condizione dal quale partono due archi:

- uno verso il ramo `then`;
- uno verso il ramo `else`.

I due rami convergono poi in un punto di join.

Concettualmente:

```text
       condizione
       /       \
    then       else
       \       /
        join
```

Il join permette di rappresentare in modo uniforme il punto successivo all'istruzione condizionale.

---

## Domanda: Perché introdurre un nodo di join?

### Risposta

Il nodo di join semplifica la composizione del CFG e permette di mantenere un unico punto di uscita per la costruzione considerata.

Senza un join, il codice successivo dovrebbe essere collegato separatamente agli exit di entrambi i rami.

Con un join, il comando `if` ha un exit unico e può essere trattato come qualunque altro comando.

---

## Domanda: Come viene rappresentato un `while`?

### Risposta

Un `while` contiene un nodo condizione.

Se la condizione è vera, il controllo entra nel body.

Alla fine del body viene aggiunto un **back-edge** verso la condizione.

Se la condizione è falsa, il controllo esce dal ciclo.

```text
        condizione
        /       \
     true       false
      |           |
     body        exit
      |
      └──────────→ condizione
```

---

## Domanda: Che cos'è un back-edge?

### Risposta

Un back-edge è un arco che riporta il flusso di controllo verso una parte precedente del CFG.

Nel caso di un ciclo `while`, l'exit del body viene collegato nuovamente alla condizione.

Questo arco rappresenta la possibilità di eseguire una nuova iterazione.

---

# 6. MiniImp — Data-flow analysis

## Domanda: Che cos'è una data-flow analysis?

### Risposta

Una data-flow analysis calcola informazioni relative al comportamento dei dati nei diversi punti del programma.

Il CFG viene utilizzato per propagare queste informazioni lungo gli archi.

Esempi sono:

- liveness analysis;
- reaching definitions;
- available expressions;
- constant propagation.

Le analisi vengono spesso espresse come equazioni di trasferimento e risolte iterativamente fino a raggiungere un punto fisso.

---

## Domanda: Che cosa significa raggiungere un fixpoint?

### Risposta

Un fixpoint viene raggiunto quando un'ulteriore applicazione delle funzioni di analisi non modifica più le informazioni calcolate.

In presenza di cicli nel CFG, una singola visita dei nodi non è generalmente sufficiente.

È quindi necessario ripetere la propagazione finché gli insiemi o gli altri valori associati ai nodi smettono di cambiare.

---

## Domanda: Perché una singola visita del CFG non è sufficiente?

### Risposta

Nei cicli esistono dipendenze circolari.

L'informazione calcolata per un nodo può dipendere da un nodo che, attraverso un back-edge, dipende a sua volta dal primo.

Di conseguenza l'informazione deve essere propagata ripetutamente fino a stabilizzazione.

---

## Domanda: Che cos'è una worklist?

### Risposta

Una worklist è una struttura che contiene i nodi che devono ancora essere rianalizzati.

Quando l'informazione di un nodo cambia, vengono inseriti nella worklist i nodi che potrebbero essere influenzati da quel cambiamento.

Questo evita di rieseguire inutilmente l'analisi dell'intero CFG a ogni iterazione.

---

# 7. Liveness Analysis

## Domanda: Che cosa significa che una variabile è live?

### Risposta

Una variabile è **live** in un determinato punto del programma se il suo valore corrente potrà essere utilizzato in futuro prima di essere sovrascritto.

In altre parole, il valore attualmente contenuto nella variabile è ancora potenzialmente necessario per una futura computazione.

---

## Domanda: Perché la liveness è una backward analysis?

### Risposta

Per sapere se una variabile è necessaria prima di un'istruzione, bisogna sapere cosa accadrà dopo quell'istruzione.

La liveness dipende quindi dalle esigenze dei successori.

Per questo l'informazione viene propagata concettualmente all'indietro nel CFG.

---

## Domanda: Quali sono le equazioni della liveness analysis?

### Risposta

Per un nodo `n`:

```text
LiveOut[n] = ⋃ LiveIn[s]
             s ∈ successors(n)
```

e:

```text
LiveIn[n] = Use[n] ∪ (LiveOut[n] - Def[n])
```

Il primo insieme raccoglie le variabili necessarie all'ingresso di almeno uno dei successori.

Il secondo indica quali variabili devono essere disponibili prima dell'esecuzione del nodo.

Le variabili utilizzate dal nodo sono necessarie.

Le variabili definite dal nodo non richiedono il loro valore precedente, a meno che non siano utilizzate nella stessa istruzione secondo la semantica del linguaggio.

---

## Domanda: Cosa rappresentano `Use` e `Def`?

### Risposta

`Use[n]` rappresenta le variabili il cui valore viene letto dal nodo `n`.

`Def[n]` rappresenta le variabili il cui valore viene definito o sovrascritto dal nodo `n`.

Per esempio:

```text
x := y + z
```

si ha:

```text
Use = {y, z}
Def = {x}
```

---

## Domanda: Faccia un esempio di liveness.

### Risposta

Consideriamo:

```text
x := 5
y := x + 1
```

Prima della seconda istruzione, `x` è live perché il suo valore verrà utilizzato.

Dopo:

```text
x := 5
```

il valore precedente di `x` non è più necessario perché viene sovrascritto.

---

# 8. Reaching Definitions

## Domanda: Che cos'è una reaching definition?

### Risposta

Una definizione raggiunge un punto del programma se esiste almeno un percorso dal punto in cui la definizione viene eseguita fino a quel punto, senza che la variabile definita venga nuovamente ridefinita lungo il percorso.

---

## Domanda: Perché reaching definitions è una forward analysis?

### Risposta

Una definizione nasce in un punto del programma e la sua informazione viene propagata verso i possibili successori.

Per questo la direzione naturale dell'analisi è in avanti.

---

## Domanda: Quali sono le informazioni fondamentali della reaching definitions analysis?

### Risposta

Per ogni nodo si considerano tipicamente:

- le definizioni che raggiungono l'ingresso del nodo;
- le definizioni generate dal nodo;
- le definizioni uccise perché la stessa variabile viene ridefinita.

La forma generale è:

```text
RD_in[n] = ⋃ RD_out[p]
           p ∈ predecessors(n)
```

e:

```text
RD_out[n] = Gen[n] ∪ (RD_in[n] - Kill[n])
```

---

## Domanda: Perché rappresentare una definizione tramite l'identificatore del nodo?

### Risposta

Se un nodo rappresenta una specifica istruzione di assegnazione, il suo identificatore individua univocamente quella definizione.

Le informazioni sulla variabile definita sono già contenute nel nodo.

Rappresentare la definizione tramite l'id del nodo evita quindi di duplicare dati e consente di distinguere facilmente definizioni diverse della stessa variabile.

---

## Domanda: Faccia un esempio.

### Risposta

Consideriamo:

```text
1: x := 1
2: y := x
3: x := 2
```

Nel punto immediatamente prima dell'istruzione 2, la definizione di `x` che può raggiungere quel punto è quella prodotta dal nodo 1.

Dopo il nodo 3, la definizione precedente di `x` viene uccisa lungo quel percorso e viene sostituita dalla nuova definizione.

---

# 9. Ottimizzazioni

## Domanda: Quali ottimizzazioni principali vengono applicate?

### Risposta

Una pipeline tipica comprende:

```text
Constant Propagation
        ↓
Constant Folding
        ↓
Dead Store Elimination
```

Queste trasformazioni possono essere ripetute fino al fixpoint.

---

## Domanda: Che cos'è la constant propagation?

### Risposta

La constant propagation sostituisce l'uso di una variabile con un valore costante quando è possibile dimostrare che la variabile possiede quel valore nel punto considerato.

Esempio:

```text
x := 5
y := x + 1
```

può diventare:

```text
x := 5
y := 5 + 1
```

---

## Domanda: Quando la constant propagation deve essere conservativa?

### Risposta

Quando esistono più percorsi di controllo che possono raggiungere un punto.

Per esempio:

```text
if c then
    x := 1
else
    x := 2

y := x
```

Non è corretto sostituire `x` con `1` o con `2`.

L'ottimizzazione deve quindi propagare una costante soltanto quando l'informazione disponibile permette di dimostrare in modo sicuro che tutte le possibili definizioni rilevanti concordano sullo stesso valore.

---

## Domanda: Perché è importante la soundness in un'ottimizzazione?

### Risposta

Un'ottimizzazione deve preservare il comportamento osservabile del programma.

Non è sufficiente che una trasformazione migliori alcuni casi: deve essere corretta per tutti i possibili percorsi di esecuzione.

Nel caso della constant propagation, scegliere arbitrariamente una delle possibili definizioni in presenza di un join potrebbe cambiare il risultato del programma.

---

## Domanda: Che cos'è il constant folding?

### Risposta

Il constant folding valuta a compile-time espressioni composte interamente da costanti.

Per esempio:

```text
y := 5 + 1
```

diventa:

```text
y := 6
```

---

## Domanda: Qual è la differenza tra constant propagation e constant folding?

### Risposta

La constant propagation utilizza informazioni sulle variabili per sostituirle con valori costanti.

Il constant folding calcola espressioni che sono già diventate completamente costanti.

Per esempio:

```text
x := 5
y := x + 3
```

La propagation produce:

```text
y := 5 + 3
```

Il folding produce:

```text
y := 8
```

---

## Domanda: Che cos'è la dead store elimination?

### Risposta

La dead store elimination elimina un'assegnazione quando il valore assegnato non verrà mai utilizzato prima di essere sovrascritto o prima della fine dell'esecuzione rilevante.

Esempio:

```text
x := 1
x := 2
```

La prima assegnazione può essere eliminata se non esiste alcun percorso nel quale il valore `1` venga utilizzato.

---

## Domanda: Perché le ottimizzazioni vengono ripetute fino al fixpoint?

### Risposta

Una trasformazione può creare nuove opportunità per una trasformazione successiva.

Per esempio:

```text
x := 5
y := x + 3
z := y
```

La constant propagation può rendere l'espressione completamente costante.

Il constant folding può quindi calcolarla.

Dopo ulteriori propagazioni alcune assegnazioni possono diventare inutilizzate e quindi eliminabili.

Ripetere il processo fino al fixpoint permette di sfruttare le opportunità create dalle trasformazioni precedenti.

---

# 10. Generazione LLVM

## Domanda: Perché generare LLVM IR?

### Risposta

LLVM IR è una rappresentazione intermedia che permette di delegare al framework LLVM molte attività di compilazione e ottimizzazione.

Il progetto può concentrarsi sulla traduzione del proprio linguaggio nella rappresentazione LLVM, lasciando a LLVM la generazione finale di codice per l'architettura target.

---

## Domanda: Che approccio viene utilizzato per rappresentare le variabili?

### Risposta

Un approccio semplice consiste nel rappresentare le variabili tramite memoria:

```text
alloca
store
load
```

Una variabile viene allocata.

Le assegnazioni producono `store`.

Le letture della variabile producono `load`.

---

## Domanda: Perché non generare direttamente SSA?

### Risposta

Generare direttamente SSA richiede di gestire il problema delle diverse definizioni di una variabile che convergono in un punto del CFG.

In particolare, occorre introdurre correttamente i `phi node`.

Per una piccola implementazione didattica, è più semplice generare inizialmente codice memory-based e delegare successivamente la promozione delle variabili in registri a un pass LLVM come `mem2reg`.

---

## Domanda: Che cos'è un phi node?

### Risposta

Un phi node seleziona concettualmente il valore corretto di una variabile in base al predecessore dal quale è stato raggiunto un blocco.

Per esempio:

```text
if c then
    x := 1
else
    x := 2
```

dopo il join, una rappresentazione SSA richiede concettualmente un valore:

```text
x3 = phi [x1, then], [x2, else]
```

---

## Domanda: Perché la conversione in SSA è complessa?

### Risposta

Bisogna determinare:

- dove inserire i phi node;
- quali definizioni devono essere rinominate;
- quali valori raggiungono ciascun join.

Queste operazioni sono strettamente collegate alla struttura del CFG e, nelle implementazioni classiche, a concetti come dominatori e dominance frontier.

---

# 11. MiniFun — Environment e interprete

## Domanda: Che cos'è un environment?

### Risposta

Un environment associa identificatori a valori.

Durante l'interpretazione, quando viene incontrata una variabile, l'interprete cerca il suo valore nell'environment.

Concettualmente:

```text
x ↦ valore
y ↦ valore
f ↦ closure
```

---

## Domanda: Perché l'environment è importante in un linguaggio funzionale?

### Risposta

In un linguaggio funzionale le funzioni possono essere definite in un punto e applicate successivamente in un altro contesto.

Per preservare il significato delle variabili libere presenti nel corpo della funzione è necessario conservare l'ambiente nel quale la funzione è stata creata.

Questo porta al concetto di closure.

---

# 12. Closure e lexical scoping

## Domanda: Che cos'è una closure?

### Risposta

Una closure è una struttura che rappresenta una funzione insieme all'ambiente lessicale nel quale la funzione è stata definita.

Concettualmente:

```text
closure =
    parametro
    corpo
    environment catturato
```

---

## Domanda: Perché una funzione non può essere rappresentata soltanto da parametro e corpo?

### Risposta

Perché il corpo della funzione può contenere variabili libere.

Per esempio:

```text
let x = 10 in
let f = fun y => x + y in
...
```

Quando `f` viene applicata, deve sapere quale valore possiede `x`.

Il valore di `x` non deve dipendere dall'ambiente del chiamante, ma dall'ambiente nel quale `f` è stata definita.

---

## Domanda: Che cos'è lo scoping lessicale?

### Risposta

Nello scoping lessicale il significato di una variabile libera dipende dalla posizione sintattica nella quale la funzione viene definita.

Una closure cattura quindi l'ambiente della definizione, non quello della chiamata.

---

## Domanda: Perché non bisogna condividere indiscriminatamente un environment mutabile?

### Risposta

Se più closure condividono la stessa struttura mutabile, modifiche successive all'ambiente potrebbero diventare visibili anche a closure create precedentemente.

Questo può violare lo scoping lessicale e produrre comportamenti simili a un cattivo dynamic scoping.

Per evitare questo problema, quando viene esteso un environment è possibile creare una nuova versione dell'ambiente contenente i binding precedenti più il nuovo binding.

---

## Domanda: Che differenza c'è tra lexical scoping e dynamic scoping?

### Risposta

Con lexical scoping, una variabile libera viene risolta in base al contesto della definizione della funzione.

Con dynamic scoping, viene risolta in base al contesto della chiamata.

Le closure sono uno strumento fondamentale per implementare correttamente lo scoping lessicale.

---

# 13. Funzioni ricorsive

## Domanda: Perché una normale closure non basta per una funzione ricorsiva?

### Risposta

Una funzione ricorsiva deve poter trovare il proprio nome nell'environment quando il suo corpo viene eseguito.

Per questo l'ambiente utilizzato nell'applicazione deve contenere anche un binding dal nome della funzione alla closure stessa.

---

## Domanda: Come funziona concettualmente una recursive closure?

### Risposta

Per una definizione:

```text
letfun f x = e1 in e2
```

la closure ricorsiva memorizza:

- il nome `f`;
- il parametro `x`;
- il corpo `e1`;
- l'ambiente della definizione.

Quando la funzione viene applicata:

1. viene ricostruito l'ambiente catturato;
2. viene aggiunto il binding `f → closure`;
3. viene aggiunto il binding `x → argomento`;
4. viene valutato il corpo.

In questo modo il corpo può richiamare `f`.

---

# 14. Type checking con annotazioni

## Domanda: Qual è il ruolo del type checker?

### Risposta

Il type checker verifica staticamente che le espressioni rispettino le regole del sistema di tipi.

Per esempio:

- un'operazione aritmetica richiede operandi numerici;
- una condizione richiede un booleano;
- una funzione deve essere applicata a un argomento compatibile con il tipo del parametro.

---

## Domanda: Come viene tipizzata una funzione annotata?

### Risposta

Per una funzione:

```text
fun x : τ1 => e
```

si estende l'ambiente dei tipi con:

```text
x : τ1
```

e si calcola il tipo del corpo:

```text
Γ, x : τ1 ⊢ e : τ2
```

Quindi:

```text
Γ ⊢ fun x : τ1 => e : τ1 → τ2
```

---

## Domanda: Cosa significa che il type checking è syntax-directed?

### Risposta

Significa che la forma sintattica dell'espressione determina direttamente quale regola di typing deve essere applicata.

Per esempio:

- un intero ha tipo `int`;
- un booleano ha tipo `bool`;
- un'addizione richiede due interi;
- un'applicazione richiede una funzione.

Il type checker procede quindi ricorsivamente sulla struttura dell'AST.

---

## Domanda: Qual è il vantaggio delle annotazioni?

### Risposta

Le annotazioni eliminano parte dell'incertezza.

Il tipo del parametro di una funzione è già disponibile nella sintassi, quindi non deve essere inferito.

Questo rende il type checker più diretto rispetto a un sistema di inferenza completo.

---

# 15. Algorithm W

## Domanda: Che cos'è l'Algorithm W?

### Risposta

L'Algorithm W è un algoritmo classico per l'inferenza dei tipi nei sistemi in stile Hindley-Milner.

Dato un ambiente di tipi e un'espressione, inferisce un tipo applicando:

- generazione di type variables fresche;
- unificazione;
- sostituzioni;
- istanziazione;
- generalizzazione.

Il risultato tipicamente comprende una sostituzione e il tipo inferito.

---

## Domanda: Qual è la differenza tra monotipo e politipo?

### Risposta

Un monotipo non contiene quantificatori universali espliciti.

Esempi:

```text
int
bool
'a
'a -> int
```

Un politipo può quantificare alcune type variables:

```text
∀a. a -> a
```

Il politipo rappresenta una forma di polimorfismo.

---

## Domanda: Perché servono type variables fresche?

### Risposta

Durante l'inferenza si introducono variabili che rappresentano tipi ancora sconosciuti.

Devono essere fresche per evitare collisioni accidentali con type variables già utilizzate in altri contesti.

---

# 16. Unificazione

## Domanda: Che cos'è l'unificazione?

### Risposta

L'unificazione cerca una sostituzione che renda due tipi uguali.

Per esempio:

```text
'a -> int
```

e:

```text
bool -> 'b
```

possono essere unificati con:

```text
'a := bool
'b := int
```

ottenendo:

```text
bool -> int
```

---

## Domanda: Che cos'è una sostituzione?

### Risposta

Una sostituzione associa type variables a tipi.

Per esempio:

```text
S = {
    'a ↦ int,
    'b ↦ bool
}
```

Applicare `S` a:

```text
'a -> 'b
```

produce:

```text
int -> bool
```

---

## Domanda: Perché le sostituzioni devono essere applicate anche agli ambienti e ai tipi intermedi?

### Risposta

Durante l'inferenza, nuove informazioni possono rendere più specifici tipi precedentemente sconosciuti.

Se una variabile di tipo viene unificata con `int`, le occorrenze rilevanti devono riflettere questa nuova informazione.

L'applicazione coerente delle sostituzioni è quindi essenziale per mantenere la consistenza dell'inferenza.

---

# 17. Occurs Check

## Domanda: Che cos'è l'occurs check?

### Risposta

L'occurs check verifica che una type variable non venga sostituita con un tipo che contiene la stessa variabile.

Per esempio, non è lecito imporre:

```text
'a = 'a -> int
```

perché `a` compare all'interno del tipo con cui dovrebbe essere sostituita.

---

## Domanda: Perché l'occurs check è necessario?

### Risposta

Senza occurs check si potrebbero generare tipi infiniti.

Infatti:

```text
'a = 'a -> int
```

implicherebbe:

```text
'a = ('a -> int)
```

e sostituendo nuovamente `a`:

```text
'a = (('a -> int) -> int)
```

e così via.

Il sistema Hindley-Milner non ammette questo tipo di tipi infiniti nella normale unificazione.

---

# 18. Let-polymorphism

## Domanda: Che cos'è il let-polymorphism?

### Risposta

Il let-polymorphism permette a un valore definito con `let` di essere generalizzato e utilizzato successivamente con istanziazioni diverse.

Per esempio:

```text
let id = fun x => x in
...
```

può ricevere il tipo generale:

```text
∀a. a -> a
```

---

## Domanda: Perché una funzione polimorfica può essere usata con tipi diversi?

### Risposta

Ogni utilizzo del politipo viene istanziato con nuove type variables fresche.

Quindi:

```text
id 3
```

può utilizzare:

```text
int -> int
```

mentre:

```text
id true
```

può utilizzare:

```text
bool -> bool
```

Entrambe le istanziazioni derivano dallo stesso schema generale:

```text
∀a. a -> a
```

---

## Domanda: Che differenza c'è tra generalizzazione e istanziazione?

### Risposta

La generalizzazione prende un monotipo e quantifica le type variables che possono essere rese generiche rispetto all'ambiente.

L'istanziazione prende un politipo e sostituisce le variabili quantificate con nuove type variables fresche.

In breve:

```text
generalizzazione:
tipo specifico/intermedio
        ↓
schema polimorfico

istanziazione:
schema polimorfico
        ↓
nuovo tipo utilizzabile in uno specifico contesto
```

---

## Domanda: Perché non tutte le type variables vengono sempre generalizzate?

### Risposta

Le variabili che sono già vincolate dall'ambiente non devono essere rese arbitrariamente polimorfiche.

La generalizzazione considera quindi le type variables libere del tipo inferito che non sono già libere nell'ambiente.

Questo evita di trasformare in polimorfica un'informazione che dipende da vincoli esterni.

---

# 19. Domande insidiose da orale

## Domanda: Se il CFG usasse basic block massimali, cosa cambierebbe?

### Risposta

Il CFG avrebbe meno nodi, ma ciascun nodo potrebbe contenere più istruzioni.

Le analisi dovrebbero quindi gestire il comportamento interno al blocco, calcolando correttamente `Use`, `Def`, `Gen` e `Kill` per l'intera sequenza.

Con blocchi minimi l'analisi è più granulare e diretta.

---

## Domanda: Perché la liveness usa i successori mentre reaching definitions usa i predecessori?

### Risposta

La liveness è una backward analysis: per sapere cosa serve prima di un nodo bisogna sapere cosa serve dopo.

Reaching definitions è una forward analysis: per sapere quali definizioni raggiungono un nodo bisogna considerare le informazioni provenienti dai predecessori.

---

## Domanda: Perché non si può propagare una costante prendendo semplicemente una reaching definition?

### Risposta

Perché in presenza di branch diversi possono raggiungere un punto definizioni diverse della stessa variabile.

Prendere una sola definizione ignorando le altre potrebbe cambiare il comportamento del programma.

È necessario considerare tutte le definizioni che possono raggiungere il punto e propagare soltanto informazioni dimostrabili come sicure.

---

## Domanda: Perché `mem2reg` può essere considerato un buon compromesso?

### Risposta

Permette di separare due problemi.

Il progetto genera una rappresentazione LLVM corretta e semplice basata su memoria.

LLVM si occupa successivamente della trasformazione in una forma più efficiente, introducendo registri e, quando necessario, phi node.

Questo evita di reimplementare manualmente un algoritmo complesso già disponibile nell'infrastruttura LLVM.

---

## Domanda: Che relazione esiste tra CFG e generazione LLVM?

### Risposta

Entrambe le rappresentazioni modellano il controllo tramite blocchi e salti.

Il CFG del compilatore può quindi essere tradotto naturalmente in basic block LLVM e terminatori che rappresentano salti condizionati o incondizionati.

La struttura di controllo è già esplicita nel CFG.

---

## Domanda: Perché una closure deve catturare l'environment della definizione?

### Risposta

Per implementare lexical scoping.

Le variabili libere nel corpo della funzione devono essere risolte in base al contesto nel quale la funzione è stata scritta e definita, non in base al luogo da cui viene chiamata.

---

## Domanda: Perché Algorithm W ha bisogno dell'unificazione?

### Risposta

Durante l'inferenza vengono generate variabili di tipo sconosciute.

Le diverse operazioni impongono vincoli su queste variabili.

L'unificazione risolve tali vincoli cercando sostituzioni che rendano compatibili i tipi.

---

## Domanda: Perché il let-polymorphism è importante?

### Risposta

Permette di definire una funzione una sola volta con un tipo generale e di utilizzarla in contesti differenti.

Senza generalizzazione, una funzione come l'identità potrebbe essere fissata al primo tipo con cui viene utilizzata.

---

# 20. Risposta introduttiva consigliata per l'esame

## Domanda: Mi descriva il progetto.

### Risposta modello

Il progetto affronta diversi aspetti delle tecniche di compilazione attraverso l'implementazione di due linguaggi, MiniImp e MiniFun, in OCaml.

Per MiniImp ho seguito una pipeline completa che parte dal lexer e dal parser, costruisce un AST e successivamente un Control Flow Graph. Sul CFG vengono eseguite analisi di data-flow, in particolare liveness analysis e reaching definitions. Le informazioni ottenute vengono utilizzate per supportare ottimizzazioni come constant propagation, constant folding e dead-store elimination. Infine il programma viene tradotto in LLVM IR, utilizzando una rappresentazione inizialmente memory-based e delegando a LLVM ulteriori trasformazioni, come la promozione delle variabili in registri.

Per MiniFun il progetto affronta invece l'interpretazione di un linguaggio funzionale e il suo sistema di tipi. L'interprete utilizza environment e closure per implementare correttamente lo scoping lessicale, comprese le funzioni ricorsive. Dal punto di vista statico sono presenti sia un type checker con annotazioni esplicite sia un sistema di inferenza basato sull'Algorithm W, con unificazione, substitutions, occurs check, generalizzazione e let-polymorphism.

Nel complesso, il progetto permette quindi di attraversare diverse fasi fondamentali di un compilatore e di un interprete: analisi lessicale e sintattica, rappresentazioni intermedie, analisi statica, ottimizzazione, inferenza dei tipi ed esecuzione.

---

# Come utilizzare questo documento per prepararsi

Un buon metodo di studio è:

1. Leggere la domanda.
2. Provare a rispondere senza guardare.
3. Confrontare la risposta con la risposta modello.
4. Individuare i concetti chiave mancanti.
5. Ripetere la risposta a voce senza leggere.

Per l'orale è particolarmente importante non imparare le risposte parola per parola, ma comprendere i collegamenti:

```text
Parser
  ↓
AST
  ↓
CFG
  ↓
Data-flow analysis
  ↓
Ottimizzazioni
  ↓
Code generation
```

e, per MiniFun:

```text
AST
  ↓
Environment / Closure
  ↓
Interpretazione

AST
  ↓
Type checking / Algorithm W
  ↓
Tipo inferito
```

Una volta consolidate queste connessioni, è molto più facile rispondere anche a domande formulate in modo diverso da quelle presenti in questo documento.
