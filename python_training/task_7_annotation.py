a: int = 5
b: str = 'строка'
c: list = [1, 2]


def indent(s: str = '', width: int = 0) -> str:
    return ' ' * (max(0, width - len(s))) + s


print(indent('123', 123))


def dlina_stroki(s: str = '') -> int:
    return len(s)


print(dlina_stroki('dgsfgbs'))


def max_list(list1: list, list2: list) -> int:
    return max(len(list1), len(list2))


print(max_list([2, 3, 4], [1, 2, 3, 4]))
