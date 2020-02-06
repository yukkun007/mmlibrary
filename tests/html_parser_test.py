import os
import pytest
from unittest.mock import patch
from dotenv import load_dotenv
from mmlibrary.user import User
from mmlibrary.html_page import HtmlPage
from mmlibrary.html_parser import HtmlParser
from mmlibrary.library import Library
from mmlibrary.rental_books import RentalBooks
from mmlibrary.reserved_books import ReservedBooks
from mmlibrary.books import Books


class TestHtmlParser:
    def setup(self):
        load_dotenv(verbose=True)

    @pytest.mark.slow
    def test_get_rental_books(self):
        page = HtmlPage()
        user = User(os.environ["USER1"])
        html = page.fetch_login_page(Library.LIBRALY_HOME_URL, user)
        HtmlParser.get_rental_books(html)
        page.release_resource()

    def test_get_rental_books_no_table(self):
        with patch("mmlibrary.html_parser.HtmlParser._get_books_table") as method:
            method.return_value = None
            books = HtmlParser.get_rental_books(None)
            assert isinstance(books, RentalBooks)
            assert books.len == 0

    def test_get_reserved_books_no_table(self):
        with patch("mmlibrary.html_parser.HtmlParser._get_books_table") as method:
            method.return_value = None
            books = HtmlParser.get_reserved_books(None)
            assert isinstance(books, ReservedBooks)
            assert books.len == 0

    @pytest.mark.parametrize(
        "type, table_name", [("RentalBooks", "FormLEND"), ("ReservedBooks", "FormRSV")]
    )
    def test_get_books_table(self, type, table_name):
        with patch("mmlibrary.html_parser.HtmlParser._get_table") as mock:
            HtmlParser._get_books_table(None, type)
            mock.assert_called_once_with(None, table_name)

    def test_get_books_table_empty(self):
        HtmlParser._get_books_table(None, type="hoge")

    def test_get_table_empty(self):
        result = HtmlParser._get_table("<html></html>", "empty")
        assert result is None

    def test_create_books(self):
        books = HtmlParser._create_books(type="hoge")
        assert isinstance(books, Books)
