# Реализуйте функцию count_pythagorean_triplets(), которая принимает три аргумента в следующем порядке:
# nums1 – список целых чисел
# nums2 – список целых чисел
# nums3 – список целых чисел
# Функция должна возвращать количество способов, которыми можно выбрать число а из списка nums1, число b из списка nums2 и число с из списка nums3 так, чтобы для выбранных чисел выполнялось равенство a2 + b2 = c2


from collections import defaultdict


def count_pythagorean_triplets(
        nums1: list[int],
        nums2: list[int],
        nums3: list[int],
) -> int:
    ab_sums = defaultdict(int)
    for a in nums1:
        for b in nums2:
            ab_sums[a ** 2 + b ** 2] += 1

    counter = 0
    for c in nums3:
        c_squared = c ** 2
        counter += ab_sums[c_squared]

    return counter


print(count_pythagorean_triplets([2, 3, 4], [4, 3], [3, 5]))       # (3, 4, 5), (4, 3, 5)
print(count_pythagorean_triplets([-1, 0, 5], [-2, 1, 3], [4]))
print(count_pythagorean_triplets([-3], [-4], [-5]))                # (-3, -4, -5)
print(count_pythagorean_triplets([1, 1], [2, 2], [3, 3]))
print(count_pythagorean_triplets([0], [0], [0]))                   # (0, 0, 0)
print(count_pythagorean_triplets([3, 1, 2], [0, 0, 0], [2, 0, 3]))
