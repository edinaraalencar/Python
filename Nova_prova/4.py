'''
4 - Escreva uma função que faça a verificação de existência de um item em uma
lista. A função deve retornar o tamanho da lista caso o item não exista ou o próprio
item caso ele exista.
'''

cod = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]

num =int(input("Digite um codigo: \n"))


def item_lista(cod, num):
    if num in cod:
        print (num)
    else:
        print(len(cod))
        
    

item_lista(cod, num)