class Book:
    def __init__(self, title: str, genre: str, author: str, borrowed: bool, release_date: int):
        self.title = title
        self.genre = genre
        self.author = author
        self.borrowed = borrowed
        self.release_date = release_date

    def __str__(self):
        return f"Título: {self.title}, Gênero: {self.genre}, Escritor: {self.author}, Publicado: {self.release_date}"