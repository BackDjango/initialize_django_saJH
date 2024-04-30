from typing import Optional

from django.db.models import Q

from apps.users.models import User


class UserSelector:
    def check_is_exist_user_by_email_or_username(self, email: str, username: str) -> bool:
        return User.objects.filter(Q(email=email) | Q(username=username)).exists()

    def get_user_by_username(self, username: str) -> Optional[User]:
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
