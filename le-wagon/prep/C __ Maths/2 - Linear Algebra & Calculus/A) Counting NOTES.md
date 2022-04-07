# COUNTING
[Counting](https://web.archive.org/web/20210413231103/https://the-learning-machine.com/article/math/counting)

## CONTENTS

1. Counting: Sum rule
2. Counting: Product rule
3. Counting: Inclusion-exclusion principle
4. The pigeonhole principle
5. The generalized pigeonhole principle


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
  - 