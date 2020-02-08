import os
import pytest
from os.path import join, dirname
from typing import List
from dotenv import load_dotenv
from mmlibrary.user import User
from mmlibrary.library import Library
from mmlibrary.message_maker import MessageMaker
from mmlibrary.user_book_info import UserBookInfo


class TestLibrary:
    def setup(self):
        load_dotenv(verbose=True)

    @pytest.fixture()
    def library1(self) -> Library:
        return Library()

    @pytest.fixture()
    def users1(self) -> List[User]:
        return [User(os.environ["USER1"])]

    @pytest.fixture()
    def users2(self) -> List[User]:
        return [User(os.environ["USER1"]), User(os.environ["USER2"])]

    @pytest.mark.slow
    def test_get_all_books(self, library1, users1):
        mmaker = MessageMaker()
        for user in users1:
            # 指定ユーザの借りている本を全て取得
            rental_books = library1.get_all_rental_books(user)
            print("====================")
            print("指定ユーザの借りている本を全て取得")
            print("====================")
            print(rental_books)
            print(mmaker.get_rental_books_message(UserBookInfo(user, rental_books=rental_books)))
            # 指定ユーザの予約本を全て取得
            reserved_books = library1.get_all_reserved_books(user)
            print("====================")
            print("指定ユーザの予約している本を全て取得")
            print("====================")
            print(reserved_books)
            print(
                mmaker.get_reserved_books_message(UserBookInfo(user, reserved_books=reserved_books))
            )

            print("====================")
            print("指定ユーザの借り本・予約本を全て表示")
            print("====================")
            info = UserBookInfo(user, rental_books=rental_books, reserved_books=reserved_books)
            print(mmaker.get_rental_and_reserved_books_message(info))

    @pytest.mark.slow
    def test_get_spesific_books(self, library1, users1):
        mmaker = MessageMaker()
        for user in users1:
            # 指定ユーザの借りている本で2日以内に期限切れの本を取得
            expire_books = library1.get_expire_rental_books(user, param={"xdays": 2})
            print("====================")
            print("期限切れ間近の本のみ取得")
            print("====================")
            if expire_books is not None or len(expire_books.list) == 0:
                print(expire_books)
                print(
                    mmaker.get_rental_books_message(UserBookInfo(user, rental_books=expire_books))
                )
            # 指定ユーザの予約本で「準備完了」「移送中」の本を取得
            prepared_reserved_books = library1.get_prepared_reserved_books(user)
            print("====================")
            print("準備できた予約本のみ取得")
            print("====================")
            if prepared_reserved_books is not None or len(prepared_reserved_books.list):
                print(prepared_reserved_books)
                print(
                    mmaker.get_reserved_books_message(
                        UserBookInfo(user, reserved_books=prepared_reserved_books)
                    )
                )

    @pytest.mark.slow
    def test_get_all_users_books(self, library1, users1):
        infos = []
        mmaker = MessageMaker()
        for user in users1:
            # 指定ユーザの借りている本を全て取得
            rental_books = library1.get_all_rental_books(user)
            # 指定ユーザの予約本を全て取得
            reserved_books = library1.get_all_reserved_books(user)

            info = UserBookInfo(user, rental_books=rental_books, reserved_books=reserved_books)
            infos.append(info)

        # 各ユーザの借り本・予約本をまとめて表示
        print(mmaker.get_all_users_rental_books_message(infos))
        print(mmaker.get_all_users_reserved_books_message(infos))
