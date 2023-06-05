import matrix_multiply as mm
import matrix_identity as mi
import matrix_determinant as md
import invertable as iZn

# see if m and n are inverts of each other
def invertable(m, n):
    a = mm.multiply(m, n)
    b = mm.multiply(n, m)
    i = mi.identity(len(m))
    if (a == b and a == i):
        return True
    return False

# A is invertable iff det(A) is invertable in Zn
def invertableb(A, Zn):
    d = md.determinant(A, Zn)
    print(d)
    if (iZn.isInvertable(d, Zn)):
        return True
    return False

if __name__ == "__main__":
    a = [[4, -2, 3], [8, -3, 5], [7, -2, 4]]
    b = [[-2, 2, -1], [3, -5, 4], [5, -6, 4]]
    print(invertable(a, b))
    c = [[1, 1], [0, 1]]
    d = [[1, -1], [0, 1]]
    print(invertable(c, d))

    e = [[1, 1], [0, 1]]
    print(invertableb(e, 5))
    f = [[0, 1], [1, 0]]
    print(invertableb(f, 5))

