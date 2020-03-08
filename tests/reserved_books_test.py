import pytest
from mmlibrary.reserved_book import ReservedBook
from mmlibrary.reserved_books import ReservedBooks


class TestReservedBooks:
    @pytest.fixture()
    def books1(self):
        return ReservedBooks()

    def test_is_prepared_reserved_book_true(self, books1):
        book = ReservedBook(
            "ご用意できました", "", "title", "kind", "yoyaku_date", "torioki_date", "receive"
        )
        books1.append(book)
        assert books1.is_prepared() is True

    def test_is_prepared_reserved_book_false(self, books1):
        book = ReservedBook("status", "", "title", "kind", "yoyaku_date", "torioki_date", "receive")
        books1.append(book)
        assert books1.is_prepared() is False
