
'''
Input fromattin: Accept input form user
integer,Float,string,comma separated values,space separated values

#input from user --> input() --> can accpecet any type only in str

name = input("Enter a name: ")
print(name)
print(type(name))
print(len(name))

#split()
#by default it will be space separated

name = input("Enter a name: ").split( )#space separated
print(name)
print(type(name))
print(len(name))


#split(',') --> comma separated values

name = input("Enter a name: ").split(',')
print(name)
print(type(name))
print(len(name))

#Accept single integer,multiple integer values,group of integers

num = int(input("enter a number: "))
print(num)
print(type(num))

#Every built-int datatype is a built_in fuction --> fuctions --> objects

#Usage of map() --> group of integers

number = list(map(int,input('Enter the values: ').split(',')))
print(number)
print(type(number))

#Every built-int datatype is a built_in fuction --> fuctions --> objects

#Usage of map() --> group of integers

temperatures = list(map(float,input('Enter the values: ').split(',')))
print(temperatures)
print(type(temperatures))'''

#Accept multiple values --> integres,float,name(str)..

temperatures,pressure = map(float,input('Enter the values: ').split(','))
print('Temperature is',temperatures)
print('Pressure is',pressure)








































