from typing import Tuple, Dict
import unittest
from vrp.distance import Distance
from vrp.vrp import savings


class SavingsTest(unittest.TestCase):

    def test_savings(self):
        distance: Distance = Distance()
        distance.distances.clear()

        distance.add_distance("Barcelona", (41.3, 2.1))
        distance.add_distance("Girona", (41.9, 2.8))

        warehouse: Tuple[float, float] = (50.1, 2.5)

        s: Dict[Tuple[float, float], Tuple[float, float]] = \
            savings(distance.distances, warehouse)
        self.assertIsNotNone(s)

        saving_distance: float = 16.09261774225319
        self.assertEqual(("Barcelona", "Girona"), s[0][0])
        self.assertEqual(
            s[0][1],
            saving_distance,
            "The distance it's not correct"
        )
        self.assertEqual(("Girona", "Barcelona"), s[1][0])
        self.assertEqual(
            s[1][1],
            saving_distance,
            "The distance it's not correct"
        )
