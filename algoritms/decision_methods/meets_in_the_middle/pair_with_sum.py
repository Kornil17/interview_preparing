# Реализуйте функцию pair_with_sum(), которая принимает два аргумента в следующем порядке:
# nums – список различных целых чисел
# k – целое число
# Функция должна находить в списке nums пару чисел, сумма которых равна k. Возвращаемое значение функции – отсортированный по неубыванию кортеж из двух найденных чисел.
# Примечание. Гарантируется, что искомая пара чисел в списке nums всегда есть, причем она единственная.


def pair_with_sum(nums: list[int], k: int):
    seen = set()
    for num in nums:
        x = k - num
        if x in seen:
            return min(num, x), max(num, x)
        seen.add(num)



print(pair_with_sum([1, 16, 9, 10, 4], 26))
print(pair_with_sum([4, 5, -1, 10, -5], 0))
print(pair_with_sum([1, 3], 4))
print(pair_with_sum([0, -4, 5, 10], 1))
print(pair_with_sum([1, 2, 3, 4, 5], 9))
print(pair_with_sum([6, 8, -10, -3], -2))
