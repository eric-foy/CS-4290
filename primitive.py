from divmul import power

def isPrimitive(a, Zn, disp=False):
    Z = set(range(1, Zn))
    x = set()
    y = power(a, 1, Zn)
    if disp:
        print(f"{a} = {y}")
    x.add(y)
    c = 2
    while y != 1:
        y = power(a, c, Zn)
        if disp:
            print(f"{a}^{c} = {y}")
        x.add(y)
        c += 1

    if disp:
        print(f"Z={Z}")
        print(f"x={x}")

    if x == Z:
        return True
    else:
        return False


if __name__ == "__main__":
    print(isPrimitive(1, 3, True))
    print(isPrimitive(2, 3, True))

    print()
    print(isPrimitive(1, 7, True))
    print(isPrimitive(2, 7, True))
    print(isPrimitive(3, 7, True))
    print(isPrimitive(6, 7, True))

    print()
    print(isPrimitive(2, 19, True))
    print(isPrimitive(3, 19, True))
    print(isPrimitive(4, 19, True))
