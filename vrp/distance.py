from typing import Dict, Tuple


class Distance(object):

    def __init__(self, distances: Dict[str, Tuple[float, float]] = {}):
        self.distances = distances

    def add_distance(
        self, name: str, coordinates: Tuple[float, float]
    ) -> None:
        self.distances[name] = coordinates
