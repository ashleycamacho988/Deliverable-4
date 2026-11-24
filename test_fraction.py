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


# Arithmetic operations
@pytest.mark.parametrize(
    "frac1, frac2, expected",
    [
        (Fraction(1, 2), Fraction(3, 4), Fraction(5, 4)),
        (Fraction(1, 2), Fraction(1, 2), Fraction(1, 1)) 
    ]
)
def test_add(frac1: Fraction, frac2: Fraction, expected: Fraction) -> None:
    """Tests addition between fractions"""
    assert frac1 + frac2 == expected 

@pytest.mark.parametrize(
    "frac1, frac2, expected",
    [
        (Fraction(3, 4), Fraction(1, 2), Fraction(1, 4)),
        (Fraction(1, 2), Fraction(3, 4), Fraction(-1, 4)),
        (Fraction(1, 2), Fraction(1, 2), Fraction(0, 1)) 
    ]
)
def test_sub(frac1: Fraction, frac2: Fraction, expected: Fraction) -> None:
    """Tests subtraction between fractions"""
    assert frac1 - frac2 == expected 


# Comparisons
def test_eq() -> None:
    """Tests equality between fractions"""
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(3, 4) == Fraction(6, 8)

def test_ne() -> None:
    """Tests inequality between fractions"""
    assert Fraction(1, 2) != Fraction(3, 4)

def test_lt() -> None:
    """Tests the smaller-than comparison"""
    assert Fraction(1, 3) < Fraction(1, 2)
    assert not Fraction(3, 4) < Fraction(6, 8)

def test_le() -> None:
    """Tests the smaller-than-or-equal-to comparison"""
    assert Fraction(1, 3) <= Fraction(1, 2)
    assert Fraction(1, 2) <= Fraction(2, 4)

def test_gt() -> None:
    """Tests the greater-than comparison"""
    assert Fraction(3, 4) > Fraction(1, 2)
    assert not Fraction(1, 2) > Fraction(2, 4)

def test_ge() -> None:
    """Tests the greater-than-or-equal comparison"""
    assert Fraction(3, 4) >= Fraction(1, 2)
    assert Fraction(1, 2) >= Fraction(2, 4)
    
@pytest.mark.parametrize(
    "method",
    ["__eq__", "__ne__", "__lt__", "__le__", "__gt__", "__ge__"]
)
def test_non_frac_comparison(method: str) -> None:
    """Tests comparisons with non-fractions"""
    frac = Fraction(1, 2)

    assert getattr(frac, method)(2) is NotImplemented

@pytest.mark.parametrize("method", ["__add__", "__sub__"])
def test_invalid_arith(method: str) -> None:
    """Tests arithmetic operations with non-fractions"""
    frac = Fraction(1, 2)

    assert getattr(frac, method)(2) is NotImplemented


