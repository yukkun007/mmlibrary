from typing import Dict
from mmlibrary.rental_books import RentalBooks
from mmlibrary.rental_book_filter import RentalBookFilter


class RentalBookExpiredFilter(RentalBookFilter):
    def __init__(self, param: Dict) -> None:
        super().__init__(param)

    def do(self, rental_books: RentalBooks) -> RentalBooks:
        filterd_books = list(filter(lambda book: book.is_expired(), rental_books.list))
        rental_books.list = self._sort(filterd_books)
        return rental_books
