import os
import logging
from os.path import join, dirname
from typing import Dict, List
from dotenv import load_dotenv
from mmlibrary.user import User
from mmlibrary.library import Library
from mmlibrary.message_maker import MessageMaker
from mmlibrary.user_book_info import UserBookInfo


load_dotenv(dotenv_path=join(dirname(__file__), ".env"), verbose=True)


def search_rental(params: Dict) -> List[str]:
    library: Library = Library()
    message_maker: MessageMaker = MessageMaker()
    rental_infos: List[UserBookInfo] = []
    messages: List[str] = []

    users = _fix_users(params)
    for user in users:
        if params.get("mode", "rental") == "expire":
            # 指定ユーザの借りている本で2日以内に期限切れの本を取得
            rental_books = library.get_expire_rental_books(user, param={"xdays": 2})
        else:
            # 指定ユーザの借りている本を全て取得
            rental_books = library.get_all_rental_books(user)

        info = UserBookInfo(user, rental_books=rental_books)
        if params.get("separate", False):
            _append_message(messages, message_maker.get_rental_books_message(info, params))
        else:
            rental_infos.append(info)

    if params.get("separate", False) is False:
        # 各ユーザの借り本をまとめて表示
        _append_message(
            messages, message_maker.get_all_users_rental_books_message(rental_infos, params)
        )

    return messages


def _append_message(messages: List[str], message: str) -> None:
    if message is not None and message is not "":
        messages.append(message)
    else:
        logging.debug("message is not appended. because message is empty.")


def search_reserve(params: Dict) -> List[str]:
    library: Library = Library()
    message_maker: MessageMaker = MessageMaker()
    reserved_infos: List[UserBookInfo] = []
    messages: List[str] = []

    users = _fix_users(params)
    for user in users:
        if params.get("mode", "reserve") == "prepare":
            # 指定ユーザの借りている本を全て取得
            rental_books = library.get_all_rental_books(user)
            # 指定ユーザの予約本で「準備完了」「移送中」の本を取得
            reserved_books = library.get_prepared_reserved_books(user)
            info = UserBookInfo(user, rental_books=rental_books, reserved_books=reserved_books)
        else:
            # 指定ユーザの予約本を全て取得
            reserved_books = library.get_all_reserved_books(user)
            info = UserBookInfo(user, reserved_books=reserved_books)

        if params.get("separate", False):
            if params.get("mode", "reserve") == "prepare":
                _append_message(
                    messages, message_maker.get_rental_and_reserved_books_message(info, params)
                )
            else:
                _append_message(messages, message_maker.get_reserved_books_message(info, params))
        else:
            reserved_infos.append(info)

    if params.get("separate", False) is False:
        # 各ユーザの予約本をまとめて表示
        _append_message(
            messages, message_maker.get_all_users_reserved_books_message(reserved_infos, params)
        )

    return messages


def _fix_users(params: Dict) -> List[User]:
    users = []
    users.append(User(os.environ["USER1"]))
    users.append(User(os.environ["USER2"]))
    users.append(User(os.environ["USER3"]))
    users.append(User(os.environ["USER4"]))

    user_dict = {}
    for user in users:
        user_dict[user.name] = user

    if params.get("all_user", False):
        return users
    else:
        new_users = []
        target_users: List[str] = params["users"]
        for target_user in target_users:
            new_user = user_dict.get(target_user)
            if new_user is not None:
                new_users.append(new_user)
        if len(new_users) <= 0:
            logging.warning("user not found.")
        return new_users
