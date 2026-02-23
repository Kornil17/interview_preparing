def sort_binary_list(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        while left < len(nums) and nums[left] == 0:
            left += 1
        while right >= 0 and nums[right] == 1:
            right -= 1

        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

l = [0, 1, 1, 0, 0, 1]
sort_binary_list(l)
print(l)