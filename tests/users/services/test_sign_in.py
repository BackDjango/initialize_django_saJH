import pytest

from apps.commons.exceptions import AuthenticationFailedException
from apps.users.services import UserService

pytestmark = pytest.mark.django_db


class TestCreateUser:
    def setup_method(self):
        self._user_service = UserService()

    def test_sign_in_success(self, active_user):
        username = active_user.username
        password = "password"

        tokens = self._user_service.sign_in(
            username=username,
            password=password,
        )

        assert tokens["access_token"] is not None
        assert tokens["refresh_token"] is not None

    def test_sign_in_fail_password(self, active_user):
        username = active_user.username
        password = "password1"

        with pytest.raises(AuthenticationFailedException) as e:
            self._user_service.sign_in(
                username=username,
                password=password,
            )

        assert str(e.value) == "아이디 또는 비밀번호가 일치하지 않습니다."
        assert isinstance(e.value, AuthenticationFailedException)

    def test_sign_in_fail_username(self, active_user):
        username = "test"
        password = "password"

        with pytest.raises(AuthenticationFailedException) as e:
            self._user_service.sign_in(
                username=username,
                password=password,
            )

        assert str(e.value) == "아이디 또는 비밀번호가 일치하지 않습니다."
        assert isinstance(e.value, AuthenticationFailedException)

    def test_sign_in_fail_inactive(self, inactive_user):
        username = inactive_user.username
        password = "password"

        with pytest.raises(AuthenticationFailedException) as e:
            self._user_service.sign_in(
                username=username,
                password=password,
            )

        assert str(e.value) == "아이디 또는 비밀번호가 일치하지 않습니다."
        assert isinstance(e.value, AuthenticationFailedException)
