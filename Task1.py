# Code for task 1
import subprocess
import sys

from temperature import Temperature

# A demonstration of temperature conversions
temp = Temperature(30, "C")
print(f"Original temperature: {temp}")
print(f"In Fahrenheit: {temp.to_fahrenheit():.2f} °F")
print(f"In Kelvin: {temp.to_kelvin()} K")

# Creates a new object in Fahrenheit
converted = temp.convert_to("F")
print(f"Converted: {converted}")
print(f"Original is unchanged: {temp}")


# A comparison of equivalent temperatures in different units
print(f"0 °C equals 32 °F: {Temperature(0, 'C') == Temperature(32, 'F')}") 
print(f"100 °C is higher than 300 K: {Temperature(100, 'C') > Temperature(300, 'K')}")

# String representations
print(str(temp))
print(repr(temp))


# A demonstration of invalid units
for value, unit in [(30, "X"), (-279, "C")]:
    try:
        Temperature(value, unit)
    except ValueError as error:
        print(f"{value} {unit}: {error}")