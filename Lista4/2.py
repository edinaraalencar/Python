print("""2 - Faça o mesmo que se pede na questão anterior, mas a terceira lista não 
pode ter itens repetidos.\n""")

pares = [x for x in range(0, 11, 2)] 
impares = [x for x in range (1, 15, 3)] 

def teste(impares, pares):
    numeros = pares + impares
    numeros = set(numeros)
    print(numeros)

print("Nova Lista criada: ")
teste(impares, pares)
