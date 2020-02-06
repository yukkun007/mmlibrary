from typing import Dict
from mmlibrary.html_page import HtmlPage
from mmlibrary.html_parser import HtmlParser
from mmlibrary.user import User
from mmlibrary.rental_books import RentalBooks
from mmlibrary.reserved_books import ReservedBooks
from mmlibrary.book_filter import BookFilter


class Library:

    LIBRALY_HOME_URL = "https://www.lib.nerima.tokyo.jp/opw/OPW/OPWUSERCONF.CSP"
    LIBRALY_BOOK_URL = (
        "https://www.lib.nerima.tokyo.jp/opw/OPW/OPWBOOK.CSP?DB="
        "LIB&MODE=1&PID2=OPWSRCH1&SRCID=1&WRTCOUNT=10&LID=1&GBID={0}&DispDB=LIB"
    )

    def __init__(self) -> None:
        self._html_page = HtmlPage()

    def __del__(self) -> None:
        self._html_page.release_resource()

    def get_all_rental_books(self, user: User) -> RentalBooks:
        return self._get_rental_books(user, type=BookFilter.TYPE_RENTAL_NORMAL)

    def get_expire_rental_books(self, user: User, param: Dict = {"xdays": "2"}) -> RentalBooks:
        return self._get_rental_books(user, type=BookFilter.TYPE_RENTAL_EXPIRE, param=param)

    # 使ってない
    # def get_expired_rental_books(self, user: User) -> Books:
    #     return self._get_rental_books(user, type=BookFilter.TYPE_RENTAL_EXPIRED)

    def _get_rental_books(
        self, user: User, type: str = BookFilter.TYPE_RENTAL_NORMAL, param: Dict = {}
    ) -> RentalBooks:
        html = self._html_page.fetch_login_page(Library.LIBRALY_HOME_URL, user)
        all_books = HtmlParser.get_rental_books(html)
        filtered_books = BookFilter.do(all_books, type=type, param=param)
        return filtered_books

    def get_all_reserved_books(self, user: User) -> ReservedBooks:
        return self._get_reserved_books(user, type=BookFilter.TYPE_RESERVED_NORMAL)

    def get_prepared_reserved_books(self, user: User) -> ReservedBooks:
        return self._get_reserved_books(user, type=BookFilter.TYPE_RESERVED_PREPARED)

    def _get_reserved_books(
        self, user: User, type: str = BookFilter.TYPE_RESERVED_NORMAL
    ) -> ReservedBooks:
        html = self._html_page.fetch_login_page(Library.LIBRALY_HOME_URL, user)
        all_books = HtmlParser.get_reserved_books(html)
        filtered_books = BookFilter.do(all_books, type=type)
        return filtered_books
