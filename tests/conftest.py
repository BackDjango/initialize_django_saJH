import pytest
from rest_framework.test import APIClient

from tests.factories import BoardsFactory, UserFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def active_user(db):
    return UserFactory(
        is_active=True,
        is_admin=False,
    )


@pytest.fixture
def admin_user(db):
    return UserFactory(
        is_active=True,
        is_admin=True,
    )


@pytest.fixture
def inactive_user(db):
    return UserFactory(
        is_active=False,
        is_admin=False,
    )


@pytest.fixture
def board(db, active_user):
    return BoardsFactory(
        author=active_user,
    )
