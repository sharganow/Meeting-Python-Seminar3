# 1.
# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
while True:
    try:
        len_list, dimention_value = input('Введите размер списка и диапазон значений элементов списка '
                                          'через пробел: ').split()
        len_list = int(len_list)
        if len_list >= 2:
            dimention_value = abs(int(dimention_value))
            if dimention_value == 0:
                print('Диапазон значений списка должен быть отличным от нуля')
            else:
                break
        else:
            print('Размер списка должен быть минимум равен двум (число положительное)')
    except:
        print('Введено должно быть два положительные значения')

list_rand = []
for _ in range(len_list):
    list_rand.append(random.randint(-dimention_value, dimention_value))
list_odd = list_rand[1::2]

print(f'У списка {list_rand} на нечетных позициях \nстоят элементы ', end='')
print(*list_odd, sep=' и ', end='')
print(f', а их сумма равна {sum(list_rand[1::2])}')

