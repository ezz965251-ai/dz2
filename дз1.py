test_numbers = [2, -3, 5, -8, 10, -1, 4, 7, -6]
print("Тестовый список:", test_numbers)

evens = []
odds = []
negs = []
pos = []

for number in test_numbers:
    if number % 2 == 0:
        evens.append(number)

    if number % 2 != 0:
        odds.append(number)

    if number < 0:
        negs.append(number)

    if number > 0:
        pos.append(number)

print("Результаты:")
print("Четные:", evens)
print("Нечетные:", odds)
print("Отрицательные:", negs)
print("Положительные:", pos)