import sys

def divpart(b):
    o = ""
    pows = []
    p = 0
    while b != 1:
        o += str(b % 2)
        if b % 2 == 1:
            pows += [2**p]
        b = int(b / 2)
        p += 1
    o += str(b % 2)
    if b % 2 == 1:
        pows += [2**p]
    return o


def divmul(a, b, n):
    # a**b
    if (b == 0):
        return 1

    binb = divpart(b)
    o = 1
    c = a
    for i in binb:
        if i == "1":
            o = o * c
            o = o % n
        c = c**2
        c = c % n
    return o

def check(a, b, n):
    # a**b
    c = a
    for i in range(1, b):
        c = c * a
        c = c % n
    return c

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    n = int(sys.argv[3])
    print(divmul(a, b, n))
    print(check(a, b, n))
