import math


def print_menu():
    s = "\navailable commands:\n"
    s += "\t1 - print the list\n"
    s += "\t2 - add an element\n"
    s += "\t3 - longest sequence of complex numbers with strictly increasing real part\n"
    s += "\t4 - longest sequence of complex numbers with the same modulus\n"
    s += "\t0 - exit\n"
    print(s)


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


def read():
    """
    read a complex number
    input: 2 integers representing real and imaginary part of the number
    output: a complex number
    """
    while True:
        try:
            real = int(input('please enter the real part: '))
            imaginary = int(input('please enter the imaginary part: '))
            z = create_complex(real, imaginary)
            return z
        except:
            print('please input integer numbers')


def add(l, z):
    """
    adds a number into the list
    input: l - the list
           z - the complex number
    output: l - the list after the addition
    """
    l.append(z)


def print_list(l):
    """
    prints the list of complex numbers
    input: l - the list
    """
    print(l)


def seq_real(l):
    """
    return the longest sequence of complex numbers with strictly increasing real part
    input: l - the list
    output: the longest sequence
    """
    i = 0
    start = 0
    max = 0
    m1 = 0
    while i < len(l) - 1:
        if (l[i][0]) < (l[i + 1][0]):
            m1 += 1
        else:
            if m1 > max:
                max = m1
                start = i - m1
            m1 = 0
        i += 1
    if m1 > max:
        max = m1
        start = i - m1
    if max == 0:
        return None
    return l[start:start + max + 1]


def modulo(z):
    """
    returns the modulus of a complex number
    input: z - the complex number
    output: the modulus
    """
    result = math.sqrt(z[0] * z[0] + z[1] * z[1])
    return result


def seq_modulus(l):
    """
    return the longest sequence of complex numbers with the same modulus
    input: l - the list
    output: the longest sequence
    """
    i = 0
    start = 0
    max = 0
    m1 = 0
    while i < len(l) - 1:
        if modulo(l[i]) == modulo(l[i + 1]):
            m1 += 1
        else:
            if m1 > max:
                max = m1
                start = i - m1
            m1 = 0
        i += 1
    if m1 > max:
        max = m1
        start = i - m1
    if max == 0:
        return None
    return l[start:start + max + 1]


def test_add():
    l = []
    z = (5, -3)
    add(l, z)
    assert l[0] == (5, -3)


def test_seq_real():
    l1 = [(2, 3), (-2, -3), (7, -7), (5, 8), (0, 2), (-4, 7), (9, 2), (3, 0), (5, 2), (7, 1), (9, 8)]
    l2 = [(2, 3), (-2, -3), (7, -7), (5, 8), (3, 0), (5, 2), (7, 1), (9, 8), (0, 2), (-4, 7), (9, 2)]
    l3 = [(3, 0), (5, 2), (7, 1), (9, 8), (2, 3), (-2, -3), (7, -7), (5, 8), (0, 2), (-4, 7), (9, 2)]
    assert seq_real(l1) == [(3, 0), (5, 2), (7, 1), (9, 8)]
    assert seq_real(l2) == [(3, 0), (5, 2), (7, 1), (9, 8)]
    assert seq_real(l3) == [(3, 0), (5, 2), (7, 1), (9, 8)]


def test_seq_modulus():
    l1 = [(2, 3), (-2, -3), (7, -7), (5, 8), (0, 2), (4, 7), (-9, 2), (3, 0), (5, 2), (7, 1), (9, 8)]
    l2 = [(7, -7), (5, 8), (0, 2), (2, 3), (-2, -3), (4, 7), (-9, 2), (3, 0), (5, 2), (7, 1), (9, 8)]
    l3 = [(7, -7), (5, 8), (0, 2), (4, 7), (-9, 2), (3, 0), (5, 2), (7, 1), (9, 8), (2, 3), (-2, -3)]
    assert seq_modulus(l1) == [(2, 3), (-2, -3)]
    assert seq_modulus(l2) == [(2, 3), (-2, -3)]
    assert seq_modulus(l3) == [(2, 3), (-2, -3)]


def tests():
    test_add()
    test_seq_real()
    test_seq_modulus()


def run():
    l = [create_complex(2, 3), create_complex(-2, -3), create_complex(4, 7), create_complex(9, 2), create_complex(3, 0), create_complex(5, 2), create_complex(7, 1), create_complex(9, 8), create_complex(7, 7), create_complex(5, 8), create_complex(0, 2)]

    while True:
        print_menu()
        cmd = str(input("please enter the command: "))
        if cmd == "1":
            print_list(l)
        elif cmd == "2":
            c = read()
            add(l, c)
        elif cmd == "3":
            print(seq_real(l))
        elif cmd == "4":
            print(seq_modulus(l))
        elif cmd == "0":
            break
        else:
            print("please enter a valid command")


tests()
run()
