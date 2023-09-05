num_float = -3.4

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

num = 5

permit_print = True


if num > 0 and permit_print:
    print('num - положительное  число')
elif not permit_print:
    print('Печать запрещена')


tmp = int(input('Введите число: '))

if tmp in range(1, 5):
    print('Бакалавр')
elif tmp in range(5, 7):
    print('Магистр')
elif tmp in (7, 8, 9):
    print('Аспирант')
else:
    print('Некорректное число')


x = 452
if x > 100 or x < -100:
    print('-')
else:
    print('+')
