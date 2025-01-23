from lib.user_repository import UserRepository
from lib.user import User
from datetime import datetime
import bcrypt
"""
When we call UserRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_get_all_users(db_connection): 
    # Seed the database with test data
    db_connection.seed("seeds/makers_bnb_seed.sql")

    # Create a new UserRepository
    repository = UserRepository(db_connection)

    # Retrieve all users
    users = repository.all()

    for user in users:
        # Verify the created_at field
        assert user.user_created_at is not None
        assert isinstance(user.user_created_at, datetime)

    # Dynamically verify the data against the test records
    expected_users = [
        User(1, 'john_doe', '$2a$12$X5qvZad9iXsT1fnjFvjqNuESs0U6hKFH3w55dPAdIu5G75E0Q2iK', 'john.doe@example.com', 'user', users[0].user_created_at),
        User(2, 'alice_smith', '$2a$12$8dbW8ZCqzJjzDwFJ7tLg/d6N7OrC6Eczw8w0YhS6nVppGKmjNNO5q', 'alice.smith@example.com', 'host', users[1].user_created_at),
        User(3, 'bob_jones', '$2a$12$R6vsG0.r1tJHGmRzR5lFdL/29KQmdErfuLrD9k2l3TKHqS7zEy/oq', 'bob.jones@example.com', 'user', users[2].user_created_at),
        User(4, 'susan_lee', '$2a$12$w.mgVZy3cFdyU5NoVJ7gsdkjfN1OAxY4h./RHKZIM6aP2L5ouAA9S', 'susan.lee@example.com', 'host', users[3].user_created_at),
        User(5, 'mike_brown', '$2a$12$kjJovGn1Uvc5sg6me5RgI4C/zmfuWo8u3.IJajDkzjRkj0ZK5L6y6', 'mike.brown@example.com', 'user', users[4].user_created_at),
    ]

    assert users == expected_users

"""
When we call UserRepository#create
We get a new user in the database.
"""
def test_create_user(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "aysinakpinar", '$2a$12$kjJovGn1Uvc5sg6me5RgI4C/zmfuWo8u3.IJajDkzjRkj0ZK5L6y654', 'aysinakpinar@gmail.com', 'user', "2025/01/20"))

    users = repository.all()

    assert users == [
        User(1, 'john_doe', '$2a$12$X5qvZad9iXsT1fnjFvjqNuESs0U6hKFH3w55dPAdIu5G75E0Q2iK', 'john.doe@example.com', 'user', users[0].user_created_at),
        User(2, 'alice_smith', '$2a$12$8dbW8ZCqzJjzDwFJ7tLg/d6N7OrC6Eczw8w0YhS6nVppGKmjNNO5q', 'alice.smith@example.com', 'host', users[1].user_created_at),
        User(3, 'bob_jones', '$2a$12$R6vsG0.r1tJHGmRzR5lFdL/29KQmdErfuLrD9k2l3TKHqS7zEy/oq', 'bob.jones@example.com', 'user', users[2].user_created_at),
        User(4, 'susan_lee', '$2a$12$w.mgVZy3cFdyU5NoVJ7gsdkjfN1OAxY4h./RHKZIM6aP2L5ouAA9S', 'susan.lee@example.com', 'host', users[3].user_created_at),
        User(5, 'mike_brown', '$2a$12$kjJovGn1Uvc5sg6me5RgI4C/zmfuWo8u3.IJajDkzjRkj0ZK5L6y6', 'mike.brown@example.com', 'user', users[4].user_created_at),
        User(6, 'aysinakpinar', '$2a$12$kjJovGn1Uvc5sg6me5RgI4C/zmfuWo8u3.IJajDkzjRkj0ZK5L6y654', 'aysinakpinar@gmail.com', 'user', datetime(2025, 1, 20, 0, 0))
    ]

def test_delete_user(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = UserRepository(db_connection)

    repository.delete("aysinakpinar@gmail.com")

    users = repository.all()

    assert users == [
        User(1, 'john_doe', '$2a$12$X5qvZad9iXsT1fnjFvjqNuESs0U6hKFH3w55dPAdIu5G75E0Q2iK', 'john.doe@example.com', 'user', users[0].user_created_at),
        User(2, 'alice_smith', '$2a$12$8dbW8ZCqzJjzDwFJ7tLg/d6N7OrC6Eczw8w0YhS6nVppGKmjNNO5q', 'alice.smith@example.com', 'host', users[1].user_created_at),
        User(3, 'bob_jones', '$2a$12$R6vsG0.r1tJHGmRzR5lFdL/29KQmdErfuLrD9k2l3TKHqS7zEy/oq', 'bob.jones@example.com', 'user', users[2].user_created_at),
        User(4, 'susan_lee', '$2a$12$w.mgVZy3cFdyU5NoVJ7gsdkjfN1OAxY4h./RHKZIM6aP2L5ouAA9S', 'susan.lee@example.com', 'host', users[3].user_created_at),
        User(5, 'mike_brown', '$2a$12$kjJovGn1Uvc5sg6me5RgI4C/zmfuWo8u3.IJajDkzjRkj0ZK5L6y6', 'mike.brown@example.com', 'user', users[4].user_created_at)
    ]

def test_update_username(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = UserRepository(db_connection)

    repository.update_username('mike.brown@example.com','m_brown')

    users = repository.all()

    assert users == [
        User(1, 'john_doe', '$2a$12$X5qvZad9iXsT1fnjFvjqNuESs0U6hKFH3w55dPAdIu5G75E0Q2iK', 'john.doe@example.com', 'user', users[0].user_created_at),
        User(2, 'alice_smith', '$2a$12$8dbW8ZCqzJjzDwFJ7tLg/d6N7OrC6Eczw8w0YhS6nVppGKmjNNO5q', 'alice.smith@example.com', 'host', users[1].user_created_at),
        User(3, 'bob_jones', '$2a$12$R6vsG0.r1tJHGmRzR5lFdL/29KQmdErfuLrD9k2l3TKHqS7zEy/oq', 'bob.jones@example.com', 'user', users[2].user_created_at),
        User(4, 'susan_lee', '$2a$12$w.mgVZy3cFdyU5NoVJ7gsdkjfN1OAxY4h./RHKZIM6aP2L5ouAA9S', 'susan.lee@example.com', 'host', users[3].user_created_at),
        User(5, 'm_brown', '$2a$12$kjJovGn1Uvc5sg6me5RgI4C/zmfuWo8u3.IJajDkzjRkj0ZK5L6y6', 'mike.brown@example.com', 'user', users[4].user_created_at)
    ]

def test_update_user_password(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = UserRepository(db_connection)

    # Update the user password
    new_password = 'new_secure_password123'
    repository.update_user_password('mike.brown@example.com', new_password)
    
    # all users from the repository
    users = repository.all()

    # Find the updated user
    updated_user = next(user for user in users if user.user_email == 'mike.brown@example.com')

    # Verify the password hash matches the new password
    assert bcrypt.checkpw(new_password.encode('utf-8'), updated_user.user_password_hash.encode('utf-8'))

    # Verify other users' data remains unchanged
    assert users[:4] == [
        User(1, 'john_doe', '$2a$12$X5qvZad9iXsT1fnjFvjqNuESs0U6hKFH3w55dPAdIu5G75E0Q2iK', 'john.doe@example.com', 'user', users[0].user_created_at),
        User(2, 'alice_smith', '$2a$12$8dbW8ZCqzJjzDwFJ7tLg/d6N7OrC6Eczw8w0YhS6nVppGKmjNNO5q', 'alice.smith@example.com', 'host', users[1].user_created_at),
        User(3, 'bob_jones', '$2a$12$R6vsG0.r1tJHGmRzR5lFdL/29KQmdErfuLrD9k2l3TKHqS7zEy/oq', 'bob.jones@example.com', 'user', users[2].user_created_at),
        User(4, 'susan_lee', '$2a$12$w.mgVZy3cFdyU5NoVJ7gsdkjfN1OAxY4h./RHKZIM6aP2L5ouAA9S', 'susan.lee@example.com', 'host', users[3].user_created_at)
    ]

def test_update_user_email(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = UserRepository(db_connection)

    repository.update_user_email('mike.brown@example.com', 'mike_brown@example.com')

    users = repository.all()

    assert users == [
        User(1, 'john_doe', '$2a$12$X5qvZad9iXsT1fnjFvjqNuESs0U6hKFH3w55dPAdIu5G75E0Q2iK', 'john.doe@example.com', 'user', users[0].user_created_at),
        User(2, 'alice_smith', '$2a$12$8dbW8ZCqzJjzDwFJ7tLg/d6N7OrC6Eczw8w0YhS6nVppGKmjNNO5q', 'alice.smith@example.com', 'host', users[1].user_created_at),
        User(3, 'bob_jones', '$2a$12$R6vsG0.r1tJHGmRzR5lFdL/29KQmdErfuLrD9k2l3TKHqS7zEy/oq', 'bob.jones@example.com', 'user', users[2].user_created_at),
        User(4, 'susan_lee', '$2a$12$w.mgVZy3cFdyU5NoVJ7gsdkjfN1OAxY4h./RHKZIM6aP2L5ouAA9S', 'susan.lee@example.com', 'host', users[3].user_created_at),
        User(5, 'mike_brown', '$2a$12$kjJovGn1Uvc5sg6me5RgI4C/zmfuWo8u3.IJajDkzjRkj0ZK5L6y6', 'mike_brown@example.com', 'user', users[4].user_created_at)
    ]