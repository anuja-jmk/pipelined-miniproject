import pytest
from calculator import square_root, factorial, natural_log, power_function


def test_square_root():
    assert square_root(16) == 4.0
    assert square_root(9) == 3.0


def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-4)


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 23


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)


def test_natural_log():
    assert natural_log(1) == 0.0


def test_natural_log_invalid():
    with pytest.raises(ValueError):
        natural_log(0)


def test_power_function():
    assert power_function(2, 3) == 8.0
    assert power_function(5, 2) == 25.0