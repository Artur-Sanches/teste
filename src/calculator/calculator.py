"""Simple calculator module used as a sample for automation testing."""


class Calculator:
    """Provides basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Return the sum of *a* and *b*."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of *a* minus *b*."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return the product of *a* and *b*."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Return the quotient of *a* divided by *b*.

        Raises:
            ValueError: If *b* is zero.
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        """Return *base* raised to *exponent*."""
        return base ** exponent

    def square_root(self, n: float) -> float:
        """Return the square root of *n*.

        Raises:
            ValueError: If *n* is negative.
        """
        if n < 0:
            raise ValueError("Square root of a negative number is not defined.")
        return n ** 0.5
