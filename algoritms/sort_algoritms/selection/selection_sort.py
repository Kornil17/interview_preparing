# Реализуйте функцию selection_sort(), которая принимает один аргумент:
# nums – список целых чисел
# Функция должна выполнять сортировку списка nums по невозрастанию путем его изменения.


def selection_sort(nums: list[int]) -> list[int]:
    """Сортировка выбором."""
    for target_idx in range(len(nums)):
        max_idx = target_idx
        for current_idx in range(target_idx, len(nums)):
            if nums[current_idx] > nums[max_idx]:
                max_idx = current_idx

        if nums[target_idx] < nums[max_idx]:
            nums[target_idx], nums[max_idx] = nums[max_idx], nums[target_idx]

    return nums
