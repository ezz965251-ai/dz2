def find_max_recursive(lst):
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]

    first = lst[0]
    rest_of_list = lst[1:]
    max_in_rest = find_max_recursive(rest_of_list)

    if first > max_in_rest:
        return first
    else:
        return max_in_rest
numbers = [3, 7, 2, 9, 1, 4]
print(f"Максимальный элемент в {numbers}: {find_max_recursive(numbers)}")
negative_numbers = [-5, -2, -10, -1]
print(f"Максимальный элемент в {negative_numbers}: {find_max_recursive(negative_numbers)}")
empty_list = []
print(f"Максимальный элемент в пустом списке: {find_max_recursive(empty_list)}")
