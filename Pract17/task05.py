import random

desc = """
Напишите рекурсивную функцию, которая принимает список из 100 целых чисел,
полученных случайным образом, и находит позицию,
с которой начинается последовательность из 10 чисел, сумма которых минимальна."""


# def index_of_min_sum_sequence(collection: list, sequence_length):
#     if sequence_length > len(collection):
#         raise ValueError('sequence is bigger than collection')
#     temp = sum(collection[:sequence_length])
#     position = 0
#     for i in range(len(collection) - sequence_length + 1):
#         if sum(collection[i:i+sequence_length]) < temp:
#             position = i
#         temp = sum(collection[i:i + sequence_length])
#     return position
#
#
def random_collection(range_nums: tuple, length: int):
    return [random.randint(*range_nums) for _ in range(length)]


sums = []


def index_of_min_sum_sequence(collection, seq_len, position):
    if seq_len > len(collection):
        raise ValueError('sequence length is bigger than collection')
    global sums
    sums.append((sum(collection[-seq_len:]), len(collection) - seq_len))
    if len(collection) == seq_len:
        s = [i[0] for i in sums]
        return sums[s.index(min(s))][1]
    return index_of_min_sum_sequence(collection[:position], seq_len, position-1)


if __name__ == '__main__':
    random_numbers = random_collection((1, 5), 100)
    seq_length = 10
    print(f'Random numbers: {random_numbers}')
    print(f'Sequence length: {seq_length}')
    print(f'Index of min sum sequence: {index_of_min_sum_sequence(random_numbers, seq_length, len(random_numbers) - 1)}')





