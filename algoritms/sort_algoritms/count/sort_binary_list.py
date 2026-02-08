def sort_binary_list(nums: list[int]) -> list[int]:
    extra_nums = [0, 0]

    for num in nums:
        extra_nums[num] += 1

    index = 0
    for num in range(2):
        for _ in range(extra_nums[num]):
            nums[index] = num
            index += 1

    return nums


binary_list = [0, 1, 1, 0, 1]
sort_binary_list(binary_list)
print(binary_list)
