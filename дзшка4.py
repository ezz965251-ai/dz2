#задание 3
my_lst = [15, 3, 89, 42, 7, 56, 23, 91, 12, 38]
if len(my_lst) == 0:
    print("Список пустой! нет чисел для поиска максимума.")
else:
    max_num = my_lst[0]
    print(f"Начинаем поиск с первого числа: {max_num}")
    step = 1
    for num2 in my_lst:
        print(f" {step} проверяем число {num2}")
        if num2 > max_num:
            print(f"  найдено число больше  {num2} > {max_num}")
            max_num = num2
            print(f"  новое максимальное число: {max_num}")
        else:
            print(f"  {num2} максимальное число {max_num} ")

        step = step + 1
        print()
    print(f"поиск закончен ")
    print(f"Максимальное число в списке : {max_num}")
print("проверка с пустым списком:")
non_lst = []
if len(non_lst) == 0:
    print("ошибка список пустой нету максимального числа ")
else:
    max_num1 = non_lst[0]
    for number in non_lst:
        if number > max_num1:
            max_num1 = number
    print(f"максимальное число : {max_num1}")