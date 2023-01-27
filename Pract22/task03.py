desc = """
Существует два множества, содержащие названия 
городов. Необходимо создать третье множество, содержащее названия,
которые есть в первом множестве, но нет во втором.
"""


def get_difference(*args):
    return set.difference(*args)


if __name__ == '__main__':
    largest_europe_cities = {'Istanbul', 'London', 'Berlin', 'Madrid', 'Kyiv', 'Rome'}
    largest_world_cities = {'Tokyo', 'Delhi', 'Beijing', 'Los Angeles', 'New York', 'Istanbul'}
    print(f'{desc}\n----------\n')
    print(f'Set 1: {largest_europe_cities}\n'
          f'Set 2: {largest_world_cities}\n'
          f'Intersection: {get_difference(largest_europe_cities, largest_world_cities)}')