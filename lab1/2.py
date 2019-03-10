def palindrome(nr):
    temp = nr
    rev = 0
    while nr > 0:
        dig = nr % 10
        rev = rev * 10 + dig
        nr = nr//10
    if temp == rev:
        return True
    else:
        return False


# nr = int(input("Give a number:"))
# palindrome(nr)


def tests():
    assert palindrome(77577) is True
    assert palindrome(1) is True
    assert palindrome(4) is True
    assert palindrome(79) is False
    assert palindrome(7979) is False


tests()
