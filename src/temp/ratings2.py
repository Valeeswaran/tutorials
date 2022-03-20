import math
rating = [2, 1, 3, 4, 5]
rcount = len(rating)

ones = 0
twos = 0
threes = 0

ones = len(rating)

if len(rating) >= 3:
    threes = 1
elif len(rating) > 3:
    threes = math.floor(len(rating) / 3)

if len(rating) != 3 and len(rating) > 2:
    twos = len([j for j in range(len(rating), 0, -2)])




r = ones + twos + threes
print(r)




