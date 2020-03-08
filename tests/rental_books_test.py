import pytest
from mmlibrary.rental_books import RentalBooks


class TestRentalBooks:
    @pytest.fixture()
    def books1(self):
        return RentalBooks()

    def test_can_extend_period_1(self, books1):
        assert books1._can_extend_period("延長できません") is False

    def test_can_extend_period_2(self, books1):
        assert books1._can_extend_period("すでに延長されています") is False

    def test_can_extend_period_3(self, books1):
        assert books1._can_extend_period("それ以外") is True
