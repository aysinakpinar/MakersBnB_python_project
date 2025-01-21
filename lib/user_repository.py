from lib.user import User

class UserRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all users
    def all(self):
        rows = self._connection.execute('SELECT * from user_details')
        print(rows)
        users = []
        for row in rows:
            item = User(row["user_id"], row["user_username"], row["user_password_hash"], row["user_email"], row["user_role"], row["user_created_at"])
            users.append(item)
        return users
    
    # Create a new user
    def create(self, user):
        self._connection.execute('INSERT INTO user_details (user_username, user_password_hash, user_email, user_role, user_created_at) VALUES (%s, %s, %s, %s, %s)', [
            user.user_username, user.user_password_hash, user.user_email, user.user_role, user.user_created_at])
        return None

    # Find a single user by its user email
    def find(self, user_email):
        rows = self._connection.execute(
            'SELECT * from user_details WHERE user_email = %s', [user_email])
        row = rows[0]
        return User(row["user_id"], row["user_username"], row["user_password_hash"], row["user_email"], row["user_role"], row["user_created_at"])

    # Delete a user by its user email
    def delete(self, user_email):
        self._connection.execute(
            'DELETE FROM user_details WHERE user_email = %s', [user_email])
        return None
    
    # Update a username by its user email
    def update_username(self, user_email, user_username):
        self._connection.execute(
            f"UPDATE user_details SET user_username = '{user_username}' WHERE user_email = {user_email}"
        )
        return None
    
    # Update a user password by its user email
    def update_user_password(self, user_email, user_password_hash):
        self._connection.execute(
            f"UPDATE user_details SET user_password_hash = '{user_password_hash}' WHERE user_email = {user_email}"
        )
        return None
    