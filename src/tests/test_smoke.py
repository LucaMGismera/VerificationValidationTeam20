from bookit.models import Book
from bookit.commands import add_book




def test_add_book_ok():
    books = []
    msg = add_book(books, "Harry Potter", "J.K. Rowling", "4", "8478884459", "1999")
    assert msg == "The book was added successfully"
    assert len(books) == 1