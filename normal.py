# Задача-1:

# Дан список, заполненный произвольными целыми числами, получите новый список,

# элементами которого будут квадратные корни элементов исходного списка,

# но только если результаты извлечения корня не имеют десятичной части и

# если такой корень вообще можно извлечь

# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

number = [2, -5, 8, 9, -25, 25, 4]
new_number = []
for i in number:
   if i > 0 and (math.sqrt(i)) % 1 == 0:
        new_number.append(int(math.sqrt(i)))
print(new_number)



# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.

# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.

# Склонением пренебречь (2000 года, 2010 года)





# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами

# в диапазоне от -100 до 100. В списке должно быть n - элементов.

# Подсказка:

# для получения случайного числа используйте функцию randint() модуля random





# Задача-4: Дан список, заполненный произвольными целыми числами.

# Получите новый список, элементами которого будут:

# а) неповторяющиеся элементы исходного списка:

# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]

# б) элементы исходного списка, которые не имеют повторений:

# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
