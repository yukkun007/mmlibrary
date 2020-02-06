import pytest
from mmlibrary.core import (
    search_all,
    search_rental,
    search_reserve,
    search_expire,
    search_prepare,
    _fix_users,
)


class TestCore:
    def setup(self):
        pass

    @pytest.mark.slow
    def test_search_all(self):
        params = {"all_user": False, "users": ["yutaka"], "debug": True}
        search_all(params)

    @pytest.mark.slow
    def test_search_rental(self):
        params = {"all_user": False, "users": ["yutaka"], "debug": False}
        search_rental(params)

    @pytest.mark.slow
    def test_search_reserve(self):
        params = {"all_user": True, "users": ["yutaka"], "debug": False}
        search_reserve(params)

    @pytest.mark.slow
    def test_search_expire(self):
        params = {"all_user": False, "users": ["yutaka"], "debug": False}
        search_expire(params)

    @pytest.mark.slow
    def test_search_prepare(self):
        params = {"all_user": False, "users": ["yutaka"], "debug": False}
        search_prepare(params)

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
