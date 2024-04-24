from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from apps.users.managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=128, unique=True)
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        db_table = "user"

    @property
    def is_staff(self):
        return self.is_admin
