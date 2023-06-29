import sys

def gcd(a, b):
    if (a < b):
        c = a
        a = b
        b = c

    if (b == 0):
        return a

    q = int(a / b)
    r = a % b

    if (r == 0):
        return b

    return gcd(b, r)

if __name__ == "__main__":
    print(gcd(int(sys.argv[1]), int(sys.argv[2])))
