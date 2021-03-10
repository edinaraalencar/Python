'''
15 - Imprimia as seguintes sequências utilizando `for` e o método `range()`:
 - ímpares de 1000 a 43
 - pares de 2 a 100
 '''

print("\nImpares\n")
for i in range(43, 1000):
    if(i % 2) != 0:
        print (i)

print("\n\nPar\n")
for i in range(2, 102):
    if(i % 2) == 0:
        print (i)