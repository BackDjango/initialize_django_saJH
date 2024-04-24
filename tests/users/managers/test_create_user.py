import pytest
from django.contrib.auth.hashers import check_password

from apps.users.models import User

pytestmark = pytest.mark.django_db


class TestCreateUser:
    def test_create_user_success(self):
        email = "test@test.com"
        username = "테스트"
        password = "test1234"

        user = User.objects.create_user(
            email=email,
            username=username,
            password=password,
        )

        assert user.email == email
        assert check_password(password, user.password)
        assert user.username == username
