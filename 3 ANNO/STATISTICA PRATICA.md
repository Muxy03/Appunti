
$\def\over{\overline}$
$\def\R{\mathbb{R}}$
# TEORIA:

- retta di regressione quantifica la presenza di una relazione lineare tra x e y
- si parla di probabilità discreta quando ci sono un numero finito o numerabile di esiti possibili
- probabilità uniforme = probabilità discreta + stessa probabilità per ogni esito possibile
- probabilità condizionata indica la probabilità che si verifichi A dopo che si è verificato B
- sistema di alternative = partizione dei possibili esiti 
- formula di fattorizzazione  = P(A) come somma delle probabilità condizionate di A rispetto a un sistema di alternative
- due eventi disgiunti sono indipendenti solo se almeno uno dei 2 è trascurabile (P(\*) = 0)
- densità di probabilità $f:\R \rightarrow [0,+\infty)$:
	- non negativa
	- continua
	- $\int_{- \infty}^{+ \infty}{f(x) dx} = 1$
- 2 variabili aleatorie sono equi-distribuite se hanno la stessa legge di probabilità
- una variabile aleatoria è discreta o con densità se la sua legge di probabilità è discreta o definita da una densità di probabilità
- cdf = funzione di ripartizione $F_X:\R \rightarrow [0,1]$:
	- non decrescente = $x<y \implies F_X(x) \le F_X(y)$
	- $\lim_{x \rightarrow - \infty}{F_X(x) = 0}$
	- $\lim_{x \rightarrow + \infty}{F_X(x) = 1}$
	- continua a destra
- una variabile aleatoria Binomiale è discreta e conta il numero di successi in n prove indipendenti con solo 2 esiti possibili
- una variabile aleatoria Geometrica è discreta e conta il numero di prove, indipendenti e con pari probabilità di successo, necessarie per ottenere il primo successo
	- assenza di memoria = la probabilità di ottenere il primo successo in un certo numero di prove non dipende da quante prove senza successo siano già state fatte
- una variabile aleatoria Poisson è discreta e conta il numero di h successi in prove ripetute con n grande e p bassa.
	- $\lambda$ rappresenta il numero medio di eventi attesi in un intervallo di tempo
	- quando n è abbastanza grande (n ≥ 50) e p è abbastanza piccolo (p < 0.1), allora la distribuzione di Poisson è una buona approssimazione della distribuzione binomiale, dove $\lambda = np$
- variabili uniformi su intervalli sono una v.a. con densità in cui ogni valore all'interno dell’intervallo specifico ha la stessa probabilità di realizzarsi
- Le variabili esponenziali sono una v.a. con densità che descrivono il tempo di attesa tra due eventi aleatori
	-  $\lambda$ rappresenta il numero medio di eventi attesi in un intervallo di tempo
- Le v.a. gaussiane sono funzioni con una forma a campana che vengono utilizzate come approssimazione per altre distribuzioni di probabilità, facendo uso del teorema del limite centrale
- la variabile aleatoria gaussiana standard caso particolare delle variabili aleatorie gaussiane con media = 0 e varianza = 1
- per usare la formula del cambio di variabile:
	- $h:A \rightarrow B$ biunivoca, differenziabile e con inversa differenziabile
	- X deve avere la sua densità supportata su un intervallo A aperto (nulla in $A^c$)
- il valore atteso rappresenta il valore medio "atteso" di una variabile aleatoria X. è la media campionaria di una v.a (centro della distribuzione di probabilità di X)
- ![[Pasted image 20241216234142.png]]
- due variabili aleatorie equi-distribuite hanno stesso valore atteso
- ![[Pasted image 20241216234338.png]]
- Disuguaglianza di Markov => se il valore atteso è basso, la probabilità che la variabile assuma valori molto grandi (rispetto al valore atteso) deve essere piccola.
- Disuguaglianza di Chebyshev => se la varianza è piccola, la probabilità di grandi deviazioni dal valore atteso è bassa.
- Funzioni di più variabili indipendenti sono indipendenti se la stessa variabile non compare in due funzioni diverse
- ![[Pasted image 20241216235533.png]]
- X,Y v.a indipendenti B(n,p) e B(m,p) rispettivamente => X + Y è B(n+m,p)
- X,Y v.a indipendenti $N(m_1,\sigma_1)$ e $N(m_2,\sigma_2)$ rispettivamente => X + Y è $N(m_1+m_2,\sigma_1^2+\sigma_2^2)$
- ![[Pasted image 20241216235847.png]]
- La covarianza tra v.a. quantifica il grado di relazione lineare tra due v.a. 𝑋 e 𝑌, ovvero indica come tendono a variare congiuntamente rispetto alle loro medie
- Il coefficiente di correlazione misura la presenza di una relazione lineare tra 𝑋 e 𝑌 (non misura l'indipendenza)
- $Cov(X,Y) = 0 = \rho(X,Y)$ => X e Y sono scorrelate
- iid = le v.a sono indipendenti ed equi-distribuite
- ![[Pasted image 20241217001011.png]]
- Per la legge dei grandi numeri, il comportamento di una v.a. per 𝑛 grande corrisponde alla varianza campionaria degli esiti delle variabile aleatoria $X_i$
- ![[Pasted image 20241217001511.png]]
- la gamma di Eulero per r intero è uguale a (r-1)!
- La densità esponenziale di parametro 𝜆 corrisponde alla densità $\Gamma(r,\lambda)$
- X,Y indipendenti $\Gamma(r,\lambda)$ e $\Gamma(s,\lambda)$ rispettivamente => $\Gamma(r+s,\lambda)$
- X,Y indipendenti $\chi^2(n)$  e $\chi^2(m)$ rispettivamente => $\chi^2(n+m)$
-  approssimazioni per $\chi^2(n),n \ge 80$:
	- per la legge dei grandi numeri $C_n=(X_1^2+\dots+X_n^2)$ converge in probabilità a 1
	- per il teorema del limite centrale $\frac{C_n-n}{sqrt{2n}}$ converge in distribuzione a N(0,1).
- una variabile aleatoria di Student ha momenti fino all'ordine (n-1) e quelli di ordine dispari se esistono sono nulli
- ![[Pasted image 20241217014705.png]]
- ![[Pasted image 20241217014737.png]]
- campione statistico = famiglia di $X_1,\dots,X_n$ variabili aleatorie iid con la stessa cdf
- ![[Pasted image 20241217014928.png]]
- statistica campionaria = $g(X_1,\dots,X_n)$
- stimatore di un parametro $\theta$  della distribuzione = statistica che approssima il valore di $\theta$
- uno stimatore è corretto se la media di tutte le stime calcolate con lo stimatore, su tutti i campioni di una statistica campionaria, è uguale al parametro della popolazione
- ![[Pasted image 20241217015447.png]]
- Correzione di Bessel => nella varianza campionaria si divide per n-1 per ottenere $S^2_n=\sigma^2$
- uno stimatore è consistente se all'aumentare della numerosità campionaria n tende a $\theta$ ovvero se l'errore standard dello stimatore tende a zero
- secondo la legge dei grandi numeri la media e la varianza campionarie sono stimatori consistenti rispettivamente del valore atteso e della varianza
- ![[Pasted image 20241217015951.png]]
- La funzione di verosimiglianza indica quanto è probabile osservare il campione dato se il parametro assume un valore. Maggiore è il valore della verosimiglianza, più plausibile è il valore del parametro
- ![[Pasted image 20241217020438.png]]
- la funzione di verosimiglianza non è altro che la funzione di massa o la densità congiunta delle variabili aleatorie $X_1,\dots,X_n$
- La stima di massima verosimiglianza è un metodo per stimare il parametro 𝜃 scegliendo il valore che massimizza la funzione di verosimiglianza.
- la stima di massima verosimiglianza sceglie un parametro 𝜃̂ che massimizza la probabilità (o la densità) dell’esito $𝑥_1, … , 𝑥_𝑛$ effettivamente ottenuto
- ![[Pasted image 20241217021900.png]]
- il livello di fiducia $1-\alpha$ indica la probabilità, decisa a priori, che la procedura identifichi un intervallo di possibili valori per il parametro $\theta$
- ![[Pasted image 20241217024258.png]]
- un intervallo di fiducia è un intervallo i cui estremi sono calcolati a partire dai valori assunti da v.a $X_1,\dots,X_n$ ed è utilizzato per stimare il parametro $\theta$ della popolazione
- $X_1,\dots,X_n$ campione statistico N(m,$\sigma^2$) implica che la precisione della stima d > 0 è la semi-ampiezza dell'intervallo:
	- cresce al crescere del livello di fiducia 1-$\alpha$
	- cresce al crescere di $\sigma^2$
	- decresce al crescere di n
- ![[Pasted image 20241217025923.png]]
- ![[Pasted image 20241217030157.png]]
- ![[Pasted image 20241217032745.png]]
- ![[Pasted image 20241217032939.png]]
- ![[Pasted image 20241217032952.png]]
- rifiutare l'ipotesi nulla => che i dati forniscono un’evidenza contro l’ipotesi nulla
- accettare l'ipotesi nulla =>  che i dati non forniscono evidenza contro l’ipotesi nulla
- ![[Pasted image 20241217033355.png]]
- errore di prima specie = falso positivo
- errore di seconda specie = falso negativo
- livello $\alpha$ di un test = limite superiore alla probabilità di commettere errori di 1 specie
- potenza di un test = probabilità di non commettere errori di 2 specie
- livello e potenza di un test sono inversamente proporzionali
- ![[Pasted image 20241217033916.png]]
- Z-test = test statistico verifica ipotesi sulla media m di un campione gaussiano $N(m,\sigma^2)$ con varianza nota
	- ![[Pasted image 20241217034504.png]]
- T-test = test statistico verifica ipotesi sulla media m di un campione gaussiano $N(m,\sigma^2)$ con varianza non nota
- ![[Pasted image 20241217035655.png]]
- ![[Pasted image 20241217040131.png]]
- L’effettivo empirico è la v.a. che indica il numero di osservazioni $X_i$ che hanno valore j
- L’effettivo teorico indica, dato il numero totale di osservazioni nel campo, il numero atteso di osservazioni in ciascuna categoria della distribuzione teorica
- ![[Pasted image 20241217041040.png]]
- ![[Pasted image 20241217041502.png]]
- 
# FORMULARIO:

- media campionaria = $\over{x} = \frac{1}{n}*\sum_{i=1}^n x_i$
- varianza campionaria (misura la dispersione dei dati intorno a $\over{x}$) = $var(x) = \sigma^2(x) = \frac{1}{n-1}*\sum_{i=1}^n(x_i - \over{x})^2$
- deviazione standard = $\sigma(x) = \sqrt{var(x)}$ 
- covarianza campionaria (misura quanto 2 variabili varino insieme) = $cov(x,y) = \frac{1}{n-1}*\sum_{i=1}^n (x_i - \over{x})(y_i- \over{y})$
- coefficiente di correlazione (misura la presenza di una correlazione lineare) = $r(x,y)=\frac{cov(x,y)}{\sigma(x)\sigma(y)}$
	- r(x,y) = 0 => no correlazione
	- r(x,y) = -1 => max discordanza
	- r(x,y) = 1 => max concordanza
	- $-1 \le r(x,y) \le 0$ => buona discordanza
	- $0 \le r(x,y) \le 1$ => buona concordanza
- probabilità discreta = $P(A) = \sum_{w_i \in A}P(w_i)$
- permutazione (tutti gli elementi sono presenti in tutti i gruppi) = $n!$
- Disposizione (gli elementi sono raggruppati k alla volta e l'ordine conta):
	- con ripetizioni = $n^k$
	- senza ripetizioni = $\frac{n!}{(n-k)!}$
- combinazione (gli elementi sono raggruppati k alla volta ma l'ordine non conta) = $\binom{n}{k} = \frac{n!}{k! * (n-k)!}$
- probabilità condizionata = $P(A|B) = \frac{P(A \cap B)}{P(B)}$
- condizionamento ripetuto = $P(A_1 \cap \dots \cap A_n) = P(A_1)*P(A_2|A_1)*\dots*P(A_n|A_1 \cap \dots \cap A_{n-1})$
- formula di fattorizzazione = $P(A) = \sum_{i=1}^n P(A|B_i)*P(B_i)$
- Bayes:
	- $P(B|A) = \frac{P(A|B)*P(B)}{P(A)}$
	- $P(B_i|A) = \frac{P(A|B_i)*P(B_i)}{\sum_{j=1}^n P(A|B_j)P(B_j)}$
- A e B sono indipendenti se $P(A \cap B) = P(A)*P(B)$
- densità uniforme su \[0,1\] = $f(x) = 1$ per $0 \le x \le 1$ else $f(x) = 0$
- v.a discreta = $P_X(A) = \sum_{x_i \in A}{P_X(x_i)}$
- v.a con densità = $P_X(A) = \int_A {f(x)dx}$
- cdf = $F_X(x) = P\{X \le x\}$
- $P(a < X \le b) = F_X(b) - F_X(a)$
- cdf discreta = $F_X(t) = \sum_{x_i \le t}{P_X(x_i)}$
- cdf con densità = $F_X(x) = \int_{-\infty}^x{f(t)dt}$
- densità di una v.a con densità = $f(x) = \frac{dF_X(x)}{dx}$
- variabili aleatorie discrete:
	- v.a Binomiale = $B(n,p):P\{X=h\}=\binom{n}{h}*p^h*(1-p)^{n-h}$
	- v.a Geometrica = $G(p):P\{X = h\} = (1 - p)^{h-1}*p$
	- v.a Poisson =  $P(\lambda):P\{X = h\} = e^{-\lambda} * \frac{\lambda^h}{h!}$
- variabili aleatorie con densità:
	- v.a uniformi su intervalli finiti \[a,b\] = $f(t) = \frac{1}{b-a}$ per $a < t <b$ else $f(t) = 0$
		- cdf = $F(t) = \frac{t}{b-a}$ per $0 < t \le b$ , $F(t) = 0$ per $t \le a$ , $F(t) = 1$ per t > b
	- v.a esponenziali = $f(t) = \lambda*e^{-\lambda*t}$  per t > 0 , $f(t) = 0$ per $t \le 0$
		- cdf = $F(t) = 1-e^{-\lambda*t}$ per t > 0, $F(t) = 0$ per $t \le 0$
	- v.a gaussiane = $N(m,\sigma^2):f(t) = \frac{1}{\sqrt{2\pi}*\sigma} * e^{-\frac{(t-m)^2}{\sigma^2}}$
		- guassiana standard $N(0,1)$:
			- densità = $\phi(x) = f(t)$ con m = 0 e $\sigma$ = 1
			- cdf = $\Phi(x) = \frac{1}{\sqrt{2\pi}}*\int_{-\infty}^x{e^{-\frac{t^2}{2}}dt}$
			- $\phi(x)$ è pari => $\Phi(-x) = 1 - \Phi(x)$ e $q_{1-\alpha} = -q_\alpha$
			- $P\{-t \le X \le t\} = 2\Phi(t) - 1$
		- cdf generale = $F(t) = \Phi(\frac{t-m}{\sigma})$
- cambio variabile = $f_Y(y)=f_X(h^{-1}(y))*|\frac{d h^{-1}(y)}{dy}|$ per $y \in B$ , $f_Y(y) = 0$ per $y \notin B$
- valore atteso v.a discreta = $E[X] = \sum_i {x_i*P_X(x_i)}$
- valore atteso v.a con densità = $E[X] = \int_{- \infty}^{+ \infty} {t*f(t)dt}$
- valore atteso nuova v.a discreta = $E[g(X)] = \sum_i {g(x_i)*P_X(x_i)}$
- valore atteso v.a con densità = $E[X] = \int_{- \infty}^{+ \infty} {g(t)*f(t)dt}$
- varianza v.a = $Var(X) = E[X^2]-E[X]^2$
- deviazione standard = $\sigma(X) = \sqrt{Var(X)}$
- momenti notevoli:
	- B(n,p): $E[X] = np,Var(X)=np*(1-p)$
	- P($\lambda$): $E[X]=\lambda,E[X^2]=\frac{a^2+ab+b^2}{3},Var(X)=\frac{(b-a)^2}{12}$
	- v.a esponenziali: $E[X^n] = \frac{n!}{\lambda^n},Var(X) = \frac{1}{\lambda^2}$
	- v.a gaussiane: $E[X]=m,E[X^2]=\sigma^2,Var(X)=\sigma^2$
- v.a indipendenti = $P(X \in A, Y \in B) = P(X \in A)*P(Y \in B)$
- funzione di massa Z=X+Y (X e Y indipendenti discrete) = $p_Z(n) = \sum_{h=0}^n{p_X(h)*p_Y(n-h)}$
- funzione della convoluzione Z=X+Y (X e Y indipendenti con densità) = $f_Z(z)=\int_{- \infty}^{+ \infty}f_Y(y)*f_X(z-y)dy$
- valore atteso prodotto di v.a (X e Y hanno valore atteso e sono indipendenti) = $E[XY] = E[X]*E[Y]$
- ![[Pasted image 20241217000420.png]]
- covarianza tra v.a = $Cov(X,Y) = E[XY]-E[X]E[Y]$
- coefficiente di correlazione = $\rho(X,Y) = \frac{Cov(X,Y)}{\sigma(X)\sigma(Y)}$
- media campionaria v.a = $\over{X}_n = \frac{X_1 + \dots + X_n}{n}$
- ![[Pasted image 20241217001123.png]]
- varianza campionaria v.a = $S^2_n = \frac{1}{n-1} * \sum_{i=1}^n{(X_i-\over{X}_n)^2}$
- gamma di Eulero = $\Gamma(r) = \int_0^{+ \infty}{x^{r-1}*e^{-x}dx}$
	- densità = $\Gamma(r,\lambda) = f(x) = \frac{1}{\Gamma(r)} * \lambda^r*x^{r-1}*e^{-\lambda*x}$ per x > 0, $f(x) = 0$ per $x \le 0$
	- momento densità Gamma = $E[X^\beta]=\frac{\Gamma(r+\beta)}{\Gamma(r)*\lambda^\beta}$
	- momento primo = $E[X] = \frac{r}{\lambda}, E[X^2]=\frac{(r+1)*r}{\lambda^2}$
	- momento secondo = $Var(X) = \frac{r}{\lambda^2}$
- v.a Chi-Quadro = $(X_1^2+\dots+X_n^2)$:
	- densità = $\chi^2(n) = \Gamma(\frac{n}{2},\frac{1}{2})$
	- momento primo = $E[X] = n,E[X^2] = n^2+2n$
	- momento secondo = $Var(X) = 2n$
- v.a Student (X e $C_n$ indipendenti N(0,1) e $\chi^2(n)$) = $T_n = \sqrt(n)*\frac{X}{\sqrt(C_n)}$ :
	- densità = $f_{T_n}(t) = \frac{\Gamma(\frac{n+1}{2})}{\sqrt{n\pi}*\Gamma(\frac{n}{2})} * (1+ \frac{t^2}{n})^{-\frac{n}{2}-\frac{1}{2}}$
	- la densità è una funzione pari => $F_n(-x) = 1- F_n(x)$ e $\tau_{(\alpha,n)} = -\tau_{(1-\alpha),n}$
- funzione di verasimiglianza $L:\Theta \times \R^n \rightarrow [0,1]$:
	- caso discreto = $L(\theta;x_1,\dots,x_n)=\prod_{i=1}^n{p_\theta(x_i)}$
	- caso con densità = $L(\theta;x_1,\dots,x_n)=\prod_{i=1}^n{f_\theta(x_i)}$
- stima di massima verosimiglianza: $L(\theta';x_1,\dots,x_n)=\max_{\theta \in \Theta}{L(\theta;x_1,\dots,x_2)}$
- stima col metodo dei momenti: $E_{\tilde{\theta}}[X^k] = \frac{1}{n} * \sum_{i=1}^n{x_i^k}$
- intervallo di fiducia per la media varianza nota = $[\over{X}_n \pm \frac{\sigma}{\sqrt n} * q_{1-\frac{\alpha}{2}}]$
- intervallo di fiducia per la media varianza non nota = $[\over{X}_n \pm \frac{S_n}{\sqrt n} * \tau_{1-\frac{\alpha}{2},n-1}]$
	- per $n \ge 60$ è possibile approssimare il quantile della v.a Student con quello della gaussiana standard
- intervalli di fiducia unilaterali per la media varianza nota:
	- sx: $(-\infty,\over{X}_n + \frac{\sigma}{\sqrt n}*q_{1-\alpha}]$
	- dx: $[\over{X}_n - \frac{\sigma}{\sqrt n}*q_{1-\alpha}, + \infty)$
- intervalli di fiducia unilaterali per la media varianza non nota:
	- sx: $(-\infty,\over{X}_n + \frac{S_n}{\sqrt n}*\tau_{1-\alpha,n-1}]$
	- dx: $[\over{X}_n - \frac{S_n}{\sqrt n}*\tau_{1-\alpha,n-1}, + \infty)$
- intervalli di fiducia per la varianza (varianza non nota):
	- sx: $(0,\frac{(n-1)*S^2_n}{\chi^2_{\alpha,n-1}}]$
	- dx: $[\frac{(n-1)*S^2_n}{\chi^2_{1-\alpha,n-1}},+ \infty)$
- intervallo di fiducia per la media p (Bernoulli) = $[\over{X}_n \pm \sqrt{\frac{\over{X}_n*(1-\over{X}_n)}{n}}*q_{1-\frac{\alpha}{2}}]$
- ![[Pasted image 20241217032842.png]]
- Z Test:
	- $H_0)m = m_0,H_1)m \neq m_0$
	- $H_0$ accettata al livello $\alpha$ <=> $m_0$ appartiene all'intervallo di fiducia per la media con livello di fiducia $1-\alpha$ 
	- $C = \{|\over{X}_n - m_0| > \frac{\sigma}{\sqrt n}*q_{1-\frac{\alpha}{2}}\}$
	- p-value = $\over{\alpha} = 2[1 - \Phi(\frac{\sqrt n}{\sigma}*|\over{X}_n - m_0|)]$
	- ![[Pasted image 20241217034709.png]]
- Z Test unilatero:
	- ![[Pasted image 20241217034810.png]]
- Z Test Bernoulli:
	- ![[Pasted image 20241217034918.png]]
- T Test:
	-  $H_0)m = m_0,H_1)m \neq m_0$
	- si rifiuta $H_0$ se $\sqrt{n}*\frac{|\over{X}_n-m_0|}{S} > \tau_{1-\frac{\alpha}{2},n-1}$
	- $C = \{\sqrt{n}*\frac{|\over{X}_n-m_0|}{S} > \tau_{1-\frac{\alpha}{2},n-1}\}$
	- p-value = $\over{\alpha} = 2[1 - F_{T_{n-1}}(\frac{\sqrt n}{s}*|\over{X}_n-m_0|)]$
- T Test unilatero:
	- ![[Pasted image 20241217035616.png]]
- ![[Pasted image 20241217035732.png]]
- ![[Pasted image 20241217035830.png]]
- Test CHI QUADRO:
	- ![[Pasted image 20241217040208.png]]
	- $C_\alpha = \{T_n > \chi^2_{r-1,1-\alpha}\}$
	- p-value = $\over{alpha} = 1 - G_{n-1}(\sum_{j=1}^r {\frac{(O_{n,j}-n*p_j)^2}{n*p_j}})$
- ![[Pasted image 20241217041010.png]]
- statistica di Pearson = $T_n = \sum_{i=1}^r{\frac{(O_{n,j}-n*p_j)^2}{n*p_j}}$
- effettivo empirico = $O_{n,j} = \#\{i: X_i = x_j\}$
- effettivo teorico del valore j = $n*p_j$
- 
---
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

