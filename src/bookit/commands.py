from __future__ import annotations
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
return MSG_NO_BOOKS_TO_SORT # Simplísimo: evita errores por atributo inválido
reverse = sorting.lower().startswith("decre")
books.sort(key=key_fn, reverse=reverse)
# Devuelve listado completo en formato completo para facilitar ver el orden
return "\n".join(_fmt_full(b) for b in books)