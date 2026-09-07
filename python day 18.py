importing modules: 
To use functions, classes, or variables defined in another Python file (module),
you can import that module into your current script using the 'import' statement.
This allows you to access and utilize the code from the imported module.
syntax: import module_name
example:
import math
print(math.sqrt(16))  # Output: 4.0

example-2:
import random
print(random.randint(1, 10))  # Output: A random integer between 1 and 10

example-3:
import python_module
python_module.greet("Alice")  # Output: Hello, Alice!

User-defined modules:
You can create your own Python modules by defining functions, classes, or variables in a separate .py file.
To use your user-defined module, you can import it into another Python script using the 'import' statement.
example: 
import my_module
my_module.my_function()  # Calling a function from the user-defined module

example-2:
from my_module import my_function
my_function()  # Calling the imported function from the user-defined module 

example-3:
from newfile import add, sub, mul
print(add(5, 3))  # Output: 8
print(sub(10, 4))  # Output: 6
print(mul(2, 7))  # Output: 14

example-4:
import newfile as nf
print(nf.add(5, 3))  # Output: 8


built-in modules:
Python provides a wide range of built-in modules that offer various functionalities,
such as math operations, file handling, data manipulation, and more.
You can import and use these modules in your Python programs without the need for external installations.
examples: os, sys, math, random, datetime, json, re, itertools, functools, collections, and many more.
import os (To communicate with the operating system)
print(os.getcwd())  # Output: /your/current/directory (current working directory)

example-2:
import sys (To access system-specific parameters and functions)
print(sys.version)  # Output: 3.8.5 (or your current Python version)

example-3:
import datetime (To work with dates and times)
print(datetime.datetime.now())  # Output: 2026-09-05 14:27:17.550060 (current date and time)

example-4:
import random (To generate random numbers)
print(random.randint(1, 100))  # Output: A random integer between 1 and 100

example-5:
import smtplib
print("Welcome to the email sender program!")
'''
