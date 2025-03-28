## LEZIONE 1 18/2/25

![[Pasted image 20250218163434.png]]

riguardare linguaggi di fondamenti 

![[Pasted image 20250218171116.png]]

![[Pasted image 20250218171149.png]]

![[Pasted image 20250218171551.png]]

![[Pasted image 20250218171847.png]]

![[Pasted image 20250218171912.png]]

![[Pasted image 20250218172018.png]]

S ::= (S) | $\epsilon$ | SS

do c while(!b);

approcci semantica:
- operational -> macchine astratte
- denotational -> function from Programs to Domains
- axiomatic

compositionally principle:
![[Pasted image 20250218173549.png]]

![[Pasted image 20250218174154.png]]

![[Pasted image 20250218174335.png]]

![[Pasted image 20250218174721.png]]

![[Pasted image 20250218174923.png]]


## LEZIONE 2 20/2/25

1 small-step freccia + corta
1 big-step freccia + lunga 
freccia start => n small-step

![[Pasted image 20250220141852.png]]

![[Pasted image 20250220142657.png]]

![[Pasted image 20250220143151.png]]

![[Pasted image 20250220143450.png]]

![[Pasted image 20250220143807.png]]

![[Pasted image 20250220143856.png]]

$\equiv_s$ -> small-step
$\equiv_b$ -> big-step
$\equiv_d$ -> denotational semantics

![[swcomp1]]

![[Pasted image 20250220152746.png]]

![[Pasted image 20250220152901.png]]

![[Pasted image 20250220152955.png]]

![[Pasted image 20250220153157.png]]

![[Pasted image 20250220153309.png]]

![[Pasted image 20250220153830.png]]

![[Pasted image 20250220153941.png]]

![[Pasted image 20250220154059.png]]

![[Pasted image 20250220154416.png]]

![[Pasted image 20250220154834.png]]

ogni soluzione di G è un unificatore di G

![[Pasted image 20250220155426.png]]

![[Pasted image 20250220155603.png]]

![[Pasted image 20250220155659.png]]

![[Pasted image 20250220155722.png]]

eliminate -> se c'è una sostituzione applicabile si applica

## LEZIONE 3 21/2/25

![[Pasted image 20250221093047.png]]

assioma = rule con 0 premesse

![[Pasted image 20250221093135.png]]
logic system = set of inference rules e axioms

if an inference rule contains some variables, we assume all its instances are in the logic system

![[Pasted image 20250221093519.png]]

![[Pasted image 20250221094204.png]]

![[Pasted image 20250221094824.png]]

![[Pasted image 20250221095024.png]]

![[Pasted image 20250221095217.png]]

![[Pasted image 20250221095618.png]]

![[Pasted image 20250221095711.png]]

![[Pasted image 20250221100220.png]]

![[Pasted image 20250221101905.png]]

![[Pasted image 20250221102157.png]]

mirror(t1,t2) :- t1 

## LEZIONE 4 25/2/25

![[Pasted image 20250225161453.png]]

![[Pasted image 20250225161920.png]]

![[Pasted image 20250225162500.png]]

![[Pasted image 20250225162520.png]]

![[Pasted image 20250225163610.png]]

![[Pasted image 20250225163747.png]]

![[Pasted image 20250225164228.png]]

![[Pasted image 20250225164211.png]]

![[Pasted image 20250225164356.png]]

![[Pasted image 20250225164458.png]]

![[Pasted image 20250225164555.png]]

![[Pasted image 20250225164639.png]]

![[Pasted image 20250225164934.png]]

![[Pasted image 20250225164759.png]]

![[Pasted image 20250225165246.png]]

![[Pasted image 20250225165340.png]]

![[Pasted image 20250225165648.png]]

![[Pasted image 20250225165852.png]]

![[Pasted image 20250225171405.png]]

![[Pasted image 20250225172202.png]]

![[Pasted image 20250225172215.png]]

![[Pasted image 20250225172231.png]]

![[Pasted image 20250225172245.png]]

![[Pasted image 20250225173503.png]]

![[Pasted image 20250225173517.png]]

![[Pasted image 20250225173711.png]]

![[Pasted image 20250225174050.png]]

![[Pasted image 20250225174151.png]]

![[Pasted image 20250225174257.png]]

![[Pasted image 20250225174353.png]]

![[Pasted image 20250225174830.png]]

![[Pasted image 20250225174936.png]]

![[Pasted image 20250225175240.png]]

![[Pasted image 20250225175250.png]]

![[Pasted image 20250225175330.png]]

![[Pasted image 20250225175338.png]]

![[Pasted image 20250225175514.png]]

![[Pasted image 20250225175527.png]]

## LEZIONE 4/3/25


TERMINATION = A RESULT CAN ALWAYS BE RETURNED
DETERMINACY = ANY TWO RESULTS ARE THE SAME

![[Pasted image 20250304172031.png]]

![[Pasted image 20250304172423.png]]

![[Pasted image 20250304172515.png]]

![[Pasted image 20250304172526.png]]
![[Pasted image 20250304172742.png]]

![[Pasted image 20250304172754.png]]

![[Pasted image 20250304172807.png]]

![[Pasted image 20250304173136.png]]

![[Pasted image 20250304173146.png]]

![[Pasted image 20250304173454.png]]

![[Pasted image 20250304173614.png]]

![[Pasted image 20250304173942.png]]

![[Pasted image 20250304173957.png]]

![[Pasted image 20250304174030.png]]

![[Pasted image 20250304174123.png]]

![[Pasted image 20250304174148.png]]

![[Pasted image 20250304174411.png]]

![[Pasted image 20250304174427.png]]

![[Pasted image 20250304174627.png]]

![[Pasted image 20250304174639.png]]

![[Pasted image 20250304175044.png]]

![[Pasted image 20250304175318.png]]

### ESERCIZI:

### EX 1:

```prolog
prod(0,y,0).
prod(s(x),y,z) :- prod(x,y,w),sum(w,y,z).

pow(0,s(y),0).
pow(s(x),0,s(0)).
pow(x,s(y),z) :- pow(x,y,w),prod(w,x,z).

div(s(y),z) :- prod(x,s(y),z).
```

### EX 2:

1) not possible
2) \[x=s(y), z=s(y)\]
3) not possible

### EX 3:

RECUPERARE SLIDES

### EX 4:

RECUPERARE SLIDES

### EX 5:

RECUPERA SLIDES

### EX 6:
 
 RECUPERA SLIDES

## LEZIONE 6/3/25

![[20250306_250306_163234.pdf]]

## LEZIONE 

![[2025-03-07 - 06 - Equivalence.pdf]]

![[2025-03-07 - 07 - Recursion.pdf]]

## LEZIONE 

![[20250311  08a  CPO_250312_132832.pdf]]

## LEZIONE 13/03/2025

![[softwareComposition13032025_250313_153822.pdf]]

## LEZIONE 18/3/25

![[18032025.pdf]]
![[18032025 2.pdf]]

## LEZIONE 20/3/25

![[2025-03-20 - 10 - Consistency IMP.pdf]]

## LEZIONE 21/3/25

![[2025-03-21 - 11 - Haskell.pdf]]

## LEZIONE 27/3/25

![[2025-03-27 - 12a - HOFL Types.pdf]]

## LEZIONE 28/3/25

![[2025-03-28 - 12b - HOFL Operational.pdf]]

![[2025-03-28 - 13a - Cartesian Domains.pdf]]

![[2025-03-28 - Haskell Badge.pdf]]