from typing import Dict


class BaseBookFilter:
    def __init__(self, param: Dict) -> None:
        self.param = param
