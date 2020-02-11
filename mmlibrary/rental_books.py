from mmlibrary.books import Books
from mmlibrary.rental_book import RentalBook


class RentalBooks(Books):
    def __init__(self) -> None:
        super().__init__()

    def create_and_append(self, data) -> None:
        no = data[0].string.strip()
        # タイトル
        title = data[2].get_text().strip()
        # 返却期限日
        expire_date = data[7].get_text().strip()
        # 貸出更新
        can_extend_period = self._can_extend_period(data[1].get_text().strip())
        # 更新ボタンの名前
        extend_period_button_name = "L(" + no + ")"

        rental_book = RentalBook(title, expire_date, can_extend_period, extend_period_button_name)

        self.append(rental_book)

    def _can_extend_period(self, text: str) -> bool:
        if "延長できません" in text:
            return False
        if "すでに延長されています" in text:
            return False
        return True
