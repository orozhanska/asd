roads = [
    (0, 1, 4),
    (0, 2, 6),
    (0, 3, 7),
    (0, 4, 10),
    (1, 2, 2),
    (1, 3, 3),
    (1, 4, 6),
    (2, 3, 1),
    (2, 4, 4),
    (3, 4, 3)
]
list1 = [road[1] for road in roads]
city_names = [road[0] for road in roads]
city_names.extend(list1)
city_names = list(set(city_names))


print(city_names)