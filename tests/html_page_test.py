import os
import pytest
from mmlibrary.user import User
from mmlibrary.html_page import HtmlPage
from mmlibrary.library import Library


class TestHtmlPages:
    def setup(self):
        pass

    @pytest.fixture()
    def html_page1(self):
        return HtmlPage()

    @pytest.mark.slow
    def test_fetch_login_page(self, html_page1):
        user = User(os.environ["USER1"])
        html_page1.fetch_login_page(Library.LIBRALY_HOME_URL, user)
