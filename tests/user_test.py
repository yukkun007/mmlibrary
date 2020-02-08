import os
from dotenv import load_dotenv
from mmlibrary.user import User


class TestUser:
    def setup(self):
        load_dotenv(verbose=True)

    def test_user(self):
        data_json = os.environ["USER_TEST1"]
        user = User(data_json)
        assert user.name == "test1"
        assert user.disp_name == "disp_test1"
