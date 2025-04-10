Author: Andrea Mussari

## Problem 1

| P1 \ P2     | Rock | Paper | Scissors | Probability |
| ----------- | ---- | ----- | -------- | ----------- |
| Rock        | 0,0  | -1,1  | 1,-1     | p1          |
| Paper       | 1,-1 | 0,0   | -1,1     | p2          |
| Scissors    | -1,1 | 1,-1  | 0,0      | 1-p2        |
| Probability | p1   | p2    | 1-p1-p2  |             |
No nash equilibria

Mixed Strategy Nash Equilibrium:

$EU_1(R) = -p_2+1-p-1-p_2 = -2p_2-p_1+1$
$EU_1(P) = p_1-1+p_1+p_2=p_2+2p_1-1$
$EU_1(S) = p_2-p_1$

$EU_1(R) = EU_1(S) \implies -3p_2=-1 \iff p_2=\frac{1}{3}$
$EU_1(P) = EU_1(S) \implies 3p_1=1 \iff p_1=\frac{1}{3}$

## Problem 2

| P1 \ P2     | P (Principal) | S (Secondary) | Probability |
| ----------- | ------------- | ------------- | ----------- |
| P           | -1,-1         | 1,0           | p           |
| S           | 0,1           | 1,1           | 1-p         |
| Probability | q             | 1-q           |             |
Nash equilibria = (S,S)

Mixed Strategy:

Player 1:
	$EU(P) = -q+1-q$
	$EU(S) = 1-q$
	$EU(P)=EU(S) \iff q=0$
	
Player 2:
	$EU(P) = -p$
	$EU(S) = p+1-p$
	$EU(P)=EU(S) \iff p=0$

$q,p = 0 \implies$(S,S) 

## Problem 3

Payoff function for Families:
$$
U_i(k) = \alpha_1*D_{home,k}+\alpha_2*D_{work,k}*SP_i+\alpha_3*SIB_{i,k}
$$
Legend:
- $U_i(k)$ Payoff for family i if assigned to kindergarten k
- $D_{x,y}$  distance between x and y (Manhattan distance)
- $SP_i$  1 if single parent, 0 otherwise for family i
- $SIB_{i,k}$ 1 if child has sibiling at kindergarten k, 0 otherwise for family i
- $\alpha_3>\alpha_2>\alpha_1$ weight parameters to reflect priority rules 

Payoff function for Kindergartens:
$$V_k(M) = \sum_{i \in M_k}(\beta_1*SIB_{i,k}+\beta_2*SP_i*D_{work,k})-\beta_3*max(0,|M_k| - C_k)$$
Legend:
- $V_j(M)$ Payoff for kindergarten k under matching M
- $M_k$ set of families assigned to kindergarten k under matching M
- $SIB_{i,k}$ defined above
- $SP_i$ defined above
- $D_{work,k}$ defined above
- $|M_j|$ is the number of children assigned to kindergarten k
- $C_k$ capacity of kindergarten k
- $\beta_1,\beta_2,\beta_3$ weight parameters to reflect priority rules, $\beta_3 >> \beta_1$ and $\beta_3 >> \beta_2$

In the case of twin sibilings (a,b)  we can modify the payoff function for families so that if $k_a \neq k_b$  the function return $-\infty$.