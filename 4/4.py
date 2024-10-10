# 7. Реализовать модуль, содержащий функцию, которая вставляет в массив элемент с заданным индексом и заданным значением. Лишний элемент должен пропасть.

def insert_element(array, index, element):
    return array[:index] + [element] + array[index + 1:]

# Проверка
array = [1, 2, 3, 4, 5]
index = 2
element = 6
print(insert_element(array, index, element))