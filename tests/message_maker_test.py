import pytest
from mmlibrary.message_maker import MessageMaker
from mmlibrary.rental_books import RentalBooks
from mmlibrary.reserved_book import ReservedBook
from mmlibrary.reserved_books import ReservedBooks
from mmlibrary.user import User
from mmlibrary.user_book_info import UserBookInfo


class TestMessageMaker:
    @pytest.fixture()
    def message_maker1(self):
        return MessageMaker()

    def test_prepared_message(self, message_maker1: MessageMaker):
        reserved_books = ReservedBooks()

        book = ReservedBook(
            "ご用意できました", "", "title", "kind", "yoyaku_date", "torioki_date", "receive"
        )
        reserved_books.append(book)

        info = UserBookInfo(User("{}"), reserved_books=reserved_books)
        message_maker1.get_all_users_reserved_books_message([info])

    @pytest.mark.parametrize("zero_behavior", [("message"), ("none")])
    def test_empty(self, zero_behavior, message_maker1: MessageMaker):
        rental_books = RentalBooks()
        reserved_books = ReservedBooks()
        empty_info = UserBookInfo(
            User("{}"), rental_books=rental_books, reserved_books=reserved_books
        )
        message_maker1.get_all_users_rental_books_message(
            [empty_info], params={"zero": zero_behavior}
        )
        message_maker1.get_all_users_reserved_books_message(
            [empty_info], params={"zero": zero_behavior}
        )
        message_maker1.get_rental_books_message(empty_info, params={"zero": zero_behavior})
        message_maker1.get_reserved_books_message(empty_info, params={"zero": zero_behavior})
        message_maker1.get_rental_and_reserved_books_message(
            empty_info, params={"zero": zero_behavior}
        )
