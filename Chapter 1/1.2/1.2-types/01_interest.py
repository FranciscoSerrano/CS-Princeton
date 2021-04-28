"""
Continuously compounded interest. 
Compose a program that calculates and writes 
the amount of money you would have if you invested it 
at a given interest rate compounded continuously, taking 
the number of years t, the principal P, and the annual interest 
rate r as commmand-line arguments. The desired value is 
given by the formula pert.
"""
import math

e = math.e
# Function to calculate the Compound Interest
def comp_interest(p, r, t,):
    interest_amount = p * (pow(e, r*t))
    return interest_amount

print(comp_interest(1000.50, 0.05, 5))