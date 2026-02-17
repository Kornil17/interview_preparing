# Реализуйте функцию product_in_segments(), которая принимает два аргумента в следующем порядке:
# nums – список положительных целых чисел
# segments – список кортежей, каждый из которых состоит из двух целых чисел
# Функция должна вычислять произведения элементов списка nums на отрезках, перечисленных в списке segments.
# Например, если список segments имеет вид [(1; 3), (7; 8)], то функция должна вычислить следующие произведения:

def product_in_segments(
        nums: list[int],
        segments: list[tuple[int, int]],
) -> list[int]:
    n = len(nums) + 1
    prefix_mul = [1] * n
    result = []

    for i in range(1, n):
        prefix_mul[i] = prefix_mul[i - 1] * nums[i - 1]

    for start, stop in segments:
        result.append(prefix_mul[stop + 1] // prefix_mul[start])

    return result

print(product_in_segments([2, 6, 1, 4, 2], [(0, 2), (1, 4)]))           # 2*6*1 = 12; 6*1*4*2 = 48
print(product_in_segments([1, 1, 5, 3, 2], [(0, 4), (3, 4)]))           # 1*1*5*3*2 = 30; 3*2 = 6
print(product_in_segments([1], [(0, 0)]))
print(product_in_segments([1, 3, 2, 4], [(0, 1), (0, 3)]))              # 1*3 = 3; 1*3*2*4 = 24
print(product_in_segments([1, 1, 1, 1, 1], [(0, 1), (1, 2), (2, 3)]))   # 1*1 = 1; 1*1 = 1; 1*1 = 1
print(product_in_segments([1, 2, 3, 4, 5], [(1, 1), (2, 2), (3, 3)]))
