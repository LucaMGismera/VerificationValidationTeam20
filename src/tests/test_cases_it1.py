from bookit.models import Book
from bookit.commands import *




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

def test_update_rating_ok():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    msg = update_rating(books, "8478884459", "5")
    assert msg == "Update success"
    assert len(books) == 1

def test_update_rating_error_isbn():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    msg = update_rating(books, "84788844590", "5")
    assert msg == "Incorrect ISBN"
    assert len(books) == 1

def test_update_rating_error_rating_1():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    msg = update_rating(books, "8478884459", "A")
    assert msg == "Invalid Rating"
    assert len(books) == 1

def test_update_rating_error_rating_2():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    msg = update_rating(books, "8478884459", "10")
    assert msg == "Invalid Rating"
    assert len(books) == 1

def test_update_rating_error_not_found():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    msg = update_rating(books, "8424874459824", "5")
    assert msg == "Book not found"
    assert len(books) == 1

def test_search_by_title_ok():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    add_book(books, "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "4", "8478884460", "1998")
    add_book(books, "Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", "5", "8478884461", "1999")
    add_book(books, "The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien", "4", "8473886459", "1954")
    add_book(books, "The Lord of the Rings: The Two Towers", "J.R.R. Tolkien", "5", "8473886460", "1954")
    msg = search_by_title(books, "Harry Potter")
    assert msg == ("Harry Potter and the Philosopher's Stone;J.K. Rowling;4;8478884459;1997\n"
    "Harry Potter and the Chamber of Secrets;J.K. Rowling;4;8478884460;1998\n"
    "Harry Potter and the Prisoner of Azkaban;J.K. Rowling;5;8478884461;1999"
    )
    assert len(books) == 5

def test_search_by_title_error():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    add_book(books, "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "4", "8478884460", "1998")
    msg = search_by_title(books, "The Lord of the Rings")
    assert msg == "Oops, no books are found"
    assert len(books) == 2

def test_search_by_author_ok():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    add_book(books, "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "4", "8478884460", "1998")
    add_book(books, "Fantastic Beasts and Where to Find Them", "J.K. Rowling", "4", "8478824470", "2001")
    add_book(books, "The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien", "4", "8473886459", "1954")
    msg = search_by_author(books, "J.K. Rowling")
    assert msg == ("Harry Potter and the Philosopher's Stone;J.K. Rowling;4;8478884459;1997\n"
    "Harry Potter and the Chamber of Secrets;J.K. Rowling;4;8478884460;1998\n"
    "Fantastic Beasts and Where to Find Them;J.K. Rowling;4;8478824470;2001"
    )
    assert len(books) == 4

def test_search_by_author_error():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    add_book(books, "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "4", "8478884460", "1998")
    add_book(books, "Fantastic Beasts and Where to Find Them", "J.K. Rowling", "4", "8478824470", "2001")
    msg = search_by_author(books, "J.R.R. Tolkien")
    assert msg == "Oops, no books are found"
    assert len(books) == 3

def test_search_by_year_ok():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    add_book(books, "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "4", "8478884460", "1998")
    msg = search_by_year(books, "1998")
    assert msg == "Harry Potter and the Chamber of Secrets;J.K. Rowling;4;8478884460;1998"
    assert len(books) == 2

def test_search_by_year_error_year():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    add_book(books, "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "4", "8478884460", "1998")
    msg = search_by_year(books, "-1998")
    assert msg == "Incorrect publication year"
    assert len(books) == 2

def test_search_by_year_error_not_match():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    add_book(books, "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "4", "8478884460", "1998")
    msg = search_by_year(books, "2001")
    assert msg == "Oops, no books are found"
    assert len(books) == 2

def test_list_all_ok():
    books = []
    add_book(books, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "4", "8478884459", "1997")
    add_book(books, "Harry Potter and the Chamber of Secrets", "J.K. Rowling", "4", "8478884460", "1998")
    add_book(books, "Harry Potter and the Prisoner of Azkaban", "J.K. Rowling", "5", "8478884461", "1999")
    add_book(books, "Fantastic Beasts and Where to Find Them", "J.K. Rowling", "4", "8478824470", "2001")
    add_book(books, "The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien", "4", "8473886459", "1954")
    add_book(books, "The Lord of the Rings: The Two Towers", "J.R.R. Tolkien", "5", "8473886460", "1954")
    msg = list_all(books)
    assert msg == (
        "Harry Potter and the Philosopher's Stone;J.K. Rowling;4\n"
        "Harry Potter and the Chamber of Secrets;J.K. Rowling;4\n"
        "Harry Potter and the Prisoner of Azkaban;J.K. Rowling;5\n"
        "Fantastic Beasts and Where to Find Them;J.K. Rowling;4\n"
        "The Lord of the Rings: The Fellowship of the Ring;J.R.R. Tolkien;4\n"
        "The Lord of the Rings: The Two Towers;J.R.R. Tolkien;5"
    )
    assert len(books) == 6

def test_list_all_error():
    books = []
    msg = list_all(books)
    assert msg == "The list is empty"
    assert len(books) == 0

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
    test_search_by_title_ok()
    test_search_by_title_error()
    test_search_by_author_ok()
    test_search_by_author_error()
    test_search_by_year_ok()
    test_search_by_year_error_year()
    test_search_by_year_error_not_match()
    test_list_all_ok()
    test_list_all_error()

    return 0

main()