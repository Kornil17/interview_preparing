# Реализуйте функцию count_pairs_with_sum(), которая принимает два аргумента в следующем порядке:
# nums – отсортированный по неубыванию список целых чисел
# k – целое число
# Функция должна определять, какое максимальное количество пар можно составить из элементов списка nums так, чтобы сумма элементов в каждой паре была равна k.
# Каждый элемент списка nums может использоваться только один раз.
# Возвращаемое значение функции – полученное количество пар.


def count_pairs_with_sum(nums: list[int], k: int) -> int:
    count = 0
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == k:
            count += 1
            left += 1
            right -= 1

        if total < k:
            left += 1
        elif total > k:
            right -= 1

    return count

print(count_pairs_with_sum([1, 1, 2, 2, 3], 4))     # пары: (1, 3), (2, 2)
print(count_pairs_with_sum([1, 2, 3, 4, 5, 6], 7))  # пары: (1, 6), (2, 5), (3, 4)
print(count_pairs_with_sum([1, 1, 2, 2, 3], 8))     # подходящих пар нет
print(count_pairs_with_sum([1], 1))                 # подходящих пар нет
print(count_pairs_with_sum([1, 1, 1, 1, 1], 2))     # пары: (1, 1), (1, 1)
print(count_pairs_with_sum([-1, -1, 1, 1], 0))      # пары: (-1, 1), (-1, 1)
