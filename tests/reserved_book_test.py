import pytest
from mmlibrary.reserved_book import ReservedBook


class TestReservedBook:
    @pytest.fixture()
    def book1(self):
        return ReservedBook("status", "", "title", "kind", "yoyaku_date", "torioki_date", "receive")

    def test_to_string(self, book1):
        print(book1)

    def test_get_order_num(self, book1):
        num = book1._get_order_num(" 1 / 10")
        assert num == 1

    def test_is_prepared_true(self, book1):
        assert book1._is_prepared("ご用意できました") is True

    def test_is_prepared_false(self, book1):
        assert book1._is_prepared("status") is False

    def test_is_dereverd_true(self, book1):
        assert book1._is_dereverd("移送中です") is True

    def test_is_dereverd_false(self, book1):
        assert book1._is_dereverd("status") is False
