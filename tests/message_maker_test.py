from mmlibrary.message_maker import MessageMaker
from mmlibrary.reserved_book import ReservedBook
from mmlibrary.reserved_books import ReservedBooks
from mmlibrary.user_book_info import UserBookInfo


class TestMessageMaker:
    def test_prepared_message(self):
        user = "dummy"

        book = ReservedBook(
            "ご用意できました", "", "title", "kind", "yoyaku_date", "torioki_date", "receive"
        )

        reserved_books = ReservedBooks()
        reserved_books.append(book)

        info = UserBookInfo(user, reserved_books=reserved_books)
        mmaker = MessageMaker()
        mmaker.get_all_users_reserved_books_message([info])
