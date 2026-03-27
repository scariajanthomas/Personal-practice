import pytest
from user import User

@pytest.fixture
def user():
    return User("john", "secret123")

@pytest.fixture
def admin_user():
    return User("admin", "password")

@pytest.mark.parametrize("input, expected", [
    ("secret123", True),
    ("qwertyu", False),
    ("", False),
])
def test_validate(user, input, expected):
    assert user.validate(input) == expected


def test_is_admin(admin_user):
    assert admin_user.is_admin() == True

def test_invalid_password(user):
    with pytest.raises(ValueError):
        user.update_password("")

def test_whitespace_password(user):
    with pytest.raises(ValueError):
        user.update_password("   ")
