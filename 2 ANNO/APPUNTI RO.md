## PROGRAMMAZIONE LINEARE

[APPUNTI PROF](https://pages.di.unipi.it/bigi/dida/rob/2223/appunti.html)

Problema avente:
- vettore $\vec{x} = (x_1,...,x_n)\in R^n$ che rappresenta le variabili
- funzione obiettivo -> $f(\vec{x}) = c_1x_1+\dots+c_nx_n = \vec{c}*\vec{x}$ (prodotto scalare) dove $c = (c_1,\dots,c_n)\in R^n$
- vincoli lineari -> $\vec{a}*\vec{x} = a_1x_1+\dots+a_nx_n ( \le,\ge,<,>)$ b dove $\vec{a}=(a_1,\dots,a_n)\in R^n$ e $b \in R$

>forma canonica:
>max $\vec{c}*\vec{x}$ 
>$A*\vec{x} \le \vec{b}$ con $\vec{b} \in R^m$ (componente per componente)
>i vincoli si considerano come le righe di una matrice $A \in R^{m*n}$ 
>( m = numero vincoli, n=numero variabili, $m \ge n$ )

trasformazioni in forma canonica:
1. min $\vec{c}*\vec{x} =$ $-max (-\vec{c})*\vec{x}$
2. $A_i*\vec{x}=b_i \equiv A_i*\vec{x} \le b_i$ , $A_i*\vec{x} \ge b_i$
3. $A_i*\vec{x} \ge b_i \equiv (-A_i)*\vec{x} \le -b_i$
4. $A_i*\vec{x} \ge b_i \equiv A_i*\vec{x}-s=b_i$ con $s \ge 0$
5. $A_i*\vec{x} \ge b_i \equiv A_i*\vec{x}+s=b_i$ con $s \ge 0$
6. $s \in R$ è una variabile di scarto che misura lo scarto tra $A_i*\vec{x}$ **e** $b_i$

>Esempio di forma canonica:
>![](R1.jpeg)

regione di spazio ammissibile del problema -> $P=\{\vec{x} \in R^n : A*\vec{x} \le \vec{b}\}$-> è identificata dall'intersezione dei semipiani ottenuti dai vincoli (ovvero un poliedro) 

faccia del poliedro ->dato $I \subseteq\{1,\dots,m\}$ ( insieme dei vincoli attivi ( soddisfatti come uguaglianze ) ) e $P_I=\{\vec{x} \in P: A_i*\vec{x} \le b_i$  $\forall i \in I\}\ne \emptyset$, le facce costituite da un solo punto sono dette *vertici*

>Esempio (riferito ad esempio precedente):![](R2.jpeg)

se un vertice viene identificato da più di n vincoli attivi, non per forza significa che almeno uno di quei vincoli sia "superfluo" (ciò è vero in $R^2$)

$\bar{x} \in P$ -> $I_{(\bar{x})}=\{i : A_i*\bar{x}=b_i\}$ => $A_i*\bar{x}=b_i$ $\forall i \in I_{(\bar{x})}$ => $A_{I_{(\bar{x})}}*\bar{x}=\vec{b}_{I_{(\bar{x})}}$ dove :
- $A_{I_{(\bar{x})}}$ è una sottomatrice di A ottenuta prendendo solo le righe i cui indici appartengono ad $I_{(\bar{x})}$ 
- $\vec{b}_{I_{(\bar{x})}}$ è un sottovettore di $\vec{b}$ ottenuto prendendo le componenti i cui indici appartengono ad $I_{(\bar{x})}$

>Esempio(riferito agli esempi precedenti)![](R3.jpeg)

Essendo il det di $A_{I_{(\bar{x})}}$ diverso da zero, $A_{I_{(\bar{x})}}$ è invertibile => $\bar{x} = A^{-1}_{I_{(\bar{x})}} * \vec{b}_{I_{(\bar{x})}}$ perche n=m

Se A ha rango = n, tutte le colonne sono LI tra loro, allora il poliedro ha almeno un vertice

Involucro convesso = $conv_{\{x^1,\dots,x^s\}}=\{\sum_{i=1}^{s}\lambda_{i}*x^i:\lambda_{i} \ge 0, \sum_{i=1}^{s} \lambda_{i} = 1\}$ -> gli elementi sono punti

al variare di $\lambda_i$ viene descritta la combinazione convessa, segmento composto dagli s punti, che forma un poliedro limitato nello spazio (non va all'infinito) i cui vertici sono un sottoinsieme degli $x^i$

Un insieme è convesso se presi 2 punti tutto il segmento tra di loro è contenuto nell'insieme

involucro conico = $cono_{\{v^1,\dots,v^t\}}=\{\sum_{j=1}^{t} \gamma_j*v^j : \gamma_j \ge 0\}$ -> un cono è una regione dello spazio nel quale, se ci appartiene un vettore, allora ci appartengono tutti i suoi multipli -> gli elementi sono vettori (direzioni)

>Teorema decomposizione di poliedri (Motzkin):
>Sia $P \subseteq R^n$ un regione dello spazio $R^n$
>P poliedro $\Leftrightarrow$ $\exists x^1,\dots,x^s,v^1,\dots,v^t \in R^n : P=conv_{\{x^1,\dots,x^s\}}+cono_{\{v^1,\dots,v^t\}}$

Proprietà $X=\{x^1,\dots,x^s\},V=\{v^1,\dots,v^t\}$:
- P è limitato $\Leftrightarrow V=\{0\}$
- $P=\{\vec{x} \in R^n : A*\vec{x} \le \vec{b}\} \Rightarrow cono_{(V)}=\{\vec{v} \in R^n : A*\vec{v} \le 0\}$
- $\vec{v} \in cono_{(V)} \Leftrightarrow \forall \vec{x} \in P, \forall \alpha \ge 0:\vec{x}+\alpha \vec{v} \in P$-> il poliedro nella direzione $\vec{v}$ sta recedendo all'infinito
- Se un poliedro possiede dei vertici, allora $X=\{vertici\}$-> un poliedro è l'involucro convesso dei suoi vertici, più le direzioni in cui recede all'infinito

>Teorema fondamentale della PL:
>Sia $P=conv_{\{x^1,\dots,x^s\}}+cono_{\{v^1,\dots,v^t\}} \subseteq R^n$ un poliedro
>$max\{\vec{c}*\vec{x}:\vec{x} \in P\}$ ha ottimo finito $\Leftrightarrow \vec{c}*v^j \le 0 ,\forall j=1,\dots,t$
>Allora $\exists i \in \{1,\dots,s\}:x^i$ è una soluzione ottima 

>coppia simmetrica di problemi di PL:
>$min\{\vec{y}*\vec{b}:\vec{y}*A \ge \vec{c},\vec{y}\ge 0\}$ -> i vincoli della matrice si leggono per colonne (n vincoli e m variabili)
>$max\{\vec{c}*\vec{x}:A*\vec{x} \le \vec{b},\vec{x} \ge 0\}$ -> Vincoli della matrice si leggono per righe (n variabili e m vincoli)

>coppia assimmetrica di problemi di PL:
>$min\{\vec{y}*\vec{b}:\vec{y}*A = \vec{c},\vec{y}\ge 0\}$ -> Problema duale (D)
>$max\{\vec{c}*\vec{x}:A*\vec{x} \le \vec{b}\}$ -> Problema primale (P)
$A \in R^{n*m},\vec{b} \in R^m, \vec{c} \in R^n$

>Dualità debole:
Sia $\vec{x} \in R^n$ una soluzione ammissibile per (P) e $\vec{y} \in R^m$ una soluzione ammissibile per (D), allora $\vec{c}*\vec{x} \le \vec{y}*\vec{b}$

>Dimostrazione:![](R4.jpeg)

(P) superiormente illimitato => (D) vuoto (no soluzioni ammissibili)<br>
(D) è inferiormente illimitato => (P) vuoto (no soluzioni ammissibili)<br>
$max\{\vec{c}*\vec{x}:A*\vec{x} \le \vec{b}\} \le min\{\vec{y}*\vec{b}:\vec{y}*A = \vec{c},\vec{y}\ge 0\}$

Sia $\vec{x} \in R^n$ una soluzione ammissibile per (P) e $\vec{y} \in R^m$ una soluzione ammissibile per (D), $\vec{c}*\vec{x}=\vec{y}*\vec{b} \Rightarrow \vec{x}$ e $\vec{y}$ sono soluzioni ottime rispettivamente per (P) e (D)

![](R5.jpeg)

direzione ammissibile per $\vec{x}$ la quale mantiene il punto all'interno del poliedro, se esiste $\lambda>0$ tale che $\vec{x}+\lambda\vec{\xi}$ è ammissibile per (P), $\forall \lambda \in [0,\lambda]$

![](R6.jpeg)

$\vec{c}*\vec{\xi}>0 \Rightarrow$ la direzione è di crescita

>$\vec{x} \in R^n$ è una soluzione ammissibile ottima per (P) $\Leftrightarrow$ non ammette direzioni ammissibili e di crescita

>$\vec{\xi} \in R^n$ è una direzione ammissibile  per $\vec{x}\Leftrightarrow A_i*\vec{\xi} \le 0, \forall i \in I_{(\vec{x})}$

se non presenti vincoli attivi, il punto si trova all'interno del poliedro e qualsiasi direzione è ammissibile

> Lemma di Farkas:![](R7.jpeg)

>Dualità forte:
>Si suppone che (P) e (D) abbiano regioni ammissibili non vuote
>$max\{\vec{c}*\vec{x}:A*\vec{x} \le \vec{b}\} = min\{\vec{y}*\vec{b}:\vec{y}*A = \vec{c},\vec{y}\ge 0\}$

(P) superiormente illimitato $\Rightarrow$ (D) vuoto (no soluzioni ammissibili)
(D) è inferiormente illimitato $\Rightarrow$ (P) vuoto (no soluzioni ammissibili)
(P) ha finito $\Leftrightarrow$ (D) ha finito

>Siano $\vec{x}\in R^n,\vec{y}\in R^m$ soluzioni ammissibili rispettivamente per (P) e (D)
>$\vec{c}*\vec{x}=\vec{y}*\vec{b} \Leftrightarrow \vec{x},\vec{y}$ siano soluzioni ottime rispettivamente per (P) e (D)
>$\Leftarrow$ (dualità forte)
>$\Rightarrow$ (dualità debole)

>Scarti complementari:
>Siano $\vec{x}\in R^n,\vec{y}\in R^m$ soluzioni ammissibili rispettivamente per (P) e (D)
>$\vec{y}*(\vec{b}-A*\vec{x}) = 0 \Leftrightarrow \vec{x},\vec{y}$ siano soluzioni ottime rispettivamente per (P) e (D)![](R8.jpeg)

per trovare 2 soluzioni ottime:
- a partire da $\vec{x}$, si controlla quali sono i vincoli attivi ($i \in I_{(\vec{x})}$)
- si impostano a zero tutte le $\overline{y_i}$ dei vincoli non attivi
- si cerca l'ammissibilità, ovvero si risolve:![](R9.jpeg)

Gli scarti complementari sono soddisfatti quando:
- $A_i*\vec{x}<b_i \rightarrow \overline{y_i}=0$, ovvero a un vincolo non attivo in (P) corrisponde una variabile di (D) posta a 0
- $\overline{y_i}>0 \rightarrow A_i*\vec{x}=b_i$, ovvero a una variabile positiva del problema (D) corrisponde un vincolo attivo

![](R10.jpeg)

>passaggi per verificare l'ottimalità di una soluzione:
>- si scrivono $\vec{c},\vec{b}$ e la matrice A del problema (P)
>- si scrive il problema (D) corrispondente
>- costruire $\vec{y}$ ammissibile di (D) in scarti complementari con $\vec{x}$:
>- si trovano i vincoli attivi (vincoli rispettati come uguaglianze) da $\vec{x}$
>- si pongono a 0 le variabili di (D) che appartengono ai indici dei vincoli non attivi
>- si risolve il sistema per trovare le variabili di (D) che appartengono ai vincoli attivi ( devono essere >=0)

![](R11.jpeg)

Sia $B \subseteq \{1,\dots,n\}$ una base ( $|B|=n$ e $A_B \in R^{n*n}$ è invertibile )

Sia $\vec{x}=A^{-1}_B*\vec{b_B}$ la soluzione primale (unico punto in cui i vincoli sono attivi, i vertici sono tutte le soluzioni primali di base possibili)

una soluzione primale di base può essere:
- Degenere-> $\exists i \notin B : A_i*\vec{x}=b_i$ oppure $B \subset I_{(\vec{x})}$
- ammissibile, $A_N*\vec{x} \le b_N$ (con $N=\{1,\dots,m\}\setminus B$), ovvero rispettando i vincoli che non appartengono alla base, è un vertice

Sia $\vec{y}=(\vec{y_B},\vec{y_N})$, con $\vec{y_B}=\vec{c}*A^{-1}_B$ e $\vec{y_N}=0$, una soluzione duale di base (le componenti dei vincoli non in base devono essere uguali a 0 per rispettare gli scarti complementari)

una soluzione duale di base può essere:
- Degenere-> $\exists i \in B : \vec{y_i}=0$ ovvero una componente della base è nulla (B non è unica)
- ammissibile, $\vec{y_B}=\vec{c}*A^{-1}_B \ge 0$

![](R12.jpeg)

![](R13.jpeg)

>Algoritmo Simplesso Primale:
>Sia B una base primale ammissibile, così da avere un vertice 
>1. Si calcolano le due soluzioni di base $\vec{x}=A^{-1}_B*\vec{b_B}$ e $(\vec{y_B},\vec{y_N})=(\vec{c}*A^{-1}_B,0)$
>2. se tutte le componenti $\vec{y_B} \ge 0$ allora STOP ($\vec{x},\vec{y}$ sono soluzioni ottime rispettivamente per (P) e (D))
>3. Si sceglie un indice uscente $h \in B : \vec{y_h} \le 0$
>4. direzione di crescita $\vec{\xi}=-A^{-1}_B * \vec{u_{B(h)}}$
>5. Si calcola il passo di spostamento $\lambda = min\{\lambda_i:i \in N\}$ lungo la direzione $\vec{\xi}$ con:
>- $\lambda_i = (b_i-A_i*\vec{x})/(A_i*\vec{\xi})$ se $A_i*\vec{\xi} >0$
>- $\lambda_i = +\infty$ se $A_i*\vec{\xi} \le 0$
>6. Se tutti gli $\lambda_i = +\infty$ allora STOP ( (P) superiormente illimitato e (D) vuoto )
>7. Si sceglie un indice entrante $k \in N:\lambda = \lambda_k$
>8. Cambio di base -> $B'=B\setminus\{h\} \cup \{k\}$
>9. ritorno a 1

>Regola anticiclo di Bland:
>$h=min\{i \in B: \vec{y_i}<0\}$ e $k=min\{i \in N : \lambda = \lambda_i\}$

![](R14.jpeg)

[ESERCIZIO ESEMPIO](https://unipiit-my.sharepoint.com/:o:/r/personal/g_pasquini6_studenti_unipi_it/Documents/Dispense/Secondo%20anno/Primo%20semestre/Ricerca%20operativa/Appunti%20lezione/Ricerca%20Operativa?d=w21951a37895e44c08e7b74e1fb324836&csf=1&web=1&e=dTjbp4)

>Algoritmo Simplesso Duale:
>Sia B una base duale ammissibile, così da avere un vertice 
>1. Si calcolano le due soluzioni di base $\vec{x}=A^{-1}_B*\vec{b_B}$ e $(\vec{y_B},\vec{y_N})=(\vec{c}*A^{-1}_B,0)$
>2. se tutte le componenti $A_N*\vec{x} \le b_N$ con ( $N=\{1,\dots,m\}\setminus B$ ) allora STOP ( $\vec{x},\vec{y}$ sono soluzioni ottime rispettivamente per (P) e (D) )
>3. Si sceglie un indice entrante $k=min\{i \in N: A_i*\vec{x}>b_i\}$
>4. direzione di decrescita $\vec{d}=(-\eta_B,1(k),0(N\setminus\{k\}))$ con $\eta_B = A_k*A^{-1}_B$
>5. Si calcola il passo di spostamento $\Theta = min\{\Theta_i:i \in B\}$ lungo la direzione $\vec{d}$ con:
>- $\Theta_i = \overline{y_i}/\eta_i$ se $\eta_i >0$
>- $\Theta_i = +\infty$ se $\eta_i \le 0$
>6. Se tutti gli $\Theta_i = +\infty$ allora STOP ( (D) inferiormente illimitato e (P) vuoto )
>7. Si sceglie un indice uscente $h = min\{i \in B : \Theta=\Theta_i\}$
>8. Cambio di base -> $B'=B\setminus\{h\} \cup \{k\}$
>9. ritorno a 1

[ESERCIZIO ESEMPIO](https://unipiit-my.sharepoint.com/personal/g_pasquini6_studenti_unipi_it/_layouts/15/Doc.aspx?sourcedoc={21951a37-895e-44c0-8e7b-74e1fb324836}&action=view&wd=target%28Terzo%20compitino%2C%2016.%20-%2024.%20Lezione.one%7C59eac0db-06a7-43fb-ac10-fc55af3e2c6b%2FAlgoritmo%20del%20simplesso%20duale%7Cf92df589-1986-f240-8ebf-b65f5c0f5f2d%2F%29&wdorigin=NavigationUrl)

![](R15.jpeg)

Se tutti i vertici di (P) sono  a componenti intere allora (P) ammette soluzione ottima a componenti intere ( analogo per (D) )

In PLI è presente la dualità debole, essendo le soluzioni ($P_I$) e ($D_I$) rispettivamente soluzioni particolari di (P) (D), ma non è presente la dualità forte per via del vincolo di interezza

scopo in un problema di PLI -> costruire l'involucro convesso del reticolo S<br>
$conv(S)=\{\sum_{i=1}^{n+1}\lambda_{i}*x^i:x^i \in S, \sum_{i=1}^{n+1} \lambda_{i} = 1,\lambda_i \ge 0\}$

Se S è un reticolo finito allora conv(S) è un poliedro con la proprietà dell'interezza 

Se S è un reticolo infinito (quantità numerabile ma infinita di punti) allora conv(S) non è un poliedro

se $P=\{\vec{x}\in R^n : A*\vec{x} \le \vec{b}\}$, con $A \in Z^{m*n}$ e $\vec{b} \in Z^m$ allora $conv(P \cap Z^n)$ è un poliedro

un vincolo di disuguaglianza soddisfatto da tutti i punti del reticolo intero è detto disuguaglianza valida

un piano di taglio è una disugualianza valida che taglia la soluzione ottima, non a componenti intere, ottenuta dal rilassamento continuo (non soddisfa la disuguaglianza)

![](R16.jpeg)

[ESERCIZIO ESEMPIO](https://unipiit-my.sharepoint.com/personal/g_pasquini6_studenti_unipi_it/_layouts/15/Doc.aspx?sourcedoc={21951a37-895e-44c0-8e7b-74e1fb324836}&action=view&wd=target%28Terzo%20compitino%2C%2016.%20-%2024.%20Lezione.one%7C59eac0db-06a7-43fb-ac10-fc55af3e2c6b%2FProgrammazione%20Lineare%20Intera%7C1dad2350-ad73-2e45-99b2-07219031594f%2F%29&wdorigin=NavigationUrl)

i metodi enumerativi permettono di enumerare e analizzare le possibili soluzioni di problemi PLI di natura combinatoria (numero finito di possibili soluzioni aventi variabili binare ( $x\in\{0,1\}^n$ ) il cui numero massimo di soluzioni possibili ( ammissibili o meno ) sono pari a $2^n$ 

>Branch and Bound (ramificazione e potatura):
>1. una soluzione ammissibile di partenza, attraverso tecniche euristiche
>2. regole di ramificazione, per costruire dinamicamente l'albero
>3. un rilassamento del problema, per confrontare più facilmente la soluzione ammissibile con la stima della soluzione ottima di un sottoproblema
>4. regola di potatura, per non far analizzare parti inutili:
>- il valore ottimo del rilassamento del sottoproblema analizzato non è migliore del valore dell'attuale soluzione ammissibile
>- la soluzione ottima del rilassamento del sottoproblema è ammissibile per il problema di partenza (è migliore di quella attuale)
>- il sottoalbero non contiene soluzioni ammissibili per il problema di partenza

PROBLEMA ZAINO:
- b>0 -> capacità zaino
- n oggetti -> $c_i>0$ beneficio e $a_i>0$ peso per ogni i-esimo oggetto
- $\forall i$  $a_i \le b$  e  $\sum_i a_i>b$

>formulazione come PLI:
> max  $c_1*x_1+\dots+c_n*x_n$
>$a_1*x_1+\dots+a_n*x_n \le b$
>$x_i \in \{0,1\}$

![](R17.jpeg)

[ZAINO SPIEGATO CON ESERCIZIO](https://unipiit-my.sharepoint.com/personal/g_pasquini6_studenti_unipi_it/_layouts/15/Doc.aspx?sourcedoc={21951a37-895e-44c0-8e7b-74e1fb324836}&action=view&wd=target%28Terzo%20compitino%2C%2016.%20-%2024.%20Lezione.one%7C59eac0db-06a7-43fb-ac10-fc55af3e2c6b%2FProblema%20dello%20zaino%7Cc69859b6-a5e7-b742-a552-fc9ee9fa7296%2F%29&wdorigin=NavigationUrl)

COMMESSO VIAGGIATORE:

G = (N,A)-> grafo completo non orientato dove N sono le città e A le connessioni e per ogni arco $(i,j)\in A$ è associato un costo $c_{ij}$ che indica il tempo di percorrenza da una città i ad una città j

Lo scopo è quello di trovare un ciclo hamiltoniano (tutti i nodi 1 volta sola) di costo minimo (costo = somma costi archi che lo compongono)

$x_{ij}$ = 1 ( se ( i,j ) appartiene al ciclo ) oppure 0 ( else )

>formulazione come PLI:
>$min\sum_{(i,j)\in A} c_{ij}*x_{ij}$
>$\sum_{(i,j)\in A_k} x_{ij}=2, \forall k \in N$ -> $A_k$ = insieme archi incidenti nel k-esimo nodo
>$\sum_{(i,j)\in A_{(N',N'')}} x_{ij}\ge 2, \forall taglio(N',N'')$-> almeno 2 archi devono attraversare il taglio
>$x_{ij} \in \{0,1\}$

![TUTTI I CICLI HAMILTONIANI SONO K-ALBERI (NO VICEVERSA)](R18.jpeg)

[ESERCIZIO SPIEGATO](https://unipiit-my.sharepoint.com/personal/g_pasquini6_studenti_unipi_it/_layouts/15/Doc.aspx?sourcedoc={21951a37-895e-44c0-8e7b-74e1fb324836}&action=view&wd=target%28Terzo%20compitino%2C%2016.%20-%2024.%20Lezione.one%7C59eac0db-06a7-43fb-ac10-fc55af3e2c6b%2FProblema%20del%20commesso%20viaggiatore%20%28TSP%5C%29%7Ca610e076-6e48-cb4e-97ab-41216b3b98de%2F%29&wdorigin=NavigationUrl)

![](R19.jpeg)


