'''
7- Utilizando List Comprehension crie uma lista de listas
'''

pares = [x for x in range(0, 11, 2)] 
impares = [x for x in range (1, 15, 3)] 

numeros = list(pares + impares) #Concatenando listas

print("Nova Lista criada: ")
print(numeros)
print(type(numeros))