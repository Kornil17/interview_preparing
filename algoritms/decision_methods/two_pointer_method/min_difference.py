# Реализуйте функцию min_difference(), которая принимает два аргумента в следующем порядке:
# nums1 – список положительных целых чисел
# nums2 – список положительных целых чисел
# Функция должна выбирать одно число из списка nums1 и одно число из списка nums2 так, чтобы разница между этими числами была минимально возможной.
# Возвращаемое значение функции – разница между выбранными числами.


def min_difference(
    nums1: list[int],
    nums2: list[int],
) -> int:
    nums1.sort()
    nums2.sort()

    left, right = 0, 0
    minimum = float('inf')

    while left < len(nums1) and right < len(nums2):
        diff = abs(nums1[left] - nums2[right])
        minimum = min(diff, minimum)

        if nums1[left] < nums2[right]:
            left += 1
        else:
            right += 1
    return minimum



print(min_difference([4, 1, 5], [8, 11, 9, 10]))    # (5, 8)
print(min_difference([3, 2, 7, 5], [6, 4, 0]))      # (5, 6)
print(min_difference([3], [1]))                     # (3, 1)
print(min_difference([1, 2, 3], [1, 2, 3]))         # (1, 1)
print(min_difference([10, 10], [5, 5]))             # (10, 5)
