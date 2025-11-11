from __future__ import annotations
import sys
from pathlib import Path
from typing import Callable
from .storage import load_books, save_books
from . import commands as c


# Formato de entrada de usuario:
# <command> <arg1>;<arg2>;...;<argN>




def _dispatch() -> dict[str, Callable[[list], str]]:
return {
"addBook": lambda a: c.add_book(BOOKS, *a),
"updateRating": lambda a: c.update_rating(BOOKS, *a),
"searchByTitle": lambda a: c.search_by_title(BOOKS, *a),
"searchByAuthor": lambda a: c.search_by_author(BOOKS, *a),
"searchByYear": lambda a: c.search_by_year(BOOKS, *a),
"listAll": lambda a: c.list_all(BOOKS),
"removeByISBN": lambda a: c.remove_by_isbn(BOOKS, *a),
"removeByAuthor": lambda a: c.remove_by_author(BOOKS, *a),
"bookOfTheDay": lambda a: c.book_of_the_day(BOOKS),
"orderBy": lambda a: c.order_by(BOOKS, *a),
}


BOOKS = [] # se inicializa en main()




def main(argv: list[str] | None = None) -> int:
global BOOKS
argv = argv if argv is not None else sys.argv[1:]
if not argv:
print("Usage: bookit <input-file>")
return 2


db_path = Path(argv[0])
BOOKS = load_books(db_path)


dispatch = _dispatch()
try:
for line in sys.stdin if not sys.stdin.isatty() else _repl_prompt():
line = line.strip()
if not line:
continue
if line.lower() in {"exit", "quit"}:
break
cmd, *rest = line.split(" ", 1)
args = rest[0].split(";") if rest else []
fn = dispatch.get(cmd)
if not fn:
# Simplicidad: ignoramos comandos inválidos
continue
try:
out = fn(args)
if out is not None:
print(out)
except TypeError:
# Argumentos insuficientes/excesivos: política simple
pass
finally:
save_books(db_path, BOOKS)
return 0




def _repl_prompt():
# Generador sencillo de líneas para modo interactivo
while True:
try:
yield input("> ")
except EOFError:
break