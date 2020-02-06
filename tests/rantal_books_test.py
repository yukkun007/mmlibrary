from mmlibrary.rental_book import RentalBook
from mmlibrary.rental_books import RentalBooks
from mmlibrary.book_filter import BookFilter


class TestRentalBooks:
    def test_basic(self):
        books = RentalBooks()
        books.append(RentalBook("test1", "2017/01/01", True, "hoge"))
        books.append(RentalBook("test2", "9999/01/02", True, "hoge"))
        assert books.len == 2

    def test_filter_to_rental_books_expired(self):
        books = RentalBooks()
        book = RentalBook("test1", "2017/01/01", True, "hoge")
        books.append(book)
        books.append(RentalBook("test2", "9999/01/02", True, "hoge"))
        books.append(RentalBook("test3", "9999/01/07", True, "hoge"))
        new_books = BookFilter.do(books, BookFilter.TYPE_RENTAL_EXPIRED)
        assert new_books.len == 1
        assert new_books.get(0) == book  # メモリ比較

    def test_filter_to_rental_books_expire_in_xdays(self):
        books = RentalBooks()
        book = RentalBook("test1", "2017/01/02", True, "hoge")
        books.append(book)
        books.append(RentalBook("test2", "2017/01/03", True, "hoge"))
        books.append(RentalBook("test3", "2017/01/05", True, "hoge"))
        new_books = BookFilter.do(books, BookFilter.TYPE_RENTAL_EXPIRE, {"xdays": "5"})
        assert new_books.len == 3
        assert new_books.get(0) == book  # メモリ比較

    def test_sort(self):
        books = RentalBooks()
        books.append(RentalBook("test3", "2017/01/05", True, "hoge"))
        books.append(RentalBook("test1", "2017/01/03", True, "hoge"))
        book = RentalBook("test1", "2017/01/02", True, "hoge")
        books.append(book)
        new_books = BookFilter.do(books, BookFilter.TYPE_RENTAL_EXPIRE, {"xdays": "5"})
        assert new_books.len == 3
        assert new_books.get(0) == book  # メモリ比較
