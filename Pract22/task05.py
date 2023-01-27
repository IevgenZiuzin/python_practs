desc = """
Существует два множества, содержащие названия городов.
Необходимо создать третье множество, содержащее уникальные названия для каждого множества.
"""


def get_unics(*args):
    return set.symmetric_difference(*args)


if __name__ == '__main__':
    largest_europe_cities = {'Istanbul', 'London', 'Berlin', 'Madrid', 'Kyiv', 'Rome'}
    largest_world_cities = {'Tokyo', 'Delhi', 'Beijing', 'Los Angeles', 'New York', 'Istanbul'}
    print(f'{desc}\n----------\n')
    print(f'Set 1: {largest_europe_cities}\n'
          f'Set 2: {largest_world_cities}\n'
          f'Intersection: {get_unics(largest_world_cities, largest_europe_cities)}')
