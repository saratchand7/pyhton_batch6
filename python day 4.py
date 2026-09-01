
concatination
--------------

--> the + will behave two ways for numeric it work normally and for other datatypes like string,list,tuple it concatinate
_____________________________________________________________________________________________________________________________


Operators
-----------

--> The operators are used to perform operations in variables and values..

1.Arthematic operator
-------------------------
+,-,*,/,//,%

+ --> to add the values

eg:-

num = 78
num_2 = 9
print(num + num_2)

- --> to subtract the vaules

eg:-
num = 9
num_2 = 7
print(num - num_2)

* --> to multiple the values

eg:-
v = 8
n = 4
print(v - n)

/ --> to divide the value

eg:-
v = 8
n = 4
print(v / n)

// --> to divide the value and removes the float point

eg:-
v = 8
n = 4
print(v // n)
_____________________________________________________________________________________________________________________________________

2. Assingment operator
-------------------------
= ,+=, -=, *=, %=, /=

+= --> is increment operator

a = 0
print(a)
 a += 1
print(a)

-= --> decrement operator
a = 9
print(a)
a -= 2
print(a)

*= -->

c = 7
c *= 2
print(c)

%= -->

e = 5
e %= 2
print(e)

/= -->

d = 18
d /= 2
print(d)


3. Compaarison operator
------------------------
==, >= ,<= , < , > , !=

--> == checks the values are same or not

a = 9
b = 5
print(a == b)

#false

--> != checks the values shouldnt match

a = 9
b = 5
print(a != b)

#True

--> >

a = 9
b = 5
print(a > b)

#True

--> <

a = 9
b = 5
print(a < b)

#false

--> >=

a = 9
b = 7
print(a >= b)

#True

--> <=

a = 9
b = 7
print(a <= b)

#false
___________________________________________________________________________________________________________________________________________________________________

4. Logical operator
---------------------
and , or , not

and -->

num = 9
num_2 = 13
print(num >= num_2 and num <= 10)# 9 >= 13 and 9 <= 10
print(num <= num_2 and num <= 10)# 9 <= 13 and 9 <= 10

or -->

num = 9
num_2 = 13
print(num >= num_2 or num < 10)

not -->

num = 9
num_2 = 13
print(not(num >= num_2 or num < 10))

____________________________________________________________________________________________________________________________________________________________________

5. Identity operator
---------------------
is, is not

is -->

num = [1,2]
num_2 = [1,2]
print(num == num_2)#Ture
print(num is num_2)#False

is not -->

a = [1,2]
b = [1,2]
print(id(a))
print(id(b))
print(a is b)# False
__________________________________________________________________________________________________________________________________________________________________

6. membership operator
----------------------
in , not in

in -->

nums = [1,2,3,56]
print( 8 in nums)#False

not in -->

print( 57 not in nums)#Ture
__________________________________________________________________________________________________________________________________________________________________

7. Bitwise operator
--------------------

5 --> 1010
3 --> 0011
1 --> 0010

-->bitwise &

eg:
print(5 & 3)


--> bitwise Or

print(5 | 3)

5 --> 0101
3 --> 0011
7 --> 0111


^ --> bitwise Xor

print(5 ^ 3)

5 --> 0101
3 --> 0011
6 --> 0110


>> --> Right Shift

5 --> 0101
1 --> 0001
0001

print( 5 >> 1)

<< -->

print(5 << 1)

5 --> 0101
1 --> 0001








































