import matrix_minors as mm
import matrix_determinant as md
import matrix_smprint as mp

def adjoint(A, Zn):
    x = []
    for i in range(0, len(A)):
        y = []
        for j in range(0, len(A[i])):
            d = md.determinant(mm.minors(A, j+1, i+1), Zn)
            z = (-1)**(i+j) * d
            z %= Zn
            y += [z]
        x += [y]
    return x

if __name__ == "__main__":
    A = [[3, 3, 6], [8, 4, 10], [1, 4, 6]]
    print(mp.smprint(adjoint(A, 11)))
