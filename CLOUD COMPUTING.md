# 29/1/24

![[Introduction to cloud computing.pdf]]

QoS = Quality of Service
SLA = Service Level Agreement -> contratto tra service provider and client

![[IaaS.pdf]]

Tipi di Hypervisor:
consolidation ratio = \#VMs that can run on physical server
- 1:
	- loaded directly on the HW -> lightweight OS
	- higher consolidation ratio
	- for datacenter
- 2:
	- loaded on OS running on the HW -> software
	- lower consolidation ratio
	- for desktop/laptop

![[Pasted image 20240316164538.png]]

![[Pasted image 20240316164715.png]]

![[Pasted image 20240316165032.png]]

![[Pasted image 20240316165052.png]]

![[Pasted image 20240316165527.png]]

![[Pasted image 20240316165551.png]]

![[Containers.pdf]]

[Glossario container][https://developers.redhat.com/blog/2018/02/22/container-terminology-practical-introduction#containers_101]

![[Pasted image 20240316172608.png]]

![[Pasted image 20240316173816.png]]

docker compose -> consente, in modo piuttosto pratico, di gestire i propri container salvandone la configurazione di istanziamento in un unico file di configurazione in formato YAML

swarm mode -> managing a cluster of Docker hosts called a swarm

manager fails => un altro manager prende il controllo dei worker del fallito

worker fails => un altro worker, sotto lo stesso manager del fallito (possibilmente), prenderà il controllo del container del fallito

![[Pasted image 20240316175405.png]]

![[FaaS.pdf]]

vendor lock-in -> makes a customer dependent on a vendor for products or services, unable to use another vendor without substantial switching costs.



![[PaaS.pdf]]

![[Pasted image 20240316183218.png]]

![[Pasted image 20240316184459.png]]


## LAB AWS:
chiave.pem -> per accedere via ssh all'istanza di EC2

Per accedere al bucket S3 dalle istanze EC2 è necessario creare un Ruolo IAM per concedere l’accesso. -> il ruolo viene aggiunto all'istanza

Caricare file su S3 da EC2![[Pasted image 20240316171954.png]]

![[Pasted image 20240316172118.png]]

## LAB CONTAINER

![[Pasted image 20240316175817.png]]

![[Pasted image 20240316175853.png]]

se docker non trova in locale l'immagine va a fare il pull.

![[Pasted image 20240316180118.png]]

![[Pasted image 20240316180209.png]]

docker image ls -> list of local image

docker ps -a -> all of container (flag -a = all)

![[Pasted image 20240316180747.png]]

docker build -t nome -> -t sta per tag e permette di nominare l'immagine che creo con build

docker run -p host(PORT):container(PORT) nome -> -p sta per publish e serve per pubblicare una porta del container all'host

## LAB LAMBDA

 per le Lambda Functions dobbiamo prima concedere i permessi per poter interagire con i nostri buckets S3.

![[Pasted image 20240316182903.png]]

 nella creazione del livello bisogna specificare come runtime lo stesso della funzione 

input e output sono JSON

![[Pasted image 20240316183105.png]]

## LAB FIREBASE

[TUTORIAL][https://firebase.google.com/codelabs/firebase-get-to-know-web]

