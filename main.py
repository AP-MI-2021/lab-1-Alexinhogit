'''
Returneaza true daca n este prim si false daca nu.
'''


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n // 2):
        if n % i == 0:
            return False

    return True


'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
    n = 1
    for element in lst:
        n *= element

    return n


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(x, y):
    if y == 0:
        return x
    elif x == 0:
        return y
    return get_cmmdc_v1(y, x % y)


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    if x > y:
        return get_cmmdc_v2(x - y, y)
    return get_cmmdc_v2(x, y - x)


def main():
    n = int(input("Introduceti numar:"))
    print(is_prime(n))

    lst = []
    nr = int(input("Cate numere se vor inmulti? "))
    print("Introduceti cele ", nr, " numere.")
    for i in range(nr):
        x = int(input())
        lst.append(x)

    print(get_product(lst))

    x = int(input("Introduceti primul numar pentru calcularea CMMDC:"))
    y = int(input("Introduceti al doilea numar pentru calcularea CMMDC:"))
    print(get_cmmdc_v1(x, y))


if __name__ == '__main__':
    main()
