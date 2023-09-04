def task1() -> None:
    v1: int = 23
    v2: float = 312.4
    v3: str = 'строка'
    v4: list = [5, 7, 8, 9]
    v5: bool = True
    print(type(v1), ' ', type(v2), ' ', type(v3), ' ', type(v4), ' ', type(v5), ' ')
    return


task1()


def task2() -> None:
    a = [1, 2, 3, 5, 8, 13, 21]
    print('a[0:3] = ', a[0:3])
    return


task2()


def task3(x: float) -> float:
    return x*x


print('квадрат числа 1.1 = ', task3(1.1))


def task4(test_list: list) -> list:
    test_list.append('gdsgdsgsd')
    return test_list


ab = [1, 2]
print(task4(ab))


def task5(test_list2: list) -> int:
    res = 0
    for elem in test_list2:
        res = res + elem
    return res


print(task5([1, 2, 3, 4]))
