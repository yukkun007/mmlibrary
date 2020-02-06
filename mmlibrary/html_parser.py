import logging
from bs4 import BeautifulSoup
from mmlibrary.books import Books
from mmlibrary.rental_books import RentalBooks
from mmlibrary.reserved_books import ReservedBooks


class HtmlParser:
    @staticmethod
    def get_rental_books(html) -> RentalBooks:
        return HtmlParser._get_books(html, type="RentalBooks")

    @staticmethod
    def get_reserved_books(html) -> ReservedBooks:
        return HtmlParser._get_books(html, type="ReservedBooks")

    @staticmethod
    def _get_books(html, type: str = "RentalBooks") -> Books:
        books = HtmlParser._create_books(type)
        table = HtmlParser._get_books_table(html, type)
        if table is None:
            logging.warning("table is not found.")
            return books

        tds_list = HtmlParser._get_target_tds_list(table)
        for tds in tds_list:
            books.create_and_append(tds)

        logging.info("found {} {}.".format(books.len, books.__class__.__name__))

        return books

    @staticmethod
    def _create_books(type: str = "RentalBooks") -> Books:
        if type in {"RentalBooks"}:
            return RentalBooks()
        elif type == "ReservedBooks":
            return ReservedBooks()
        else:
            return Books()

    @staticmethod
    def _get_books_table(html, type: str = "RentalBooks"):
        if type in {"RentalBooks"}:
            return HtmlParser._get_table(html, "FormLEND")
        elif type == "ReservedBooks":
            return HtmlParser._get_table(html, "FormRSV")
        else:
            return None

    @staticmethod
    def _get_table(html, id_string):
        soup = BeautifulSoup(html, "html.parser")
        table = soup.select("form[name='" + id_string + "'] > div > table[border]")

        if len(table) <= 0:
            logging.warning("table not found.")
            return None

        return table

    @staticmethod
    def _get_target_tds_list(table):
        trs = table[0].find_all("tr")

        target_tds_list = []
        for tr in trs:
            tds = tr.find_all(["td", "th"])
            no = tds[0].string.strip()
            if no.isnumeric() is False:
                continue
            target_tds_list.append(tds)

        logging.info("number of target tr tag:{0}".format(len(target_tds_list)))

        return target_tds_list
