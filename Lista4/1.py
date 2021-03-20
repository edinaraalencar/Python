print("""1 - Faça uma função que receba duas listas e que gere uma terceira com os 
elementos das duas primeiras.\n""")

pares = [x for x in range(0, 11, 2)]
impares = [x for x in range (1, 10, 2)]

def teste(impares, pares):
    list = pares + impares
    print(list)

print("Nova Lista criada: ")
teste(impares, pares)