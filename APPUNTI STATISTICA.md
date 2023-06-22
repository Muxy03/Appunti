statistica descrittiva quando i dati vengono analizzati, seppur con tecniche anche raffinate, senza fare assunzioni esterne all'insieme di dati considerati.

L’inferenza statistica invece studia i dati utilizzando un modello probabilistico, cioè suppone che i dati siano valori assunti da variabili aleatorie aventi una certa distribuzione di probabilità dipendente da dei parametri non noti.

**popolazione** -> l’insieme di oggetti o fenomeni che si vuole studiare, su ognuno dei quali è possibile effettuare la stessa misura, ovvero considerarne un carattere. 

Un campione statistico (statistical sample) -> un sottoinsieme della popolazione scelto per rappresentarla.

Un carattere **quantitativo** -> una quantità numerica, ovvero gli esiti della misura sono numeri paragonabili tra loro

Un carattere **qualitativo** -> produce misure che non possiamo paragonare tra loro in modo significativo con dei numeri

carattere **discreto** -> carattere può assumere una quantità finita e relativamente piccola di valori (qualitativi o quantitativi);

diagramma a barre -> che consiste in una serie di barre verticali, ciascuna delle quali ha altezza pari (o proporzionale) alla frequenza relativa di un possibile esito della misura. Un altro modo di rappresentare questi dati è il diagramma a torta (piechart).

carattere **continuo** -> carattere che può assumere un qualunque valore positivo. 

![][IMMAGINI/ISTOGRAMMA.png]

$$x = (x_1,\dots,x_n) \in R^n$$
$$\overline{x} = \frac{1}{n}* \sum_{i=1}^{n} x_i$$
La mediana -> è il dato $x_i$ tale che metà degli altri valori è minore o uguale a $x_i$ e l’altra metà maggiore o uguale (nel caso n sia pari si può prendere la media aritmetica dei due valori centrali in questo senso).

varianza campionaria -> $var(x) = \frac{1}{n-1} \sum_{i=1}^{n}(x_i-\overline{x})^2$

varianza empirica -> $var_e(x) = \frac{1}{n} \sum_{i=1}^{n}(x_i-\overline{x})^2$

deviazione standard/empirica ->$\sigma(x) = \sqrt{var(x)}$  / $\sigma_e(x) = \sqrt{var_e(x)}$

la varianza ( $\sigma^2(x)$ ) è uguale a 0 <=> i dati sono tutti uguali

> campione di dati x e numero positivo d:
>$$\frac{\#\{x_i:|x_i-\overline{x}|>d\}}{n} \le \frac{var_e(x)}{d^2}$$
>Dimostrazione: (passo finale dividere entrambe le parti per n)
>$$\sum_{i=1}^{n}(x_i - \overline{x})^2 \ge \sum_{i:|x_i-\overline{x}|>d}^{n}(x_i - \overline{x})^2 \ge \sum_{i:|x_i-\overline{x}|>d}^{n}d^2 = \#\{x_i:|x_i-\overline{x}|>d\}\le \frac{\sum_{i=1}^{n}(x_i-\overline{x})^2}{d^2}$$

sample skewness (misura campionaria di asimmetria) -> $b=\frac{1}{\sigma^3}*\frac{1}{n}*\sum_{i=1}^{n}(x_i-\overline{x})^3$

>ecdf : funzione di ripartizione empirica -> restituisce la frequenza relativa dei dati minori uguali a t 
>$x=(x_1,\dots,x_n)\in R^n$
>$$F_e(t)=\frac{\#\{x_i|x_i \le t\}}{n}$$

![[K-PERCENTILE.png]]

![[Pasted image 20230416174111.png]]

![[Pasted image 20230416173822.png]]

![[Pasted image 20230416174007.png]]

considerando n coppie di numeri $(x,y)=((x_1,y_1),\dots,(x_n,y_n)) \in R^{2 \times n}$, $\overline{x}$ e $\overline{y}$ corrispondono alle medie campionarie di x e y

covarianza campionaria/empirica -> $cov(x)=\sum_{i=1}^{n}\frac{(x_i-\overline{x})*(y_i-\overline{y})}{n-1}$ / $cov_e(x)=\sum_{i=1}^{n}\frac{(x_i-\overline{x})*(y_i-\overline{y})}{n}$

coefficiente di correlazione tra x e y -> $r(x,y)=\frac{cov(x,y)}{\sigma(x)*\sigma(y)}$ $,\sigma(x) \neq 0$ e $\sigma(y) \neq 0,$$|r(x,y)|\le 1$

![[Pasted image 20230416175137.png]]

r(x,y) misura il legame di natura lineare tra i dati x e y -> quantifichiamo mediante la retta di regressione

![[Pasted image 20230416175910.png]]

$\Omega$ = spazio di probabilità (insieme astratto degli esiti possibili) -> i suoi sottoinsiemi si chiamano eventi -> evento elementare = $\omega \in \Omega$ oppure $\{\omega\}$

![[Pasted image 20230416180645.png]]![[Pasted image 20230416180709.png]]

la definizione di $\sigma$-algebra permette di eseguire operazioni insiemistiche anche se $\Omega$ è inifinito 

![[Pasted image 20230416181031.png]]

per specializzare la $\sigma$-addittività al caso finito basta porre $A_n=\emptyset$ per un certo n in poi

![[Pasted image 20230416181616.png]]

![[Pasted image 20230416181659.png]]

una distribuzione di probabilità $\pmb{P}$ si dice uniforme su $\Omega$:
- se $\Omega$ è finito
- se $F=P(\Omega)$ , l'insieme famiglia di sotto-insiemi di $\Omega$ corrisponde all'insieme delle parti di $\Omega$
- gli eventi elementari $\omega_i$ sono equiprobabili

per $\pmb{P}$ uniforme e $\Omega$ finito -> $\pmb{P}(A)= \frac{\#A}{\#\Omega},A \subseteq \Omega$
(#A = casi favorevoli = cardinalità di A ,#Ω = casi possibili = cardinalità di Ω)

il numero di sequenze ordinate, possibilmente con ripetizione, di k numeri da 1 a n, cioè il numero di funzioni da {1,..., k} a {1,...,n} è $n^k$

il numero di modi in cui si possono ordinare gli elementi di {1,...,n} (ovvero il numero di funzioni biiettive dall’insieme a se stesso, o di permutazioni di n elementi) è $n!$

se 0 ≤ k ≤ n, il numero di sottinsiemi di {1,...,n} formati da k elementi (coefficiente binomiale) è $\binom{n}{k}=\frac{n!}{k!*(n-k)!}=\frac{n*(n-1)*\dots*(n-k+1)}{k!}$

formula del binomio di Newton -> $(a+b)^n=\sum_{k=0}^{n}\binom{n}{k}*a^k*b^{n-k}$

![[Pasted image 20230416183213.png]]

![[Pasted image 20230416183301.png]]

![[Pasted image 20230416183445.png]]

![[Pasted image 20230416183630.png]]

![[Pasted image 20230416183657.png]]
$^3$ = per n eventi le eguaglianze da verificare sono $2^n-n-1$

Probabilità discreta -> probabilità sullo spazio $\Omega = R$ con la $\sigma$-algebra  $F=P(R)$ che sia contentrata su una successione (finita o numerabile) di punti $x_1,x_2,\dots \in R^4$. Posto $p_i=p(x_i)=\pmb{P}(x_i)$, vale
$$
\pmb{P}(A)=\sum_{i:x_i \in A}p(x_i), \forall A \subseteq R
$$
densità concreta della probabilità discreta $\pmb{P}$ la funzione $p(x_i)=\pmb{P}(x_i)$ 

![[Pasted image 20230424183800.png]]

![[Pasted image 20230424184219.png]]

![[Pasted image 20230424184409.png]]

![[Pasted image 20230424184518.png]]

una variabile aleatoria è detta discreta se la sua immagine $X(\Omega) \subset R$ è un sottoinsieme al più numerabile di R, o equivalentemente se la sua legge di probabilità è discreta

![[Pasted image 20230424185510.png]]

Funzione di ripartizione della v.a X -> $F_X:R \rightarrow [0,1],F_X=\pmb{P}\{X \le x\}$ 

![[Pasted image 20230424190225.png]]

$\pmb{P}\{a<X\le b\}=F(b)-F(a)$ 

Assegnata una v.a. X ed un numero $\beta$ con $0<\beta<1$, si chiama $\beta$-quantile un numero r tale che si abbia $\pmb{P}(X\le r)\ge \beta$ e $\pmb{P}(X \ge r)\ge 1-\beta$ 

Variabili aleatorie notevoli:
- Variabili binomiali:
	- $X:\Omega \rightarrow \{1,\dots,n\}$
	- $p \in (0,1)$
	- $\pmb{P}(X=h)=\binom{h}{n} *p^h*(1-p)^{n-h},0\le h \le n$ 
	- $B(n,p)$ -> per n=1 la v.a è detta di Bernoulli
- Variabili geometriche:
	- $\pmb{P}(X=h)=(1-p)^{h-1}*p,h \in N_0$ 
	- assenza di memoria
- Variabile di Poisson:
	- $\lambda>0,X:\Omega \rightarrow N$ valori naturali
	- $\pmb{P}(X=h)=e^{-\lambda}*\frac{\lambda^{h}}{h!},h \in N$ 
- Variabili uniformi su intervalli:
	- Dati due numeri reali a < b, la densità uniforme sull’intervallo \[a,b\] è costante sull’intervallo e nulla fuori da esso
	- ![[Pasted image 20230510165303.png]]
- Variabili Esponenziali:
	- ![[Pasted image 20230510165414.png]]

![[Pasted image 20230510165654.png]]

## Variabili Gaussiane: 
N(0,1) -> densità di probabilità = $\phi(x)=\frac{1}{\sqrt{2\pi}}*e^{-t^2/2}$

funzione di ripartizione = $\Phi(x) = \frac{1}{\sqrt{2\pi}}*\int^x_{-\infty} e^{-t^2/2}dt$

$q_\alpha$ = $\alpha$-quantile della variabile N(0,1)

![[Pasted image 20230510171833.png]]

Valore Atteso = $E[X] = \sum_i x_i*p(x_i)$ -> p = funzione di massa, X = variabile discreta -> $\sum_i |x_i|*p(x_i) < +\infty$ condizione per cui X ha valore atteso

Valore Atteso = $E[X] = \int_{-\infty}^\infty x*f(x) dx$ -> f = densità, X= variabile con densità f -> $\int_{-\infty}^\infty |x|*f(x) dx < +\infty$ condizione per cui X ha valore atteso

![[Pasted image 20230510172512.png]]

![[Pasted image 20230510172556.png]]

$1 \le m < n:$ se $E[|X|^n]<+\infty$ anche $E[|X|^m]<+\infty$ 

se X è una variabile aleatoria (discreta o con densità) a valori positivi e a >0 :
$a*\pmb{P}\{X \ge a\} \le E[X]$ 

Varianza di una variabile aleatoria = $Var(X)=E[(X-E[X])^2]=E[X^2]-E[X]^2$ 

deviazione standard di una variabile aleatoria = $\sigma(X)=\sqrt{Var(X)}$ 

$Var(aX+b)=a^2*Var(X)$ 

>se X è una variabile aleatoria e d>0 vale 
>$$\pmb{P}\{|X-E[X]|>d\} \le \frac{Var(X)}{d^2}$$

![[Pasted image 20230510174036.png]]

![[Pasted image 20230510174234.png]]


## Variabili Aleatorie Doppie

![[Pasted image 20230510174608.png]]

![[Pasted image 20230510174629.png]]

![[Pasted image 20230510174848.png]]

![[Pasted image 20230510175026.png]]

![[Pasted image 20230510175225.png]]

![[Pasted image 20230510175451.png]]

![[Pasted image 20230510175634.png]]

![[Pasted image 20230510175701.png]]

![[Pasted image 20230510175719.png]]

![[Pasted image 20230510175746.png]]

![[Pasted image 20230510175808.png]]

![[Pasted image 20230510175837.png]]

![[Pasted image 20230510175909.png]]

![[Pasted image 20230510175956.png]]

![[Pasted image 20230510180036.png]]

![[Pasted image 20230510181759.png]]

![[Pasted image 20230510181816.png]]

![[Pasted image 20230510181858.png]]

![[Pasted image 20230510181939.png]]

![[Pasted image 20230510182006.png]]

![[Pasted image 20230510182035.png]]

![[Pasted image 20230510182115.png]]

![[Pasted image 20230510182140.png]]

![[Pasted image 20230510182334.png]]

![[Pasted image 20230510182422.png]]

![[Pasted image 20230510182448.png]]

![[Pasted image 20230510182507.png]]

>Data $F=F_X$ c.d.f. di una variabile aleatoria X, una famiglia finita $X_1,\dots,X_n$ di variabili aleatorie i.i.d. con legge data dalla c.d.f. si dice _campione statistico_ o _campione aleatorio_ della v.a. X di numerosità (o _taglia_) n.

![[Pasted image 20230531114830.png]]

![[Pasted image 20230531114958.png]]

![[Pasted image 20230531115038.png]]

![[Pasted image 20230531115047.png]]

![[Pasted image 20230531115103.png]]

![[Pasted image 20230531115147.png]]

![[Pasted image 20230531120637.png]]

>Siano $X_1,\dots,X_n$ un campione Gaussiano $N(m,\sigma^2)$ e poniamo come sopra:
>$$
 \overline{X}_n = \frac{1}{n}*\sum^n_{i=1} X_i
$$
>$$
 S^2_n = \frac{1}{n-1}*\sum^n_{i=1}(X_i - \overline{X}_n)^2
$$
>Valgono i seguenti risultati:
>1. le variabili $\overline{X}_n$ e $S^2_n$ sono indipendenti;
>2. la variabile $\overline{X}$ ha densità $N(m,\sigma^2/n);$ 
>3. la variabile $\frac{n-1}{\sigma^2}*S^2_n$ ha densità $\chi^2(n-1);$
>4. la variabile $T=\sqrt{n}*\frac{(\overline{X}_n -m)}{S}$ ha densità di Student T(n-1);

![[Pasted image 20230531172406.png]]

![[Pasted image 20230531172443.png]]

![[Pasted image 20230531172506.png]]

![[Pasted image 20230531172601.png]]

![[Pasted image 20230531172621.png]]

![[Pasted image 20230531172638.png]]

![[Pasted image 20230531172706.png]]

![[Pasted image 20230531172715.png]]

![[Pasted image 20230531172752.png]]

![[Pasted image 20230531172811.png]]

![[Pasted image 20230531172822.png]]

![[Pasted image 20230531172841.png]]

![[Pasted image 20230531172905.png]]

![[Pasted image 20230531172916.png]]

![[Pasted image 20230531172933.png]]

![[Pasted image 20230531173004.png]]

![[Pasted image 20230531173023.png]]

![[Pasted image 20230531173035.png]]

![[Pasted image 20230531173241.png]]

![[Pasted image 20230531173300.png]]

![[Pasted image 20230531173340.png]]

![[Pasted image 20230531173518.png]]

![[Pasted image 20230531173651.png]]

![[Pasted image 20230531173713.png]]

![[Pasted image 20230531173735.png]]

![[Pasted image 20230531173742.png]]

![[Pasted image 20230531173758.png]]

