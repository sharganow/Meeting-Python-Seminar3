# 4.
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


def get_bec_num():
    while True:
        try:
            dec_number = int(input('Задайте целое десятичное число: '))
            dec_number = abs(dec_number)
            break
        except:
            print('Введите одно число, используя цифровые символы')
    return dec_number


def tranc_dec_bin(decim):
    while True:
        try:
            decim = int(decim)
            break
        except:
            print('Преобразование не возможно')

    bin_value = []
    while decim > 0:
        if decim % 2 > 0:
            bin_value.append('1')
        else:
            bin_value.append('0')
        decim //= 2
    if len(bin_value) == 0:
        bin_value.append('0')
    return bin_value


dec_val = get_bec_num()
bin_val = tranc_dec_bin(dec_val)[::-1]
print(f'---\nВы ввели: {dec_val} и ему соответствует\n'
      f'бинарное представление: ', end='')
print(*bin_val, sep='')
print(f'---')
