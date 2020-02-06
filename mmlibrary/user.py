import json


class User:
    def __init__(self, data_json: str) -> None:
        data = json.loads(data_json)

        self.name: str = data.get("name")
        self.disp_name: str = data.get("disp_name")
        self.id: str = data.get("id")
        self.password: str = data.get("password")
