# Будем называть одной операцией такое действие, в результате которого один символ строки заменяется на любой другой. Например, одна операция относительно строки beegeek может заменять последний символ строки на символ b:
# beegeek -> beegeeb
# Реализуйте функцию smallest_palindrome(), которая принимает один аргумент:
# s – строка из строчных английских букв
# Функция должна составлять из строки s палиндром за минимальное количество операций и возвращать полученный результат в виде новой строки. Если за минимальное количество операций из строки s можно составить несколько палиндромов, то функция должна вернуть тот, что меньше в лексикографическом сравнении.


def smallest_palindrome(s):
    letters = list(s)
    left = 0
    right = len(letters) - 1

    while left < right:
        if letters[left] > letters[right]:
            letters[left] = letters[right]

        elif letters[left] < letters[right]:
            letters[right] = letters[left]

        left += 1
        right -= 1

    return ''.join(letters)


print(smallest_palindrome('beegeek'))
print(smallest_palindrome('pygen'))

