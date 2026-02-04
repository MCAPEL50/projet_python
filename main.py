print("Hello")


def table(n: int):
    for k in range(1, 11):
        print(n, "* ", k, " = ", n * k)


def punition_table(m: int):
    for n in range(1, m + 1):
        print("table de", n)
        table(n)
        print("*" * 12)


punition_table(0)


def somme(n: int):
    s = 0
    for z in range(1, n + 1):
        s = s + z
    print(s)


somme(0)


def somme_carre(n: int):
    s = 0
    for z in range(1, n + 1):
        s = s + z**2
    print(s)


somme_carre(0)


def somme_puissance(n: int, m: int):
    s: int = 0
    for z in range(1, n + 1):
        s += z**m
    print(s)


somme_puissance(1, 2)


def somme_binaire(n: int):
    s = 1
    for z in range(1, n + 1):
        s = s + 0.5**z
    print(s)


somme_binaire(0)

for c in range(5):
    print(
        " " * ((11 - 1 - 2 * c) // 2)
        + "M" * (1 + 2 * c)
        + " " * ((11 - 1 - 2 * c) // 2)
    )
print("-" * 11)
for c in range(4, -1, -1):
    print(
        " " * ((11 - 1 - 2 * c) // 2)
        + "W" * (1 + 2 * c)
        + " " * ((11 - 1 - 2 * c) // 2)
    )
