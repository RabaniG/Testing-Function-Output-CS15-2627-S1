import pytest


def area_of_triangle(base: float, height: float) -> float:
    """Calculate the area of a triangle.

    :param base: The base length of the triangle.
    :param height: The height of the triangle.
    :return: The calculated area.
    """
    area = 0.5 * base * height
    return area


def average_of_two(a: float, b: float) -> float:
    """Calculate the average of two numbers.

    :param a: The first number.
    :param b: The second number.
    :return: The average of the two numbers.
    """
    average = (a + b) / 2
    return average


def multiply_three(a: float, b: float, c: float) -> float:
    """Multiply three numbers together.

    :param a: The first factor.
    :param b: The second factor.
    :param c: The third factor.
    :return: The product of the three numbers.
    """
    product = a * b * c
    return product


def test_area_of_triangle_integers():
    assert area_of_triangle(10, 4) == 20.0


def test_area_of_triangle_decimals():
    assert pytest.approx(8.8) == area_of_triangle(5.5, 3.2)


def test_average_of_two_integers():
    assert average_of_two(80, 90) == 85.0


def test_average_of_two_decimals():
    assert pytest.approx(87.25) == average_of_two(85.5, 89.0)


def test_multiply_three_integers():
    assert multiply_three(2, 3, 4) == 24


def test_multiply_three_decimals():
    assert pytest.approx(0.006) == multiply_three(0.1, 0.2, 0.3)