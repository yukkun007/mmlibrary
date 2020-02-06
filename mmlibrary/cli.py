import os
import argparse
import logging
from typing import List
from dotenv import load_dotenv
from mmlibrary.user import User
from .core import search_all, search_rental, search_expire, search_reserve, search_prepare


def main():
    parser = argparse.ArgumentParser(
        description="""
    図書館で借りた本, 予約した本の状況を検索します。
    """
    )

    parser.add_argument("-u", "--users", help="検索対象のユーザを名前(name)で指定します", nargs="*")
    parser.add_argument(
        "-m", "--mode", help="検索モード", choices=["all", "rental", "expire", "reserve", "prepare"]
    )
    parser.add_argument(
        "-z",
        "--zero",
        help="結果0件の場合の表示モード",
        default="always",
        choices=["always", "message", "none"],
    )

    parser.add_argument("-A", "--alluser", help="全ユーザを対象に検索します", action="store_true")
    parser.add_argument("-D", "--debug", help="デバッグ出力をONにします", action="store_true")
    parser.add_argument("-U", "--userlist", help="登録済みユーザのリストを表示します", action="store_true")

    args = parser.parse_args()

    # userlistの処理
    # returnする
    if args.userlist:
        _show_user_list()
        return

    # log設定
    formatter = "%(asctime)s : %(levelname)s : %(message)s"
    if args.debug:
        # ログレベルを DEBUG に変更
        logging.basicConfig(level=logging.DEBUG, format=formatter)
    else:
        logging.basicConfig(format=formatter)

    params = {"all_user": args.alluser, "users": args.users, "zero": args.zero}

    if args.mode == "all":
        # 借りてる + 予約
        messages = search_all(params)
        _print_messages(messages)
    elif args.mode == "rental":
        # 借りてる
        messages = search_rental(params)
        _print_messages(messages)
    elif args.mode == "expire":
        # 借りてる(期限切れ間近のみ)
        messages = search_expire(params)
        _print_messages(messages)
    elif args.mode == "reserve":
        # 予約
        messages = search_reserve(params)
        _print_messages(messages)
    elif args.mode == "prepare":
        # 予約(到着済みのみ) + 借りてる
        messages = search_prepare(params)
        _print_messages(messages)
    else:
        parser.print_help()


def _print_messages(messages: List[str]):
    if len(messages) > 0:
        print("=====================================")
    for message in messages:
        print(message)
        print("=====================================")


def _show_user_list():
    load_dotenv(verbose=True)
    users = []
    users.append(User(os.environ["USER1"]))
    users.append(User(os.environ["USER2"]))
    users.append(User(os.environ["USER3"]))
    users.append(User(os.environ["USER4"]))
    print("user list is.....")
    for user in users:
        print("\tname: {} [{}({})]".format(user.name, user.disp_name, user.id))


if __name__ == "__main__":
    main()
