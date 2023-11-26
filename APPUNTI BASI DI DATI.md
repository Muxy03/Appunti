
DDL -> Data Definition Language

3 livelli di schemi:
1. livello vista logica -> descrizione dell'aspetto della base di dati ad una certa applicazione
2. livello logico -> descrizione logica dei dati e delle loro relazioni senza riferimento all'organizzazione fisica in memoria
3. livello fisico -> descrizione organizzazione fisica dei dati in memoria e delle strutture dati ausiliari

Indipendenza logica: i programmi applicativi non devono essere modificati in seguito a modifiche dello schema logico. 

Indipendenza fisica: i programmi applicativi non devono essere modificati in seguito a modifiche dell’organizzazione fisica dei dati.

DDL -> definizione schemi
DML  (Data Manipulation Language) -> query e aggiornamento istanze di base di dati

![[Pasted image 20231112000758.png]]

![[Pasted image 20231112000807.png]]

![[Pasted image 20231112000911.png]]

![[Pasted image 20231112002046.png]]

![[Pasted image 20231112001250.png]]

![[Pasted image 20231112001510.png]]

tipi di proprietà:
- atomica/strutturata 
- totale(obbligatoria)/parziale(opzionale) 
- costante/variabile
- calcolata/non calcolata 

![[Pasted image 20231112001933.png]]

![[Pasted image 20231112001345.png]]

![[Pasted image 20231112001731.png]] 

Una classe è un insieme di oggetti dello stesso tipo, modificabile con operatori per includere o estrarre elementi dall’insieme.

![[Pasted image 20231112002210.png]]

tipi di associazioni:
- totale ->(surgettiva) se per ogni elemento di X corrisponde almeno un elemento di Y
- parziale -> opposto totale

![[Pasted image 20231112002601.png]]

![[Pasted image 20231112002621.png]]

![[Pasted image 20231112002702.png]]

![[Pasted image 20231112002853.png]]

![[Pasted image 20231112002953.png]]

![[Pasted image 20231112003010.png]]

Disgunzione + Copertura => Partizione 

![[Pasted image 20231112003316.png]]

![[Pasted image 20231112003326.png]]

# Modello relazionale

una relazione matematica su N insiemi è un sottoinsieme del prodotto cartesiano dei sudetti N insiemi

![[Pasted image 20231112003559.png]]

![[Pasted image 20231112003638.png]]

![[Pasted image 20231112003649.png]]

![[Pasted image 20231112003705.png]]

T = tipo ennupla -> insieme finito di coppie (Attr, Tipo elementare)

R(T) = schema relazione R

schema base di dati = insieme di $R_i(T_i)$ 

istanza di R(T) -> insieme finito di ennuple di tipo T

T insieme di attr. -> $R(T) = R(A_1,\dots,A_n)$ -> $R=\{R_1(X_1),\dots,R_k(X_k)\}$ -> $X_1,\dots,X_k$ sono insiemi di attr.

![[Pasted image 20231112010347.png]]

![[Pasted image 20231112010829.png]]

![[Pasted image 20231112010841.png]]

una superchiave contiene attr. superflui
una chiave contiene il minimo numero di attr. non superflui 

![[Pasted image 20231112011336.png]]

chiave primaria -> chiave NO NULL

chiave esterna -> riferimento(puntatore) ad una chiave primaria di un'altra tabella -> vincolo d'integrità referenziale

![[Pasted image 20231112011649.png]]

![[Pasted image 20231112011708.png]]

![[Pasted image 20231112011800.png]]

![[Pasted image 20231112011832.png]]

![[Pasted image 20231112012022.png]]

![[Pasted image 20231112012052.png]]

![[Pasted image 20231112012110.png]]

![[Pasted image 20231112012121.png]]

# ALGEBRA RELAZIONALE

DDL -> operazioni sullo schema
DML -> operazioni sui dati

$\rho$ -> ridenominazione -> modifica lo schema ma lascia intatto l'stanza

$\pi$ -> proiezione:
- ![[Pasted image 20231112012845.png]]
- ![[Pasted image 20231112012925.png]]

$\sigma$ -> selezione :
- ![[Pasted image 20231112013208.png]]

![[Pasted image 20231112013305.png]]

![[Pasted image 20231112013335.png]]

condizione atomica vera solo per valori non nulli -> quanto si ha a che fare con NULL **usare IS NULL o IS NOT NULL**

![[Pasted image 20231112013518.png]]

![[Pasted image 20231112013737.png]]

![[Pasted image 20231112013937.png]]

![[Pasted image 20231112014020.png]]

![[Pasted image 20231112014132.png]]

![[Pasted image 20231112014221.png]]

![[Pasted image 20231112014346.png]]

theta-join diventa equi-join se l'operatore è sempre '='

![[Pasted image 20231112014730.png]]

![[Pasted image 20231112014753.png]]

![[Pasted image 20231112015027.png]]

![[Pasted image 20231112015052.png]]

![[Pasted image 20231112015123.png]]

![[Pasted image 20231112015147.png]]

$\pi_A(R_1-R_2)$ != $\pi_A(R_1) - \pi_A(R_2)$ 

![[Pasted image 20231112015411.png]]

$_{\{A_i\}} \gamma _{\{f_i\}}(R)$  -> raggruppamento:
- ![[Pasted image 20231112015852.png]]
- ![[Pasted image 20231112015913.png]]

![[Pasted image 20231112020036.png]]

![[Pasted image 20231112020116.png]]

![[Pasted image 20231112020412.png]]

![[Pasted image 20231112020539.png]]

![[Pasted image 20231112020602.png]]

![[Pasted image 20231112020609.png]]

![[Pasted image 20231112020705.png]]

# SQL

Calcolo su Multiinsiemi -> sono permessi elementi cloni

![[Pasted image 20231113182500.png]]
![[Pasted image 20231113182519.png]]

![[Pasted image 20231113182603.png]]
![[Pasted image 20231113182846.png]]

## SELECT:
![[Pasted image 20231113182016.png]]
![[Pasted image 20231113182124.png]]
![[Pasted image 20231113182136.png]] ![[Pasted image 20231113182156.png]]

La SELECT implementa gli operatori di Proiezione, Selezione e Join dell'Algebra Relazionale, ecc.

![[Pasted image 20231113182901.png]]

![[Pasted image 20231114215507.png]]

![[Pasted image 20231114215532.png]]

![[Pasted image 20231114215632.png]]

![[Pasted image 20231114215644.png]]

![[Pasted image 20231114215657.png]]

![[Pasted image 20231114215714.png]]

![[Pasted image 20231114215754.png]]

![[Pasted image 20231114215823.png]]

![[Pasted image 20231114215841.png]]

SE DEVI GESTIRE NULL -> **IS / IS NOT NULL**

![[Pasted image 20231114220027.png]]

![[Pasted image 20231114220038.png]]

![[Pasted image 20231114220047.png]]

![[Pasted image 20231114224817.png]]

![[Pasted image 20231114224829.png]]

![[Pasted image 20231114225334.png]]

![[Pasted image 20231116175820.png]]

![[Pasted image 20231116175644.png]]

![[Pasted image 20231116175658.png]]

![[Pasted image 20231116175737.png]]

![[Pasted image 20231116175748.png]]

![[Pasted image 20231116175944.png]]

![[Pasted image 20231116175958.png]]

![[Pasted image 20231116180013.png]]

![[Pasted image 20231116180055.png]]

![[Pasted image 20231116180107.png]]

![[Pasted image 20231116180206.png]]

![[Pasted image 20231116180706.png]]

![[Pasted image 20231116180740.png]]

![[Pasted image 20231116180824.png]]

![[Pasted image 20231116180839.png]]

![[Pasted image 20231116180905.png]]

![[Pasted image 20231116181017.png]]

cross join (prodotto cartesiano) -> ![[Pasted image 20231116181104.png]]

![[Pasted image 20231116181123.png]]

![[Pasted image 20231116181200.png]]

![[Pasted image 20231116181356.png]]

![[Pasted image 20231116181406.png]]

![[Pasted image 20231116181503.png]]

equi-join = NATURAL JOIN

![[Pasted image 20231116181617.png]]

![[Pasted image 20231116181642.png]]

![[Pasted image 20231116181813.png]]

![[Pasted image 20231117090149.png]]

![[Pasted image 20231117090205.png]]

![[Pasted image 20231117090228.png]]

![[Pasted image 20231117091219.png]]

![[Pasted image 20231117091240.png]]

![[Pasted image 20231117160629.png]]

![[Pasted image 20231117160715.png]]

![[Pasted image 20231117160742.png]]

![[Pasted image 20231117160852.png]]

![[Pasted image 20231117160935.png]]

![[Pasted image 20231117161008.png]]

![[Pasted image 20231117161105.png]]

![[Pasted image 20231117161117.png]]

![[Pasted image 20231117161206.png]]


