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

    # The read-only attributes
    @property
    def value(self) -> float:
        """Returns the read-only temperature value"""
        return self._value
        
    @property
    def unit(self) -> str:
        """Returns the read-only temperature unit"""
        return self._unit 

    # The conversion methods
    def to_celsius(self) -> float:
        """Converts the temperature to Celsius"""
        if self.unit == "K": # From Kelvin
            return self.value - 273.15
    
        if self.unit == "F": # From Fahrenheit
            return (self.value - 32) * 5 / 9
    
        return self.value
    
    def to_fahrenheit(self) -> float:
        """Converts the temperature to Fahrenheit"""
        if self.unit == "C": # From Celsius
            return self.value * 9 / 5 + 32
    
        if self.unit == "K": # From Kelvin
            return (self.value - 273.15) * 9 / 5 + 32
    
        return self.value
    
    def to_kelvin(self) -> float:
        """Converts the temperature to Kevin"""
        if self.unit == "C": # From Celsius
            return self.value + 273.15
    
        if self.unit == "F": # From Fahrenheit
            return (self.value - 32) * 5 / 9 + 273.15
    
        return self.value
    
    def convert_to(self, target_unit: str) -> "Temperature":
        """Returns a new temperature object in the the target unit"""
        target_unit = target_unit.upper()
    
        # Converts the temperature to the requested unit
        if target_unit == "C":
            value = self.to_celsius()
            minimum = -273.15
    
        elif target_unit == "F":
            value = self.to_fahrenheit()
            minimum = -459.67
    
        elif target_unit == "K":
            value = self.to_kelvin()
            minimum = 0.0
    
        else:
            raise ValueError("Invalid target temperature unit")
    
        # Prevents rounding errors below absolute zero
        if isclose(
            value, minimum, rel_tol=0.0, abs_tol=self.TOLERANCE
            ) and value < minimum:
            value = minimum
    
        return Temperature(value, target_unit)

    # The string representations
    def __repr__(self) -> str:
        """Returns an unambiguous representation of the object"""
        return f"Temperature({self.value}, '{self.unit}')"
    
    def __str__(self) -> str:
        """Returns a human-readable string formatted to 2 decimal places"""
        if self.unit == "K":
            return f"{self.value:.2f} K" 
    
        return f"{self.value:.2f} °{self.unit}"

    # The comparison methods
    def __eq__(self, other: object) -> bool | NotImplementedType:
        """Checks if 2 temperatures are equal"""
        if not isinstance(other, Temperature):
            return NotImplemented
    
        return isclose(
            self.to_kelvin(),
            other.to_kelvin(),
            rel_tol=0.0,
            abs_tol=self.TOLERANCE
        )
    
    def __ne__(self, other: object) -> bool | NotImplementedType:
        """Checks if 2 temperatures are not equal"""
        if not isinstance(other, Temperature):
            return NotImplemented
    
        return not self == other
    
    def __lt__(self, other: object) -> bool | NotImplementedType:
        """Checks if the temperature is lower than another"""
        if not isinstance(other, Temperature):
            return NotImplemented
    
        return self.to_kelvin() < other.to_kelvin() and self != other

    def __le__(self, other: object) -> bool | NotImplementedType:
        """Checks if the temperature is lower than or equal to another"""
        if not isinstance(other, Temperature):
            return NotImplemented
    
        return self < other or self == other
    
    def __gt__(self, other: object) -> bool | NotImplementedType:
        """Checks if the temperature is higher than another"""
        if not isinstance(other, Temperature):
            return NotImplemented
    
        return self.to_kelvin() > other.to_kelvin() and self != other 
    
    def __ge__(self, other: object) -> bool | NotImplementedType:
        """Checks if the temperature is higher than or equal to another"""
        if not isinstance(other, Temperature):
            return NotImplemented
    
        74return self > other or self == other
        
