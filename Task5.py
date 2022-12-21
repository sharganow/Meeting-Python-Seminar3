# 5.
# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


def get_bec_num():
    while True:
        try:
            dec_number = int(input('Задайте целое десятичное число: '))
            dec_number = abs(dec_number)
            break
        except:
            print('Введите одно число, используя цифровые символы')
    return dec_number


def make_negafibonacci(indx):
    nega = []
    fibonacci = []
    for i in range(indx + 1):
        match i:
            case 0:
                continue
            case 1:
                nega.append(1)
                fibonacci.append(1)
            case 2:
                nega.append(-1)
                fibonacci.append(1)
            case _:
                nega.append(nega[i - 3] - nega[i - 2])
                fibonacci.append(fibonacci[i - 2] + fibonacci[i - 3])
    else:
        if indx == 0:
            return []
    return nega[::-1] + [0] + fibonacci


indx = get_bec_num()
negafibonacci = make_negafibonacci(indx)
print(f'---\nДля размерности k={indx} ряд Негафибоначи выглядит так:\n'
      f'{negafibonacci}\n---')
