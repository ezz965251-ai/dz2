def min_index(simple_list):
    min_a = 0
    for i in range(len(simple_list)):
        if simple_list[i] < simple_list[min_a]:
            min_a = i
    return min_a
numbers = [4, 2, 7, 1, 9, 3]
min_a = min_index(numbers)
print(f"Список: {numbers}")
print(f"Минимальное число: {numbers[min_a]}")
print(f"Оно находится на позиции: {min_a}")