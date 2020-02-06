from mmlibrary.books import Books
from mmlibrary.reserved_book import ReservedBook


class ReservedBooks(Books):
    def __init__(self):
        super().__init__()

    def create_and_append(self, data):
        status = data[1].get_text().strip()
        order = data[2].get_text().strip()
        title = data[3].get_text().strip()
        kind = data[4].get_text().strip()
        yoyaku_date = data[6].get_text().strip()
        torioki_date = data[7].get_text().strip()
        receive_lib = data[8].get_text().strip()

        reserved_book = ReservedBook(
            status, order, title, kind, yoyaku_date, torioki_date, receive_lib
        )

        self.append(reserved_book)

    def is_prepared(self) -> bool:
        for book in self.list:
            if book.is_prepared:
                return True
        return False
