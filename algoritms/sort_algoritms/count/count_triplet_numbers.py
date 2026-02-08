# Реализуйте функцию count_triplet_numbers(), которая принимает один аргумент:
# nums – список, содержащий только целые числа в диапазоне от 1 до 1000 включительно
# Функция должна определять, сколько чисел в списке nums встречается ровно три раза, и возвращать полученный результат.


def count_triplet_numbers(nums: list[int]) -> int:
    counts = [0] * 1000

    for num in nums:
        counts[num - 1] += 1

    triplet_count = 0
    for count in counts:
        if count == 3:
            triplet_count += 1

    return triplet_count


print(count_triplet_numbers([4, 5, 6, 4, 5, 4, 5, 6]))    # числа 4 и 5 встречаются ровно 3 раза
