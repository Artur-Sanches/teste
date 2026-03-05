"""Integration tests – combined workflows across multiple modules."""

import pytest

from src.calculator import Calculator
from src.user_manager import UserManager


class TestCalculatorWorkflow:
    """Tests realistic multi-step calculation scenarios."""

    def test_chained_operations(self, calculator: Calculator) -> None:
        result = calculator.add(
            calculator.multiply(3, 4),
            calculator.divide(10, 2),
        )
        assert result == pytest.approx(17.0)

    def test_tax_calculation(self, calculator: Calculator) -> None:
        price = 200.0
        tax_rate = 0.15
        tax = calculator.multiply(price, tax_rate)
        total = calculator.add(price, tax)
        assert total == pytest.approx(230.0)


class TestUserManagerWorkflow:
    """Tests realistic user management lifecycle scenarios."""

    def test_create_and_deactivate_user(self, user_manager: UserManager) -> None:
        user = user_manager.create_user("Alice", "alice@example.com")
        assert user_manager.list_users(active_only=True) == [user]

        user_manager.deactivate_user(user.id)
        assert user_manager.list_users(active_only=True) == []
        assert user_manager.list_users() == [user]

    def test_multiple_users_only_active_listed(self, user_manager: UserManager) -> None:
        u1 = user_manager.create_user("Alice", "alice@example.com")
        u2 = user_manager.create_user("Bob", "bob@example.com")
        u3 = user_manager.create_user("Carol", "carol@example.com")

        user_manager.deactivate_user(u2.id)

        active = user_manager.list_users(active_only=True)
        assert u1 in active
        assert u3 in active
        assert u2 not in active

    def test_delete_user_frees_email(self, user_manager: UserManager) -> None:
        u1 = user_manager.create_user("Alice", "alice@example.com")
        user_manager.delete_user(u1.id)

        # Same e-mail can now be registered again
        u2 = user_manager.create_user("Alice Reborn", "alice@example.com")
        assert u2.email == "alice@example.com"
