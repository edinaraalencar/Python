print("""2 - Faça o mesmo que se pede na questão anterior, mas a terceira lista não 
pode ter itens repetidos.\n""")

pares = [x for x in range(0, 11, 2)] #Usando o list comprehension para gerar lista pares
impares = [x for x in range (1, 15, 3)] 

def teste(impares, pares):
    numeros = impares + pares
    print(numeros)
    L = [] #Cria e inicializa uma lista vazia
    for i in numeros: #Percorre a nova lista
        if i not in L: #Se o numero não estiver ainda na lista 
            L.append(i) #Ele adiciona no fim dela com o metodo append
    L.sort() #Metodo sort para ordenar a lista
    print(L)

print("Nova Lista criada: ")
teste(impares, pares)

