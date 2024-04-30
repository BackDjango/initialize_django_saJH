import pytest

from apps.users.selectors import UserSelector

pytestmark = pytest.mark.django_db


class TestCheckIsExistUserByEmailOrUsername:
    def setup_method(self):
        self._user_selector = UserSelector()

    def test_check_is_exist_user_by_email_or_username_success(self, active_user):
        is_exist = self._user_selector.check_is_exist_user_by_email_or_username(active_user.email, active_user.username)

        assert is_exist is True

    def test_check_is_exist_user_by_email_or_username_fail(self):
        is_exist = self._user_selector.check_is_exist_user_by_email_or_username("test@test.com", "test")

        assert is_exist is False
