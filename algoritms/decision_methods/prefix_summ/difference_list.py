# Реализуйте функцию difference_list(), которая принимает один аргумент:
# nums – список положительных целых чисел
# Функция должна создавать и возвращать список, на i-й позиции которого находится разница между суммой элементов левее nums[i] и суммой элементов правее nums[i], то есть значение:
# abs(sum(nums[:i]) - sum(nums[i + 1:]))
# Примечание. Длина списка, возвращаемого функцией difference_list(), должна совпадать с длиной списка nums.


def difference_list(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]

    result = []
    for i in range(n):
        result.append(abs(prefix[i] - (prefix[n] - prefix[i + 1])))
    return result




print(difference_list([2, 3, 6, 1, 4]))    # |0 - 14| = 14; |2 - 11| = 9; |5 - 5| = 0;
                                           # |11 - 4| = 7; |12 - 0| = 12
print(difference_list([1, 2, 3, 4, 5]))    # |0 - 14| = 14; |1 - 12| = 11; |3 - 9| = 6;
                                           # |6 - 5| = 1; |10 - 0| = 10
print(difference_list([1]))                # |0 - 0| = 0;
print(difference_list([1, 1, 1, 1, 1]))    # |0 - 4| = 4; |1 - 3| = 2; |2 - 2| = 0;
                                           # |3 - 1| = 2; |4 - 0| = 4
print(difference_list([10, 4, 8, 3]))      # |0 - 15| = 15; |10 - 11| = 1; |14 - 3| = 11; |22 - 0| = 22
print(difference_list([1, 2]))             # |0 - 2| = 2; |1 - 0| = 1
