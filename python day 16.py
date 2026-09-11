
Lambda fuction (or) anonymus fuction :-
-----------------------------------

--> Lambda fuction is a small anonymous fuction
--> Lambda can take n number of arguments, but only with one expression
--> the fuction is defined by using lambda keyword

syntax --> lambda agruments : expression

eg:-

add_ = lambda a,b,c: a + b + c
print(add_(5,6,5))

even = lambda num : num % 2 == 0
print(even(7))

g = lambda a,b : a if a > b else b
print(g(10,20))

a = lambda a : a**3
print(a(5))

------------------

filter()
-------

--> filter() fuction will perfrom only on selected elemets of itterables

syntax --> filter(lambda argument : expression)

nums = [1,2,3,4,5]
data_ = filter(lambda a: a > 2 , nums)
print(set(data_))

map()
----

--> map() fuction  will perfrom on all elemts  of a itterable

syntax --> map(lambda arguments : epression, iterable)

eg:-

nums = [1,2,3,4,5]
data_ = map(lambda a: a+6 , nums)
print(list(data_))


reduce()
---------

-->reduce() fuction repeatedly applies a fuctions to the elements and reduce them to one final value.
--> it is available in the fuctions module


syntax -->reduce(lambda arguments: expression, iterable)

eg:-

from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b : a+b , nums)
print(data_)


from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b : a+b ,range(1,10))
print(data_)


































