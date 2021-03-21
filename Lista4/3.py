print("""3 - Escreva uma função que receba uma lista com itens repetidos e retorne a 
mesma lista com itens únicos.""")

itens = [int(input("Digite o cod dos itens: ")) for i in range(4)]

def numeros(itens):
    L = []
    for i in itens:
        if i not in L:
            L.append(i)
    print(L)

numeros(itens)

