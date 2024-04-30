import factory
from django.contrib.auth.hashers import make_password
from faker import Faker

from apps.boards.models import Board
from apps.users.models import User

faker = Faker("ko_KR")


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.LazyAttribute(lambda _: faker.unique.email())
    username = factory.LazyAttribute(lambda _: faker.name())
    password = factory.LazyAttribute(lambda _: make_password("password"))

    class Meta:
        model = User

    @factory.post_generation
    def is_admin(self, create, extracted, **kwargs):
        if isinstance(extracted, bool):
            self.is_admin = extracted
        else:
            self.is_admin = False

    @factory.post_generation
    def is_active(self, create, extracted, **kwargs):
        if isinstance(extracted, bool):
            self.is_active = extracted
        else:
            self.is_active = True


class BoardFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda _: faker.sentence())
    content = factory.LazyAttribute(lambda _: faker.text())
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Board
