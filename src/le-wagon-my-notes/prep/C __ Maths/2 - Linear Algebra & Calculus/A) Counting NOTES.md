# COUNTING
[Counting](https://web.archive.org/web/20210413231103/https://the-learning-machine.com/article/math/counting)

## CONTENTS

1. Counting: Sum rule
2. Counting: Product rule
3. Counting: Inclusion-exclusion principle
4. The pigeonhole principle
5. The generalized pigeonhole principle
6. Permutations
7. r-Permutation
8. Combinations
9. Pascal's identity (QUESTION HERE)
10. Sum of all r-combinations
11. Vandermonde's identity
12. The binomial theorem
13. Permutations with repetition
14. Combinations with repetition
15. Permutations with indistinguishable objects


- ## Counting: Sum rule
  - Consider two tasks that **cannot be done simultaneously**. If one task can be done in n ways and the other in m ways, then the total number of ways to do either of these tasks is **n+m**
    <p align="left">
    <img src="https://web.archive.org/web/20210413231103im_/https://the-learning-machine.com/static/published-articles/math/counting/assets/img/sum-rule.svg" alt="" style="width:70%; border:0; background:white;">
    </p>
- ## Counting: Product rule
  - Consider two sub-tasks that **need to be performed sequentially** to complete a task. If the first sub-task can be done in n ways and the second sub-task can be done in m ways, then the total number of ways of accomplishing the overall task is **nm**
    <p align="left">
    <img src="https://web.archive.org/web/20210413231103im_/https://the-learning-machine.com/static/published-articles/math/counting/assets/img/product-rule.svg" alt="" style="width:70%; border:0; background:white;">
    </p>
  
- ## Counting: Inclusion-exclusion principle
  - Naive Sum Rule application n/a
  - First perform the sum rule (include) and then remove those possibilities that have been counted repeatedly (exclude). This is known as the **inclusion-exclusion principle** of counting
  - $\color{yellow}|A∪B|=|A|+|B|−|A∩B|$
  - ∩ = intersection
  - ∪ = union
    <p align="left">
    <img src="https://web.archive.org/web/20210413231103im_/https://the-learning-machine.com/static/published-articles/math/counting/assets/img/inclusion-exclusion.svg" alt="" style="width:70%; border:0; background:white;">
    </p>
- ## The pigeonhole principle
  - states that if k+1 objects are placed in k containers, then at least one container has two or more objects
  - Birthday Example:
    - In a room full of 367 people, there are at least two people with the same birthday as there are only 366 possible birthdays. In this example, people are the so-called pigeons and birthdays are the so-called holes. There is at least one birthday (hole) that is shared by two or more people (pigeons)
- ## The generalized pigeonhole principle
  - If n objects are placed in k containers, then there is at least one container containing at least $\color{yellow} ⌈\frac{n}{k}⌉$ objects
  - Birthday Example:
    - Among a group of 40 people, there are at least $\color{yellow} ⌈\frac{40}{12}⌉=4$ people born in the same month, because there are only 12 possible months
  
- ## Permutations (ordered arrangement)
  - The number of ways of arranging a set of n distinct elements is $\color{yellow}n!$
  - There is no standard symbol for permutations of n objects. In mathematical literature, it is denoted as $\color{yellow} P(n,n)$ or $\color{yellow} _nP_n$. In our articles, we will use the latter to distinguish it from the notation for probability. 
  - USE: 
    - $\color{yellow} _nP_n$
- ## r-Permutation (ordered arrangement)
  - An ordered arrangement of r elements of a set is known as an **r-permutation**
  - The number of r-permutations of a set of n elements is usually denoted as $\color{yellow} _nP_r$ 
  - It can be calculated using the product rule as follows
  - $\color{yellow} _nP_r=n(n−1)(n−2)…(n−r+1)$
  - simplifies to:
  - $\color{yellow} _nP_r=\frac{n!}{(n−r)!}$
  - Example:
    - Consider arranging 3 vases on a dining table from a collection of 10 vases. There are $\color{yellow} _{10}P_3=10×9×8=720$ different ways of arranging the vases
- ## Combinations (unordered selection)
  - In permutations, order of the elements matters, in combinations, it does not.
  - See relationship with Permutations:
    <p align="left">
    <img src="https://web.archive.org/web/20210413231103im_/https://the-learning-machine.com/static/published-articles/math/counting/assets/img/combinations.svg" alt="" style="width:100%; border:0; background:white;">
    </p>
  - An r-combination is an unordered selection of r elements from a set consisting of n distinct elements, such that 0≤r≤n. It is usually denoted as $\color{yellow} C(n,r)$, $\color{yellow} _nC_r$ or succinctly as $\color{yellow} (\frac{n}{r})$, 
  - Vocalize as **"n choose r"**
  - $\color{yellow} _nC_r=\frac{nPr}{rPr}$
  - $\color{yellow} _nC_r=\frac{n!}{(n−r)!r!}$
- Example:
  - Consider selecting 3 representatives from a group of 100 people. There are $\color{yellow} C(100,3)=\frac{100!}{97!3!}=\frac{100×99×98}{3×2×1}=161,700$ possible ways of selecting the representatives.
- ## Pascal's identity
  - QUESTION HERE: Don't get the Pascal's triangle structure bit AT ALL!
  - If **n** and **r** are positive integers such that **n ≥ r** then:
  - Pascal's identity: $\color{yellow} C(n+1,r)=C(n,r−1)+C(n,r)$

- ## Sum of all r-combinations
  $$\color{yellow} \sum^{n}_{r=0} C(n,r)=2n$$
  -Proof via:
    <p align="left">
    <img src="https://web.archive.org/web/20210413231103im_/https://the-learning-machine.com/static/published-articles/math/counting/assets/img/bitstring-subset-selector.svg" alt="" style="width:80%; border:0; background:white;">
    </p>
- ## Vandermonde's identity
  - For nonnegative integers n, m, and r, such that r does not exceed n or m, it is the case that:
    $$\color{yellow} C(m+n,r)=\sum^{n}_{r=0} C(m,r−k)C(n,k)$$
  - **USE FOR**:
    - calculating the number of **r-combinations of a union of two disjoint sets**, if it is easier to calculate the r combinations of the individuals sets
  - If we need to choose **r** from **m+n** total candidates it is $\color{yellow} C(m+n,r)$
  - See proof of Vandermode's if required.
- ## The binomial theorem
  - Let **x** and **y** be variables. The sum of these two variables, **$\color{yellow} x+y$**, is known as a **binomial  expression**.
  - If **n** is some positive integer, then:
  $$\color{yellow} (x+y)^n=\sum^{n}_{j=0} C(n,j)x^{n−j}y^j$$
  ### **N.B. Full binomial theorum expansion in that section on that page.**
  - This result is known as the **binomial theorem**. It is useful in listing out the terms of powers of such binomial expressions.
  - **VERY POWERFUL: EXAMPLE**
    - Suppose we wish to find the coefficient of x3y6 in the expansion of (x+y)9. Using the binomial theorem it is easy to note that it will be C(9,6)
- ## Permutations with repetition
  - If the same element can be repeated in a permutation, then the number of r-permutations of a set of **n** elements is $\bold{n^r}$
- ## Combinations with repetition
  - If the same element can be repeated in a combination, then the number of **r-combinations** of a set of n elements is $\color{yellow} C(n+r−1,r)$
  - **Example**:
    - Suppose we wish to pack a fruit basked with oranges, apples, and mangoes such that the total number of fruits in the basket is **10**. Since in our case we have a choice of **3** fruits, so **n = 3**. The number of ways of filling up such a basket is then $\color{yellow} C(3+10−1,10)=C(12,10)$
- ## Permutations with indistinguishable objects
  - Consider the word "**BOOKKEEPER**". How many words can be generated by reordering the letters of this word? There are 10 letters, but some letters are repeated. To avoid overcounting, the frequency of each letter must be taken into account to arrive at the result.
    <p align="left">
    <img src="https://web.archive.org/web/20210413231103im_/https://the-learning-machine.com/static/published-articles/math/counting/assets/img/permutation-with-indistinguishable.svg" alt="" style="width:80%; border:0; background:white;">
    </p>
  - More generally with a collection of **n** elements including repetitions. In the collection there are $n_1$ repetitions of the element of type 1, $n_2$ of type 2, …, and $n_k$ repetitions for the type k.
  - $\color{yellow} _nP_n$
  - Imagine that all n elements were distinct then, we know that the number of possible rearrangements is $\color{yellow} _nP_n=n!$. Of these, $\color{yellow} n_1!$ permutations consist of rearrangement of the n1 repetitions of the elements of type 1. Similarly, there are $\color{yellow} n2!,n3!,…nk!$ permutations of rearrangements of the $\color{yellow} n2,n3,…,nk$ indistinguishable elements of types 2,3,…,k
  - Thus, the number of different permutations of n elements containing groups of indistinguishable objects is:
  $$\color{yellow} \frac{n!}{n1!n2!…nk!}$$
- ## Distributing objects into distinguishable boxes
  - I.e. the task of placing **n** distinguishable objects in **k** distinguishable boxes. How many ways to achieve this? 
  - Imagine all the objects lined up from left-to-right. The first $n_1$ objects are assigned to first box, the next $n_2$ to the second, and so on. 
      <p align="left">
    <img src="https://web.archive.org/web/20210413231103im_/https://the-learning-machine.com/static/published-articles/math/counting/assets/img/distribute-in-boxes.svg" alt="" style="width:80%; border:0; background:white;">
    </p>
  - the number of ways to distribute $n$ distinguishable objects into $k$ distinguishable boxes, so that $n_i$ objects are placed into the box $i$, for $i=1,2,…,k$ equals:
  - $$\color{yellow}\frac{n!}{n1!n2!…nk!}$$
  - **Example**:
    - Consider a 4-player card game that involves distributing **8** cards to each player from a standard **52 card deck**. To count the number of ways this can be accomplished, know that there are **5 total "boxes"** that we need to distribute the cards into. One for each player to hold their 8 cards and one for the remaining **52 − 4 × 8 = 20** cards. Thus, the number of ways is then:
  $$\color{yellow} \frac{52!}{8!8!8!8!20!}$$