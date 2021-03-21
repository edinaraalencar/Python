print("""1 - Faça uma função que receba duas listas e que gere uma terceira com os 
elementos das duas primeiras.\n""")

pares = [x for x in range(0, 11, 2)] #Usando o list comprehension para gerar a lista pares
impares = [x for x in range (1, 15, 3)] 

def teste(impares, pares):
    numeros = pares + impares #Concatenando listas
    print(numeros)

print("Nova Lista criada: ")
teste(impares, pares)