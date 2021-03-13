
print("""1 - Converta as seguintes expressões matemáticas para que possam ser calculadas
usando Python: \n""")

print("a) 10 + 20 x 30")
print("b) 4² / 3")
print("c) (9⁴ + 2) x 6 -1")
print("d) (9⁴ + 2)⁴ + ( 10 / 1)\n")
print("Respostas: \n")


def função(a, b, c):
    print (f'a) {a + b * c}')

função(10, 20, 30)


def função (a, b):
    print (f'b) {(a ** 2) / b}')

função(4, 3)


def função (a, b, c, d):
    print (f'c) {((a ** 4) + b) * (c - d)}')

função(9, 2, 6, 1)


def função (a, b, c, d):
    print (f'd) {(((9 ** 4) + 2) ** 4) + (10 / 1)}')

função(9, 2, 10, 1)