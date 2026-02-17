# Реализуйте функцию zeros_in_segments(), которая принимает два аргумента в следующем порядке:
# nums – список целых чисел
# segments – список кортежей, каждый из которых состоит из двух целых чисел
# Функция должна определять количество нулей на отрезках списка nums, перечисленных в списке segments. Например, если список segments имеет вид [(1; 3), (7; 8)], то функция должна определить количество нулей среди следующих элементов:
# Полученные результаты функция должна вернуть в виде списка, первым элементом которого является количество нулей на первом отрезке списка nums, вторым – на втором, третьим – на третьем и так далее.
# Примечание. Гарантируется, что в каждом кортеже из списка segments первый элемент не больше второго.


def zeros_in_segments(
        nums: list[int],
        segments: list[tuple[int, int]],
) -> list[int]:
    n = len(nums)
    prefix_zeros = [0] * (n + 1)
    for i in range(1, n + 1):
        if nums[i - 1] == 0:
            prefix_zeros[i] = prefix_zeros[i - 1] + 1
        else:
            prefix_zeros[i] = prefix_zeros[i - 1]

    result = []
    for start, stop in segments:
        result.append(prefix_zeros[stop + 1] - prefix_zeros[start])
    return result


print(zeros_in_segments([2, 0, 6, 1, 0, 4, 2, 0], [(0, 7), (2, 3), (4, 7)]))
print(zeros_in_segments([1, 2, 3, 4, 5, 6, 7, 8], [(0, 7), (2, 3), (4, 7)]))
print(zeros_in_segments([0], [(0, 0)]))
print(zeros_in_segments([0, 0, 0, 0, 0], [(0, 4)]))
print(zeros_in_segments([-1, 0, 2, -4, 0], [(0, 1), (1, 2), (0, 4)]))
print(zeros_in_segments([0, 0, 0, 0, 1], [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]))
