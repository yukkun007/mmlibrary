from typing import List, Dict


class Books:
    def __init__(self) -> None:
        self._list: List = []
        self._filter_type: str = "none"
        self._filter_param: Dict = {}

    @property
    def list(self) -> List:
        return self._list

    @list.setter
    def list(self, list: List) -> None:
        self._list = list

    @property
    def filter_type(self) -> str:
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type: str) -> None:
        self._filter_type = filter_type

    @property
    def filter_param(self) -> Dict:
        return self._filter_param

    @filter_param.setter
    def filter_param(self, filter_param: Dict) -> None:
        self._filter_param = filter_param

    @property
    def len(self) -> int:
        return len(self._list)

    def append(self, book) -> None:
        self._list.append(book)

    def get(self, index: int):
        return self._list[index]

    def create_and_append(self, data):
        pass

    def __str__(self) -> str:
        string = ""
        for item in self._list:
            string += "{}\n".format(item.get_list_string())
        return string
