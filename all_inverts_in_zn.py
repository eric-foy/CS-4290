import sys
import gcd

def check(n):
    c = 0
    for i in range(1, n):
        if (gcd.gcd(i, n) == 1):
            c += 1
            print(i)
    print("Number in Zn:", c)

if __name__ == "__main__":
    check(int(sys.argv[1]))
