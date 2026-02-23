# Будем называть строку почти палиндромом, если она становится палиндромом после удаления из нее одного конкретного символа.
# Например, строка abca – почти палиндром, потому что если убрать из нее символ c, то получится палиндром: aba.
# Реализуйте функцию is_almost_palindrome(), которая принимает один аргумент:
# s – строка из строчных английских букв
# Функция должна возвращать значение True, если строка s является почти палиндромом, и False в противном случае.
# Примечание. Палиндром – это текст, фраза или число, которое читается одинаково, как справа налево, так и слева направо.


def is_almost_palindrome(s: str) -> bool:
    def is_palindrome_range(left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
        left += 1
        right -= 1
    return True

print(is_almost_palindrome('abca'))       # aba
print(is_almost_palindrome('abcddba'))    # abddba
print(is_almost_palindrome('spyder'))
print(is_almost_palindrome('a'))
print(is_almost_palindrome('aaaa'))       # aaa
print(is_almost_palindrome('ab'))         # a, b
print(is_almost_palindrome('abcdbadba'))
print(is_almost_palindrome('dlldl'))