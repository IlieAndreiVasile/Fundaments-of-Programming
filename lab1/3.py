def divsum(nr):
    s = 0
    for i in range(1, nr // 2 + 1):
        if nr % i == 0:
            s += i
    return s


def is_perfect(nr):
    if nr == 0:
        return False
    return divsum(nr) == nr


def lperfect(nr):
    i = nr-1
    while i > 1:
        if is_perfect(i):
            return i
        i -= 1
    return 'does not exist'


# nr = int(input("Give a number:"))
# print(lperfect(nr))


def tests():
    assert lperfect(1) == 'does not exist'
    assert lperfect(0) == 'does not exist'
    assert lperfect(6) == 'does not exist'
    assert lperfect(7) == 6
    assert lperfect(496) == 28
    assert lperfect(497) == 496


tests()
