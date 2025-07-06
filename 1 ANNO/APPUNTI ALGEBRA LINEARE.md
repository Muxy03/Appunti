Tutorial Matrici: 
$$
\begin{bmatrix}
1 & 2 & 3 \\
Porco & DIO & Bastardo \\ 
Puttana & La & Madonna \\
\end{bmatrix}
$$

Tutorial Sistemi:
$$
\begin{equation*}
\left\{
\begin{alignedat}{3}
% R & L   &  R & L   &  R & L 
 2x & +{} &  y & +{} & 3z & = 10 \\
  x & +{} &  y & +{} &  z & = 6 \\
  x & +{} & 3y & +{} & 2z & = 13
\end{alignedat}
\right.
\end{equation*}
$$


determinare numero di soluzioni di un sistema lineare -> riduzione matrice corrispondente

Esempio: (ultima colonna rappresenta il vettore di termini noti/membri destri delle eq)
$$
\begin{equation*}
\left\{
\begin{alignedat}{3}
% R & L   &  R & L   &  R & L 
 2x & +{} &  y & +{} & 3z & = 10 \\
  x & +{} &  y & +{} &  z & = 6 \\
  x & +{} & 3y & +{} & 2z & = 13
\end{alignedat}
\right.
\end{equation*}
\rightarrow 
\begin{bmatrix}
2 & 1 & 3 & (10) \\
1 & 1 & 1 & (6)  \\ 
1 & 3 & 2 & (13) \\
\end{bmatrix}
$$

>eq impossibile => 0 soluzioni
>0 colonne libere => 1 soluzione
>eq del tipo " $0x=5$ "=> $\infty$ soluzioni


>Procedura soluzioni speciali:
>
>$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 0 & 1 & 1 \\ 
0 & 0 & 0 & 0 \\
\end{bmatrix}
$$
> la 2 e 4 colonna sono colonne L => per trovare le soluzioni speciali bisogna porre $x_2,x_4$ uno alla volta =1 e = 0 (esempio sotto)
> $$
  \begin{equation*}
\left\{
\begin{alignedat}{0}
% R & L   &  R & L   &  R & L 
 x_1 & +{} & x_2 & +{} & x_3 & +{} & x_4 & = 0 \\
 x_3 & +{} & x_4 & = 0
\end{alignedat}
\right.
\end{equation*}
 $$
> ponendo una volta $(x_2=1,x_4=0)$ => $s_1 = \begin{bmatrix} -1\\ 1 \\ 0 \\ 0\end{bmatrix}$
>  ponendo una volta $(x_2=0,x_4=1)$ => $s_2 = \begin{bmatrix} 0\\ 0 \\ -1 \\ 1\end{bmatrix}$ 

