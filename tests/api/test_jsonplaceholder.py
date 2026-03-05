"""API tests – exercises the JSONPlaceholder public REST API.

These tests demonstrate how to write HTTP-level automation tests
using the ``requests`` library and ``pytest``.  They hit a real
(but free) external API; if you need fully isolated tests, replace
``BASE_URL`` with a mock server or a VCR cassette.
"""

import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="module")
def session() -> requests.Session:
    """Return a shared ``requests.Session`` for all API tests."""
    with requests.Session() as s:
        yield s


class TestGetPosts:
    def test_list_posts_returns_200(self, session: requests.Session) -> None:
        response = session.get(f"{BASE_URL}/posts")
        assert response.status_code == 200

    def test_list_posts_returns_json_list(self, session: requests.Session) -> None:
        response = session.get(f"{BASE_URL}/posts")
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

    def test_get_single_post_returns_200(self, session: requests.Session) -> None:
        response = session.get(f"{BASE_URL}/posts/1")
        assert response.status_code == 200

    def test_get_single_post_has_required_fields(
        self, session: requests.Session
    ) -> None:
        response = session.get(f"{BASE_URL}/posts/1")
        post = response.json()
        for field in ("id", "userId", "title", "body"):
            assert field in post, f"Missing field: {field}"

    def test_get_nonexistent_post_returns_404(
        self, session: requests.Session
    ) -> None:
        response = session.get(f"{BASE_URL}/posts/99999")
        assert response.status_code == 404


class TestCreatePost:
    def test_create_post_returns_201(self, session: requests.Session) -> None:
        payload = {"title": "Automation Test", "body": "Created via pytest", "userId": 1}
        response = session.post(f"{BASE_URL}/posts", json=payload)
        assert response.status_code == 201

    def test_create_post_returns_body(self, session: requests.Session) -> None:
        payload = {"title": "Automation Test", "body": "Created via pytest", "userId": 1}
        response = session.post(f"{BASE_URL}/posts", json=payload)
        data = response.json()
        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert "id" in data


class TestUpdatePost:
    def test_update_post_returns_200(self, session: requests.Session) -> None:
        payload = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
        response = session.put(f"{BASE_URL}/posts/1", json=payload)
        assert response.status_code == 200

    def test_patch_post_returns_200(self, session: requests.Session) -> None:
        response = session.patch(f"{BASE_URL}/posts/1", json={"title": "Patched"})
        assert response.status_code == 200


class TestDeletePost:
    def test_delete_post_returns_200(self, session: requests.Session) -> None:
        response = session.delete(f"{BASE_URL}/posts/1")
        assert response.status_code == 200
