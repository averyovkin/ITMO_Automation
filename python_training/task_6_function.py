def add(x, y):
    return x + y


print(add(1, 2))

#   вызываем функцию с другими аргументами
print(add('I a', 'm tester'))


def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1, 1, 1))
print(arg(2, 2))


#   порядок аргументов
def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d


print(range_arg('1', '2', '3', '4'))
print(range_arg('1', '2', d='3', c='4'))


def first_elem(a=(1, 2, 3, 4)):
    return a[0]


print(first_elem())


def square_circle(rad, pi=3.14159):
    return pi*rad*rad


print(square_circle(5))
