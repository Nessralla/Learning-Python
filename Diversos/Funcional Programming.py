# Programação baseada em funções high order, ou seja, funções que recebem outras funções como parâmetros

# Neste primeiro exemplo, a função apply_twice executa duas vezes a função que receberá de parâmetro

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

# Functional programming seeks to use pure functions. They have no side affects on your program, because it
# does not affect other variables or objects. One example of pure function is math function cos(x), every
# time you execute cos(x) for an x, it will be the same result. Examples above:

# Pure funcion
def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

# Impure function, because it changes the variable some_list after being executed
some_list = []

def impure(arg):
  some_list.append(arg)

# Using pure functions has both advantages and disadvantages.
# Pure functions are:
# - easier to reason about and test.
# - more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
# - easier to run in parallel.

# The main disadvantage of using only pure functions is that they majorly complicate the otherwise simple task 
# of I/O, since this appears to inherently require side effects. They can also be more difficult to write in some situations.

# LAMBDA FUNÇÕES

# São funções anônimas que executam uma operação simples de uma linha, exemplo (lambda x: x*2*x)

# Mais exemplos abaixos, comparando a mesma função com nome e lambda

#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

# Lambda functions can be assigned to variables, and used like normal functions. NOT RECOMMENDED

triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))



"""MAP""" 

""" The built-in functions map and filter are very useful higher-order functions that operate on lists 
(or similar objects called iterables). The function map takes a function and an iterable as arguments, 
and returns a new iterable with the function applied to each argument."""

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

""" OR, IF WE USE LAMBDA"""

nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x+5, nums))
print(result)

"""FILTER"""

"""The function filter filters an iterable by removing items that don't match a predicate 
(a function that returns a Boolean)."""

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

"""Generators are a type of iterable, like lists or tuples.
Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops.
They can be created using functions and the yield statement.
Example:"""

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

"""Due to the fact that they yield one item at a time, generators don't have the memory restrictions of lists.
In fact, they can be infinite!"""

def infinite_sevens():
  while True:
    yield 7
        
for i in infinite_sevens():
  print(i)

"""In short, generators allow you to declare a function that behaves like an iterator, 
i.e. it can be used in a for loop."""

"""Finite generators can be converted into lists by passing them as arguments to the list function.
"""

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

"""Using generators results in improved performance, which is the result of the lazy (on demand) 
generation of values, which translates to lower memory usage. Furthermore, we do not need to wait until 
all the elements have been generated before we start to use them."""