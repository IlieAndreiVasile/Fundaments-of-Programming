from commands import *
from tests import *


def main():
    l = []
    c = create_complex(2, 3)
    add(l, c)
    c = create_complex(5, -6)
    add(l, c)
    c = create_complex(-3, -9)
    add(l, c)
    c = create_complex(7, 0)
    add(l, c)
    c = create_complex(1, 10)
    add(l, c)
    c = create_complex(15, 0)
    add(l, c)
    c = create_complex(6, 4)
    add(l, c)
    c = create_complex(0, 9)
    add(l, c)
    c = create_complex(12, 0)
    add(l, c)

    undo = []
    while True:
        cmd = read_command()
        if cmd[0] == "add":
            undo = l[:]
            add_command(l, cmd)
        elif cmd[0] == "insert":
            undo = l[:]
            insert_command(l, cmd)
        elif cmd[0] == "remove":
            undo = l[:]
            remove_command(l, cmd)
        elif cmd[0] == "replace":
            undo = l[:]
            replace_command(l, cmd)
        elif cmd[0] == "list":
            list_command(l, cmd)
        elif cmd[0] == "sum":
            sum_command(l, cmd)
        elif cmd[0] == "product":
            product_command(l, cmd)
        elif cmd[0] == "filter":
            undo = l[:]
            filter_command(l, cmd)
        elif cmd[0] == "undo":
            l = undo[:]
        elif cmd[0] == "help":
            help_command()
        elif cmd[0] == "exit":
            break
        else:
            print("Invalid command! Type help to see the valid commands :)")


tests()
main()
