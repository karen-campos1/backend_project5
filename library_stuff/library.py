import mysql.connector
from mysql.connector import Error
from book import Book
from user import User
from author import Author
from genre import Genre

class Library:
    def __init__(self):
        self.db = self.connect_to_db()
        self.cursor = self.db.cursor()
        self.books = []
        self.borrowed_books = []
        self.users = []
        self.genres = []
        self.authors = []

    def connect_database():
#connecting to OUR database - e_commerce_db
        db_name = "e_commerce_db"
        user = "root"
        password = "Carmen!1994"
        host = "localhost"

        try:
    #attempting to establish a connection
            conn = mysql.connector.connect(
                database=db_name,
                user=user,
                password=password,
                host=host)
     # checking if the connection is successful   
            if conn.is_connected(): #returns True if a connection was successfully made
            # print("Connected to MySQL DB successfully!")
                return conn
 
 # handling any connection errors        
        except Error as e:
            print(f"Error {e}")
        
# first menu: book operations menu    
# Book Operations:
# 1. Add a new book
# 2. Borrow a book
# 3. Return a book
# 4. Search for a book
# 5. Display all books

    def add_book(self):
        title = input("Enter book title: ")
        author_id = input("Enter author ID: ")
        genre_id = input("Enter genre ID: ")
        isbn = input("Enter ISBN: ")
        publication_date = input("Enter publication date (YYYY-MM-DD): ")
        availability = True

        book = Book(None, title, author_id, genre_id, isbn, publication_date, availability)
        book.save_to_db(self.cursor)
        self.db.commit()
        print("Book added successfully!")

    def borrow_book(self):
        isbn = input("Enter ISBN: ")
        book = Book.find_by_isbn(self.cursor, isbn)
        if book and book.availability:
            book.update_availability(self.cursor, False)
            self.db.commit()
            print("Book borrowed successfully!")
        else:
            print("Book not available.")

    def return_book(self):
        isbn = input("Enter ISBN: ")
        book = Book.find_by_isbn(self.cursor, isbn)
        if book and not book.availability:
            book.update_availability(self.cursor, True)
            self.db.commit()
            print("Book returned successfully!")
        else:
            print("Book is not borrowed.")

    def search_book(self):
        isbn = input("Enter ISBN: ")
        book = Book.find_by_isbn(self.cursor, isbn)
        if book:
            print(f'ID: {book.id}, Title: {book.title}, Author ID: {book.author_id}, Genre ID: {book.genre_id}, ISBN: {book.isbn}, Publication Date: {book.publication_date}, Available: {book.availability}')
        else:
            print("Book not found.")

    def display_books(self):
        self.cursor.execute("SELECT * FROM books")
        for (id, title, author_id, genre_id, isbn, publication_date, availability) in self.cursor:
            print(f'ID: {id}, Title: {title}, Author ID: {author_id}, Genre ID: {genre_id}, ISBN: {isbn}, Publication Date: {publication_date}, Available: {availability}')
# 2nd menu:                
# User Operations:
# 1. Add a new user
# 2. View user details
# 3. Display all users        
        

    def add_user(self):
        name = input("Enter name: ")
        library_id = input("Enter library ID: ")

        user = User(None, name, library_id)
        user.save_to_db(self.cursor)
        self.db.commit()
        print("User added successfully!")

    def view_user(self):
        user_id = input("Enter User ID: ")
        user = User.find_by_id(self.cursor, user_id)
        if user:
            print(f'ID: {user.id}, Name: {user.name}, Library ID: {user.library_id}')
        else:
            print("User not found.")

    def display_users(self):
        self.cursor.execute("SELECT * FROM users")
        for (id, name, library_id) in self.cursor:
            print(f'ID: {id}, Name: {name}, Library ID: {library_id}')
            
            
#Author Operations:
# 1. Add a new author
# 2. View author details
# 3. Display all authors

 
    def add_author(self):
        name = input("Enter name: ")
        biography = input("Enter biography: ")

        author = Author(None, name, biography)
        author.save_to_db(self.cursor)
        self.db.commit()
        print("Author added successfully!")

    def view_author(self):
        author_id = input("Enter Author ID: ")
        author = Author.find_by_id(self.cursor, author_id)
        if author:
            print(f'ID: {author.id}, Name: {author.name}, Biography: {author.biography}')
        else:
            print("Author not found.")

    def display_authors(self):
        self.cursor.execute("SELECT * FROM authors")
        for (id, name, biography) in self.cursor:
            print(f'ID: {id}, Name: {name}, Biography: {biography}')
            
# Genre Operations:
# 1. Add a new genre
# 2. View genre details
# 3. Display all genres


     
    def add_genre(self):
        genre_name = input("Enter genre name: ")
        genre_details = input("Enter genre details: ")

        genre = Genre(None, genre_name, genre_details)
        genre.save_to_db(self.cursor)
        self.db.commit()
        print("Genre added successfully!")

    def view_genre(self):
        genre_id = input("Enter Genre ID: ")
        genre = Genre.find_by_id(self.cursor, genre_id)
        if genre:
            print(f'ID: {genre.id}, Genre Name: {genre.genre_name}, Genre Details: {genre.genre_details}')
        else:
            print("Genre not found.")

    def display_genres(self):
        self.cursor.execute("SELECT * FROM genres")
        for (id, genre_name, genre_details) in self.cursor:
            print(f'ID: {id}, Genre Name: {genre_name}, Genre Details: {genre_details}')

    def close(self):
        self.cursor.close()
        self.db.close()

def main():
    library = Library()
