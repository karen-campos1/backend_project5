import mysql.connector

class Book:
    def __init__(self, id, title, author_id, genre_id, isbn, publication_date, availability=True):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publication_date = publication_date
        self.availability = availability

    def save_to_db(self, cursor):
        cursor.execute(
            "INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)",
            (self.title, self.author_id, self.genre_id, self.isbn, self.publication_date, self.availability))

    @classmethod
    def find_by_isbn(cls, cursor, isbn):
        cursor.execute("SELECT * FROM books WHERE isbn = %s", (isbn,))
        result = cursor.fetchone()
        if result:
            return cls(*result)
        return None

    def update_availability(self, cursor, available):
        self.availability = available
        cursor.execute("UPDATE books SET availability = %s WHERE id = %s", (self.availability, self.id))

    def delete_from_db(self, cursor):
        cursor.execute("DELETE FROM books WHERE id = %s", (self.id,))
