"""Unit tests for the UserManager module."""

import pytest

from src.user_manager import User, UserManager


class TestUserCreation:
    def test_create_user_returns_user_object(self, user_manager: UserManager) -> None:
        user = user_manager.create_user("Alice", "alice@example.com")
        assert isinstance(user, User)

    def test_created_user_has_correct_name(self, user_manager: UserManager) -> None:
        user = user_manager.create_user("Alice", "alice@example.com")
        assert user.name == "Alice"

    def test_created_user_has_correct_email(self, user_manager: UserManager) -> None:
        user = user_manager.create_user("Alice", "alice@example.com")
        assert user.email == "alice@example.com"

    def test_created_user_is_active_by_default(self, user_manager: UserManager) -> None:
        user = user_manager.create_user("Alice", "alice@example.com")
        assert user.active is True

    def test_created_users_have_sequential_ids(self, user_manager: UserManager) -> None:
        u1 = user_manager.create_user("Alice", "alice@example.com")
        u2 = user_manager.create_user("Bob", "bob@example.com")
        assert u2.id == u1.id + 1

    def test_create_user_empty_name_raises(self, user_manager: UserManager) -> None:
        with pytest.raises(ValueError, match="name"):
            user_manager.create_user("", "valid@example.com")

    def test_create_user_empty_email_raises(self, user_manager: UserManager) -> None:
        with pytest.raises(ValueError, match="e-mail"):
            user_manager.create_user("Alice", "")

    def test_create_user_invalid_email_raises(self, user_manager: UserManager) -> None:
        with pytest.raises(ValueError, match="Invalid e-mail"):
            user_manager.create_user("Alice", "not-an-email")

    def test_create_user_duplicate_email_raises(self, user_manager: UserManager) -> None:
        user_manager.create_user("Alice", "alice@example.com")
        with pytest.raises(ValueError, match="already registered"):
            user_manager.create_user("Another Alice", "alice@example.com")


class TestGetUser:
    def test_get_existing_user(self, user_manager: UserManager) -> None:
        created = user_manager.create_user("Alice", "alice@example.com")
        fetched = user_manager.get_user(created.id)
        assert fetched == created

    def test_get_nonexistent_user_returns_none(self, user_manager: UserManager) -> None:
        assert user_manager.get_user(999) is None


class TestListUsers:
    def test_list_all_users(self, populated_user_manager: UserManager) -> None:
        users = populated_user_manager.list_users()
        assert len(users) == 3

    def test_list_active_only(self, populated_user_manager: UserManager) -> None:
        users = populated_user_manager.list_users()
        populated_user_manager.deactivate_user(users[0].id)
        active = populated_user_manager.list_users(active_only=True)
        assert len(active) == 2
        assert all(u.active for u in active)

    def test_empty_manager_returns_empty_list(self, user_manager: UserManager) -> None:
        assert user_manager.list_users() == []


class TestDeactivateUser:
    def test_deactivate_marks_user_inactive(self, user_manager: UserManager) -> None:
        user = user_manager.create_user("Alice", "alice@example.com")
        user_manager.deactivate_user(user.id)
        assert user_manager.get_user(user.id).active is False

    def test_deactivate_nonexistent_user_raises(self, user_manager: UserManager) -> None:
        with pytest.raises(KeyError):
            user_manager.deactivate_user(999)


class TestDeleteUser:
    def test_delete_removes_user(self, user_manager: UserManager) -> None:
        user = user_manager.create_user("Alice", "alice@example.com")
        user_manager.delete_user(user.id)
        assert user_manager.get_user(user.id) is None

    def test_delete_nonexistent_user_raises(self, user_manager: UserManager) -> None:
        with pytest.raises(KeyError):
            user_manager.delete_user(999)
