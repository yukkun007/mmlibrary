import pytest
from mmlibrary.core import search_rental, search_reserve, _fix_users, _append_message


class TestCore:
    def setup(self):
        pass

    @pytest.mark.slow
    @pytest.mark.parametrize(
        "mode, zero_behavior, separate",
        [
            ("rental", "message", False),
            ("rental", "none", True),
            ("expire", "message", True),
            ("expire", "none", False),
        ],
    )
    def test_search_rental(self, mode, zero_behavior, separate):
        params = {
            "mode": mode,
            "all_user": False,
            "users": ["yutaka"],
            "debug": False,
            "zero_behavior": zero_behavior,
            "separate": separate,
        }
        search_rental(params)

    @pytest.mark.slow
    @pytest.mark.parametrize(
        "mode, zero_behavior, separate",
        [
            ("reserve", "message", False),
            ("reserve", "none", True),
            ("prepare", "message", True),
            ("prepare", "none", False),
        ],
    )
    def test_search_reserve(self, mode, zero_behavior, separate):
        params = {
            "mode": mode,
            "all_user": True,
            "users": ["yutaka"],
            "debug": False,
            "zero_behavior": zero_behavior,
            "separate": separate,
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
