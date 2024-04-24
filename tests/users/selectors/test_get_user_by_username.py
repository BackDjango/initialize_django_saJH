import pytest

from apps.users.selectors import UserSelector

pytestmark = pytest.mark.django_db


class TestGetUserByUsername:
    def setup_method(self):
        self._user_selector = UserSelector()

    def test_get_user_by_username_success(self, active_user):
        user = self._user_selector.get_user_by_username(active_user.username)

        assert user == active_user

    def test_get_user_by_username_fail(self):
        user = self._user_selector.get_user_by_username("test")

        assert user is None
