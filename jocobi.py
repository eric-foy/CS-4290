import sys

def jocobi(a, b):
    if a > b:
        a = a % b

    if a == 1:
        return 1

    if a == 0:
        return 0

    if (a % 2 == 0):
        return jocobi(int(a / 2), b) * int((-1)**((b**2 - 1)/8))
    else:
        return int((-1)**(((a-1)/2)*((b-1)/2))) * jocobi(b, a)

def legendre(a, p):
    e = (p - 1)/2
    o = a**e
    o %= p
    return o

def isSquare(a, Zn):
    l = legendre(a, Zn)
    if (l != 1):
        print("legendre not equal to 1, maybe ", Zn, " not odd prime")
    return l

def squares(Zn, check=True):
    o = set()
    for i in range(1, Zn):
        x = i**2
        x %= Zn
        o.add(x)
    if check:
        for i in o:
            isSquare(i, Zn)
    return o

def roots(a, Zn):
    o = []
    for i in range(1, Zn):
        x = i**2
        x %= Zn
        if x == a:
            o += [i]

    return o

def test():
    print(jocobi(51, 133))
    print(jocobi(31, 51))
    print(jocobi(2, 75))
    print(jocobi(19, 101))
    print(jocobi(54, 101))

    print(squares(7))
    print(roots(4, 7))

if __name__ == "__main__":
    print(jocobi(int(sys.argv[1]), int(sys.argv[2])))
