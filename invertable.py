import sys
import gcd

def isInvertable(a, n):
    if (gcd.gcd(a, n) == 1):
        return True
    else:
        return False

if __name__ == "__main__":
    print(isInvertable(int(sys.argv[1]), int(sys.argv[2])))
