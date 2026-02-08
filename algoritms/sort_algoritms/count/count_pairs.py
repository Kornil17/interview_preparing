# Реализуйте функцию count_pairs(), которая принимает один аргумент:
# nums – список, содержащий только целые числа в диапазоне от −1000 до 1000 включительно
# Функция должна возвращать количество всех различных пар чисел (i; j) таких, что:
# j >= i
# nums[i] == nums[j]


from collections import Counter


def count_pairs(nums: list[int]) -> int:
    result = 0
    counts = Counter(nums)

    for count in counts.values():
        result += count * (count + 1) // 2  # C(n+1,2) = n*(n+1)/2

    return result


print(count_pairs([1, 2, 3, 4]))       # пары: (0; 0), (1; 1), (2; 2), (3; 3)
