# A) LINEAR ALGEBRA NOTES
## First, take a look at the big picture (note, part of part a!)


### [DataTypes:](https://web.archive.org/web/20210413222941/https://the-learning-machine.com/article/linear-algebra/data-types)
- Scalars
   1. greek $\alpha, \beta, \gamma$ etc for constant
   2. x, y, z, for variables
- Vectors
   1. 1-D collection of scalars
   2. $\color{yellow}a\in\mathbb{R}^n$ = [row / column vector]
   3. Transpose row to column and v.v with $\color{yellow}a = b^T$ and $\color{yellow}b = a^T$
   4. Column vector precedent
- Matrices
   - Let's stack each vector in the **set** $\color{yellow} {\{a1,…,am}\}$ such that $\color{yellow} a_i∈R^n,∀i$ as shown below and refer to the entire box by the symbol A, a matrix:
  $\color{yellow} 
  \begin{bmatrix} 
  a_{1,1} … a_{1,n} \\⋮⋱⋮\\ a_{m,1} … a_{m,n}
  \end{bmatrix}$
   - Here, $ai,j$ represents the $j$-th element of the $i$-th vector. 
   - This composite representation of multiple vectors is known as a matrix. It is a 2-dimensional data type
   - **ROW**: $\color{yellow}  
    [a_{1,1},a_{1,2},…,a_{1,n}]$ form the first **row** of the matrix **A**
   - **COLUMN**: $\color{yellow}
    [a_{1,1},a_{2,1},…,a_{m,1}]$ form the first **column** of the matrix **A**
   - **DIAGONAL** of the matrix. For example, the elements $\color{yellow}
    [a_{1,1},a_{2,2},…,a_{n,n}]$ form the **diagonal** of the `matrix A.


### [Vector geometry](http://web.archive.org/web/20210413224828/https://the-learning-machine.com/article/linear-algebra/vector-geometry): - `**warm-up**`
```
QUICK NOTES ONLY HERE
__________ see REF for full info

Lots to do and this is relatively simple

Has been covered in the Linear Algebra 
```

## Vector: a geometric perspective
- Essentially, we use geometry to represent vectors, this is super helpful 
## Vector magnitude and direction
- The magnitude of a vector is measured in terms of its **NORM**. The `p-norm`, for $\color{yellow} p≥1$, provides a generalized way of computing any `norm of a vector`.
  $$\color{yellow} ||a||p = (\sum^{n}_{i}=|a_i|^p)^{\frac{1}{p}}$$
- There are 3 well known and popular NORMS
- L1, L2, and L$\infty$
- L1: `Manhattan or Taxi-cab norm` ___ $\color{yellow} ||a||_1$
- L2: `Euclidean norm` ___ $\color{yellow} ||a||_2$
- L$\infty$: `max norm` ___ $\color{yellow} ||a||_\infty$
- ## UNIT NORM and Unit Vector:
  - A vector with unit Euclidean norm, $\color{yellow} ||a||_2=1$, is the unit vector
  - Any vector can be normalized to a unit vector by dividing it with its norm, for example, the Euclidean norm.
  - ## $\color{yellow} a = \frac{a}{∣∣a∣∣_2}$
  - ## **`a`** has the same direction as that of the original vector, but has unit-magnitude.
  - ....
  - THIS IS IMPORTANT and FUNDAMENTAL
  - ..
  - .
  - ...
  - 
- ## Stretching or shrinking a vector
  - The magnitude of the vector can be stretched or shrunk. This is achieved by multiplication with a scalar.

    $\color{yellow} \bold{b}=α\bold{a}$

    - above the unit vector `a` is stretched by $\color{yellow}\alpha$
    - `b`, is a vector with the same number of entries as `a`.
- ## Rotating a vector (see next!)
  
- ## [Linear combination of vectors](http://web.archive.org/web/20210413224828/https://the-learning-machine.com/article/linear-algebra/linear-combination-of-vectors): - `**warm-up**`
  - Suppose an object **`a`** is moving in a certain direction. Another object **`b`** strikes it, moving in another direction, not necessarily head-on.
  - `What happens?` 
    - The object changes its original trajectory
    - The new trajectory and the new speed is a result of two conditions prior to the strike.
      - `The speed of the object a relative to that of the object b`
      - `The direction of the object a with respect to that of the object b`
- Resulting vector $\color{yellow} c=αa+βb$
- 

### []()


### []()