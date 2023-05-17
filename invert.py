import sys
import invertable

def egcd(a, b, s0, s1, t0, t1):
    if (a < b):
        c = a
        a = b
        b = c

    q = int(a / b)
    r = a % b

    s2 = s0 - q*s1
    t2 = t0 - q*t1

    if (r == 0):
        return t1

    return egcd(b, r, s1, s2, t1, t2)

def AinverseZ(a, z, n):
    return (a*z % n == 1)

def invert(a, n):
    if (invertable.isInvertable(a, n)):
        a = a % n
        z = egcd(a, n, 1, 0, 0, 1)
        z = z % n
        if (AinverseZ):
            return z
        else:
            print("a not inverse to z.")
            return -1
    else:
        print("not invertable")
        return -1

if __name__ == "__main__":
    print(invert(int(sys.argv[1]), int(sys.argv[2])))
