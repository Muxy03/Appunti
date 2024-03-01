
![[1-IIA-24-introduzione-V1.0.pdf]]

# PRIMA PARTE

![[2-IIA-2024-agents.pdf]]

Agente razionale -> fa la cosa "giusta" -> per ogni sequenza di percezioni compie l’azione che massimizza il valore atteso della misura delle prestazioni, considerando le sue percezioni passate e la sua conoscenza pregressa.

Agente autonomo -> il suo comportamento dipende dalla sua capacità di ottenere esperienza (e non dall’aiuto del progettista)

Problemi -> PEAS = Performance Envoriment Actuators Sensors

Proprietà ambiente-problema:
- Osservabilità:
	- completamente osservabile
		- ![[Pasted image 20240212113837.png]]
	- parzialmente osservabile -> Sono presenti limiti o imprecisioni dell’apparato sensoriale
- Singolo/Multi-agente:
	- M. competitivo
	- M. cooperativo
- Predicibilità:
	- Deterministico ->Se lo stato successivo è completamente determinato dallo stato corrente e dall’azione -> scacchi
	- Stocastico -> Esistono elementi di incertezza con associata probabilità ->tiro in porta
	- Non Deterministico -> Si tiene traccia di più stati possibili risultato dell’azione (ma non in base ad una probabilità)
- "Frequenza":
	- Episodico -> L’esperienza dell’agente è divisa in episodi atomici indipendenti -> no pianificare
	- Sequenziale -> Ogni decisione influenza le successive
- "Stato":
	- Statico -> il mondo non cambia mentre l'agente decide l'azione
	- Dinamico -> Cambia nel tempo, va osservata la contingenza -> tardare equivale a non agire
	- Semi-Dinamico -> L’ambiente non cambia ma la valutazione dell’agente -> scacchi con timer
- "Range Valori":
	- Discreto
	- Continuo
- "Stato di Conoscenza":
	- Noto -> Noto diverso da osservabile (es. carte coperte, ma regole note)
	- Ignoto 

Ambiente razionale: parzialmente osservabili, stocastici, sequenziali, dinamici, continui, multi-agente, ignoti

![[Pasted image 20240212123058.png]]

![[Pasted image 20240212123140.png]]

Tipi di Agenti:
- basato su tabella -> La scelta dell’azione è un accesso a una «tabella» che associa un’azione ad ogni possibile sequenza di percezioni.
- Agente reattivo semplice -> non storia in memoria 
	- ![[Pasted image 20240212123750.png]]
- basato su modello
	- ![[Pasted image 20240212124039.png]]
- con obiettivo
	- ![[Pasted image 20240212124130.png]]
- con valutazione di utilità
	- ![[Pasted image 20240212124301.png]]
- che apprendono
	- ![[Pasted image 20240212124543.png]]

![[Pasted image 20240212124703.png]]

![[3-IIA-2024-problem_solving.pdf]]

ricerca su albero -> Ossia senza controllare se i nodi (stati) siano già stati esplorati
ricerca su grafo -> controllando se i nodi (stati) siano già stati esplorati -> esplora uno stato al più una volta -> frontiera separa nodi esplorati da quelli esplorati
ricerca bidirezionale ->  si procede sia da start che da goal per incontrarsi ->complex spazio e tempo : $O(b^{d/2})$

 **distanza di Manhattan** = $|x_1-x_2|+|y_1-y_2|$

Algoritmi non informati:
- BF -> FIFO -> inserisco in coda ed estraggo dalla testa (QUEUE) -> inserimento e estrazione agli estremi:
	- strategia completa
	- strategia ottimale se  gli operatori hanno tutti lo stesso costo k, cioè g(n) = k · depth(n), dove g(n) è il costo del cammino per arrivare a n
	- complex tempo: $O(b^{d})$ 
	- complex spazio: $O(b^{d})$  -> dim frontiera
- DF -> LIFO -> inserisco ed estraggo dalla testa (STACK) -> inserimento e estrazione stesso punto
	- complex tempo: $O(b^m)$ con b = fattore di diramazione e m = lunghezza max dei cammini nello spazio degli stati
	- complex spazio: bm (frontiera sul cammino)
	- versione su albero -> no completa e no ottimale
	- versione su grafo -> si perde vantaggio sulla memoria -> completa solo in spazi di stati finiti
- DL -> DF limitato
	- strategia completa se d < l, d= profondità nodo obiettivo più superficiale 
	- non ottimale
	- complex tempo: $O(b^l)$
	- complex spazio : $O(b*l)$
- ID -> approfondimento iterativo -> DL con l=0 che poi incrementa per ogni interazione
	- completo
	- ottimale per costo fisso di operazione
	- complex tempo: $O(b^d)$
	- complex spazio: $O(bd)$
	- best compromesso fra BF e DF
- UC ->  si espande sui contorni di uguale (o meglio uniforme) costo (e.g. in km) invece che sui contorni di uguale profondità (BF)
	- ottimalita e completezza garantite se il costo degli archi sia > 0 ($\epsilon > 0$)
	- numero di mosse nel caso peggiore $\lfloor C/\epsilon \rfloor$ con C = costo soluzione ottima 
	- complex: $O(b^{1+\lfloor C/\epsilon \rfloor})$ -> quando ogni azione ha lo stesso costo UC somiglia a BF ma con complex: $O(b^{1+d})$
- ![[Pasted image 20240216165540.png]]

![[Pasted image 20240214173324.png]]
Valutazione Strategia:
- ![[Pasted image 20240214181258.png]]

![[Pasted image 20240216160711.png]]

```python
"""Ricerca-grafo in ampiezza"""

def BF(problem): #CODA -> PUSH E UNSHIFT -> FIFO

    # explored = []

    # node = Node(problem.initial_state)

    # if problem.goal_test(node.state):

    #     return node.solution(explored_set = explored)

    # frontier = FIFOQueue()

    # frontier.insert(node)

    # while not frontier.isempty():

    #     node = frontier.pop()

    #     explored.append(node.state)

    #     for action in problem.actions(node.state):

    #         child_node = node.child_node(problem,action)

    #         if (child_node.state not in explored) and (not frontier.contains_state(child_node.state)):

    #             if problem.goal_test(child_node.state):

    #                 return child_node.solution(explored_set = explored)

    #             frontier.insert(child_node)

    return None
```
```python
"""Ricerca in profondita' ricorsiva """

def DF_ricorsiva(problem,node): #STACK -> PUSH E POP -> LIFO

    # if problem.goal_test(node.state):

    #     return node.solution()

    # for action in problem.actions(node.state):

    #     child_node = node.child_node(problem, action)

    #     result = DF_ricorsiva(problem, child_node)

    #     if result is not None:

    #         return result

    return None
```
```python
"""Ricerca-grafo UC"""

def UC(problem):

    # explored = []

    # node = Node(problem.initial_state)

    # frontier = PriorityQueue(f = lambda x:x.path_cost)

    # frontier.insert(node)

    # while not frontier.isempty():

    #     node = frontier.pop()

    #     if problem.goal_test(node.state):

    #         return node.solution(explored_set = explored)

    #     else:

    #         explored.append(node.state)

    #     for action in problem.actions(node.state):

    #         child_node = node.child_node(problem, action)

    #         if (child_node.state not in explored) and (not frontier.contains_state(child_node.state)):

    #             frontier.insert(child_node)

    #         elif frontier.contains_state(child_node.state) and (frontier.get_node(frontier.index_state(child_node.state)).path_cost > child_node.path_cost):

    #             frontier.remove(frontier.index_state(child_node.state))

    #             frontier.insert(child_node)

  

    return None
```
![[4-IIA-2024-infosearch-v2.pdf]]

pruning -> evitare di generare i cammini meno promettenti

h = funzione di valutazione euristica -> $h: n \rightarrow R$  -> si applica al nodo ma dipende solo dallo stato 

$f(n) = g(n) + h(n)$ ove g(n) è il costo del cammino fino al nodo 

Best first -> algoritmo UC ma con uso di f per la coda con priorità -> si prende il nodo + promettente

Greedy Best first -> caso speciale dove f = h

Algoritmo A = algoritmo best first con $f(n) = g(n) + h(n),$ $h(n) \ge 0$ e $h(goal) = 0$
- g(n) = costo cammino percorso per giungere a n
- h(n) stima cost oper raggiungere da n un nodo goal
- h(n) = 0 => UC
- g(n) = 0 => Greedy Best First
- è completo con la condizione $g(n) \ge d(n)*ε,(ε \gt 0)$ ove d(n) indica la profondità

Algoritmo A*:
-  oracolo = $f^*(n) = g^*(n)+h^*(n)$ 
	- ![[Pasted image 20240216171649.png]]
- euristica ammissibile = $\forall{n}. h(n) \le h^*(n)$ -> h è una sottostima
- A* = A in cui h è una funzione euristica ammissibile
- ottimale -> BF (con passi a costo costante) e UC sono ottimali perché h(n) = 0
	- ![[Pasted image 20240216172248.png]]
	- ![[Pasted image 20240216172301.png]]
	- ![[Pasted image 20240216172313.png]]
	- ![[Pasted image 20240219093133.png]]
- A* espande tutti i nodi con f(n) < C
- A* espande alcuni nodi con f(n) = C
- A* non espande alcun nodo con f(n) > C
- stesso algoritmo di UC usando f=g+h (h euristica A*  sennò A)
- A* è completo
- A* è ottimale con euristica monotona
- A* è ottimamente efficiente: a parità di euristica nessun altro algoritmo espande meno nodi (senza rinunciare a ottimalità)
- ![[Pasted image 20240216173313.png]]
- ![[Pasted image 20240219092839.png]]
- UC con f= -d(n), d(n) = profondità nodo => DF
- ![[Pasted image 20240219093705.png]]
- ![[Pasted image 20240219093734.png]]
- $\forall n. h_1(n) \le h_2(n)$ => h2 domina h1 perché h2 è + informata
- ![[Pasted image 20240219094150.png]]
- ![[Pasted image 20240219094322.png]]
- ![[Pasted image 20240219094509.png]]
- ![[Pasted image 20240219094634.png]]
- ![[Pasted image 20240219094719.png]]
- ![[Pasted image 20240219094742.png]]

Beam Search:
- ![[Pasted image 20240219094824.png]]

Algoritmo IDA:
- ![[Pasted image 20240219094900.png]]
- ![[Pasted image 20240219094942.png]]

algoritmo RBFS (best first ricorsivo):
- ![[Pasted image 20240219095149.png]]

algoritmo SMA*:
- ![[Pasted image 20240219095228.png]]

![[Pasted image 20240219095246.png]]

![[5-IIA-2024-oltre_ricerca_classica.pdf]]

![[Pasted image 20240221110310.png]]

![[Pasted image 20240221110400.png]]

Hill climbing:
- ![[Pasted image 20240221110607.png]]
- ASCENT: ![[Pasted image 20240221110740.png]]
- ![[Pasted image 20240221110955.png]]
- ![[Pasted image 20240221111029.png]]
- ![[Pasted image 20240221111059.png]]
Tempra simulata:
- ![[Pasted image 20240221111409.png]]
- ![[Pasted image 20240221111511.png]]
- ![[Pasted image 20240221111551.png]]
- ![[Pasted image 20240221111712.png]]
Local Beam:
- ![[Pasted image 20240221111847.png]]
Beam Search stocastica:
- ![[Pasted image 20240221112235.png]]
Algoritmi genetici:
- ![[Pasted image 20240221112435.png]]
- ![[Pasted image 20240221112721.png]]
- ![[Pasted image 20240221112917.png]]
- ![[Pasted image 20240221113115.png]]
- ![[Pasted image 20240221113138.png]]

Spazi continui => uno stato è descritto da un vettore x di variabili continue

![[Pasted image 20240221113446.png]]

![[Pasted image 20240221113614.png]]

![[Pasted image 20240221113635.png]]

![[Pasted image 20240221113801.png]]

![[Pasted image 20240221113837.png]]

![[Pasted image 20240221113954.png]]



# SECONDA PARTE

![[Parte2_Lezione_1.pdf]]

![[Pasted image 20240225172815.png]]

linguaggio + espressivo => - efficiente

Calcolo proposizionale:
- modello = interpretazione di una formula che la rende vera
- ![[Pasted image 20240225174144.png]]
- $KB\models\alpha (formula) \iff M(KB) \subseteq M(\alpha)$ -> M(..) = insieme modelli di ...
- Model checking:
  ![[Pasted image 20240225174915.png]]
- ![[Pasted image 20240225175055.png]]

![[Parte2_Lezione_2.pdf]]

Equivalenza logica -> $\alpha \equiv \beta \iff a\models \beta$ e $\beta \models \alpha$ -> sono equivalenti se sono vere nello stesso insieme di modelli

![[Pasted image 20240225175427.png]]

una formula è valida $\iff$ se è vera in tutte le interpretazioni -> una formula valida è detta anche tautologia

$\alpha \models \beta \iff (\alpha \implies \beta)$ è valida

una formula è soddisfacibile $\iff$ esiste una interpretazione in cui la formula è vera (esiste un modello della formula) -> SAT = determinare la soddisfacibilità di formule della logica proposizionale

$\alpha$ è valida $\iff \neg\alpha$ è soddisfacibile
$\alpha$ è soddisfacibile $\iff \neg \alpha$  non è valida

![[Pasted image 20240225180145.png]]

![[Pasted image 20240225180221.png]]

![[Pasted image 20240225180324.png]]

disgiunzione,congiunzione -> OR,AND

clausola = disgiunzione di letterali (e/o letterali negati) -> $A \vee B \vee \neg C \vee D$

DPLL:
- ![[Pasted image 20240225181656.png]]
- ![[Pasted image 20240225181755.png]]
- ![[Pasted image 20240225192413.png]]
- ![[Pasted image 20240225192511.png]]

Metodi Locali per SAT:
- ![[Pasted image 20240225192904.png]]
- ![[Pasted image 20240225194638.png]]
- ![[Pasted image 20240225194858.png]]
- ![[Pasted image 20240225195009.png]]
- ![[Pasted image 20240225195052.png]]
- rapporto $\frac{m}{n}$ -> m = \# clausole, \# simboli -> + è grande + il problema è vincolato (complex)

Inferenza di deduzione -> $KB \vdash A$ ovvero A è deducibile da KB

![[Pasted image 20240225195448.png]]

correttezza -> $KB \vdash \alpha \implies KB \models \alpha$

completezza -> $KB \models \alpha \implies KB \vdash \alpha$

schema regola d'inferenza -> $\frac{Premesse}{Conclusione}$ -> $EX:\frac{\{P\},\{\neg P\}}{\{\}}$

![[Pasted image 20240225201346.png]]

Problema di Ricerca:
- ![[Pasted image 20240225201038.png]]
- ![[Pasted image 20240225201101.png]]
- ![[Pasted image 20240225201321.png]]
- ![[Pasted image 20240225201434.png]]
- ![[Pasted image 20240225201502.png]]

![[Parte2_Lezione_3.pdf]]

![[Pasted image 20240227161749.png]]

LOGICA 1 ORDINE:
- concettualizzazione: si tratta di decidere quali sono le cose di cui si vuole parlare -> trovare dominio, funzioni e relazioni interessanti
- oggetti
- funzioni -> relazioni con un solo valore per ogni input
- proprietà -> relazioni unarie
- insieme degli oggetti = dominio del discorso (finito/infinito)
- <dominio,funzioni,relazioni> = concettualizzazione
- Simboli:
	- costante -> rappresentano gli oggetti
	- predicato -> ... relazioni
	- funzione -> ... funzioni
	- Variabile -> un simbolo che rappresenta elementi arbitrari del dominio -> ... oggetti non specificati
	- termine -> expr logica che si riferisce a un oggetto -> Costante|Var|Fun(Termine,...)
	- x = y -> x e y si riferiscono allo stesso oggetto
	- formula atomica -> l'espressione più semplice e indivisibile che afferma una relazione tra oggetti del dominio di discorso. -> predicato seguito da una lista di termini
	- ![[Pasted image 20240227162926.png]]
	- Formula -> Form.Atomica | Form connettivo Form | Quantificatore var Form | NOT Form | (Formula)
	- Quantificatori
		- $\forall$ -> relazione si applica a tutti gli elementi del dominio
		- $\exists$ -> la relazione si applica ad almeno un elemento del dominio
	- ![[Pasted image 20240227163347.png]]
	- variabile in uno scope di un quantificatore -> legata -> altrimenti è libera
	- Formula chiusa -> non ci sono variabili libere
	- Formula aperta -> c'è almeno una variabile libera
	- Formula ground -> non ci sono variabili
	- ![[Pasted image 20240227164013.png]]
-  ![[Pasted image 20240227164202.png]]
-  ![[Pasted image 20240227164240.png]]
- Interpretazione -> stabilire una corrispondenza precisa tra elementi atomici del linguaggio ed elementi della concettualizzazione
- ![[Pasted image 20240227164346.png]]
- ![[Pasted image 20240227164552.png]]
- $\forall x A(x)$ è vera  se è vera per ogni elemento del dominio di A -> con dominio finito è praticamente un grosso AND
- $\exists x A(x)$ è vera se è vera per almeno un elemento del dominio per cui A è vera -> con dominio finito è praticamente un grosso OR
- ![[Pasted image 20240227164957.png]]
- ![[Pasted image 20240227165134.png]]

![[Pasted image 20240227165448.png]]

A\[x/g\] -> sostituiamo g per x in A

Regole di inferenza:
- $\frac{\forall x A[x]}{A[x/g]}$ -> g = termine ground e il denominatore è il risultato della sostituzione di g per x in A
	- ![[Pasted image 20240227171159.png]]
- ![[Pasted image 20240227171449.png]]
- ![[Pasted image 20240227171622.png]]

Teorema di Herbrand:
- $KB \models \alpha \implies$ esiste una dimostrazione che coinvolge solo un sotto-insieme finito della KB proposizionalizzata
- ![[Pasted image 20240227172042.png]]
Forma a clausole:
- costanti, fun e predicati sono come definiti
- ![[Pasted image 20240227172357.png]]
- ![[Pasted image 20240227172415.png]]
- ![[Pasted image 20240227174017.png]]
- ![[Pasted image 20240227174035.png]]
- ![[Pasted image 20240227174155.png]]
- ![[Pasted image 20240227174852.png]]
- ![[Pasted image 20240227174915.png]]
- ![[Pasted image 20240227175142.png]]
- ![[Pasted image 20240227175618.png]]
- 

# ESERCITAZIONI

## PARTE 1

![[es1_teseo-testo-2024.pdf]]

![[es1_teseo-sol-2024.pdf]]

![[es2-testi-2024.pdf]]

![[es2_sol-2024.pdf]]