# User Operations:
# ```
# User Operations:
# 1. Add a new user
# 2. View user details
# 3. Display all users
import mysql.connector

class User:
    def __init__(self, id, name, library_id):
        self.id = id
        self.name = name
        self.library_id = library_id

    def save_to_db(self, cursor):
        cursor.execute(
            "INSERT INTO users (name, library_id) VALUES (%s, %s)",
            (self.name, self.library_id))

    @classmethod
    def find_by_id(cls, cursor, user_id):
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None

    @classmethod
    def find_by_library_id(cls, cursor, library_id):
        cursor.execute("SELECT * FROM users WHERE library_id = %s", (library_id,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None
