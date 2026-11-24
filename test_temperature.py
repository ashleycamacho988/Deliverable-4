# Testing temperature methods and attributes
import pytest

from temperature import Temperature

TOLERANCE = 1e-9


# Initialisation
def test_default_unit() -> None:
    """Tests that Celsius is the default unit"""
    temp = Temperature(25)

    # Checks the default temperature value
    assert temp.value == 25.0
    # Checks that Celsius is the default unit
    assert temp.unit == "C"

@pytest.mark.parametrize(
    "unit, expected",
    [
        ("c", "C"),
        ("f", "F"),
        ("k", "K"),
        ("C", "C"),
        ("F", "F"),
        ("K", "K")
    ]
)
def test_case_insensitive(unit: str, expected: str) -> None:
    """Tests that lowercase and uppercase units are allowed"""
    temp = Temperature(25, unit)

    # Checks that the unit is stored in uppercase
    assert temp.unit == expected

def test_read_onlys() -> None:
    """Tests that the temperature attributes are read-only"""
    temp = Temperature(25, "C")

    # Checks that the read-only attributes can't be changed
    with pytest.raises(AttributeError):
        temp.value = 30

    with pytest.raises(AttributeError):
        temp.unit = "F"


# Validation
@pytest.mark.parametrize("unit", ["X", "ABC", "", "Kelvin"])
def test_invalid_unit(unit: str) -> None:
    """Tests that invalid units raises ValueError"""
    # Checks that invalid inputs raises an error
    with pytest.raises(ValueError):
        Temperature(25, unit)

@pytest.mark.parametrize(
    "value, unit",
    [
        (-274, "C"),
        (-460, "F"),
        (-1, "K")
    ]
)
def test_below_abs_zero(value: float, unit: str) -> None:
    """Tests that temperatures below absolute zero are rejected"""
    with pytest.raises(ValueError):
        Temperature(value, unit)

def test_invalid_targets() -> None:
    """Tests that invalid conversion units raises ValueError"""
    temp = Temperature(25, "C")

    with pytest.raises(ValueError):
        temp.convert_to("X")


# Conversions
@pytest.mark.parametrize(
    "celsius, fahrenheit, kelvin",
    [
        (-273.15, -459.67, 0.0),
        (-40.0, -40.0, 233.15),
        (0.0, 32.0, 273.15),
        (37.0, 98.6, 310.15),
        (100.0, 212.0, 373.15)
    ]
)
def test_convers(celsius: float, fahrenheit: float, kelvin: float) -> None:
    """Tests conversions between the 3 units"""
    temp_c = Temperature(celsius, "C")
    temp_f = Temperature(fahrenheit, "F")
    temp_k = Temperature(kelvin, "K")

    # Test conversions from Celsius
    # Checks the results witin the tolerance
    assert temp_c.to_celsius() == pytest.approx(celsius, abs=TOLERANCE, rel=0.0)
    assert temp_c.to_fahrenheit() == pytest.approx(fahrenheit, abs=TOLERANCE, rel=0.0)
    assert temp_c.to_kelvin() == pytest.approx(kelvin, abs=TOLERANCE, rel=0.0)

    # From Fahrenheit
    assert temp_f.to_celsius() == pytest.approx(celsius, abs=TOLERANCE, rel=0.0)
    assert temp_f.to_fahrenheit() == pytest.approx(fahrenheit, abs=TOLERANCE, rel=0.0)
    assert temp_f.to_kelvin() == pytest.approx(kelvin, abs=TOLERANCE, rel=0.0)

    # From Kelvin
    assert temp_k.to_celsius() == pytest.approx(celsius, abs=TOLERANCE, rel=0.0)
    assert temp_k.to_fahrenheit() == pytest.approx(fahrenheit, abs=TOLERANCE, rel=0.0)
    assert temp_k.to_kelvin() == pytest.approx(kelvin, abs=TOLERANCE, rel=0.0)

def test_convert_to() -> None:
    """Tests that the convert_to method returns a new Temperature object"""
    original = Temperature(25, "C")
    converted = original.convert_to("f")

    assert isinstance(converted, Temperature)  # Checks that conversion returns a Temperature object
    assert converted is not original  # Conversion creates a new object
    assert converted.unit == "F"  # The actual result matches with the expected one
    assert converted.value == pytest.approx(77.0, abs=TOLERANCE) 
    assert original.unit == "C"  
    assert original.value == 25.0


# Round-trip conversions
@pytest.mark.parametrize(
    "value",
    [-273.15, -40.0, 0.0, 37.0, 100.0]
)
def test_round_trip(value: float) -> None:
    """Tests a round-trip conversion from Celsius back to Celsius"""
    original = Temperature(value, "C")
    converted = (original.convert_to("F").convert_to("K").convert_to("C"))

    assert converted == original  # Checks that round-trip conversion preserves temperature
    assert converted.unit == original.unit
    assert converted.value == pytest.approx(original.value, abs=TOLERANCE, rel=0.0)


# Cross-unit comparisons
def test_eq() -> None:
    """Tests equality between temperatures with different units"""
    assert Temperature(0.0, "C") == Temperature(32.0, "F")
    assert Temperature(0.0, "C") == Temperature(273.15, "K")

def test_ne() -> None:
    """Tests inequality between different temperatures"""
    # Checks that the 2 values are different
    assert Temperature(25.0, "C") != Temperature(32.0, "F")

def test_lt() -> None:
    """Tests the lower-than comparison"""
    # Checks the lower-than comparisons
    assert Temperature(0.0, "C") < Temperature(98.6, "F")
    assert not Temperature(0.0, "C") < Temperature(32.0, "F")

def test_le() -> None:
    """Tests the lower-than-or-equal-to comparison"""
    assert Temperature(0.0, "C") <= Temperature(32.0, "F")
    assert Temperature(0.0, "C") <= Temperature(300.0, "K")

def test_gt() -> None:
    """Tests the higher-than comparison"""
    assert Temperature(100.0, "C") > Temperature(32.0, "F")
    assert not Temperature(0.0, "C") > Temperature(32.0, "F")

def test_ge() -> None:
    """Tests the higher-than-or-equal comparison"""
    assert Temperature(100.0, "C") >= Temperature(350.15, "K")
    assert Temperature(100.0, "C") >= Temperature(32.0, "F")
    assert Temperature(0.0, "C") >= Temperature(32.0, "F")

def test_tolerance() -> None:
    """Tests comparisons within the floating-point tolerance"""
    temp1 = Temperature(25.0, "C")
    temp2 = Temperature(25.0 + 1e-10, "C")
    temp3 = Temperature(25.0 + 1e-8, "C")

    assert temp1 == temp2  # Checks that the actual result matches the expected one
    assert not temp1 < temp2  # The lower-than comparison
    assert not temp1 > temp2  # The higher-than comparison
    assert temp1 != temp3 
    assert temp1 < temp3

@pytest.mark.parametrize(
    "method",
    ["__eq__", "__ne__", "__lt__", "__le__", "__gt__", "__ge__"]
)
def test_non_temp(method: str) -> None:
    """Tests comparisons with non-Temperature objects"""
    temp = Temperature(25.0, "C")

    # Checks that comparisons with other types are invalid
    assert getattr(temp, method)(25) is NotImplemented


# Formatting
@pytest.mark.parametrize(
    "value, unit, expected",
    [
        (25.0, "C", "25.00 °C"),
        (98.6, "F", "98.60 °F"),
        (273.15, "K", "273.15 K")
    ]
)
def test_str(value: float, unit: str, expected: str) -> None:
    """Tests the human-readable string output"""
    # Checks the temperature format
    assert str(Temperature(value, unit)) == expected

def test_repr() -> None:
    """Tests the unambiguous string output"""
    temp = Temperature(25.0, "C")

    assert repr(temp) == "Temperature(25.0, 'C')"
    