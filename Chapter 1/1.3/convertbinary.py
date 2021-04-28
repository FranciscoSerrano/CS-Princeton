import sys

n = int(input("\nEnter a number you wish to convert: "))

# Compute v as the largest power of 2 <= n
v = 1 
while v <= n // 2:
    v *= 2
# Cast out powers of two in decreasing order
while v > 0:
    binary = ''
    if  n < v:
        print(0)
    else:
        print(1)
        n -= v
    v //= 2
