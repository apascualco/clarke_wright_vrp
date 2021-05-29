from typing import Tuple, Dict, List
import unittest
from vrp.distance import Distance
from vrp.order import Order
from vrp.vrp import savings, greedy


def data_stub():
    distance: Distance = Distance()
    distance.distances.clear()

    distance.add_distance("Barcelona", (41.230, 2.154))
    distance.add_distance("Manresa", (41.720, 1.822))
    distance.add_distance("Begues", (41.333, 1.933))
    distance.add_distance("Sant Cugat del Valles", (41.472, 2.086))
    distance.add_distance("Martorell", (41.474, 1.930))
    distance.add_distance("Badalona", (41.450, 2.247))
    distance.add_distance("Sant Vicenc dels Horts", (41.393, 2.006))
    distance.add_distance("Montcada", (41.483, 2.183))
    distance.add_distance("Viladecans", (41.314, 2.014))
    distance.add_distance("Sant Andreu de la Barca", (41.446, 1.971))

    order: Order = Order()
    order.orders.clear()

    order.add_order("Barcelona", 10)
    order.add_order("Manresa", 13)
    order.add_order("Begues", 7)
    order.add_order("Sant Cugat del Valles", 11)
    order.add_order("Martorell", 15)
    order.add_order("Badalona", 8)
    order.add_order("Sant Vicenc dels Horts", 6)
    order.add_order("Montcada", 7)
    order.add_order("Viladecans", 8)
    order.add_order("Sant Andreu de la Barca", 14)

    return distance, order


class GreedyTest(unittest.TestCase):

    def test_greedy_with_max_default_40(self):
        distance, order = data_stub()

        warehouse: Tuple[float, float] = (40.24, -3.41)

        s: Dict[Tuple[float, float], Tuple[float, float]] = \
            savings(distance.distances, warehouse)

        self.assertIsNotNone(s)

        delivery_routes: List = greedy(s, order.orders)
        self.assertIsNotNone(delivery_routes)
        expected_delivery_routes = [
            ['Barcelona', 'Badalona', 'Montcada', 'Sant Cugat del Valles'],
            [
                'Begues', 'Viladecans',
                'Sant Vicenc dels Horts', 'Sant Andreu de la Barca'
            ],
            ['Manresa', 'Martorell']
        ]
        self.assertEqual(delivery_routes, expected_delivery_routes)

    def test_greedy_with_max_50(self):
        distance, order = data_stub()

        warehouse: Tuple[float, float] = (40.24, -3.41)

        s: Dict[Tuple[float, float], Tuple[float, float]] = \
            savings(distance.distances, warehouse)

        self.assertIsNotNone(s)

        delivery_routes: List = greedy(s, order.orders, 50)
        self.assertIsNotNone(delivery_routes)
        expected_delivery_routes = [
            [
                'Viladecans', 'Barcelona', 'Badalona',
                'Montcada', 'Sant Cugat del Valles', 'Sant Vicenc dels Horts'
            ],
            ['Manresa', 'Martorell', 'Sant Andreu de la Barca', 'Begues']
        ]
        self.assertEqual(delivery_routes, expected_delivery_routes)
