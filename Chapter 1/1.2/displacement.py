'''
Compose a program that takes three floats x0, v0, 
and t from the command line, evaluates x0 + v0t - Gt2 / 2, 
and writes the result. (Note: G is the constant 9.80665. This value is 
the displacement in meters after t seconds when an object is thrown straight 
up from initial position x0 at velocity v0 meters per second.)
'''
import sys

G = 9.80665

x = float(sys.argv[1])
v = float(sys.argv[2])
t = float(sys.argv[3])

solution = x + (v * t) - ((G * t * 2) / 2)

print(solution)