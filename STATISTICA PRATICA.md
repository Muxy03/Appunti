
X e Y variabili aleatorie sono indipendenti se $P(X \in A,Y \in B) = P(X \in A)*P(Y, \in B)$

la funzione di ripartizione è data da un integrale solo per le variabili aleatorie con densità, per cui la densità è uguale a $f(x)$ dove $f(x) = 0$ per $x < 0$ 

ammettere un momento significa che $E[|X|^n] < +\infty$ 

legge debole dei grandi numberi = sia $X_1,X_2,\dots$ uan successione di v.a. iid con momento secondo finito, $\mu = E[X_i]$ il loro valore atteso. Allora la media $\overline{X_n}$ converge in probabilità a $\mu$ per n -> +inf

Teorema Centrale del Limite: sia $X_1,X_2,\dots$ uan successione di v.a. iid con momento secondo finito, $\mu = E[X_i]$ il loro valore atteso e $\sigma^2(X_i)=\sigma^2 > 0$. Presi $-\infty \le a < b \le +\infty$ si ha che 
$$
\lim_{n \rightarrow +\infty}{P(a \le \frac{X_1+X_2+\dots-n*\mu}{\sigma*\sqrt{n}} \le b)} = \frac{1}{2\pi}*\int_a^b{e^{-\frac{x^2}{2}}dx} = \Phi(b) - \Phi(a) 
$$

ovvero ciò che sta tra a e b in P converge in distribuzione a una v.a Gaussiana standard

![[Pasted image 20241214194449.png]]

![[Pasted image 20241214003105.png]]

![[Pasted image 20241213234309.png]]
## TEST

campione statistico = famiglia finita di variabili aleatorie iid (indipendenti e equi-distribuite)

statistica = $g(X_1,\dots,X_n)$

![[Pasted image 20241213231725.png]]

media campionaria = $\overline{X_n} = \frac{X_1+\dots+X_n}{n}$
varianza campionaria = $S^2_n = \frac{\sum_{i=1}^n (X_i-\overline{X})^2}{n-1}$

media campionaria e varianza campionaria sono stimatori corretti.

media campionaria e varianza campionaria sono stimatori consistenti rispettivamente per valore atteso e varianza. (grazie a LGN e suo corollario)

stimatore di un parametro θ della distribuzione è una statistica che approssima il valore di θ

stimatore corretto se ammette momento primo (valore atteso) e $E_\theta[g(X_1,\dots,X_n)] = \theta$ (la media dello stimatore è il parametro θ)

stimatore x Bernoulli media campionaria
stimatore x Gaussiana varianza campionaria (m già nota e $\sigma^2$ da stimare)

![[Pasted image 20241213233925.png]]

![[Pasted image 20241213234030.png]]

![[Pasted image 20241213235459.png]]

![[Pasted image 20241214003444.png]]

campione iid con momento secondo finito => l'efficienza della media campionaria cresce col crescere di n

![[Pasted image 20241214003837.png]]

stima di massima verosimiglianza = sceglie un parametro $\theta$ per massimizzare la funzione di verosimiglianza

![[Pasted image 20241214004536.png]]

![[Pasted image 20241214005227.png]]

Intervalli di fiducia per la media con campione statistico Gaussiano $N(m,\sigma)$:
- intervallo di fiducia sensato = $[\overline{X}_n \pm d]$, con d >0
- d = precisione della stima se l'intervallo sopra è un intervallo di fiducia per la media m
- $d/\overline{X}_n$ con le condizione di sopra è detta precisione relativa della stima
- ![[Pasted image 20241214010126.png]]
- ![[Pasted image 20241214011014.png]]
- per n >= 60 possiamo approssimare il quantile della variabile di Student con quello della Gaussiana standard
- $t_{\beta,n} > q_\beta, \forall{\beta > 1/2}$

- ![[Pasted image 20241214012251.png]]
- ![[Pasted image 20241214012457.png]]
- Gli intervalli di fiducia unilateri con varianza sconosciuta sono perfettamente analoghi, sostituendo a σ la variabile $S_n$ e ai quantili della variabile Gaussiana standard quelli della distribuzione di Student

Intervalli di fiducia per la media con campione statistico Bernoulli $B(p)$:
- ![[Pasted image 20241214012803.png]]

 ![[Pasted image 20241214013519.png]]

analogo a sopra per caso con varianza non nota -> al posto di $\sigma$ mettere $S_n$

![[Pasted image 20241214013930.png]]

![[Pasted image 20241214014201.png]]

Un test statistico è una procedura per decidere se accettare o rifiutare l’ipotesi nulla $H_0$ a partire dai valori assunti dal campione

![[Pasted image 20241214014401.png]]

rifiutare l'ipotesi nulla => i dati sono contro $H_0$
accettare l'ipotesi nulla => i dati non dicono niente contro $H_0$

![[Pasted image 20241214020658.png]]

![[Pasted image 20241214020814.png]]

![[Pasted image 20241214020949.png]]

la potenza è la probabilità di rifiutare correttamente l'ipotesi nulla quando questa è falsa.

![[Pasted image 20241214021315.png]]

![[Pasted image 20241214021437.png]]

Z TEST = test media di campione gaussiano con varianza nota

ESEMPIO Z TEST (bilatero):
- $H_0)m=m_0,H_1) m \neq m_0$
- regione critica di livello $\alpha$ -> $C=\{|\overline{X}_n-m_0| > \frac{\sigma}{\sqrt{n}} * q_{1- (\alpha/2)}\}$
- se viene rispettata la condizione di C si rifiuta $H_0$ altrimenti si accetta
- l'ipotesi $H_0$ viene accettata <=> $m_0$ appartiene all'intervallo di fiducia per la media con livello di fiducia (1−α)
- p-value = $2*[1 - \Phi(\frac{\sqrt{n}}{\sigma}*|\overline{X}_n - m_0|)]$
- si rifiuta $H_0$ <=> $\alpha > \overline{\alpha}$
- probabilità errore seconda specie (falso negativo) = $\Phi(\sqrt{n} * \frac{|m_0-m|}{\sigma}+q_{1-(\alpha/2)}) - \Phi(\sqrt{n} * \frac{|m_0-m|}{\sigma} - q_{1-(\alpha/2)})$
- ![[Pasted image 20241214163605.png]]

![[Pasted image 20241214163921.png]]

![[Pasted image 20241214163950.png]]
## VARIABILI ALEATORIE:

quando 2 va hanno la stessa legge di probabilità sono equi-distribuite.

Una variabile aleatoria è detta discreta se la sua immagine X(Ω) ⊂ R è un sottoinsieme al più numerabile di R

p($x_i$) = probabilità che X = $x_i$ -> funzione di massa = $p_X(x) = P_X(x) = P(X = x)$

v.a discreta:
- legge = funzione di massa = $P_X(A) = \sum_{x_i \in A}{p_X(x_i)}$

v.a con densità:
- legge = densità di probabilità = $P_X(A) = \int_A{f(x)dx}$

funzione di ripartizione (cdf) = $F_X(x) = P\{X \le x\}$:
- ![[Pasted image 20241214173558.png]]
- caso v.a discreta => $F_X(t) = \sum_{x_i \le t} {p(x_i)}$ | $P\{X = x\} = F(x) - F_\_(x),F_\_(x) = \lim_{y \rightarrow x^-}{F(y)}$
- caso v.a con densità => $F_X(x) = \int_{-\infty}^x{f(t)dt}$ | la densità è uguale alla derivata della funzione di ripartizione

![[Pasted image 20241214174353.png]]

### BINOMIALE

variabile discreta che conta il numero di successi in una sequenza di n prove indipendenti, dove ogni prova ha solo 2 esiti (+/-).
probabilità di successo di ogni singola prova: 0 < p < 1
$$B(n,p):P\{X = h\} = \binom{n}{h}*p^h*(1-p)^{n-h}$$
$$
\binom{a}{b} = \frac{a!}{b!*(a-b)!}
$$
### GEOMETRICA

variabile discreta che conta il numero di prove necessarie per ottenere il primo successo in una sequenza di prove indipendenti, ognuna con stessa probabilità 0< p < 1

$$
G(p):P\{X = h\} = (1-p)^{h-1}*p,0 \le h\le n
$$
assenza di memoria: $P\{X = n+h | X > n\} = P\{X = h\}$

### IPERGEOMETRICA

variabile discreta che conta il numero di successi in un campione di dimensione r, estratto senza rimpiazzo da una popolazione di dimensione n, contenente h successi

$$
I(n,h,r): P(X = k) = \frac{\binom{h}{k} * \binom{n-h}{n-k}}{\binom{n}{r}},k=0,\dots,h
$$

### POISSON

variabile discreta che conta il numero di h successi in prove ripetute, quando il numero n di prove è grande e la probabilità p di successo è bassa. il parametro $\lambda$ rappresenta il numero medio di eventi attesi in un intervallo di tempo

$$
P(\lambda):P\{X = h\} = e^{-\lambda}*\frac{\lambda^h}{h!},\lambda > 0, h \in \mathbb{N}
$$

in altre parole calcola la probabilità che un evento si verifichi un numero h di volte in un certo intervallo di tempo
### BERNOULLI

variabile discreta che descrive la probabilità di successo o insuccesso in una singola prova di un esperimento.

B(p) -> p  = probabilità di successo (0 < p < 1)

1-p = prob. di insucesso

Valore atteso = p = $E[X^k] = p$ con $k \ge 1$
varianza = p*(1-p) = $VAR(X)=p-p^2=p*(1-p)$
### VA INTERVALLI E DOPPIE:
![[Pasted image 20241214185920.png]]

![[Pasted image 20241214190024.png]]

![[Pasted image 20241214190448.png]]

![[Pasted image 20241214190853.png]]

![[Pasted image 20241214190920.png]]

disuguaglianza di Markov = stima della probabilità che una v.a X (a valori +) superi una certa soglia a >0 : 
$$
a*P\{X \ge a\} \le E[X]
$$

![[Pasted image 20241214191141.png]]

![[Pasted image 20241214192919.png]]

![[Pasted image 20241214193222.png]]

![[Pasted image 20241214193517.png]]

![[Pasted image 20241214193913.png]]

covarianza tra v.a:
$Cov(X,Y) = E[(X-E[X])*(Y-E[Y])] = E[XY] - E[X]*E[Y]$

![[Pasted image 20241214194917.png]]

