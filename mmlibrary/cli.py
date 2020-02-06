import argparse
import logging
from typing import List
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

    parser.add_argument("-A", "--all", help="全ユーザを対象に検索します", action="store_true")
    parser.add_argument("-D", "--debug", help="デバッグ出力をONにします", action="store_true")
    parser.add_argument("-U", "--userlist", help="登録済みユーザのリストを表示します", action="store_true")

    args = parser.parse_args()

    # userlistの処理
    # returnする

    # log設定
    if args.debug:
        # ログレベルを DEBUG に変更
        logging.basicConfig(level=logging.DEBUG)

    params = {"all_user": args.all, "users": args.users}

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
    print("=====================================")
    for message in messages:
        print(message)
        print("=====================================")


if __name__ == "__main__":
    main()
