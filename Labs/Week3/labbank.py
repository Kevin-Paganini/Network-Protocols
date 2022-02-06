def n1(x):
    if x == b'\x03\xe8':
        return "Correct"
    return "Incorrect"


def n2(x):
    if x == 14109235489236324:
        return "Correct"
    return "Incorrect"


def n3(x):
    if x == b'2 Faced':
        return "Correct"
    return "Incorrect"


def n4(x):
    if x == b'\x04\x1f':
        return "Correct"
    return "Incorrect"


def n5(x):
    if x == b'\xe8\x03':
        return "Correct"
    return "Incorrect"


def n6(x):
    if x == 100:
        return "Correct"
    return "Incorrect"


def n7(x):
    if x == b'File length: 100':
        return "Correct"
    return "Incorrect"


from random import randint


def n9(my_str):
    pass_all = True
    for i in range(10):
        x = randint(0, 100000)
        if str(x) != my_str(x):
            pass_all = False
    if pass_all:
        return "Correct"
    return "Incorrect"


def n10(my_int):
    pass_all = True
    for i in range(10):
        x = str(randint(0, 100000))
        if int(x) != my_int(x):
            pass_all = False
    if pass_all:
        return "Correct"
    return "Incorrect"