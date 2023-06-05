import matrix_minors as mm
# negate if m[i][j] is even?

def determinant(A, Zn):
    # should be square
    n = len(A)
    for i in A:
        if len(i) != n:
            print("not square")
            return -1

    if n == 1:
        return A[0][0]

    x = 0
    for i in range(0, n):
        x += A[0][i] * (-1)**i * determinant(mm.minors(A, 1, i+1), Zn)
        x %= Zn
    return x

def det(A, Zn):
    return determinant(A, Zn)

if __name__ == "__main__":
    # 2 by 2 should be 10-2
    A = [[1, 2], [3, 4]]
    print(determinant(A, 10))
    # 3 by 3 should be 1000-306
    A = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
    print(determinant(A, 1000))
    # 4 by 4 should be 1000-270
    A = [[6, 1, 1, 5], [4, -2, 5, 1], [2, 8, 7, 7], [3, 4, 1, 6]]
    print(determinant(A, 1000))
