# Testing temperature methods and attributes
import pytest

from temperature import Temperature

TOLERANCE = 1e-9


# Initialisation
def test_default_unit() -> None:
    """Tests that Celsius is the default unit"""
    temperature = Temperature(25)

    assert temperature.value == 25.0
    assert temperature.unit == "C"

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
    temperature = Temperature(25, unit)

    assert temperature.unit == expected

def test_read_onlys() -> None:
    """Tests that the temperature attributes are read-only"""
    temperature = Temperature(25, "C")

    with pytest.raises(AttributeError):
        temperature.value = 30

    with pytest.raises(AttributeError):
        temperature.unit = "F"


# Validation
@pytest.mark.parametrize("unit", ["X", "ABC", "", "Kelvin"])
def test_invalid_unit(unit: str) -> None:
    """Tests that invalid units raises ValueError"""
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
    temperature = Temperature(25, "C")

    with pytest.raises(ValueError):
        temperature.convert_to("X")


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

    assert isinstance(converted, Temperature)
    assert converted is not original
    assert converted.unit == "F"
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

    assert converted == original
    assert converted.unit == original.unit
    assert converted.value == pytest.approx(original.value, abs=TOLERANCE, rel=0.0)

    