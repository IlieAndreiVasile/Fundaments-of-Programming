from operations import *


def read_command():
    cmd = input("insert command: ")
    command = cmd.split(" ")
    return command


def add_command(l, cmd):
    if len(cmd) == 3:
        try:
            z = create_complex(int(cmd[1]), int(cmd[2]))
            # z = complex(cmd[1])
            l.append(z)
            return l
        except:
            print('please input a complex number')
    else:
        print("Invalid input! the number was not added")


def insert_command(l, cmd):
    if len(cmd) == 5:
        if cmd[3] != "to":
            print("Invalid input! the number was not inserted")
        else:
            try:
                z = create_complex(int(cmd[1]), int(cmd[2]))
                # z = complex(cmd[1])
                pos = int(cmd[4])
                insert(l, pos, z)
                return l
            except:
                print('please input a complex and an integer number')
    else:
        print("Invalid input! the number was not inserted")


def remove_command(l, cmd):
    if len(cmd) == 2:
        try:
            pos = int(cmd[1])
            remove(l, pos)
            return l
        except:
            print('please input an integer number')
    elif len(cmd) == 4:
        if cmd[2] != "to":
           print("Invalid input! the number was not removed")
        else:
            try:
                pos1 = int(cmd[1])
                pos2 = int(cmd[3])
                remove_sublist(l, pos1, pos2)
                return l
            except:
                print('please input 2 integer numbers')
    else:
        print("Invalid input! the number was not removed")


def replace_command(l, cmd):
    if len(cmd) != 6:
        print("Invalid input! the number was not replaced")
    elif cmd[2] != "with":
        print("Invalid input! the number was not replaced")
    else:
        try:
            z1 = create_complex(int(cmd[1]), int(cmd[2]))
            z2 = create_complex(int(cmd[4]), int(cmd[5]))
            # z1 = complex(cmd[1])
            # z2 = complex(cmd[3])
            replace(l, z1, z2)
            return l
        except:
            print('please input 2 complex numbers')


def list_command(l, cmd):
    if len(cmd) == 1:
        print_list(l)
    elif len(cmd) == 5:
        if cmd[1] != "real" or cmd[3] != "to":
            print("Invalid input!")
        else:
            try:
                pos1 = int(cmd[2])
                pos2 = int(cmd[4])
                print_real(l, pos1, pos2)
            except:
                print('please input 2 integer numbers')
    elif len(cmd) == 4:
        if cmd[1] != "modulo":
            print("Invalid input!")
        else:
            if cmd[2] == "<" or cmd[2] == "=" or cmd[2] == ">":
                try:
                    m = int(cmd[3])
                    print_modulo(l, cmd[2], m)
                except:
                    print('please input an integer number')
            else:
                print("please input a logical operator!")
    else:
        print("Invalid input!")


def sum_command(l, cmd):
    if len(cmd) == 4:
        if cmd[2] != "to":
           print("Invalid input!")
        else:
            try:
                pos1 = int(cmd[1])
                pos2 = int(cmd[3])
                s = sum(l, pos1, pos2)
                print(s)
            except:
                print('please input 2 integer numbers')
    else:
        print("Invalid input!")


def product_command(l, cmd):
    if len(cmd) == 4:
        if cmd[2] != "to":
            print("Invalid input!")
        else:
            try:
                pos1 = int(cmd[1])
                pos2 = int(cmd[3])
                p = product(l, pos1, pos2)
                print(p)
            except:
                print('please input 2 integer numbers')
    else:
        print("Invalid input!")


def filter_command(l, cmd):
    if len(cmd) == 2:
        if cmd[1] != "real":
            print("Invalid input!")
        else:
            k = len(l)
            i = 0
            while i < k:
                if l[i].imag != 0:
                    l.pop(i)
                    k -= 1
                else:
                    i += 1
        return l
    elif len(cmd) == 4:
        if cmd[1] != "modulo":
            print("Invalid input!")
        else:
            if cmd[2] == "<" or cmd[2] == "=" or cmd[2] == ">":
                try:
                    m = int(cmd[3])
                    filter_modulo(l, cmd[2], m)
                    return l
                except:
                    print('please input an integer number')
            else:
                print("please input a logical operator!")
    else:
        print("Invalid input!")


def help_command():
    s = "Valid commands:\n"
    s += '\tadd <number>\n'
    s += '\tinsert <number> at <position>\n'
    s += '\tremove <position>'
    s += '\tremove <start position> to <end position>\n'
    s += '\treplace <old number> with <new number>\n'
    s += '\tlist\n'
    s += '\tlist real <start position> to <end position>\n'
    s += '\tlist modulo [ < | = | > ] <number>\n'
    s += '\tsum <start position> to <end position>\n'
    s += '\tproduct <start position> to <end position>\n'
    s += '\tfilter real\n'
    s += '\tfilter modulo [ < | = | > ] <number>\n'
    s += '\tundo\n'
    s += '\thelp\n'
    s += '\texit\n'
    print(s)
