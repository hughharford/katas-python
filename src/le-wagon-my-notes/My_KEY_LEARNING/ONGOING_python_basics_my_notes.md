# CONTENTS

NOT QUITE WORKING:
<a href="Python Comprehensions (for Lists)">**Python Comprehensions (for Lists)**</a>

## - Python Comprehensions (for Lists)
## - Operator precedence with NOT AND & OR behaviour
## - IMMUTABLE and MUTABLE Python datatypes
____


# Python Comprehensions (for Lists)
REF: https://www.freecodecamp.org/news/the-python-handbook/#listcomprehensionsinpython
### Better here:
REF: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

```Python
data = [1,2,3,4,5,6]
comp = [(ele - 0.1)**2 for ele in data if ele > 3]
```
gives:
>    [15.209999999999999, 24.010000000000005, 34.81]


# Operator precedence with NOT AND & OR behaviour
## and & or in comparative expressions
REF: https://docs.python.org/3/reference/expressions.html#operator-precedence

**not**  ___  **and** ___ && ___  **or** return specific values based on:

The operator **not** yields True if its argument is false, False otherwise.

The expression x **and** y first evaluates x; if x is false, its value is returned; otherwise, y is evaluated and the resulting value is returned.

The expression x **or** y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.

Note that neither **and** nor **or** restrict the value and type they return to False and True, but rather return the last evaluated argument.

## This is sometimes useful:
 e.g., if s is a string that should be replaced by a default value if it is empty, the expression s or 'foo' yields the desired value. Because not has to create a new value, it returns a boolean value regardless of the type of its argument (for example, not 'foo' produces False rather than ''.)


# IMMUTABLE and MUTABLE Python datatypes
REF: https://towardsdatascience.com/https-towardsdatascience-com-python-basics-mutable-vs-immutable-objects-829a0cb1530a

## IMMUTABLE
# Good for managing scope and variable "rights"

1. int
2. float
3. decimal
4. bool
5. string
6. tuple
7. range


## MUTABLE

1. list
2. dictionary
3. set
4. user-defined classes
