import random
numbers = [3, -5, 8, -2, 10, -7, 4, -1, 6]
print("Список чисел:", numbers)

sum_neg = 0
for n in numbers:
    if n < 0:
        sum_neg = sum_neg + n
print("Сумма отрицательных:", sum_neg)

sum_even = 0
for n in numbers:
    if n % 2 == 0:
        sum_even = sum_even + n
print("Сумма четных:", sum_even)

sum_odd = 0
for n in numbers:
    if n % 2 == 1 or n % 2 == -1:
        sum_odd = sum_odd + n
print("Сумма нечетных:", sum_odd)

product = 1
for i in range(len(numbers)):
    if i % 3 == 0:
        product = product * numbers[i]
print("Произведение элементов с индексами кратными 3:", product)