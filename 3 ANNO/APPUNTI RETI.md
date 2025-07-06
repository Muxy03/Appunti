# INTRODUZIONE ALLE RETI

$2^{10} = 1KB, 2^{20} = 1MB, \dots$

Rete = interconnessione di dispositivi

sistemi terminali = host

dispositivi di interconnessione = router e switch

link = mezzi trasmissivi 

ISP = Internet Service Provider

IXP = Internet Exchange Point = peering point (inoltro) tra 2+ ISP

IETF = Internet Engineering Task Force = organismo che studia e sviluppa i protocolli in uso su Internet

ICANN = Internet Corporation for Assigned Names and Numbers = Coordina il sistema dei nomi di dominio (DNS), assegna i gruppi di indirizzi di rete,
identificativi di protocollo e ha funzioni di controllo (blando) dello sviluppo di Internet

W3C = World Wide Web Consortium = comunità internazionale che sviluppa standard aperti per favorire lo sviluppo del Web (HTML,...)

LAN < MAN < WAN

Tipi di WAN:
- punto a punto: ![[Pasted image 20231112150810.png]]
- a commutazione:![[Pasted image 20231112150925.png]]

Tipi di reti a commutazione:
-  di circuito:
	- ![[Pasted image 20231112151120.png]]
	- ![[Pasted image 20231112151133.png]]
	- ![[Pasted image 20231112151205.png]]
- di pacchetto:
	- ![[Pasted image 20231112151311.png]]
	- ![[Pasted image 20231112151321.png]]
- ![[Pasted image 20231112151251.png]]

![[Pasted image 20231112151403.png]]

![[Pasted image 20231112151416.png]]

Transmission rate -> bits/sec
Bandwith -> Hz

![[Pasted image 20231112151703.png]]

Throughput = Quantità di dati che possono essere trasmessi con successo dalla sorgente alla destinazione in un certo intervallo di tempo

![[Pasted image 20231112152402.png]]

![[Pasted image 20231112152523.png]]

cause di Latenza:
- elaborazione nodo
- accodamento
- trasmissione -> L/R -> R = transmission rate, L = len pachetto in bit
- propagazione -> d/s -> d = len link fisico (Ex. len cavo), s = vel. propagazione mezzo
- ![[Pasted image 20240504191033.png]]

![[Pasted image 20231112153103.png]]

Ritardo end-to-end = somma dei ritardi dei singoli collegamenti

Prodotto rate-ritardo: numero massimo di bit che il link può contenere ad un certo istante

![[Pasted image 20231112153244.png]]

![[Pasted image 20231112153256.png]]

- Modello ISO/OSI:
	- Struttura:
	1.  Fisico: Comprende tutte le funzioni (procedure meccaniche ed elettroniche) che permettono una connessione a livello fisico.
	2. Collegamento: Si occupa di formare i dati da inviare attraverso il livello fisico, incapsulando i dati in un pacchetto provvisto di header (intestazione) e tail (coda), chiamato frame
	3. Rete: Si occupa dell’instradamento (“routing”) dei pacchetti cioè di determinare la sequenza di collegamenti punto-punto necessari per trasmettere un pacchetto da un nodo generico della rete a un altro
	4. Trasporto: Si occupa di instaurare, mantenere terminare una connessione
	5. Sessione: Assembla il dialogo tra nodi in unità logiche (sessione)
	6. Presentazione: Adatta la sintassi dei dati di ciascuna applicazione alla sintassi richiesta dalla sessione
	7. Applicazione: Protocolli a supporto di applicazioni distribuite
	- ![[Pasted image 20231112153416.png]]
	- ![[Pasted image 20231112153423.png]]
	- ![[Pasted image 20240505163356.png]]

![[Pasted image 20231112153806.png]]

il flusso parte dal 7 strato e scende fino al 1 strato -> Ogni livello aggiunge all’informazione del livello superiore una propria sezione informativa (o più di una)

![[Pasted image 20231112154000.png]]

![[Pasted image 20231112154015.png]]

Stack TCP/IP:
- Struttura:
	1. Fisico
	2. Link
	3. Rete
	4. Trasporto
	5. Applicazione

- ![[Pasted image 20231112154142.png]]

![[Pasted image 20231112154232.png]]

![[Pasted image 20231112154243.png]]

# STRATO APPLICATIVO / LIVELLO APPLICAZIONE

![[Pasted image 20240505164753.png]]

![[Pasted image 20231112154418.png]]

Paradigma client-server:
- ![[Pasted image 20231112154445.png]]

![[Pasted image 20231112154506.png]]

![[Pasted image 20231112154550.png]]

Socket Address -> 48 bit -> 32 bit IP address + 16 bit numero porta

![[Pasted image 20231112154712.png]]

![[Pasted image 20240505170314.png]]

![[Pasted image 20231112154730.png]]

URI = Uniform Resource Identifier

tipi di URI:
- URL = UR Locator -> e identifica le risorse attraverso il loro meccanismo di accesso
	- \<scheme>://\<user>:\<password>\@\<host>:\<port>\<path>
	- scheme = protocollo di accesso
	- host = nome di dominio di un host o indirizzo IP
	- port = numero porta del server
	- path = contiene dati specifici per l’host (o scheme) e identifica la risorsa nel contesto di quello schema e host
	- URL assoluta = identifica una risorsa indipendentemente dal contesto in cui è usata
	- URL relativa = informazioni per identificare una risorsa in relazione ad un'altra URL
		- ![[Pasted image 20231112160022.png]]
- URN = UR Name -> devono rimanere globalmente unici e persistente anche quando la risorsa cessa di esistere e diventa non disponibile

![[Pasted image 20231112155830.png]]

## HTTP

HyperText Transfer Protocol

![[Pasted image 20231112160603.png]]

![[Pasted image 20231112160623.png]]

![[Pasted image 20231112160634.png]]

![[Pasted image 20231112160648.png]]

![[Pasted image 20231112160806.png]]

![[Pasted image 20240505215414.png]]

![[Pasted image 20240505215854.png]]

![[Pasted image 20231112160917.png]]

![[Pasted image 20231112161011.png]]

![[Pasted image 20231112161022.png]]

Tipi di header (coppie nome,valore):
- general -> relativi alla trasmissione
- entity -> relativi all'entità stessa
- request -> relativi alla richiesta
- response -> messaggio di risposta

![[Pasted image 20231112161256.png]]

![[Pasted image 20231112161342.png]]

![[Pasted image 20231112161351.png]]

![[Pasted image 20231112161401.png]]

![[Pasted image 20231112161412.png]]

![[Pasted image 20231112161432.png]]

![[Pasted image 20231112161442.png]]

![[Pasted image 20231112161519.png]]

![[Pasted image 20231112161535.png]]

![[Pasted image 20231112161606.png]]

![[Pasted image 20231112161618.png]]

![[Pasted image 20231112161646.png]]

![[Pasted image 20231112161721.png]]

![[Pasted image 20231112161733.png]]

HEAD = SIMILE A GET MA SENZA MESSAGE BODY NELLA RISPOSTA![[Pasted image 20231112162014.png]]

![[Pasted image 20231112162028.png]]

![[Pasted image 20231112162040.png]]

![[Pasted image 20231112162452.png]]

![[Pasted image 20231112162631.png]]

![[Pasted image 20231112162648.png]]

![[Pasted image 20231112162704.png]]

![[Pasted image 20231112164124.png]]

## TELNET

TErminaL NETwork -> uso di macchine remote

![[Pasted image 20231112164354.png]]

![[Pasted image 20231112164413.png]]

![[Pasted image 20231112164434.png]]

![[Pasted image 20231112164446.png]]

![[Pasted image 20231112164501.png]]

![[Pasted image 20231112164509.png]]

![[Pasted image 20231112164518.png]]


## EMAIL-SMTP

![[Pasted image 20231112164821.png]]

![[Pasted image 20231112164830.png]]

![[Pasted image 20231112164848.png]]

![[Pasted image 20231112164901.png]]

alias = cassetta postale virtuale -> molti-uno / uno-molti

Simple Mail Transfer Protocol

![[Pasted image 20231112165010.png]]

![[Pasted image 20231112165034.png]]

![[Pasted image 20231112165053.png]]

![[Pasted image 20231112165103.png]]

![[Pasted image 20231112165112.png]]

![[Pasted image 20240506171152.png]]

![[Pasted image 20231112165138.png]]

![[Pasted image 20231112165150.png]]

![[Pasted image 20231112165210.png]]

![[Pasted image 20231112165451.png]]

![[Pasted image 20231112165504.png]]

![[Pasted image 20231112165643.png]]

![[Pasted image 20231112165653.png]]

## FTP

File Transfer Protocol

![[Pasted image 20231112233913.png]]

![[Pasted image 20231112233946.png]]

Tipi di connessioni: (usano TCP)
- control -> scambio di comandi e risposte tra client e server (Telnet)
- data -> connessione su cui i dati sono trasferiti con modi e tipi specificati. I dati trasferiti possono essere parte di un file, un file o un set di file.

FTP è stateful

![[Pasted image 20231112234205.png]]

![[Pasted image 20231112234538.png]]

![[Pasted image 20231112234556.png]]

modalità creazione connessione TCP:
- Active:
	- ![[Pasted image 20231112234644.png]]
- Passive:
	- ![[Pasted image 20231112234704.png]]

![[Pasted image 20231112234730.png]]

![[Pasted image 20231112234741.png]]

![[Pasted image 20231112234818.png]]

![[Pasted image 20231112234828.png]]


## DNS

Domain Name System

![[Pasted image 20231112235123.png]]

![[Pasted image 20231112235201.png]]

![[Pasted image 20231112235220.png]]

![[Pasted image 20231112235231.png]]

![[Pasted image 20231112235253.png]]

![[Pasted image 20231112235327.png]]

![[Pasted image 20231112235344.png]]

![[Pasted image 20231112235429.png]]

![[Pasted image 20231112235442.png]]

![[Pasted image 20231112235456.png]]

![[Pasted image 20231112235507.png]]

![[Pasted image 20231112235530.png]]

![[Pasted image 20231112235540.png]]

Query Ricorsiva:
	![[Pasted image 20231112235627.png]]

Query Iterativa:
	![[Pasted image 20231112235659.png]]

![[Pasted image 20231112235726.png]]

![[Pasted image 20231112235736.png]]

![[Pasted image 20231112235754.png]]

![[Pasted image 20231112235809.png]]

![[Pasted image 20231112235940.png]]

![[Pasted image 20240110000004.png]]

![[Pasted image 20231112235952.png]]


# STRATO DI TRASPORTO

![[Pasted image 20231116182143.png]]

![[Pasted image 20231116182206.png]]

![[Pasted image 20231116182215.png]]

![[Pasted image 20231116182304.png]]

![[Pasted image 20231116182323.png]]

![[Pasted image 20231116182344.png]]

![[Pasted image 20231117085712.png]]

![[Pasted image 20231117085724.png]]

![[Pasted image 20231117085746.png]]

![[Pasted image 20231117085804.png]]

![[Pasted image 20231117085817.png]]

![[Pasted image 20231117085835.png]]

![[Pasted image 20231117085851.png]]

## TCP

orientamento allo stream -> TCP vede i dati come un flusso di byte ordinati ma non strutturati (len indefinita)

orientato alla connessione:
- handshake fra processi (source e dest); 
- lo stato della connessione risiede solo nei punti terminali (es. router) della rete (NO INTERMEDI)
- connessione = circuito dedicato -> per gli applicativi  -> TCP offre servizi CONNECTION ORIENTED (IP invece CONNECTION LESS)
- connessione full-duplex -> connessione in tutte e due le direzioni contemporaneamente (slegate fra loro) e connessione punto-punto

![[Pasted image 20231126170935.png]]

![[Pasted image 20231126170952.png]]

![[Pasted image 20231126171003.png]]

![[Pasted image 20231126171018.png]]

![[Pasted image 20231126171038.png]]

TCP numera i byte:
- Numero di sequenza = numero del primo byte del segmento (si parte da un initial sequence number random != 0)
- Numero di riscontro = numero ultimo byte correttamente ricevuto + 1 -> ACK = y significa che aspetto il byte y e che ho ricevuto correttamente tutti i byte fino a y-1 incluso

![[Pasted image 20231126171335.png]]

FLAG SYN settato $\Rightarrow$ numero di sequenza = ISN (initial sequence number) e il primo byte di dati è ISN+1

FLAG ACK settato $\Rightarrow$ numero di riscontro = valore del prossimo numero di sequenza che il mittente del segmento si aspetta di ricevere dall'altro host. Una volta che la connessione è stabilita è sempre inviato

HLEN = len header TCP espressa in parole di 4 byte -> 1 to 15 parole da 4 byte

![[Pasted image 20231126172039.png]]

![[Pasted image 20231126172052.png]]

![[Pasted image 20231126172105.png]]

Handshake a 3 vie:
- ![[Pasted image 20231126172223.png]]
- dopo l'handshake a livello trasporto non c'è più distinzione tra client e server
- ![[Pasted image 20231126172340.png]]

![[Pasted image 20231126172428.png]]

![[Pasted image 20231126172453.png]]

![[Pasted image 20231126172603.png]]

![[Pasted image 20240507173706.png]]

![[Pasted image 20231126172723.png]]

![[Pasted image 20231126172745.png]]

![[Pasted image 20231126172758.png]]

![[Pasted image 20231126172914.png]]

![[Pasted image 20231126173736.png]]

![[Pasted image 20231126173745.png]]

![[Pasted image 20231126173758.png]]

![[Pasted image 20231126173824.png]]

![[Pasted image 20231126173837.png]]

![[Pasted image 20231126173856.png]]

![[Pasted image 20231126173908.png]]

![[Pasted image 20231126173925.png]]

![[Pasted image 20231126174014.png]]

![[Pasted image 20231126174036.png]]

![[Pasted image 20231126174058.png]]

![[Pasted image 20231126174152.png]]

RTO = tempo timeout
RTT = tempo trascorso da quando si invia un segmento a quando se ne riceve il riscontro

![[Pasted image 20231126174511.png]]

$\alpha = \frac{1}{8}$ 

![[Pasted image 20231126174530.png]]

sliding window:![[Pasted image 20231126174629.png]]

![[Pasted image 20231126175005.png]]

![[Pasted image 20231126175043.png]]

![[Pasted image 20231126181019.png]]

![[Pasted image 20231126181050.png]]

![[Pasted image 20231126181101.png]]

![[Pasted image 20240507181800.png]]

![[Pasted image 20231126181159.png]]

sliding window = min(rwnd,cwnd) = min(receiver window, congestion window)

rate invio $\leq \frac{min(rwnd,cwnd)}{RTT}$ 

Congestion Control Algorithm:
- slow start
- AIMD (Incremento addittivo e decremendo moltiplicativo)
- fast recovery
- Reazione ai time-out

![[Pasted image 20231126181733.png]]

![[Pasted image 20231126181756.png]]

![[Pasted image 20231126181855.png]]

![[Pasted image 20240110171353.png]]

![[Pasted image 20231126181913.png]]

### TCP RENO:

Algoritmo di congestione

![[Pasted image 20231126182115.png]]

![[Pasted image 20231126182728.png]]

![[Pasted image 20231126182742.png]]
![[Pasted image 20240110171320.png]]
### TCP Tahoe:

![[Pasted image 20231126182826.png]]

![[Pasted image 20240110171433.png]]
### TCP CUBIC:

![[Pasted image 20231126183417.png]]

![[Pasted image 20231126183427.png]]



### ECN (Explicit Congestion Notification):

![[Pasted image 20231126183508.png]]



![[Pasted image 20231126183536.png]]

![[Pasted image 20231126183545.png]]

![[Pasted image 20231126183704.png]]

![[Pasted image 20231126183714.png]]


## UDP:

User Datagram Protocol

![[Pasted image 20231126183758.png]]

![[Pasted image 20231126183822.png]]

![[Pasted image 20231126183900.png]]

![[Pasted image 20231126183908.png]]

![[Pasted image 20231126183920.png]]

![[Pasted image 20231126183952.png]]

![[Pasted image 20231126184004.png]]

![[Pasted image 20231126184052.png]]

![[Pasted image 20231126184101.png]]

![[Pasted image 20231126184113.png]]

![[Pasted image 20231126184125.png]]

![[Pasted image 20231126184135.png]]

![[Pasted image 20231126184147.png]]


# LIVELLO RETE:

Responsabile della consegna dei datagrammi tra gli host

![[Pasted image 20231126184334.png]]

![[Pasted image 20231126184347.png]]

![[Pasted image 20231126184430.png]]

![[Pasted image 20231126184442.png]]

![[Pasted image 20231126184458.png]]

![[Pasted image 20231126184555.png]]

![[Pasted image 20231126185025.png]]

![[Pasted image 20231126185034.png]]

![[Pasted image 20231126185043.png]]

![[Pasted image 20231126185052.png]]

>![[Pasted image 20231126185112.png]]
> - TCP:
>	If the lower level is IP (or other protocol that provides this feature) and source routing is used, the interface must allow the route information to be communicated.  This is especially important so that the source and destination addresses used in the TCP checksum be the originating source and ultimate destination. It is also important to preserve the return route to answer connection requests.
>- UDP:
>	![[Pasted image 20240508161202.png]]

![[Pasted image 20231126185132.png]]

![[Pasted image 20231126185148.png]]

![[Pasted image 20231126185158.png]]

![[Pasted image 20231126185242.png]]

![[Pasted image 20231126185256.png]]

SCHEMA FRAMMENTAZIONE:
- ![[Pasted image 20240508162547.png]]
- \# frammenti = len iniziale / MTU -> (4020 / 1420)
- offset = (MTU - 20) / 8 -> (1400 / 8) (20 = dim header IP)

![[Pasted image 20231126185317.png]]

![[Pasted image 20231126185331.png]]

![[Pasted image 20231126185343.png]]

![[Pasted image 20231126185358.png]]

![[Pasted image 20231126185418.png]]

![[Pasted image 20240508163339.png]]

![[Pasted image 20231126185437.png]]

![[Pasted image 20231126185449.png]]

![[Pasted image 20231126185504.png]]

![[Pasted image 20231126185536.png]]

![[Pasted image 20231126185548.png]]

![[Pasted image 20231126185626.png]]

![[Pasted image 20231126185652.png]]

## DHCP:

![[Pasted image 20231126190257.png]]

![[Pasted image 20231126190243.png]]

![[Pasted image 20231126190400.png]]

SCHEMA:
- n = \# numero ind. del sottoblocco
- m = potenza di 2 >= n
- n = 120 => m = 7 ($2^7 = 128$) => /25 (32 - 7) (25 bit per la rete) -> 126 host disponibili ($2^7-2$)

![[Pasted image 20231126190441.png]]

![[Pasted image 20231126190455.png]]

![[Pasted image 20231126190554.png]]

![[Pasted image 20231126190605.png]]

![[Pasted image 20231126190620.png]]

![[Pasted image 20231126190630.png]]

USA UDP A LIVELLO TRASPORTO

![[Pasted image 20231126190900.png]]

![[Pasted image 20231126190913.png]]

![[Pasted image 20231126190930.png]]

![[Pasted image 20231126190938.png]]

![[Pasted image 20231126190953.png]]

forwarding diretto -> destinatario appartiene alla stessa rete -> controllo nella tabella IP-MAC addr. soddisfatto

forwarding indiretto -> destinatario non appartiene alla stessa rete -> controllo nella tabella IP-MAC addr. non soddisfatto -> default router

![[Pasted image 20231126191041.png]]

![[Pasted image 20231126191257.png]]

![[Pasted image 20231126191312.png]]

Aggregazione indirizzi:
- ![[Pasted image 20240508174612.png]]

![[Pasted image 20240508234712.png]]


![[Pasted image 20240508234800.png]]

## NAT e ICMP:

![[Pasted image 20231129112417.png]]

![[Pasted image 20231129112426.png]]

![[Pasted image 20240508175032.png]]

![[Pasted image 20231129112444.png]]

![[Pasted image 20231129112625.png]]

![[Pasted image 20231129112641.png]]

quante comunicazioni può gestire un router NAT con un solo indirizzo pubblico ? il numero delle porte di router

![[Pasted image 20231129112715.png]]

![[Pasted image 20231129114041.png]]

![[Pasted image 20231129114626.png]]

![[Pasted image 20231129114059.png]]

![[Pasted image 20231129114148.png]]

![[Pasted image 20231129114203.png]]

![[Pasted image 20231129114236.png]]

![[Pasted image 20231129114248.png]]

![[Pasted image 20231129114333.png]]

![[Pasted image 20231129114344.png]]


## ARCHITETTURA ROUTER:

![[Pasted image 20231129122516.png]]

![[Pasted image 20231129123036.png]]

![[Pasted image 20231129123050.png]]

![[Pasted image 20231129123923.png]]

![[Pasted image 20231129123947.png]]

![[Pasted image 20231201141555.png]]

![[Pasted image 20231201141604.png]]

![[Pasted image 20231201141619.png]]

![[Pasted image 20231201141634.png]]

![[Pasted image 20231201141646.png]]

![[Pasted image 20231201141720.png]]

### Distance Vector Algorithm:
distribuito, iterativo, asincrono

![[Pasted image 20231201141829.png]]

![[Pasted image 20231201141900.png]]

![[Pasted image 20231201141912.png]]

![[Pasted image 20231201141925.png]]

![[Pasted image 20240508182650.png]]

![[Pasted image 20240509171352.png]]
SCHEMA:
- ![[Pasted image 20240509171810.png]]

![[Pasted image 20231201141941.png]]

![[Pasted image 20231201141952.png]]

![[Pasted image 20231201142003.png]]

### Link-State Algoritm:

![[Pasted image 20231201142021.png]]

![[Pasted image 20231201142051.png]]

![[Pasted image 20231201142111.png]]

![[Pasted image 20231201142138.png]]

![[Pasted image 20231201142152.png]]

![[Pasted image 20231201142213.png]]

![[Pasted image 20231201142221.png]]

TIPI DI AS:
- AS stub -> collegato ad un solo altro AS
- AS multihomed -> collegato a più di un altro AS (ma trasporta – come lo stub - solo traffico di cui è origine o destinazione)
- AS transito

![[Pasted image 20231201142233.png]]

### RIP:

usa UDP (porta 520)

![[Pasted image 20231201142254.png]]

![[Pasted image 20231201142311.png]]

### OSPF:

Open Shortest Path First

![[Pasted image 20231201142322.png]]

![[Pasted image 20231201142415.png]]

### BGP:

Border Gateway Protocol

![[Pasted image 20231201142446.png]]

![[Pasted image 20231201142455.png]]

![[Pasted image 20231201142504.png]]

![[Pasted image 20231201142521.png]]

![[Pasted image 20231201142532.png]]

![[Pasted image 20231201142543.png]]

![[Pasted image 20231201142633.png]]

![[Pasted image 20231201142642.png]]

### IPV6:

![[Pasted image 20231201142658.png]]

![[Pasted image 20231201142709.png]]

![[Pasted image 20231201142720.png]]

![[Pasted image 20231201142738.png]]

![[Pasted image 20231201142747.png]]

![[Pasted image 20231201142756.png]]


# LIVELLO COLLEGAMENTO:

![[Pasted image 20231201142920.png]]

![[Pasted image 20231201142930.png]]

![[Pasted image 20231201142956.png]]

![[Pasted image 20231201143006.png]]

![[Pasted image 20231201143015.png]]

![[Pasted image 20231201143059.png]]

![[Pasted image 20231201143108.png]]

![[Pasted image 20231201143119.png]]

![[Pasted image 20231201143126.png]]

![[Pasted image 20231201143142.png]]

![[Pasted image 20231201143214.png]]

![[Pasted image 20231201143228.png]]

![[Pasted image 20231201143238.png]]

## SLOTTED ALOHA:

![[Pasted image 20231201143258.png]]

![[Pasted image 20231201143308.png]]

## ALOHA PURE (UNSLOTTED):

![[Pasted image 20231201143332.png]]

## CSMA:

carrier sense multiple access

![[Pasted image 20231201143657.png]]

![[Pasted image 20231201143712.png]]

## CSMA/CD:

![[Pasted image 20231201143741.png]]

![[Pasted image 20231201143753.png]]

![[Pasted image 20231201143810.png]]

![[Pasted image 20231201143826.png]]

![[Pasted image 20231201143836.png]]

![[Pasted image 20231201143850.png]]

![[Pasted image 20231201143902.png]]

![[Pasted image 20231201143911.png]]

![[Pasted image 20231201143924.png]]

![[Pasted image 20231201143931.png]]

![[Pasted image 20231201143947.png]]

ARP: IP -> MAC

![[Pasted image 20231201144021.png]]

![[Pasted image 20231201144029.png]]

![[Pasted image 20231201144040.png]]

![[Pasted image 20231201144049.png]]

![[Pasted image 20231201144111.png]]

![[Pasted image 20231201144119.png]]

![[Pasted image 20231201144132.png]]

![[Pasted image 20231201144157.png]]

![[Pasted image 20231201144209.png]]

![[Pasted image 20231201144228.png]]

![[Pasted image 20231201144236.png]]

![[Pasted image 20231201144247.png]]

![[Pasted image 20231201144258.png]]

ESEMPIO 51-53![[L14_Collegamento.pdf#Page=51]] 
## ETHERNET:

![[Pasted image 20231228183928.png]]

![[Pasted image 20231228183947.png]]

![[Pasted image 20231228184003.png]]

![[Pasted image 20231228184028.png]]

![[Pasted image 20231228184048.png]]

![[Pasted image 20231228184101.png]]

![[Pasted image 20231228184120.png]]

![[Pasted image 20231228184129.png]]

![[Pasted image 20231228184148.png]]

![[Pasted image 20231228184425.png]]

![[Pasted image 20231228184432.png]]

![[Pasted image 20231228184443.png]]

![[Pasted image 20231228184454.png]]

![[Pasted image 20231228184508.png]]

![[Pasted image 20231228184533.png]]

![[Pasted image 20231228184545.png]]

## VLAN:

![[Pasted image 20231228184636.png]]

![[Pasted image 20231228184649.png]]

![[Pasted image 20231228184658.png]]

![[Pasted image 20231228184728.png]]

![[Pasted image 20231228184739.png]]

![[Pasted image 20231228184747.png]]

![[Pasted image 20231228184811.png]]

![[Pasted image 20231228184820.png]]

![[Pasted image 20231228184935.png]]

ESEMPIO 33-39 ![[L14_Collegamento_parte2.pdf#Page=33]]

# CENNI DI SICUREZZA:

## Peer-to-Peer:

paradigma peer-to-peer (P2P) -> tutti gli host fanno da client e da server (servent)

![[Pasted image 20240515000027.png]]

![[Pasted image 20240515000114.png]]

- ![[Pasted image 20240515000146.png]]
	- ![[Pasted image 20240515000324.png]]
	- ![[Pasted image 20240515000340.png]]
	- ![[Pasted image 20240515000353.png]]
- ![[Pasted image 20240515000543.png]]
	- ![[Pasted image 20240515000616.png]]
	- ![[Pasted image 20240515000626.png]]
	- ![[Pasted image 20240515000642.png]]
	- ![[Pasted image 20240515000652.png]]
	- ![[Pasted image 20240515000705.png]]
	- ![[Pasted image 20240515000714.png]]
	- ![[Pasted image 20240515000723.png]]


## SICUREZZA:

![[Pasted image 20240515000840.png]]

![[Pasted image 20240515000906.png]]

![[Pasted image 20240515000927.png]]

![[Pasted image 20240515000940.png]]

![[Pasted image 20240515001103.png]]

![[Pasted image 20240515001131.png]]

![[Pasted image 20240515001256.png]]

![[Pasted image 20240515001313.png]]

![[Pasted image 20240515001332.png]]

![[Pasted image 20240515001342.png]]

IPSec = set di protocolli per fornire sicurezza e livello rete -> modalità trasporto / tunnel

![[Pasted image 20240515001453.png]]

![[Pasted image 20240515001607.png]]

![[Pasted image 20240515001621.png]]

![[Pasted image 20240515001634.png]]

![[Pasted image 20240515001646.png]]

![[Pasted image 20240515001707.png]]

![[Pasted image 20240515001715.png]]

