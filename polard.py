import sys
import gcd
import divmul

def factor(a, B, Zn):
    b = a
    for i in range(1, B+1):
        b = divmul.divmul(b, i, Zn)
    d = gcd.gcd(b - 1, Zn)
    return d


if __name__ == "__main__":
    a = int(sys.argv[1])
    B = int(sys.argv[2])
    Zn = int(sys.argv[3])
    print(factor(a, B, Zn))
