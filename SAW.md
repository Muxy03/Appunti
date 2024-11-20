
Tipi di App:
- Native app (spec SDK)
- Web app 
- Hybrid app -> Web app + accesso alle risorse del device (Electron)
- Progressive Web App -> Web app installabili, offline, feature of Native app

## CSS

Selettori:
- E F -> F discendente di E
- E > F -> F figlio di E
- E + F -> F subito preceduto da E
- E ~ F -> F preceduto da E
- E\[foo\] = E con attr "foo"
- E\[foo="bar"\] = E con attr foo="bar"
- E\[foo~=”bar”\] = E con attr foo che ha uno dei valori (" " separati) = "bar"
- E\[foo^="bar"\] = E con attr foo che inizia con "bar"
- E\[foo$="bar"\] = E con attr foo che termina con "bar"
- E\[foo*="bar"\] = E con attr foo che contiene "bar"
- ![[Pasted image 20241119182908.png]]
- ![[Pasted image 20241119182916.png]]

![[Pasted image 20241119183102.png]]


em -> dim font
rem -> dim font della root
vw,vh -> 1% della viewport
% -> el padre

## JS

![[Pasted image 20241119183307.png]]

![[Pasted image 20241119183732.png]]

![[Pasted image 20241119183752.png]]

![[Pasted image 20241119183814.png]]

![[Pasted image 20241119183827.png]]

![[Pasted image 20241119183927.png]]

![[Pasted image 20241119183944.png]]

![[Pasted image 20241119184003.png]]

![[Pasted image 20241119184025.png]]

![[Pasted image 20241119184045.png]]

runtime:
- stack -> pila di frame -> frame contiene funzione,fargs,variabili locali
- heap -> contiene gli oggetti, alloc a dichiarazione, garbage collector pulisce
- queue -> contiene messaggi 

![[Pasted image 20241119184121.png]]

![[Pasted image 20241119184145.png]]

![[Pasted image 20241119184155.png]]

![[Pasted image 20241119184219.png]]

![[Pasted image 20241119184252.png]]

![[Pasted image 20241119184454.png]]

![[Pasted image 20241119184513.png]]

![[Pasted image 20241119184551.png]]


## NPM 

MAJOR.MINOR.PATCH

package-lock -> Descrive in maniera univoca un albero delle dipendenze

## DOM

![[Pasted image 20241119184754.png]]

![[Pasted image 20241119184825.png]]

![[Pasted image 20241119184843.png]]

![[Pasted image 20241119184920.png]]

![[Pasted image 20241119185035.png]]

## REACT (bleah)

componente = un’istanza della classe  React.Component || una funzione che accetta degli input 
(props) e restituisce un ReactElement

expr JSX =  valore restituito da un componente React

JSX = mix HTML, JS

<> <\h1>BOH<\/h1> \</> = \<h1>BOH\</h1> in HTML finale

JSX impone la chiusura di qualunque tag

nome eventi camelCase

Hooks:
- useState(initValue) -> \[value,setValue\] -> considerare value readOnly -> lo stato è privato al componente -> l'update può essere asincrono
- useRef(initValue) -> {current} -> current punta al valore attuale
- useEffect(()=>{}) -> ![[Pasted image 20241119185317.png]]

![[Pasted image 20241119185350.png]]

![[Pasted image 20241119185423.png]]


## ANGULAR

out of box:
- Routing = navigazione client-side
- Forms = 2 modelli gestione di form
- HttpClient = client-sverver
- Animation = sistema di animazione basato sullo stato dell’applicazion
- PWA = strumenti per develope PWA
- Schematics =  scaffolding, refactoring, updat

GoF = gang of four -> Creational/Structural/Behavioral Patterns

Decorator pattern -> structural

Decoratori -> Sono funzioni che applicano il pattern al loro target -> in ts sono speciali dichiarazioni  applicabili a classi, metodi, proprietà (@sealed/ Object.seal(constructor);Object.seal(constructor.prototype))

Componenti -> classi ts @Component() -> selettore CSS, html template, set stili css

ng generate component -> stub nuovo componente

Componenti standalone -> sono direttamente importabili tramite imports

Modulo = isnieme di blocchi di codice coeso dedicato ad un specifico doimnio applicativo, contiene componenti e servizi, esporta componenti, etc -> @NgModule({...})

Templates = Html esteso -> {{expr js}}, \[proprietà/attributi\] = "cond", \[style.qualcosa\]="valore", (eventListener)="funzione"

Pipes = funzione per trasformare l'input in un altro valore -> @Pipe({})... -> classi che implementano PipeTransform (transform metodo)

builtin pipes:
- date -> {{today \| date}}
- async -> {{data \| async}}
- json -> {{obj \| json}}
- uppercase -> {{string \| uppercase}}
- ...

@Input rende visibile la proprietà al componente padre -> \[proprietà\]="valore"

il padre può rispondere agli eventi di un figlio:
- figlio -> @Output name = New EventEmitter\<type>(); -> (click)="name.emit(value)"
- padre -> (name)="onName($event)"

@Input name + @Output nameChange || \[(name)\]

\#indentificatore -> variabile locale in template

@ViewChild -> ![[Pasted image 20241119192630.png]]

Lifecycle:
- Creation: chiamata costruttore
- Change Detection
	- ngOnInit -> 1 volta init inputs
	- ngOnChanges -> on change inputs
	- ngDoCheck -> on control of changes
	- ngAfterViewInit -> 1 init vista
	- ngAfterViewChecked -> on control of changes vista
	- ngAfterContentChecked -> on control of changes content
- Rendering:
	- afterNextRender -> 1 volta init tutti componenti rendirizzati
	- afterRender -> ogni volta che i componenti vengono rendirizzati
- Desctruction:
	- ngOnDestroy -> 1 volta quando il componente viene distrutto

Attribute Directive -> ![[Pasted image 20241119192647.png]]

control flow:
- @if () {}
- @else if () {}
- @else {}
- @for () {} -> \$count,\$index,\$first,\$last,\$even,$odd
- @empty {}
- @switch () {@case () {} } -> cond controllata con ===
- @default {} -> opzionale
- @defer {} -> lazy loading componenti (solo standalone) -> when default = browser idle
- @placeholder(minimum 500ms/s) -> Esegue il rendering di un template da visualizzare prima del trigger di un blocco @defer
- @loading (after 100ms/s; minumum 1s) {} -> mostra blocco durante il caricamento di @defer
- @error {} -> mostra blocco se il caricamento di @defer fallisce

Triggers per @defer:
- on -> idle || viewport || interaction || hover || immediate || timer
- when -> cond
- on idle; on timer(5s) === on idle || on timer(5s)
- hover, interaction, viewport possono specificare un elemento tramite template reference (#id) che verrà usato come riferimento per la condizion
- prefetch -> permette di specificare delle condizioni (on e when) per il caricare le dipendenze del blocco defer prima che siano utilizza

dependency provider/consumer -> parlano tramite un Injector

Injector -> oggetto che trova una dipendenza come singleton in cache o la fornisce tramite un provider (ex: root)

definire dipendenze per DI -> 

![[Pasted image 20241119185658.png]]

modi di gestire form:
- Template-driven
- Reactive

![[Pasted image 20241119185807.png]]

![[Pasted image 20241119185824.png]]


RxJs = libreria composizione programmi su eventi asincroni -> Observable
![[Pasted image 20241119192723.png]]

Signals = wrapper di valori -> writable || read-only

Writable signals:
- const x = signal(initValue)
- x.set(value)
- console.log(x())
- x.update(v => v +1)

Computed signals:
- valutati lazy -> quando vengono letti per la prima volta
- memorized
- const cx = computed(() => x() \*2);

input signal:
![[Pasted image 20241119185902.png]]

model signals:
![[Pasted image 20241119185924.png]]

signal queries:
![[Pasted image 20241119185948.png]]

effect(()=>{
	...
})

toSignal(v) -> observable to signal
toObservable(v) -> signal to observable

## SVELTE

## REST

URI = Uniform Resource Identifier

HATEOAS = Hypermedia as the Engine of Application State

REST -> Stateless, cacheable, client-server, sistema stratificato

verbi HTTP:
- GET = ottenere risorsa -> 200 OK, 404 Not Found, 400 BadRequest, 500 Internal Server Error, idempotente (lato server)
- POST = aggiungere risorsa -> 201 Created, 500 Internal Server Error
- PUT = modifica, sostituendola, risorsa -> 200 OK, 204 No Content, 201 Created, 500 Internal Server Error, idempotente (lato server)
- PATCH = modifica risorsa (dati alcuni campi) -> simile a PUT ma invece di passare un'intera risorsa passiamo solo alcune chiavi
- DELETE -> 200 OK, 204 No Content, 404 Not Found, 500 Internal Server Error

![[Pasted image 20241119192156.png]]

CORS = Cross-Origin Resource Sharing -> l server nel caso di PUT, PATCH e DELETE deve 
anche permettere il metodo corrispondente con l’header Access-Control-Allow-Method

![[SAW24_12_-_Sviluppare_una_REST_API.pdf]]

## Authentication

![[Pasted image 20241119192320.png]]

OAuth2 -> framework 

![[Pasted image 20241119192335.png]]

Access Tokens = token scambiati che permettono l'accesso alle risorse

scambiare i token su TLS

tipi di token:
- Basic = username:password codificati base64
- Opaque Tokens = chunk di byte random
- JWT = token basati su JSON
- Refresh token =  utilizzati per rinnovare i token senza richiedere una nuova autenticazione

JWT:
- header.payload.signature
- header = algoritmo, tipo di token
- payload = set di claims
- signature = server per verificare l'integrità del messaggio
- ciascuna parte viene codificata in base64

![[Pasted image 20241119192350.png]]

## NOTIFICHE
![[SAW24_18_-_Notifiche.pdf]]
## PWA

caratteristiche:
- Reliable = devono caricarsi istant indipendentemente dalle cond di rete
- Fast
- Enganging = deve comportarsi come una app nativa

WebApp Manifest:
- name
- icons
- start_url
- display

\<link rel="manifest" type="application/manifest+json" href="manifest.webmanifest" />

Service Worker =  web worker: esegue uno script in background su un thread separato

SW proxy tra browser e la rete

SW states:
- Installing = dopo la reg del SW
- Actived = installazione OK
- Error = installazione NO OK
- Idle
- Terminated -> Idle
- Fetch/Message -> Idle

## FIREBASE AUTH
 BAAS = Backend As A Service 

Firebase Project -> 1+ Firebase Apps -> Risorse e Servizi

inizializzazione -> const auth = getAuth(fbConfig)

Operazioni possibili:
- OnAuthStateChanged(auth, (user) => {}) -> if(user) => Signed in else => Signed out
- signInWithEmailAndPassword(auth,email,password).then((userCred)=>{})
- signOut(auth).then(()=>{})
- createUserWithEmailAndPassword(auth, email, password).then((userCred)=>{})
- sendEmailVerification(auth.currentUser).then(()=>{})
- updatePassword(auth,newPassword).then(()=>{})
- sendPasswordResetEmail(auth,email).then(()=>{})
- deleteUser(aut.currentUser).then(()=>{})

![[Pasted image 20241119192517.png]]

## FIREBASE FIRESTORE

tipi database:
- Realtime -> database originale, JSON database, sync offline e realtime, scalabile
- Firestore -> NoSQL JSON-like database, ..., query dei dati, organizzato in documenti e collezioni, supporta transazioni
- Cloud Store -> object Storage, auto scaling, si integra con auth

const app = initializeApp(fbConfig);
const db = getFirestore(app);

operazioni disponibili:
- setDoc
- AddDoc
- UpdateDoc
- DeleteDoc
- getDoc
- getDocs
- onSnapShot -> collezioni e singoli doc
- query
- where -> dentro query
- orderBy
- limit
- count
- offlineData
- getDocFromCache
