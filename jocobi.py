def jocobi(a, b):
    if a > b:
        a = a % b

    if a == 1:
        return 1

    if a == 0:
        return 0

    if (a % 2 == 0):
        return jocobi(int(a / 2), b) * int((-1)**((b**2 - 1)/8))
    else:
        return int((-1)**(((a-1)/2)*((b-1)/2))) * jocobi(b, a)


if __name__ == "__main__":
    print(jocobi(51, 133))
    print(jocobi(31, 51))
    print(jocobi(2, 75))
    print(jocobi(19, 101))
    print(jocobi(54, 101))
