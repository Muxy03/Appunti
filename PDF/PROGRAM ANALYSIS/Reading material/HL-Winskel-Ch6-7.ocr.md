In  this  chapter we  turn to  the business  of systematic verification of programs in IMP. The Hoare rules for showing the partial correctness of programs are introduced and shown sound.  This involves extending the boolean expressions  to a  rich  language of assertions about program states.  The chapter concludes with an example of verification conducted within the framework of Hoare rules.

## 6.1 The idea

We  turn  to  consider  the  problem  of how  to prove  that  a  program  we  have  written  in IMP does what we  require of it.

Let's start with a simple example of a program to compute the sum of the first hundred numbers,  the  naive  way. Here  is  a  program  in IMP to  compute Ll::;m::;lOo m  (The notation Ll::;m::;100 m  means 1 + 2 + ... + 100).

<!-- formula-not-decoded -->

How would we  prove that this program, when it terminates,  is such that the value of S . '" 7 IS L....l::;m::;100 m.

Of  course  one  thing  we  could  do  would  be  to  run  it  according  to  our  operational semantics and see what we get.  But suppose we change our program a bit, so that instead of  "while -,(N = 101) do ...  "  we  put  "while -.(N = P + 1) do ...  "  and  imagine making some arbitrary assignment to P before we begin.  In this case the resulting value of  S  after  execution  should  be Ll::;m::;P m,  no  matter what  the value  of P. As P can take  an  infinite set  of values we  cannot justify this fact  simply by running the program for  all  initial values of P. We need to be a little more clever, and abstract, and use some logic  to reason about the program.

We'll  end  up  with  a  formal  proof system  for  proving  properties  of IMP programs, based on proof rules for  each programming construct of IMP. Its rules are called Hoare rules  or  Floyd-Hoare  rules. Historically  R.W.Floyd  invented  rules  for  reasoning  about flow  charts,  and later  C.A.R.Hoare modified  and extended these to give  a  treatment of a  language like IMP but with procedures.  Originally their approach was advocated not just for  proving  properties of programs  but  also  as  giving  a  method for  explaining the meaning  of  program  constructs;  the  meaning  of a  construct  was  specified  in  terms  of "axioms"  (more accurately rules)  saying how  to prove properties of it.  For  this  reason, the approach is  traditionally called axiomatic semantics.

For now let's not be too formal.  Let's look at the program and reason informally about it, for  the moment based on our intuitive understanding of how it behaves.  Straigr  taway we  see  that  the  commands S := 0; N := 1 initialise  the  values  in  the locations. So  we can annotate our program with a  comment:

<!-- formula-not-decoded -->

with the understanding that S = 0 for  example means the location S has value 0,  as  in the treatment  of boolean expressions.  We  want  a  method to justify the final  comment in:

<!-- formula-not-decoded -->

-meaning that if S = 0 1\ N = 1  before  the  execution  of the  while-loop  then S = 2:1:5m90o m  after its execution.

Looking at the boolean, one fact we know holds after the execution of the while-loop is that we cannot have N =I101;  because if we  had -.(N = 101)  then the while-loop would have continued running.  So,  at the end of its execution we know N = 101.  But we want to know S!

Of course,  with a  simple  program like  this  we  can look  and see what the values  of S and N are the first  time round the loop, S = 1, N = 2.  And the second time round the loop S = 1 + 2, N = 3 ... and so  on,  until we see the pattern:  after the i th time round the loop S = 1 + 2 + ... +  i and N = i + 1.  From which we see,  when we  exit the loop, that S = 1 + 2 + ... + 100,  because when we exit N = 101.

At the beginning and end of each iteration of the while-loop we  have

<!-- formula-not-decoded -->

which expresses  the  key  relationship  between  the value  at  location  S  and  the value  at location  N.  The  assertion  I  is  called  an invariant of the while-loop  because  it  remains true under each iteration of the loop.  So finally when the loop terminates I will  hold at the end.  We  shall say more about invariants later.

For now it appears we  can base a  proof system on assertions of the form

<!-- formula-not-decoded -->

where A and B are assertions like those we've already seen in Bexp and c is a command. The precise interpretation of such a  compound assertion is  this:

for  all states 1.7 which satisfy A if the execution c from state 1.7 terminates in state 1.7' then 1.7' satisfies B.

Put another way, {A}c{B} means that any successful (i.e., terminating)  execution of c from  a  state satisfying A ends up in a  state satisfying B. The assertion A is  called  the precondition and B the postcondition of the partial correctness assertion {A}c{B}.

Assertions of the form {A }c{  B} are called partial  correctness assertions because they say nothing about the command c if it fails to terminate.  As an extreme example consider

## c == while true do skip.

The execution of c from  any state does  not terminate.  According to the interpretation we  give  above the following  partial correctness assertion is  valid:

## { true} c{ false}

simply because the execution of c does not terminate.  More generally,  because c loops, any partial correctness  assertion {A }c{ B} is  valid. Contrast  this  with  another  notion, that of total correctness.  Sometimes people write

<!-- formula-not-decoded -->

to mean that the execution of c from any state which satisfies A will terminate in a state which  satisfies B. In this  book we  shall  not  be  concerned  much  with total  correctness assertions.

Warning: There are several different  notations around for  expressing partial and total correctness.  When dipping into a  book make doubly sure which notation is used there.

We  have  left  several  loose  ends. For one,  what  kinds  of  assertions A and B do  we allow in partial correctness assertions {A}c{B}? We say more in a moment, and turn to a  more general issue.

The next  issue  can  be  regarded  pragmatically as one of notation,  though  it  can  be viewed  more conceptually as the semantics of assertions for  partial correctness--see the "optional"  Section  7.5  on denotational semantics using  predicate transformers. Firstly let's  introduce an abbreviation to mean the state 1.7 satisfies assertion A, or equivalently the assertion A is  true at state 1.7. We abbreviate this to:

Of course,  we'll need to define it, though we  all have an intuitive idea of what it means. Consider our interpretation of a  partial correctness assertion {A}c{B}. As  a  command c  denotes  a  partial  function  from  initial  states  to  final  states,  the  partial  correctness assertion means:

<!-- formula-not-decoded -->

It is  awkward working so often with the proviso that C[c]a is  defined.  Recall Chapter 5 on the denotational semantics of IMP. There we  suggested that we  use the symbol  J.. to represent an undefined state (or more strictly, null information about the state).  For a  command c we can write C[c]a = J..  whenever C[c]a is  undefined,  and,  in accord with the composition of partial functions,  take C[c]J..  =  J... If we  adopt  the convention that J..  satisfies  any  assertion,  then  our  work  on  partial  correctness  becomes  much  simpler notationally.  With the understanding that

for  any assertion A, we  can describe the meaning of {A}c{B} by

<!-- formula-not-decoded -->

Because  we  are  dealing  with  partial  correctness  this  convention  is  consistent  with  our previous interpretation of partial correctness assertions.  It's quite intuitive too; diverging computations denote J..  and as we've seen they satisfy any postcondition.

## 6.2 The assertion language Assn

What kind of assertions  do  we  wish  to  make  about IMP programs?  Because we  want to reason  about  boolean expressions we'll certainly need to include all the assertions  in Bexp. Because we want to make assertions using the quantifiers  "Vi· ..  "  and  ":li· ..  "  we will  need to work with extensions of Bexp and  Aexp which include integer variables i over which we can quantify.  Then, for example, we can say that an integer k is  a mUltiple of another 1 by writing

<!-- formula-not-decoded -->

It will be shown in reasonable detail how to introduce integer variables and quantifiers for a particular language of assertions Assn.  In principle, everything we'll do with assertions can be done in  Assn-it is  expressive  enough-but in  examples  and exercises  we  will extend Assn in various ways, without being terribly strict about it.  (For instance, in one example we'll use the notation n! = n x (n -1)  x  ... x  2 x  1 for  the factorial function.)

Firstly, we extend Aexp to include integer variables i, j, k, etc  .. This is done simply by extending the BNF description of Aexp by the additional rule which makes any integer variable i, j, k, ... an integer expression.  So  the extended syntactic category Aexpv of arithmetic expressions is  given by:

<!-- formula-not-decoded -->

n ranges over numbers, N

X ranges over locations, Loc

i ranges over integer variables, Intvar.

We extend boolean expressions  to include these  more general  arithmetic expressions and quantifiers,  as well  as implication.  The rules are:

<!-- formula-not-decoded -->

We call the set of extended boolean assertions, Assn.

At school we have had experience in manipulating expressions like those above, though in  those days we  probably wrote mathematics down in a less abbreviated way,  not using quantifiers  for  instance. When  we  encounter  an  integer  variable i we  think  of  it  as standing for  some  arbitrary  integer  and  do  calculations  with  it  like  those  "unknowns" x, y,' .. at school.  An implication like Ao =&gt; Al means if Ao then AI, and will  be true if either Ao is  false  or Al is  true.  We have used implication before in our mathematics, and now we  have added it to our set of formal  assertions Assn. We have a  "commonsense" understanding of the  expressions  and assertions  (and  this  should  be  all  that  is  needed when  doing  the  exercises). However,  because  we  want  to  reason  about  proof systems based on assertions, not just examples, we shall be more formal,  and give a theory of the meaning of expressions and assertions with integer variables.  This is part of the predicate calculus.

## 6.2.1 Free and bound variables

We sayan occurrence of an integer variable i in an assertion is bound if it  occurs  in  the scope of an enclosing quantifier Vi  or ::li. If it is  not bound we say it is free. For example, in

<!-- formula-not-decoded -->

the  occurrence of the integer  variable i is  bound,  while  those  of k and I are  free-the variables k and I are  understood  as  standing for  particular integers  even  if we  are  not

where precise  about  which. The same  integer variable  can  have  different  occurrences  in  the same assertion one of which is  free  and another bound.  For example, in

<!-- formula-not-decoded -->

the  first  occurrence  of i is  free  and the second  bound,  while  the sole  occurrence of j is free.

Although this informal explanation will probably suffice,  we  can give  a  formal  definition  using  definition  by  structural induction. Define  the  set FV(a) of free  variables  of arithmetic expressions,  extended by integer variables, a E  Aexpv, by structural induction

<!-- formula-not-decoded -->

for  all n E  N, X E  Loc, i E  Intvar,  and ao, al  E  Aexpv. Define  the  free  variables FV(A) of an assertion A by structural induction to be

<!-- formula-not-decoded -->

for  all aO,aI E  Aexpv, integer variables i and assertions Ao,Al,A. Thus we  have made precise the notion of free  variable.  Any variable which occurs in an assertion A and yet is  not  free  is  said to be bound.  An assertion with no free  variables is closed.

## 6.2.2 Substitution

We can picture an assertion A as

<!-- formula-not-decoded -->

say,  with  free  occurrences  of the  integer variable  i. Let a be an  arithmetic expression, which for simplicity we  assume contains no integer variables.  Then

<!-- formula-not-decoded -->

is  the  result  of substituting a for  i. If a contained  integer  variables  then  it  might  be necessary  to  rename  some  bound  variables  of A in  order  to  avoid  the  variables  in a becoming bound by quantifiers in A-this is  how it's done for  general substitutions.

We describe substitution more precisely in the simple case.  Let i be an integer variable and a be an arithmetic expression without integer variables, and firstly define substitution into arithmetic expressions by the following structural induction:

<!-- formula-not-decoded -->

where n is a number, X a location, j is an integer variable with j =f:. i and ao, al  E Aexpv. Now we define substitution of a for i in assertions by structural induction-remember a does not have any free variables so we need not take any precautions to avoid its variables becoming bound:

<!-- formula-not-decoded -->

where ao, al  E Aexpv, Ao, Al and A are  assertions  and j is  an  integer  variable  with j =f:. i.

As  was mentioned, defining substitution A[a/i] in the case  where a contains free  variables  is  awkward  because it  involves  the renaming of bound variables.  Fortunately we don't need this more complicated definition of substitution for  the moment.

We use the same notation for substitution in place of a  location X, so if an assertion A == ---X -- then A[a/X] = ---a --,  putting a in place of X. This time the (simpler)  formal  definition is  left  to the reader.

Exercise 6.1 Write down an assertion A E Assn with one free integer variable i which expresses that i is  a  prime number, i.e. it is  required that:

<!-- formula-not-decoded -->

Exercise 6.2 Define a formula LCM E Assn with free integer variables i, j and k, which means  "i is  the least common multiple of j and k,"  i.e. it  is  required that:

U  1=1 LCM iff I(k) is  the least  common multiple of I(i) and I(j).

(Hint:  The least  common  multiple of two numbers is  the smallest  non-negative integer divisible  by both.) 0

## 6.3 Semantics of assertions

Because arithmetic expressions have been extended to include integer variables, we  cannot  adequately  describe  the  value  of one  of these  new  expressions  using  the  semantic function A of earlier. We  must  first  interpret  integer  variables  as  particular  integers. This is  the role of interpretations.

An interpretation is  a  function  which assigns an integer to each integer variable  i. e. a function I : Intvar ---&gt;  N.

## The meaning of expressions,  Aexpv

Now  we  can  define  a  semantic  function Av which  gives  the  value  associated  with  an arithmetic expression with integer variables in a particular state in a particular interpretation;  the  value of an expression a E Aexpv in  a  an  interpretation I and a  state u  is written as Av[a]Iu or equivalently as (Av[a](I))(u). Define,  by structural induction,

<!-- formula-not-decoded -->

The definition of the semantics of arithmetic expressions with integer variables extends the denotational semantics given in Chapter 5 for  arithmetic expressions without them.

Proposition 6.3 For  all a E Aexp (without  integer variables),  for  all  states u and for all  interpretations I

<!-- formula-not-decoded -->

Proof: The proof is a simple exercise in structural induction on arithmetic expressions.

o

## The meaning of assertions, Assn

Because  we  include  integer  variables,  the  semantic  function  requires  an  interpretation function  as  a  further  argument. The  role  of  the  interpretation  function  is  solely  to provide a  value in N  which is  the interpretation of integer variables.

Notation: We use the notation I[n/i] to mean the interpretation got from interpretation I by changing the value for  integer-variable i  to n i. e.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We could specify the meanings of assertions in Assn in the same way we did for expressions  with integer variables,  but this time taking the semantic function from  assertions to functions  which,  given  an interpretation and state as  an argument,  returned  a  truth value.  We choose an alternative though equivalent course.  Given an interpretation I we define directly those states which satisfy an assertion.

In  fact,  it  is  convenient  to  extend  the  set  of states  2:; to  the  set  2:;.1  which  includes the value  1.associated with a  nonterminating computation-so 2:;.1 =def 2:; U {1.-}. For A E Assn we  define  by structural induction when

<!-- formula-not-decoded -->

for  a  state a E 2:;,  in  an  interpretation I, and then extend it so  1.pIA. The relation a pI A means  state a satisfies  A in  interpretation I, or  equivalently,  that  assertion A is  true  at  state a, in  interpretation I. By structural induction  on  assertions,  for  an interpretation I, we  define for  all a E  2:;:

<!-- formula-not-decoded -->

Note that, not 0"  FI A is  generally written as 0" A.

The above tells  us  formally  what it means for  an assertion to be true at a  state once we  decide  to  interpret  integer  variables  in  a  particular  way  fixed  by  an  interpretation. The semantics of boolean expressions provides another way of saying what it means for certain kinds of assertions  to be true or false  at a  state.  We  had  better check that  the two ways agree.

Proposition 6.4 For bE Bexp, 0" E  L;,

<!-- formula-not-decoded -->

for  any interpretation I.

Proof: The  proof  is  by  structural  induction  on  boolean  expressions,  making  use  of Proposition 6.3. o

Exercise 6.5 Prove the above proposition.

Exercise 6.6 Prove by structural induction on expressions a E Aexpv that

<!-- formula-not-decoded -->

(N  ote that n occurs as an element of N  on the left and as the corresponding number in N  on  the right.)

By using the fact  above,  prove

<!-- formula-not-decoded -->

## The extension of an assertion

Let I be  an  interpretation. Often  when  establishing  properties  about  assertions  and partial correctness assertions  it  is  useful  to consider  the extension of an  assertion  with respect to I i. e. the set of states at which the assertion is  true.

Define the extension of A, an assertion, with respect  to an interpretation I to be

o

## Partial correctness assertions

A partial correctness assertion has the form

<!-- formula-not-decoded -->

where A, B E Assn and c E Com.  Note that partial correctness  assertions  are not  in Assn.

Let I be an interpretation.  Let a E  I;.L. We define  the satisfaction relation  between states and partial correctness assertions, with respect to I, by

for  an interpretation I. In other words,  a  state a satisfies a  partial correctness assertion {A}c{B}, with respect to an interpretation I, iff any successful computation of c from a ends up in a state satisfying B.

## Validity

Let I be an interpretation.  Consider {A}c{B} .  We are not so  much interested in this partial correctness assertion  being true at a  particular state so  much as  whether or not it is  true at all  states  i. e.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

expressing that the partial correctness assertion is valid with respect to the interpretation I, because {A  }c{ B} is  true regardless of which state we  consider.  Further, consider e.g.

<!-- formula-not-decoded -->

We  are  not  so  much  interested  in  the  particular  value  associated  with i by  the  interpretation I. Rather  we  are  interested  in  whether  or  not  it  is  true  at  all  states  for  all interpretations I. This motivates the notion of validity. Define

<!-- formula-not-decoded -->

to mean for  all interpretations I and all states a

<!-- formula-not-decoded -->

When F {A}c{B} we say the partial correctness assertion {A}c{B} is valid.

which we  can write as Similarly  for  any  assertion A, write  F A iff  for  all  interpretations I and  states a, a F' A. Then say A is valid.

Warning: Although closely related, our notion of validity is not the same as the notion of validity generally met in a standard course on predicate calculus or "logic programming." There  an  assertion  is  called  valid  iff  for  all  interpretations  for  operators  like +, x···, numerals  0, 1,···, as well as free  variables,  the  assertion  turns out  to  be true. We  are not interested in arbitrary interpretations in this general sense because IMP programs operate  on  states  based  on  locations  with  the  standard  notions  of integer  and  integer operations.  To  distinguish the notion of validity  here from  the more general  notion  we could call our notion arithmetic-validity, but we'll omit the  "arithmetic."

Example:  Suppose F (A::::}  B). Then for  any interpretation I,

<!-- formula-not-decoded -->

.

i. e. A I B'. In a  picture:

<!-- image -->

So F (A::::}  B) iff for  all  interpretations I, all  states which satisfy A also  satisfy B. 0

Example:  Suppose  F {A}c{B}. Then for  any interpretation I,

<!-- formula-not-decoded -->

i.e. the image of A under C[c]  is  included in B  i.e.

<!-- image -->

In a  picture:

So F {A}c{B} iff  for  all  interpretations J, if c is  executed from  a state which satisfies A then if its execution terminates in a  state that state will satisfy B. 1 0

Exercise 6.7  In an earlier exercise it was  asked  to write down  an assertion A E  Assn with  one  free  integer  variable i expressing that i was  prime. By  working  through  the appropriate  cases  in  the  definition  of the  satisfaction  relation F I between  states  and assertions,  trace out the argument that FI A iff J(i) is  indeed  a  prime number. 0

## 6.4 Proof rules for  partial correctness

We present proof rules which generate the valid partial correctness assertions.  The proof rules  are  syntax-directed;  the  rules  reduce  proving  a  partial  correctness  assertion  of a compound command to proving partial correctness assertions of its immediate subcommands.  The proof rules are often called Hoare  rules and the proof system, consisting of the collection of rules, Hoare  logic.

Rule for skip:

Rule for  assignments:

Rule for sequencing:

Rule for  conditionals:

Rule for while  loops:

Rule  of consequence:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

IThe picture suggests,  incorrectly, that the extensions of assertions .4 1  and Bl are disjoint;  they will both always contain 1., and perhaps have other states in common.

Being rules, there is  a notion of derivation for  the Hoare rules.  In this context the Hoare rules  are  thought of as  a  proof system,  derivations are  called proofs and any conclusion of a  derivation a theorem. We shall write f-{A}c{B} when {A}c{B} is  a  theorem.

The rules  are  fairly  easy  to  understand,  with  the  possible  exception  of the  rules  for assignments and while-loops. If an assertion is  true of the state before the execution of skip it is  certainly true afterwards as  the state is  unchanged.  This is  the content of the rule for skip.

For the moment, to convince that the rule for assignments really is the right way round, it  can  be  tried  for  a  particular  assertion  such  as X = 3  for  the simple  assignment  like X  :=X +3.

The rule  for  sequential  compositions  expresses  that  if {A}co{C} and {C}cdB} are valid  then  so  is {A}co; Cl {B}: if a  successful  execution  of Co  from  a  state satisfying A ends  up  in  one  satisfying C and  a  successful  execution  of c 1 from  a  state satisfying C ends up  in  one satisfying B, then  any successful  execution  of Co  followed  by  Cl  from  a state satisfying A ends up in one satisfying B.

The two premises in the rule for  conditionals cope with two arms of the conditional.

In the rule for while-loops while b do c,  the assertion A is called the invariant because the premise,  that {A 1\  b  }c{  A} is  valid,  says  that  the  assertion A is  preserved  by  a  full execution of the body of the loop,  and in a  while loop such executions only  take place from states satisfying b. From a state satisfying A either the execution of the while-loop diverges or a  finite  number of executions of the body are  performed,  each  beginning in a state satisfying b. In the latter case,  as A is  an invariant the final state satisfies A and also -,b on exiting the loop.

The consequence rule is  peculiar because the premises include valid implications.  Any instance of the  consequence  rule  has  premises  including ones  of the  form  1= (A '* A') and  1= (B' '* B) and  so  producing  an  instance  of  the  consequence  rule  with  an  eye to  applying  it  in  a  proof  depends  on  first  showing  assertions (A '* A ') and (B' '* B) are  valid. In  general  this  can  be  a  very  hard  task-such  implications  can  express complicated facts  about arithmetic.  Fortunately, because programs often do not involve deep  mathematical  facts,  the demonstration  of these  validities  can  frequently  be  done with elementary mathematics.

## 6.5 Soundness

We  consider for  the Hoare rules  two very general properties of logical systems:

Soundness: Every rule should preserve validity,  in the sense  that if the assumptions in  the  rule's  premise  is  valid  then  so  is  its  conclusion. When this  holds  of a  rule  it  is called sound. When  every  rule  of a  proof system  is  sound,  the  proof system  itself  is said  to  be sound. It follows  then  by  rule-induction  that  every  theorem  obtained  from the proof system of Hoare rules is  a  valid partial correctness assertion.  (The comments which follow  the rules are informal arguments for  the soundness of some of the rules.)

Completeness: Naturally we would like the proof system to be strong enough so that all  valid  partial correctness  assertions  can  be obtained as  theorems.  We  would like  the proof system to be complete in  this sense.  (There are some subtle issues here which we discuss  in the next chapter.)

The proof of soundness of the rules depends on some facts about substitution.

Lemma 6.8 Let I  be  an interpretation.  Let a, ao E  Aexpv. Let X  E  Loc. Then for all interpretations I  and states (J

<!-- formula-not-decoded -->

Proof:  The proof is  by structural induction on ao--¤

xercise! o

Lemma 6.9 Let I  be  an  interpretation.  Let B E Assn, X E Loc and a E Aexp. For all  states (J E I;

<!-- formula-not-decoded -->

Proof:  The proof is  by structural induction on B--¤

xercise! o

Exercise 6.10  Provide the proofs for  the lemmas above. o

Theorem 6.11 Let {A}c{B}  be  a partial correctness  assertion. Iff-- {A}c{B}  then 1= {A}c{B}.

Proof:  Clearly  if we  can  show  each  rule  is  sound  (i. e. preserves  validity  in  the  sense that if its  premise consists  of valid  assertions and  partial correctness assertions then so is  its  conclusion)  then by  rule-induction we  can see  that every theorem is  valid.

The  rule  for skip: Clearly f= {A}skip{A} so the rule for  skip is sound.

The  rule  for  assignments: Assume  c == (X := a). Let I be an interpretation.  We  have (11=1  B[a/X] iff B, by Lemma 6.9.  Thus

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

and hence  1= {B[a/X]}X:= a{B}, showing the soundness of the assignment rule.

The  rule  for  sequencing: Assume  1= {A}c{}OC and  1= {C}c{}lB. Let I be  an  interpretation. Suppose (I 1=1 A. Then 1=1 C  because  1=1 {A }chOC. Also 1=1 B because  1=1 {C}ch1B. Hence  1= {A}co; C1 {B}.

The  rule  for  conditionals: Assume  1= {A 1\  b}co{B} and  1= {A 1\  -,b}cI{B}. Let I be an  interpretation. Suppose (I 1= I A. Either (I 1=1 b or (I 1=1 -,b. In the  former  case (11=1  Al\b so C[co](I 1=1 B, as  1=1 {Al\b}co{B}. In the latter  case (11=1  AI\-,b so 1=1 B, as  1=1 {A 1\  -,b}C1 {B}. This ensures  1= {A}if b then Co else C1 {B}.

The  rule  for  while-loops: Assume  1= {A 1\  b}c{A},  i.e.  A is  an invariant of

<!-- formula-not-decoded -->

Let I be an interpretation.  Recall that =  UnEw On where

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

We shall show by mathematical induction that Pen) holds where

<!-- formula-not-decoded -->

for  all nEw. It then follows  that

for  all  states (I, and hence that  1= {A}w{A 1\ -,b}, as  required.

Base case n =  0:  When n =  0, 0 0 =  0 so  that induction hypothesis P(O) is  vacuously true.

Induction Step:  We assume the induction hypothesis Pen) holds for n :::: ° and attempt to prove Pen + 1).  Suppose ((I, (I') E On+1 and (I 1=1 A. Either

- (i) 13[b](I = true and ((I,  (I') E On 0 C[c],  or
- (ii) 13[b](I = false and (I' =
- (I.

<!-- formula-not-decoded -->

We show in either case that a ' 1=1 A A ---,b.

Assume (i).  As 8[b]a = true we  have a 1=1 b and hence a 1=1 A A b. Also (a, a") E C[c] and (a", u ' ) E en for  some state a". We obtain a" 1=1 A, as  1= {A A b  }c{  A}. From the assumption P(n), we  obtain u' 1=1 A A ---,b.

Assume (ii).  As 8[b]a = false we  have a 1=[ ---,b and hence a 1=1 A A ---,b. But a ' = a.

This  establishes  the  induction  hypothesis P(n + 1). By  mathematical  induction we conclude P(n) holds for  all n. Hence the rule for  while loops is  sound.

The  consequence  rule: Assume  1= (A =} A') and  1= {A'}C{B'} and  1= (B' =} B). Let I be an interpretation.  Suppose u 1=1 A. Then a 1=1 A', hence  C[c]a  1=1 B' and  hence C[c]a 1=1 B. Thus  1= {A}c{B}. The consequence rule is  sound.

By rule-induction, every theorem is  valid. o

Exercise 6.12 Prove  the  above  using  only  the  operational  semantics,  instead  of  the denotational semantics.  What proof method is  used for  the case of while-loops? 0

## 6.6 Using the Hoare rules-an example

The  Hoare  rules  determine  a  notion  of formal  proof of partial  correctness  assertions through  the  idea of derivation. This  is  useful  in  the  mechanisation  of  proofs. But  in practice,  as  human  beings  faced  with  the  task of verifying  a  program,  we  need  not  be so  strict  and  can  argue  at  a  more  informal  level  when  using  the  Hoare  rules. (Indeed working with the more formal  notion of derivation might well  distract  from  getting the proof; the task of producing the formal derivation should be delegated to a proof assistant like  LCF or  HOL  [74],  [43].)

As an example we show in detail how to use the Hoare rules to verify that the command

<!-- formula-not-decoded -->

does indeed compute the factorial function n! = n x (n -1)  x (n -2)  x  ... x  2 x  1,  with O! understood to be 1,  given that X = n, a  nonnegative number, and Y = 1 initially.  2

More precisely,  we  wish to prove:

<!-- formula-not-decoded -->

To  prove  this  we  must  clearly  invoke  the  proof rule  for  while-loops  which  requires  an invariant.  Take

<!-- formula-not-decoded -->

2For this example, we imagine our syntax of programs and assertions to be extended to include&gt; and the factorial  function  which strictly speaking do  not  appear in  the boolean and arithmetic  expressions defined earlier.

We show f is  indeed an invariant  i. e.

<!-- formula-not-decoded -->

From the rule for  assignment we have

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where f[(X -1)/ Xl == (Y x (X -I)!  = n! A (X -1) 0).  Again by the assignment rule:

<!-- formula-not-decoded -->

Thus, by the rule for  sequencing,

<!-- formula-not-decoded -->

Clearly

<!-- formula-not-decoded -->

Thus by the consequence rule

<!-- formula-not-decoded -->

establishing that f is  an invariant.

Now applying the rule for  while-loops we  obtain

<!-- formula-not-decoded -->

Clearly (X = n) A (n 0) A (Y = 1)  =} f, and

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus by the consequence rule we conclude

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

There are a couple of points to note about the proof given in the example.  Firstly, in dealing with a chain of commands composed in sequence it is generally easier to proceed

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

in  a  right-to-left manner because the rule for  assignment is  of this nature.  Secondly, our choice  of I may seem  unduly strong.  Why did we  include the  assertion  X  ;::::  0  in  the invariant?  Notice where it was used,  at  (*),  and without  it we  could  not have  deduced that on exiting the while-loop the value of X  is  O. In getting invariants to prove  what we  want  they  often  must  be  strengthened. They  are  like  induction  hypotheses. One obvious way to strengthen an invariant is to specify the range of the variables and values at  the  locations  as  tightly  as  possible. Undoubtedly,  a  common  difficulty  in examples is  to  get  stuck  on  proving  the  "exit  conditions". In  this  case,  it  is  a  good  idea  to  see how  to strengthen  the  invariant  with  information  about  the  variables  and  locations  in the boolean expression.

Thus it is  fairly  involved to show even trivial programs are correct.  The same is true, of course, for  trivial bits of mathematics, too,  if one spells out all the details in a  formal proof system.  One point of formal proof systems is that proofs of properties of programs can be automated as in e.g. [74][41]-see also Section 7.4 on verification conditions in the next chapter.  There is another method of application of such formal proof systems which has  been  advocated  by  Dijkstra  and  Gries  among others,  and  that  is  to  use  the  ideas in  the study of program correctness in  the design  and development of programs.  In his book  "The Science of Programming"  [44],  Gries says

"the study of program correctness proofs has led to the discovery and elucidation of methods for  developing programs.  Basically, one attempts to develop a program and its proof hand-in-hand, with the proof ideas leading the way!"

See  Gries'  book for  many interesting examples of this approach.

Exercise 6.13 Prove,  using the  Hoare  rules,  the  correctness  of the  partial correctness assertion:

<!-- formula-not-decoded -->

Exercise 6.14 Find an appropriate invariant  to  use  in  the  while-rule  for  proving  the following  partial correctness assertion:

<!-- formula-not-decoded -->

Exercise 6.15 Using the Hoare rules,  prove that for  integers n, m,

<!-- formula-not-decoded -->

where c is  the while-program

<!-- formula-not-decoded -->

with the understanding that Y  /2 is the integer resulting from  dividing the contents of Y by 2,  and even(Y) means the content of Y  is  an even number.

(Hint:  Use mn = Z x X Y as the invariants.)

## Exercise 6.16

- (i)  Show  that  the  greatest  common  divisor,  gcd(n, m)  of  two  positive  numbers n, m satisfies:

<!-- formula-not-decoded -->

- (ii)  Using the Hoare rules  prove

<!-- formula-not-decoded -->

where

<!-- formula-not-decoded -->

Exercise 6.17 Provide a  Hoare rule for  the repeat construct and prove it sound.

<!-- formula-not-decoded -->

## 6.7 Further reading

The book  [44]  by  Gries  has  already  been  mentioned. Dijkstra's  "A  discipline  of programming"  [36]  has  been  very  influential. A  more  elementary  book  in  the  same  vein

0

is  Backhouse's  "Program  construction  and  verification"  [12J. A  recent  book which  is recommended is  Cohen's  "Programming in  the  1990's"  [32J. A  good  book  with  many exercises is Alagic and Arbib's  "The design of well-structured and correct programs"  [5J. An elementary treatment of Hoare logic with a lot of informative discussion can be found in  Gordon's recent book [42J.  Alternatives to this book's treatment, concentrating more on semantic  issues  than the other references,  can be found  in  de  Bakker's  "Mathematical  theory  of program  correctness"  [13J  and  Loeckx  and  Sieber's  "The foundations  of program verification"  [58J.

## 7 Completeness of the Hoare rules

In this chapter it is  discussed what it means for  the Hoare rules to be complete.  Codel's Incompleteness Theorem implies there is  no complete proof system for  establishing precisely  the  valid  assertions. The  Hoare  rules  inherit  this  incompleteness. However  by separating incompleteness of the assertion language from  incompleteness  due to inadequacies in the axioms and rules for the programming language constructs, we can obtain relative completeness in the sense of Cook.  The proof that the Hoare rules are relatively complete relies on the idea of weakest liberal precondition, and leads into a discussion of verification-condition generators.

## 1.1 Godel's Incompleteness Theorem

Look again at the proof rules for  partial correctness assertions,  and in  particular at the consequence rule.  Knowing we  have a rule instance of the consequence rule requires that we  determine  that  certain  assertions  in Assn are  valid. Ideally,  of  course,  we  would like  a  proof system of axioms  and rules  for  assertions which enabled us to prove all  the assertions  of Assn which  are  valid,  and  none  which  are  invalid. Naturally  we  would like  the  proof system  to  be effective in  the  sense  that  it  is  a  routine  matter  to  check that  something  proposed  as  a  rule  instance  really  is  one. It should  be  routine  in  the sense  that  there  is  a  computable  method  in  the  form  of a  program  which,  with  input a  real  rule  instance,  returns  a  confirmation  that  it  is,  and  returns  no  confirmation on inputs which are not rule instances, without necessarily even terminating.  Lacking such a  computable method we might well have a proof derivation without knowing it because it uses  a step we  cannot check is  a rule instance.  We  cannot claim that the proof system of Hoare  rules  is  effective  because  we  do  not  have  a  computable  method  for  checking instances of the consequence rule.  Having such depends on having a computable method to  check  that  assertions  of Assn are  valid. But  here  we  meet  an  absolute  limit. The great  Austrian  logician  Kurt  Codel  showed  that  it  is  logically  impossible  to  have  an effective  proof system  in  which  one  can  prove  precisely  the  valid  assertions  of  Assn. This remarkable result,  called Codel's Incompleteness Theorem 1  is  not so hard to prove nowadays,  if one  goes  about  it  via  results  from  the  theory of computability. Indeed a proof of the theorem, stated now, will be given in Section 7.3 based on some results from computability. Any gaps  or  shortcomings there  can be  made  up for  by  consulting the Appendix on computability and undecidability based on the language of while programs, IMP.

IThe Incompleteness Theorem is  not to be confused with Godel's Completeness Theorem which says that  the proof system for  predicate  calculus generates precisely  those  assertions which are  valid  for all interpretations.

Theorem 7.1 Cadel's Incompleteness  Theorem {1931}:

There is no  effective proof system for Assn such that the theorems coincide with the valid assertions  of Assn.

This theorem means we  cannot have an effective proof system for  partial correctness assertions.  As  F B iff F {true}skip{B}, if we had an effective proof system for  partial correctness it would reduce to an effective proof system for  assertions in Assn, which is impossible by G6del's Incompleteness Theorem.  In fact we can show there is  no effective proof system for  partial correctness assertions more directly.

Proposition 7.2 There  is  no  effective  proof system  for  partial  correctness  assertions such  that its  theorems  are  precisely  the  valid partial  correctness  assertions.

Proof:  Observe that  F {true }c{ false}  iff the command c diverges on all  states. If we had an effective proof system for partial correction assertions it would yield a computable method of confirming that a command c diverges on all states.  But this is  known  to be impossible-see Exercise A.13 of the Appendix. 0

Faced  with  this  unsurmountable  fact,  we  settle  for  the  proof system  of  Hoare  rules in  Section  6.4  even  though  we  know  it  to  be  not  effective  because  of  the  nature  of the  consequence  rule;  determining  that  we  have  an  instance of the  consequence  rule  is dependent on certain assertions being valid.  Still, we can inquire as  to the completeness of  this  system. That  it  is  complete  was  established  by  S.  Cook  in  [33]. If a  partial correctness assertion is  valid then there is  a proof of it  using the Hoare rules,  i. e. for  any partial correctness assertion {A }c{ B},

<!-- formula-not-decoded -->

though the fact that it is  a proof can rest on certain assertions in Assn being valid. It is as if in  building proofs one could consult an oracle at any stage one needs to know if an assertion in  Assn is  valid.  For this reason Cook's result  is  said  to establish the relative completeness of the Hoare rules for  partial correctness-their completeness is  relative to being  able  to  draw  from  the  set  of valid  assertions  about  arithmetic. In this  way  one tries  to  separate concerns  about  programs  and reasoning  about  them  from  concerns  to do with arithmetic and the incompleteness of any proof system for  it.

## 7.2 Weakest preconditions and expressiveness

The proof of relative completeness relies on another concept.  Consider trying to prove

<!-- formula-not-decoded -->

In order to use the rule for  composition one requires an intermediate assertion C  so that

<!-- formula-not-decoded -->

are  provable. How  do  we  know  such  an  intermediate  assertion  C  can  be  found? A sufficient  condition  is  that  for  every  command  c  and  postconditions B we  can  express their weakest precondition 2 in Assn.

Let  c  E  Com and B E  Assn.  Let I be an interpretation.  The weakest  precondition wpI[c, B] of B with respect to c in I is  defined by:

<!-- formula-not-decoded -->

It's  all  those  states  from  which  the  execution  of c either  diverges  or  ends  up  in  a  final state satisfying B. Thus if 1=1 {A}c{B} we know

<!-- formula-not-decoded -->

and vice  versa. Thus 1=1 {A }c{  B} iff A I wpI [c, Ell.

Suppose there is  an assertion Ao such that in all interpretations I,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So  we  see  why  it  is  called  the  weakest  precondition,  it  is  implied  by any  precondition which  makes  the  partial  correctness  assertion  valid. However  it's  not  obvious  that  a particular language of assertions has an assertion Ao such that A&amp; = wpI[c, B].

Definition:  Say Assn is expressive iff for  every command c and assertion B there is  an assertion Ao such that A&amp; = wpI[c, B] for  any interpretation I.

In showing expressiveness  we  will  use  G6del's (3 predicate  to  encode  facts  about  sequences of states as assertions in Assn.  The (3 predicate involves the operation a mod b which  gives  the  remainder  of a when  divided  by b. We can express  this  notion  as  an assertion in Assn.  For x = a mod b we write

2What we shall call weakest  precondition is  generally  called  weakest  liberal  precondition,  the  term weakest precondition referring to a  related notion but for  total correctness.

Then

for  any interpretation I i. e.

Define

<!-- formula-not-decoded -->

Lemma 7.3 Let f3(a,  b, i, x)  be  the  predicate  over natural numbers defined  by

<!-- formula-not-decoded -->

For any sequence no, ... ,nk  of natural numbers  there  are  natural numbers n, m such that for  all j, 0 5, j 5, k, and all x  we have

<!-- formula-not-decoded -->

Proof: The proof of this arithmetical fact is left to the reader as a small series of  exercises at the end of this section. 0

The f3 predicate is  important because with it we  can encode a  sequence of k natural numbers no," " nk  as a  pair n, m. Given n, m,  for  any  length k, we  can  extract  a sequence, viz. that sequence of numbers no, ... ,nk such that

for  0 j 5, k. Notice that the definition of f3 shows that the list no,'" ,nk is  uniquely determined by the choice of n, m.  The lemma above asserts that any sequence no, ... ,nk can be encoded in this way.

We  must  now face  a  slight  irritation.  Our states and our language of assertions  can involve negative as well as positive numbers.  We are obliged to extend Godel's f3 predicate so as to encode sequences of positive and negative numbers.  Fortunately,  this  is  easily done by encoding positive numbers as the even and negative numbers as the odd natural numbers.

Lemma 7.4 Let F(x,y)  be  the  predicate  over natural  numbers x  and positive  and  negative numbers y  given  by

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Then for any sequence no, ... ,nk of positive or negative  numbers there  are  natural numbers n, m such that for  all j, 0 ::; j ::; k,  and all x  we  have

<!-- formula-not-decoded -->

Proof: Clearly F(n, m) expresses the 1-1  correspondence between natural numbers m E wand n E  N in which even m  stand for  non-negative and odd m  for  negative numbers. The lemma follows from Lemma 7.3. 0

The predicate f3± is  expressible in Assn because f3 and F are.  To avoid introducing a further symbol, let us write f3± for the assertion in Assn expressing this predicate.  This assertion in Assn will  have free  integer variables, say n, m, j, x, understood in the same way  as  above,  i. e. n, m  encodes  a  sequence  with  jth element x. We will  want  to use other integer variables besides n, m, j, x, so we write f3± (n', m', j', x') as an abbreviation for f3± [n'/n,m'/m,j'fj,x'/x], got  by substituting the the  integer variable n' for n, m' for  m,  and so  on.  We have not give  a  formal  definition  of what it means to substitute integer  variables  in  an  assertion. The  definition  of substitution  in  Section  6.2.2  only defines substitutions A[a/i] of arithmetic expressions a without integer variables,  for  an integer  variable i in  an  assertion A. However,  as  long  as  the  variables n', m'  , l' ,x' are "fresh"  in the sense of their being distinct  and not occurring (free or bound)  in f3 ±, the same definition applies equally well to the substitution of integer variables; the assertion f3± [n' In, m' /m, j'  fj, x'  /x] is that given by f3± [n' /n][m' /m][j' fj][x' /x] using the definition of Section 6.2.2.3

Now we can show:

Theorem 7.5  Assn is  expressive.

Proof: We show by structural induction on commands c that for  all assertions B there is  an assertion w[c, B] such that for  all  interpretations I

<!-- formula-not-decoded -->

for  all  commands c.

Note that by the definition of weakest  precondition that, for I an interpretation,  the equality wpI[c, B] = w[c, B]f amounts to

<!-- formula-not-decoded -->

3To illustrate the technical problem with substitution of integer variables which are not fresh, consider the  assertion A == (:li'.  2  x  i' = i)  which  means "i is  even." The naive definition  of A[i'li] yields  the assertion  (:li'.  2  x  i' = i')  which happens to be valid,  and so certainly does  not mean  "i is  even."

holding for  all states 0-, a  fact  we  shall use occasionally in the proof.

C == skip: In this case, take w[skip, == B. Clearly, for  all states 0and interpretations

I,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

C == co; Cl :  Inductively  define w[co; Cl, Bn == w[co, W[Cl' BnDThen,  for 0E and interpretation I,

<!-- formula-not-decoded -->

C == if b then Co else Cl : Define

w[if b then Co  else Cl, B] == [(b A w[co, Bm V (-,b A W[Cl' Bn)]. Then, for 0E and interpretation I,

<!-- formula-not-decoded -->

c == while b do co: This is the one difficult  case.  For a state a and interpretation I, we have  (from Exercise 5.8)  that a E wpI[c,B] iff

<!-- formula-not-decoded -->

As  it  stands the mathematical characterisation of states a in wpI[c, B] is  not  an assertion  in  Assn;  in  particular it  refers  directly  to states ao,"', ak. However we  show how to replace  it  by an equivalent  description which  is. The first  step  is  to  replace  all references to the states ao, ... , ak by references to the values they contain at the locations mentioned  in  c  and B. Suppose  X = Xl, ... ,Xl are  the  locations  mentioned  in  c and B-the values at the remaining locations  are irrelevant to the computation.  We  make use of the following fact:

Suppose A is  an assertion in Assn which mentions only locations from  X = Xl, ... , Xl. For a state a, let  Si = a(X i ), for  1 :::; i  :::; t, and write S = Sl,"', Sl. Then

for  any  interpretation I. The  assertion A[s/ Xl is  that  obtained  by  the  simultaneous substitution of s for  X in A. This fact can be proved by structural induction (Exercise!).

Using the fact  (*)  we can convert (1)  into an equivalent assertion about sequences.  For i 2:  0,  let  Si  abbreviate Si1, ... , Sil, a  sequence in N.  We  claim: a E wpI[c, B] iff

<!-- formula-not-decoded -->

We  have used X = So to abbreviate Xl = SOl /I.  ... /I. Xl = SOL.

<!-- formula-not-decoded -->

To prove the claim we  argue that  (1)  and  (2)  are equivalent.  Parts of the argument are straightforward.  For example, it follows directly from  (*)  that, assuming state 0" i has values Si at X,

for an interpretation I. The hard part hinges on showing that assuming 0" i  and O"i+l  have values Si and Si+l, respectively, at X and agree elsewhere,  we have

for  an interpretation I. To see this we first  observe that

<!-- formula-not-decoded -->

(Why?)  From the induction hypothesis we obtain

<!-- formula-not-decoded -->

-recall that O"i E wpl [co, false]  iff Co  diverges on O"i. Consequently,

This covers the difficulties in showing (1)  and  (2)  equivalent.

Finally,  notice  how  (2)  can  be expressed in Assn, using the Godel predicate j3 ±. For simplicity assume I = 1 with X = X.  Then we  can rephrase (2)  to get: 0" E wpI[c, B] iff

0" FI VkVm,n 0.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

This  is  the  assertion  we  take  as w[c, B] in  this  case. (In  understanding this assertion compare it line-for-line with (2),  bearing in mind that j3±(n,m,i,x) means that x is  the ith element of the sequence encoded by the pair n, m.) The form of the assertion in the general case,  for  arbitrary I, is  similar,  though more clumsy,  and left to the reader.

This completes the proof by structural induction. D

As Assn is expressive for any command c and assertion B there is an assertion w[c, B] with the property that

for  any  interpretation I. Of course,  the  assertion w[c, B] constructed  in  the  proof of expressiveness above, is not the unique assertion with this property (Why not?).  However suppose Ao is  another assertion such that Al = wpI [c,  B] for  all I. Then

<!-- formula-not-decoded -->

So the assertion expressing a weakest precondition is unique to within logical equivalence. The useful key fact about such an assertion w[c, B] is  that, from the definition of weakest precondition, it is  characterised by:

<!-- formula-not-decoded -->

for  all  states a and interpretations I.

From  the expressiveness of Assn we  shall  prove  relative  completeness. First  an  important lemma.

Lemma 7.6 For c  E  Com and B E  Assn, let  w[c, B]  be  an  assertion  expressing  the weakest  precondition i. e. w[c, B] I = wpI [c, B]  (the  assertion  w[c, B]  need  not  be  necessarily that  constructed  by  Theorem 7.5 above).  Then

<!-- formula-not-decoded -->

Proof:  Let w[c, B] be an assertion which expresses the weakest  precondition of a  command c and postcondition B. We show by structural induction on c that

<!-- formula-not-decoded -->

for  all commands c.

(In  all  but the last case,  the proof overlaps with that of Theorem 7.5.)

c == skip  :  In  this  case F  w[skip, B] {::::::::&gt; B, so  f{w[skip, B]}skip{ B} by  the consequence rule.

c == (X := a) : In this case

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Thus F (w[c, B] B[a/ Xl).  Hence by the rule for  assignment with the consequence rule we  see  f-{w[c, B]}c{  B} in  this case.

c == co; Cl  : In this case,  for CT E and interpretation I,

<!-- formula-not-decoded -->

Thus F w[co; C1,  B] w[co, W[Cl, B]]. By the induction hypothesis

<!-- formula-not-decoded -->

Hence,  by the rule for  sequencing,  we  deduce

<!-- formula-not-decoded -->

By the consequence rule we get

C == if b then Co  else Cl  :  In this case,  for CT E and interpretation I,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Hence

<!-- formula-not-decoded -->

Now  by the induction hypothesis

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

So  by the consequence rule

<!-- formula-not-decoded -->

By the rule for  conditionals we  obtain I{w[e, Bne{  B} in this case.

Finally we  consider the case:

c == while b do Co  : Take A == w[e, B]. We show

- (1) 1= {A t\ b}eo{A},
- (2) 1= (A t\ .....,b) =? B.

Then, from  (1),  by the induction hypothesis we  obtain I{A t\ b}co{A}, so  that by the while-rule I{A}e{A t\ .....,b}. Continuing,  by  (2),  using the consequence  rule,  we  obtain I{A}c{B}. Now we  prove  (1)  and  (2).

- (1)  Let 0' 1=1 A  t\  b, for  an  interpretation I. Then 0' 1=1 w[e, B] and 0' 1=1 b, i.e. C[e]O'  1=1  Band 0' 1=1 b. But C[e]  is  defined so

<!-- formula-not-decoded -->

which makes C[eo; e]O' 1=1 B,  i.e. C[e](C[eo]O')  1=1 B. Therefore C[eo]O' 1=1 w[e, B],  i.e. C[eo]O' 1=1 A. Thus 1= {A t\ b}eo{A}.

- (2)  Let 0' 1=1 A t\ .....,b, for  an interpretation I. Then C[e]O' 1=1 Band 0' 1=1 .....,b. Again note C[e] =  C[if b then co; e else skip],  so C[e]O' = 0'. Therefore 0' 1=1 B. It follows that  1=1 A t\.....,b =? B. Thus 1= A t\.....,b =? B, proving (2).

This completes all the cases.  Hence, by structural induction, the lemma is  proved. 0

Theorem 7.7 The  proof system  for  partial  correctness  is  relatively  complete, i. e. for any partial correctness  assertion {A}e{B},

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

But Proof: Suppose 1= {A}c{B}. Then by the above lemma f-{w[c, B]}c{B} where w[c, B] I :::: wpI[c, B] for  any interpretation I. Thus as 1= (A =? w[c, B]), by the consequence rule, we  obtain f-{A}c{B}. 0

Exercise 7.8 (The G6del f3 predicate)

- (a)  Let no, ... ,nk be a  sequence of natural numbers and let

<!-- formula-not-decoded -->

Show that the numbers

<!-- formula-not-decoded -->

are coprime (i.e.,  gcd(Pi,pj) = 1 for i  f. j) and that ni &lt; Pi·

- (b)  Further, define
- (c) In addition, define

Show that

when 0 :::; i  :::; k.

- (d)  Finally prove lemma 3.

## 7.3 Proof of Godel's Theorem

G6del's Incompleteness Theorem amounts to the fact  that the subset of valid assertions in Assn is  not recursively enumerable (i. e.  ,  there  is  no program which given  assertions as  input  returns  a  confirmation  precisely  on the valid  assertions-see  the Appendix on computability for  a  precise definition and a  more detailed treatment).

Theorem 7.9 The  subset  of assertions  {A E Assn I 1= A}  is  not  recursively  enumerable.

<!-- formula-not-decoded -->

Show that for  all i,  0 :::; i  :::; k, there is  a  unique di , 0 :::; di &lt; Pi, such that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

o

Proof:  Suppose on the contrary that the set {A E  Assn I 1= A} is  recursively enumerable. Then there is  a  computable method  to  confirm  that  an  assertion  is  valid. This provides a  computable method to confirm that a  command c diverges on the zero-state &lt;70,  in  which each location X has contents 0:

Construct the assertion w[c, false]  as  in  the proof of Theorem 7.5.  Let X consist of all the locations mentioned in w[c, false].  Let A be the assertion w[c, false] [0/  XL obtained by  replacing the locations  by zeros. Then the divergence of c on the zero-state can  be confirmed by checking the validity of A, for  which there is  assumed to be a  computable method.

But  it  is  known  that  the  commands  c  which  diverge  on  the  zero-state  do  not  form a  recursively  enumerable set-see Theorem  A.12  in  the  Appendix. This contradiction shows {A E Assn I 1= A} to not be recursively enumerable. D

As  a  corollary we  obtain Godel's Incompleteness Theorem:

Theorem 7.10 (Theorem 7.1 restated)  (Gadel's  Incompleteness  Theorem):

There  is  no  effective  proof system for Assn such  that  its  theorems  coincide  with  the valid  assertions  of Assn.

Proof:  Assume  there were  an  effective  proof system such  that  for  an  assertion A, we have A is  provable iff A is  valid.  The proof system being effective implies that there is a computable method to confirm precisely when something is  a  proof.  Searching through all  proofs  systematically  till  a  proof of an assertion A is  found  provides  a  computable method of confirming precisely  when an assertion A is  valid.  Thus there cannot be an effective  proof system. D

Although we have stated Godel's Theorem for assertions Assn the presence of locations plays no essential role in the results.  Godel's Theorem is generally stated for  the smaller language  of  assertions  without  locations-the  language  of  arithmetic. The  fact  that the  valid  assertions  in  this  language  do  not  form  a  recursively  enumerable  set  means that  the  axiomatisation of arithmetic is  never  finished-there  will  always  be some fact about arithmetic which remains unprovable.  Nor can we  hope to have a  program which generates an infinite  list  of axioms  and effective  proof rules  so that  all  valid  assertions about arithmetic follow. If there were such a  program there would be an effective proof system for  arithmetical assertions,  contradicting Godel's Incompleteness Theorem.

Godel's result had tremendous historical significance.  Godel did not have the concepts of computability available to him.  Rather his result stimulated logicians to research different  formulations  of what  it  meant  to  be computable.  The original  proof worked  by expressing  the  concept  of provability of a  formal  system  for  assertions  as  an  assertion itself,  and  constructing  an  assertion  which  was  valid  iff  it  was  not  provable. It  should be admitted that we  have only considered Godel's First Incompleteness Theorem; there is  also  a  second which says that a formal system for  arithmetic cannot be proved free of contradiction in the system itself. It was clear to Godel that his proofs of incompleteness hinged  on  being  able  to  express  a  certain  set  of functions  on  the  natural  numbers  by assertions-the set  has come  to be  called  the primitive  recursive  functions. The realisation that a  simple extension led  to a  stable notion of computable function took some years longer, culminating in the Church-TUring thesis.  The incompleteness theorem devastated  the programme set  up  by Hilbert.  As  a  reaction  to paradoxes like  Russell's  in mathematical foundations,  Hilbert had advocated a  study of the finitistic  methods employed when reasoning within some formal system, hoping that this would lead to proofs of  consistency  and  completeness  of  important  proof  systems,  like  one  for  arithmetic. Godel's Theorem established an absolute limit on the power ot finitistic reasoning.

## 7.4 Verification conditions

In principle, the fact that Assn is expressive provides a method to reduce the demonstration that a partial correctness assertion is valid to showing the validity of an assertion in Assn; the validity of a partial correctness assertion of the form {A  }c{  B} is  equivalent to the validity of the assertion A =? w[c, B], from which the command has been eliminated. In this way,  given a theorem prover for predicate calculus we might hope to derive a theorem prover for  IMP programs.  Unfortunately,  the method we  used  to obtain w[c, B] was convoluted and inefficient, and definitely not practical.

However,  useful  automated  tools  for  establishing  the  validity  of  partial  correctness assertions can be obtained along similar lines once we  allow a little human guidance.  Let us annotate programs by assertions.  Define the syntactic set of annotated commands by:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where X is  a  location, a an  arithmetic  expression, b is  a  boolean  expression,  c, co, Cl are  annotated  commands  and D is  an  assertion  such  that  in co; {D}cl, the annotated command  Cl,  is not an  assignment. The  idea  is  that  an  assertion  at  a  point  in  an annotated command is  true whenever flow  of control reaches that point.  Thus we  only annotate a  command of the form co; CI  at  the point  where  control shifts from  Co  to  CI. lt is  unnecessary  to do this  when  Cl  is  an  assignment  X := a because  in  that  case  an annotation can be derived simply from a postcondition.  An annotated while-loop

<!-- formula-not-decoded -->

contains an assertion  D which is intended to be an invariant.

An annotated partial correctness  assertion has the form

<!-- formula-not-decoded -->

where c is  an annotated command.  Annotated commands are associated with ordinary commands,  got  by  ignoring  the  annotations. It  is  sometimes  convenient  to  treat  annotated commands as  their  associated  commands. In this  spirit,  we  sayan annotated partial correctness assertion is valid when its associated (unannotated) partial correctness assertion is.

An annotated while-loop

is  valid.  In order to ensure

<!-- formula-not-decoded -->

contains an assertion D, which we hope has been chosen judiciously so D is  an invariant. Being an invariant means that

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

is  valid,  once it is  known that D is  an  invariant,  it suffices  to show that both assertions

<!-- formula-not-decoded -->

are  valid.  A quick way to see this is  to notice that we  can derive {A }while b do c{ B} from {D 1\  b}c{D} using  the Hoare  rules  which  we  know to be sound.  As  is  clear,  not all  annotated partial correctness assertions are valid.  To be so it is sufficient to establish the  validity of certain  assertions,  called verification  conditions for  which  all  mention of commands  is  eliminated. Define  the  verification  conditions  (abbreviated  to vc) of an annotated partial correctness assertion by structural induction on annotated commands:

<!-- formula-not-decoded -->

Exercise 7.11  Prove by structural induction on  annotated commands that for  all  annotated partial correctness assertions {A }c{ B} if all assertions in vc( {A }c{ B}) are valid then {A }c{  B} is  valid. (The proof follows  the general line  of Lemma 7.6.  A  proof can be found  in  [42],  Section 3.5.) D

Thus to show the validity of an annotated partial correctness assertion it is  sufficient to show its verification conditions are valid.  In this way the task of program verification can  be passed to a  theorem  prover for  predicate calculus.  Some commercial programverification systems, like  Gypsy [41],  work in this way.

Note,  that  while  the  validity  of  its  verification  conditions  is  sufficient  to  guarantee the validity of an annotated partial correctness assertion,  it is  not  necessary.  This can occur because the invariant chosen is  inappropriate for  the pre and post conditions.  For example,  although

## {true  }while false do {false  }skip{  true}

is  certainly valid with false as an invariant, its verification conditions contain

<!-- formula-not-decoded -->

which is  certainly not a valid assertion.

We conclude this section by pointing out a  peculiarity in our treatment of annotated commands.  Two commands, built up as (Ci X := al)i X := a2 and Ci (X := ali X := a2), are understood in  essentially the same waYi  indeed in  many imperative languages they would both be written as:

<!-- formula-not-decoded -->

However  the  two  commands  support  different  annotations  according  to  our  syntax  of annotated  commands. The  first would  only  allow  possible  annotations  to  appear  in C whereas  the  second  would  be  annotated  as  Ci {D}(X := aliX := a2). The  rules for  annotations  do  not  put  annotations  before  a  single  assignment  but  would  put  an annotation in before any other chain of assignments.  This is even though it is still easily possible to derive the annotation from  the postcondition,  this  time  through  a  series  of substitutions.

Exercise 7.12  Suggest  a  way  to  modify  the  syntax of annotated  commands  and  the definition of their verification conditions to address this peculiarity, so that any chain of assignments or skip is  treated in the same way as a single assignment is  presently. D

Exercise 7.13 A larger project is  to program a  verification-condition generator (e.g.in standard ML or prolog) which, given an annotated partial correctness assertion as input, outputs a set, or list, of its verification conditions.  (See Gordon's book [42] for a program in lisp.) 0

## 7.5 Predicate transformers

This  section  is  optional  and  presents  an  abstract,  rather  more  mathematical  view  of assertions  and weakest  preconditions.  Abstractly a  command is  a  function f : L; ---&gt; L;.l from states to states together with an element .1, standing for  undefined; such functions are  sometimes  called state  transformers. They form  a  cpo,  isomorphic  to  that  of the partial functions on states, when ordered pointwise.  Abstractly, an assertion for  partial correctness is a subset of states which contains..1, so we define the set of partial correctness predicates to be

<!-- formula-not-decoded -->

We  can make predicates into a  cpo by ordering them by  reverse  inclusion.  The cpo of predicates for  partial correctness is

<!-- formula-not-decoded -->

Here,  more  information  about  the  final  state  delivered  by  a  command  configuration corresponds to having bounded it to lie within a smaller set provided its execution halts. In  particular the very  least  information  corresponds  to the element  ..1 Pred =  L; U {..1}. We shall use simply Pred(L;)  for  the cpo of partial-correctness predicates.

The weakest precondition construction determines a continuous function on the cpo of predicates-a predicate transformer. 4

Definition: Let f : ---&gt;  L;.l  be a  partial function  on states.  Define

<!-- formula-not-decoded -->

A  command  c can  be  taken  to  denote  a  state transformer C[c]  : ---&gt; L;.l  with the convention that undefined is represented by ..i.  Let B be an assertion.  According to this understanding, with respect to an interpretation I,

<!-- formula-not-decoded -->

4This term is  generally used for  the corresponding notion when considering total correctness.

Exercise 7.14  Write ST for  the cpo of state transformers [E 1- -1E1-]  and PT for  the cpo of predicate transformers  [Pred(E) Pred(E)].

Show W : ST -1PT and W is continuous (Care!  there are lots of things to check here). Show = i.e.,  W takes  the identity function  on the cpo of states to the identity function on predicates Pred(E).

<!-- formula-not-decoded -->

In the context of total correctness Dijkstra has argued that one can specify the meaning of a command as a predicate transformer [36].  He argued that to understand a command amounts to knowing the weakest precondition which ensures a given postcondition.  We do  this for  partial correctness.  As we  now have a  cpo of predicates we  also have the cpo

<!-- formula-not-decoded -->

of  predicate  transformers. Thus  we  can  give  a  denotational  semantics  of commands in  IMP as  predicate  transformers,  instead  of as  state  transformers. We  can  define  a semantic function

<!-- formula-not-decoded -->

from  commands  to  predicate  transformers. Although  this  denotational  semantics, in which  the  denotation  of  a  command  is  a  predicate  transformer  is  clearly  a  different denotational  semantics  to  that  using  partial  functions,  if  done  correctly  it  should  be equivalent  in  the  sense  that  two  commands  denote  the  same  predicate  transformer  iff they denote the same partial function.  You may like to do this as  the exercise below.

## Exercise 7.15  (Denotations as predicate transformers)

Define a semantic function

by

<!-- formula-not-decoded -->

where G : PT -PT is  given by G(p)(Q) = (b n Pt[eo] (P(Q)) U (...,b n Q). Show G is continuous.

<!-- formula-not-decoded -->

Show W(C[clJ = Pt[c] for  any command c.  Observe

<!-- formula-not-decoded -->

for  two  strict continuous functions J, J' on 2:.L. Deduce

<!-- formula-not-decoded -->

for  any commands c, c'  .

Recall the ordering on predicates.  Because it is  reverse inclusion:

<!-- formula-not-decoded -->

This suggests that if we were to allow infinite conjunctions in our language of assertions, and  did  not  have  quantifiers,  we  could  express  weakest  preconditions  directly. Indeed this is  so,  and you might like to extend Bexp by infinite conjunctions, to form another set of assertions  to replace Assn, and modify the above semantics to give an assertion, of the new kind,  which expresses the weakest precondition for  each command.  Once we have expressiveness a proof of relative completeness follows for this new kind of assertion, in  the same way as earlier in Section 7.2. 0

## 1.6 Further reading

The book  "What is  mathematical logic?"  by Crossley  et al [34]  has  an excellent  explanation of Godel's Incompleteness Theorem,  though with the details  missing. The logic texts by Kleene [54],  Mendelson [61]  and Enderton [38]  have full treatments.  A treatment aimed  at  Computer Science students is  presented in the book  [11]  by Kfoury,  Moll  and Arbib.  Cook's original proof of relative completeness in  [33]  used  "strongest postconditions"  instead of weakest preconditions; the latter are used instead by Clarke in [23]  and his  earlier  work. The paper by  Clarke has,  in addition,  some  negative  results  showing the impossibility of having sound and relatively complete proof systems for programming languages  richer  than  the  one  here. Apt's paper  [8]  provides  good orientation. Alternative presentations of the material of this chapter can be found  in  [58],  [13].  Gordon's book  [42]  contains a  more elementary and detailed treatment of verification conditions.

- [1] Abramsky,  S.,  "The lazy  lambda calculus."  In  Research  Topics  in  Functional  Programming  (ed. Turner,D.A.),  The UT Year of Programming Series,  Addison-Wesley,  1990.
2. [2J Abramsky, S.,  "Domain theory in logical form."  In IEEE Proc. of Symposium on Logic in Computer Science,  1987.  Revised version in Annals of pure and Applied Logic, 51,  1991.
3. [3J Abramsky, S.,  "A computational interpretation of linear logic."  To appear in Theoretical Computer Science.
- [4] Aczel,  P.,  "An  introduction  to  inductive  definitions."  A  chapter  in  the  Handbook  of Mathematical Logic,  Barwise, J.,  (ed),  North Holland,  1983.
5. [5J Alagic,  S.,  and Arbib,  M.,  "The design of well-structured and correct programs."  Springer-Verlag, 1978.
6. [6J Andersen, H.R.,  "Model checking and boolean graphs."  Proc. of ESOP 92, Springer-Verlag Lecture Notes in  Computer Science vo1.582,  1992.
- [7] Andersen,  H.R.,  "Local computation of alternating fixed-points."  Tehnical Report No.  260,  Computer Laboratory,  University of Cambridge,  1992.
- [8] Apt,  K.R.,  "Ten years of Hoare's Logic:  a  survey."  TOPLAS, 3,  pp.  431-483,  1981.
9. [9J Apt,  K.R,  and  Olderog,  E-R,  "Verification  of  Sequential  and  Concurrent  Programs," Springer-Verlag,  1991.
10. [10J Arbib,  M.,  and Manes,  E.,  "Arrows, structures and functors."  Academic Press,  1975.
11. [11J Kfoury,  A.J.,  Moll,  R.N. &amp; Arbib,  M.A.,  "A  programming  approach  to  computability." Springer-Verlag,  1982.
12. [12J Backhouse, R, "Program construction and verification."  Prentice Hall,  1986.
13. [13J de Bakker,  J.,  "Mathematical theory of program correctness."  Prentice-Hall,  1980.
- [14] Barendregt, H.,  "The lambda calculus, its syntax and semantics."  North Holland,  1984.
15. [15J Barr,  M.,  and Wells,  C.,  "Category theory for  computer science."  Prentice-Hall,  1990.
- [16] Berry, G., Curien, P-L., and Levy,  J-J.,  "Full abstraction for sequential languages:  the state of the art.  In  Nivat,  M.,  and  Reynolds,  J.,  (ed),  Algebraic  Methods  in  Semantics,  Cambridge University Press,  1985.
- [17] S0rensen,  B.B.,  and  Clausen,  C.,  "Adequacy results  for  a  lazy functional  language with recursive and polymophic types."  DAIMI Report, University of Aarhus, submitted to Theoretical Computer Science.
- [18] Camilleri,  J.A.,  and  Winskel,  G.,  "CCS  with  priority  choice."  Proc.  of Symposium  on  Logic  in Computer Science,  Amsterdam, IEEE, 1991. Extended version to appear in Information and Computation.
19. [19J Crole,  R,  "Programming  metalogics  with  a  fixpoint  type."  University  of Cambridge  Computer Laboratory Technical Report No.  247,  1992.
- [20] Cutland, N.J.,  "Computability:  an introduction to recursive function theory."  Cambridge University  Press,  1983.
21. [21J Bird,  R,  "Programs and machines."  John Wiley,  1976.
22. [22J Bird,  R.,  and Wadler, P.,  "Introduction to functional  programming."  Prentice-Hall,  1988.
23. [23J Clarke,  E.M.  Jr.,  "The  characterisation  problem  for  Hoare  Logics"  in  Hoare,  C.A.R  and  Shepherdson, J.C.  (eds.),  "  Mathematical logic and programming languages."  Prentice-Hall, 1985.
24. [24J Clarke,  E.M.,  Emerson,  E.A.,  and  Sistla,  A.P.,  "Automatic  verification  of finite  state concurrent sytems using temporal logic."  Proc. of 10th Annual ACM Symposium on Principles of Programming Languages, Austin,  Texas,  1983.
25. [25J Cleaveland, R.,  "Tableau-based model checking in  the propositional mu-calculus."  Acta Informatica,  27,  1990.
26. [26J Clement,  J.,  Despeyroux,  J.,  Despeyroux,  T.,  and  Kahn,  G., "A  simple  applicative  language: mini-ML."  Proc. of the 1986 ACM Conference on Lisp and Functional Programming,  1986.
27. [27J Cosmadakis,  S.S.,  Meyer,  A.R,  and  Riecke,  J.G.,  "Completeness  for  typed  lazy  languages  (Preliminary report)."  Proc.  of Symposium on Logic  in Computer Science,  Philadelphia,  USA,  IEEE, 1990.
28. [28J Despeyroux,  J., "Proof of  translation  in  natural  semantics."  Proc.  of  Symposium  on  Logic  in Computer Science,  Cambridge, Massachusetts, USA,  IEEE,  1986.
29. [29J Despeyroux,  T.,  "Typol:  a  formalism  to  implement  natural semantics."  INRIA  Research Report 94,  Roquencourt,  France,  1988.

- [30] Cleaveland,  R.,  Parrow,  J.  and  Steffen.  B.,  "The  Concurrency  Workbench."  Report  of LFCS, Edinburgh University,  1988.
- [31] Clocksin, W.F.,  and Mellish,  C.,  "Programming in PROLOG."  Springer-Verlag,  1981.
- [32] Cohen,  "Programming for  the 1990's". Springer-Verlag,  1991.
- [33] Cook, S.A.,  "Soundness and completeness of an axiom system for  program verification."  SIAM  J. Comput. 7,  pp.  70-90,  1978.
- [34] Crossley,  J.N.,  "What is  mathematical logic?."  Oxford University Press,  1972.
- [35] Davis,  M.,  "Hilbert's tenth problem is  unsolvable."  Am.Math.Monthly 80,  1973.
- [36] Dijkstra,  E.W.,  "A discipline of programming."  Prentice-Hall,  1976.
- [37] Emerson, A. and Lei, C.,  "Efficient model checking in fragments of the propositional mu-calculus." Proc. of Symposium on Logic in Computer Science,  1986.
- [38] Enderton, H.B.,  "A mathematical introduction to logic."  Academic Press,  1972.
- [39] Enderton, H.B.,  "Elements of set  theory."  Academic Press, 1977.
- [40] Girard,  J-Y.,  Lafont, Y.,  and Taylor, P.,  "Proofs and types."  Cambridge University Press, 1989.
- [41] Good,  D.l.,  "Mechanical  proofs  about  computer  programs."  in  Hoare,  C.A.R.,  and  Shepherdson, J.C.  (eds.),  "Mathematical Logic and Programming Languages."  Prentice-Hall, 1985.
- [42] Gordon,  M.J.C.,  "Programming language theory and its implementation."  Prentice-Hall, 1988.
- [43] Gordon,  M.J.C.,  HOL:  A  proof generating system for  higher-order logic,  in VLSI Specification, Verification and Synthesis, (ed.  Birtwistle, G., and Subrahmanyam, P.A.) Kluwer,  1988.
- [44] Gries,  D.,  "The science of programming."  Springer Texts and  Monographs in  Computer Science,  1981.
- [45] Hindley,  R.,  and  Seldin,  J.P,  "Introduction  to  combinators  and  lambda-calculus."  Cambridge University Press,  1986.
- [46] Godskesen, J.C., and Larsen, KG., and Zeeberg, M.,  "TAV (Tools for Automatic Verification) users manual."  Technical Report R  89-19,  Department of Mathematics and Computer Science,  Aalborg University,  1989.  Presented  at  the  workshop  on  Automated  Methods  for  Finite  State  Systems, Grenoble,  France,  June 1989.
- [47] Halmos,  P.R.,  "Naive set theory."  Litton Ed Publ.  Inc.,  1960.
- [48] Hennessy, M.C,  "Algebraic theory of processes."  MIT Press,  1988.
- [49] Hoare,  C.A.R.,  "Communicating sequential processes."  CACM, vo1.21,  No.8,  1978.
- [50] Hoare,  C.A.R.,  "Communicating sequential processes." Prentice-Hall,  1985.
- [51] Huet, G., "A  uniform  approach  to  type theory."  In  Logical  Foundations of Functional  Programming (ed.  Huet,G.),  The UT Year of Programming Series,  Addison-Wesley,  1990.
- [52] Jensen,  C.T.,  "The  Concurrency  Workbench  with  priorities."  To  appear  in  the  proceedings  of Computer Aided Verification,  Aalborg,  1991, Springer-Verlag Lecture Notes in  Computer Science.
- [53] Johnstone,  P.T.,  "Stone spaces."  Cambridge University Press,  1982.
- [54] Kleene,  S.C.,  "Mathematical logic."  John Wiley,  1967.
- [55] Kozen,  D.,  "Results on the propositional mu-calculus,"  Theoretical  Computer Science 27,  1983.
- [56] Lamport, L.,  "The temporal logic of actions." Technical Report 79,  Digital Equipment Corporation, Systems Research Center,  1991.
- [57] Larsen,  KG.,  "Proof systems for  Hennessy-Milner logic."  Proc.  CAAP,  1988.
- [58] Loeckx,  J.  and  Sieber,  K "The foundations of program verification."  John Wiley,  1984.
- [59] Manna,  Z.,  "Mathematical theory of computation."  McGraw-Hill,  1974.
- [60] Manna,  Z.,  and  Pnueli,  A.,  "How to cook  a  temporal proof system  for  your  pet language."  Proc. of 10th Annual ACM Symposium on Principles of Programming Languages,  Austin, Texas,  1983.
- [61] Mendelson, E., "Introduction to mathematical logic."  Van Nostrand, 1979.
- [62] Milner, A.J.R.G.,  "Fully abstract models of typed lambda-calculi."  Theoretical Computer Science 4,  1977.
- [63] Milner,  A.J.R.G.,  "Communication and concurrency."  Prentice Hall,  1989.
- [64] Milner,  A.J  .R.G.,  "Operational  and  algebraic  semantics  of concurrent  processes."  A  chapter  in Handbook of Theoretical Computer Science, North Holland,  1990.
- [65] Mitchell,  J.C.,  "Type systems  for  programming languages."  A  chapter in  Handbook of Theoretical  Computer Science, North Holland,  1990.

- [66] Moggi, E.,  "Categories of partial morphisms and the lambdap-calculus."  In proceedings of Category Theory and Computer Programming, Springer-Verlag Lecture Notes in Computer Science vo1.240, 1986.
- [67] Moggi, E.,  "Computational lambda-calculus and monads."  Proc. of Symposium on Logic in Computer Science,  Pacific  Grove,  California,  USA,  IEEE,  1989.
- [68] Mosses,  P.D.,  "Denotational  semantics."  A  chapter  in  Handbook  of Theoretical  Computer Science, North Holland,  1990.
- [69] Nielson.  H.R., and Nielson,  F.,  "Semantics with applications:  a  formal  introduction."  John Wiley,  1992.
- [70] inmos,  "Occam programming manual."  Prentice Hall,  1984.
- [71] Ong,  C-H.L.,  "The lazy lambda calculus:  an investigation into the foundations  of functional  programming."  PhD thesis,  Imperial College, University of London,  1988.
- [72] Parrow, J.,  "Fairness properties in process algebra."  PhD thesis,  Uppsala University, Sweden, 1985.
- [73] Paulson,L.C.,  "ML for  the working programmer." Cambridge University Press, 1991.
- [74] Paulson,  L.C.,  "Logic  and computation:  interactive proof with  Cambridge LCF."  Cambridge University Press,  1987.
- [75] Pitts, A.,  "Semantics of programming languages." Lecture notes, Computer Laboratory, University of Cambridge,  1989.
- [76] Pitts,  A., "A  co-induction  principle  for  recursively  defined  domains."  University  of Cambridge Computer Laboratory Technical  Report No.252,  1992.
- [77] Plotkin, G.D.,  "Call-by-name, Call-by-value and the lambda calculus"  Theoretical Computer Science  1,  1975.
- [78] Plotkin, G.D.,  "LCF considered as programming language."  Theoretical Computer Science 5,  1977.
- [79] Plotkin,  G.D.,  "A powerdomain construction."  SIAM J.  Comput.5,  1976.
- [80] Plotkin, G.D" "The Pisa lecture notes."  Notes for  lectures at the University of Edinburgh, extending lecture notes for  the Pisa Summerschool, 1978.
- [81] Plotkin,  G.D.,  "Structural operational semantics."  Lecture Notes,  DAIMI FN-19.  Aarhus University,  Denmark,  1981  (reprinted  1991).
- [82] Plotkin,  G.D.,  "An operational semantics  for  CSP."  In Formal Description  of Programming Concepts II, Proc.  of TC-2 Work.  Conf.  (ed.  Bj0rner,  D.),  North-Holland,  1982.
- [83] Plotkin, G.D.,  "Types and partial functions."  Notes of lectures at CSLI, Stanford University,  1985.
- [84] Prawitz,  D.,  "Natural deduction,  a  proof-theoretical study."  Almqvist &amp; WikselL  Stockholm,  1965.
- [85] Reisig,  W., "Petri  nets: an  introduction."  EATCS  Monographs  on  Theoretical  Computer Science,  Springer-Verlag,  1985.
- [86] Rogers,  H.,  "Theory  of recursive  functions  and  effective  computability." McGraw-Hill, 1967.
- [87] Roscoe,A.W., and Reed,G.M  .·  "Domains for  denotational semantics."  Prentice Hall,  1992.
- [88] schmidt, D.,  "Denotational semantics:  a  methodology for language development."  Allyn &amp; Bacon,  1986.
- [89] Scott,  D.S.,  "Lectures on a  mathematical theory of computation."  PRG Report  19, Programming Research Group,  Univ.  of Oxford,  1980.
- [90] Scott,  D.S.,  "Domains for  denotational semantics."  In proceedings of ICALP  '82,  Springer-Verlag Lecture Notes in Computer Science vo1.l40,  1982.
- [91] Scott,  D.S.,  and  Gunter, c., "Semantic  domains."  A  chapter  in  Handbook  of Theoretical Computer Science, North Holland,  1990.
- [92] Smyth, M.,  "Powerdomains."  JCSS 16(1),  1978.
- [93] Stirling,  C.  and  Walker  D.,  "Local  model  checking  the  modal  mu-calculus."  Proc.of TAPSOFT, 1989.
- [94] Stoughton, A.,  "Fully abstract models of programming languages."  Pitman, 1988.
- [95] Stoy,  J.,  "Denotational semantics:  the Scott-Strachey approach to programming language theory."  MIT Press,  1977.
- [96] Tarski, A.,  "A lattice-theoretical fixpoint  theorem and its applications."  Pacific Journal of Mathematics,  5,  1955.
- [97] Tennent, R.D.,  "Principles of programming languages."  Prentice-Hall,  1981.

- [98] Vickers, S.,  "Topology via logic."  Cambridge University Press,  1989.
- [99] Vuillemin,  J.E.,  "Proof techniques for  recursive  programs."  PhD Thesis,  Stanford  Artificial  Intelligence Laboratory,  Memo AIM-218,  1973.
- [100] Walker,  D.,  "Automated analysis of mutual exclusion algorithms  using CCS."  Formal Aspects of Computing 1, 1989.
- [101] Wikstrom, A. "Functional programming using Standard ML."  Prentice-Hall,  1987.
- [102] Winskel, G.,  "On powerdomains and modality."  Theoretical Computer Science 36,  1985.
6. (103] Winskel,  G.  and  Larsen,  K., "Using  information  systems  to  solve  recursive  domain  equations effectively."  In the proceedings of the conference on Abstract Datatypes, Sophia-Antipolis, France, Springer-Verlag Lecture Notes in Computer Science vol.l73,  1984.
- [104] Winskel, G., "Event structures."  Lecture notes for  the Advanced Course on Petri nets, September 1986, Springer-Verlag Lecture Notes in Computer Science,  vol.255,  1987.
- [105] Winskel, G., "An introduction to event structures."  Lecture  notes for  the  REX  summerschool  in temporal logic,  May 88,  Springer-Verlag Lecture Notes in Computer Science,  vol.354,  1989.
- [106] Winskel,  G.,  "A  note  on  model  checking  the  modal  nu-calculus."  Theoretical  Computer  Science 83,  1991.
- [107] Winskel, G., and Nielsen,  M.,  "Models for concurrency." To appear as a chapter in the Handbook of Logic and the Foundations of Computer Science, Oxford University Press.
- [108] Zhang,  G-Q.,  "Logic of domains."  Birkhiiuser,  1991.