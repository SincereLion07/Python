# Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается
# у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия
# указанному в условии ввода данных.
#
# Далее программа работает по следующему алгоритму:
# Преобразование введённой последовательности в список
# Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска. Реализуйте его также отдельной функцией


def step(x):
    return sorted(x)


def binary_search(array, element):
    try:
        element = int(element)
    except ValueError:
        return "Введенное значение не является числом"
    if element not in array:
        return "Число выходит за пределы заданного списка"
    middle = len(array) // 2  # Индекс центрального элемента
    if array[middle] == element:
        try:
            return array[middle - 1], array[middle + 1]
        except IndexError:
            return array[middle - 1], array[middle]
    elif element > array[middle]:
        return binary_search(array[middle:], element)
    else:
        return binary_search(array[:middle + 1], element)


user_numbers = int(input("Введите число от 0 до 1000: "))
numbers = list(range(1001))
print(binary_search(numbers, user_numbers))
