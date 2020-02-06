class ReservedBook:
    def __init__(self, status, order, title, kind, yoyaku_date, torioki_date, receive_lib):
        self.status: str = status
        self.order: str = order
        self.order_num: int = self._get_order_num(order)
        self.title: str = title
        self.kind: str = kind
        self.yoyaku_date: str = yoyaku_date
        self.torioki_date: str = torioki_date
        self.receive_lib: str = receive_lib
        self.is_prepared: bool = self._is_prepared(status)
        self.is_dereverd: bool = self._is_dereverd(status)

    def get_list_string(self) -> str:
        string = "{},{},{},{},{},{}".format(
            self.status, self.order, self.title, self.kind, self.yoyaku_date, self.receive_lib
        )
        return string

    def __str__(self) -> str:
        string = (
            """
            status: {}
            order: {}
            title: {}
            kind: {}
            yoyaku_date: {}
            receive_lib: {}"""
        ).format(self.status, self.order, self.title, self.kind, self.yoyaku_date, self.receive_lib)
        return string

    def _is_prepared(self, status: str) -> bool:
        if status == "ご用意できました":
            return True
        return False

    def _is_dereverd(self, status: str) -> bool:
        if status == "移送中です":
            return True
        return False

    def _get_order_num(self, order: str) -> int:
        try:
            return int(order.split("/")[0])
        except ValueError:
            return 0
