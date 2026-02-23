# Реализуйте функцию have_common_element(), которая принимает два аргумента в следующем порядке:
# nums1 – отсортированный по неубыванию список целых чисел
# nums2 – отсортированный по неубыванию список целых чисел
# Функция должна возвращать значение True, если существует такое число, которое содержится как в списке nums1, так и в списке nums2.
# В противном случае функция должна вернуть значение False.


def have_common_element(
    nums1: list[int],
    nums2: list[int],
) -> bool:
    left = 0
    right = 0
    while left < len(nums1) and right < len(nums2):
        if nums1[left] == nums2[right]:
            return True
        elif nums1[left] < nums2[right]:
            left += 1
        elif nums1[left] > nums2[right]:
            right += 1

    return False


print(have_common_element([1, 2, 3, 4], [2, 8, 16]))
print(have_common_element([1, 2, 3], [1, 2, 3, 4]))
print(have_common_element([1, 3], [0, 2, 4, 8]))
print(have_common_element([1], [2]))
print(have_common_element([1, 1, 1], [1]))
print(have_common_element([-1, 0, 1], [0, 2]))
nums1 = [-10, -9, -9, -8, -8, -7, -6, -4, -3, -2, -2, -1, -1, -1, 0, 3, 3, 4, 4, 7, 8, 8, 8, 9, 9]
nums2 = [11, 12, 12, 14, 15, 17, 17, 18, 19, 19]
print(have_common_element(nums1, nums2))
nums1 = list(range(10**5))
nums2 = [99999]
print(have_common_element(nums1, nums2))