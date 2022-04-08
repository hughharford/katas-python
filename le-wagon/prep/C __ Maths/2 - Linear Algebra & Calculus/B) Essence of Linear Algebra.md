# ESSENCE OF LINEAR ALGEBRA

## FOLLOW UPS REQUIRED:

1. Three-dimensional linear transformations

## CONTENTS

- Vectors | Chapter 1, Essence of linear algebra
- Linear combinations, span, and basis vectors | Chapter 2, Essence of linear algebra
- Linear transformations and matrices | Chapter 3, Essence of linear algebra
- Matrix multiplication as composition | Chapter 4, Essence of linear algebra
- Three-dimensional linear transformations | Chapter 5, Essence of linear algebra
- The determinant | Chapter 6, Essence of linear algebra


## Vectors | Chapter 1, Essence of linear algebra
### [Vectors](https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=1)


## Linear combinations, span, and basis vectors | Chapter 2, Essence of linear algebra
### [Linear combinations, span, and basis vectors](https://www.youtube.com/watch?v=k7RM-ot2NWY&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=2)

## Linear transformations and matrices | Chapter 3, Essence of linear algebra
### [Linear transformations and matrices](https://www.youtube.com/watch?v=kYB8IZa5AuE&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=3)
- AMAZING video
- Lines remain lines (it's Linear Transformation after all)
- The origin must remain fixed
- Think of: Keeping 2D Grid lines parallel and evenly spaced
- Only need to record **$\hat{i}$** and **$\hat{j}$** the unit vectors and everything else follows from there
- This way, an entire Linear Transformation can be described with just 4 numbers $[\frac{x}{y}]$ for $\hat{i}$ and for $\hat{j}$
- Matrix Notation:  
- $\color{yellow} M = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ 
- $\color{yellow} \hat{i} = \begin{bmatrix} x \\ y \end{bmatrix} and \space \hat{j} = \begin{bmatrix} x \\ y \end{bmatrix}$
- This is often written in a 2x2 Matrix:
  - $\color{yellow} \begin{bmatrix} a & b \\ c & d \end{bmatrix}$
  - The columns describe where each lands: $\hat{i} get a-c$ and $\hat{j} gets b-d$  
  - 90 degree rotation counterclockwise (a Linear Transformation):
  $\color{yellow} \begin{bmatrix} 
  0 & -1 \\ 
  1 & 0   \end{bmatrix}$
  - Shear (a Linear Transformation):
  $\color{yellow} \begin{bmatrix} 
  1 & 1 \\ 
  0 & 1   \end{bmatrix}$
  - Every 2x2 Matrix is a Linear Transformation of Space
- ## [Matrix multiplication as composition](https://www.youtube.com/watch?v=kYB8IZa5AuE&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=3)
  ### RECAP
  - Lines remain lines (it's Linear Transformation after all)
  - The origin must remain fixed
  - Think of: **Keeping 2D Grid lines parallel and evenly spaced**
  - Matrix vector multiplication
  - $\color{yellow} \begin{bmatrix} 
  a & b \\ 
  c & d   \end{bmatrix} * \begin{bmatrix} x \\ y \end{bmatrix} = x \begin{bmatrix} 
  a \\ 
  c \end{bmatrix} + y \begin{bmatrix} 
  b \\ 
  d \end{bmatrix} = \begin{bmatrix} 
  ax & by \\ 
  cx & dy   \end{bmatrix}$
  ### APPLYING > 1 TRANFORMATION
  - One followed by another is the composition, the result of the Transformations applied
  - Shear * Rotation = Composition
  - BUT: Read RIGHT to LEFT - as the functions are inside each other
  - $\color{yellow} M_1 * M_2:$
  - $\color{yellow} M_1 \begin{bmatrix} 
  e & f \\ 
  g & h   \end{bmatrix} * M_2 \begin{bmatrix} 
  a & b \\ 
  c & d   \end{bmatrix} = \begin{bmatrix} 
  ae + bg & af + bh \\ 
  ce + dg & cf + dh \end{bmatrix}$
  - This is applying 1 Transformation and then another
  - Does it matter what order you do them? YES => order does matter:
    - $\color{yellow} M_1 * M_2 \neq M_2 * M_1$
  - Associative?
    - Yes, Matrix Multiplication is Associative
- ## [Three-dimensional linear transformations](https://www.youtube.com/watch?v=rHLEWRxRGiM&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=5)
  - Use: 
  - $\hat{i}$
  - $\hat{j}$
  - $\hat{k}$
  - FOLLOW UP ON THIS Three-dimensional linear transformations
  - **Matrix multiplication** for two successfive transformations in space
- ## [The determinant](https://www.youtube.com/watch?v=Ip3X9LOh2dk&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=6)
  - 