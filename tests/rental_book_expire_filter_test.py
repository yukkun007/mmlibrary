import pytest
from mmlibrary.rental_book_expire_filter import RentalBookExpireFilter


class TestRentalBookExpireFilter:
    @pytest.fixture()
    def filter1(request):
        return RentalBookExpireFilter({})

    def test_xdays_getter(self, filter1):
        assert filter1.xdays == 2

    def test_xdays_setter(self, filter1):
        with pytest.raises(AttributeError):
            filter1.xdays = 1

    def test_convert_xdays(self):
        filter2 = RentalBookExpireFilter({"xdays": "3日で延滞"})
        assert filter2.xdays == 3

    def test_convert_xdays_2(self):
        filter2 = RentalBookExpireFilter({"xdays": "3日"})
        # 「x日で延滞」しか受け付けない、それ以外はデフォルト値になる
        assert filter2.xdays == 2
