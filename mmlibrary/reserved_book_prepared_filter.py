from typing import Dict
from mmlibrary.reserved_book_filter import ReservedBookFilter
from mmlibrary.reserved_books import ReservedBooks


class ReservedBookPreparedFilter(ReservedBookFilter):
    def __init__(self, param: Dict):
        super().__init__(param)

    def do(self, reserved_books: ReservedBooks) -> ReservedBooks:
        filterd_books = list(
            filter(lambda book: book.is_prepared or book.is_dereverd, reserved_books.list)
        )
        reserved_books.list = self._sort(filterd_books)
        return reserved_books
