from operations import *
from commands import *


def tests():
    l = []

    c = create_complex(2, 3)
    add(l, c)
    assert l[0] == (2, 3)
    c = create_complex(4, 0)
    add(l, c)
    assert l[1] == (4, 0)
    c = create_complex(3, -2)
    add(l, c)
    c = create_complex(7, 1)
    add(l, c)
    c = create_complex(2, -3)
    add(l, c)
    c = create_complex(10, 9)
    add(l, c)
    c = create_complex(7, 1)
    add(l, c)

    insert(l, 0, 5)
    assert l[0] == 5
    insert(l, 0, (-1, -7))
    assert l[0] == (-1, -7)

    remove(l, 0)
    assert l[0] == 5
    assert l[1] == (2, 3)

    remove_sublist(l, 1, 3)
    assert l[0] == 5
    assert l[1] == (7, 1)

    replace(l, (7, 1), 2)
    assert l[1] == 2
    assert l[4] == 2

    # s = sum(l, 0, 3)
    # print(s)
    # #assert s == (4, -3)
    #
    # p = product(l, 1, 4)
    # print(p)
    # #assert p == (47, -12)

    # filter_real(l)
    # print(l)
    # #assert l == [5, 2, 2]

    # c = create_complex(3, -2)
    # add(l, c)
    # c = create_complex(7, 1)
    # add(l, c)
    # c = create_complex(2, -3)
    # add(l, c)
    # c = create_complex(10, 9)
    # add(l, c)
    # c = create_complex(7, 1)
    # add(l, c)
    # filter_modulo(l, "<", 5)
    # assert l == ([2, 2, (3, -2), (2, -3)])


# def test_add():
#     l = []
#     add(l, 2-3j)
#     assert l[0] == 2-3j
#     add(l, 4)
#     assert l[1] == 4
#
#
# def test_insert():
#     l = []
#     insert(l, 0, 5)
#     assert l[0] == 5
#     insert(l, 0, -1-7j)
#     assert l[0] == -1-7j
#
#
# def test_remove():
#     l = [(3-2j), (7+1j)]
#     remove(l, 0)
#     assert l[0] == 7+1j
#
#
# def test_remove_sublist():
#     l = [(3-2j), (7+1j), (2-3j), 5, (10+9j)]
#     remove_sublist(l, 1, 3)
#     assert l[1] == 10+9j
#
#
# def test_replace():
#     l = [(3-2j), (7+1j), (2-3j), 5, (10+9j), (7+1j)]
#     replace(l, 7+1j, 2)
#     assert l[1] == 2
#     assert l[5] == 2
#
#
# def test_sum():
#     l = [(3-2j), (7+1j), (2-3j), 5, (10+9j), (7+1j)]
#     s = sum(l, 0, 4)
#     assert s == 14-2j
#
#
# def test_product():
#     l = [(3-2j), (7+1j), (2-3j), 5, (10+9j), (7+1j)]
#     p = product(l, 1, 6)
#     assert p == 1705-185j
#
#
# def test_filter_real():
#     l = [(3-2j), (7+1j), (2-3j), 5, (10+9j), (7+1j)]
#     filter_real(l)
#     assert l == [5]
#
#
# def test_filter_modulo():
#     l = [(3-2j), (7+1j), (2-3j), 5, (10+9j), (7+1j)]
#     filter_modulo(l, "<", 5)
#     assert l == ([(3-2j), (2-3j)])


# l = [(2+3j), (3-0j), (-5-7j), (8+0j), (9-4j), (-1-7j)]
# filter_command(l, "filter modulo > 3")
# print(l)


# l = [(2+3j), (3-0j), (-5-7j), (8+0j), (9-4j), (-1-7j)]
# filter_command(l, "filter real")
# print(l)


# l = [(2+3j), (3-0j), (-5-7j), (8+0j), (9-4j), (-1-7j)]
# s = sum_command(l, "sum 2 to 5")
# print(s)


# l = [(2+3j), (3-0j), (-5-7j), (8+0j), (9-4j), (-1-7j)]
# p = product_command(l, "product 2 to 5")
# print(p)

# l = [(2+3j), (3-0j), (-5-7j), (8+0j), (9-4j), (-1-7j)]
# list_command(l, "list modulo > 4")


# l = [(2+3j), (3-0j), (-5-7j), (8+0j), (9-4j), (-1-7j)]
# list_command(l, "list modulo = 3")


# l = [(2+3j), (3-0j), (-5-7j), (8+0j), (9-4j), (-1-7j)]
# list_command(l, "list real 1 to 4")


# l = [(2+3j), (3-4j), (-5-7j), (8+3j), (9-4j), (-1-7j), (10+0j), (2+3j)]
# replace_command(l, "replace 2+3j with 10")
# print(l)


# l = [(2+3j), (3-4j), (-5-7j), (8+3j), (9-4j), (-1-7j)]
# remove_command(l, "remove 1 to 3")
# print(l)


# l = [(2+3j), (3-4j), (-5-7j)]
# insert_command(l, "insert 1+1j at 1")
# print(l)


# command = input("input: ")
# command = command.split(" ")
# print(command[2])
