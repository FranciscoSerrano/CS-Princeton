"""
Great circle. Compose a program that takes four float command-line arguments x1, y1, x2, and y2 (the latitude and longitude, in degrees, of two points on the earth) and writes the great-circle distance between them. The great-circle distance d (in nautical miles) is given by the formula derived from the law of cosines:

    d = 60 * arccos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))

Note that this equation uses degrees, whereas Python's trigonometric functions use radians. Use math.radians() and math.degrees() to convert between the two. Use your program to compute the great-circle distance between Paris (48.87° N, -2.33° W) and San Francisco (37.8° N, 122.4° W).

Note: the shape of the earth is more like a flattened spheroid than a sphere, so the formula above is only an approximation (up to around 0.5% error). Also, this formula is unreliable for small distances because the inverse cosine function is ill-conditioned.

Here is the Haversine formula:

    a = sin2((L2-L1)/2) + cos(L1) * cos(L2) * sin2((G2-G1)/2) c = 2 * arcsin(min(1, sqrt(a))) # distance in radians distance = 60 * c # nautical miles

The Haversine formula is accurate for most distances, but it suffers from rounding errors when the points are (nearly) antipodal. The following formula is accurate for all distances.

    delta = G1 - G2 p1 = cos(L2) * sin(delta) p2 = cos(L1) * sin(L2) - sin(L1) * cos(L2) * cos(delta) p3 = sin(L1) * sin(L2) + cos(L1) * cos(L2) * cos(delta) distance = 60 * atan2(sqrt(p1*p1 + p2*p2), p3)

This Kahan reference provides more details.
"""

import sys
import math

acos = math.acos
sin = math.sin
cos = math.cos

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# convert to radians because it doesnt work otherwise
x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

angle = acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))
degrees = math.degrees(angle)

distance = 60.0 * degrees

print(str(distance) + ' nautical miles')
