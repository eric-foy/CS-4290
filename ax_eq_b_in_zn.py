import sys
import gcd
import invert

def findSolutions(a, b, n):
    d = gcd.gcd(a, n)
    if (b % d != 0):
        print("no solutions")
        return None
    else:
        # expect a/d, b/d, and n/d to be integers
        if (a/d != int(a/d)):
            print("a/d not an integer")
            return None
        elif (b/d != int(b/d)):
            print("b/d not an integer")
            return None
        elif (n/d != int(n/d)):
            print("n/d not an integer")
            return None
        elif (gcd.gcd(a/d, n/d) != 1):
            print("gcd(a/d, n/d) != 1)")
            return None
        else:
            if (invert.invert(a/d, n/d) != -1):
                x = int(b/d) * invert.invert(int(a/d), int(n/d))
                x = x % int(n/d)
                o = []
                for i in range(0, d):
                    o += [x + i*int(n/d)]
                return o
            else:
                return None
            

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    n = int(sys.argv[3])
    print(findSolutions(a, b, n))
