class User:
    def __init__(self, name: str, id: int, status: str = "Livre"):
        self.name = name
        self.id = id
        self.status = status