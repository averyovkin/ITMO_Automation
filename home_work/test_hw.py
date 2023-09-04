def test_hw1():
    assert ('home', 'work') == ('home', 'work')


def test_hw2():
    assert not 'QA' == 'QC'


def test_hw3():
    x = (1, 1, 2, 3, 5)
    y = (2, 3, 5)
    assert not x == y
