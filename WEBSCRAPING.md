
![[Pasted image 20240901191355.png]]

![[Pasted image 20240901191416.png]]

![[Pasted image 20240901191439.png]]

![[Pasted image 20240901191459.png]]

![[Pasted image 20240901191537.png]]

![[Pasted image 20240901191622.png]]

![[Pasted image 20240901191649.png]]

![[Pasted image 20240901192101.png]]

![[Pasted image 20240901192321.png]]

![[Pasted image 20240901193407.png]]

![[Pasted image 20240901194350.png]]

![[Pasted image 20240901194954.png]]

![[Pasted image 20240901195009.png]]

![[Pasted image 20240901195252.png]]

![[Pasted image 20240901195410.png]]

![[Pasted image 20240901195431.png]]

![[Pasted image 20240901195449.png]]

![[Pasted image 20240901195504.png]]

![[Pasted image 20240901195517.png]]

![[Pasted image 20240901195529.png]]

![[Pasted image 20240901195547.png]]

![[Pasted image 20240901195608.png]]

![[matplotlib-cheatsheet.pdf]]

![[Pasted image 20240901200201.png]]

![[Pasted image 20240901200310.png]]

![[Pasted image 20240901200412.png]]

![[Pasted image 20240901200525.png]]

![[Pasted image 20240901200719.png]]


![[Pasted image 20240901200931.png]]

![[Pasted image 20240901202228.png]]

![[Pasted image 20240901202931.png]]

![[Pasted image 20240901203102.png]]

![[Pasted image 20240902161528.png]]

![[Pasted image 20240902163533.png]]

![[Pasted image 20240902164141.png]]

![[Pasted image 20240902164753.png]]

![[Pasted image 20240902170654.png]]

![[Pasted image 20240902170812.png]]

![[Pasted image 20240902170934.png]]

```html
tr = riga tabella
<table class="table-1">
  <tr> 
	NOMI COLONNE
	<th>Corso</th>
    <th>Laurea</th>
    <th>Numero Studenti</th>
  </tr>
  <tr>
    <td>Laboratorio Web Scraping</td>
    <td>Informatica</td>
    <td>20</td>
  </tr>
  <tr>
    <td>Blockchains</td>
    <td>Magistrale Informatica</td>
    <td>40</td>
  </tr>
</table>
```

Layout x grafi:
- circular_layout
- fruchterman_reingold_layout
- random_layout
- shell_layout
- spectral_layout

>degree centrality: 
>$$\frac{\#archi\_incidenti}{\#tot\_archi}$$

![[Pasted image 20240917215324.png]]

![[Pasted image 20240917215415.png]]

![[Pasted image 20240917215628.png]]

![[Pasted image 20240917221209.png]]

Modelli di grafi:
- Random Graph (Erdos,Renyi)
- Watts-Strogatz
- Kleinberg
- Barabasi-Albert

## Random Graph:

n = \#nodi
p = probabilità

![[Pasted image 20240917215024.png]]

![[Pasted image 20240917215705.png]]

![[Pasted image 20240917223107.png]]

![[Pasted image 20240917223130.png]]

Clustering coefficient di un nodo:
- caso g orientato: 
	- ![[Pasted image 20240917232511.png]]
- caso g non orientato:
	- ![[Pasted image 20240917232630.png]]

Clustering coefficient di un grafo (CC):
- $$\frac{\sum Clustering\_coefficient}{\#nodi}$$
- $$\frac{\#triangoli\_presenti}{\#triangoli\_possibili}$$

Graph Density:
- $$\rho = \frac{2*\#archi}{\#nodi*(\#nodi-1)/2}$$
- $\rho$ small $\implies$ sparse
- $\rho$ large $\implies$ dense

High clustering if CC >> $\rho$

![[Pasted image 20240921005448.png]]

## Small World:

![[Pasted image 20240921005637.png]]

## Watts e Strogatz:

![[Pasted image 20240921005735.png]]

![[Pasted image 20240921005938.png]]

![[Pasted image 20240921010119.png]]

p=0 => grafo regolare
p=1 => grafo random

**X = log(xi)**: ogni valore **xi** è rappresentato sull'asse delle x da una distanza dall'origine pari a **log(xi)** => 1 (distanza = 0), 10 (distanza = 1), ...

np.logspace(-4,0,10) -> range potenze (-4,0) di 10

**la rete è una small world** se ha il coefficiente di clustering significativo, diametro basso

![[Pasted image 20240921011317.png]]

- Degree centrality -> numero archi incidenti nel nodo: $$\frac{Archi\_connessi}{\#TotArchi}$$
- Betweeness centrality: $$\frac{\#Cammini\_minimi\_incidenti}{\#TotCammini\_minimi}$$
- Closeness Centrality -> distanza media del nodo rispetto agli altri nodi della rete (+alto => + centrale)

- Eigenvector centrality -> pagerank (l'**importanza** di un nodo in un grafo è determinata dall'**importanza dei nodi vicini**)


![[Pasted image 20240922160633.png]]

## Power Law Distribution

![[Pasted image 20240922161217.png]]

![[Pasted image 20240922161342.png]]

## Barabasi Albert

![[Pasted image 20240922162323.png]]

![[Pasted image 20240922163030.png]]

![[Pasted image 20240922163420.png]]

## BITCOIN

![[Pasted image 20240922164133.png]]

![[Pasted image 20240922164421.png]]

![[Pasted image 20240922165020.png]]

![[Pasted image 20240922165216.png]]

![[Pasted image 20240922165328.png]]

![[Pasted image 20240922165808.png]]

![[Pasted image 20240922165937.png]]

![[Pasted image 20240922170608.png]]

![[Pasted image 20240922171238.png]]


## BeautifulSoup:

![[justin1209_beautiful-soup.pdf]]

## SELENIUM:

![[lezione030424.pdf]]

![[lezione100424.pdf]]

## PANDAS:

![[Pandas_Cheat_Sheet.pdf]]

![[lezione-30-04-24.pdf]]

