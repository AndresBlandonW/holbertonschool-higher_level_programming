#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last = str(number)[-1]
    lastd = int(last) * (-1)
else:
    lastd = number % 10

if lastd > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastd))
elif lastd == 0:
    print("Last digit of {} is {} and is 0".format(number, lastd))
elif lastd < 6:
    print("Last digit of {0} is {1}".format(number, lastd), end=' ')
    print("and is less than 6 and not 0")
