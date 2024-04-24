from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email: str, username: str, password: str, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)  # type: ignore
        user.save()
        return user

    def create_superuser(self, email: str, username: str, password: str, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        return self.create_user(email, username, password, **extra_fields)
