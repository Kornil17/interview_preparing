# Реализуйте функцию alternate_order(), которая принимает один аргумент:
# nums – список целых чисел
# Функция должна возвращать новый список, состоящий из всех элементов списка nums, расположенных в следующем порядке:
# nums[0], nums[-1], nums[1], nums[-2], nums[2], ... # первый, последний, второй, предпоследний, третий, ...


def alternate_order(nums: list[int]) -> list[int]:
    n = len(nums)
    result = []
    left, right = 0, n - 1

    while left < right:
        result.append(nums[left])
        result.append(nums[right])
        left += 1
        right -= 1

    if n % 2 != 0:
        result.append(nums[left])

    return result


print(alternate_order([1, 2, 3, 4, 5, 6]))
print(alternate_order([2, 8, 6, 0, 4]))
print(alternate_order([1]))
print(alternate_order([1, 1, 1, 1, 1]))
print(alternate_order([-1, 2, -3, 1, 0]))
print(alternate_order([1, 3, 5, 4, 2]))
