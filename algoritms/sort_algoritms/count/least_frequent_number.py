# Реализуйте функцию least_frequent_number(), которая принимает один аргумент:
# nums – список, содержащий только целые числа в диапазоне от 1 до 1000 включительно
# Функция должна возвращать число, которое встречается в списке nums реже всего.
# Если таких чисел в списке nums несколько, функция должна вернуть наименьшее из них.


from collections import Counter


def least_frequent_number(nums: list[int]) -> int:
    counts = Counter(nums)
    return min(counts.items(), key=lambda x: (x[1], x[0]))[0]


print(least_frequent_number([4, 2, 4, 1, 3, 2, 1]))
print(least_frequent_number([3, 2, 1, 1, 3, 2, 1]))
