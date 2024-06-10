
# PARTE 1:

![[Pasted image 20240329140800.png]]

![[Pasted image 20240329140817.png]]

![[Pasted image 20240329140836.png]]

![[Pasted image 20240329140941.png]]

![[Pasted image 20240329141000.png]]

![[Pasted image 20240329141026.png]]

![[Pasted image 20240329141159.png]]

Livelli:
- Logico = schema dati e delle relazioni fra loro secondo un certo modello (no ref alla org fisica)
- fisico = schema dell'organizzazione fisica dei dati 
- vista logica = descrive come deve apparire la struttura della base di dati ad una certa applicazione -> livello logico restricted

![[Pasted image 20240329141743.png]]

DML -> x query e update istanze di basi di dati
DDL -> x def di schemi e altre op generali

![[Pasted image 20240329142051.png]]

![[Pasted image 20240329142108.png]]

![[Pasted image 20240329142258.png]]

![[Pasted image 20240329142449.png]]

![[Pasted image 20240329142526.png]]

![[Pasted image 20240329142931.png]]

Tipi proprietà:
- atomica = valore non scomponibile
- strutturata = not atomica
- univoca = valore unico
- multivalore = not univoca
- totale = obbligatoria
- parziale = not totale
- costante
- variabile
- calcolata
- non calcolata

![[Pasted image 20240329143347.png]]

![[Pasted image 20240329143506.png]]

![[Pasted image 20240329143524.png]]

![[Pasted image 20240329143657.png]]

![[Pasted image 20240329143905.png]]

![[Pasted image 20240329143947.png]]

![[Pasted image 20240329145436.png]]

![[Pasted image 20240329145914.png]]

![[Pasted image 20240329150059.png]]

![[Pasted image 20240329150210.png]]

![[Pasted image 20240329150426.png]]

# PARTE 2:

![[Pasted image 20240329151441.png]]

![[Pasted image 20240329151600.png]]

![[Pasted image 20240329151618.png]]

![[Pasted image 20240329152419.png]]

![[Pasted image 20240329152509.png]]

![[Pasted image 20240329153424.png]]

![[Pasted image 20240329153447.png]]

![[Pasted image 20240329153458.png]]

![[Pasted image 20240329153639.png]]

![[Pasted image 20240329153932.png]]


![[Pasted image 20240329154027.png]]

![[Pasted image 20240329154600.png]]

![[Pasted image 20240329154611.png]]

![[Pasted image 20240329154631.png]]

![[Pasted image 20240329154650.png]]

![[Pasted image 20240329154921.png]]

![[Pasted image 20240329155006.png]]

![[Pasted image 20240329155034.png]]

![[Pasted image 20240329155054.png]]

![[Pasted image 20240329155349.png]]

![[Pasted image 20240329155400.png]]

![[Pasted image 20240329155412.png]]

![[Pasted image 20240329155425.png]]

![[Pasted image 20240329155435.png]]

![[Pasted image 20240329155445.png]]

![[Pasted image 20240329155600.png]]

![[Pasted image 20240329155618.png]]

![[Pasted image 20240329155633.png]]

![[Pasted image 20240329155812.png]]

![[Pasted image 20240329155839.png]]

![[Pasted image 20240329160117.png]]

# ALGEBRA RELAZIONALE

![[Pasted image 20240525183827.png]]

![[Pasted image 20240525183855.png]]

![[Pasted image 20240525183930.png]]

![[Pasted image 20240525184020.png]]

![[Pasted image 20240525184138.png]]

![[Pasted image 20240525184156.png]]

![[Pasted image 20240525184245.png]]

![[Pasted image 20240525184358.png]]

![[Pasted image 20240525184422.png]]

![[Pasted image 20240525184459.png]]

![[Pasted image 20240525184705.png]]

![[Pasted image 20240525184725.png]]

![[Pasted image 20240525184931.png]]

![[Pasted image 20240525185017.png]]

![[Pasted image 20240525185036.png]]

![[Pasted image 20240525185113.png]]

![[Pasted image 20240525185218.png]]

![[Pasted image 20240525185329.png]]

IS NULL / IS NOT NULL = orme apposite di condizioni per i valori null

![[Pasted image 20240525185447.png]]

proiezione -> sub set di colonne
restrizione -> subset di righe

![[Pasted image 20240525185800.png]]

![[Pasted image 20240525190042.png]]

![[Pasted image 20240525190237.png]]

![[Pasted image 20240525190331.png]]

![[Pasted image 20240525190905.png]]

![[Pasted image 20240525191111.png]]

![[Pasted image 20240525191236.png]]

Tipi di JOIN:
- NATURALE:
	- ![[Pasted image 20240525191323.png]]
	- ![[Pasted image 20240525191509.png]]
- COMPLETO:
	- ![[Pasted image 20240525192055.png]]
	- ![[Pasted image 20240525192243.png]]
- NON COMPLETO:
	- ![[Pasted image 20240525192130.png]]
- VUOTO
- ESTERNO:
	- ![[Pasted image 20240525192706.png]]
	- ![[Pasted image 20240525192757.png]]
	- ![[Pasted image 20240525192833.png]]
	- ![[Pasted image 20240525192847.png]]
- THETA-JOIN:
	- ![[Pasted image 20240525193640.png]]
	- ![[Pasted image 20240525193700.png]]
	- ![[Pasted image 20240525193801.png]]
	- ![[Pasted image 20240525193843.png]]
- SELF-JOIN:
	- ![[Pasted image 20240525194144.png]]
	- ![[Pasted image 20240525194204.png]]
	- ![[Pasted image 20240525194328.png]]

![[Pasted image 20240525192346.png]]

![[Pasted image 20240525192607.png]]

![[Pasted image 20240525192930.png]]

![[Pasted image 20240525193054.png]]

![[Pasted image 20240525193220.png]]

PRODOTTO CARTESIANO = JOIN NATURALE SENZA ATTR. IN COMUNE (\# ENNUPLE = |A| * |B|)

# SQL

![[Pasted image 20240525194803.png]]

![[Pasted image 20240525194820.png]]

![[Pasted image 20240525195033.png]]

![[Pasted image 20240525195053.png]]

![[Pasted image 20240525195130.png]]

![[Pasted image 20240525195551.png]]

![[Pasted image 20240526162717.png]]

![[Pasted image 20240526163039.png]]

![[Pasted image 20240526163150.png]]

![[Pasted image 20240526163214.png]]

![[Pasted image 20240526163456.png]]

![[Pasted image 20240526163610.png]]

![[Pasted image 20240526163639.png]]

![[Pasted image 20240526163859.png]]

![[Pasted image 20240526164046.png]]

![[Pasted image 20240526164407.png]]

![[Pasted image 20240526164626.png]]

![[Pasted image 20240526165103.png]]

![[Pasted image 20240526165204.png]]

![[Pasted image 20240526165255.png]]

![[Pasted image 20240526165323.png]]

![[Pasted image 20240526165407.png]]

![[Pasted image 20240526165431.png]]

![[Pasted image 20240526165559.png]]

![[Pasted image 20240526165628.png]]

![[Pasted image 20240526165801.png]]

![[Pasted image 20240526165911.png]]

![[Pasted image 20240526170110.png]]

![[Pasted image 20240526170359.png]]

![[Pasted image 20240526170510.png]]

![[Pasted image 20240526170731.png]]

![[Pasted image 20240526170828.png]]

![[Pasted image 20240526170957.png]]

![[Pasted image 20240526171150.png]]

![[Pasted image 20240526171332.png]]

![[Pasted image 20240526171458.png]]

![[Pasted image 20240526171559.png]]

![[Pasted image 20240526171956.png]]

![[Pasted image 20240526172718.png]]

![[Pasted image 20240526173133.png]]

![[Pasted image 20240526173305.png]]

![[Pasted image 20240526173341.png]]

![[Pasted image 20240526173531.png]]

![[Pasted image 20240526173911.png]]

![[Pasted image 20240526173936.png]]

![[Pasted image 20240526174308.png]]

![[Pasted image 20240526174445.png]]

![[Pasted image 20240526174805.png]]

![[Pasted image 20240526175002.png]]

![[Pasted image 20240526175218.png]]

![[Pasted image 20240526175241.png]]

![[Pasted image 20240526180619.png]]

![[Pasted image 20240526180800.png]]

![[Pasted image 20240526181128.png]]

![[Pasted image 20240526181400.png]]

![[Pasted image 20240526181444.png]]

![[Pasted image 20240526181727.png]]

![[Pasted image 20240526181747.png]]

![[Pasted image 20240526182927.png]]

![[Pasted image 20240526183021.png]]

![[Pasted image 20240526183215.png]]

![[Pasted image 20240526183310.png]]

![[Pasted image 20240526183556.png]]

![[Pasted image 20240526183725.png]]

![[Pasted image 20240526183815.png]]

![[Pasted image 20240526184014.png]]

![[Pasted image 20240526230708.png]]

![[Pasted image 20240526230758.png]]

![[Pasted image 20240526231021.png]]

![[Pasted image 20240526231234.png]]

![[Pasted image 20240526231505.png]]

![[Pasted image 20240526231707.png]]

![[Pasted image 20240526231729.png]]

![[Pasted image 20240526232026.png]]

![[Pasted image 20240526232336.png]]

![[Pasted image 20240526232552.png]]

![[Pasted image 20240526232652.png]]

![[Pasted image 20240526232730.png]]

![[Pasted image 20240526232846.png]]

![[Pasted image 20240526233053.png]]

![[Pasted image 20240526233123.png]]

![[Pasted image 20240526233233.png]]

![[Pasted image 20240526233345.png]]

![[Pasted image 20240526233417.png]]

![[Pasted image 20240526233538.png]]

![[Pasted image 20240526233848.png]]

![[Pasted image 20240526234418.png]]

![[Pasted image 20240526234847.png]]

![[Pasted image 20240526235139.png]]

![[Pasted image 20240526235434.png]]

![[Pasted image 20240527000316.png]]

![[Pasted image 20240527000612.png]]

![[Pasted image 20240527001111.png]]

![[Pasted image 20240527001404.png]]

![[Pasted image 20240527001641.png]]

![[Pasted image 20240527001940.png]]

![[Pasted image 20240527155015.png]]

![[Pasted image 20240527155241.png]]

![[Pasted image 20240527155348.png]]

![[Pasted image 20240527155902.png]]

![[Pasted image 20240527160050.png]]

![[Pasted image 20240527160254.png]]

![[Pasted image 20240527160340.png]]

![[Pasted image 20240527160416.png]]

![[Pasted image 20240527161005.png]]

![[Pasted image 20240527161034.png]]

![[Pasted image 20240527161256.png]]

![[Pasted image 20240527162501.png]]

![[Pasted image 20240527162653.png]]

![[Pasted image 20240527162805.png]]

![[Pasted image 20240527162842.png]]

![[Pasted image 20240527163026.png]]

![[Pasted image 20240527163125.png]]

![[Pasted image 20240528180703.png]]

![[Pasted image 20240528180831.png]]

![[Pasted image 20240528180910.png]]

![[Pasted image 20240528181534.png]]

![[Pasted image 20240528181826.png]]

![[Pasted image 20240528181934.png]]

![[Pasted image 20240528182011.png]]

![[Pasted image 20240528182125.png]]

![[Pasted image 20240528182204.png]]

![[Pasted image 20240528182248.png]]

![[Pasted image 20240528182315.png]]

![[Pasted image 20240528182431.png]]

![[Pasted image 20240528182450.png]]

![[Pasted image 20240528182606.png]]

![[Pasted image 20240528182852.png]]

Esercizio Esempio:![[7.SQLDefinizioneDati.pdf#page=22]]
![[Pasted image 20240528183517.png]]

![[Pasted image 20240528184027.png]]

![[Pasted image 20240528184057.png]]

![[Pasted image 20240528184250.png]]

![[Pasted image 20240528184404.png]]

![[Pasted image 20240528184526.png]]

![[Pasted image 20240528184659.png]]

![[Pasted image 20240528184800.png]]

![[Pasted image 20240528185037.png]]

![[Pasted image 20240528185358.png]]

![[Pasted image 20240528185926.png]]

![[Pasted image 20240528190016.png]]

![[Pasted image 20240528190055.png]]

![[Pasted image 20240528190133.png]]

![[Pasted image 20240528190404.png]]

![[Pasted image 20240528190713.png]]

view => NO OPERATORI UNION, INTERSECT, EXCEPT e non clausola ORDER BY

![[Pasted image 20240528191040.png]]

![[Pasted image 20240528191112.png]]

![[Pasted image 20240528191221.png]]

![[Pasted image 20240528191425.png]]

![[Pasted image 20240528191750.png]]

![[Pasted image 20240528191810.png]]

![[Pasted image 20240528192013.png]]

![[Pasted image 20240528192213.png]]

![[Pasted image 20240528192300.png]]

![[Pasted image 20240528192706.png]]

![[Pasted image 20240528192732.png]]

![[Pasted image 20240528193246.png]]

![[Pasted image 20240528194300.png]]

![[Pasted image 20240528194330.png]]

![[Pasted image 20240528194545.png]]

![[Pasted image 20240529002931.png]]

![[Pasted image 20240529002943.png]]

![[Pasted image 20240529003019.png]]

View => indipendenza logica, visione degli stessi dati senza duplicati, + semplici alcune query

![[Pasted image 20240529003622.png]]

![[Pasted image 20240529003655.png]]

![[Pasted image 20240529004141.png]]

![[Pasted image 20240529004232.png]]

trigger => evento-condizione-azione

![[Pasted image 20240529004408.png]]

![[Pasted image 20240529004737.png]]

![[Pasted image 20240529005121.png]]

trigger:
- attivo -> modifica lo stato della base di dati
- passivo -> provoca il fallimento della transazione current sotto cond.

![[Pasted image 20240529005257.png]]

![[Pasted image 20240529005332.png]]

![[Pasted image 20240529005427.png]]

![[Pasted image 20240529005447.png]]

![[Pasted image 20240529005609.png]]

![[Pasted image 20240529005702.png]]

![[Pasted image 20240529005719.png]]

![[Pasted image 20240529005900.png]]

![[Pasted image 20240529005928.png]]

![[Pasted image 20240529010046.png]]

![[Pasted image 20240529010253.png]]

![[Pasted image 20240529010237.png]]

# DBMS

![[Pasted image 20240527163406.png]]

![[Pasted image 20240527163445.png]]

![[Pasted image 20240527163744.png]]

![[Pasted image 20240527170005.png]]

![[Pasted image 20240527170056.png]]

![[Pasted image 20240527170200.png]]

![[Pasted image 20240527170442.png]]

![[Pasted image 20240527170519.png]]

![[Pasted image 20240527170821.png]]

![[Pasted image 20240527171027.png]]

![[Pasted image 20240527171101.png]]

![[Pasted image 20240527171127.png]]

![[Pasted image 20240527171303.png]]

![[Pasted image 20240527171949.png]]

![[Pasted image 20240527172018.png]]

![[Pasted image 20240527172043.png]]

Tipi di organizzazioni:
- seriale:
	- ![[Pasted image 20240527172357.png]]
- sequenziale:
	- ![[Pasted image 20240527172515.png]]
	- ![[Pasted image 20240527172552.png]]
- per chiave:
	- ![[Pasted image 20240527172618.png]]
	- ![[Pasted image 20240527172708.png]]
	- ![[Pasted image 20240527172817.png]]
	- ![[Pasted image 20240527172854.png]]
	- ![[Pasted image 20240527173047.png]]
	- ![[Pasted image 20240527173236.png]]
	- ![[Pasted image 20240527173627.png]]
	- ![[Pasted image 20240527173345.png]]
	- ![[Pasted image 20240527173520.png]]
	- ![[Pasted image 20240527173606.png]]
	- ![[Pasted image 20240527174012.png]]
	- ![[Pasted image 20240527174115.png]]
	- ![[Pasted image 20240527174154.png]]
	- ![[Pasted image 20240527174241.png]]
	- ![[Pasted image 20240527174332.png]]
	- ![[Pasted image 20240527174543.png]]
	- ![[Pasted image 20240527174645.png]]
	- ![[Pasted image 20240527174719.png]]
	- ![[Pasted image 20240527174807.png]]
	- ![[Pasted image 20240527174911.png]]
	- ![[Pasted image 20240527174938.png]]
	- ![[Pasted image 20240527175003.png]]
	- ![[Pasted image 20240527175129.png]]
- per attrs:
	- 
Parametri che caratterizzano un'organizzazione:
- occupazione memoria
- costo operazioni di:
	- ricerca per valore / intervallo
	- modifica
	- inserzione
	- cancellazione

![[Pasted image 20240527185938.png]]

![[Pasted image 20240527190019.png]]

![[Pasted image 20240527190155.png]]

![[Pasted image 20240527190227.png]]

![[Pasted image 20240527190345.png]]

![[Pasted image 20240527190419.png]]

![[Pasted image 20240527190637.png]]

![[Pasted image 20240527190839.png]]

![[Pasted image 20240527190927.png]]

![[Pasted image 20240527190953.png]]

![[Pasted image 20240527191052.png]]

![[Pasted image 20240527191209.png]]

![[Pasted image 20240527191538.png]]

![[Pasted image 20240527230359.png]]

![[Pasted image 20240527230443.png]]

![[Pasted image 20240527230905.png]]

![[Pasted image 20240527231017.png]]

![[Pasted image 20240527231142.png]]

![[Pasted image 20240527231237.png]]

![[Pasted image 20240527231311.png]]

![[Pasted image 20240527231639.png]]

![[Pasted image 20240527231742.png]]

![[Pasted image 20240527231846.png]]

![[Pasted image 20240527232224.png]]

![[Pasted image 20240527232340.png]]

![[Pasted image 20240527232449.png]]

![[Pasted image 20240527232506.png]]

![[Pasted image 20240527232605.png]]

![[Pasted image 20240527232907.png]]

![[Pasted image 20240527233011.png]]

![[Pasted image 20240527233318.png]]

![[Pasted image 20240527233631.png]]

![[Pasted image 20240527233658.png]]

![[Pasted image 20240527233910.png]]

![[Pasted image 20240527234034.png]]

![[Pasted image 20240527234234.png]]

![[Pasted image 20240527234403.png]]

![[Pasted image 20240527234434.png]]

![[Pasted image 20240527234549.png]]

![[Pasted image 20240527235102.png]]

![[Pasted image 20240527235704.png]]

![[Pasted image 20240528000015.png]]

![[Pasted image 20240528000147.png]]

![[Pasted image 20240528000340.png]]

![[Pasted image 20240528000556.png]]

![[Pasted image 20240528000616.png]]

![[Pasted image 20240528001008.png]]

![[Pasted image 20240528001032.png]]

![[Pasted image 20240528001241.png]]

![[Pasted image 20240528001339.png]]

![[Pasted image 20240528001428.png]]

![[Pasted image 20240528001716.png]]

![[Pasted image 20240528003619.png]]

![[Pasted image 20240528003822.png]]

![[Pasted image 20240528004048.png]]

![[Pasted image 20240528004242.png]]

![[Pasted image 20240528004422.png]]

![[Pasted image 20240528004607.png]]

![[Pasted image 20240528004647.png]]

![[Pasted image 20240528004818.png]]

![[Pasted image 20240528171721.png]]

![[Pasted image 20240528171744.png]]

![[Pasted image 20240528171831.png]]

![[Pasted image 20240528171926.png]]

![[Pasted image 20240528171955.png]]

![[Pasted image 20240528172011.png]]

![[Pasted image 20240528172440.png]]

![[Pasted image 20240528172645.png]]

![[Pasted image 20240528172946.png]]

![[Pasted image 20240528173045.png]]

![[Pasted image 20240528173102.png]]

![[Pasted image 20240528173334.png]]

![[Pasted image 20240528173405.png]]

![[Pasted image 20240528173841.png]]

![[Pasted image 20240528173941.png]]

![[Pasted image 20240528174004.png]]

![[Pasted image 20240528174232.png]]

![[Pasted image 20240528174258.png]]

![[Pasted image 20240528174433.png]]

- perdita update:
	- ![[Pasted image 20240528174610.png]]
- read sporca:
	- ![[Pasted image 20240528174652.png]]
- read inconsistente:
	- ![[Pasted image 20240528174739.png]]

![[Pasted image 20240528174820.png]]

![[Pasted image 20240528174946.png]]

![[Pasted image 20240528175101.png]]

![[Pasted image 20240528175130.png]]

tecniche di concorrenza:
- con lock:
	- ![[Pasted image 20240528175536.png]]
	- ![[Pasted image 20240528175717.png]]
	- ![[Pasted image 20240528175740.png]]
	- ![[Pasted image 20240528175808.png]]
	- ![[Pasted image 20240528175848.png]]
	- gestione deadlock:
		- ![[Pasted image 20240528175929.png]]
		- ![[Pasted image 20240528175948.png]]
		- ![[Pasted image 20240528180023.png]]
- con timestamp:
	- ![[Pasted image 20240528180110.png]]

![[Pasted image 20240528180148.png]]









# domande:
1. definizione di dipendenza funzionale:
![[Pasted image 20240610005908.png]]
2. definizione di chiave e superchiave usando le df:
![[Pasted image 20240610011202.png]]
Dato lo schema R<T, F> un insieme di attributi $W \subseteq T$ è superchiave se $T \in W_F^+$ (se la chisura di W rispetto a F contiene tutti gli attributi)
![[Pasted image 20240610011701.png]]
![[Pasted image 20240610012021.png]]
3. i due modi per preservare i dati in una decomposizione:
![[Pasted image 20240610014050.png]]
![[Pasted image 20240610014120.png]]
![[Pasted image 20240610014215.png]]
![[Pasted image 20240610014403.png]]
![[Pasted image 20240610014513.png]]
 4. definizione BCNF e 3FN usando le df:
![[./IMMAGINI/Pasted image 20240610012758.png]]
![[./IMMAGINI/Pasted image 20240610013103.png]]
 - BNCF -> X->Y con X superchiave
 - 3NF -> X->Y con X superchiave oppure ogni attr. di Y è contenuto in almeno in una chiave
5. conversione di gerarchie da schema concettuale a logico:
![[./IMMAGINI/Pasted image 20240610015159.png]]
![[./IMMAGINI/Pasted image 20240610015224.png]]
![[./IMMAGINI/Pasted image 20240610015400.png]]
![[./IMMAGINI/Pasted image 20240610015420.png]]
6. schema transizioni con insiemi undo, redo:
![[./IMMAGINI/Pasted image 20240610020559.png]]
7. scrivere algoritmo analisi da schema in BCNF:
![[./IMMAGINI/Pasted image 20240610020704.png]]
![[./IMMAGINI/Pasted image 20240610020743.png]]
(VERSIONE SINTESI PER 3NF):
![[./IMMAGINI/Pasted image 20240610020959.png]]
![[./IMMAGINI/Pasted image 20240610021121.png]]
![[./IMMAGINI/Pasted image 20240610021136.png]]
![[./IMMAGINI/Pasted image 20240610021154.png]]
![[./IMMAGINI/Pasted image 20240610021210.png]]
![[./IMMAGINI/Pasted image 20240610021243.png]]
![[./IMMAGINI/Pasted image 20240610021309.png]]
