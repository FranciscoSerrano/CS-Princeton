'''
Compose a program that takes two integers m and d 
from the command line and writes True if day d of month m 
is between March 20 and June 20, and False otherwise. 
(Interpret m with 1 for January, 2 for February, and so forth.)
'''
import sys

month = int(sys.argv[1])
day = int(sys.argv[2])

isSpring = (month == 3 and day >= 20 and day <= 31) or \
           (month == 4 and day >=  1 and day <= 30) or \
           (month == 5 and day >=  1 and day <= 31) or \
           (month == 6 and day >=  1 and day <= 20)

print(isSpring)
