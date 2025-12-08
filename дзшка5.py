# задание 7
num = [45, 12, 89, 3, 67]
try:
    sort = sorted(num)
    print("Исходный список:", num)
    print("Отсортированный список:", sort)
except TypeError:
    print("Ошибка в списке есть что то кроме чисел !")
    print("Проверьте список:", num)