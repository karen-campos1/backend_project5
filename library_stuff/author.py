import mysql.connector

class Author:
    def __init__(self, id, name, biography):
        self.id = id
        self.name = name
        self.biography = biography

    def save_to_db(self, cursor):
        cursor.execute(
            "INSERT INTO authors (name, biography) VALUES (%s, %s)",
            (self.name, self.biography))

    @classmethod
    def find_by_id(cls, cursor, author_id):
        cursor.execute("SELECT * FROM authors WHERE id = %s", (author_id,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None
