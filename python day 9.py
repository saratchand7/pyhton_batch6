

Dictinory

-------------

--> Dictinory is an collection of key value pairs
--> key must be unique and it should be immutable data type
(int, str, tuple)

Accessing
-----------

--> dict can access by calling key, we will get value from that key

sytax --> dict['key']

--> get() method is also used to get the value from that key

syntx --> dict.get('key')

eg:-

data_ = {'name' : 'Sarat',
         'balcance': 7000,
         'adr' : 1235464,
         'panc': 'CHVIC484C',
         2 :[3,4]}

print(data_['name'])
print(data_.get(2))

-------------------
update()
------------

--> method is used update a key, incase if the key is not present inside dict then it add that key:value

syntx --> dict.update({key:value})

--> there is another way to update a key
syntx --> dict[key] = value

eg:-

data_ = {'name' : 'Sarat',
         'balcance': 7000,
         'adr' : 1235464,
         'panc': 'CHVIC484C',
         2 :[3,4]}

print(data_)
data_['AC'] = 23456789



=====
updateing a key

-->

data_ = {'name' : 'Sarat',
         'balcance': 7000,
         'adr' : 1235464,
         'panc': 'CHVIC484C',
         2 :[3,4]}

print(data_)
data_['name'] = 'sarath'
print(data_)
---------------
will add new key value pair
--
data_['AC'] = 12546987
print(data_)
--------------
will update the pervious key
--
data_.update({'name':'chand'})
print(data_)

------------------------------------------

Values()
-----------

--> values() method is used to accsess the values from dict

syntx --> dict.values()

data_ = {'name' : 'Sarat',
         'balcance': 7000,
         'adr' : 1235464,
         'panc': 'CHVIC484C',
         2 :[3,4]}

print(data_.values())

--------------------------------------

keys()
-----

--> keys() only used to get the key values only

syntax--> dict.key()


eg:-
data_ = {'name' : 'Sarat',
         'balcance': 7000,
         'adr' : 1235464,
         'panc': 'CHVIC484C',
         2 :[3,4]}
print(data_.keys())

-------------------------------------

items()
----------

--> items() this method will get the key:value separated from the dict


syntx --> dict.items()

eg:-

data_ = {'name' : 'Sarat',
         'balcance': 7000,
         'adr' : 1235464,
         'panc': 'CHVIC484C',
         2 :[3,4]}

print(data_.items())

--------------------------------

clear()
---------

--> clear() is used to delet all data from the dictinory

syntx --> dict.clear()

eg:-

data_ = {'name' : 'Sarat',
         'balcance': 7000,
         'adr' : 1235464,
         'panc': 'CHVIC484C',
         2 :[3,4]}
data_.clear()
print(data_)

===========

del()

--> del() is used to delet the key:value pair 

syntx -->

eg:-

data_ = {'name' : 'Sarat',
         'balcance': 7000,
         'adr' : 1235464,
         'panc': 'CHVIC484C',
         2 :[3,4]}
del data_[2]
print(data_)

========================================================================

if statement
------------

--> if condition become true then it will execute inside block of code

--> in case it become False then it will never enter into inside block


eg:-

age = int(input())
if age>=18:
    print('Eligibale to vote')

---------------

if-else statement
-------

-->else for if statement is a fall back statement, incase if condition is false then else block will execute


eg:-

age = int(input("Enter your age: "))
if age>=18:
    print(f'your {age} Eligibale to vote')
else:
    print(f'your {age} you have to wait {18-age} years')














































