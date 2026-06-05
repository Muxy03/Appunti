## 01-Introduction.pdf

a program *c* syntax, its meaning *\[\[c]]* semantics

$\sigma:X \to \mathbb{Z}$ (state: set(variables) -> set(integers))

$\Sigma \triangleq \{\sigma:X \to \mathbb{Z}\}$ (set(states))

![[Pasted image 20260508011059.png]]

![[Pasted image 20260508011110.png]]

![[Pasted image 20260508011125.png]]

![[Pasted image 20260508011135.png]]

![[Pasted image 20260508011149.png]]

![[Pasted image 20260508011230.png]]

![[Pasted image 20260508011302.png]]

![[Pasted image 20260508011313.png]]

![[Pasted image 20260508011324.png]]

![[Pasted image 20260508011429.png]]

![[Pasted image 20260508011355.png]]

![[Pasted image 20260508011450.png]]

![[Pasted image 20260508011502.png]]

![[Pasted image 20260508012403.png]]

![[Pasted image 20260508012418.png]]

![[Pasted image 20260508012511.png]]

Machine-assisted Proving:
- not automatic: key proof arguments provided by users and checked by the system
- sound: if the formalization is correct
- quasi-complete: (only limited by the expressiveness of the logics)
- Rocq

![[Pasted image 20260508012659.png]]

![[Pasted image 20260508012711.png]]

![[Pasted image 20260508012725.png]]

![[Pasted image 20260508012741.png]]


---

## 02-Denotational.pf

![[Pasted image 20260508012933.png]]

![[Pasted image 20260508012947.png]]

![[Pasted image 20260508012959.png]]

![[Pasted image 20260508013025.png]]

![[Pasted image 20260508013113.png]]

![[Pasted image 20260508013150.png]]

![[Pasted image 20260508013213.png]]

![[Pasted image 20260508013226.png]]

![[Pasted image 20260508013404.png]]

![[Pasted image 20260508013433.png]]

![[Pasted image 20260508013441.png]]

![[Pasted image 20260508013501.png]]

![[Pasted image 20260508013636.png]]

![[Pasted image 20260508013645.png]]

![[Pasted image 20260508013718.png]]

![[Pasted image 20260508013746.png]]

![[Pasted image 20260508013815.png]]

![[Pasted image 20260508014424.png]]

![[Pasted image 20260508014438.png]]

![[Pasted image 20260508014457.png]]

![[Pasted image 20260508014527.png]]

![[Pasted image 20260508014613.png]]

![[Pasted image 20260508014635.png]]

![[Pasted image 20260508014647.png]]

![[Pasted image 20260508014719.png]]

![[Pasted image 20260508014735.png]]

![[Pasted image 20260508014746.png]]

![[Pasted image 20260508014803.png]]

![[2025-03-11 - 08b - Kleene.pdf#page=52]]

![[Pasted image 20260508014838.png]]

![[Pasted image 20260508014944.png]]

![[Pasted image 20260508014955.png]]

![[Pasted image 20260508015102.png]]

![[Pasted image 20260508015121.png]]

![[Pasted image 20260508015140.png]]

![[Pasted image 20260508015316.png]]

![[Pasted image 20260605161612.png]]

![[Pasted image 20260508015501.png]]

### Question 1

Dato il comando $c \triangleq (z := x) + (z := y)$ (scelta non deterministica) e la pre-condizione $P \triangleq (x = y = 0)$:

1. **Cosa è $[[c]]P$ ?**
    - **Risposta:** $(x = y = z = 0)$. Entrambi i rami portano allo stesso stato finale.
2. **Esempio di sovra-approssimazione:**
    - **Risposta:** $(x = y = 0)$. Questo insieme include lo stato reale ma è meno preciso (non specifica il valore di $z$).
3. **Esempio di sotto-approssimazione:**
    - **Risposta:** $(x = y = z = 0)$. In questo caso, essendo il calcolo esatto, la sotto-approssimazione coincide con il risultato reale.
4. **Cosa è $wlp(c, z=0)$?**
    - **Risposta:** $(x = 0 \wedge y = 0)$. La _weakest liberal precondition_ richiede che **tutti** i rami possibili terminino in uno stato dove $z=0$.
5. **Cosa è $wpp(c, z=0)$?**
    - **Risposta:** $(x = 0 \vee y = 0)$. La _weakest possible precondition_ richiede che **almeno uno** dei rami termini in uno stato dove $z=0$.

---

### Question 2

Dato $c \triangleq \text{if } x < y \text{ then } x := y \text{ else } (\text{while true do skip})$ e specifica di correttezza $Q \triangleq (x = y = 0)$:

1. **Cosa è $wlp(c, Q)$?**
    - **Risposta:** $(x \ge y \vee y = 0)$. Se $x \ge y$, il programma non termina (soddisfacendo vacuamente la proprietà "se termina, allora $Q$"). Se $x < y$, deve valere $y = 0$ affinché l'assegnamento $x := y$ risulti in $x=0$.
2. **Cosa è $wpp(c, Q)$?**
    - **Risposta:** $(x < y \wedge y = 0)$. Affinché esista **almeno** una computazione che termina in $Q$, dobbiamo evitare il ramo divergente (quindi $x < y$) e garantire che il risultato sia zero (quindi $y = 0$).

---

### Question 3

![[Pasted image 20260605163129.png]]

---
## 03-HL.pdf

![[Pasted image 20260508015755.png]]

![[Pasted image 20260508015808.png]]

![[Pasted image 20260508015816.png]]

![[Pasted image 20260508015834.png]]

![[Pasted image 20260508015909.png]]

![[Pasted image 20260508015921.png]]

![[Pasted image 20260508015937.png]]

![[Pasted image 20260508020044.png]]

![[Pasted image 20260508020129.png]]

![[Pasted image 20260508020309.png]]

![[Pasted image 20260508020317.png]]

>HL rules:
>$$
\begin{align}
& \frac{}{\{P\}skip\{P\}} & \\ \\
& [Floyd]\frac{}{\{P\}x:=a\{\exists x'.P[x'/x] \land x=a[x'/x]\}} & \\ \\
& [Hoare]\frac{}{\{Q[a/x]x:=a\{Q\}\}} & \\ \\ 
& \frac{\{P\}c_1\{R\} \space \{R\}c_2\{Q\}}{\{P\}c_1;c_2\{Q\}} & \\ \\
& \frac{\{P \land b\}c_1\{Q\} \land \{P \land \lnot b\}c_2\{Q\}}{\{P\} \text{if b then c1 else c2} \{Q\}} & \\ \\
& \frac{\{P \land b\} c \{P\}}{\{P\} \text{while b do c} \{P \land \lnot b\}} & \\ \\
& \frac{P \implies P' \space \{P'\}c\{Q'\} \space Q' \implies Q}{\{P\}c\{Q\}}
\end{align}$$

![[Pasted image 20260508022300.png]]

![[Pasted image 20260508022351.png]]

![[Pasted image 20260508022617.png]]

![[Pasted image 20260508023101.png]]

![[Pasted image 20260508023336.png]]

![[Pasted image 20260508023434.png]]

#TODO Exercises

---

## 04-TotalCorrectness.pdf

![[Pasted image 20260508023655.png]]

![[Pasted image 20260508023901.png]]

![[Pasted image 20260508023936.png]]

![[Pasted image 20260508024007.png]]

![[Pasted image 20260508024025.png]]

![[Pasted image 20260508024130.png]]

![[Pasted image 20260508024140.png]]

![[Pasted image 20260508024935.png]]

![[Pasted image 20260508024959.png]]

![[Pasted image 20260508025020.png]]

![[Pasted image 20260508025034.png]]

![[Pasted image 20260508025051.png]]

![[Pasted image 20260508025102.png]]

![[Pasted image 20260508025144.png]]

![[Pasted image 20260508025155.png]]

![[Pasted image 20260508025207.png]]

![[Pasted image 20260508025218.png]]

![[Pasted image 20260508025230.png]]

$$
P \implies wlp(c,Q) \iff [[c]]P \subseteq Q
$$

![[Pasted image 20260508025337.png]]

![[Pasted image 20260508025347.png]]

$\text{if b then c1 else c2} \triangleq (b?;c_1)+(\lnot b?;c_2)$
$\text{while b do c} \triangleq (b?;c)*;\lnot b?$

![[Pasted image 20260508025612.png]]

![[Pasted image 20260508025627.png]]

![[Pasted image 20260508025710.png]]

#TODO Questions

---

## 05-IL-draft.pdf

![[Pasted image 20260508025811.png]]

![[Pasted image 20260508025905.png]]

![[Pasted image 20260508025918.png]]

stronger $P \subseteq Q$ weaker
stronger $P \implies Q$ weaker
stronger $P \land Q \implies P \lor Q$ weaker

IL = Incorrectness Logic

![[Pasted image 20260508030115.png]]

![[Pasted image 20260508030127.png]]

![[Pasted image 20260508030200.png]]

![[Pasted image 20260508030230.png]]

![[Pasted image 20260508030242.png]]

$$
\begin{align}
& [Floyd]\frac{}{[P]x:=a[\exists x'.P'[x'/x] \land x=a[x'/x]]} & \\ \\
& [cons]\frac{P'\implies P \space [P']c[Q'] \space Q \implies Q'}{[P]c[Q]} & \\ \\
& [disj]\frac{[P_1]c[Q_1] \space [P_2]c[Q_2]}{[P_1 \lor P_2]c[q_1 \lor Q_2]} & \\ \\
& [Hoare]\frac{}{[Q[a/x]]x:=a[Q]} & \\ \\
& [skip]\frac{}{[P]skip[P]} & \\ \\
& [assume]\frac{}{[P]b?[P \land b]} & \\ \\
& [error]\frac{}{[P]error()[false]} & \\ \\
& [nondet]\frac{}{[P]x:=nondet()[\exists x.P]} & \\ \\
& [seq]\frac{[P]c_1[R] \space [R]c_2[Q]}{[P]c_1;c_2[Q]} & \\ \\
& [choice]\frac{[P]c_1[Q_1] \space [P]c_2[Q_2]}{[P]c_1+c_2[Q_1 \lor Q_2]} & \\ \\
& [if]\frac{[P \land b]c_1[Q_1] \space [P \land \lnot b]c_2[Q_2]}{[P]\text{if b then c1 else c2}[Q_1 \lor Q_2]}
\end{align}
$$

![[Pasted image 20260508030903.png]]

![[Pasted image 20260508031102.png]]

![[Pasted image 20260508031114.png]]

![[Pasted image 20260508031229.png]]

![[Pasted image 20260508031803.png]]

![[Pasted image 20260508031821.png]]

![[Pasted image 20260508031832.png]]

![[Pasted image 20260508031904.png]]

![[Pasted image 20260508031919.png]]

$\text{if b then c1 else c2} \triangleq (b?;c_1)+(\lnot b?;c2)$

![[Pasted image 20260508032236.png]]

![[Pasted image 20260508032259.png]]

![[Pasted image 20260508032322.png]]

![[Pasted image 20260508032333.png]]

![[Pasted image 20260508032419.png]]

![[Pasted image 20260508032432.png]]

![[Pasted image 20260508032447.png]]

![[Pasted image 20260508032507.png]]

![[Pasted image 20260508032528.png]]

![[Pasted image 20260508032536.png]]

![[Pasted image 20260508032549.png]]

![[Pasted image 20260508032655.png]]

#TODO Exercise

---

## 06-RealIL.pdf

$\epsilon \in \{ok, er\}$
$[P]c[\epsilon : Q]$

![[Pasted image 20260509014036.png]]

![[Pasted image 20260509014047.png]]

![[Pasted image 20260509014103.png]]

![[Pasted image 20260509014117.png]]

![[Pasted image 20260509014252.png]]

![[Pasted image 20260509014521.png]]

![[Pasted image 20260509014541.png]]

![[Pasted image 20260509014550.png]]

![[Pasted image 20260509014600.png]]

![[Pasted image 20260509014701.png]]

![[Pasted image 20260509015248.png]]

![[Pasted image 20260509015258.png]]

![[Pasted image 20260509015343.png]]

![[Pasted image 20260509015352.png]]

![[Pasted image 20260509015403.png]]

![[Pasted image 20260509015413.png]]

![[Pasted image 20260509015507.png]]

![[Pasted image 20260509015518.png]]

![[Pasted image 20260509015528.png]]

![[Pasted image 20260509015536.png]]

![[Pasted image 20260509015545.png]]

![[Pasted image 20260509015554.png]]

![[Pasted image 20260509015601.png]]

![[Pasted image 20260509015614.png]]

![[Pasted image 20260509015632.png]]

![[Pasted image 20260509015641.png]]

![[Pasted image 20260509015652.png]]

![[Pasted image 20260509015725.png]]

![[Pasted image 20260509020012.png]]

![[Pasted image 20260509020025.png]]

![[Pasted image 20260509020155.png]]

![[Pasted image 20260509020209.png]]

![[Pasted image 20260509020244.png]]

![[Pasted image 20260509020256.png]]

![[Pasted image 20260509020330.png]]

![[Pasted image 20260509020400.png]]

![[Pasted image 20260509020443.png]]

![[Pasted image 20260509020516.png]]

---

## 07-MoreIL.pdf

![[Pasted image 20260509020601.png]]

![[Pasted image 20260509020618.png]]

![[Pasted image 20260509020736.png]]

![[Pasted image 20260509020757.png]]

![[Pasted image 20260509020808.png]]

![[Pasted image 20260509020858.png]]

![[Pasted image 20260509020911.png]]

![[Pasted image 20260509021539.png]]

![[Pasted image 20260509021553.png]]

![[Pasted image 20260509021603.png]]

![[Pasted image 20260509021615.png]]

![[Pasted image 20260509021701.png]]

![[Pasted image 20260509021726.png]]

![[Pasted image 20260509021809.png]]

![[Pasted image 20260509021823.png]]

![[Pasted image 20260509021841.png]]

![[Pasted image 20260509021853.png]]

![[Pasted image 20260509021918.png]]

![[Pasted image 20260509021937.png]]

![[Pasted image 20260509021956.png]]

![[Pasted image 20260509022022.png]]

![[Pasted image 20260509022036.png]]

![[Pasted image 20260509022050.png]]

![[Pasted image 20260509022111.png]]

NC = Necessary conditions

![[Pasted image 20260509022126.png]]

![[Pasted image 20260509022154.png]]

![[Pasted image 20260509022204.png]]

![[Pasted image 20260509022214.png]]

![[Pasted image 20260509022223.png]]

![[Pasted image 20260509022235.png]]

![[Pasted image 20260509022248.png]]

![[Pasted image 20260509022918.png]]

![[Pasted image 20260509022927.png]]

![[Pasted image 20260509022938.png]]

![[Pasted image 20260509022953.png]]

![[Pasted image 20260509023008.png]]

![[Pasted image 20260509023021.png]]

---

## 08-SIL.pdf

![[Pasted image 20260509023323.png]]

![[Pasted image 20260509023343.png]]

![[Pasted image 20260509023449.png]]

![[Pasted image 20260509023543.png]]

![[Pasted image 20260509023621.png]]

![[Pasted image 20260509023630.png]]

![[Pasted image 20260509023740.png]]

![[Pasted image 20260509023749.png]]

![[Pasted image 20260509023757.png]]

![[Pasted image 20260509023817.png]]

![[Pasted image 20260509023848.png]]

![[Pasted image 20260509023855.png]]

![[Pasted image 20260509023907.png]]

![[Pasted image 20260509024047.png]]

![[Pasted image 20260509024102.png]]

![[Pasted image 20260509024111.png]]

![[Pasted image 20260509024224.png]]

![[Pasted image 20260509024244.png]]

![[Pasted image 20260509024253.png]]

![[Pasted image 20260509024308.png]]

![[Pasted image 20260509024318.png]]

![[Pasted image 20260509024328.png]]

![[Pasted image 20260509024447.png]]


---
## 09-SL.pdf

![[Pasted image 20260509024541.png]]

![[Pasted image 20260509024559.png]]

![[Pasted image 20260509024849.png]]

![[Pasted image 20260509024914.png]]

![[Pasted image 20260509024930.png]]

![[Pasted image 20260509025003.png]]

![[Pasted image 20260509025026.png]]

![[Pasted image 20260509025138.png]]

![[Pasted image 20260509025609.png]]

![[Pasted image 20260509025944.png]]

![[Pasted image 20260509030007.png]]

![[Pasted image 20260509030028.png]]

![[Pasted image 20260509030040.png]]

![[Pasted image 20260509030050.png]]

![[Pasted image 20260509030101.png]]

![[Pasted image 20260509030113.png]]

![[Pasted image 20260509030125.png]]

![[Pasted image 20260509030134.png]]

![[Pasted image 20260509030152.png]]

![[Pasted image 20260509030203.png]]

![[Pasted image 20260509030544.png]]

![[Pasted image 20260509030556.png]]

![[Pasted image 20260509030609.png]]

![[Pasted image 20260509030655.png]]

![[Pasted image 20260509030703.png]]

![[Pasted image 20260509030714.png]]

![[Pasted image 20260509030729.png]]

![[Pasted image 20260509030738.png]]

![[Pasted image 20260509030751.png]]

Separation logic = local axioms + frame rule

![[Pasted image 20260509030857.png]]

![[Pasted image 20260509030906.png]]

![[Pasted image 20260509031046.png]]

![[Pasted image 20260509031055.png]]

![[Pasted image 20260509031103.png]]

![[Pasted image 20260509031118.png]]

![[Pasted image 20260509031126.png]]

![[Pasted image 20260509031147.png]]

![[Pasted image 20260509031156.png]]

![[Pasted image 20260509031210.png]]

![[Pasted image 20260509031224.png]]

![[Pasted image 20260509031310.png]]

![[Pasted image 20260509031327.png]]

![[Pasted image 20260509031339.png]]

![[Pasted image 20260509031355.png]]

![[Pasted image 20260509031406.png]]

![[Pasted image 20260509031415.png]]

![[Pasted image 20260509031429.png]]

![[Pasted image 20260509031442.png]]

![[Pasted image 20260509031452.png]]

![[Pasted image 20260509031500.png]]

![[Pasted image 20260509031513.png]]

---

## 10-ISL-SepSIL.pdf

![[Pasted image 20260509031715.png]]

![[Pasted image 20260509031726.png]]

![[Pasted image 20260509031737.png]]

![[Pasted image 20260509031748.png]]

![[Pasted image 20260509031759.png]]

![[Pasted image 20260509031814.png]]

![[Pasted image 20260509031855.png]]

![[Pasted image 20260509031927.png]]

![[Pasted image 20260509031939.png]]

![[Pasted image 20260509032005.png]]

![[Pasted image 20260509032016.png]]

![[Pasted image 20260509032033.png]]

![[Pasted image 20260509032105.png]]

![[Pasted image 20260509032129.png]]

![[Pasted image 20260509032140.png]]

![[Pasted image 20260509032158.png]]

![[Pasted image 20260509032212.png]]

![[Pasted image 20260509032221.png]]

![[Pasted image 20260509032235.png]]

![[Pasted image 20260509032248.png]]

![[Pasted image 20260509032257.png]]

![[Pasted image 20260509032306.png]]

![[Pasted image 20260509032315.png]]

![[Pasted image 20260509032324.png]]

![[Pasted image 20260509032340.png]]

![[Pasted image 20260509032433.png]]

![[Pasted image 20260509032447.png]]

![[Pasted image 20260509032456.png]]

![[Pasted image 20260509032506.png]]

![[Pasted image 20260509032515.png]]

![[Pasted image 20260509032524.png]]

![[Pasted image 20260509032533.png]]

![[Pasted image 20260509032605.png]]

![[Pasted image 20260509032641.png]]

![[Pasted image 20260509032652.png]]

![[Pasted image 20260509033133.png]]

![[Pasted image 20260509033148.png]]

![[Pasted image 20260509033221.png]]

![[Pasted image 20260509033232.png]]

![[Pasted image 20260509033253.png]]

![[Pasted image 20260509033325.png]]

![[Pasted image 20260509033336.png]]

![[Pasted image 20260509033408.png]]

![[Pasted image 20260509033423.png]]

![[Pasted image 20260509033434.png]]

![[Pasted image 20260509033446.png]]

![[Pasted image 20260509033457.png]]

![[Pasted image 20260509033519.png]]

![[Pasted image 20260509033546.png]]

---

## 11-IntroAI-basic.pdf

![[Pasted image 20260509194426.png]]

![[Pasted image 20260509194444.png]]

![[Pasted image 20260509194501.png]]

![[Pasted image 20260509194546.png]]

![[Pasted image 20260509194556.png]]

E = Hypothetical error zone![[Pasted image 20260509211125.png]]

![[Pasted image 20260509211101.png]]

![[Pasted image 20260509211126.png]]

![[Pasted image 20260509211142.png]]

![[Pasted image 20260509211154.png]]

![[Pasted image 20260509211236.png]]

![[Pasted image 20260509211225.png]]

![[Pasted image 20260509211331.png]]

![[Pasted image 20260509211345.png]]

![[Pasted image 20260509211402.png]]

![[Pasted image 20260509211412.png]]

![[Pasted image 20260509211421.png]]

![[Pasted image 20260509211457.png]]

![[Pasted image 20260509211518.png]]

![[Pasted image 20260509211751.png]]

![[Pasted image 20260509211800.png]]

![[Pasted image 20260509211810.png]]

![[Pasted image 20260509211821.png]]

![[Pasted image 20260509211829.png]]

![[Pasted image 20260509212131.png]]

![[Pasted image 20260509212141.png]]

![[Pasted image 20260509212151.png]]

![[Pasted image 20260509212246.png]]

![[Pasted image 20260509212257.png]]

![[Pasted image 20260509212309.png]]

![[Pasted image 20260509212321.png]]

![[Pasted image 20260509212332.png]]

![[Pasted image 20260509212347.png]]

![[Pasted image 20260509212403.png]]

![[Pasted image 20260509212412.png]]

![[Pasted image 20260509212423.png]]

![[Pasted image 20260509212431.png]]

![[Pasted image 20260509212452.png]]

![[Pasted image 20260509212502.png]]

![[Pasted image 20260509212514.png]]

![[Pasted image 20260509212522.png]]

![[Pasted image 20260509212531.png]]

![[Pasted image 20260509212542.png]]

![[Pasted image 20260509212555.png]]

![[Pasted image 20260509212605.png]]

![[Pasted image 20260509212615.png]]

![[Pasted image 20260509212702.png]]

![[Pasted image 20260509212712.png]]

![[Pasted image 20260509212719.png]]

![[Pasted image 20260509212740.png]]

![[Pasted image 20260509212749.png]]

![[Pasted image 20260509212921.png]]

---
## 12-IntroAI-formal.pdf

![[Pasted image 20260509213021.png]]

![[Pasted image 20260509213038.png]]

![[Pasted image 20260509213046.png]]

![[Pasted image 20260509213108.png]]

![[Pasted image 20260509213117.png]]

![[Pasted image 20260509213127.png]]

![[Pasted image 20260509213136.png]]

![[Pasted image 20260509225515.png]]

![[Pasted image 20260509225530.png]]

![[Pasted image 20260509225539.png]]

![[Pasted image 20260509225548.png]]

![[Pasted image 20260509225559.png]]

![[Pasted image 20260509225610.png]]

![[Pasted image 20260509225626.png]]

![[Pasted image 20260509231349.png]]

![[Pasted image 20260509231410.png]]

![[Pasted image 20260509231434.png]]

![[Pasted image 20260509231659.png]]

![[Pasted image 20260509231711.png]]

![[Pasted image 20260510005505.png]]

![[Pasted image 20260510005520.png]]

![[Pasted image 20260510005536.png]]

![[Pasted image 20260510005552.png]]

![[Pasted image 20260510005602.png]]

![[Pasted image 20260510005618.png]]

![[Pasted image 20260510005640.png]]

![[Pasted image 20260510010634.png]]

![[Pasted image 20260510010649.png]]

![[Pasted image 20260510010703.png]]

![[Pasted image 20260510010804.png]]

![[Pasted image 20260510010813.png]]

![[Pasted image 20260510011622.png]]

![[Pasted image 20260510011633.png]]

![[Pasted image 20260510011827.png]]

![[Pasted image 20260510011850.png]]

![[Pasted image 20260510011901.png]]

![[Pasted image 20260510011911.png]]

![[Pasted image 20260510011932.png]]

![[Pasted image 20260510012049.png]]

![[Pasted image 20260510012105.png]]

![[Pasted image 20260510012119.png]]

![[Pasted image 20260510012129.png]]

![[Pasted image 20260510012139.png]]

![[Pasted image 20260510012153.png]]

![[Pasted image 20260510012311.png]]

![[Pasted image 20260510012335.png]]

![[Pasted image 20260510012402.png]]

![[Pasted image 20260510012634.png]]

![[Pasted image 20260510012650.png]]

![[Pasted image 20260510012958.png]]

![[Pasted image 20260510013011.png]]

![[Pasted image 20260510013023.png]]

---
## 13-Galois-draft.pdf

![[Pasted image 20260510013110.png]]

![[Pasted image 20260510013121.png]]

![[Pasted image 20260510013136.png]]

![[Pasted image 20260510013146.png]]

![[Pasted image 20260510013452.png]]

![[Pasted image 20260510013606.png]]

![[Pasted image 20260510013619.png]]

![[Pasted image 20260510013755.png]]

![[Pasted image 20260510013818.png]]

![[Pasted image 20260510013831.png]]

![[Pasted image 20260510014022.png]]

![[Pasted image 20260510014035.png]]

![[Pasted image 20260510014052.png]]

![[Pasted image 20260510014109.png]]

![[Pasted image 20260510014121.png]]

![[Pasted image 20260510014132.png]]

![[Pasted image 20260510014143.png]]

![[Pasted image 20260510014155.png]]

![[Pasted image 20260510014204.png]]

![[Pasted image 20260510014218.png]]

![[Pasted image 20260510014231.png]]

![[Pasted image 20260510014239.png]]

![[Pasted image 20260510014249.png]]

![[Pasted image 20260510014304.png]]

![[Pasted image 20260510014316.png]]

![[Pasted image 20260510014328.png]]

![[Pasted image 20260510014338.png]]

![[Pasted image 20260510014407.png]]

![[Pasted image 20260510014421.png]]

![[Pasted image 20260510014432.png]]

![[Pasted image 20260510014445.png]]

![[Pasted image 20260510014605.png]]

#TODO Exercises

![[Pasted image 20260510014639.png]]

![[Pasted image 20260510014648.png]]

![[Pasted image 20260510014658.png]]

![[Pasted image 20260510014749.png]]

![[Pasted image 20260510014759.png]]

![[Pasted image 20260510014808.png]]

![[Pasted image 20260510014822.png]]

![[Pasted image 20260510014832.png]]

![[Pasted image 20260510014944.png]]

![[Pasted image 20260510014955.png]]

![[Pasted image 20260510015006.png]]

![[Pasted image 20260510015118.png]]

![[Pasted image 20260510015129.png]]

![[Pasted image 20260510015140.png]]

![[Pasted image 20260510174756.png]]

![[Pasted image 20260510174808.png]]

![[Pasted image 20260510174817.png]]

![[Pasted image 20260510174834.png]]

![[Pasted image 20260510174845.png]]

![[Pasted image 20260510174853.png]]

![[Pasted image 20260510174902.png]]

![[Pasted image 20260510174911.png]]

![[Pasted image 20260510174925.png]]

![[Pasted image 20260510174935.png]]

![[Pasted image 20260510174945.png]]

![[Pasted image 20260510175000.png]]

![[Pasted image 20260510175010.png]]

![[Pasted image 20260510175020.png]]

![[Pasted image 20260510175031.png]]

![[Pasted image 20260510175039.png]]

![[Pasted image 20260510175048.png]]

![[Pasted image 20260510175058.png]]

![[Pasted image 20260510175106.png]]

![[Pasted image 20260510175117.png]]

![[Pasted image 20260510175131.png]]

#TODO Exercises

![[Pasted image 20260510175157.png]]

![[Pasted image 20260510175211.png]]

---

## 14-AbstractDomains-draft.pdf

![[Pasted image 20260510175320.png]]

![[Pasted image 20260510175333.png]]

![[Pasted image 20260510175645.png]]

![[Pasted image 20260510175658.png]]

![[Pasted image 20260510175710.png]]

![[Pasted image 20260510175743.png]]

![[Pasted image 20260510175832.png]]

![[Pasted image 20260510175851.png]]

![[Pasted image 20260510175900.png]]

![[Pasted image 20260510175908.png]]

![[Pasted image 20260510175919.png]]

![[Pasted image 20260510175928.png]]

![[Pasted image 20260510175937.png]]

![[Pasted image 20260510175945.png]]

![[Pasted image 20260510175954.png]]

![[Pasted image 20260510180008.png]]

![[Pasted image 20260510180025.png]]

![[Pasted image 20260510180051.png]]

#TODO Exercises

![[Pasted image 20260510180118.png]]

![[Pasted image 20260510180127.png]]

![[Pasted image 20260510180137.png]]

![[Pasted image 20260510180155.png]]

![[Pasted image 20260510180211.png]]

![[Pasted image 20260510180224.png]]

![[Pasted image 20260510180232.png]]

![[Pasted image 20260510180245.png]]

![[Pasted image 20260510180254.png]]

![[Pasted image 20260510180307.png]]

![[Pasted image 20260510180318.png]]

![[Pasted image 20260510180327.png]]

![[Pasted image 20260510180337.png]]

![[Pasted image 20260510180348.png]]

![[Pasted image 20260510180358.png]]

![[Pasted image 20260510180408.png]]

![[Pasted image 20260510180416.png]]

![[Pasted image 20260510180425.png]]

![[Pasted image 20260510180435.png]]

![[Pasted image 20260510180443.png]]

![[Pasted image 20260510180452.png]]

![[Pasted image 20260510180459.png]]

![[Pasted image 20260510180510.png]]

![[Pasted image 20260510180537.png]]

![[Pasted image 20260510180639.png]]

![[Pasted image 20260510180647.png]]

![[Pasted image 20260510180703.png]]

---

## 15-AbstractAnalysis.pdf

![[Pasted image 20260510180747.png]]

![[Pasted image 20260510180802.png]]

![[Pasted image 20260510180812.png]]

![[Pasted image 20260510180822.png]]

![[Pasted image 20260510180835.png]]

![[Pasted image 20260510180844.png]]

![[Pasted image 20260510180854.png]]

![[Pasted image 20260510180907.png]]

![[Pasted image 20260510180916.png]]

![[Pasted image 20260510180926.png]]

![[Pasted image 20260510180935.png]]

![[Pasted image 20260510180946.png]]

![[Pasted image 20260510181021.png]]

![[Pasted image 20260510181030.png]]

![[Pasted image 20260510181038.png]]

![[Pasted image 20260510181126.png]]

#TODO Exercises

![[Pasted image 20260510181155.png]]

![[Pasted image 20260510181203.png]]

![[Pasted image 20260510181212.png]]

![[Pasted image 20260510181222.png]]

![[Pasted image 20260510181229.png]]

![[Pasted image 20260510181235.png]]

![[Pasted image 20260510181244.png]]

![[Pasted image 20260510181253.png]]

![[Pasted image 20260510181312.png]]

![[Pasted image 20260510181322.png]]

![[Pasted image 20260510181337.png]]

![[Pasted image 20260510181349.png]]

![[Pasted image 20260510181356.png]]

![[Pasted image 20260510181403.png]]

![[Pasted image 20260510181413.png]]

![[Pasted image 20260510181424.png]]

![[Pasted image 20260510181434.png]]

![[Pasted image 20260510181450.png]]

![[Pasted image 20260510181500.png]]

![[Pasted image 20260510181508.png]]

![[Pasted image 20260510182324.png]]

![[Pasted image 20260510182332.png]]

![[Pasted image 20260510182344.png]]

![[Pasted image 20260510182354.png]]

![[Pasted image 20260510182404.png]]

![[Pasted image 20260510182412.png]]

![[Pasted image 20260510182421.png]]

![[Pasted image 20260510182430.png]]

![[Pasted image 20260510182440.png]]

![[Pasted image 20260510182451.png]]

![[Pasted image 20260510182500.png]]

![[Pasted image 20260510182509.png]]

![[Pasted image 20260510182517.png]]

![[Pasted image 20260510182525.png]]

![[Pasted image 20260510182536.png]]

![[Pasted image 20260510182544.png]]

![[Pasted image 20260510184411.png]]

![[Pasted image 20260510184419.png]]

![[Pasted image 20260510184427.png]]

![[Pasted image 20260510184436.png]]

![[Pasted image 20260510184444.png]]

![[Pasted image 20260510184454.png]]

#TODO Exercises

---
## 16-LCL.pdf

![[Pasted image 20260510202320.png]]

![[Pasted image 20260510202329.png]]

![[Pasted image 20260510202346.png]]

![[Pasted image 20260510202400.png]]

![[Pasted image 20260510202410.png]]

![[Pasted image 20260510202510.png]]

![[Pasted image 20260510202521.png]]

![[Pasted image 20260510202537.png]]

![[Pasted image 20260510202548.png]]

![[Pasted image 20260510202601.png]]

![[Pasted image 20260510202613.png]]

![[Pasted image 20260510202622.png]]

![[Pasted image 20260510202632.png]]

![[Pasted image 20260510202641.png]]

![[Pasted image 20260510202652.png]]

![[Pasted image 20260510202706.png]]

![[Pasted image 20260510202715.png]]

![[Pasted image 20260510202817.png]]

![[Pasted image 20260510202825.png]]

![[Pasted image 20260510202832.png]]

![[Pasted image 20260510202845.png]]

![[Pasted image 20260510202852.png]]

![[Pasted image 20260510202906.png]]

![[Pasted image 20260510202922.png]]

![[Pasted image 20260510202935.png]]

![[Pasted image 20260510202944.png]]

![[Pasted image 20260510202952.png]]

![[Pasted image 20260510203000.png]]

![[Pasted image 20260510203017.png]]

![[Pasted image 20260510203029.png]]

![[Pasted image 20260510203040.png]]

![[Pasted image 20260510203051.png]]

![[Pasted image 20260510203059.png]]

![[Pasted image 20260510203111.png]]

![[Pasted image 20260510203123.png]]

![[Pasted image 20260510203136.png]]

Logical correctness:
![[Pasted image 20260510203145.png]]

![[Pasted image 20260510203205.png]]

![[Pasted image 20260510203215.png]]

![[Pasted image 20260510203225.png]]

![[Pasted image 20260510203243.png]]

![[Pasted image 20260510203301.png]]

![[Pasted image 20260510203309.png]]

![[Pasted image 20260510203343.png]]

![[Pasted image 20260510203419.png]]

![[Pasted image 20260510203428.png]]

![[Pasted image 20260510203438.png]]

---
## Control Flow Analysis (CFA)
![[Pasted image 20260510225631.png]]
### 17:

![[Pasted image 20260510225634.png]]

![[Pasted image 20260510225647.png]]

![[Pasted image 20260510225657.png]]

![[Pasted image 20260510225706.png]]

![[Pasted image 20260510225718.png]]

![[Pasted image 20260510225724.png]]

![[Pasted image 20260510225734.png]]

![[Pasted image 20260510225745.png]]

![[Pasted image 20260510225756.png]]

![[Pasted image 20260510225804.png]]

![[Pasted image 20260510225815.png]]

![[Pasted image 20260510225833.png]]

![[Pasted image 20260511005555.png]]

![[Pasted image 20260511005610.png]]

![[Pasted image 20260511005620.png]]

![[Pasted image 20260511005656.png]]

![[Pasted image 20260511005716.png]]

![[Pasted image 20260511005724.png]]

![[Pasted image 20260511005737.png]]

![[Pasted image 20260511005913.png]]

![[Pasted image 20260511005923.png]]

![[Pasted image 20260511005937.png]]

![[Pasted image 20260511005946.png]]

![[Pasted image 20260511005954.png]]

![[Pasted image 20260511010001.png]]

![[Pasted image 20260511010018.png]]

![[Pasted image 20260511010027.png]]

![[Pasted image 20260511010039.png]]

![[Pasted image 20260511010048.png]]

![[Pasted image 20260511010124.png]]

![[Pasted image 20260511010137.png]]

![[Pasted image 20260511010150.png]]

![[Pasted image 20260511010210.png]]

![[Pasted image 20260511010231.png]]

![[Pasted image 20260511010240.png]]

![[Pasted image 20260511010249.png]]

![[Pasted image 20260511010259.png]]

![[Pasted image 20260511010307.png]]

![[Pasted image 20260511010316.png]]

![[Pasted image 20260511010327.png]]

![[Pasted image 20260511010336.png]]

![[Pasted image 20260511010345.png]]

![[Pasted image 20260511010400.png]]

![[Pasted image 20260511010409.png]]

![[Pasted image 20260511010418.png]]

![[Pasted image 20260511010438.png]]

![[Pasted image 20260511010447.png]]

### 18:

![[Pasted image 20260511010553.png]]

![[Pasted image 20260511010602.png]]

![[Pasted image 20260511010613.png]]

![[Pasted image 20260511010638.png]]

![[Pasted image 20260511010648.png]]

![[Pasted image 20260511010657.png]]

![[Pasted image 20260511010707.png]]

![[Pasted image 20260511010716.png]]

#TODO Exercise 3

![[Pasted image 20260511010741.png]]

![[Pasted image 20260511010749.png]]

![[Pasted image 20260511010800.png]]

![[Pasted image 20260511010810.png]]

![[Pasted image 20260511010819.png]]

![[Pasted image 20260511010829.png]]

![[Pasted image 20260511010841.png]]

![[Pasted image 20260511010851.png]]

![[Pasted image 20260511010900.png]]

![[Pasted image 20260511010908.png]]

![[Pasted image 20260511010917.png]]

![[Pasted image 20260511010929.png]]

![[Pasted image 20260511010937.png]]

![[Pasted image 20260511010947.png]]

![[Pasted image 20260511010956.png]]

![[Pasted image 20260511011007.png]]

![[Pasted image 20260511011019.png]]

![[Pasted image 20260511011025.png]]

![[Pasted image 20260511011038.png]]

![[Pasted image 20260511011047.png]]

![[Pasted image 20260511011055.png]]

![[Pasted image 20260511011106.png]]

### 19:

![[Pasted image 20260511011133.png]]

![[Pasted image 20260511011140.png]]

![[Pasted image 20260511011149.png]]

![[Pasted image 20260511011158.png]]

![[Pasted image 20260511011206.png]]

![[Pasted image 20260511011215.png]]

![[Pasted image 20260511011224.png]]

![[Pasted image 20260511011233.png]]

![[Pasted image 20260511011242.png]]

![[Pasted image 20260511011250.png]]

![[Pasted image 20260511011300.png]]

![[Pasted image 20260511011309.png]]

![[Pasted image 20260511011318.png]]

![[Pasted image 20260511011330.png]]

![[Pasted image 20260511011339.png]]

![[Pasted image 20260511011348.png]]

![[Pasted image 20260511011359.png]]

![[Pasted image 20260511011410.png]]

![[Pasted image 20260511011418.png]]

![[Pasted image 20260511011430.png]]

![[Pasted image 20260511011439.png]]

![[Pasted image 20260511011448.png]]

![[Pasted image 20260511011507.png]]

![[Pasted image 20260511011517.png]]

![[Pasted image 20260511011525.png]]

![[Pasted image 20260511011534.png]]

![[Pasted image 20260511011544.png]]

![[Pasted image 20260511011552.png]]

![[Pasted image 20260511011603.png]]

![[Pasted image 20260511011611.png]]

![[Pasted image 20260511011626.png]]

![[Pasted image 20260511011634.png]]

#TODO Exercise 1

![[Pasted image 20260511011658.png]]

![[Pasted image 20260511011709.png]]

![[Pasted image 20260511011717.png]]

![[Pasted image 20260511011727.png]]

![[Pasted image 20260511011740.png]]

![[Pasted image 20260511011748.png]]

![[Pasted image 20260511011759.png]]

![[Pasted image 20260511011808.png]]

![[Pasted image 20260511011814.png]]

![[Pasted image 20260511011826.png]]

![[Pasted image 20260511011835.png]]

![[Pasted image 20260511011843.png]]

### 20:

![[Pasted image 20260511011945.png]]

![[Pasted image 20260511011954.png]]

![[Pasted image 20260511012002.png]]

![[Pasted image 20260511012013.png]]

![[Pasted image 20260511012022.png]]

![[Pasted image 20260511012032.png]]

![[Pasted image 20260511012043.png]]

![[Pasted image 20260511012055.png]]

![[Pasted image 20260511012106.png]]

![[Pasted image 20260511012117.png]]

![[Pasted image 20260511012129.png]]

![[Pasted image 20260511012140.png]]

![[Pasted image 20260511012147.png]]

![[Pasted image 20260511012157.png]]

![[Pasted image 20260511012205.png]]

![[Pasted image 20260511012219.png]]

![[Pasted image 20260511013012.png]]

![[Pasted image 20260511013025.png]]

![[Pasted image 20260511013036.png]]

![[Pasted image 20260511015200.png]]

![[Pasted image 20260511015209.png]]

![[Pasted image 20260511015219.png]]

![[Pasted image 20260511015232.png]]

![[Pasted image 20260511015317.png]]

![[Pasted image 20260511015455.png]]

![[Pasted image 20260511015506.png]]

![[Pasted image 20260511015513.png]]

![[Pasted image 20260511015626.png]]

![[Pasted image 20260511015635.png]]

![[Pasted image 20260511015644.png]]

![[Pasted image 20260511015655.png]]

![[Pasted image 20260511015711.png]]

![[Pasted image 20260511015719.png]]

![[Pasted image 20260511015726.png]]

![[Pasted image 20260511015736.png]]

![[Pasted image 20260511015744.png]]

![[Pasted image 20260511015752.png]]

![[Pasted image 20260511015801.png]]

![[Pasted image 20260511015809.png]]

![[Pasted image 20260511015817.png]]

![[Pasted image 20260511015825.png]]

![[Pasted image 20260511015833.png]]

![[Pasted image 20260511015841.png]]

![[Pasted image 20260511015903.png]]

![[Pasted image 20260511015909.png]]

![[Pasted image 20260511015920.png]]

![[Pasted image 20260511022017.png]]

![[Pasted image 20260511022029.png]]

![[Pasted image 20260511022038.png]]

![[Pasted image 20260511022045.png]]

![[Pasted image 20260511022054.png]]

![[Pasted image 20260511022102.png]]

![[Pasted image 20260511022111.png]]

![[Pasted image 20260511022351.png]]

![[Pasted image 20260511022359.png]]

![[Pasted image 20260511022408.png]]

![[Pasted image 20260511022418.png]]

![[Pasted image 20260511022427.png]]

![[Pasted image 20260511022438.png]]

![[Pasted image 20260511022449.png]]

![[Pasted image 20260511022459.png]]

![[Pasted image 20260511022514.png]]

![[Pasted image 20260511022522.png]]

![[Pasted image 20260511022531.png]]

![[Pasted image 20260511022624.png]]

![[Pasted image 20260511022632.png]]

### 21:

![[Pasted image 20260511022657.png]]

![[Pasted image 20260511022705.png]]

![[Pasted image 20260511022713.png]]

![[Pasted image 20260511022722.png]]

![[Pasted image 20260511022731.png]]

![[Pasted image 20260511022741.png]]

![[Pasted image 20260511022751.png]]

![[Pasted image 20260511022800.png]]

![[Pasted image 20260511022811.png]]

![[Pasted image 20260511022821.png]]

![[Pasted image 20260511022829.png]]

![[Pasted image 20260511022836.png]]

![[Pasted image 20260511022845.png]]

![[Pasted image 20260511022853.png]]

![[Pasted image 20260511022902.png]]

![[Pasted image 20260511022912.png]]

![[Pasted image 20260511022922.png]]

![[Pasted image 20260511022930.png]]

![[Pasted image 20260511022942.png]]

![[Pasted image 20260511022950.png]]

![[Pasted image 20260511022958.png]]

![[Pasted image 20260511023005.png]]

![[Pasted image 20260511023015.png]]

![[Pasted image 20260511023024.png]]

![[Pasted image 20260511023036.png]]

![[Pasted image 20260511023048.png]]

![[Pasted image 20260511023058.png]]

![[Pasted image 20260511023114.png]]

![[Pasted image 20260511023122.png]]

![[Pasted image 20260511023131.png]]

![[Pasted image 20260511023139.png]]

![[Pasted image 20260511023231.png]]

![[Pasted image 20260511023241.png]]

![[Pasted image 20260511023251.png]]

![[Pasted image 20260511023301.png]]

![[Pasted image 20260511023310.png]]

![[Pasted image 20260511023320.png]]

![[Pasted image 20260511023330.png]]

![[Pasted image 20260511023341.png]]

![[Pasted image 20260511023355.png]]

![[Pasted image 20260511023406.png]]

