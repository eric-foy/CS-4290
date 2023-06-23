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


def one(a, b):
    return divmul(a, b, 10)

def two(a, b):
    return divmul(a, b, 100)

def three(a, b):
    return divmul(a, b, 1000)

if __name__ == "__main__":
    print(one(23, 23))
    print(two(23, 23))
    print(two(23, 123))
