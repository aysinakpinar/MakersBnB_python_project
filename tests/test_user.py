from lib.user import User

"""
User constructs with an id, name and password
"""
def test_user_constructs():
    user = User(1, "Test Username", "Test Password hash", "Test email", "Test User Role", "Test User created date")
    assert user.user_id == 1
    assert user.user_username == "Test Username"
    assert user.user_password_hash == "Test Password hash"
    assert user.user_email== "Test email"
    assert user.user_role == "Test User Role"
    assert user.user_created_at== "Test User created date"

"""
We can format books to strings nicely
"""
def test_users_format_nicely():
    user = User(1, "Test Username", "Test Password hash", "Test email", "Test User Role", "Test User created date")
    assert str(user) == "User(1, Test Username, Test Password hash, Test email, Test User Role, Test User created date)"
    

"""
We can compare two identical users
And have them be equal
"""
def test_books_are_equal():
    user1 = User(1, "Test Name", "Test Password hash", "Test email", "Test User Role", "Test User created date")
    user2 = User(1, "Test Name", "Test Password hash", "Test email", "Test User Role", "Test User created date")
    assert user1 == user2
