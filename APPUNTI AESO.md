
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

pagina 152