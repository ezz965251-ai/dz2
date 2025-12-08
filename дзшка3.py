# Задание 1
my_lst1 = [20, 20, 30, 40, 50]
sum_res = 0
has_error = False
for element in my_lst1:
    if type(element) == int or type(element) == float:
        sum_res = sum_res + element
    else:
        print(f"Ошибка! Элемент '{element}' не является числом")
        has_error = True
        break
if not has_error:
    print(f"Сумма всех чисел: {sum_res}")