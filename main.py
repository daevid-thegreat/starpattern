def pattern1():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
    print("\n")


def pattern2():
    for i in range(6, 0, -1):
        for j in range(1, i - 1):
            print("*", end=" ")
        print()


def pattern3():
    for i in range(6, 0, -1):
        for j in range(6 - i):
            print("", end=" ")
        for j in range(0, i - 1):
            print("*", end=" ")
        print()

def pattern4():
    for i in range(6, 0, -1):
        for j in range(0, i - 1):
            print("", end=" ")
        for j in range(7, i + 1, -1):
            print("*", end=" ")
        print()

def pattern5():
    for i in range(6, 0, -1):
        for j in range(0, i - 1):
            print("", end=" ")
        for j in range(7, i + 1, -1):
            print("*", end=" ")
        print()
    for i in range(6, 0, -1):
        for j in range(6 - i):
            print("", end=" ")
        for j in range(0, i - 1):
            print("*", end=" ")
        print()


pattern1()
pattern2()
pattern3()
pattern4()
pattern5()
