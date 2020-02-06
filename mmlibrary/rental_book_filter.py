from typing import List, Dict
from mmlibrary.rental_books import RentalBooks
from mmlibrary.base_book_filter import BaseBookFilter


class RentalBookFilter(BaseBookFilter):
    def __init__(self, param: Dict) -> None:
        super().__init__(param)

    def do(self, rental_books: RentalBooks) -> RentalBooks:
        # ソートするだけ
        rental_books.list = self._sort(rental_books.list)
        return rental_books

    def _sort(self, rental_book_list: List) -> List:
        new_rental_book_list = sorted(
            rental_book_list, key=lambda book: (book.expire_date, book.name)
        )
        return new_rental_book_list
