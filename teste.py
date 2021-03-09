def consulta_desconto (preço):
    if preço <= 20:
        desconto = preço - preço * (20/100)
        categoria = 5
        print (f'Categoria: {categoria}\nParabéns! Seu desconto é de 20%')
        print (f'De R${preço} por apenas R${desconto}')
    elif 20 < preço <= 50: #Alterei o > pelo <
        desconto = preço - preço * (15/100)
        categoria = 4
        print (f'Categoria: {categoria}\nParabéns! Seu desconto é de 15%')
        print (f'De R${preço} por apenas R${desconto}')
    elif 50 < preço <= 100:
        desconto = preço - preço * (10/100)
        categoria = 3
        print (f'Categoria: {categoria}\nParabéns! Seu desconto é de 10%')
        print (f'De R${preço} por apenas R${desconto}')
    elif 100 < preço <= 500:
        desconto = preço - preço * (7/100)
        categoria = 2
        print (f'Categoria: {categoria}\nParabéns! Seu desconto é de 7%')
        print (f'De R${preço} por apenas R${desconto}')
    else:
        desconto = preço - preço * (5/100)
        categoria = 1
        print (f'Categoria: {categoria}\nParabéns! Seu desconto é de 5%')
        print (f'De R${preço} por apenas R${desconto}')


#Programa Principal
print ('-'*50)
print ('        SISTEMA PARA CONSULTA DE DESCONTO              ')
print ('-'*50)
print ('\n')
print ('O Desconto do Produto será de acordo com a Categoria')
preço = float (input('Digite o preço do produto: '))
consulta_desconto(preço)  