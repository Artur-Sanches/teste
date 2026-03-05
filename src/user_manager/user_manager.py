"""User manager module used as a sample for automation testing."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class User:
    """Represents a user in the system."""

    id: int
    name: str
    email: str
    active: bool = True


class UserManager:
    """Manages a collection of users (in-memory store)."""

    def __init__(self) -> None:
        self._users: Dict[int, User] = {}
        self._next_id: int = 1

    def create_user(self, name: str, email: str) -> User:
        """Create and store a new user.

        Args:
            name: Full name of the user.
            email: E-mail address of the user.

        Raises:
            ValueError: If *name* or *email* are empty, or if the e-mail is
                already registered.
        """
        if not name or not name.strip():
            raise ValueError("User name cannot be empty.")
        if not email or not email.strip():
            raise ValueError("User e-mail cannot be empty.")
        if "@" not in email:
            raise ValueError(f"Invalid e-mail address: {email!r}")
        if any(u.email == email for u in self._users.values()):
            raise ValueError(f"E-mail {email!r} is already registered.")

        user = User(id=self._next_id, name=name.strip(), email=email.strip())
        self._users[self._next_id] = user
        self._next_id += 1
        return user

    def get_user(self, user_id: int) -> Optional[User]:
        """Return the user with the given *user_id*, or ``None``."""
        return self._users.get(user_id)

    def list_users(self, active_only: bool = False) -> List[User]:
        """Return all users, optionally filtered to active ones."""
        users = list(self._users.values())
        if active_only:
            users = [u for u in users if u.active]
        return users

    def deactivate_user(self, user_id: int) -> User:
        """Deactivate the user with the given *user_id*.

        Raises:
            KeyError: If no user with *user_id* exists.
        """
        user = self._users.get(user_id)
        if user is None:
            raise KeyError(f"User with id={user_id} not found.")
        user.active = False
        return user

    def delete_user(self, user_id: int) -> None:
        """Permanently delete the user with the given *user_id*.

        Raises:
            KeyError: If no user with *user_id* exists.
        """
        if user_id not in self._users:
            raise KeyError(f"User with id={user_id} not found.")
        del self._users[user_id]
