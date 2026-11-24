# The Fraction class
# Allows type hints to refer to the class itself
from __future__ import annotations

from math import gcd
from types import NotImplementedType


class Fraction:
    """Represents fractions with integer numerators and denominators"""
    def __init__(self, numerator: int, denominator: int) -> None:
        """Initialises a fraction with a positive denominator"""

        # Checks if the numerator and denominator are integers
        if type(numerator) is not int or type(denominator) is not int:
            raise TypeError("Numerator and denominator must both be integers")

        # Checks if the denominator is positive
        if denominator <= 0:
            raise ValueError("Denominator should strictly be positive")

        # Finds the greatest common divisor 
        divisor = gcd(numerator, denominator)

        # Stores the simplified fraction
        self._numerator = numerator // divisor
        self._denominator = denominator // divisor

    # The read-only attributes
    @property
    def numerator(self) -> int:
        """Returns the numerator of the fraction"""
        return self._numerator

    @property
    def denominator(self) -> int:
        """Returns the denominator of the fraction"""
        return self._denominator

    # The string representations
    def __repr__(self) -> str:
        """Returns an unambiguous representation of the fraction"""
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self) -> str:
        """Returns a human-readable string of the fraction"""
        return f"{self.numerator}/{self.denominator}"

    # The arithmetic methods 
    def __add__(self, other: object) -> Fraction | NotImplementedType:
        """Adds 2 fractions"""
        # Checks whether the other value is a fraction
        if not isinstance(other, Fraction):
            return NotImplemented

        # Calculates the numerator for addition
        numerator = (self.numerator * other.denominator + other.numerator * self.denominator)
        # Multiplies the denominators
        denominator = self.denominator * other.denominator

        # Returns a new simplified fraction
        return Fraction(numerator, denominator)

    def __sub__(self, other: object) -> Fraction | NotImplementedType:
        """Subtracts one fraction from another"""
        if not isinstance(other, Fraction):
            return NotImplemented
        
        numerator = (self.numerator * other.denominator - other.numerator * self.denominator)
        denominator = self.denominator * other.denominator
        
        return Fraction(numerator, denominator)

    # The comparison methods
    def __eq__(self, other: object) -> bool | NotImplementedType:
        """Checks if 2 fractions are equal"""
        if not isinstance(other, Fraction):
            return NotImplemented

        # Compares fractions by cross-multiplication
        return (self.numerator * other.denominator == other.numerator * self.denominator)
     
    def __ne__(self, other: object) -> bool | NotImplementedType:
        """Checks if 2 fractions are not equal"""
        if not isinstance(other, Fraction):
            return NotImplemented

        # Overturns the equality result
        return not self == other
    
    def __lt__(self, other: object) -> bool | NotImplementedType:
        """Checks if the fraction is smaller than another"""
        if not isinstance(other, Fraction):
            return NotImplemented

        # Checks which one is smaller
        return (self.numerator * other.denominator < other.numerator * self.denominator)
    
    def __le__(self, other: object) -> bool | NotImplementedType:
        """Checks if the fraction is smaller than or equal to another"""
        if not isinstance(other, Fraction):
            return NotImplemented

        # Checks whether the fraction is smaller or equal
        return self < other or self == other
    
    def __gt__(self, other: object) -> bool | NotImplementedType:
        """Checks if the fraction is greater than another"""
        if not isinstance(other, Fraction):
            return NotImplemented

        # Checks which one is greater
        return (self.numerator * other.denominator > other.numerator * self.denominator)
    
    def __ge__(self, other: object) -> bool | NotImplementedType:
        """Checks if the fraction is greater than or equal to another"""
        if not isinstance(other, Fraction):
            return NotImplemented

        # Checks whether the fraction is greater or equal
        return self > other or self == other
   