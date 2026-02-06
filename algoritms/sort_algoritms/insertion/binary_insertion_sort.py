# Реализуйте функцию binary_insertion_sort(), которая принимает один аргумент:
# nums – список целых чисел
# Функция должна выполнять сортировку списка nums по неубыванию путем его изменения.


def binary_insertion_sort(nums: list[int]) -> list[int]:
    for idx in range(1, len(nums)):
        left, right = 0, idx
        target = nums[idx]

        while left <= right:
            middle = left + (right - left) // 2
            elem = nums[middle]

            if elem < target:
                left = middle + 1
            else:
                right = middle - 1

        for idx2 in range(idx - 1, left - 1, -1):
            nums[idx2 + 1] = nums[idx2]

        nums[left] = target

    return nums
