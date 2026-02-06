# Реализуйте функцию insertion_sort(), которая принимает один аргумент:
# nums – список целых чисел
# Функция должна выполнять сортировку списка nums по невозрастанию путем его изменения.


def insertion_sort(nums: list[int]) -> list[int]:
    for idx in range(1, len(nums)):
        item = nums[idx]
        idx2 = idx - 1

        while idx2 >= 0 and item > nums[idx2]:
            nums[idx2 + 1] = nums[idx2]
            idx2 -= 1
        nums[idx2 + 1] = item
    return nums
