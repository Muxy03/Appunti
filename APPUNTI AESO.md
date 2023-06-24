
# Capitolo 1

$10110_{2} = 1*2^4+0*2^3+1*2^2+1*2^1+0*2^0 = 22_{10}$

0,...,9,A,...,F -> A = 10,...,F = 15

$2ED_{16} = 2*16^2+E*16^1+D*16^0=749_{10}$

$1+1 = 0$ con riporto di 1 (carry)

modulo e segno:
- 1 bit per il segno (0->+ e 1->-) e N-1 bit per il modulo
- $[-2^{N-1}+1,2^{N-1}-1]$  intervallo di variabilità
- 0 ha 2 rappresentazioni -> +0 e -0
- non è possibile utilizzare la somma usuale -> -5 +5 torna diverso da 0

complemento a 2:
-  bit significativo = 0 (+) / 1 (-)
- $[-2^{N-1},2^{N-1}-1]$  intervallo di variabilità
-  risolve i problemi della rappresentazione modulo e segno
- calcolo complemento a 2 -> inverti bit e sommi 1
- I numeri in complemento a due hanno il vantaggio che la somma è eseguibile in maniera corretta utilizzando il metodo usuale sia per i numeri positivi sia per quelli negativi. Si ricordi soltanto che quando si sommano numeri a N bit il riporto dell’N­esimo bit (cioè il bit di posizione N + 1 all’interno del risultato) deve essere scartato. La sottrazione viene effettuata effettuando il complemento a 2 del secondo numero e poi procedendo con la somma.
- estensione del segno -> i numeri 3 e –3 si scrivono numeri in complemento a due a 4 bit rispettivamente 0011 e 1011. Questi ultimi vengono estesi a 7 bit copiando il bit che dà il segno nella posizione dei tre nuovi bit per formare rispettivamente 0000011 e 1111101.
- positivo+positivo oppure negativo+negativo implica overflow
- $-2^{N-1}$ non ha controparte positiva

![[range rappresentazioni.png]]

Porte Logiche:
- NOT -> NOT(1) = 0; NOT(0) = 1
- BUFFER -> BUF(1) = 1; BUF(0) = 0
- AND -> A∩B = 1 <=> A=B=1
- OR -> A+B = 0 <=> A=B=0
- XOR -> A (+) B = 1 <=> numero dispari di ingressi a 1
- NAND -> NOT-AND
- NOR -> NOT-OR

![[Livelli logici.png]]

>Transistor MOSFET (MetalOxide-Semiconductor Field Effect) -> nMOS e pMOS
>
>La giunzione tra un silicio di tipo n e uno di tipo p viene chiamata diodo. La regione di tipo p è chiamata anodo, mentre quella di tipo n catodo
>
>![[Schermata del 2023-04-15 17-46-23.png]]
>
>la tensione sul gate regola il flusso di corrente da source a drain (canale di elettroni e cariche positive sul fondo del polisilicio)
>
>![[Schermata del 2023-04-15 17-50-26.png]]

# Capitolo 2

circuito -> rete elettrica che elabora variabili a valori discreti 

>![[Schermata del 2023-04-15 18-06-26.png]]

reti combinatorie -> una rete combinatoria utilizza i valori presenti agli ingressi per calcolare i valori delle uscite (un esempio di rete combinatoria è una porta logica) -> NO MEMORIA

reti sequenziali -> Le uscite di una rete sequenziale, invece, dipendono sia dai valori presenti agli ingressi, sia dai valori precedenti; in altre parole, i valori delle uscite dipendono dalla sequenza dei valori degli ingressi -> SI MEMORIA

FULL ADDER -> Ingressi: (A,B,$R_{in}$), Output: (S,$R_{out}$)

>Terminologia:
> -  $\overline{A}$ = complemento di A (NOT di A) -> $\overline{A}$ indica che A = 0 nella true table
> -  AB = prodotto logico (A AND B)
> - A+B = somma logica (A OR B)
> - NOT >> AND >> OR (ordine priorità)

N ingressi => $2^N$ righe nella true table

>![[Pasted image 20230415182356.png]]
>
>![[Pasted image 20230415183424.png]]>
>![[Pasted image 20230415183529.png]]

Codice di Gray -> 00 01 11 10 -> mappe Karnaugh

Regole mappe Karnaugh:
- se nella true table c'è indifferenza possiamo inserire 0/1 a nostra scelta
![[Pasted image 20230415184847.png]]

multiplexer (mux) -> N ingressi e 1 uscita con S (segnale di controllo) che decide quale ingresso uscirà -> un multiplexer N:1 necessita di $\log_{2}(N)$ ingressi di selezione

![[Pasted image 20230415190355.png]]

componenti reti combinatorie -> appunti onenote

![[Pasted image 20230415194009.png]]

ritardo di propragazione -> tempo massimo che trascorre dal momento in cui avviene un cambiamento nell'ingresso al momento in cui l'uscita/e raggiunge il suo valore finale

ritardo di contaminazione -> tempo minimo che trascorre dal momento in cui cambia l'ingresso al momento in cui una qualsiasi uscita comincia il processo di adattamento del suo valore

![[Pasted image 20230415194451.png]]

![[Pasted image 20230415194646.png]]

alee -> singolo cambiamento d'ingresso che genera molteplici cambiamenti in uscita

MAPPA CON ALEA
![[Pasted image 20230415194834.png]]
MAPPA SENZA ALEA
![[Pasted image 20230415195017.png]]

# Capitolo 3

>Latch SR -> rete sequenziale (S=set, R=reset, Q=State) -> 2 porte NOR collegate a croce -> S=R=1 comportamento incredibile
>
>![[Pasted image 20230417182048.png]]
>
>![[Pasted image 20230417181656.png]]
>
>![[Pasted image 20230417182304.png]]

>Latch D -> rete sequenziale (D=dati(new State), CLK=clock) 
>
>![[Pasted image 20230417182737.png]]
>
>CLK = 1/0 -> Trasparente (i dati scorrono da D a Q) / Opaco (blocco passaggio dati)
>
>Il latch D aggiorna continuamente il suo stato mentre CLK = 1

>Flip-Flop D -> 2 LATCH D a cascata con CLK e $\overline{CLK}$ 
>
>1 latch è master e il 2 latch è slave
>
>Quando CLK = 0, il latch master è trasparente, mentre il latch slave è opaco. Di conseguenza, qualsiasi valore di D viene portato a N1. Quando invece CLK = 1, il latch master diventa opaco e quello slave trasparente. In questo caso, il valore di N1 viene trasmesso a Q, ma N1 resta isolato da D. Quindi, qualunque sia il valore di D subito prima del fronte di salita (passaggio da 0 a 1) del clock, questo è il valore che viene trasferito a Q al momento di tale fronte. In tutti gli altri casi, Q mantiene il suo valore precedente, dal momento che c’è sempre un latch opaco che blocca il passaggio di dati tra D e Q.
>
> i lflip-flop copia D su Q al fronte di salita del clock e ricorda il suo stato in tutti gli altri casi
> 
> ![[Pasted image 20230417184214.png]]
> 
>Il fronte di salita del clock viene spesso chiamato con l’abbreviazione “fronte del clock” (clock edge). L’ingresso D specifica quale sarà il nuovo stato, mentre il fronte del clock indica il momento di aggiornamento dello stato.

>Registro -> Un registro a N bit è un banco di N flip-flop che condividono un ingresso CLK comune, in modo che tutti i bit vengano aggiornati allo stesso tempo. I registri costituiscono i blocchi costitutivi chiave per la maggior parte delle reti sequenziali.
>
>![[Pasted image 20230417184907.png]]

Una rete sequenziale sincrona ha un ingresso di clock i cui fronti di salita indicano una sequenza di istanti di tempo nei quali hanno luogo le transizioni di stato -> flip-flop

![[Pasted image 20230417190625.png]]

![[Pasted image 20230417190914.png]]

Moore -> le uscite dipendono solamente dallo stato corrente nella macchina

Mealy -> le uscite dipendono dallo stato corrente della macchina e dagli ingressi attuali

![[Pasted image 20230417191703.png]]

![[Pasted image 20230417191839.png]]

sistema con K stati -> $\log_{2}K$ bit di stato

Quindi nel diagramma degli stati per le macchine alla Moore i valori delle uscite vengono indicati nei cerchi. Le macchine alla Mealy, come già detto, sono molto simili a quelle alla Moore, ma le uscite possono dipendere sia dallo stato presente sia dagli ingressi. Ne consegue che un diagramma degli stati per una macchina alla Mealy avrà le uscite indicate sugli archi invece che nei cerchi

$T_c \ge t_{ps} + t_{pc} +t_{setup}+t_{skew}$ :
- $T_c$ = periodo di clock -> $f_c = \frac{1}{T_c}$ = frequenza di clock 
- $t_{ps}$ = ritardo di propagazione (sequenziale) -> $t_{pcq}$
- $t_{pc}$ = ritardo propagazione (combinatorio)
- $t_{setup}$ = tempo dopo cui gli ingressi sono stabili prima del fronte di salita del clock
- $t_{skew}$ = tempo in cui il clock raggiunge tutti i registri

$t_{cs} + t_{cc} \ge t_{hold}+t_{skew}$ :
- $t_{cs}$ = ritardo di contaminazione (sequenziale) -> $t_{ccq}$
- $t_{cc}$ = ritardo di contaminazione (combinatorio)
- $t_{hold}$ = tempo in cui gli ingressi devono rimanere stabili dopo il fronte di salita del clock 

$t_{hold} \ge t_{cs}$

![[Pasted image 20230417195818.png]]

![[Pasted image 20230417200457.png]]

$P(t_{res}>t)=\frac{T_0}{T_c}*e^{\frac{t}{\tau}}$  :
- $t_{res}$ = tempo di risoluzione della metastabilità richiesto perché l'uscita venga riportata a uno stato stabile -> se l'ingresso cambia fuori dal tempo di apertura (setup+hold) allora $t_{res} = t_{ps}$
-  $T_c$ = periodo di clock
- $T_0$  = dato caratteristico del flip-flop
- $\tau$ = costante di tempo che indica quanto velocemente il flip-flop si allontana dallo stato metastabile
- l'espressione è valida solo se t è significativamente più lungo di $t_{ps}$
- $\frac{T_0}{T_c}$ = probabilità che l'ingresso cambi al momento sbagliato

![[Pasted image 20230425163913.png]]

token -> gruppo di ingressi che vengono elaborati per produrre un gruppo di uscite
latenza -> tempo richiesto a un token per attraversare il sistema dall'inizio alla fine
capacità produttiva -> numero di token che possono essere elaborati per unità di tempo

Parallelismo:
- spaziale -> + lavori svolti contemporaneamente
- temporale -> , invece, ogni compito viene diviso in fasi, come in una catena di montaggio. Più compiti possono essere distribuiti tra le varie fasi. Nonostante ogni compito debba passare attraverso tutte le fasi, compiti diversi possono trovarsi in ogni fase in un qualsiasi momento, cosicché i diversi compiti si sovrappongono -> pipelining

![[Pasted image 20230425164427.png]]

![[Pasted image 20230425164555.png]]

# Capitolo 4

modulo ->  blocco circuitale con ingressi e uscite
stile comportamentale -> descrive cosa fa il modulo
stile strutturale -> visione generale della struttura del modulo

![[Pasted image 20230425165134.png]]

![[Pasted image 20230425165213.png]]

![[Pasted image 20230425165313.png]]

```verilog
module and8(input logic [7:0]a, output logic y);
	assign y=&a; // and bit a bit di a
endmodule;
```

![[Pasted image 20230425165630.png]]

![[Pasted image 20230425165711.png]]

![[Pasted image 20230425165748.png]]

![[Pasted image 20230425165802.png]]

![[Pasted image 20230425165917.png]]

![[Pasted image 20230425170021.png]]

0,1,z,x valori segnali in verilog:
![[Pasted image 20230425170120.png]]

![[Pasted image 20230425170222.png]]

![[Pasted image 20230425170248.png]]

![[Pasted image 20230425170332.png]]

![[Pasted image 20230425170427.png]]

![[Pasted image 20230425170449.png]]

![[Pasted image 20230425170549.png]]

![[Pasted image 20230425170612.png]]

![[Pasted image 20230509164208.png]]

![[Pasted image 20230509164300.png]]

![[Pasted image 20230509164427.png]]

![[Pasted image 20230509164550.png]]

![[Pasted image 20230509164907.png]]

![[Pasted image 20230509164942.png]]

![[Pasted image 20230509164957.png]]

![[Pasted image 20230509165018.png]]

![[Pasted image 20230509165136.png]]

![[Pasted image 20230509165423.png]]

![[Pasted image 20230509165153.png]]

![[Pasted image 20230509165517.png]]

![[Pasted image 20230509165620.png]]

![[Pasted image 20230509170010.png]]

![[Pasted image 20230509170048.png]]

![[Pasted image 20230509170305.png]]

![[Pasted image 20230509170605.png]]

![[Pasted image 20230509170802.png]]

![[Pasted image 20230509170828.png]]

![[Pasted image 20230509170909.png]]

![[Pasted image 20230509170930.png]]

![[Pasted image 20230509171014.png]] ![[Pasted image 20230509171138.png]]

# Capitolo 5

## ADDIZIONE

![[Pasted image 20230509171820.png]]

>Sommatore completo (_Full Adder_) :
>
>![[Pasted image 20230509172602.png]]

>Sommatore a propragazione di riporto (_Carry Propagate Adder_):
>$ritardo_{CPA} = N*ritardo_{FA}$
>
>![[Pasted image 20230509172815.png]]

>Sommatore ad anticipazione di riporto (_Carry-Lookhead Adder_):
>
>risolve il problema della velocità dividendo il sommatore stesso in blocchi e aggiungendo un circuito per determinare velocemente il riporto di uscita da ciascun blocco appena è noto il riporto di ingresso. Per questo si dice che il sommatore è in grado di “anticipare” o “guardare avanti” (look ahead) attraverso i blocchi invece di attendere che il riporto si propaghi attraverso tutti i full adder del blocco. Per esempio, un sommatore a 32 bit può essere diviso in otto blocchi da 4 bit ciascuno. I sommatori ad anticipazione di riporto utilizzano segnali di generazione (G) e di propagazione (P) che descrivono come una colonna o un blocco determinano il proprio riporto.
>
>$G_i = A_i*B_i$ , $P_i=A_i + B_i$ , $R_i=G_i+P_i*R_{i-1}$
>$G_{3:0} = G_3+P_3*(G_2+P_2*(G_1+P_1*G_0))$ , $P_{3:0}=P_3*P_2*P_1*P_0$ , $R_i = G_{i:j}+P_{i:j}*R_{j-1}$
>
>$t_{CLA}=t_{pg}+t_{pg\_blocco}+(\frac{N}{k}-1)*t_{AND/OR}+k*t_{FA}$
>
>>Legenda:
>>- $t_{pg}$ = ritardo delle porte di generazione e propagazione per calcolare $G_i$ e $P_i$ di ogni colonna (in una sola porta AND o OR)  
>>- $t_{pg\_blocco}$ = ritardo per calcolare i segnali di generazione e propagazione $P_{i:j}$ e $G_{i:j}$ per ogni blocco a k bit
>>- $t_{AND/OR}$ = ritardo da $R_{in}$ a $R_{out}$ attraverso la porta AND/OR finale del blocco ad anticipazione di riporto a k bit
>
>![[Pasted image 20230509173124.png]]

sommatore a prefissi ??

![[Pasted image 20230509180431.png]]

## SOTTRAZIONE

![[Pasted image 20230509180702.png]]

Y = A - B = A + NOT(B) +1 -> A + NOT(B) con $R_{in}=1$ 

![[Pasted image 20230509180829.png]]

## Comparatore

faccio AND dei risultati delle XNOR (NOT XOR)
![[Pasted image 20230509181021.png]]

N-1 bit = 1 <=> A < B , problemi con overflow
![[Pasted image 20230509181256.png]]

![[Pasted image 20230509181552.png]]

## ALU: Arithmetic Logical Unit

![[Pasted image 20230509181619.png]]

![[Pasted image 20230509181636.png]]

![[Pasted image 20230509181708.png]]

flagALU ->4 bit: N,Z,C,V -> negativo, zero, Carry, overflow

overflow -> la somma di 2 numeri concordi genera un numero di segno opposto

![[Pasted image 20230509182021.png]]

## Traslatori e rotatori

![[Pasted image 20230509182416.png]]

\>>,\<<,>>> -> LSL, LSR, ARS

3 LSL 4 = 3 * 2^4 = 48

-4 ARS 2 = -4 / 2^2 = -1

![[Pasted image 20230509183315.png]]

## MOLTIPLICAZIONE

![[Pasted image 20230509183518.png]]

![[Pasted image 20230509183627.png]]

## DIVISIONE

![[Pasted image 20230509183810.png]]

![[Pasted image 20230509184009.png]]

## NUMERI IN VIRGOLA FISSA

notazione in virgola fissa -> parte intera.parte frazionaria ->0110.1100 = $2^2+2^1+2^{-1}+2^{-2}$ = 6.75 

rappresentati in modulo e esegno o in complemento 2 

notazione virgola mobile -> 4100 = $4.1*10^3$  -> $\pm M \times B^E$ , M = mantissa, B = base, E = esponente -> virgola mobile perché viene spostata a destra della cifra + significativa

## NUMERI IN VIRGOLA MOBILE

I numeri in virgola mobile sono in base 2 con una mantissa binaria: vengono usati 32 bit per rappresentare 1 bit di segno, 8 bit di esponente e 23 bit di mantissa.

![[Pasted image 20230509185704.png]]

![[Pasted image 20230509185900.png]]

![[Pasted image 20230509185936.png]]

![[Pasted image 20230509185952.png]]

![[Pasted image 20230509190207.png]]

![[Pasted image 20230509190247.png]]

## Contatori 

![[Pasted image 20230509190611.png]]

![[Pasted image 20230509190718.png]]

## REGISTRI

![[Pasted image 20230509192617.png]]

![[Pasted image 20230509192657.png]]

![[Pasted image 20230509192721.png]]

## COMPONENTI DI MEMORIA

memoria ad accesso casuale dinamica -> DRAM
memoria ad accesso casuale statica -> SRAM
memoria a sola lettura -> ROM

memoria con N bit indirizzo e M bit di dato -> matrice $2^N \times M$ -> 2^N righe e M colonne -> ogni riga della matrice è una parola -> \#righe = lunghezza, larghezza = \#colonne

![[Pasted image 20230509195433.png]]

![[Pasted image 20230509195659.png]]

per leggere -> si attiva la linea di parola corrispondente e le linee di bit rimangono fluttuanti

per scrivere -> si porta le linee di bit al valore che vogliamo scrivere e poi viene attivata la linea di parola corrispondente e il nuovo valore viene immagazzinato nelle celle di bit 

![[Pasted image 20230509200225.png]]

>DRAM:
>![[Pasted image 20230511160030.png]]

>SRAM:
>![[Pasted image 20230511160107.png]]

![[Pasted image 20230511160133.png]]

throughput = quantità di bit scambiabili nel tempo

SDRAM -> DRAM sincrone
DDR SDRAM -> SDRAM a doppia velocità

register file -> gruppo di registri per immagazzinare variabili temporanee

![[Pasted image 20230511160510.png]]

![[Pasted image 20230511160556.png]]

![[Pasted image 20230511160713.png]]

PROM -> ROM programmabile -> ![[Pasted image 20230511161048.png]]

EPROM -> PROM cancellabile -> al posto del transistor e del fusibile c'è un transistor a gate sommerso

![[Pasted image 20230511161449.png]]

![[Pasted image 20230511161609.png]]

PLA -> matrici logich programmabili 

![[Pasted image 20230511161633.png]]


![[Pasted image 20230511161753.png]]

![[Pasted image 20230511161932.png]]

![[Pasted image 20230511162026.png]]

# Capitolo 6

Assembly (_MERDA_)

registri = variabili di Assembly -> ARM usa 16 registri (0-15) 

constanti -> immediati -> #... -> decimali o esadecimali(0x...) -> unsigned (8 o 12 bit)
![[Pasted image 20230511163325.png]]

```armasm
; R0 = a, R1 = b, R2 = c, R3 = d 

ADD R0, R1, R2 ; a = b + c
SUB R0, R1, R2 ; a = b - c

ADD R0,R1,#4 ; a = b+4
SUB R1,R2,#0xC ; b = c+12
MOV R2,#4 ; c = 0 (inizializzazione) 

MOV R1,#0 ; indirizzo base = 0
LDR R0,[R1,#8] ; R0 = dato memorizzato nella cella di indirizzo (R1+8)

MOV R1,#0
MOV R2,#42
STR R2,[R1,#0x14]; dato memorizzato nella cella di indirizzo(R1+20)=42

; al posto di R2 ci può essere un immediato
AND R0,R1,R2 ; R0 = R1 && R2
ORR R0,R1,R2 ; R0 = R1 || R2
EOR R0,R1,R2 ; R0 = R1 XOR R2
BIC R0,R1,R2 ; R0 = R1 && NOT(R2) azzera i bit che sono a 1 in R2
MVN R0,R2 ; R0 = NOT(R2)

; AL POSTODI #5 CI PUÒ ESSERE UN INDIRIZZO
LSL R0,R2,#5 ;R0 = R2 << 5 (SHIFT SINISTRO LOGICO)
lSR R0,R2,#5 ;R0 = R2 >> 5 (SHIFT DESTRO LOGICO)
ASR R0,R2,#5 ;R0 = R2 >>> 5 (SHIFT DESTRO ARITMETICO)
ROR R0,R2,#5 ;R0 = R2 ROR 5 (ROTAZIONE DESTRA)

MUL R0,R1,R2 ;R0 = R1*R2 (32 BIT MENO SIGNIFICATIVI)
UMULL R0,R1,R2,R3 ;MULL A 64 BIT -> R0=32 BIT(-SIGN) E R1 = 32 BIT(+SIGN) DI R2*R3
SMULL = UMULL SIGNED

CMP R0,#0 ;R0 === 0
ADDS E SUBS = ADD E SUB MA IMPOSTANO LE FLAG

LDR R3,[R0,R1,LSL #2] ;R3 = R0+ R1*2^2

```

![[Pasted image 20230511164306.png]]

ogni parola di dato è 4 byte -> indirizzo di parola = 4 * indice di parola

![[Pasted image 20230511165245.png]]

![[Pasted image 20230511173908.png]]

![[Pasted image 20230511174153.png]]

![[Pasted image 20230511174209.png]]

![[Pasted image 20230511174829.png]]

![[Pasted image 20230511174940.png]]

![[Pasted image 20230511175222.png]]

![[Pasted image 20230511175335.png]]

![[Pasted image 20230511175449.png]]

![[Pasted image 20230511175528.png]]

![[Pasted image 20230511175601.png]]

![[Pasted image 20230511175904.png]]

![[Pasted image 20230511175846.png]]

![[Pasted image 20230511180135.png]]

![[Pasted image 20230511180223.png]]

![[Pasted image 20230511180348.png]]

![[Pasted image 20230511180523.png]]

![[Pasted image 20230511181411.png]]

![[Pasted image 20230511181705.png]]

![[Pasted image 20230511184102.png]]

![[Pasted image 20230511184029.png]]

![[Pasted image 20230512174028.png]]

![[Pasted image 20230512174127.png]]

![[Pasted image 20230512174334.png]]

![[Pasted image 20230512174416.png]]

![[Pasted image 20230512174509.png]]

![[Pasted image 20230512174809.png]]

![[Pasted image 20230512175119.png]]

![[Pasted image 20230512175326.png]]

![[Pasted image 20230512175438.png]]

![[Pasted image 20230512175453.png]]

![[Pasted image 20230512175846.png]]

![[Pasted image 20230512175857.png]]

![[Pasted image 20230512175954.png]]

![[Pasted image 20230512180034.png]]

![[Pasted image 20230512180400.png]]

![[Pasted image 20230512180553.png]]

![[Pasted image 20230606150055.png]]

![[Pasted image 20230606150344.png]]

>![[Pasted image 20230606150726.png]]
>![[Pasted image 20230606150741.png]]

![[Pasted image 20230606150957.png]]

![[Pasted image 20230606151145.png]]

![[Pasted image 20230606151224.png]]

# CAPITOLO 7

micro-architettura ->  anello di congiunzione tra i circuiti logici e l'architettura

datapath -> costituito da strutture (registri, ALU, multiplexer, etc) e opera su parole di dati

control path -> riceve l’istruzione corrente dal datapath e  gli comunica
come eseguirla, attivando opportunamente gli ingressi di selezione dei multiplexer, le abilitazioni dei registri e i segnali di lettura e scrittura in memoria per controllare le operazioni del percorso dati.

>![[Pasted image 20230606152716.png]]
>![[Pasted image 20230606152732.png]]

MA (micro-architettura) a ciclo singolo -> 1 istruzione a ciclo
MA multi ciclo -> esegue le istruzioni in sequenze di cicli + brevi
MA pipeline -> + istruzioni (contemporaneamente) in un singolo ciclo

tempo di esecuzione = $\#istruzioni *(cicli/istruzione)*(secondi/ciclo)$

CPI = numero di cicli di clock per istruzione (in media)

IPC = numero di istruzioni per ciclo (in media)

$T_{ck}$ = periodo di clock = numero di secondi per ciclo


## MA ciclo singolo

PC = program counter = contiene l'indirizzo dell'istruzione da eseguire
>![[Pasted image 20230606160452.png]]
>![[Pasted image 20230606160415.png]]

![[Pasted image 20230606154858.png]]

PC si incrementa di 4 perché le istruzioni sono di 32 bit (4 byte)

INSTR(19-16) = Rn = registro sorgente

INSTR(11:0) = immediato -> viene esteso aggiungo 0 -> 31:12 = 0 e 11:0 = INSTR(11:0)

INSTR(15:12) = Rd = registro destinazione

ALU control:
- 00 = somma
- 01 = sottrazione
- 10 = AND
- 11 = ORR

RF = register file 

porta A3 = porta di scrittura
porta WD3 = porta ingresso dati per la scrittura
RegWrite = permesso di scrittura (0/1)

![[Pasted image 20230606160104.png]]

![[Pasted image 20230606160236.png]]

>![[Pasted image 20230606160718.png]]
>![[Pasted image 20230606160907.png]]

![[Pasted image 20230606160920.png]]

![[Pasted image 20230606161510.png]]

![[Pasted image 20230606161542.png]]

>![[Pasted image 20230606161713.png]]
>![[Pasted image 20230606161731.png]]

![[Pasted image 20230606161853.png]]

![[Pasted image 20230606161906.png]]

>![[Pasted image 20230606162013.png]]
>![[Pasted image 20230606162119.png]]
>![[Pasted image 20230606162134.png]]


![[Pasted image 20230606162245.png]]

![[Pasted image 20230606162304.png]]

![[Pasted image 20230606162333.png]]

![[Pasted image 20230606162457.png]]

![[Pasted image 20230606162514.png]]

![[Pasted image 20230606162538.png]]

![[Pasted image 20230606162758.png]]


## MA multiciclo

![[Pasted image 20230606162903.png]]

![[Pasted image 20230606163024.png]]

>![[Pasted image 20230606163035.png]]
>![[Pasted image 20230606163122.png]]
>![[Pasted image 20230606163141.png]]


![[Pasted image 20230606163253.png]]

![[Pasted image 20230606163309.png]]

![[Pasted image 20230606163506.png]]

![[Pasted image 20230606163622.png]]

![[Pasted image 20230606163633.png]]

![[Pasted image 20230606163648.png]]

>![[Pasted image 20230606163725.png]]
>![[Pasted image 20230606163738.png]]

![[Pasted image 20230606163752.png]]

![[Pasted image 20230606163829.png]]

![[Pasted image 20230606163845.png]]

>![[Pasted image 20230606163943.png]]
>![[Pasted image 20230606164002.png]]
>![[Pasted image 20230606164030.png]]
>![[Pasted image 20230606164102.png]]
>![[Pasted image 20230606164132.png]]
>![[Pasted image 20230606164148.png]]
>![[Pasted image 20230606164205.png]]
>![[Pasted image 20230606164230.png]]

![[Pasted image 20230606164251.png]]

![[Pasted image 20230606164303.png]]

![[Pasted image 20230606164348.png]]

![[Pasted image 20230606164416.png]]

![[Pasted image 20230606164442.png]]

![[Pasted image 20230606164536.png]]

![[Pasted image 20230606164704.png]]

![[Pasted image 20230606164828.png]]


## MA PIPELINE

>![[Pasted image 20230606165022.png]]
>![[Pasted image 20230606165042.png]]
>![[Pasted image 20230606165058.png]]

![[Pasted image 20230606165118.png]]

![[Pasted image 20230606165140.png]]

>![[Pasted image 20230606165205.png]]
>![[Pasted image 20230606165324.png]]

![[Pasted image 20230606165347.png]]

>![[Pasted image 20230606165442.png]]
>![[Pasted image 20230606165508.png]]


![[Pasted image 20230606165539.png]]

>![[Pasted image 20230606165605.png]]
>![[Pasted image 20230606165629.png]]
>![[Pasted image 20230606165645.png]]
>![[Pasted image 20230606165736.png]]
>![[Pasted image 20230606165754.png]]
>![[Pasted image 20230606165808.png]]
>![[Pasted image 20230606165820.png]]
>![[Pasted image 20230606165833.png]]

![[Pasted image 20230606170014.png]]

![[Pasted image 20230606170027.png]]

![[Pasted image 20230606170045.png]]

![[Pasted image 20230606170140.png]]

![[Pasted image 20230606170153.png]]

![[Pasted image 20230606170209.png]]

![[Pasted image 20230606170225.png]]

![[Pasted image 20230606170246.png]]

>![[Pasted image 20230606170308.png]]
>![[Pasted image 20230606170938.png]]


![[Pasted image 20230606170320.png]]

![[Pasted image 20230606181046.png]]

>![[Pasted image 20230606181104.png]]
>![[Pasted image 20230606181128.png]]
>![[Pasted image 20230606181139.png]]

>![[Pasted image 20230606181220.png]]
>![[Pasted image 20230606181239.png]]
>![[Pasted image 20230606181255.png]]
>![[Pasted image 20230606181307.png]]

![[Pasted image 20230606181317.png]]

>![[Pasted image 20230606181351.png]]
>![[Pasted image 20230606181406.png]]
>![[Pasted image 20230606181418.png]]

![[Pasted image 20230606181432.png]]

![[Pasted image 20230606181446.png]]

>![[Pasted image 20230606181541.png]]
>![[Pasted image 20230606181559.png]]
>![[Pasted image 20230606181622.png]]
>![[Pasted image 20230606181713.png]]

![[Pasted image 20230606181734.png]]



>![[Pasted image 20230606181747.png]]
>![[Pasted image 20230606181819.png]]

![[Pasted image 20230606181832.png]]

>![[Pasted image 20230606181920.png]]
>![[Pasted image 20230606181930.png]]
>![[Pasted image 20230606181944.png]]
>![[Pasted image 20230606182005.png]]

# SISTEMI OPERATIVI

## MEMORY HIERARCHY

![[Pasted image 20230622174337.png]]

![[Pasted image 20230622174356.png]]

![[Pasted image 20230622174426.png]]

![[Pasted image 20230622174524.png]]

![[Pasted image 20230622174559.png]]

![[Pasted image 20230622174839.png]]

![[Pasted image 20230622174849.png]]

![[Pasted image 20230622174953.png]]

![[Pasted image 20230622175007.png]]

![[Pasted image 20230622175036.png]]

$$CPU_{time} = IC*CPI*ClockCycleTime$$
$$CPI=CPI_{perfect}+CPI_{stall} \rightarrow CPI_{stall}=\frac{Memory\_Instructions}{Program\_Instructions}*Miss\_rate*Miss\_penalty$$

IC -> the number of program instructions executed

$\frac{Memory\_Instructions}{Program\_Instructions}*Miss\_rate$ -> Miss rate per memory instruction 

![[Pasted image 20230622175805.png]]

>C = capacità cache
>B = numero blocchi nella cache
>b = numero di word per blocco
>S = set di blocchi
>N = numero blocchi in un set

1. Direct mapped -> \#S = \#B
2. N-way set-asocative -> S = B/N
3. Fully assocative -> S = 1

$\log_2(S)$ = numero di bit per distinguere i vari set (dimensione SetOffset)

<Tag, SetOffset, ByteOffset> -> memory address (b = 1)
<Tag, SetOffset, BlockOffset, ByteOffset> -> memory address (b > 1)

V = valid bit

![[Pasted image 20230622180650.png]]

![[Pasted image 20230622180914.png]]

![[Pasted image 20230622181010.png]]

>![[Pasted image 20230622181122.png]]
>![[Pasted image 20230622181133.png]]

![[Pasted image 20230622181337.png]]

![[Pasted image 20230622181400.png]]

![[Pasted image 20230622181427.png]]

![[Pasted image 20230622181631.png]]


![[Pasted image 20230622181742.png]]

![[Pasted image 20230622181831.png]]

![[Pasted image 20230622182605.png]]

![[Pasted image 20230622182939.png]]

![[Pasted image 20230622182924.png]]

![[Pasted image 20230622183027.png]]

![[Pasted image 20230622183230.png]]

![[Pasted image 20230622183346.png]]

![[Pasted image 20230622183422.png]]

![[Pasted image 20230622183444.png]]

![[Pasted image 20230622183759.png]]

![[Pasted image 20230622183816.png]]

![[Pasted image 20230622184003.png]]

![[Pasted image 20230622184049.png]]

![[Pasted image 20230622184127.png]]

![[Pasted image 20230622184146.png]]

![[Pasted image 20230622184213.png]]

![[Pasted image 20230622184315.png]]

![[Pasted image 20230622184424.png]]

## INPUT OUTPUT

![[Pasted image 20230622185113.png]]

>Amdahl's law:
>![[Pasted image 20230622220127.png]]

![[Pasted image 20230622220201.png]]

I/O devices -> Control (commands e status report), Data

![[Pasted image 20230622220334.png]]

![[Pasted image 20230622220436.png]]

Bus -> A collection of data lines that is treated together as a single logical signal

![[Pasted image 20230622220630.png]]

![[Pasted image 20230622220659.png]]

![[Pasted image 20230622220916.png]]

![[Pasted image 20230622220946.png]]

![[Pasted image 20230622221138.png]]

![[Pasted image 20230623160954.png]]

![[Pasted image 20230623161133.png]]

>![[Pasted image 20230623161155.png]]
>![[Pasted image 20230623161223.png]]

>![[Pasted image 20230623161253.png]]
>![[Pasted image 20230623161327.png]]

![[Pasted image 20230623161417.png]]

![[Pasted image 20230623162238.png]]

![[Pasted image 20230623162354.png]]

![[Pasted image 20230623162412.png]]

![[Pasted image 20230623162618.png]]

![[Pasted image 20230623162652.png]]

![[Pasted image 20230623162715.png]]

![[Pasted image 20230623162740.png]]

![[Pasted image 20230623162830.png]]

![[Pasted image 20230623162908.png]]

![[Pasted image 20230623162933.png]]

![[Pasted image 20230623162949.png]]

![[Pasted image 20230623163001.png]]

## DISKS

