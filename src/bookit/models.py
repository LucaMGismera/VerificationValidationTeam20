from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    rating: int
    isbn: str
    publication_year: int

    def to_row(self) -> list[str]:
        return [self.title, self.author, str(self.rating), self.isbn, str(self.publication_year)]