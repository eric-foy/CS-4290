import sys
import gcd

def check(n):
    for i in range(1, n):
        if (gcd.gcd(i, n) == 1):
            print(i)

if __name__ == "__main__":
    check(int(sys.argv[1]))
