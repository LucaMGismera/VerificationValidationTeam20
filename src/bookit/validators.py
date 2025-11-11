import re


def valid_isbn(isbn: str) -> bool:
# Solo formato: 10 o 13 dígitos (sin guiones)
return bool(re.fullmatch(r"\d{10}|\d{13}", isbn))




def valid_rating(rating_str: str) -> tuple[bool, int | None]:
try:
r = int(rating_str)
except ValueError:
return False, None
return (1 <= r <= 5), (r if 1 <= r <= 5 else None)




def valid_year(year_str: str) -> tuple[bool, int | None]:
try:
y = int(year_str)
except ValueError:
return False, None
return (y > 0), (y if y > 0 else None)