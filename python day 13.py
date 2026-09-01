

palindrome

----------------

words = 'madam'
empty_ste = ''
for i in words:
    empty_ste = i + empty_ste
if empty_ste == words:
    print(f'{words} is a palindrome')
else:
    print(f'{words} is not a palindrome')

------------------

amstrong number
-------------------------------------------------------
num = int(input('Enter a number: '))
lenght = len(str(num))
amstrong = 0
for i in str(num):
    amstrong = amstrong + int(i)**lenght
if amstrong == num:
    print(f'{num} is a amstrong number')
else:
    print(f'{num} is not a amstrong number')

-------------------------------------------------------

perfect number

---------------

num = int(input("Enter a number: "))
sum_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_divisors += i
if sum_divisors == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")

-----------------------------------------------

fibonacci series

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(a,b,end = ' ')
for i in range(1,10):
    c = a + b
    a = b
    b = c 
    print(c,end=" ")

















































