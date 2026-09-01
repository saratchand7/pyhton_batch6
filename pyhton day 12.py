

find the number is even or odd?

num = int(input('Enter number: '))
if num % 2 == 0:
    print(f'{num} is even number')
else:
    print(f'{num} is odd number')
============================
remove duplicates from the list?

data_ = [1,2,2,3,3,4,5,5,6,6,6,7,8,9,9]
new_ = list(dict.fromkeys(data_))
print(new_)

==============================

find the given number is amstrong number?


num = int(input("Enter a number: "))
original_num = num
num_digits = len(str(num))
total_sum = 0
while num > 0:
    digit = num % 10
    total_sum += digit ** num_digits
    num //= 10
if total_sum == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")

==============================

nuber of owels in the string?

text = "i am very happy today and what about you"
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(count)

==============================

count the number words in the string?

text = "i am very happy today and what about you"
words = text.split()
print(len(words))

==========================

print triangle pattern with stars?

star_ = int(input('Enter number of stars: '))
for i in range(2,star_+1):
    for j in range(1,i+1):
        print('*', end = " ")
    print()






















