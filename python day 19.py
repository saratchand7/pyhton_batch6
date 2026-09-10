
import math
print(math.pi)
print(math.ceil(4.3))
print(math.floor(5.6))
print(math.sqrt(25))
print(math.sin(2))
print(math.pow(2,3))


import random
print(random.randint(1000,9999))
print(random.randrange(1,100))
colour = ['red','blue','green','yellow']
print(random.choice(colour))
random.shuffle(colour)
print(colour)


import platform
print(platform.python_version)
print(platform.system())
print(platform.platform())
print(platform.processor())


from collections import defaultdict
data_  = defaultdict(list)
data_['Python'].append('sarat')
data_['Python'].append('chand')
data_['java'].append('sony')
print(data_)

from datetime import datetime
today = datetime.today()
now = datetime.now()
print(now.strftime('%d-%m-%y'))
print(now.strftime('%H-%M-%S'))
print(now.strftime('%A'))
print(today.month)
print(today.day)
print(today.year)
print(today.hour)
print(today.minute)


import random
attempt = 3
num = random.randrange(1,10)
print(num)
while attempt > 0:
    game = int(input())
    if game == num:
        print("your guess is correct")
        break
    else:
        attempt -= 1

if attempt == 3:
        print('1000')
    elif attempt == 2:
        print('500')
    else:
        print('200')
print('your guess is correct')


import itertools
a = itertools.count(5)
print(next(a))
print(next(a))
a = itertools.repeat('python',6)
for i in a:
    print(i)
c = itertools.cycle()

n = itertools.chain[1,2,3],[4,5,6]
print(list(n))
