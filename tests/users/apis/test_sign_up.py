import pytest
from django.urls import reverse

from tests.utils import IsAuthenticateTestCase

pytestmark = pytest.mark.django_db


class TestSignUp(IsAuthenticateTestCase):
    url = reverse("api-users:sign-up")

    def test_sign_up_success(self):
        data = {
            "username": "test",
            "email": "test@test.com",
            "password": "password",
        }

        response = self.client.post(self.url, data=data, format="json")

        assert response.status_code == 201
        assert response.data["data"]["username"] == data["username"]
        assert response.data["data"]["email"] == data["email"]
