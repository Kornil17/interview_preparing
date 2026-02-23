# Реализуйте функцию has_triplet_with_zero_sum(), которая принимает один аргумент:
# nums – список целых чисел
# Функция должна возвращать значение True, если в списке nums присутствует тройка элементов, сумма которых равна нулю. В противном случае функция должна вернуть значение False.


def has_triplet_with_zero_sum(nums):
    n = len(nums)
    nums.sort()

    for cur in range(n - 2):
        left = cur + 1
        right = n - 1

        while left < right:
            current_sum = nums[cur] + nums[left] + nums[right]

            if current_sum == 0:
                return True

            elif current_sum < 0:
                left += 1

            else:
                right -= 1

    return False



print(has_triplet_with_zero_sum([1, 2, -3, 4, -2]))    # 1 + 2 - 3 = 0
print(has_triplet_with_zero_sum([1, 2, 3, 4, 5]))
print(has_triplet_with_zero_sum([0, 0, 0, 0]))         # 0 + 0 + 0 = 0
print(has_triplet_with_zero_sum([1]))
print(has_triplet_with_zero_sum([79, 6, 17, -28, 36, -43, 31, -95, 74, 30]))
print(has_triplet_with_zero_sum([1, -1]))
print(has_triplet_with_zero_sum([-6, -4, 1, 7, 8]))
print(has_triplet_with_zero_sum([-3, -2, 4, 2, 1]))