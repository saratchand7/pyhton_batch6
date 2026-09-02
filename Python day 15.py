
Scope of Variables
----------------------

1. Local Variable

 --> A variable is define inside the fuction call it as local variable, where the variable can only
 access with in that fuction

eg:-

def display()
    name = 'Sarat'
    print(name)
display()
#print(name)

========================================

2. Golbal Variable
----------------

--> Variable that is defined outside the fuction call and it can be access anywhere through out the program


eg:-

a = 90
def display():
    print(a)
display()
#print(a)



--------------------------------------

Golbal Keywor
-----------------

--> Gobal is a keyword used to reasing new values to a variable that was already define out-side the fuction call


eg:-

a = 90
print(a)
def display():
    global a
    a = 10
display()
#print(a)
-----------------------

passing by value
------------------
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(109)

-----------------

passing by reference
----------------

num = 15
def even_odd(num):
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
even_odd(num)

----------------------------

Recursive fuction
-----------

--> the fuction call itself until the base condition met...

eg:-

def fac(a):
    if a == 0 or a == 1:
        return a
    return a * fac(a-1)
print(fac(6))
                































