from utils.time_measure import timer


@timer
def selection_sort(nums: list[int]) -> list[int]:
    """Сортировка выбором."""
    n = len(nums)

    for idx in range(n - 1):
        index_min = idx
        for idx2 in range(idx + 1, n):
            if nums[idx2] < nums[index_min]:
                index_min = idx2

        if index_min != idx:
            nums[idx], nums[index_min] = nums[index_min], nums[idx]

    return nums


@timer
def buble_sort(nums: list[int]) -> list[int]:
    """Сортировка пузырьком."""
    n = len(nums)

    for idx in range(n - 1):
        for idx2 in range(n - 1 - idx):
            if nums[idx2] > nums[idx2 + 1]:
                nums[idx2], nums[idx2 + 1] = nums[idx2 + 1], nums[idx2]

    return nums


@timer
def insertion_sort(nums: list[int]) -> list[int]:
    """Сортировка вставками."""
    n = len(nums)

    for idx in range(1, n):
        item = nums[idx]
        idx2 = idx - 1

        while idx2 >= 0 and item < nums[idx2]:
            nums[idx2 + 1] = nums[idx2]
            idx2 -= 1

        nums[idx2 + 1] = item
    return nums


nums = [3, 4, 5, 7, 9, 6, 2, 8, 1]
selection_sort(nums)
print(nums)


nums2 = [3, 4, 5, 7, 9, 6, 2, 8, 1]
buble_sort(nums2)
print(nums2)


nums3 = [3, 4, 5, 7, 9, 6, 2, 8, 1]
insertion_sort(nums3)
print(nums3)