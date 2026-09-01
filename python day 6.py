

Strings
--------------------

operations
--------------------
1.Indexing
--------

-->Indexing is used to get charecter that you looking to access we have two types

text = 'Python'
print(text[2])

-> Positive indexing
---------------

-->positive indexing starts from 0 index

syntx : print(Variable_name[index_postion])

eg: text = 'Python'
print(text[2])

-> Negative indexing

--> Negative indexing starts from -1 index

syntx : print(Variable_name[Negative_index_postion])

eg:
    
text = 'Python'
print(text[-1])

task -->

text = 'Python is a programming language'
print(text[17])
print(text[-15])


2.len()
----------

--> len() is built-in fuction that used to get number of charecters present in the string


syntx :-print(len(Variable_name))

eg:

text = 'Python is a programming language'
print(len(text))

3.slicing
-----------

--> this is used to access the paticular part from the string 

syntx: print(variable_name[Start:End])

eg:

text = 'Python is a programming language'
print(text[12:])
print(text[:23])
print(text[12:23])

---------------

---> upper()

--> Used to convert all lower cases to uppercase

eg:
    
text = 'Python is a programming language'
print(text.upper())


----> lower()

-- used to conver all upper case to lower case

text = 'Python is a programming language'
print(text.lower())

---> index()

--> Used to know the index position of an charecter 

syntx:- print(variable_name.index('enter_the_alphabet'))

eg:

text = 'Python IS a Programming languAGE'
print(text.index('A'))
print(text[7])

---> replace()

--> used to replace old substring with new substring

syntx:- print(text.replace("python",'java'))




text = 'Python is a programming language'
print(text.replace('Python','java'))

--->split()

--> this method is used to separate the string based on the given substring

syntx:- print(text.split(" "))

eg:

text = 'Python is a programming language'
print(text.split(" "))

---> count()

-->

syntx:-print(text.count('substring',strat,stop))

eg:

text = 'Python is a programming language'
print(text.count('a',1,25))

===========================



List
-----

--> collection of different datatypes that separated by , and it is represented by []


indexing
---------

positive --> 0


eg:

so = [1,2,3,4,'python']
print(so([4][3])


Negative --> -1

eg:
so = [1,2,3,4,'Python']
print(so[-1][-3])

all_ = [12,[1,'python',[1,4],(78,[6,7]),['java',78]]]
print(all_[1][3][1])

data_ = ['python', [1,2,(90,'Details',[67,0]),(78,'student')]]
print(data_[1][2][1][2])

len()
-------------

--> The fuction is used to find the number of items present inside list

syntx :- len(variable_name)

eg:

data_ = ['python', [1,2,(90,'Details',[67,0]),(78,'student')]]
print(len(data_))

sliceing
---------

--->

syntx:- 

eg:

data_ = [1,2,3,4,5,6,7]
print(data_[2:6])

a = [1,2]
b = [3,4]
      
print(a+b)

Methods
----------
append()

-->append method will add new items into list at last index position

position

syntax --> variable_name.append(item)

eg:

go = [1,2]
print(go)
go.append(3)
print(go)
go.append(4)
print(go)

a = [1,2]
a.append([3,4])
print(a)

extend()

--->will add the items into a list at last index position, but it will give each value
      as one index inside the list

syntx --> variable_name.extend(items)

eg:

go = [1,2]
go.extend('python')
print(go)

eg:

go = [1,2]
go.extend([3,4,5])
print(go)

pop()
-------

--> poo() is used to remove item from the list and it will delete based on the index position 

syntx -->

eg:

m = [1,2,3,4]
m.pop(3)
print(m)


remove()
--------

--> will delete the items based on value given inti

syntx -->variable_name.remove(value)

eg:

m = [5,1,2,3,4,'pyhton']
m.remove(5)
print(m)



























