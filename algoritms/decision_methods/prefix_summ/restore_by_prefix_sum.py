# У Тимура был список nums, состоящий из целых чисел. На его основе он создал список префиксных сумм p следующим образом:
# Теперь у Тимура остался только список префиксных сумм p. С его помощью он хочет восстановить исходный список nums.
# Реализуйте функцию restore_by_prefix_sum(), которая принимает один аргумент: p
# Функция должна восстанавливать список nums, который был у Тимура, и возвращать его.


def restore_by_prefix_sum(p: list[int]) -> list[int]:
    nums = []
    for i in range(1, len(p)):
        nums.append(p[i] - p[i - 1])

    return nums


print(restore_by_prefix_sum([0, 10, 14, 20, 21, 29]))
print(restore_by_prefix_sum([0, 1, 3, 6, 10, 15]))
print(restore_by_prefix_sum([0, 5]))
print(restore_by_prefix_sum([0, -1, 1, -3, -5]))
print(restore_by_prefix_sum([0, 1, 2, 3, 4]))
print(restore_by_prefix_sum([0, 0, 0, 0, 0]))
