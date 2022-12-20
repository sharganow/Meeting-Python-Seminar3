# 2.
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

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

list_Pair_Mul = []
for i in range(len(list_rand)):
    if i <= (len(list_rand) - i - 1):
        list_Pair_Mul.append(list_rand[i] * list_rand[len(list_rand) - i - 1])
    else:
        break

print(f'У списка {list_rand} произведение пар, \nравно отстоящих элементов, '
      f'образуют новый список {list_Pair_Mul}', end='')