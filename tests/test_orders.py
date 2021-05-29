import unittest
from vrp.order import Order


class OrdersTest(unittest.TestCase):

    def test_add_order(self):
        order: Order = Order()
        order.orders.clear()

        weight: int = 20
        order.add_order("Barcelona", weight)
        barcelona_weight: int = order.orders["Barcelona"]

        self.assertIsNotNone(
            barcelona_weight,
            "Barcelona weight shouldn't be null"
        )
        self.assertEqual(barcelona_weight, weight, "Incorrect weight")
