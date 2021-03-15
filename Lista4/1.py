print("""1 - Faça uma função que receba duas listas e que gere uma terceira com os 
elementos das duas primeiras.\n""")

pares = [2, 4, 6, 8, 10]
impares = [1, 3, 5, 7, 9]

def teste(impares, pares):
    list = [impares, pares]
    print(list)

print("Nova Lista criada: ")
teste(impares, pares)