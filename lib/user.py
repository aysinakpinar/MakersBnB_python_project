class User:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, user_id, user_username, user_password_hash, user_email, user_role, user_created_at):
        self.user_id = user_id
        self.user_username= user_username
        self.user_password_hash = user_password_hash
        self.user_email = user_email
        self.user_role = user_role
        self.user_created_at = user_created_at

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"User({self.user_id}, {self.user_username}, {self.user_password_hash}, {self.user_email}, {self.user_role}, {self.user_created_at})"
