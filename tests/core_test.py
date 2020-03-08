import pytest
from mmlibrary.core import search_rental, search_reserve, _fix_users, _append_message


class TestCore:
    def setup(self):
        pass

    @pytest.mark.slow
    @pytest.mark.parametrize(
        "mode, all_user, zero, separate, result_type",
        [("prepare", True, "message", True, "message")],
    )
    def test_search_used_pattern(self, mode, all_user, zero, separate, result_type):
        params = {
            "mode": mode,
            "all_user": all_user,
            "users": ["yutaka"],
            "debug": True,
            "zero": zero,
            "separate": separate,
            "result_type": result_type,
        }
        # result = search_rental(params)
        result = search_reserve(params)
        for message in result:
            print(message)
            print("\n")

    @pytest.mark.slow
    @pytest.mark.parametrize(
        "mode, zero, separate, result_type",
        [
            ("rental", "message", False, "info"),
            ("rental", "none", True, "message"),
            ("expire", "message", True, "info"),
            ("expire", "none", False, "message"),
        ],
    )
    def test_search_rental(self, mode, zero, separate, result_type):
        params = {
            "mode": mode,
            "all_user": False,
            "users": ["yutaka"],
            "debug": False,
            "zero": zero,
            "separate": separate,
            "result_type": result_type,
        }
        search_rental(params)

    @pytest.mark.slow
    @pytest.mark.parametrize(
        "mode, zero, separate, result_type",
        [
            ("reserve", "message", False, "info"),
            ("reserve", "none", True, "message"),
            ("prepare", "message", True, "info"),
            ("prepare", "none", False, "message"),
        ],
    )
    def test_search_reserve(self, mode, zero, separate, result_type):
        params = {
            "mode": mode,
            "all_user": True,
            "users": ["yutaka"],
            "debug": False,
            "zero": zero,
            "separate": separate,
            "result_type": result_type,
        }
        search_reserve(params)

    def test_fix_users_all(self):
        params = {"all_user": True, "users": ["hoge"], "debug": False}
        users = _fix_users(params)
        assert len(users) == 4

    def test_fix_users(self):
        params = {"all_user": False, "users": ["yutaka"], "debug": False}
        users = _fix_users(params)
        assert users[0].name == "yutaka"

    def test_fix_users_empty(self):
        params = {"all_user": False, "users": ["hoge"], "debug": False}
        users = _fix_users(params)
        assert len(users) == 0

    def test_append_message_empty(self):
        _append_message([], "")
