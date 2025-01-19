from book import Book
from library import Library

class Admin:
    def __init__(self, name: str):
        self.name = name

    def add_book_to_library(self, book: Book, library: Library):
        library.add_book(book)