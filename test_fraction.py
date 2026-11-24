# Testing fraction methods and attributes
import pytest

from fraction import Fraction


# Initialisation
def test_init() -> None:
    """Tests the initialisation of a fraction"""
    frac = Fraction(5, 6)

    assert frac.numerator == 5
    assert frac.denominator == 6

@pytest.mark.parametrize(
    "numerator, denominator, expected_num, expected_den",
    [
        (6, 8, 3, 4),
        (10, 20, 1, 2),
        (-6, 8, -3, 4),
        (0, 5, 0, 1),
        (3, 4, 3, 4)
    ]
)
def test_simpli(numerator: int, denominator: int, expected_num: int, expected_den: int) -> None:
    """Tests that fractions are simplified correctly"""
    frac = Fraction(numerator, denominator)

    assert frac.numerator == expected_num
    assert frac.denominator == expected_den

def test_read_onlys() -> None:
    """Tests that the fraction attributes are read-only"""
    frac = Fraction(5, 6)

    with pytest.raises(AttributeError):
        frac.numerator = 5

    with pytest.raises(AttributeError):
        frac.denominator = 6


# Validation
@pytest.mark.parametrize(
    "numerator, denominator",
    [
        (1.5, 2),
        (1, 2.5),
        ("1", 2),
        (1, "2"),
        (True, 2)
    ]
)
def test_invalids(numerator: object, denominator: object) -> None:
    """Tests that non-integer values raise TypeError"""
    with pytest.raises(TypeError):
        Fraction(numerator, denominator)

@pytest.mark.parametrize("denominator", [0, -1, -5])
def test_invalid_den(denominator: int) -> None:
    """Tests that non-positive denominators raise ValueError"""
    with pytest.raises(ValueError):
        Fraction(1, denominator)


