import pytest
from user import User

def test_validate_correct_password():
    user = User("john", "secret123")
    assert user.validate("secret123") == True

def test_validate_wrong_password():
    user = User("john", "secret123")
    assert user.validate("qwertyu") == False

def test_is_admin():
    user = User("admin", "secret123")
    assert user.is_admin() == True

def test_invalid_password():
    user = User("spectra", "pass123")
    with pytest.raises(ValueError):
        user.update_password("")

def test_whitespace_password():
    user = User("spectra", "pass123")
    with pytest.raises(ValueError):
        user.update_password("   ")