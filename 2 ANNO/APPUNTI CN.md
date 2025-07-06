
rappresentazione di $x \in \mathbb{R},x \neq 0$ in base B con $B \in \mathbb{N},B \gt 1$:
>![[Pasted image 20240224174836.png]]
>$d_1 \neq 0$ e $d_i$ non definitivamente uguale a $B-1$ garantiscono l'unicità della rappresentazione
>$x=0$ non ammette rappresentazione normalizzata (rappr. speciale)
>La rappresentazione floating point dei numeri reali si estende all’insieme dei numeri complessi z = a + ib rappresentati come coppie di numeri reali.

STANDARD IEEE 754-1985:
- segno | esponente | cifre rappresentazione 
- 32 BIT (1+8+23) -> singola precisione
- 64 BIT (1+11+52) -> doppia precisione

insieme dei numeri di macchina in rappresentazione floating point con t cifre, base B e range (−m, M ) l’insieme dei numeri reali:
>$\mathbb{F}(B,t,m,M)=\{0\} \cup \{x \in \mathbb{R}: x = sign(x)*B^p*\sum_{i=1}^t d_i*B^{-i},0 \le d_i \le B-1,d_1 \neq 0,-m \le p \le M\}$
>cardinalità = $2*B^{t-1}*(M+m+1)+1$
>![[Pasted image 20240224181441.png]]
>![[Pasted image 20240224183609.png]]

rappresentare un numero reale diverso da 0 in macchina significa approssimarlo con $\tilde{x} \in \mathbb{F}$:
- errore relativo -> $\epsilon_x = \frac{\tilde{x}-x}{x} = \frac{\eta_x}{x},x \neq 0$ -> valutazione qualitativa
- errore assoluto -> $\eta_x = \tilde{x}-x$ -> valutazione quantitativa
- tecniche di approssimazione per $\omega \le |x| \le \Omega:$
	-  round to the nearest (arrotondamento): il numero x viene approssimato con il numero rappresentabile $\tilde{x}$ più vicino;
	- round toward zero (troncamento): il numero x viene approssimato con il più grande numero rappresentabile $\tilde{x}$ il cui valore assoluto risulti minore od uguale al valore assoluto di x;
	- round toward plus infinity: il numero x viene approssimato al più piccolo numero rappresentabile maggiore del dato;
	- round toward minus infinity: il numero x viene approssimato al più piccolo numero rappresentabile minore del dato;
- $|\epsilon_x|=|\frac{trn(x)-x}{x}| \le u = B^{1-t}$ -> $trn(x)$ = il risultato dell’approssimazione di x con troncamento ($fl(x)$ = l’approssimazione in macchina del dato x nel sistema floating point considerato)
- u = precisione di macchina -> è indipendente dalla grandezza del numero e caratteristica dell’aritmetica floating point (insieme dei numeri rappresentabili e tecnica di approssimazione) implementata sulla macchina su cui stiamo operando
- $fl(x) = x(1+\epsilon_x),|\epsilon_x|\le u$
- ![[Pasted image 20240224191451.png]]
(calcolo funzione razionale):
- errore inerente -> $\epsilon_{in} = \frac{f(\tilde{x})-f(x)}{f(x)}$ -> per $f(x) \neq 0$ -> misura la sensibilità della funzione e del problema matematico -> indipendente dall'algoritmo -> $|\epsilon_{in}|$ qualitativamente molto elevato => problema mal condizionato
- errore algoritmico -> $\epsilon_{alg} = \frac{g(\tilde{x})-f(\tilde{x})}{f(\tilde{x})}$ -> g(x) è l'approssimazione in macchina di f(x) -> dipende dall'algoritmo -> $|\epsilon_{alg}|$ qualitativamente molto elevato => problema numericamente instabile
- errore totale -> $\epsilon_{tot} = \frac{g(\tilde{x})-f(x)}{f(x)} = \epsilon_{in}+\epsilon_{alg}$ -> rappresenta la differenza relativa tra l'output atteso e ottenuto
- $\epsilon_{in} \doteq \frac{f'(x)}{f(x)}*x*\epsilon_x = c_x*\epsilon_x$ -> $c_x$ è il coefficiente d'amplificazione del cond. del problema
- $|c_x| \le 1$ => problema ben condizionato
- ![[Pasted image 20240226162529.png]]

analisi in avanti -> +pessimistica ->[[all_together.pdf#page=14&selection=490,0,533,2|all_together, pagina 14]]
analisi all'indietro -> +realistica -> $g(\tilde{x}) \doteq f(\hat{x}) \implies \epsilon_{alg} = \frac{f(\hat{x})-f(\tilde{x})}{f(\hat{x})}$

studiare condizionamento:
- $f(x,y)=x^2+y^2$![[Pasted image 20240226175347.png]]

studiare stabilità:
- ![[Pasted image 20240226180213.png]]
- ![[Pasted image 20240303164257.png]]

$||A||_\infty =$ norma matriciale infinito -> $max \sum_{j=1}^n |a_{ij}|$  (righe)

$||A||_1 =$ norma matriciale 1 -> $max \sum_{i=1}^n |a_{ij}|$  (colonne)

$||A||_2 =$ norma matriciale 2 -> $\sqrt{\rho(A^T*A)}$ , dove $\rho(X)$  è il raggio spettrale

$\rho(X)=$ raggio spettrale -> $max |\lambda_i|$ (max autovalore, in valore assoluto, di X)

$K_i(A) =||A||_i *||A^{-1}||_i$  -> condizionamento (i = 1/2/infinito) -> +grande(bad), +piccolo(good)

>![[Pasted image 20230621162508.png]]
>il centro di un cerchio è i-esimo elemento della diagonale
>il raggio di un cerchio è la sommatoria degli elementi (in valore assoluto), escluso il centro, della riga i-esima

se tutte le sotto matrici di A, fino a n-1, sono invertibili allora esiste unica LU

$E_i = I_n - v^T*e^T_i$ -> matrice E elementare di gauss -> ex. per $E_1$ = prima colonna di L con 0 al posto di 1-> i indica il passo di riduzione

$A_1 = E_1*A_0$ 

>![[Pasted image 20230621164143.png]]
>L: gli elementi sotto la diagonale di L sono i valori per cui moltiplichi le righe
>U non è altro che la matrice ottenuta alla fine della riduzione


>![[Pasted image 20230621164359.png]]

il metodo (6.2) converge <=> $\rho(P)<1$

>![[Pasted image 20230621164831.png]]
>![[Pasted image 20230621164844.png]]

Jacobi:
- M = D
- N = L+U

Gauss-Seidel:
- M = D-L
- N = U

costo di una iterazione di J o GS = nnz(A)  operazioni moltiplicative= \# elementi non nulli di A

![[Pasted image 20230621165045.png]]

A pred. diagonale implica:
- A invertibile => ammette unica LU
- J e GS sono applicabili
- J e GS sono convergenti

A simmetrica implica:
- autovalori reali
- $K_1(A) = K_\infty(A)$ -> $||A||_1 = ||A||_\infty$ 
- $K_2(A) = \frac{\max |\lambda_i|}{\min |\lambda_i|}$ 
- nei cerchi di Gerschgorin gli autovalori stanno sul diametro

A quadrata è invertibile <-> $det(A) \neq 0$ <-> 0 non è autovalore di A

A\*v = a\*v <-> a è autovalore di A (v autovettore di a)

![[Pasted image 20230621170249.png]]

![[Pasted image 20230621170421.png]]

![[Pasted image 20230621170505.png]]

![[Pasted image 20230621170550.png]]

![[Pasted image 20230621170647.png]]

![[Pasted image 20230621170629.png]]

![[Pasted image 20230621170730.png]]

![[Pasted image 20230621170804.png]]

![[Pasted image 20230625224058.png]]

![[Pasted image 20230625224434.png]]

>$|J|_\infty = (\frac{n-1}{n})$
>![[Pasted image 20230625231733.png]]

[CN GIOELE](https://unipiit-my.sharepoint.com/personal/g_pasquini6_studenti_unipi_it/_layouts/15/Doc.aspx?sourcedoc={f8358618-7bc7-4d26-b847-b2e145594772}&action=view&wd=target%28Lezioni.one%7C057e2bc6-116c-4039-9b91-5ea68119576e%2F18.%20Lezione%20-%2029%5C%2F03%5C%2F2023%7C93bbe53b-5919-3540-a2a9-612d478c5afd%2F%29&wdorigin=NavigationUrl)

```txt
PROGRAMMA DI CALCOLO
NUMERICO A.A. 2023-2024

Luca Gemignani
Dipartimento di Informatica
Universita`di Pisa
email: luca.gemignani@unipi.it
url : http://pages.di.unipi.it/gemignani/


2 L'Aritmetica del Calcolatore
Lezione 2.1:Rappresentazione in Base e Numeri di Macchina.
Lezione 2.2:Aritmetica di Macchina (Teorema 2.2.1).


3 Analisi degli Errori
Lezione 3.1:Errori nel Calcolo di una Funzione Razionale (Teorema 3.3.1)
Lezione 3.2:Tecniche per l'Analisi degli Errori (senza analisi all'indietro).
Lezione 3.3:Cenni sul Calcolo di una Funzione non Razionale.


4 I Problemi dell'Algebra Lineare Numerica:Aspetti Computazionali e Condizionamento
Lezione 4.1:Norme Matriciali e Norme Vettoriali.
Lezione 4.2:Il Problema della Risoluzione di un Sistema Lineare ed il
suo Condizionamento. 
Lezione 4.4:Teoremi di Localizzazione per Autovalori (Teorema 4.4.1).

5 Metodi Diretti per la Risoluzione di Sistemi Lineari
Lezione 5.1:Sistemi Triangolari (Teorema 5.1.1)
Lezione 5.2:Matrici Elementari di Gauss ed il Metodo di Eliminazione
Gaussiana
Lezione 5.3:Il Metodo di Gauss per Matrici Invertibili: Tecniche di
Pivoting e Stabilita`.

6 Metodi Iterativi per la Risoluzione di Sistemi Lineari
Lezione 6.1:Generalita` sui Metodi Iterativi (Teorema 6.1.2, Teorema 6.1.3). 
Lezione 6.2:I Metodi di Jacobi e Gauss-Seidel. 
Lezione 6.3:Convergenza dei Metodi di Jacobi e Gauss-Seidel (Teorema 6.3.1).

10 Metodi Numerici per l'Approssimazione degli Zeri di una Funzione
Lezione 10.1: Il Metodo di Bisezione (Teorema 10.1.1 con dimostrazione semplificata sotto l'ipotesi  addizionale di unicita` della radice nell'intervallo considerato)
Lezione 10.2: Metodi di Iterazione Funzionale (Teorema 10.2.2, Teorema 10.2.3).
Lezione 10.3: Il Metodo delle Tangenti (Teorema 10.3.1)
```

