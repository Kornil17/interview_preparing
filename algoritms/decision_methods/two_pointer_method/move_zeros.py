# Реализуйте функцию move_zeros(), которая принимает один аргумент:
# nums – список целых чисел
# Функция должна изменять список nums таким образом, чтобы все нули были перемещены в конец списка, а порядок остальных элементов относительно друг друга остался прежним.


def move_zeros(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != 0 and nums[j] == 0:
            nums[j], nums[i] = nums[i], nums[j]
        if nums[j] != 0:
            j += 1


nums = [0, 1, 2]
move_zeros(nums)
print(nums)

nums = [0, 2, 0, 0, 1]
move_zeros(nums)
print(nums)

nums = [1, 2, 3]
move_zeros(nums)
print(nums)

nums = [1]
move_zeros(nums)
print(nums)

nums = [1, 1, 1, 1]
move_zeros(nums)
print(nums)

nums = [0, 0, 0]
move_zeros(nums)
print(nums)

nums = [1, 0, 2, 0, 3, 0, 4, 0, 5]
move_zeros(nums)
print(nums)

nums = [3, 2, 4, 0, 3, 2, 2, 5, 1, 4]
move_zeros(nums)
print(nums)