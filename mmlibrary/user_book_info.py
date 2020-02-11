from mmlibrary.user import User
from mmlibrary.rental_books import RentalBooks
from mmlibrary.reserved_books import ReservedBooks


class UserBookInfo:
    def __init__(
        self,
        user: User,
        rental_books: RentalBooks = RentalBooks(),
        reserved_books: ReservedBooks = ReservedBooks(),
    ):
        self.user = user
        self.rental_books = rental_books
        self.reserved_books = reserved_books

    def __str__(self):
        string = """
username: {}
rentals:
{}
reserved:
{}""".format(
            self.user.disp_name, self.rental_books, self.reserved_books
        )
        return string
