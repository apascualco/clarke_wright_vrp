from typing import Dict, Tuple, List
import math
from operator import itemgetter


def calculate_distance(
    coord1: Tuple[float, float],
    coord2: Tuple[float, float]
) -> float:
    return math.sqrt((coord1[0]-coord2[0])**2+(coord1[1]-coord2[1])**2)


def saving_between_cities_and_warehouse(
        coord_left: Tuple[float, float],
        coord_right: Tuple[float, float],
        warehouse: Tuple[float, float]
) -> float:
    distance_city_left_to_city_right = \
        calculate_distance(coord_left, coord_right)
    distance_coord_left_to_warehouse = \
        calculate_distance(coord_left, warehouse)
    distance_coord_right_to_warehouse = \
        calculate_distance(coord_right, warehouse)
    return distance_coord_left_to_warehouse + \
        distance_coord_right_to_warehouse - \
        distance_city_left_to_city_right


def savings(
    cities: Dict[str, Tuple[float, float]],
    warehouse: (float, float)
) -> Dict[Tuple[float, float], Tuple[float, float]]:
    savings = {}
    for city_left in cities:
        for city_right in cities:
            if city_left != city_right:
                if not (city_left, city_right) in savings:
                    savings[city_left, city_right] = \
                        saving_between_cities_and_warehouse(
                            cities[city_left],
                            cities[city_right],
                            warehouse
                        )
    return sorted(savings.items(), key=itemgetter(1), reverse=True)


def delivery_route(delivery_routes: List, city: Tuple[str, str]) \
        -> Tuple[str, str]:
    for route in delivery_routes:
        if city in route:
            return route
    return None


def delivery_weight(delivery_routes: List, orders: Dict[str, int]) -> int:
    weight: int = 0
    for city in delivery_routes:
        weight += orders[city]
    return weight


def join_delivery_route(delivery_routes: List, route_left: List,
                        route_right: List, cities: Tuple[str, str],
                        orders: Dict[str, int], max_weight: int
                        ) -> None:
    if route_left[0] == cities[0] \
            and route_right[len(route_right)-1] == cities[1]:
        if delivery_weight(
            route_left + route_right,
            orders
        ) <= max_weight:
            delivery_routes[delivery_routes.index(route_right)]\
                .extend(route_left)
            delivery_routes.remove(route_left)

    elif route_left[len(route_left)-1] == cities[0] \
            and route_right[0] == cities[1]:
        if delivery_weight(
            route_left + route_right,
            orders
        ) <= max_weight:
            delivery_routes[delivery_routes.index(route_left)]\
                .extend(route_right)
            delivery_routes.remove(route_right)


def city_appear_only_in_route_left(delivery_routes: List, route_left: List,
                                   cities: Tuple[str, str],
                                   orders: Dict[str, int], max_weight: int
                                   ) -> None:
    if route_left[0] == cities[0]:
        if delivery_weight(route_left + [cities[1]], orders) <= max_weight:
            delivery_routes[delivery_routes.index(route_left)]\
                .insert(0, cities[1])

    elif route_left[len(route_left)-1] == cities[0]:
        if delivery_weight(route_left + [cities[1]], orders) <= max_weight:
            delivery_routes[delivery_routes.index(route_left)]\
                .append(cities[1])


def city_appear_only_in_route_right(delivery_routes: List, route_right: List,
                                    cities: Tuple[str, str],
                                    orders: Dict[str, int], max_weight: int
                                    ) -> None:
    if route_right == cities[1]:
        if delivery_weight(route_right + [cities[0]], orders) <= max_weight:
            delivery_routes[delivery_routes.index(route_right)]\
                .insert(0, cities[0])

    elif route_right[len(route_right)-1] == cities[1]:
        if delivery_weight(route_right + [cities[0]], orders) <= max_weight:
            delivery_routes[delivery_routes.index(route_right)]\
                .append(cities[0])


def greedy(
        s: Dict[Tuple[float, float], float],
        orders: Dict[str, int],
        max_weight: int = 40
) -> List:
    delivery_routes: List = []
    for cities, distance in s:
        print(delivery_routes)
        route_left: Tuple[str, str] = \
            delivery_route(delivery_routes, cities[0])
        route_right: Tuple[str, str] = \
            delivery_route(delivery_routes, cities[1])
        if route_left and route_right and route_left == route_right:
            continue

        elif route_left and route_right and route_left != route_right:
            join_delivery_route(delivery_routes, route_left, route_right,
                                cities, orders, max_weight)

        elif not route_left and not route_right:
            if delivery_weight(cities, orders) <= max_weight:
                delivery_routes.append([cities[0], cities[1]])

        elif route_left and not route_right:
            city_appear_only_in_route_left(delivery_routes, route_left, cities,
                                           orders, max_weight)

        elif not route_left and route_right:
            city_appear_only_in_route_right(delivery_routes, route_right,
                                            cities, orders, max_weight)
    return delivery_routes
