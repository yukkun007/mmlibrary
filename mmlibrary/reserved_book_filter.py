from typing import Dict, List
from mmlibrary.base_book_filter import BaseBookFilter
from mmlibrary.reserved_books import ReservedBooks


class ReservedBookFilter(BaseBookFilter):
    def __init__(self, param: Dict):
        super().__init__(param)

    def do(self, reserved_books: ReservedBooks) -> ReservedBooks:
        # ソートするだけ
        reserved_books.list = self._sort(reserved_books.list)
        return reserved_books

    def _sort(self, reserved_book_list: List) -> List:
        new_reserved_book_list = sorted(
            reserved_book_list, key=lambda book: (book.order_num, book.status)
        )
        return new_reserved_book_list
