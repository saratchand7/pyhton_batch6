'''cost_ = 1000
discount_ = 0.1
final_ = (cost_ - (cost_ * discount_))
print(final_)
#=======================

price = 2000
gst = 0.05
discount = 0.05
final = price -((price *discount ))
final2 = final + (final*gst)
print(final2)
#=====================

cost_price = 5000
selling_price = 7000
final = ((selling_price - cost_price) / (5000))*100
print(final)'''

#======================================================================

'''price_ = int(input('Enter amount: '))
discount_ = float(int(input('Enter the discount given:' ))
gst = 0.18

final_ = price_ - (price_ * discount_)
final2 = final_ + (final_*gst)
print(final2)'''

'''prices = [15000, 2000, 13000, 25000, 3500]

new_prices = []

for price in prices:
    if price <= 15000:
        new_prices.append(price - (price * 0.1))
    elif price > 5000:
        new_prices.append(price - (price * 0.1))
    elif price > 20000:
        new_prices.append(price - (price * 0.15))

print(new_prices)

#=================================================================================

marks = []

for mark in range(3):
    mark = int(input("Enter the marks: "))
    marks.append(mark)
marks.insert(0,90)
marks.extend([75,85])
if 75 in marks:
    marks.remove(75)
print(marks.pop())
print(f'Final list is',len(marks))

#================================================================

lst = [20,10,30,20,40,20]
lst.sort()
lst.reverse()
user_ = int(input("Enter a number to search: "))
if user_ in lst:
    print('count is',lst.count(user_))
    print('first index is',lst.index(user_))
else:
    print('No number in list')
print("samllesr Value is",min(lst))
print("largest Value is",max(lst))
print("sum of Value is",sum(lst))'''

#================================================================


'''numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
first_three = numbers[0:3]
last_three = numbers[3:6]

new_lst = numbers.copy()
numbers.clear()
print(even)
print(odd)
print(first_three)
print(last_three)'''
        

    




































