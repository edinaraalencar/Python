print("""5 - Escreva uma função que receba como argumento a quantidade de Km percorridos 
por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro
foi alugado. A função deve retornar o preço a pagar, sabendo que o carro custa R$ 60,00 
por dia e R$ 0,15 por km rodado.\n""")

def aluguel(quant, dias):
    fixo = dias * 60
    distancia = quant * 0.15
    preco_total = fixo + distancia
    return preco_total

dias = int (input("Digite a quantidade de dias que o carro foi alugado: "))
quant = int (input("Digite a quantidade de km percorridos: "))
print(f'Preço total a pagar: R${aluguel(quant, dias):.2f}')
