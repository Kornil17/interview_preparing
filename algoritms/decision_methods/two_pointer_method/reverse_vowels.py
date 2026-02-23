# Реализуйте функцию reverse_vowels(), которая принимает один аргумент:
# s – строка из строчных английских букв
# Функция должна обрабатывать строку s таким образом, чтобы все ее гласные буквы были расположены в обратном порядке, а все согласные остались на своих исходных позициях без изменений. Возвращаемое значение функции – полученная в итоге строка.
# Примечание. Список строчных английских гласных букв:
# ['a', 'e', 'i', 'o', 'u']


def reverse_vowels(s: str) -> str:
    s = list(s)
    vowels = 'aeiou'
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        elif s[left] not in vowels:
            left += 1
        elif s[right] not in vowels:
            right -= 1

    return "".join(s)


print(reverse_vowels('programmer'))
print(reverse_vowels('crocodile'))
print(reverse_vowels('a'))
print(reverse_vowels('beegeek'))
print(reverse_vowels('aeiou'))
print(reverse_vowels('bcdfg'))
