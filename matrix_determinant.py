import matrix_minors as mm
# negate if m[i][j] is even?

def determinant(A):
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
        #print(A[0][i])
        #print((-1)**i)
        #print(determinant(mm.minors(A, 1, i+1)))
        x += A[0][i] * (-1)**i * determinant(mm.minors(A, 1, i+1))
    return x

if __name__ == "__main__":
    # 2 by 2
    A = [[1, 2], [3, 4]]
    print(determinant(A))
    # 3 by 3
    A = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
    print(determinant(A))
