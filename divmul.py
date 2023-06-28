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
    p = 0
    c = a
    for i in binb:
        if i == "1":
            o = o * c
            o = o % n
        p += 1
        c = c**2
        c = c % n
    return o

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    n = int(sys.argv[3])
    print(divmul(a, b, n))
