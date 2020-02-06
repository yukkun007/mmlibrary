import os
import logging
from typing import Dict, List
from dotenv import load_dotenv
from mmlibrary.user import User
from mmlibrary.library import Library
from mmlibrary.message_maker import MessageMaker
from mmlibrary.user_book_info import UserBookInfo


load_dotenv(verbose=True)


def search_all(params: Dict) -> List[str]:
    library = Library()
    message_maker = MessageMaker()

    rental_infos = []
    reserved_infos = []

    messages = []
    users = _fix_users(params)
    for user in users:
        # 指定ユーザの借りている本を全て取得
        rental_books = library.get_all_rental_books(user)
        info = UserBookInfo(user, rental_books=rental_books)
        rental_infos.append(info)
        # 指定ユーザの予約本を全て取得
        # reserved_books = library.get_all_reserved_books(user)
        # info = UserBookInfo(user, reserved_books=reserved_books)
        # reserved_infos.append(info)

    # 各ユーザの借り本・予約本をまとめて表示
    messages.append(message_maker.get_all_users_rental_books_message(rental_infos))
    # TODO
    # message_maker.get_all_users_reserved_books_message(reserved_infos)
    return messages


def search_rental(params: Dict) -> List[str]:
    library = Library()
    message_maker = MessageMaker()

    messages = []
    users = _fix_users(params)
    for user in users:
        # 指定ユーザの借りている本を全て取得
        rental_books = library.get_all_rental_books(user)
        info = UserBookInfo(user, rental_books=rental_books)
        messages.append(message_maker.get_rental_books_message(info))
    return messages


def search_expire(params: Dict) -> List[str]:
    library = Library()
    message_maker = MessageMaker()

    messages = []
    users = _fix_users(params)
    for user in users:
        # 指定ユーザの借りている本で2日以内に期限切れの本を取得
        expire_books = library.get_expire_rental_books(user, param={"xdays": 2})
        # 0件でも空のリストができているので取り敢えずメッセージ生成
        if expire_books is not None:
            info = UserBookInfo(user, rental_books=expire_books)
            messages.append(message_maker.get_rental_books_message(info))

        # 0件の場合のメッセージ処理
        if len(expire_books.list) <= 0:
            zero_behavior = params.get("zero", "always")
            if zero_behavior == "always":
                pass
            elif zero_behavior == "message":
                # メッセージ作り直し
                messages = []
                messages.append("{}({})の本で、期限切れが近い本はありません。".format(user.disp_name, user.id))
            elif zero_behavior == "none":
                messages = []

    return messages


def search_reserve(params: Dict) -> List[str]:
    library = Library()
    message_maker = MessageMaker()

    messages = []
    users = _fix_users(params)
    for user in users:
        # 指定ユーザの予約本を全て取得
        reserved_books = library.get_all_reserved_books(user)
        info = UserBookInfo(user, reserved_books=reserved_books)
        messages.append(message_maker.get_reserved_books_message(info))
    return messages


def search_prepare(params: Dict) -> List[str]:
    library = Library()
    message_maker = MessageMaker()

    messages = []
    users = _fix_users(params)
    for user in users:
        # 指定ユーザの借りている本を全て取得
        rental_books = library.get_all_rental_books(user)
        # 指定ユーザの予約本で「準備完了」「移送中」の本を取得
        prepared_reserved_books = library.get_prepared_reserved_books(user)
        # 0件でも空のリストができているので取り敢えずメッセージ生成
        if prepared_reserved_books is not None:
            info = UserBookInfo(
                user, rental_books=rental_books, reserved_books=prepared_reserved_books
            )
            messages.append(message_maker.get_rental_and_reserved_books_message(info))

        # 0件の場合のメッセージ処理
        if len(prepared_reserved_books.list) <= 0:
            zero_behavior = params.get("zero", "always")
            if zero_behavior == "always":
                pass
            elif zero_behavior == "message":
                # メッセージ作り直し
                messages = []
                messages.append("{}({})の予約本で、届いている本はありません。".format(user.disp_name, user.id))
            elif zero_behavior == "none":
                messages = []

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
