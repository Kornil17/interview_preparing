# Реализуйте функцию min_valid_index(), которая принимает три аргумента в следующем порядке:
# nums – список, содержащий только целые числа в диапазоне
# k – целое число
# m – целое число
# Функция должна находить минимально возможное число i такое, что:
# nums[i] + nums[i + 1] + nums[i + 2] + ... + nums[i + k] = m
# Возвращаемое значение функции – найденное число i. Если числа i не существует, функция должна вернуть значение -1.


def min_valid_index(nums, k, m):
    n = len(nums)
    p = [0] * (n + 1)

    for i in range(1, n + 1):
        p[i] = p[i - 1] + nums[i - 1]

    for i in range(n - k):
        if p[i + k + 1] - p[i] == m:
            return i

    return -1


print(min_valid_index([7, 2, 3, 1, 4, 1, 1], 2, 6))    # [2, 3, 1]
print(min_valid_index([7, 3, 1, 4, 1, 1], 1, 5))       # [1, 4]
print(min_valid_index([7, 3, 1, 4, 1, 1], 3, 20))
print(min_valid_index([1, 1, 3, 2, 5, 9, -2], 1, 7))   # [2, 5]
print(min_valid_index([-2, -1, 0, 1, 3], 4, 1))        # [-2, -1, 0, 1, 3]
print(min_valid_index([1, 1, 1, 1, 1], 3, 4))          # [1, 1, 1, 1]
