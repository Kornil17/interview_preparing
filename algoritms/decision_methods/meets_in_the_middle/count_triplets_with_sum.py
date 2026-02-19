# Реализуйте функцию count_triplets_with_sum(), которая принимает четыре аргумента в следующем порядке:
# nums1 – список целых чисел
# nums2 – список целых чисел
# nums3 – список целых чисел
# k – целое число
# Функция должна возвращать количество способов, которыми можно выбрать из списков nums1, nums2 и nums3 по одному числу так, чтобы сумма трех выбранных чисел была равна k.

from collections import Counter


def count_triplets_with_sum(
    nums1: list[int],
    nums2: list[int],
    nums3: list[int],
    k: int,
) -> int:
    count = 0
    target_count = Counter(nums3)
    for n in nums1:
        for n2 in nums2:
            total = k - (n + n2)
            count += target_count[total]
    return count

print(count_triplets_with_sum([1, 2], [0, 1], [3, 4], 5))         # (1, 1, 3), (1, 0, 4), (2, 0, 3)
print(count_triplets_with_sum([1], [1], [1], 3))                  # (1, 1, 1)
print(count_triplets_with_sum([-2, -1, 0], [3], [-3, 1], 2))      # (-2, 3, 1)
print(count_triplets_with_sum([1, 1, 1], [1, 1, 1], [1, 1, 1], 1))
print(count_triplets_with_sum([1], [-2], [1], 0))                 # (1, -2, 1)



