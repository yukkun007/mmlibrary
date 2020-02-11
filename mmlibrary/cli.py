import os
import argparse
import logging
from typing import List, Union
from dotenv import load_dotenv
from mmlibrary.user import User
from mmlibrary.user_book_info import UserBookInfo
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
    parser.add_argument("-r", "--result_type", help="取得する結果の形式を指定します", choices=["message", "info"])
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
        "result_type": args.result_type,
    }

    if args.mode == "rental" or args.mode == "expire":
        # 借りてる系
        result = search_rental(params)
        _print_result(result)
    elif args.mode == "reserve" or args.mode == "prepare":
        # 予約系
        result = search_reserve(params)
        _print_result(result)
    else:
        parser.print_help()


def _print_result(result_list: Union[List[str], List[UserBookInfo]]):
    if len(result_list) > 0:
        print("=====================================")
    for result in result_list:
        print(result)
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
