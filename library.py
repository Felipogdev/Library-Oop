from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Adicionado {book.title} à biblioteca.")

    def borrow_books(self, user: User, book: Book):
        if user.status == "Com Livro":
            print(f"{user.name}, você já possui um livro emprestado.")
            return
        elif user.status == "Em atraso":
            print(f"{user.name}, você está em atraso com um livro.")
            return
        elif book.borrowed:
            print(f"Desculpe, o livro {book.title} já está emprestado.")
            return
        else:
            book.borrowed = True
            user.status = "Com Livro"
            print(f"{user.name} pegou o livro {book.title} emprestado.")

    def return_book(self, book: Book, user: User):
        if not book.borrowed:
            print(f"O livro {book.title} não foi emprestado.")
            return
        book.borrowed = False
        user.status = "Livre"
        print(f"{user.name} devolveu o livro {book.title}.")

    def view_inventory(self):
        """ Display all books in the library and their status """
        if not self.books:
            print("Não há livros na biblioteca.")
            return

        print("Inventário da biblioteca:")
        for book in self.books:
            status = "Disponível" if not book.borrowed else "Emprestado"
            print(f"{book} - Status: {status}")