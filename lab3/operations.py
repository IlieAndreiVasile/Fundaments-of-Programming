import math


def create_complex(a, b):
    return (a, b)


def set_real(c, a):
    c[0] = a


def set_immag(c, b):
    c[1] = b


def get_real(c):
    return c[0]


def get_immag(c):
    return c[1]


def modulo(z):
    """
    returns the modulus of a complex number
    input: z - the complex number
    output: the modulus
    """
    result = math.sqrt(z[0] * z[0] + z[1] * z[1])
    return result


def add(l, x):
    """
    adds an element into a list
    input: l - the list
           x - the element
    output: l - the list after the modification
    """
    l.append(x)


def insert(l, pos, x):
    """
    inserts an element into a list
    input: l - the list
           pos - the position
           x - the element
    output: l - the list after the modification
    """
    l.insert(pos, x)
    return l


def remove(l, pos):
    """
    removes an element from a list
    input: l - the list
           pos - the position
    output: l - the list after the modification
    """
    l.pop(pos)
    return l


def remove_sublist(l, s, e):
    """
    removes a sublist from a list
    input: l - the list
           s - the starting position
           e - the ending position
    output: l - the list after the modification
    """
    if s < 0 or e < 0 or s > len(l) or e > len(l) or s > e:
        print("Invalid positions!")
    else:
        for i in range(e - s + 1):
            l.pop(s)
        return l


def replace(l, x, y):
    """
    replaces all occurrences of an element from a list with another one
    input: l - the list
           x - the old element
           y - the new element
    output: l - the list after the modification
    """
    for i in range(0, len(l)):
        if l[i] == x:
            l[i] = y
    return l


def print_list(l):
    """
    prints a list
    input: l - the list
    """
    print(l)


def print_real(l, s, e):
    """
    prints the real elements of a list of complex numbers from a starting position to an ending one
    input: l - the list
           s - the starting position
           e - the ending position
    """
    if s < 0 or e < 0 or s > len(l) or e > len(l) or s > e:
        print("Invalid positions!")
    else:
        res = []
        for i in range(s + 1, e):
            if l[i] == 0:
                res.append(l[i])
        print(res)


def print_modulo(l, o, v):
    """
    prints the elements of a list of complex numbers that have the modulus < | = | > than a value
    input: l - the list
           o - the logical operator
           v - the value
    """
    res = []
    if o == '<':
        for i in range(0, len(l)):
            if modulo(l[i]) < v:
                res.append(l[i])
    elif o == '=':
        for i in range(0, len(l)):
            if modulo(l[i]) == v:
                res.append(l[i])
    elif o == '>':
        for i in range(0, len(l)):
            if modulo(l[i]) > v:
                res.append(l[i])
    print(res)


def sum(l, s, e):
    """
    returns the sum of elements from a list from a starting position to an ending one
    input: l - the list
           s - the starting position
           e - the ending position
    output: the sum
    """
    if s < 0 or e < 0 or s > len(l) or e > len(l) or s > e:
        print("Invalid positions!")
    else:

        s1 = 0
        s2 = 0
        for i in range(s + 1, e):
            s1 += l[i][0]
            s2 += l[i][1]
        sum = (s1, s2)
        return sum


def product(l, s, e):
    """
    returns the product of elements from a list from a starting position to an ending one
    input: l - the list
           s - the starting position
           e - the ending position
    output: the product
    """
    if s < 0 or e < 0 or s > len(l) or e > len(l) or s > e:
        print("Invalid positions!")
    else:
        p1 = 0
        p2 = 0
        for i in range(s + 1, e):
            p1 += l[i][0]
            p2 += l[i][1]
        p = (p1, p2)
        return p


def filter_real(l):
    """
    filters the real elements of a list of complex numbers
    input: l - the list
    output: l - the list after the modification
    """
    k = len(l)
    i = 0
    while i < k:
        if l[i][1] != 0:
            l.pop(i)
            k -= 1
        else:
            i += 1
    return l


def filter_modulo(l, o, v):
    """
    filters the elements of a list of complex numbers that have the modulus < | = | > than a value
    input: l - the list
           o - the logical operator
           v - the value
    output: l - the list after the modification
    """
    if o == '<':
        i = 0
        k = len(l)
        while i < k:
            if modulo(l[i]) >= v:
                l.pop(i)
                k -= 1
            else:
                i = i + 1
    elif o == '=':
        i = 0
        k = len(l)
        while i < k:
            if modulo(l[i]) != v:
                l.pop(i)
                k -= 1
            else:
                i += 1
    elif o == '>':
        i = 0
        k = len(l)
        while i < k:
            if modulo(l[i]) <= v:
                l.pop(i)
                k -= 1
            else:
                i = i + 1
    return l
