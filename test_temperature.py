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