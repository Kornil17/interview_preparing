# Реализуйте функцию count_pairs_divisible_by_three(), которая принимает один аргумент:
# nums – список, содержащий только целые числа в диапазоне от 1 до 1000 включительно
# Функция должна возвращать количество существующих в списке nums пар чисел, сумма которых делится на три без остатка.


from collections import Counter


def count_pairs_divisible_by_three(nums: list[int]) -> int:
    remainder_count = Counter(num % 3 for num in nums)
    # Количество пар:
    # 1) Оба числа с остатком 0
    pairs_count = remainder_count[0] * (remainder_count[0] - 1) // 2

    # 2) Одно с остатком 1, другое с остатком 2
    pairs_count += remainder_count[1] * remainder_count[2]

    return pairs_count

print(count_pairs_divisible_by_three([1, 2, 3, 4, 5]))    # пары: (1, 2), (1, 5), (2, 4), (4, 5)
print(count_pairs_divisible_by_three([3, 6, 9]))          # пары: (3, 6), (3, 9), (6, 9)
print(count_pairs_divisible_by_three([1, 1, 1, 1]))       # подходящих пар нет
print(count_pairs_divisible_by_three([1, 2]))             # пара: (1, 2)
print(count_pairs_divisible_by_three([3, 3, 3]))          # пары: (3, 3), (3, 3), (3, 3)
