def sort_numbers_string(input_string):
    numbers_str = input_string.split()
    numbers = []
    for num_str in numbers_str:
        numbers.append(int(num_str))
    numbers.sort()
    result = ""
    for num in numbers:
        result += str(num) + " "
    return result.strip()
test_string = "5 2 8 1 9 3"
result = sort_numbers_string(test_string)
print(f"Исходная строка: '{test_string}'")
print(f"Результат: '{result}'")