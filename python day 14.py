
Fucutions

----------------------

--> A fcution is a block of code that can be executed only when it is called...

syntax  -->

a fuction start with the def Keyword and the line is called as defination line
,where we can define a fuction name
--> and if we want to execute the program in the fuction ,need to call with the fuction name defined
at def line

def fuct_name(Parameters):
              pass
            fuct_name(arguments)

eg:-

def add_(a,b):
    print(a + b)
add_(5,6)

----------------------------

Arguments
-----------

Positional arugument
------------------

--> the arugument should be same at def line and calling, incase if they are not same number will
rise an error

eg:-

def feb_(a,b):
    print(a,b,end = ' ')
    for i in range(1,10):
        c = a + b
        a = b
        b = c 
        print(c,end=" ")
feb_(0,1)

-----------------------

defult arugument
--------------

--> The defult arguments where the fuction will only consider the data at calling fuction,
even though data present at def line

eg:-

def feb_(num,num_2):
    print(num+num_2)
feb_([1,3],[5,6])


def data_(a=8,b=9):
    print(a+b)
data_(1,2)


eg:-

def prime(num = 10, count = 1):
    for j in range(1,num+1):
        if num % j ==0:
            count += 1
    if count ==2:
            print(f'{num} is prime ')
    else:
            print(f'{num} is not prime')
prime(num = int(input("Enter a number: ")), count = 0)

------------------------------------

Keyword argument
----------------

-->

eg:-

def data_(age,name,batch,location):
    print(name)
    print(age)
    print(batch)
    print(location)
data_(name = 'sarat',age = 24,location = 'Vizag',batch = 6)

variable lenght arugument
----------------------------

--> adding a (* call it as args) before a variable at parameters we can pass
tuple of arguments and can be access with indexing

eg:-

def all_(*name):
    print(name[1])
all_('sarat','chand','hi')

-----------------------------

Keyword lenght argument
-------------

--> adding a (** call it as kargs) before a varible at parameters we can pass key value pairs arguments
and can be access with key word.

eg:-

def details_(**data_):
    print(data_.keys())
details_(name = 'sarat',age = 24,location = 'Vizag',batch = 6)


---------------------

Return
-----------

--> the return keyword used  inside the fuction, once the return is executed means it will
get back to calling with return values

eg:-

def all(a,b):
    return a-b
print(all(7,9))










































































