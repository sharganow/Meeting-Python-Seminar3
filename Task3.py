# 3.
# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def make_list(round_val):
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
            print('Введено должно быть два положительных целых значения')

    import random

    list_rand = []
    for _ in range(len_list):
        list_rand.append(round((random.random() * random.randint(0, dimention_value)), round_val))
        if list_rand[_] == int(list_rand[_]):
            list_rand[_] = int(list_rand[_])

    return list_rand


def calc_diff_fract(list_f, round_val):

    for i in list_f:
        if i != int(i):
            max_fract = min_fract = round(i - int(i), round_val)
            break
    else:
        return 0

    for i in range(len(list_f)):
        if list_f[i] != int(list_f[i]):
            i_fract = round((list_f[i] - int(list_f[i])), round_val)
            if i_fract >= max_fract:
                max_fract = i_fract
            elif i_fract <= min_fract:
                min_fract = i_fract
    diff_fract = round(max_fract - min_fract, round_val)

    if diff_fract == int(diff_fract):
        return int(diff_fract)
    else:
        return diff_fract


list_r = make_list(2)

print(f'---\nУ списка {list_r} \n'
      f'разница между максимальным и минимальным значениями дробной части элементов, отличной от 0\n'
      f'равна {calc_diff_fract(list_r, 3)}\n---')
