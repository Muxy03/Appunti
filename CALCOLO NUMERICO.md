
$||A||_\infty =$ norma matriciale infinito -> $max \sum_{j=1}^n |a_{ij}|$  (righe)

$||A||_1 =$ norma matriciale 1 -> $max \sum_{i=1}^n |a_{ij}|$  (colonne)

$||A||_2 =$ norma matriciale 2 -> $\sqrt{\rho(A^T*A)}$ , dove $\rho(X)$  è il raggio spettrale

$\rho(X)=$ raggio spettrale -> $max |\lambda_i|$ (max autovalore, in valore assoluto, di X)

$K_i(A) =||A||_i *||A^{-1}||_i$  -> condizionamento (i = 1/2/infinito) -> +grande(bad), +piccolo(good)

>![[Pasted image 20230621162508.png]]
>il centro di un cerchio è i-esimo elemento della diagonale
>il raggio di un cerchio è la sommatoria degli elementi (in valore assoluto), escluso il centro, della riga i-esima

se tutte le sotto matrici di A, fino a n-1, sono invertibili allora esiste unica LU

$E_i = I_n - v^T*e^T_i$ -> matrice E elementare di gauss -> v  = colonna ridotta mediante la riduzione di gauss -> i indica il passo di riduzione

$A_1 = E_1*A_0$ 

>![[Pasted image 20230621164143.png]]
>L gli elementi sotto la diagonale di L sono i valori per cui moltiplichi le righe
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

