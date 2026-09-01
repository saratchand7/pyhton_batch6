Input Formatting :
-----------------

integer -->


eg:

num = int(input("Enter a number: "))
print(num)

a = int(input("Enter a number: "))
print(a * 2)

b = float(input('Enter a decimal: '))
print(b + 7)

o/p:

Enter a decimal: 15.2
22.2

string:

so = input("Enter a string: ")
print(type(so))

List --> 1 2 3 --> [1,2,3]

nums = list(map(int, input('Enter some numbers: ').split()))
print(nums)

Tuple --> 1 2 3 --> (1,2,3)

nums = tuple(map(int, input('Enter some numbers: ').split()))
print(nums)

Set --> 1 2 3 --> {1,2,3}

nums = set(map(int, input('Enter some numbers: ').split()))
print(nums)

Any datatype -->

num = eval(input("Enter any datatype: "))
print(type(num))


name = "sarat"
age = 24
print('My name is ',name,"and age is",age)
print("Hello",name)

f string or doc string: -->

print(f'My name is {name} and my age is {age} years old')

Modules --> %

name = 'Sarat'
age = 24
print('My name is %s and i am %d years old' %(name,age)

'''

name = 'Sarat'
age = 24
print('My name is %s and i am %d years old' %(name,age))





























