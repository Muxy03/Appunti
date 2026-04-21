c -> a program -> syntax
$[\![c]\!]$ -> its meaning -> semantics

$\sigma: X \leftarrow \Z$ -> state: variables -> integers

$\Sigma \overset{\hat}{=} \{\sigma: X \leftarrow \Z\}$

#TODO: SLIDE 1 PAG 27 to 30

Semantic property of a program c:$ \P(c) \equiv \forall P \noteq \empty. \exists \delta \in [\![c]\!]P.\delta(x) \noteq 0$

#TODO: SLIDE 1 PAG 32

Collatz's conjecture

#TODO: SLIDE 1 PAG 37

over approximations -> Good for proving correctness, Bad for bug-finding (false positive)

#TODO: SLIDE 1 PAG 41,42

under approximations -> Bad for proving correctness, Good for bug-finding (false positive)

#TODO: SLIDE 1 PAG 47

#TODO: SLIDE 1 PAG 50

Spectrum of Program Analysis Techniques:
- testing
- machine-assisted proving
- finite-state model checking
- conservative static analysis
- bug-finding

#TODO: SLIDE 1 PAG 52 to 57

#TODO: SLIDE 2 PAG 10 to 12

$[\![arithmetic expr]\!]: \Sigma \leftarrow \Z$

$[\![boolean expr]\!]: \Sigma \leftarrow \B$

$[\![command]\!]: \Sigma \leftarrow \Sigma_{\bottom}$

#TODO: SLIDE 2 PAG 16 to 24

#TODO: SLIDE 2 PAG 26 to 30

$\sigma:X \leftarrow \Z$
$\Siigma ≜ \{\sigma:X \leftarrow \Z\}$
$\p(\Sigma) ≜ \{P ⊆ \Sigma\}$

state notation:
- $[x->1,...]$  -> x holds 1
- $\sigma[n/x]$ -> the state where *x* holds *n* and any other variable *y* holds *σ(y)*

(x=1,...) -> property notation -> the set of all states where x holds 1

Regular Commands:
- c ::= e \| c1:c2 \| c1+c2 \| c* -> (atomic cmd) - ... - choice - Kleene star
- e ::= skip \| x:= a \| b? \| ...
- a ::= n \| x \| a1+a2 \! ...
- b ::= a1 lteq a2 \| b1 land b2 \| ...

#TODO: SLIDE 2 PAG 37

#TODO: SLIDE 2 PAG 40

#TODO: SLIDE 2 PAG 42

#TODO: SLIDE 2 PAG 44 to 51

#TODO: SLIDE 2 PAG 53 to 60

Ecco le soluzioni dettagliate e le spiegazioni per le domande poste al termine della Lezione 2 sulla **Semantica Denotazionale** (Fonte 02).

---

### Domanda 1
Sia dato il programma $c \triangleq (z := x) + (z := y)$ (una scelta non deterministica tra assegnare $x$ o $y$ alla variabile $z$) e sia la proprietà dello stato iniziale $P \triangleq (x = y = 0)$.

#### 1.1 Qual è $[[c]]P$?
**Soluzione:** $[[c]]P = (x = 0, y = 0, z = 0)$.

**Spiegazione:**
La semantica di raccolta (collecting semantics) per una scelta non deterministica ($c_1 + c_2$) è definita come l'unione dei risultati di entrambi i rami: $[[c_1 + c_2]]P = [[c_1]]P \cup [[c_2]]P$.
*   Eseguendo il primo ramo ($z := x$) partendo da uno stato dove $x=0$ e $y=0$, otteniamo uno stato finale dove $z=0$ (e $x, y$ rimangono $0$).
*   Eseguendo il secondo ramo ($z := y$) partendo dallo stesso stato, otteniamo nuovamente $z=0$.
L'unione di questi stati produce l'unico stato possibile $(x=0, y=0, z=0)$.

#### 1.2 Esempio di sovra-approssimazione (over-approximation)
**Esempio:** $(x = y = 0)$.

**Spiegazione:**
Una sovra-approssimazione è un insieme che **include** tutti i comportamenti reali del programma ($[[c]]P \subseteq Q$). In questo caso, l'insieme degli stati dove $x=0$ e $y=0$ è una sovra-approssimazione valida perché contiene lo stato reale $(x=0, y=0, z=0)$, ma è meno preciso poiché non specifica il valore di $z$.

#### 1.3 Esempio di sotto-approssimazione (under-approximation)
**Esempio:** $(x = y = z = 0)$.

**Spiegazione:**
Una sotto-approssimazione è un insieme che è un **sottoinsieme** dei risultati reali ($Q \subseteq [[c]]P$). Poiché il risultato reale è un singolo stato, l'approssimazione più precisa (e quindi un esempio valido) è l'insieme stesso che contiene solo quello stato.

#### 1.4 Qual è $wlp(c, (z = 0))$?
**Soluzione:** $(x = 0 \wedge y = 0)$.

**Spiegazione:**
La **Weakest Liberal Precondition** ($wlp$) identifica l'insieme più grande di stati iniziali tali che **tutte** le computazioni che terminano raggiungano lo stato desiderato ($z=0$). Poiché il programma può scegliere indifferentemente $z := x$ o $z := y$, affinché $z$ sia *sempre* $0$ alla fine, è necessario che sia $x$ che $y$ siano $0$ all'inizio.

#### 1.5 Qual è $wpp(c, (z = 0))$?
**Soluzione:** $(x = 0 \vee y = 0)$.

**Spiegazione:**
La **Weakest Possible Precondition** ($wpp$) identifica l'insieme di stati iniziali tali che **almeno una** computazione possa terminare con successo in uno stato dove $z=0$. In questo caso, basta che $x=0$ (così il primo ramo ha successo) oppure che $y=0$ (così il secondo ramo ha successo).

---

### Domanda 2
Sia dato il programma $c \triangleq \text{if } x < y \text{ then } x := y \text{ else (while true do skip)}$ e sia la specifica post-condizione $Q \triangleq (x = y = 0)$.

#### 2.1 Qual è $wlp(c, Q)$?
**Soluzione:** $(x \ge y \vee y = 0)$.

**Spiegazione:**
Per la definizione di $wlp$, dobbiamo considerare sia i rami che terminano correttamente, sia quelli che non terminano:
1.  **Ramo then ($x < y$):** L'assegnamento $x := y$ deve portare a $x=y=0$. Questo avviene se partiamo da uno stato dove $y=0$. Tuttavia, la guardia del ramo è $x < y$, quindi dobbiamo avere $x < 0 \wedge y = 0$.
2.  **Ramo else ($x \ge y$):** Il comando `while true do skip` non termina mai. Per definizione, la correttezza parziale ($wlp$) è soddisfatta dai rami che non terminano. Quindi, tutti gli stati in cui $x \ge y$ soddisfano la $wlp$.
Unendo le condizioni (e semplificando $x < 0 \wedge y = 0$ in un contesto più ampio), si ottiene $(x \ge y \vee y = 0)$.

#### 2.2 Qual è $wpp(c, Q)$?
**Soluzione:** $(x < y \wedge y = 0)$.

**Spiegazione:**
La $wpp$ richiede che esista **almeno una** computazione che termini e soddisfi $Q$.
1.  Il ramo `else` non termina mai, quindi non contribuisce alla $wpp$.
2.  Il ramo `then` termina e soddisfa $Q$ solo se $x < y$ (condizione del ramo) e se il valore assegnato ($y$) è $0$. Da $y=0$ e $x<y$ deriva $x < 0$.
La condizione risultante è quindi $(x < y \wedge y = 0)$.

---

### Domanda 3
Analisi delle relazioni tra semantica e pre-condizioni.

#### 3.1 $[[c]](wpp(c, Q)) \subseteq Q$?
**Soluzione:** **No** (Nessuna inclusione garantita).

**Spiegazione:**
La $wpp$ garantisce solo che *esista* una computazione di successo. Tuttavia, se il programma è non deterministico, potrebbero esserci altre traiettorie che partono dalla stessa pre-condizione ma raggiungono stati che non sono in $Q$. In altre parole, alcuni stati in $Q$ potrebbero non essere raggiungibili da tutte le esecuzioni generate da $wpp$.

#### 3.2 $wpp(c, [[c]]P) \supseteq P$?
**Soluzione:** **No** (Nessuna inclusione garantita).

**Spiegazione:**
Anche se partiamo da uno stato in $P$, non è garantito che esso appartenga alla $wpp$ del suo stesso risultato semantico se alcune computazioni **non terminano**. La $wpp$ richiede la terminazione con successo; se uno stato in $P$ porta a un ciclo infinito, esso non soddisferà la condizione di "possibile computazione terminata con successo", venendo escluso dall'insieme.


Inference rule -> $\frac{Premises}{Conclusion}$

axioms -> Rules without premises represent facts that are accepted without proof

Derivation Tree: 
Inference rules allow proof to be constructed in the form of derivation 
trees, tree structures that represent the logical path by which a 
conclusion is reached starting from a set of premises

Hoare triplets:
{P}c{Q} -> Whenever c is executed in a state satisfying P if the execution of c terminates, it terminates in a state satisfying Q

{P}c{Q} <=> $[[c]]P \subseteq Q$

We talk about *partial correctness* because the previous semantic condition 
does not guarantee that the execution of c on  states satisfying P terminate  

Q is an over-approximation of the states that can be reached by states in P

#TODO: SLIDE 3 PAG 20 to 43

{P}c{Q} is valid if $[[c]]P \subseteq Q$

{false}c{Q} is valid
{P}c{true} is valid

#TODO: SLIDE 3 PAG 45 to 49

#TODO: SLIDE 4 PAG 2 to 20

#TODO: SLIDE 4 PAG 22 to 28

Any derivable HL triple is valid -> By induction on the derivation tree. (proof for composition of commands)
$[[c_1;c_2]]P = [[c_2]]([[c_1]]P) \subseteq [[c_2]]R \subseteq Q$

#TODO: SLIDE 4 PAG 30 to 36

P => wlp(c,Q) <=> $[[c]]P \subseteq Q$

#TODO: SLIDE 4 PAG 38 to 47






