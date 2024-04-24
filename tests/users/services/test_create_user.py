import pytest
from django.contrib.auth.hashers import check_password

from apps.commons.exceptions import AlreadyExistException
from apps.users.services import UserService

pytestmark = pytest.mark.django_db


class TestCreateUser:
    def setup_method(self):
        self._user_service = UserService()

    def test_create_user_success(self):
        email = "test@test.com"
        username = "테스트"
        password = "test1234"

        user = self._user_service.create_user(
            email=email,
            username=username,
            password=password,
        )

        assert user.email == email
        assert user.username == username
        assert check_password(password, user.password)

    def test_create_user_fail_already_exist_email(self, active_user):
        email = active_user.email
        username = "테스트"
        password = "test1234"

        with pytest.raises(AlreadyExistException) as e:
            self._user_service.create_user(
                email=email,
                username=username,
                password=password,
            )

        assert str(e.value) == "이미 존재하는 아이디 또는 이메일입니다."
        assert isinstance(e.value, AlreadyExistException)

    def test_create_user_fail_already_exist_username(self, active_user):
        email = "test@test.com"
        username = active_user.username
        password = "test1234"

        with pytest.raises(AlreadyExistException) as e:
            self._user_service.create_user(
                email=email,
                username=username,
                password=password,
            )

        assert str(e.value) == "이미 존재하는 아이디 또는 이메일입니다."
        assert isinstance(e.value, AlreadyExistException)
