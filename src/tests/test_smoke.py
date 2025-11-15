from bookit.models import Book
from bookit.commands import add_book
from bookit.commands import update_rating




def test_add_book_ok():
    books = []
    msg = add_book(books, "Harry Potter", "J.K. Rowling", "4", "8478884459", "1999")
    assert msg == "The book was added successfully"
    assert len(books) == 1

def test_add_book_error_isbn():
    books = []
    msg = add_book(books, "Harry Potter", "J.K. Rowling", "4", "847888445", "1999")
    assert msg == "Incorrect ISBN"
    assert len(books) == 0

def test_add_book_error_rating_1():
    books = []
    msg = add_book(books, "Harry Potter", "J.K. Rowling", "a", "8478884459", "1999")
    assert msg == "Invalid Rating"
    assert len(books) == 0

def test_add_book_error_rating_2():
    books = []
    msg = add_book(books, "Harry Potter", "J.K. Rowling", "7", "8478884459", "1999")
    assert msg == "Invalid Rating"
    assert len(books) == 0

def test_add_book_error_year_1():
    books = []
    msg = add_book(books, "Harry Potter", "J.K. Rowling", "4", "8478884459", "year")
    assert msg == "Incorrect publication year"
    assert len(books) == 0

def test_add_book_error_year_2():
    books = []
    msg = add_book(books, "Harry Potter", "J.K. Rowling", "4", "8478884459", "-1999")
    assert msg == "Incorrect publication year"
    assert len(books) == 0

def test_add_book_error_book_exist():
    books = []
    add_book(books, "Harry Potter", "J.K. Rowling", "4", "8478884459", "1999")
    msg = add_book(books, "Harry Potter", "J.K. Rowling", "4", "8478884459", "1999")
    assert msg == "The book already exists"
    assert len(books) == 1

def test_update_rating_ok():
    books = []
    add_book(books, "Harry Potter", "J.K. Rowling", "4", "8478884459", "1999")
    msg = update_rating(books, "8478884459", "5")
    assert msg == "Update success"
    assert len(books) == 1

def test_update_rating_error_isbn():
    books = []
    add_book(books, "Harry Potter", "J.K. Rowling", "4", "8478884459", "1999")
    msg = update_rating(books, "84788844590", "5")
    assert msg == "Incorrect ISBN"
    assert len(books) == 1

def test_update_rating_error_rating_1():
    books = []
    add_book(books, "Harry Potter", "J.K. Rowling", "4", "8478884459", "1999")
    msg = update_rating(books, "8478884459", "A")
    assert msg == "Invalid Rating"
    assert len(books) == 1

def test_update_rating_error_rating_2():
    books = []
    add_book(books, "Harry Potter", "J.K. Rowling", "4", "8478884459", "1999")
    msg = update_rating(books, "8478884459", "10")
    assert msg == "Invalid Rating"
    assert len(books) == 1

def test_update_rating_error_not_found():
    books = []
    add_book(books, "Harry Potter", "J.K. Rowling", "4", "8478884459", "1999")
    msg = update_rating(books, "8424874459824", "5")
    assert msg == "Book not found"
    assert len(books) == 1

def main():
    test_add_book_ok()
    test_add_book_error_isbn()
    test_add_book_error_rating_1()
    test_add_book_error_rating_2()
    test_add_book_error_year_1()
    test_add_book_error_year_2()
    test_add_book_error_book_exist()
    test_update_rating_ok()
    test_update_rating_error_isbn()
    test_update_rating_error_rating_1()
    test_update_rating_error_rating_2()
    test_update_rating_error_not_found()
    return 0

main()