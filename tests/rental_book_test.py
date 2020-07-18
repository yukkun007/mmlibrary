import pytest
from datetime import timedelta
from mmlibrary.rental_book import RentalBook


class TestRentalBook:
    def test_to_string(self):
        book = RentalBook("test", "2017/01/01", True, "hoge")
        print(book)

    def test_is_expired_true(self):
        book = RentalBook("test", "2017/01/01", True, "hoge")
        assert book.is_expired()

    def test_is_expired_false(self):
        book = RentalBook("test", "9999/01/1", False, "hoge")
        assert book.is_expired() is False

    @pytest.mark.parametrize("delta, result", [(-1, True), (1, False), (0, False)])
    def test_is_expired(self, delta, result):
        today = RentalBook.get_jst_now_date()
        d = today + timedelta(days=delta)
        book = RentalBook("test", d.strftime("%Y/%m/%d"), True, "hoge")
        assert book.is_expired() is result

    # -日前：期限切れの本
    # 返却0日前：返却日まで1日切ってる本：今日が返却日
    # 返却1日前：返却日まで2日切ってる本：今日・明日が返却日
    # 返却2日前：返却日まで3日切ってる本：今日・明日・明後日が返却日
    # 返却3日前：返却日まで4日切ってる本：今日・明日・明後日・明々後日が返却日
    # 返却4日前：返却日まで5日切ってる本

    @pytest.mark.parametrize(
        "delta, xdays, result",
        [(2, 3, True), (3, 3, True), (0, 0, True), (0, 3, True), (5, 3, False)],
    )
    def test_is_expire_in_xdays(self, delta, xdays, result):
        today = RentalBook.get_jst_now_date()
        d = today + timedelta(days=delta)
        book = RentalBook("test", d.strftime("%Y/%m/%d"), True, "hoge")
        assert book.is_expire_in_xdays(xdays) is result

    @pytest.mark.parametrize(
        "delta, expected_text", [(5, " (あと5日)"), (0, " (今日ﾏﾃﾞ)"), (1, " (明日ﾏﾃﾞ)"), (-5, " (延滞)")]
    )
    def test_get_expire_text_from_today(self, delta, expected_text):
        today = RentalBook.get_jst_now_date()
        d = today + timedelta(days=delta)
        book: RentalBook = RentalBook("test", d.strftime("%Y/%m/%d"), True, "hoge")
        assert book.get_expire_text_from_today() == expected_text
