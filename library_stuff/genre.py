import mysql.connector

class Genre:
    def __init__(self, id, genre_name, genre_details):
        self.id = id
        self.genre_name = genre_name
        self.genre_details = genre_details

    def save_to_db(self, cursor):
        cursor.execute(
            "INSERT INTO genres (genre_name, genre_details) VALUES (%s, %s)",
            (self.genre_name, self.genre_details))

    @classmethod
    def find_by_id(cls, cursor, genre_id):
        cursor.execute("SELECT * FROM genres WHERE id = %s", (genre_id,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None
