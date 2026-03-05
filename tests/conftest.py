"""Shared pytest fixtures available to all tests."""

import pytest

from src.calculator import Calculator
from src.user_manager import UserManager


@pytest.fixture
def calculator() -> Calculator:
    """Return a fresh Calculator instance."""
    return Calculator()


@pytest.fixture
def user_manager() -> UserManager:
    """Return a fresh UserManager instance."""
    return UserManager()


@pytest.fixture
def populated_user_manager(user_manager: UserManager) -> UserManager:
    """Return a UserManager pre-populated with three users."""
    user_manager.create_user("Alice Silva", "alice@example.com")
    user_manager.create_user("Bob Santos", "bob@example.com")
    user_manager.create_user("Carol Lima", "carol@example.com")
    return user_manager
