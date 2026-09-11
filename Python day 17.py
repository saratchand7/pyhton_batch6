
List comprehension
-----------------

--> List comprehension is the short from of syntax to create a list

--> syntax -- 1. [expression loop condition]
--> syntax -- 2. [expression condition else loop]

eg:-

old_ = [1,2,3,4,5]
new_ = [i for i in old_]
print(new_)

old_ = [1,2,3,4,5]
new_ = [i for i in old_ if i % 2 == 0]
print(new_)

--------------

Nested comprehension
---------------------

--> using a list comprehension generating list inside list

eg:-

any_ = [[i * j for i in range(1,6)]for j in range(1,10)]
print(any_)

data_ =  [[1,2,3],
        [4,5,6],
        [7,8,9]]
a = [num for i in data_ for num in i]
print(a)
------------------------------
Generator
---------------

--> a generator is a special fuction which generates one value at a time

eg:-

def data_():
    for j in range(1,10):
        yield j
j = data_()
print(next(j))




















