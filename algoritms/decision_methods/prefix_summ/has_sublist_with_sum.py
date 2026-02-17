# Реализуйте функцию has_sublist_with_sum(), которая принимает два аргумента в следующем порядке:
# nums – список целых чисел
# k – целое число
# Функция должна возвращать значение True, если в списке nums есть подсписок с суммой элементов, равной k.
# В противном случае функция должна вернуть значение False.



def has_sublist_with_sum(nums: list[int], k: int) -> bool:
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]

    seen = {0}
    for i in range(1, n + 1):
        target = prefix[i] - k
        if target in seen:
            return True
        seen.add(prefix[i])
    return False


print(has_sublist_with_sum([3, -2, 5, 1, 2], 4))      # [-2, 5, 1]
print(has_sublist_with_sum([2, 4, 6, 8], 5))          # подходящего подсписка нет
print(has_sublist_with_sum([3], 3))                   # [3]
print(has_sublist_with_sum([1, -5, 1, 2, 1, 3], 0))   # [1, -5, 1, 2, 1]
print(has_sublist_with_sum([1, 2, 3, 4, 5], 9))       # [4, 5]
print(has_sublist_with_sum([-3, -2, -5, -2, 0], -9))  # [-2, -5, -2]
