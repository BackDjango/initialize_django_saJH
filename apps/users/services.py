from rest_framework_simplejwt.tokens import RefreshToken

from apps.commons.exceptions import AlreadyExistException
from apps.users.models import User
from apps.users.selectors import UserSelector


class UserService:
    def _get_tokens_for_user(self, user: User) -> dict[str, str]:
        refresh = RefreshToken.for_user(user)

        return {
            "refresh_token": str(refresh),
            "access_token": str(refresh.access_token),  # type: ignore
        }

    def create_user(self, email: str, password: str, username: str) -> User:
        user_selector = UserSelector()

        if user_selector.check_is_exist_user_by_email_or_username(email=email, username=username):
            raise AlreadyExistException("이미 존재하는 아이디 또는 이메일입니다.")

        user = User.objects.create_user(email=email, password=password, username=username)

        return user

    def sign_in(self, username: str, password: str) -> dict[str, str]:
        user_selector = UserSelector()

        user = user_selector.get_user_by_username(username=username)

        if user is None or not user.is_active or not user.check_password(password):
            raise AlreadyExistException("아이디 또는 비밀번호가 일치하지 않습니다.")

        tokens = self._get_tokens_for_user(user)
        return tokens
