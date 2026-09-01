
Loops


for statement

--------------

--> for loop is used to iterate over a squence or iterable datatypes

for i in range i --> is called as instance variable

eg:-

nums = [12,3,5,78]
for num in nums:
    print(num)


else in for
-------------

--> unlike if-else, else block in for statment is executed after completed of all iterations

eg:-

num = 'Python'
for num in nums:
    print(num)
else:
    print('Fornt ended')

--------------------

break
---------

-->the break used to stop iteration based on the condition given

nums = [1,2,3,4,5,8,9]
for num in nums:
    print(num)
    if num ==3:
        break
----------------------------

val_ = [1,2,3,4,5,8,9]
for i in val_:
    if i % 2 ==0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

----------------------------

continue
----------

--> the continue is keyword used to skip the current iteration based on the condition

eg:-

nums = [1,2,3,4,5,8,9]
for num in nums:

    if num == 5:
        continue
    print(num)

---------------------------

for i in range(1,11):
    if i == 15:
        print(i)
    else:
        pass

----------------------------

assert
---------

--> assert is a keyword used to check the condition, incase the condition is false,it will raise the error(AssertionError)

eg:-

age = 15
assert age >= 18, 'Not eligible to vote'
print('your eligible to vote')

-------------------

while loop statement
---------------------

num = 1
while num <= 5:
    print(num)
    num += 1

==========================

































