# Номера лотерейных билетов представляют собой последовательности из 8 цифр:
# 00000000, 00000001, 00000002, …, 99999997, 99999998, 99999999
# Билет считается счастливым, если сумма первых четырех цифр в его номере равна сумме четырех последних цифр.
# Реализуйте функцию happy_tickets(), которая принимает один аргумент:
# n – целое число (0≤n≤36)
# Функция должна определять, сколько всего существует счастливых лотерейных билетов, сумма первых четырех цифр в номере которых равна n, и возвращать полученный результат.


from collections import defaultdict


from collections import defaultdict


def happy_tickets(n):
    sum_freq1 = defaultdict(int)
    sum_freq2 = defaultdict(int)

    for a in range(10):
        for b in range(10):
            sum_freq1[a + b] += 1

    for c in range(10):
        for d in range(10):
            sum_freq2[n - c - d] += 1

    counter = 0
    for key in sum_freq1:
        counter += sum_freq1[key] * sum_freq2[key]

    return counter ** 2


print(happy_tickets(1))        # 00010001, 00010010, 00010100, ...
print(happy_tickets(2))        # 00020002, 10012000, 20000110, ...
print(happy_tickets(3))        # 03000003, 20012100, 10020300, ...
print(happy_tickets(5))        # 01041220, 23012300, 50001112, ...
print(happy_tickets(10))       # 12341234, 27011090, 03070406, ...
print(happy_tickets(15))       # 17255019, 55502283, 13565406, ...


