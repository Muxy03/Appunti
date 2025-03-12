Author: Andrea Mussari

## Problem 1

Two people use the following algorithm to divide between themselves $10. 
Each person names an integer number in the range \[0, 10\].

- If the sum of the numbers is at most 10 then each person receives the amount of money she names and the remainder is destroyed.  
- Otherwise (the sum of the numbers exceeds 10) 
	- if the amounts named are different then the person who names the smaller amount receives that amount and the other person receives the remaining money.  
	- If the amounts named are the same then each person receives $5.


if $x_1 + x_2 \le 10$ then the player with the lowest x will increase his x to improve the him gain.

if $x_1 + x_2 > 10$ and $x_1 \neq x_2$ then one player will decrease his x to improve the him gain  or the other player will increase his x to improve the him gain.

if $x_1 + x_2 > 10$ and $x_1 = x_2$ then one of the players will decrease his x to improve the him gain.

These rules are valid for all cases expect these cases:
- (5,5)
- (6,6)
- (5,6)
- (6,5)

In fact in these cases we have the Nash Equilibria.

## Problem 2

Judge Actions: Incriminate, Absolve
Accused Actions: Appeal, not Appeal

We assume that the appeal is an oracle, so the guilty will always end up in jail and the innocent will never end up in jail.

the appeal on a choice of judge in case of victory entails the opposite choice.

Happiness of society = the number of guilty who end up in jail + the number of innocent people who do not end up in jail.

If the appeal is then the number of free innocents can remain the same or it can only increase.

If the appeal is exhausted, then the number of offenders who end up in prison may remain the same or it may only increase.

Finally we can say that the bill is correct because in the worst case the happiness of society remains the same.

## Problem 3

An investment agency wants to collect a certain amount of money for a project. 
Aimed at convincing all the members of a group of N people to contribute to the fund, it proposes the following contract: each member can freely decide either to contribute with 100 euros or not to contribute (retaining money on its own wallet). 
Independently on this choice, after one year, the fund will be rewarded with an interest of 50% and uniformly redistributed among all the N members of the group. 
Describe the game and find the Nash equilibrium.

$x_i = 1 \text{ if Player i decide to invest}$
$x_i = 0 \text{ otherwise}$

$U_i(x_1,\dots,x_n) = 100(1 - x_i) + \frac{3}{2N} * \sum_{j=1}^N{100*x_j}$

$$
\begin{table}[]
\caption{cazo}
\label{tab:my-table}
\begin{tabular}{|c|c|c|}
\hline
P\_1 \textbackslash P\_2 & C       & NC      \\ \hline
C                        & 150,150 & 75,175  \\ \hline
NC                       & 175,75  & 100,100 \\ \hline
\end{tabular}
\end{table}}
$$

We can see in the table $ ref{tab:my-table}$ that choosing not to contribute is the dominant strategy for all players and therefore we get the Nash Equilibria in case all players decide not to contribute.

the Nash equilibria case:
- (0,0,...,0)

