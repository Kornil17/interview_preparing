# Реализуйте функцию max_common_sum(), которая принимает один аргумент:
# nums – список положительных целых чисел
# Функция должна для каждого числа из списка nums вычислять сумму двух последних цифр и возвращать ту сумму, которая встречается чаще всего. Если таких сумм несколько, функция должна вернуть наибольшую из них.
# Примечание. Для однозначных чисел вторая последняя цифра считается равной нулю.


from collections import Counter
from math import floor, log10


def sum_of_last_two(n: int) -> int:
    if floor(log10(n)) + 1 > 1:
        return n % 10 + n // 10 % 10
    return n + 0


def max_common_sum(nums: list[int]) -> int:
    counts = Counter(sum_of_last_two(num) for num in nums)
    return max(counts.items(), key=lambda x: (x[1], x[0]))[0]


print(max_common_sum([10, 20, 21, 30, 100, 111]))
print(max_common_sum([1, 2, 3, 4, 5]))
print(max_common_sum([121, 21, 2221, 1122, 22]))
print(max_common_sum([121, 21, 2221, 1122, 3322, 22]))
print(max_common_sum([11, 11, 11, 11]))
print(max_common_sum([555]))





