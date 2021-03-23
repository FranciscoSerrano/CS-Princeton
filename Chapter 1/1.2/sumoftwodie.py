'''
Compose a program that writes the sum of 
two random integers between 1 and 6 
(such as you might get when rolling dice).
'''
import random
import sys

DICE = 6

a = random.randrange(1, DICE +1)
b = random.randrange(1, DICE +1)

total = a + b
print(total)