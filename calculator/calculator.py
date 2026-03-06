import math


def square_root(num: float) -> float:
    if not isinstance(num, (int, float)):
        raise TypeError("num must be int or float")

    if num < 0:
        raise ValueError("Cannot take square root of negative number")

    return math.sqrt(num)


def factorial(num: int) -> int:
    if not isinstance(num, int):
        raise TypeError("num must be an integer")

    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    result = 1
    for i in range(1, num + 1):
        result *= i

    return result


def natural_log(num: float) -> float:
    if not isinstance(num, (int, float)):
        raise TypeError("num must be int or float")

    if num <= 0:
        raise ValueError("Logarithm only defined for positive numbers")

    return math.log(num)


def power_function(base: float, exponent: float) -> float:
    if not isinstance(base, (int, float)):
        raise TypeError("base must be int or float")

    if not isinstance(exponent, (int, float)):
        raise TypeError("exponent must be int or float")

    return math.pow(base, exponent)