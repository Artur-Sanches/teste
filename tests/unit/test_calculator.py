"""Unit tests for the Calculator module."""

import math

import pytest

from src.calculator import Calculator


class TestCalculatorAdd:
    def test_add_two_positive_numbers(self, calculator: Calculator) -> None:
        assert calculator.add(3, 5) == 8

    def test_add_positive_and_negative(self, calculator: Calculator) -> None:
        assert calculator.add(10, -4) == 6

    def test_add_two_negative_numbers(self, calculator: Calculator) -> None:
        assert calculator.add(-3, -7) == -10

    def test_add_zeros(self, calculator: Calculator) -> None:
        assert calculator.add(0, 0) == 0

    def test_add_floats(self, calculator: Calculator) -> None:
        assert calculator.add(1.5, 2.5) == pytest.approx(4.0)


class TestCalculatorSubtract:
    def test_subtract_positive_numbers(self, calculator: Calculator) -> None:
        assert calculator.subtract(10, 3) == 7

    def test_subtract_resulting_in_negative(self, calculator: Calculator) -> None:
        assert calculator.subtract(3, 10) == -7

    def test_subtract_same_numbers(self, calculator: Calculator) -> None:
        assert calculator.subtract(5, 5) == 0


class TestCalculatorMultiply:
    def test_multiply_two_positives(self, calculator: Calculator) -> None:
        assert calculator.multiply(4, 3) == 12

    def test_multiply_by_zero(self, calculator: Calculator) -> None:
        assert calculator.multiply(100, 0) == 0

    def test_multiply_negative_numbers(self, calculator: Calculator) -> None:
        assert calculator.multiply(-2, -3) == 6

    def test_multiply_floats(self, calculator: Calculator) -> None:
        assert calculator.multiply(2.5, 4.0) == pytest.approx(10.0)


class TestCalculatorDivide:
    def test_divide_exact(self, calculator: Calculator) -> None:
        assert calculator.divide(10, 2) == 5

    def test_divide_resulting_in_float(self, calculator: Calculator) -> None:
        assert calculator.divide(7, 2) == pytest.approx(3.5)

    def test_divide_by_zero_raises(self, calculator: Calculator) -> None:
        with pytest.raises(ValueError, match="Division by zero"):
            calculator.divide(5, 0)

    def test_divide_negative_dividend(self, calculator: Calculator) -> None:
        assert calculator.divide(-10, 2) == -5


class TestCalculatorPower:
    def test_power_positive_exponent(self, calculator: Calculator) -> None:
        assert calculator.power(2, 10) == 1024

    def test_power_zero_exponent(self, calculator: Calculator) -> None:
        assert calculator.power(5, 0) == 1

    def test_power_fraction_exponent(self, calculator: Calculator) -> None:
        assert calculator.power(9, 0.5) == pytest.approx(3.0)


class TestCalculatorSquareRoot:
    def test_square_root_perfect_square(self, calculator: Calculator) -> None:
        assert calculator.square_root(16) == pytest.approx(4.0)

    def test_square_root_of_zero(self, calculator: Calculator) -> None:
        assert calculator.square_root(0) == 0

    def test_square_root_non_perfect_square(self, calculator: Calculator) -> None:
        assert calculator.square_root(2) == pytest.approx(math.sqrt(2))

    def test_square_root_negative_raises(self, calculator: Calculator) -> None:
        with pytest.raises(ValueError, match="negative"):
            calculator.square_root(-1)
