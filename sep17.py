
#Exception Handling -->
#Exception Handling is a mechanisam to a program which respond to run time
#error or compilations
#Exception --> It tries to make our program go in a noraml flow
'''
try,except,finally
#for every try except is mandatory...

try:
    #code that may cause an error...
    ...

except:
    #Code that may cause an error...
    ....

finally:
    ......
    .......


#simple scenario to understand the exception

a,b = map(int,input("Enter the Values: ").split(','))
try:
    result = a/b
    print(result)
except Exception as e:
    print("Find it")
    print(e)

#Same above case accept inputs in try block

try:
    a,b = map(int,input("Enter the Values: ").split(','))
    result = a/b
    print(result)
except Exception as e:
    print("Find it")
    print(e)
    
#In above case we will get ValueError,ZeroDivisionError
#Possible types of error --> TypeError,ValueError,NameError
#IndexError,ZeroDivisionError,AttributeError,Arithmetic Error..

try:
    a,b = map(int,input('Enter the values').split(','))
    result = a/b
    print(result)
except ValueError:
    print('Bossu sarigga chusi enter cheyyu only integers')
except ZeroDivisionError:
    print('Make sure to give denominator greater than zero')
except NameError:
    print('Please first undersrtand the synntax and be good at spellings')
except AttributeError:
    print('please check the methods r functions names properly')
finally:
    print('Learn from mistakes')

#Multiple Exception at a time

try:
    a = [12,3,4,5]
    print(a[0]) #take one example as print(a[45])
    a.append('Codegnan')#take one example as a.append('codegnan')
    print(a) #take one example as print(v)
except(IndexError,NameError,AttributeError) as e:
    print(e)
finally:
    print('done')
#In all the above cases all errors will be compromised..'''


marks = int(input("Enter the marks: "))
if marks < 0 or marks > 100:
       print("Invalid marks entered")
elif marks >= 90:
       print(f'Grade: A\nRemark: Outstanding!')
elif marks >= 80:
       print(f'Grade: B\nRemark: Excellent!')
elif marks >= 70:
       print(f'Grade: C\nRemark: Good')
elif marks >= 60:
       print(f'Grade: D\nRemark: Fair, needs improvement')
elif marks >=50:
       print(f'Grade: E\nRemark: Poor, needs serious improvement')
elif marks < 50 and marks >= 0:
       print(f'Grade: F\nRemark: Failed, needs to reappear')

number = int(input("Enter the number: "))
if number == 0:
    print('Zero is neither even nor odd ')
elif number < 0 and number % 2 == 0:
    print('Negative Even Number')
elif number < 0 and number % 2 != 0:
    print('Negative Odd Number')
elif number % 2 == 0:
    print('Positive Even Number')
elif number % 2 != 0:
    print('Positive Odd Number')

month = int(input("Enter the month number: "))
if month < 1 or month > 12:
    print("Invalid month number")
else:
    if month == 12 or month == 1 or month == 2:
        print("Season: Winter")
    elif month == 3 or month == 4 or month == 5:
        print("Season: Spring")
    elif month == 6 or month == 7 or month == 8:
        print("Season: Summer")
    elif month == 9 or month == 10 or month == 11:
        print("Season: Autumn")
        















    
