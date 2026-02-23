# Реализуйте функцию pair_with_lower_or_equal_difference(), которая принимает два аргумента в следующем порядке:
# nums – отсортированный по неубыванию список положительных целых чисел
# k – целое число
# Функция должна находить в списке nums пару чисел, разница между которыми меньше или равна k и при этом максимальна.
# Если таких пар несколько, функция должна выбрать ту, у которой минимальный элемент меньше. Возвращаемое значение функции – отсортированный по неубыванию кортеж из двух найденных чисел. Если в списке nums нет ни одной подходящей пары, возвращаемым значением функции должно быть None.


def pair_with_lower_or_equal_difference(nums: list[int], k: int) -> tuple[int, int] | None:
    left = 0
    right = 1
    best_diff = -1
    best_pair = None

    while right < len(nums):
        diff = nums[right] - nums[left]
        if diff <= k:
            if diff > best_diff or (diff == best_diff and nums[left] < best_pair[0]):
                best_diff = diff
                best_pair = (nums[left], nums[right])
            right += 1
        else:
            left += 1
            if left == right:
                right += 1

    return best_pair


print(pair_with_lower_or_equal_difference([2, 4, 7, 8, 10, 11], 3))
print(pair_with_lower_or_equal_difference([2, 3, 4, 7, 8, 10, 11], 2))
print(pair_with_lower_or_equal_difference([5], 1))
print(pair_with_lower_or_equal_difference([3, 3, 3, 3], 1))
print(pair_with_lower_or_equal_difference([1, 2, 3, 4], 0))
print(pair_with_lower_or_equal_difference([5, 5, 8, 8, 10, 10], 0))
