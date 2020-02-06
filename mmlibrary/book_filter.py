from typing import Dict
from mmlibrary.books import Books
from mmlibrary.rental_books import RentalBooks
from mmlibrary.reserved_books import ReservedBooks
from mmlibrary.rental_book_filter import RentalBookFilter
from mmlibrary.rental_book_expired_filter import RentalBookExpiredFilter
from mmlibrary.rental_book_expire_filter import RentalBookExpireFilter
from mmlibrary.reserved_book_filter import ReservedBookFilter
from mmlibrary.reserved_book_prepared_filter import ReservedBookPreparedFilter


class BookFilter:

    TYPE_RENTAL_NORMAL = "rental_normal"
    TYPE_RENTAL_EXPIRED = "rental_expired"
    TYPE_RENTAL_EXPIRE = "rental_expire"
    TYPE_RESERVED_NORMAL = "reserved_normal"
    TYPE_RESERVED_PREPARED = "reserved_prepared"

    @staticmethod
    def do(books: Books, type: str = TYPE_RENTAL_NORMAL, param: Dict = {}) -> Books:
        new_books = books
        if isinstance(books, RentalBooks):
            filter = BookFilter._create_rental_book_filter(type, param)
            new_books = filter.do(books)
        elif isinstance(books, ReservedBooks):
            filter = BookFilter._create_reserved_book_filter(type, param)
            new_books = filter.do(books)
        new_books.filter_type = type
        new_books.filter_param = param
        return new_books

    @staticmethod
    def _create_rental_book_filter(type: str, param: Dict):
        if type == BookFilter.TYPE_RENTAL_NORMAL:
            # ソートするだけのフィルタ
            return RentalBookFilter(param)
        elif type == BookFilter.TYPE_RENTAL_EXPIRED:
            # 期限切れの本のみにするフィルタ
            return RentalBookExpiredFilter(param)
        elif type == BookFilter.TYPE_RENTAL_EXPIRE:
            # 期限切れが近い本のみにするフィルタ
            return RentalBookExpireFilter(param)

    @staticmethod
    def _create_reserved_book_filter(type: str, param: Dict):
        if type == BookFilter.TYPE_RESERVED_NORMAL:
            # ソートするだけのフィルタ
            return ReservedBookFilter(param)
        elif type == BookFilter.TYPE_RESERVED_PREPARED:
            # 準備がほぼ出来た本のみにするフィルタ
            return ReservedBookPreparedFilter(param)
