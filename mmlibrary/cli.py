import os
import argparse
import logging
from os.path import join, dirname
from typing import List
from dotenv import load_dotenv
from mmlibrary.user import User
from .core import search_rental, search_reserve


def main():
    parser = argparse.ArgumentParser(
        description="""
    図書館で借りた本, 予約した本の状況を検索します。
    """
    )

    parser.add_argument(
        "-m", "--mode", help="検索モードを指定します", choices=["rental", "expire", "reserve", "prepare"]
    )
    parser.add_argument("-u", "--users", help="検索対象のユーザを名前(name)で指定します", nargs="*")
    parser.add_argument(
        "-a", "--alluser", help="全ユーザを対象に検索します(--users指定は無効になります)", action="store_true"
    )
    parser.add_argument(
        "-z",
        "--zero",
        help="結果0件の場合の表示モードを指定します",
        default="always",
        choices=["always", "message", "none"],
    )
    parser.add_argument("-s", "--separate", help="結果をユーザごとに個別表示します", action="store_true")
    parser.add_argument("-d", "--debug", help="デバッグログ出力をONにします", action="store_true")
    parser.add_argument("-l", "--userlist", help="登録済みユーザのリストを表示します", action="store_true")

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

    params = {
        "mode": args.mode,
        "all_user": args.alluser,
        "users": args.users,
        "zero": args.zero,
        "separate": args.separate,
    }

    if args.mode == "rental" or args.mode == "expire":
        # 借りてる系
        messages = search_rental(params)
        _print_messages(messages)
    elif args.mode == "reserve" or args.mode == "prepare":
        # 予約系
        messages = search_reserve(params)
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
    load_dotenv(dotenv_path=join(dirname(__file__), ".env"), verbose=True)
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
