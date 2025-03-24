In this document the fractions includes the floor operation on the result of division. 

## Part 1:

### 1)

If W is a prefix of S the computation of F(W) with only F(S) and |W|  is impossible because:

$F(W) = \frac{F(S)}{131^{|S|-|W|}}$

### 2)

$F(S) = F(W)*131^{|W|} + F(Z)$

$F(W) = \frac{F(S) - F(Z)}{131^{|Z|}}$

$F(Z) = F(S) - F(W)$

## Part 2:

DS  = HashMap -> key, value = (F($S_i$), number of occorence)

hash function H($F(S_i)$) = F($S_i$) % number

Time complexity:
- Insert/Search element = O(1) 
- Building = O(|D|) = O(M)
- Computation of the number of viruses found = O(|D|) = O(M)
Space complexity = O(|D|) = O(M)