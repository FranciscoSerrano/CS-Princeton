"""
Uniform random numbers. Compose a program that writes five uniform random floats between 0 and 1, their average value, and their minimum and marandimum value. Use the built-in marand() and min() functions.
"""
import random

N = 5

rand1 = round(random.random(), 4) # not sure what they mean by uniform numbers
rand2 = round(random.random(), 4)
rand3 = round(random.random(), 4)
rand4 = round(random.random(), 4)
rand5 = round(random.random(), 4)
print(rand1)
print(rand2)
print(rand3)
print(rand4)
print(rand5)

minimum = min(rand1, rand2, rand3, rand4, rand5)
maximum = max(rand1, rand2, rand3, rand4, rand5)
average = (rand1 + rand2 + rand3 + rand4 + rand5) / N

print('Average = ' + str(average))
print('Min     = ' + str(minimum))
print('Max     = ' + str(maximum))