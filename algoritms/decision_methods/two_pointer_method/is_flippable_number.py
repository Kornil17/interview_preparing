# Число
# 609
# 609 обладает очень интересным свойством: если его перевернуть вверх ногами (представьте, что вы поворачиваете экран на
# 180
# 180 градусов), то снова получится число
# 609
# 609. Помимо
# 609
# 609, существуют и другие числа, обладающие аналогичным свойством.
# Реализуйте функцию is_flippable_number(), которая принимает один аргумент:
# num – положительное целое число, состоящее только из цифр 0,6,9 и представленное в виде строки
# Функция должна возвращать значение True, если после переворота числа num вверх ногами снова получается число num, и False в противном случае.


def is_flippable_number(num: str) -> bool:
    flip_map = {'0': '0', '6': '9', '9': '6'}

    left, right = 0, len(num) - 1
    while left <= right:
        if flip_map[num[left]] != num[right]:
            return False
        left += 1
        right -= 1

    return True


print(is_flippable_number('609'))
print(is_flippable_number('96096'))
print(is_flippable_number('6090609'))
print(is_flippable_number('6900'))
print(is_flippable_number('6'))
print(is_flippable_number('69'))
