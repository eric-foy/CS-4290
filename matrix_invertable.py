import sys
import matrix_multiply as mm
import matrix_identity as mi

# see if m and n are inverts of each other
def invertable(m, n):
    a = mm.multiply(m, n)
    b = mm.multiply(n, m)
    i = mi.identity(len(m))
    if (a == b and a == i):
        return True
    return False

if __name__ == "__main__":
    a = [[4, -2, 3], [8, -3, 5], [7, -2, 4]]
    b = [[-2, 2, -1], [3, -5, 4], [5, -6, 4]]
    print(invertable(a, b))
    c = [[1, 1], [0, 1]]
    d = [[1, -1], [0, 1]]
    print(invertable(c, d))
