"""
Wind chill. Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the National Weather Service defines the effective temperature (the wind chill) to be:

    w = 35.74 + 0.6215 t + (0.4275 t - 35.75) v0.16

Compose a program that takes two floats t from the command-line and v and writes the wind chill. Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger than 120 or less than 3 (you may assume that the values you get are in that range).
"""
import sys
import math

# temp in F
t = float(sys.argv[1])
# wind speed in Mph
v = float(sys.argv[2])


wind_chill = 35.74 + (0.6215 * t) + (((0.4275 * t) - 35.75) * math.pow(v, 0.16))


print(wind_chill)

