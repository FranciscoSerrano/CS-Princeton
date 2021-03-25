"""
Three-sort. Compose a program that accepts three integers from the command line and writes them in ascending order. Use the built-in min() and max() functions.
"""
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

numbers = [a, b, c]
_max = max(numbers)
_min = min(numbers)
other = a + b + c - _min - _max;

print(_min, other, _max)