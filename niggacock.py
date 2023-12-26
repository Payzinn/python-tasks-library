import copy

# Создаем вложенный список
original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Поверхностное копирование
shallow_copy = original_list.copy()

# Меняем значение в поверхностно скопированном списке
shallow_copy[0][0] = 10

# Печатаем оба списка
print('Исходный список:', original_list)
print('Поверхностно скопированный список:', shallow_copy)

# Глубокое копирование
deep_copy = copy.deepcopy(original_list)

# Меняем значение в глубоко скопированном списке
deep_copy[0][0] = 20

# Печатаем оба списка
print('Исходный список:', original_list)
print('Глубоко скопированный список:', deep_copy)