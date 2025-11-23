from bookit.models import Book
from bookit.commands import *

# PRIMERA ITERACIÓN

def test_add_book_ok():
    books = []
    msg = add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    assert msg == "The book was added successfully"
    assert len(books) == 1

def test_add_book_error_isbn():
    books = []
    msg = add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "847888445", "1997")
    assert msg == "Incorrect ISBN"
    assert len(books) == 0

def test_add_book_error_rating_1():
    books = []
    msg = add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "a", "8478884459", "1997")
    assert msg == "Invalid Rating"
    assert len(books) == 0

def test_add_book_error_rating_2():
    books = []
    msg = add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "7", "8478884459", "1997")
    assert msg == "Invalid Rating"
    assert len(books) == 0

def test_add_book_error_year_1():
    books = []
    msg = add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "year")
    assert msg == "Incorrect publication year"
    assert len(books) == 0

def test_add_book_error_year_2():
    books = []
    msg = add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "-1997")
    assert msg == "Incorrect publication year"
    assert len(books) == 0

def test_add_book_error_book_exist():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    msg = add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    assert msg == "The book already exists"
    assert len(books) == 1



def main():
    test_add_book_ok()
    test_add_book_error_isbn()
    test_add_book_error_rating_1()
    test_add_book_error_rating_2()
    test_add_book_error_year_1()
    test_add_book_error_year_2()
    test_add_book_error_book_exist()

    return 0

# EJECUTAMOS LOS PRIMEROS TESTS
main()