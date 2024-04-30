import pytest
from django.urls import reverse

from tests.utils import IsAuthenticateTestCase

pytestmark = pytest.mark.django_db


class TestSignIn(IsAuthenticateTestCase):
    url = reverse("api-users:sign-in")

    def test_sign_up_success(self, active_user):
        data = {
            "username": active_user.username,
            "password": "password",
        }

        response = self.client.post(self.url, data=data, format="json")

        assert response.status_code == 200
        assert response.data["data"]["access_token"] is not None
        assert response.data["data"]["refresh_token"] is not None
