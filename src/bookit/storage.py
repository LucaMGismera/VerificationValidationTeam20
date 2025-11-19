from __future__ import annotations
from pathlib import Path
from typing import Iterable
from .models import Book

SEP = ";"

# Fichero plano con formato: title;author;rating;isbn;publicationYear (una línea por libro)

def load_books(file_path: str | Path) -> list[Book]:
    p = Path(file_path)
    if not p.exists():
        return []
    books: list[Book] = []
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            title, author, rating, isbn, year = line.split(SEP)
            books.append(Book(title, author, int(rating), isbn, int(year)))
    return books

def save_books(file_path: str | Path, books: Iterable[Book]) -> None:
    p = Path(file_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        for b in books:
            f.write(SEP.join(b.to_row()) + "\n")