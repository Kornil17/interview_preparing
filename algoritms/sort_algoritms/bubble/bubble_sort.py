# Реализуйте функцию bubble_sort(), которая принимает один аргумент:
# nums – список целых чисел
# Функция должна выполнять сортировку списка nums по невозрастанию путем его изменения.


def bubble_sort(nums: list[int]) -> list[int]:
    for idx in range(len(nums) - 1):
        for idx2 in range(len(nums) - 1 - idx):
            if nums[idx2] < nums[idx2 + 1]:
                nums[idx2], nums[idx2 + 1] = nums[idx2 + 1], nums[idx2]
    return nums
