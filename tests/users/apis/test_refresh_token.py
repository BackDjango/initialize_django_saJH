import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from tests.utils import IsAuthenticateTestCase

pytestmark = pytest.mark.django_db


class TestRefreshToken(IsAuthenticateTestCase):
    url = reverse("api-users:refresh-token")

    def test_refresh_token_success(self, active_user):
        data = {
            "refresh": str(RefreshToken.for_user(active_user)),
        }

        response = self.client.post(self.url, data=data, format="json")

        assert response.status_code == 200
        assert response.data["data"]["access_token"] is not None

    def test_refresh_token_fail(self):
        data = {
            "refresh": "test",
        }

        response = self.client.post(self.url, data=data, format="json")

        assert response.status_code == 401
        assert response.data["message"] == "토큰이 만료 또는 유효하지 않습니다."
        assert response.data["code"] == "invalid_token"
