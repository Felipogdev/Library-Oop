from book import Book
from user import User
from admin import Admin
from library import Library

def main():
    library = Library()
    admin = Admin(name="Admin")

    book1 = Book(title="1984", genre="Dystopian", author="George Orwell", release_date=1949, borrowed=False)
    book2 = Book(title="The Great Gatsby", genre="Fiction", author="F. Scott Fitzgerald", release_date=1925, borrowed=False)

    admin.add_book_to_library(book1, library)
    admin.add_book_to_library(book2, library)

    user = User(name="Gabriel Augusto", id=1)

    library.view_inventory()

    library.borrow_books(user, book1)

    library.view_inventory()

    library.return_book(book1, user)

    library.view_inventory()


    print(f"{admin.id}")
if __name__ == '__main__':
    main()
