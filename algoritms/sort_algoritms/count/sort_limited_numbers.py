from collections import Counter


def sort_limited_numbers(nums: list[int]) -> list[int]:
    counts = Counter(nums)

    index = 0
    for num in range(100, -101, -1):
        for _ in range(counts.get(num, 0)):
            nums[index] = num
            index += 1

    return nums

nums = [-15, 10, 1, -8, 24]
sort_limited_numbers(nums)
print(nums)
