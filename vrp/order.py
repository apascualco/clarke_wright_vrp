from typing import Dict


class Order(object):

    def __init__(self, orders: Dict[str, int] = {}):
        self.orders = orders

    def add_order(self, destination: str, weight: int):
        self.orders[destination] = weight
