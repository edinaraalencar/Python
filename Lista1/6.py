print("""6 - Suponha que o preço de capa de um livro seja 24.95. mas as livrarias recebem 
um desconto de 40%. O transporte custa 3.00 para o primeiro exemplar e 75 centavos para 
cada exemplar adicional. Qual é o custo total de atacado para 60 copias?\n""")

def atacado(copias):
    taxa_transporte = 3 #Taxa fixa do primeiro livro
    livro_atacado = 24.95 - (24.95 * (40/100)) #Preço do livro subtraído do desconto para o atacado
    preco_total = copias * livro_atacado #Multiplicado o valor do livro já com o desconto pelo numero de copias
    frete = ((copias - 1) * 0.75) + taxa_transporte #Copias - 1, porque o valor de 0.75 só é cobrado a partir do 2 livro
    return preco_total + frete   

copias = int (input("Quantas copias você deseja comprar? "))
print(f'{atacado(copias):.2f}')