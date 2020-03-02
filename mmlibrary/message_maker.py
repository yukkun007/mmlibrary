from collections import defaultdict
from typing import List, Dict
from mmlibrary.rental_books import RentalBooks
from mmlibrary.message import Message
from mmlibrary.user_book_info import UserBookInfo


class MessageMaker:

    TEMPLATE_RENTAL_BOOKS: str = "text_rental_books.tpl"
    TEMPLATE_RENTAL_BOOKS_EMPTY: str = "text_rental_books_empty.tpl"
    TEMPLATE_RESERVED_BOOKS = "text_reserved_books.tpl"
    TEMPLATE_RESERVED_BOOKS_EMPTY = "text_reserved_books_empty.tpl"
    TEMPLATE_ALL_USER_RENTAL_BOOKS: str = "text_all_user_rental_books.tpl"
    TEMPLATE_ALL_USER_RENTAL_BOOKS_EMPTY: str = "text_all_user_rental_books_empty.tpl"
    TEMPLATE_ALL_USER_RESERVED_BOOKS: str = "text_all_user_reserved_books.tpl"
    TEMPLATE_ALL_USER_RESERVED_BOOKS_EMPTY: str = "text_all_user_reserved_books_empty.tpl"
    TEMPLATE_RENTAL_AND_RESERVED_BOOKS: str = "text_rental_and_reserved_books.tpl"

    def get_all_users_rental_books_message(
        self, infos: List[UserBookInfo], params: Dict = {}
    ) -> str:
        sub_message = ""
        is_all_empty = True
        for info in infos:
            sub_message += self.get_rental_books_message(info, params)
            if len(info.rental_books.list) > 0:
                is_all_empty = False

        if is_all_empty:
            # 全ユーザの貸出本が0件の場合のメッセージを作成
            zero_behavior = params.get("zero", "always")
            if zero_behavior == "message":
                return Message.create(
                    MessageMaker.TEMPLATE_ALL_USER_RENTAL_BOOKS_EMPTY,
                    {"rental_books": info.rental_books, "header": True},
                )
            elif zero_behavior == "none":
                return ""

        # 1人のユーザでも貸出本が1件以上ある場合のメッセージを作成
        data = {"sub_message": sub_message, "header": True}
        return Message.create(MessageMaker.TEMPLATE_ALL_USER_RENTAL_BOOKS, data)

    def get_all_users_reserved_books_message(
        self, infos: List[UserBookInfo], params: Dict = {}
    ) -> str:
        sub_message = ""
        sub_message_list = []
        is_all_empty = True
        is_prepared = False
        for info in infos:
            sub_message_list.append(self.get_reserved_books_message(info, params))
            # sub_message += self.get_reserved_books_message(info, params)
            if len(info.reserved_books.list) > 0:
                is_all_empty = False
            if info.reserved_books.is_prepared():
                is_prepared = True
        sub_message = "\n".join(sub_message_list)

        if is_all_empty:
            # 全ユーザの予約本が0件の場合のメッセージを作成
            zero_behavior = params.get("zero", "always")
            if zero_behavior == "message":
                return Message.create(
                    MessageMaker.TEMPLATE_ALL_USER_RESERVED_BOOKS_EMPTY,
                    {"reserved_books": info.reserved_books, "header": True},
                )
            elif zero_behavior == "none":
                return ""

        # 1人のユーザでも予約本が1件以上ある場合のメッセージを作成
        data = {
            "sub_message": sub_message,
            "is_prepared": is_prepared,
            "header": True,  # 常に表示
        }
        return Message.create(MessageMaker.TEMPLATE_ALL_USER_RESERVED_BOOKS, data)

    def get_rental_and_reserved_books_message(self, info: UserBookInfo, params: Dict = {}) -> str:
        # 予約本基準で判定
        if len(info.reserved_books.list) <= 0:
            # 0件の場合のメッセージを作成
            zero_behavior = params.get("zero", "always")
            if zero_behavior == "message":
                return Message.create(
                    MessageMaker.TEMPLATE_RESERVED_BOOKS_EMPTY,
                    {
                        "user": info.user,
                        "reserved_books": info.reserved_books,
                        "header": params.get("header", False),
                    },
                )
            elif zero_behavior == "none":
                return ""

        sub_message1 = self.get_rental_books_message(info, params)
        sub_message2 = self.get_reserved_books_message(info, params)
        data = {
            "sub_message1": sub_message1,
            "sub_message2": sub_message2,
            "header": params.get("header", False),
        }
        return Message.create(MessageMaker.TEMPLATE_RENTAL_AND_RESERVED_BOOKS, data)

    def get_rental_books_message(self, info: UserBookInfo, params: Dict = {}) -> str:
        if len(info.rental_books.list) <= 0:
            # 0件の場合のメッセージを作成
            zero_behavior = params.get("zero", "always")
            if zero_behavior == "message":
                return Message.create(
                    MessageMaker.TEMPLATE_RENTAL_BOOKS_EMPTY,
                    {
                        "user": info.user,
                        "rental_books": info.rental_books,
                        "header": params.get("header", False),
                    },
                )
            elif zero_behavior == "none":
                return ""

        # 通常のメッセージを作成
        date_keyed_books_dict = self._get_date_keyed_books_dict(info.rental_books)
        data = {
            "user": info.user,
            "rental_books": info.rental_books,
            "date_keyed_books_dict": date_keyed_books_dict,
            "header": params.get("header", False),
        }
        return Message.create(MessageMaker.TEMPLATE_RENTAL_BOOKS, data)

    def _get_date_keyed_books_dict(self, rental_books: RentalBooks) -> Dict[str, List]:
        date_keyed_books_dict: Dict[str, List] = defaultdict(lambda: [])
        for book in rental_books.list:
            date_keyed_books_dict[book.expire_date_text].append(book)
        return date_keyed_books_dict

    def get_reserved_books_message(self, info: UserBookInfo, params: Dict = {}) -> str:
        if len(info.reserved_books.list) <= 0:
            # 0件の場合のメッセージを作成
            zero_behavior = params.get("zero", "always")
            if zero_behavior == "message":
                return Message.create(
                    MessageMaker.TEMPLATE_RESERVED_BOOKS_EMPTY,
                    {
                        "user": info.user,
                        "reserved_books": info.reserved_books,
                        "header": params.get("header", False),
                    },
                )
            elif zero_behavior == "none":
                return ""

        data = {
            "user": info.user,
            "reserved_books": info.reserved_books,
            "header": params.get("header", False),
        }
        return Message.create(MessageMaker.TEMPLATE_RESERVED_BOOKS, data)
