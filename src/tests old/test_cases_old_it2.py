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


# ---------------------------------------------------------------------------------
# NUEVOS TESTS PARA SEGUNDA ITERACIÓN

def test_book_to_row_serialization():
    """Cubre Book.to_row (models.py)."""
    book = Book(
        "Harry Potter and the Philosopher's Stone",
        "J.K. Rowling",
        4,
        "8478884459",
        1997,
    )
    row = book.to_row()
    assert row == [
        "Harry Potter and the Philosopher's Stone",
        "J.K. Rowling",
        "4",
        "8478884459",
        "1997",
    ]


def test_remove_by_isbn_invalid_isbn():
    """Branch: ISBN inválido -> MSG_INCORRECT_ISBN."""
    books = [
        Book("Test", "Author", 4, "1234567890", 2000)
    ]
    msg = remove_by_isbn(books, "123")  # ISBN incorrecto
    assert msg == "Incorrect ISBN"
    # no se ha borrado nada
    assert len(books) == 1


def test_remove_by_isbn_existing_book():
    """Branch: libro encontrado y eliminado -> MSG_REMOVED_OK."""
    books = [
        Book("Test", "Author", 4, "1234567890", 2000)
    ]
    msg = remove_by_isbn(books, "1234567890")
    assert msg == "book successfully removed"
    assert len(books) == 0


def test_remove_by_isbn_not_found():
    """Branch: ISBN válido pero no existe -> MSG_BOOK_NOT_FOUND_WITH..."""
    books = [
        Book("Test", "Author", 4, "1111111111", 2000)
    ]
    msg = remove_by_isbn(books, "1234567890")
    assert msg == "Book not found with 1234567890"
    # La lista sigue teniendo el mismo libro
    assert len(books) == 1


def test_remove_by_author_existing():
    """Branch: autor encontrado y eliminado -> MSG_AUTHOR_REMOVED."""
    books = [
        Book("Book1", "J.K. Rowling", 4, "1111111111", 1997),
        Book("Book2", "Another Author", 3, "2222222222", 2000),
    ]
    msg = remove_by_author(books, "J.K. Rowling")
    assert msg == "The author has been successfully removed"
    assert len(books) == 1
    assert books[0].author == "Another Author"


def test_remove_by_author_not_found():
    """Branch: autor no encontrado -> MSG_BOOKS_NOT_FOUND_WITH_AUTHOR."""
    books = [
        Book("Book1", "J.K. Rowling", 4, "1111111111", 1997),
    ]
    msg = remove_by_author(books, "J.R.R. Tolkien")
    assert msg == "Books not found with J.R.R. Tolkien"
    # No se elimina ningún libro
    assert len(books) == 1


def test_book_of_the_day_no_recommendation():
    """Branch: sin candidatos (ningún rating 4 o 5)."""
    books = [
        Book("Book1", "Author", 1, "1111111111", 1997),
        Book("Book2", "Author", 2, "2222222222", 1998),
    ]
    msg = book_of_the_day(books)
    assert msg == "No recommendation for today"


def test_book_of_the_day_single_candidate():
    """Branch: al menos un candidato -> devuelve uno en formato completo."""
    books = [
        Book("LowRated", "Author", 2, "1111111111", 1990),
        Book("TopRated", "Author", 5, "2222222222", 2000),
    ]
    msg = book_of_the_day(books)
    # Solo hay un candidato con rating 4 o 5 -> debe devolver ese
    assert msg == "TopRated;Author;5;2222222222;2000"


def test_order_by_no_books():
    """Branch: lista vacía -> MSG_NO_BOOKS_TO_SORT."""
    books = []
    msg = order_by(books, "author", "incremental")
    assert msg == "No books to sort"


def test_order_by_invalid_attribute():
    """Branch: atributo inválido -> MSG_NO_BOOKS_TO_SORT."""
    books = [
        Book("A", "Author", 4, "1111111111", 2000),
        Book("B", "Author", 3, "2222222222", 2001),
    ]
    msg = order_by(books, "pages", "incremental")  # atributo inexistente
    assert msg == "No books to sort"


def test_order_by_title_incremental():
    """Branch: orden correcto incremental (reverse=False)."""
    books = [
        Book("C", "Author", 4, "1111111111", 2000),
        Book("A", "Author", 5, "2222222222", 2001),
        Book("B", "Author", 3, "3333333333", 2002),
    ]
    msg = order_by(books, "title", "incremental")
    # Debe quedar ordenado A, B, C
    lines = msg.split("\n")
    titles = [line.split(";")[0] for line in lines]
    assert titles == ["A", "B", "C"]


def test_order_by_rating_decreasing():
    """Branch: orden decreciente (reverse=True cuando sorting empieza por 'decre')."""
    books = [
        Book("Book1", "Author", 3, "1111111111", 1997),
        Book("Book2", "Author", 5, "2222222222", 1998),
        Book("Book3", "Author", 4, "3333333333", 1999),
    ]
    msg = order_by(books, "rating", "decreciente")
    lines = msg.split("\n")
    ratings = [int(line.split(";")[2]) for line in lines]
    assert ratings == [5, 4, 3]


def main():
    # PRIMERA ITERACIÓN DE TESTS
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

    # SEGUNDA ITERACIÓN DE TESTS
    test_book_to_row_serialization()
    test_remove_by_isbn_invalid_isbn()
    test_remove_by_isbn_existing_book()
    test_remove_by_isbn_not_found()
    test_remove_by_author_existing()
    test_remove_by_author_not_found()
    test_book_of_the_day_no_recommendation()
    test_book_of_the_day_single_candidate()
    test_order_by_no_books()
    test_order_by_invalid_attribute()
    test_order_by_title_incremental()
    test_order_by_rating_decreasing()

    return 0

main()