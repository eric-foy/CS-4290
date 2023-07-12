from divmul import power

def isPrimitive(a, Zn):
    Z = set(range(1, Zn))
    x = set()
    y = power(a, 1, Zn)
    x.add(y)
    c = 2
    while y != 1:
        y = power(a, c, Zn)
        x.add(y)
        c += 1

    if x == Z:
        return True
    else:
        return False


if __name__ == "__main__":
    print(isPrimitive(1, 3))
    print(isPrimitive(2, 3))

    print()
    print(isPrimitive(1, 7))
    print(isPrimitive(2, 7))
    print(isPrimitive(3, 7))
    print(isPrimitive(6, 7))

    print()
    print(isPrimitive(2, 19))
    print(isPrimitive(3, 19))
    print(isPrimitive(4, 19))
