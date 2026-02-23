# Храбрый пожарный выносит людей из горящего здания.
# За один заход он может вынести одного или двух человек, суммарный вес которых не превышает limit.
# Пожарный знает, сколько весит каждый находящийся в здании человек: эти значения перечислены в списке weights.
# Теперь пожарный хочет знать, как быстро он сможет вынести всех людей из горящего здания.
# Реализуйте функцию count_rescue_attempts(), которая принимает два аргумента в следующем порядке:
# weights – список положительных целых чисел
# limit – целое число
# Функция должна определять, какое минимальное количество заходов понадобится пожарному, чтобы вынести из горящего здания всех людей, и возвращать полученный результат.
# Примечание. Гарантируется, что ни один элемент списка weights не превышает значения limit.


def count_rescue_attempts(weights: list[int], limit: int) -> int:
    weights.sort()
    n = len(weights)
    left, right = 0, n - 1
    count = 0

    while left <= right:
        if left < right and weights[left] + weights[right] <= limit:
            count += 1
            left += 1
            right -= 1
        else:
            count += 1
            right -= 1

    return count


print(count_rescue_attempts([1, 2], 3))          # заходы: (1, 2)
print(count_rescue_attempts([2, 3, 2, 1], 4))    # заходы: (2, 2), (1, 3)
print(count_rescue_attempts([3, 1, 2, 3], 4))    # заходы: (1, 3), (2), (3)
print(count_rescue_attempts([3, 2, 2, 3], 3))    # заходы: (3), (2), (2), (3)
print(count_rescue_attempts([50], 50))           # заходы: (50)
print(count_rescue_attempts([5, 5, 5, 5], 15))   # заход: (5, 5), (5, 5)
