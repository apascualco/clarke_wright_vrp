from typing import Tuple
import unittest
from vrp.distance import Distance


class DistancesTest(unittest.TestCase):

    def test_add_distance(self):
        distance: Distance = Distance()

        latitude: float = 42.3
        longitude: float = 2.1

        distance.add_distance("Barcelona", (latitude, longitude))
        barcelona_coords: Tuple[float, float] = distance.distances["Barcelona"]

        self.assertIsNotNone(barcelona_coords, "Coords shouldn't be null")
        barcelona_latitude: float = barcelona_coords[0]
        barcelona_longitude: float = barcelona_coords[1]

        self.assertEqual(barcelona_latitude, latitude, "Incorrect latitude")
        self.assertEqual(barcelona_longitude, longitude, "Incorrect longitude")
