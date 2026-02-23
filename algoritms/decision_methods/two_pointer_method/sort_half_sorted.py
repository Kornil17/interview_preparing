# Реализуйте функцию sort_half_sorted(), которая принимает один аргумент:
# nums – список из целых чисел, первая и вторая половины которого независимо друг от друга отсортированы по неубыванию; если длина списка нечетная, то его первая половина на единицу длиннее, чем вторая
# Функция должна выполнять сортировку списка nums по неубыванию и возвращать полученный результат в виде нового списка.


def sort_half_sorted(nums: list[int]) -> list[int]:
    # Находим точку разрыва
    break_point = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            break_point = i
            break

    if break_point == 0:
        return nums[:]

    left, right = 0, break_point
    result = []
    while left < break_point and right < len(nums):
        if nums[left] < nums[right]:
            result.append(nums[left])
            left += 1
        else:
            result.append(nums[right])
            right += 1
    result.extend(nums[left:break_point])
    result.extend(nums[right:])
    return result

print(sort_half_sorted([2, 4, 6, 1, 3, 5]))
print(sort_half_sorted([2, 4, 6, 7, 1, 3, 5]))
print(sort_half_sorted([1]))
print(sort_half_sorted([1, 1, 1, 1, 1]))
print(sort_half_sorted([1, 2, 3, 4, 5]))
print(sort_half_sorted([1, 2, 3, -1, 0, 1]))
