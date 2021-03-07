'''
Construa uma função que receba a categoria 
e o preço de um produto. A categoria varia de 1 a 5,
cada categoria tem um desconto especifico,
você deve aplicar esse desconto no preço do produto
e retornar o valor com desconto.
'''
cat = None
preco = None

def compra(cat, preco):
    preco = float (input ("Digite o valor do produto: ")) #Recebe o valor do produto do usuario
    if (preco < 50):
        print("Parabéns!\nVocê recebeu 20% de desconto !")
        preco = preco - preco*(20/100)
        print(f'O valor que você vai pagar é de R${preco}.')
        cat = 5 #O desconto está ligado ao valor do produto, 
                #sendo assim a categoria é passada se satisfizer o parametro

    elif (50 <= preco < 100):
        print("Parabéns!\nVocê recebeu 15% de desconto !")
        preco = preco - preco*(15/100)
        print(f'O valor que você vai pagar é de R${preco}.')
        cat = 4

    elif (100 <= preco < 150):
        print("Parabéns!\nVocê recebeu 10% de desconto !")
        preco = preco - preco*(10/100)
        print(f'O valor que você vai pagar é de R${preco}.')
        cat = 3

    elif (150 <= preco < 200):
        print("Parabéns!\nVocê recebeu 7% de desconto !")
        preco = preco - preco*(7/100)
        print(f'O valor que você vai pagar é de R${preco}.')
        cat = 2

    else: #Quanto maior o preço do produto menor é o desconto
        print("Parabéns!\nVocê recebeu 5% de desconto !")
        preco = preco - preco*(5/100)
        print(f'O valor que você vai pagar é de R${preco}.')
        cat = 1

    return cat, preco

#Função Principal
print("\n Estamos em Promoção !\n")
compra(cat, preco)