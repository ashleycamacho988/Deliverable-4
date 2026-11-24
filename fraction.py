# The Fraction class
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