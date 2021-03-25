'''
Compose a program that takes two positive 
integers as command-line arguments and writes 
True if either evenly divides the other.
'''
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

if a % b == 0:
    print(True)
elif b % a == 0:
    print(True)
else:
    print(False)