# Початкові дані: список із 10 int та 10 str
mixed_list = [5, "apple", 12, "banana", 7, "cherry", 18, "grape", 3, "lemon",
              10, "orange", 21, "peach", 4, "kiwi", 8, "mango", 1, "pear"]

# Розділення списку на числа та рядки
int_list = [item for item in mixed_list if isinstance(item, int)]
str_list = [item for item in mixed_list if isinstance(item, str)]

# Сортування
sorted_ints = sorted(int_list)  # по зростанню
sorted_strs = sorted(str_list)  # за алфавітом

# Об'єднаний список: числа + рядки
sorted_combined_list = sorted_ints + sorted_strs

# Список чисел, кратних 2
even_numbers = [num for num in sorted_ints if num % 2 == 0]

# Список рядків у CAPS
caps_strings = [s.upper() for s in sorted_strs]

# Почвтковий список
print("Початковий список:" )
print(mixed_list)

# Вивід результатів
print("Відсортований список (int → str):")
print(sorted_combined_list)

print("Числа, кратні 2:")
print(even_numbers)

print("Рядки у ВЕРХНЬОМУ РЕЄСТРІ:")
print(caps_strings)