
Elif
-----------------------

--> elif statement is used to check more possible outcomes or more conditions

eg:-

a = 90
b = 780
c = 670

if a>b and a>c:
    print(a)

elif b>a and b>c:
    print(b)
else:
    print(c)

eg 2:-

num = 7
num_2 = 3
urser_opt = int(input('Enter \n1.add \n2.sub \n3.mul \n: '))
if user_otp == 1:
    print(num + num_2)
elif user_otp == 2:
    print(num - num_2)
elif user_opt == 3:
    print(num * num_2)
else:
    print(num ** num_2)

-----------------------

Nested - if

-----------------------------

--> if inside an if statement is called as nested-if

eg:-

import random

app_details = {'pin':1234}
user_password = int(input("Enter your app password: ")
otp = random.randint(1000:9999)
if user_password == app_details['pin']:
    print('password is correct')
    print(otp)
    user_otp = int(input("Enter 4 digit otp: "))
    if user_otp == otp:
        print('Welcome to the app')

    else:
        print('Invaild opt')
else:
    ('Passwor is incorrect')

----------------------------------

give number is even or odd

-----

num = int(input("Enter a num : "))
if num % 2 == 0:
    print(f'{num} is a even number')
else:
    print(f'{num} is a odd number')

------------

marks:

marks = int(input("Enter your marks: "))
if marks >=90:
    print('A+')
elif marks >=80:
    print('A')
elif marks >=70:
    print('B+')
elif marks >=60:
    print('B')
elif marks >=50:
    print('C+')
else:
    print('Failed')































