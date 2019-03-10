def prime(nr):
    if nr == 1:
        return False
    if nr == 2:
        return True
    if nr % 2 == 0:
        return False

    for i in range(2, nr//2 + 1):
        if (nr % i) == 0:
            return False
    return True


def lprime(nr):
    i = nr-1
    while i > 1:
        if prime(i):
            return i
        i -= 1
    return False


# nr = int(input("Give a number:"))
# print(lprime(nr))


def tests():
    assert lprime(0) is False
    assert lprime(1) is False
    assert lprime(2) is False
    assert lprime(7) == 5
    assert lprime(10) == 7
    assert lprime(79) == 73


tests()
