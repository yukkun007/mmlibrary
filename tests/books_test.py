from mmlibrary.books import Books


class TestBooks:
    def test_init(self):
        books = Books()
        assert books.list == []

    def test_create_and_append(self):
        books = Books()
        books.create_and_append({})
