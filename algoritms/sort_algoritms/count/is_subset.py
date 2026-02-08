from collections import Counter


def is_subset(s1: str, s2: str) -> bool:
    return Counter(s1) <= Counter(s2)


print(is_subset('ace', 'abcde'))
print(is_subset('ace', 'abcd'))
print(is_subset('ace', 'aabbccddee'))
print(is_subset('a', 'a'))
print(is_subset('aaa', 'aa'))
