$\newcommand {\R}{\mathbb{R}}$

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
ricerca su grafo -> controllando se i nodi (stati) siano già stati esplorati -> esplora uno stato al più una volta -> frontiera separa nodi esplorati da quelli non esplorati
ricerca bidirezionale ->  si procede sia da start che da goal per incontrarsi ->complex spazio e tempo : $O(b^{d/2})$

 **distanza di Manhattan** = $|x_1-x_2|+|y_1-y_2|$

Algoritmi non informati:
- BF -> FIFO -> inserisco in coda ed estraggo dalla testa (QUEUE) -> inserimento e estrazione agli estremi:
	- strategia completa
	- strategia ottimale se  gli operatori hanno tutti lo stesso costo k, cioè g(n) = k · depth(n), dove g(n) è il costo del cammino per arrivare a n
	- complex tempo: $O(b^{d})$ 
	- complex spazio: $O(b^{d})$  -> dim frontiera
	- ![[Pasted image 20240302154651.png]]
- DF -> LIFO -> inserisco ed estraggo dalla testa (STACK) -> inserimento e estrazione stesso punto
	- complex tempo: $O(b^m)$ con b = fattore di diramazione e m = lunghezza max dei cammini nello spazio degli stati
	- complex spazio: bm (frontiera sul cammino)
	- versione su albero -> no completa e no ottimale
	- versione su grafo -> si perde vantaggio sulla memoria -> completa solo in spazi di stati finiti
	- ![[Pasted image 20240302154712.png]]
- DL -> DF limitato
	- strategia completa se d < l, d= profondità nodo obiettivo più superficiale 
	- non ottimale
	- complex tempo: $O(b^l)$
	- complex spazio : $O(b*l)$
- ID -> approfondimento iterativo -> DL con l=0 che poi incrementa per ogni interazione
	- completo
	- ottimale per costo fisso di operazione (come BF)
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

CODICI PYTHON -> CODICI/IIA/...

![[4-IIA-2024-infosearch-v2.pdf]]

pruning -> evitare di generare i cammini meno promettenti

h = funzione di valutazione euristica -> $h: n \rightarrow R$  -> si applica al nodo ma dipende solo dallo stato 

$f(n) = g(n) + h(n)$ ove g(n) è il costo del cammino fino al nodo 

Best first -> algoritmo UC ma con uso di f per la coda con priorità -> si prende il nodo + promettente

Greedy Best first -> caso speciale dove f = h

Algoritmo A = algoritmo best first con $f(n) = g(n) + h(n),$ $h(n) \ge 0$ e $h(goal) = 0$
- g(n) = costo cammino percorso per giungere a n
- h(n) stima costo per raggiungere da n un nodo goal
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
- $\forall n. h_1(n) \le h_2(n)$ => $h_2$ domina $h_1$ perché $h_2$ è + informata => $h_2$ efficiente almeno quanto $h_1$
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
- (conseguenza logica)$KB\models\alpha (formula) \iff M(KB) \subseteq M(\alpha)$ -> M(..) = insieme modelli di ...
- Model checking:
  ![[Pasted image 20240225174915.png]]
- ![[Pasted image 20240225175055.png]]

![[Parte2_Lezione_2.pdf]]

Equivalenza logica -> $\alpha \equiv \beta \iff a\models \beta$ e $\beta \models \alpha$ -> sono equivalenti se sono vere nello stesso insieme di modelli

![[Pasted image 20240225175427.png]]

una formula è valida $\iff$ se è vera in tutte le interpretazioni -> una formula valida è detta anche tautologia

Teorema di deduzione : $\alpha \models \beta \iff (\alpha \implies \beta)$ è valida

Teorema di refutazione: $KB \models \alpha \iff (KB \land \neg \alpha)$ è insoddisfacibile 

una formula è soddisfacibile $\iff$ esiste una interpretazione in cui la formula è vera (esiste un modello della formula) -> SAT = determinare la soddisfacibilità di formule della logica proposizionale

$\alpha$ è valida $\iff \neg\alpha$ è insoddisfacibile
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
- $\forall x .A(x)$ è vera  se è vera per ogni elemento del dominio di A -> con dominio finito è praticamente un grosso AND
- $\exists x .A(x)$ è vera se è vera per almeno un elemento del dominio per cui A è vera -> con dominio finito è praticamente un grosso OR
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


# TERZA PARTE

![[IIA-24-ML-INTRO-v0.1.pdf]]

![[Pasted image 20240324080700.png]]

Supervised Learning:
- Classification -> discreto
- Regression -> continuo
- \<x,d\> -> labeled training example \<input,output\> -> d= target value / desiderate value of unknown f(x) (categorical o numerical label)
- h hypotesis = approx di f(x) per unseen data x'

Unsupervised Learning:
- TR = training  set = set di unlabeled data \<x\>
- Clustering = Partition of data into clusters (subsets of “similar” data)

![[Pasted image 20240324081749.png]]

Linguaggi per esprimere modelli (le ipotesi h):
- logica (prop)
- equazioni numeriche
- probabilità

tipi di rappresentazoini di ipotesi:
- Linear models:
	- ![[Pasted image 20240324082329.png]]
- Symbolic Rules:
	- ![[Pasted image 20240324082352.png]]
- Probabilistic model:
	- estimate p(x,y)


![[Pasted image 20240324082446.png]]

Local search approaches

LEARNING = search of good function in a function space from known data -> Good (generalization error) =  it measures how accurately the model predicts over novel samples of data ( Error/Loss measured over new data) (low error, high accuracy and vice versa)

Generalization:
- Learning phase (training, fitting) = build the model from know data (training data) (e bias)
- Predictive phase (test) = aplly to new examples
- evaluation of the predictive hypothesis, i.e. of the generalization capability


performance in ML = predictive accuracy -> estimated by the error computed on the (Hold out) Test Set

Basic Background:
- $a \cdot b = a_1b_1+a_2b_2+\dots+a_nb_n = \sum^n_{i=1}a_ib_i$
- $a \cdot b = |a| |b| cos \Theta$
- Norma Euclidea = $\sqrt{\sum_i x_i^2}$ = $||x||$
- ![[Pasted image 20240324084509.png]]
- Cauchy-Schwarz inequality = $|<x,y>| \le ||x||*||y||,\forall x,y \in V$
- grad f = $\sum_{i=1}^n e_i * der.parziale(x_i)$ -> $e_i$ = vettori canonici
- +gradiente = direzione in cui la fun cresce
- -gradiente = la direzione in cui la fun decresce
- stationary point = the gradient is null


![[IIA-24-ML-concept-learning-v0.1.pdf]]

Classification = f(x) return the (assumed) correct class for x (discrete-valued function)
Regression = approximate a real-valued target function (in $\R$ o $\R^K$ )

![[Pasted image 20240324090039.png]]

|H| = dim insieme ipotesi = $2^{2^n}$  = $2^{\#instances}$ = dove n (per binary input/output) è la dim dell'input

ipotesi h = congiunzione  di constraints on attributes -> spefici value, ?, no value allowed (ipotesi nulla) $\emptyset$ 

$<\emptyset,\dots,\emptyset>$ -> most specific
$<?,\dots,?>$ -> most generic

![[Pasted image 20240324104920.png]]

![[Pasted image 20240324104949.png]]

![[Pasted image 20240324105246.png]]


Find-S algorithm :
> ![[IIA-24-ML-concept-learning-v0.1.pdf#page=18]]

Version Space:
- ![[Pasted image 20240324124731.png]]

![[Pasted image 20240324124827.png]]

![[Pasted image 20240324125356.png]]

![[Pasted image 20240324130236.png]]

![[Pasted image 20240324160852.png]]

![[Pasted image 20240324160945.png]]

![[Pasted image 20240324160959.png]]

![[Pasted image 20240324161055.png]]

![[Pasted image 20240324161147.png]]

![[Pasted image 20240324161218.png]]



![[IIA-24-ML-linear-v0.1.pdf]]


![[Pasted image 20240410111939.png]]

![[Pasted image 20240410112021.png]]

![[Pasted image 20240410112227.png]]

![[Pasted image 20240410112938.png]]

![[Pasted image 20240410113038.png]]

![[Pasted image 20240410113156.png]]

![[Pasted image 20240410113508.png]]

![[Pasted image 20240410113557.png]]

![[Pasted image 20240410113615.png]]

![[Pasted image 20240410114429.png]]

![[Pasted image 20240410114632.png]]

![[Pasted image 20240410115700.png]]

![[Pasted image 20240410120101.png]]

![[Pasted image 20240410120129.png]]

![[Pasted image 20240410120216.png]]

![[Pasted image 20240410120252.png]]

![[Pasted image 20240410121153.png]]

![[Pasted image 20240410121203.png]]

![[Pasted image 20240410121215.png]]

![[Pasted image 20240410121253.png]]


![[Pasted image 20240410121337.png]]

![[Pasted image 20240410121400.png]]

![[Pasted image 20240410123124.png]]

![[Pasted image 20240410123706.png]]

![[Pasted image 20240410123723.png]]

![[Pasted image 20240411111521.png]]

![[Pasted image 20240412111355.png]]

![[Pasted image 20240412111448.png]]

![[Pasted image 20240412111545.png]]

![[Pasted image 20240412111640.png]]

![[Pasted image 20240412111720.png]]


![[IIA-24-ML-DT-v0.1.pdf]]

![[Pasted image 20240412135516.png]]

![[Pasted image 20240412135539.png]]

![[Pasted image 20240412135556.png]]

![[Pasted image 20240412135722.png]]

![[Pasted image 20240412135747.png]]

![[Pasted image 20240412135809.png]]

![[Pasted image 20240412135818.png]]

![[Pasted image 20240412135830.png]]

![[Pasted image 20240412135842.png]]

![[Pasted image 20240412135853.png]]

![[Pasted image 20240412135903.png]]

![[Pasted image 20240412135919.png]]

![[Pasted image 20240412135930.png]]

![[Pasted image 20240412135942.png]]

![[Pasted image 20240412135952.png]]

![[Pasted image 20240412140006.png]]

![[IIA-24-ML-VALID-SLT-v0.1.pdf]]

![[Pasted image 20240417152258.png]]

![[Pasted image 20240417152449.png]]

![[Pasted image 20240417152511.png]]

![[Pasted image 20240417152539.png]]

![[Pasted image 20240417152824.png]]

![[Pasted image 20240417153029.png]]

![[Pasted image 20240417153050.png]]

![[Pasted image 20240417153246.png]]

![[Pasted image 20240417153527.png]]

![[Pasted image 20240417153625.png]]

![[Pasted image 20240417153719.png]]

![[Pasted image 20240417153740.png]]

![[Pasted image 20240417153946.png]]

![[Pasted image 20240417154022.png]]

![[Pasted image 20240417154158.png]]

![[Pasted image 20240417154222.png]]

![[Pasted image 20240417154244.png]]

![[Pasted image 20240417154312.png]]

![[Pasted image 20240417154425.png]]

![[Pasted image 20240417154614.png]]

![[Pasted image 20240417154644.png]]

![[IIA-24-ML-SVM-v0.1.pdf]]

![[Pasted image 20240417155740.png]]

![[Pasted image 20240417155818.png]]

![[Pasted image 20240417155847.png]]

![[Pasted image 20240417160039.png]]

![[Pasted image 20240417160115.png]]

![[Pasted image 20240417160142.png]]

![[Pasted image 20240417160158.png]]

![[Pasted image 20240417160302.png]]

![[Pasted image 20240417160326.png]]

![[Pasted image 20240421180631.png]]

![[Pasted image 20240421180721.png]]

![[Pasted image 20240421180904.png]]

![[Pasted image 20240421181150.png]]

![[Pasted image 20240421181206.png]]

![[Pasted image 20240421181311.png]]

![[Pasted image 20240421181345.png]]

![[Pasted image 20240421181550.png]]

![[Pasted image 20240421181812.png]]

![[Pasted image 20240421181910.png]]

![[Pasted image 20240421182106.png]]

![[IIA-24-ML-MIX-kNN-UNSUP-and-others-v.0.1.pdf]]

![[Pasted image 20240421193729.png]]

![[Pasted image 20240422105938.png]]

![[Pasted image 20240422105956.png]]

![[Pasted image 20240422110105.png]]

![[Pasted image 20240422110134.png]]

![[Pasted image 20240422110145.png]]

![[Pasted image 20240422110156.png]]

![[Pasted image 20240422110210.png]]

![[Pasted image 20240422111056.png]]

![[Pasted image 20240422111126.png]]

![[Pasted image 20240422111137.png]]

![[Pasted image 20240422111318.png]]

![[Pasted image 20240422111512.png]]

![[Pasted image 20240422114150.png]]

![[Pasted image 20240422114204.png]]

![[Pasted image 20240422114216.png]]

![[Pasted image 20240423162426.png]]

![[Pasted image 20240423162643.png]]

![[Pasted image 20240423162802.png]]

![[Pasted image 20240423162817.png]]

![[Pasted image 20240423162951.png]]

![[Pasted image 20240423163017.png]]

![[Pasted image 20240423163046.png]]

![[Pasted image 20240423163111.png]]

![[Pasted image 20240423163154.png]]

![[Pasted image 20240423163210.png]]



# ESERCITAZIONI

## PARTE 1

![[es1_teseo-testo-2024.pdf]]

![[es1_teseo-sol-2024.pdf]]

![[es2-testi-2024.pdf]]

![[es2_sol-2024.pdf]]

## PARTE 2
![[Parte2_Esercitazione1.pdf]]

![[Parte2_Esercitazione2.pdf]]