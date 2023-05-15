import sys
import gcd

def isInvertable(a, n):
    if (gcd.gcd(a, n) == 1):
        return True
    else:
        return False
