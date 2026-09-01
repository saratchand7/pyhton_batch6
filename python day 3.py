Datatypes & Conversions
---------------------------------------
Numeric Datatype
-----------------

--> Float and integer is called as numaric datatypes
1.Float
-----
--> A number which contains decimal values, we call it as float datatype

eg:-
56.89
integer(int)
------------------------------

--> a normal number without any decimal values

eg:-
num = 89
num_1 = 6
_______________________________________________________________________

2.string
--------

--> string is a sequence of charecters that are enclosed in '',"",'''.'''
--> String is immutable

eg:-
aby_ = 'Python is a language'
all_ = 'Ab,.&[)-+'
_______________________________________________________________________

3.List
-------

--> List is a collection of different datatypes and it is represented by [ ], that are separated by ,
-- inside the list we call it as items and lists are mutable

eg:
any_ = [1,'python',[5,6]]
print(type(any_))
______________________________________________________________________
4.tuple
--------

--> Tuple is collection of different datatypes that are enclosed in () and those are separated by ,
--> tuple is immutable

eg:

nums = (1,89.67,'Python',[3,4],(8,9))
_______________________________________________________________________

5.Dictinoary
------------

--> Dictinoary is a collection of key:value pairs , Keys and values are sperated by :
--> key and value pair is called as a item
--> this items are sperated by ,
--> Dictinory is represented using { }
--> in keys place we can use immutable data types
--> in values place we can use any datatypes

eg:
data_ = {1:2,
    'name':'Sarat',
         (2,3):'tuple'}
print(data_)
_____________________________________________________________________

6.set
-------

--> Set is collection of Unique elements and set can't allow any duplecate values inside it....
--> set is represented by { } and the elements are sapreated by ,

eg:
    an = {1,2,3}
    print(an)

_____________________________________________________________________

typeconverstion
----------------

float --> int, str

eg:int()
price = 45.78
print(int(price))
--
eg:str()
price = 45.78
con = str(price)
print(type(con)
------------------

integer --> float,str

ed:-float()
      num = 78
      print(float(num)

eg:-str()
        num = 78
        con = (str(num))
        print(con)
-----------------

string --> int,float

eg:- int()
            do = '10'
            print(int(do))

eg:- float()
            do = '10.89'
            print(float(do))

--------------------------
list --> tuple, string

eg:- tuple()
            nums = [1,2,3,4]
            print(tuple(nums)

eg:- str()
         nums = [1,2,3]
         print(str(nums)
---------------------------

tuple --> list
eg:- list()
               all_ = (5,6,7)
               print(list(all_))
               

