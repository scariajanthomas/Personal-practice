import pytest
from user import User, AdminUser

@pytest.fixture
def user():
    return User("john", "secret123")

@pytest.fixture
def admin_user():
    return AdminUser("admin", "password")

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
        user.update_password(" ")

def test_change_username(admin_user):
    admin_user.change_username("new_name")
    assert admin_user.username == "new_name"

def test_change_username_empty(admin_user):
    with pytest.raises(ValueError):
        admin_user.change_username("")

def test_change_username_whitespace(admin_user):
    with pytest.raises(ValueError):
        admin_user.change_username(" ")



def test_delete_user(admin_user):
    admin_user.delete_user("alice")

def test_delete_nonuser(admin_user):
    with pytest.raises(ValueError):
        admin_user.update_password("")


user_list = [User("alice", "pass1"), User("bob", "pass2")]


