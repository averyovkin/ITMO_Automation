def max_num(a, b):
    return max(a, b)


print('Максимум двух чисел: ', max_num(12, 24))
print('Максимум двух чисел: ', max_num(-3, -2))


def check(x, y):
    z = x - y
    if abs(z) == 135:
        print('yes')
    else:
        print('no')


check(1, 136)
check(2, 136)


def season(m):
    if m in range(1, 13):
        if m in (1, 2) or m == 12:
            print('Winter')
        elif m in (3, 4, 5):
            print('Spring')
        elif m in (6, 7, 8):
            print('summer')
        else:
            print('Autumn')
    else:
        print('Incorrect number')


season(11)


def check_decimal(u, v, w):
    if u > 10 and v > 10 and w > 10:
        print('Yes')
    else:
        print('No')


check_decimal(6, 7, 10)
check_decimal(11, 13, 112)


def check_posiitve(a, b, c, d, e):
    tmp = (a, b, c, d, e)
    counter = 0
    for i in tmp:
        if i > 0:
            counter = counter + 1
    return counter

# len(list(filtr(lambda x: x>0, a)))
# функция FILTR создает новый список из старого: на входе получает список
# и сравнивает каждый элемент этого списка с выражением

pos = check_posiitve(-5, -19, -5, 7, -2)
print('Число положительных: ', pos)


def days_count():
    years = int(input('Введите количество лет: '))
    months = int(input('Введите количество месяцев '))

    days = (years * 12) + (months * 29)
    print("Количество дней: ", days)


days_count()
