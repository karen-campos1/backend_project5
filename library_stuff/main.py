from library import Library

def main():
    library = Library()

    while True:
        print("Welcome to the Library Management System with Database Integration!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Book Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            book_choice = input("Enter your choice: ")
            if book_choice == '1':
                library.add_book()
            elif book_choice == '2':
                library.borrow_book()
            elif book_choice == '3':
                library.return_book()
            elif book_choice == '4':
                library.search_book()
            elif book_choice == '5':
                library.display_books()
            else:
                print("Invalid choice. Please try again.")
        elif choice == '2':
            print("User Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            user_choice = input("Enter your choice: ")
            if user_choice == '1':
                library.add_user()
            elif user_choice == '2':
                library.view_user()
            elif user_choice == '3':
                library.display_users()
            else:
                print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Author Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            author_choice = input("Enter your choice: ")
            if author_choice == '1':
                library.add_author()
            elif author_choice == '2':
                library.view_author()
            elif author_choice == '3':
                library.display_authors()
            else:
                print("Invalid choice. Please try again.")
        elif choice == '4':
            print("Genre Operations:")
            print("1. Add a new genre")
            print("2. View genre details")
            print("3. Display all genres")
            genre_choice = input("Enter your choice: ")
            if genre_choice == '1':
                library.add_genre()
            elif genre_choice == '2':
                library.view_genre()
            elif genre_choice == '3':
                library.display_genres()
            else:
                print("Invalid choice. Please try again.")
        elif choice == '5':
            library.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



# Book Operations:
# ```
# Book Operations:
# 1. Add a new book
# 2. Borrow a book
# 3. Return a book
# 4. Search for a book
# 5. Display all books
#     ```
# User Operations:
# ```
# User Operations:
# 1. Add a new user
# 2. View user details
# 3. Display all users
#     ```
# Author Operations:
# ```
# Author Operations:
# 1. Add a new author
# 2. View author details
# 3. Display all authors
#     ```
# Genre Operations:
# ```
# Genre Operations:
# 1. Add a new genre
# 2. View genre details
# 3. Display all genres
#     ```
