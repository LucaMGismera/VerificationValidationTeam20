from __future__ import annotations
from random import choice
from typing import Iterable
from .models import Book
from .validators import valid_isbn, valid_rating, valid_year


MSG_BOOK_ADDED = "The book was added successfully"
MSG_BOOK_EXISTS = "The book already exists"
MSG_INCORRECT_ISBN = "Incorrect ISBN"
MSG_INCORRECT_YEAR = "Incorrect publication year"
MSG_INVALID_RATING = "Invalid Rating"
MSG_UPDATE_OK = "Update success"
MSG_BOOK_NOT_FOUND = "Book not found"
MSG_BOOK_NOT_FOUND_WITH = "Book not found with {isbn}"
MSG_AUTHOR_REMOVED = "The author has been successfully removed"
MSG_BOOKS_NOT_FOUND_WITH_AUTHOR = "Books not found with {author}"
MSG_NO_BOOKS = "The list is empty"
MSG_NO_BOOKS_TO_SORT = "No books to sort"
MSG_NO_MATCHES = "Oops, no books are found"
MSG_REMOVED_OK = "book successfully removed"
MSG_NO_RECOMM = "No recommendation for today"

# Utilidades internas

def _index_by_isbn(books: list[Book]) -> dict[str, Book]:
    return {b.isbn: b for b in books}

def add_book(books: list[Book], title: str, author: str, rating_s: str, isbn: str, year_s: str) -> str:
    if not valid_isbn(isbn):
        return MSG_INCORRECT_ISBN
    ok_r, rating = valid_rating(rating_s)
    if not ok_r:
        return MSG_INVALID_RATING
    ok_y, year = valid_year(year_s)
    if not ok_y:
        return MSG_INCORRECT_YEAR
    if isbn in _index_by_isbn(books):
        return MSG_BOOK_EXISTS
    books.append(Book(title, author, rating, isbn, year))
    return MSG_BOOK_ADDED

def update_rating(books: list[Book], isbn: str, rating_s: str) -> str:
    if not valid_isbn(isbn):
        return MSG_INCORRECT_ISBN
    ok_r, rating = valid_rating(rating_s)
    if not ok_r:
        return MSG_INVALID_RATING
    idx = _index_by_isbn(books)
    b = idx.get(isbn)
    if not b:
        return MSG_BOOK_NOT_FOUND
    b.rating = rating
    return MSG_UPDATE_OK

def _fmt_full(b: Book) -> str:
    return f"{b.title};{b.author};{b.rating};{b.isbn};{b.publication_year}"

def _fmt_list(b: Book) -> str:
    return f"{b.title};{b.author};{b.rating}"

def search_by_title(books: list[Book], title: str) -> str:
    t = title.lower()
    found = [b for b in books if t in b.title.lower()]
    return "\n".join(_fmt_full(b) for b in found) if found else MSG_NO_MATCHES

def search_by_author(books: list[Book], author: str) -> str:
    a = author.lower()
    found = [b for b in books if a in b.author.lower()]
    return "\n".join(_fmt_full(b) for b in found) if found else MSG_NO_MATCHES

def search_by_year(books: list[Book], year_s: str) -> str:
    ok, year = valid_year(year_s)
    if not ok:
        return MSG_INCORRECT_YEAR
    found = [b for b in books if b.publication_year == year]
    return "\n".join(_fmt_full(b) for b in found) if found else MSG_NO_MATCHES

def list_all(books: list[Book]) -> str:
    return "\n".join(_fmt_list(b) for b in books) if books else MSG_NO_BOOKS

def remove_by_isbn(books: list[Book], isbn: str) -> str:
    if not valid_isbn(isbn):
        return MSG_INCORRECT_ISBN
    before = len(books)
    books[:] = [b for b in books if b.isbn != isbn]
    return MSG_REMOVED_OK if len(books) < before else MSG_BOOK_NOT_FOUND_WITH.format(isbn=isbn)

def remove_by_author(books: list[Book], author: str) -> str:
    before = len(books)
    books[:] = [b for b in books if b.author != author]
    return MSG_AUTHOR_REMOVED if len(books) < before else MSG_BOOKS_NOT_FOUND_WITH_AUTHOR.format(author=author)

def book_of_the_day(books: list[Book]) -> str:
    candidates = [b for b in books if b.rating in (4, 5)]
    if not candidates:
        return MSG_NO_RECOMM
    return _fmt_full(choice(candidates))

def order_by(books: list[Book], attribute: str, sorting: str) -> str:
    if not books:
        return MSG_NO_BOOKS_TO_SORT
    key_map = {
        "title": lambda b: b.title,
        "author": lambda b: b.author,
        "rating": lambda b: b.rating,
        "isbn": lambda b: b.isbn,
        "year": lambda b: b.publication_year,
    }
    key_fn = key_map.get(attribute.lower())
    if not key_fn:
        return MSG_NO_BOOKS_TO_SORT
    reverse = sorting.lower().startswith("decre")
    books.sort(key=key_fn, reverse=reverse)
    # Devuelve listado completo en formato completo para facilitar ver el orden
    return "\n".join(_fmt_full(b) for b in books)