# The temperature class
from math import isclose
from types import NotImplementedType


class Temperature:
    """Represents a temperature in Celsius (C), Fahrenheit (F) or Kelvin (K)"""
    
    TOLERANCE = 1e-9

    def __init__(self, value: float, unit: str = "C") -> None:
        """Initialises a temperature with a valid value and unit"""
        # Converts the unit to uppercase
        unit = unit.upper() 

        # Checks if the temperature unit is valid
        if unit not in ("C", "F", "K"):
            raise ValueError("Invalid temperature unit")

        # Stores the minimum temperature for each unit
        absolute_zero = {
            "C": -273.15,
            "F": -459.67,
            "K": 0.0
        }

        # Checks if the temperature is below absolute zero
        if value < absolute_zero[unit]:
            raise ValueError("Temperature can not be below absolute zero")

        # Stores the protected attributes
        self._value = float(value)
        self._unit = unit
