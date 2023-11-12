Rete = interconnessione di dispositivi

sistemi terminali = host

dispositivi di interconnessione = router e switch

link = mezzi trasmissivi 

LAN < MAN < WAN

WAN punto a punto: ![[Pasted image 20231112150810.png]]

WAN a commutazione:
![[Pasted image 20231112150925.png]]

Reti a commutazione:
- circuito:
	- ![[Pasted image 20231112151120.png]]
	- ![[Pasted image 20231112151133.png]]
	- ![[Pasted image 20231112151205.png]]
- pacchetto:
	- ![[Pasted image 20231112151251.png]]
	- ![[Pasted image 20231112151311.png]]
	- ![[Pasted image 20231112151321.png]]

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

![[Pasted image 20231112153103.png]]

Ritardo end-to-end = somma dei ritardi dei singoli collegamenti

![[Pasted image 20231112153244.png]]

![[Pasted image 20231112153256.png]]

Modello OSI/OSI:
- Struttura:
	1.  Fisico: Comprende tutte le funzioni (procedure meccaniche ed elettroniche) che permettono una connessione a livello fisico.
	2. Collegamento: Si occupa di formare i dati da inviare attraverso il livello fisico, incapsulando i dati in un pacchetto provvisto di header (intestazione) e tail (coda), chiamato frame
	3. Rete: Si occupa dell’istradamento (“routing”) dei pacchetti cioè di determinare la sequenza di collegamenti punto-punto necessari per trasmettere un pacchetto da un nodo generico della rete a un altro
	4. Trasporto: Si occupa di instaurare, mantenere terminare una connessione
	5. Sessione: Assembla il dialogo tra nodi in unità logiche (sessione)
	6. Presentazione: Adatta la sintassi dei dati di ciascuna applicazione alla sintassi richiesta dalla sessione
	7. Applicazione: Protocolli a supporto di applicazioni distribuite
- ![[Pasted image 20231112153416.png]]
- ![[Pasted image 20231112153423.png]]

![[Pasted image 20231112153806.png]]

il flusso parte dal 7 strato e scende fino al 1 strato ->Ogni livello aggiunge all’informazione del livello superiore una propria sezione informativa (o più di una)

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

# LIVELLO APPLICATIVO

![[Pasted image 20231112154418.png]]

Paradigma client-server:
- ![[Pasted image 20231112154445.png]]

![[Pasted image 20231112154506.png]]

![[Pasted image 20231112154550.png]]

Socket Address -> 48 bit -> 32 bit IP address + 16 bit numero porta

![[Pasted image 20231112154712.png]]

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

![[Pasted image 20231112160859.png]]

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

![[Pasted image 20231112162014.png]]

![[Pasted image 20231112162028.png]]

![[Pasted image 20231112162040.png]]

![[Pasted image 20231112162452.png]]

![[Pasted image 20231112162631.png]]

![[Pasted image 20231112162648.png]]

![[Pasted image 20231112162704.png]]

![[Pasted image 20231112164124.png]]

## TELNET

TErminal NETwork -> suo di macchine remote

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
- control -> scambio di comandi e risposte tra client e server (Telenet)
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

![[Pasted image 20231112235952.png]]


# STRATO DI TRASPORTO
