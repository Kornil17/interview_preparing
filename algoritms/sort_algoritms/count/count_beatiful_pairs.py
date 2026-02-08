from collections import Counter


def count_beautiful_pairs(nums: list[int]) -> int:
    counts = Counter(nums)
    return round(sum(v // 2 for v in counts.values()))


print(count_beautiful_pairs([1, 4, 5, 4, 1, 1, 0]))    # пары: (1; 1), (4; 4)
print(count_beautiful_pairs([4, 4, 4, 4, 4, 4, 4]))    # пары: (4; 4), (4; 4), (4; 4)
print(count_beautiful_pairs([1, 2, 3, 4, 5, 6, 7]))    # красивых пар нет
print(count_beautiful_pairs([0, 0]))                   # пара: (0; 0)
print(count_beautiful_pairs([1, 1, 1]))                # пара: (1; 1)
print(count_beautiful_pairs([0, 9, 9, 0]))             # пары: (0; 0), (9; 9)
