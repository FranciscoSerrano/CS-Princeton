"""
Order check. Compose a program that takes three floats x, y, and z as command-line arguments and writes True if the values are strictly ascending or descending (x < y < z or x > y > z), and False otherwise.
"""
import sys

x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]

def acs_or_dsc(x, y, z):
    if x < y and y < z:
        return True
    elif x > y and y > z:
        return True
    else:
        return False

print(acs_or_dsc(x, y, z))