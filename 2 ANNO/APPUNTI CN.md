
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
- A invertibile
- J e GS sono applicabili
- J e GS sono convergenti
- ammette unica LU

A simmetrica implica:
- autovalori reali
- $K_1(A) = K_\infty(A)$ -> $||A||_1 = ||A||_\infty$ 
- $K_2(A) = \frac{\max |\lambda_i|}{\min |\lambda_i|}$ 
- nei cerchi di Gerschgorin gli autovalori stanno sul diametro

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
NUMERICO A.A. 2022-2023

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
