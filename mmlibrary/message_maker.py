from collections import defaultdict
from typing import List, Dict
from mmlibrary.rental_books import RentalBooks
from mmlibrary.message import Message
from mmlibrary.user_book_info import UserBookInfo


class MessageMaker:

    TEMPLATE_RENTAL_BOOKS: str = "text_rental_books.tpl"
    TEMPLATE_RESERVED_BOOKS = "text_reserved_books.tpl"
    TEMPLATE_USER_RENTAL_BOOKS: str = "text_user_rental_books.tpl"
    TEMPLATE_USER_RESERVED_BOOKS: str = "text_user_reserved_books.tpl"
    TEMPLATE_ONE_USER_RESERVED_BOOKS: str = "text_one_user_reserved_books.tpl"

    def get_all_users_rental_books_message(self, infos: List[UserBookInfo]) -> str:
        sub_message = ""
        for info in infos:
            sub_message += self.get_rental_books_message(info)

        data = {"sub_message": sub_message}
        return Message.create(MessageMaker.TEMPLATE_USER_RENTAL_BOOKS, data)

    def get_all_users_reserved_books_message(self, infos: List[UserBookInfo]) -> str:
        sub_message = ""
        is_prepared = False
        for info in infos:
            if info.reserved_books.is_prepared():
                is_prepared = True
            sub_message += self.get_reserved_books_message(info)

        data = {"sub_message": sub_message, "is_prepared": is_prepared}
        return Message.create(MessageMaker.TEMPLATE_USER_RESERVED_BOOKS, data)

    def get_rental_and_reserved_books_message(self, info: UserBookInfo) -> str:
        sub_message1 = self.get_rental_books_message(info)
        sub_message2 = self.get_reserved_books_message(info)
        data = {"sub_message1": sub_message1, "sub_message2": sub_message2}
        return Message.create(MessageMaker.TEMPLATE_ONE_USER_RESERVED_BOOKS, data)

    def get_rental_books_message(self, info: UserBookInfo) -> str:
        date_keyed_books_dict = self._get_date_keyed_books_dict(info.rental_books)
        data = {
            "user": info.user,
            "rental_books": info.rental_books,
            "date_keyed_books_dict": date_keyed_books_dict,
        }
        return Message.create(MessageMaker.TEMPLATE_RENTAL_BOOKS, data)

    def _get_date_keyed_books_dict(self, rental_books: RentalBooks) -> Dict[str, List]:
        date_keyed_books_dict: Dict[str, List] = defaultdict(lambda: [])
        for book in rental_books.list:
            date_keyed_books_dict[book.expire_date_text].append(book)
        return date_keyed_books_dict

    def get_reserved_books_message(self, info: UserBookInfo) -> str:
        data = {"user": info.user, "reserved_books": info.reserved_books}
        return Message.create(MessageMaker.TEMPLATE_RESERVED_BOOKS, data)
