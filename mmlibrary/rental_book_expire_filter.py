from typing import Dict
from mmlibrary.rental_books import RentalBooks
from mmlibrary.rental_book_filter import RentalBookFilter


class RentalBookExpireFilter(RentalBookFilter):
    def __init__(self, param: Dict) -> None:
        super().__init__(param)
        xdays: str = param.get("xdays", "2")
        self._xdays: int = self._convert_xdays(xdays)

    @property
    def xdays(self) -> int:
        return self._xdays

    def do(self, rental_books: RentalBooks) -> RentalBooks:
        filterd_books = list(
            filter(lambda book: book.is_expire_in_xdays(self.xdays), rental_books.list)
        )
        rental_books.list = self._sort(filterd_books)
        return rental_books

    def _convert_xdays(self, target: str) -> int:
        default = 2

        try:
            return int(target)
        except ValueError:
            try:
                index = target.find("日で延滞")
                num_str = target[index - 1 : index + 4]
                num_str = num_str.replace("日で延滞", "")
                return int(num_str)
            except ValueError:
                return default
