import sys

def gcd(a, b, s0, s1, t0, t1):
    if (a < b):
        c = a
        a = b
        b = c

    q = int(a / b)
    r = a % b

    s2 = s0 - q*s1
    t2 = t0 - q*t1

    if (r == 0):
        print("gcd =", b)
        print("x =", s1)
        print("y =", t1)
        return

    gcd(b, r, s1, s2, t1, t2)

if __name__ == "__main__":
    gcd(int(sys.argv[1]), int(sys.argv[2]), 1, 0, 0, 1)
