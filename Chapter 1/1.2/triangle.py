'''
Compose a program that takes three positive 
integers as command-line arguments and writes False if any 
one of them is greater than or equal to the sum of 
the other two and True otherwise. (Note: This computation 
tests whether the three numbers could be the lengths of the sides of some triangle.)
'''
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a >= b + c or b >= a + c or c >= b + a: #could've been elif's too i guess
    print(False)
else:
    print(True)