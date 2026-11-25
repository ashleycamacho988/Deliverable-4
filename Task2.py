# Code for task 2
import subprocess
import sys

from fraction import Fraction

# A demonstration of fraction simplification
frac1 = Fraction(1, 2)
frac2 = Fraction(6, 8)

print(f"First fraction: {frac1}")
print(f"Second fraction: {frac2}")
print(f"Numerator: {frac1.numerator}")
print(f"Denominator: {frac1.denominator}")


# A demonstration of addition and subtraction
print(f"Addition: {frac1} + {frac2} = {frac1 + frac2}")
print(f"Subtraction: {frac2} - {frac1} = {frac2 - frac1}")


# A comparison of 2 fractions
print(f"1/2 equals 2/4: {Fraction(1, 2) == Fraction(2, 4)}")
print(f"1/3 is smaller than 1/2: {Fraction(1, 3) < Fraction(1, 2)}")

# String representations
print(str(frac2))
print(repr(frac2))
