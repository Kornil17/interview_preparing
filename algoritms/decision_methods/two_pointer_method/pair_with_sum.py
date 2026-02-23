def pair_with_sum(nums, k):
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == k:
            return (nums[left], nums[right])
        elif current_sum < k:
            left += 1
        else:
            right -= 1

    return -1

print(pair_with_sum(
    [0, 1, 3, 4, 6, 8],
    10
))