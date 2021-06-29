'''
- a cada 100 pessoas que visualizam o anúncio 12 clicam nele.
- a cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.
- cada compartilhamento nas redes sociais gera 40 novas visualizações.
- 30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido.
- o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
(1ª pessoa -> compartilha -> 2ª pessoa -> compartilha - > 3ª pessoa -> compartilha -> 4ª pessoa)

'''
# Crie um script em sua linguagem de programação preferida que receba o valor investido 
# em reais e retorne uma projeção aproximada da quantidade máxima de pessoas que 
# visualizarão o mesmo anúncio (considerando o anúncio original + os compartilhamentos)

resto_visualizacao = 0
resto_clique = 0
resto_compartilhamento = 0

# Função que calcula quantidade de cliques
def calcular_clique(visualizacao):
    clique = 0
    global resto_visualizacao

    num = visualizacao // 100 
    resto_visualizacao += visualizacao % 100

    if resto_visualizacao >= 100:
        num = num + 1

    while num > 0:
        clique += 12
        num -= 1 
    return clique

# Função que calcula quantidade de visualizações
def calcular_visualização(valor_investido):
    visualizacao =  valor_investido * 30 

    return visualizacao


def calcular_compartilhamento(clique):
    compartilhamento = 0
    global resto_clique

    num = clique // 20
    resto_clique += clique % 20
    while num > 0:
        compartilhamento += 3
        num -= 1
    
    return compartilhamento * 40

def calcular_max_compartilhamento(compartilhamento):
    #Função sem uso
    #Ainda será implementada
    visualizacao = 0
    global resto_visualizacao

    #compartilhamento = calcular_compartilhamento(calcular_clique(calcular_visualização(valor_digitado)))
    if compartilhamento == 0:
        visualizacao = 0
    elif compartilhamento == 1:
        visualizacao = 40
    elif compartilhamento == 2:
        visualizacao = 80
    elif compartilhamento == 3:
        visualizacao = 120
    else:
        visualizacao = 160

    return visualizacao
    

def calcular_total(valor):
    """Calcula quantidade total de visualizações.
   
    Exemplo de uso:
    >>> calcular_total(8)
    360
    >>> calcular_total(48)
    6
    """
    visualizacao = calcular_visualização(valor)
    compartilhamento = calcular_compartilhamento(calcular_clique(calcular_visualização(valor)))
  
    if valor <= 6:
       print(f'Quantidade de visualizações: {visualizacao}')
    if valor >= 7:
        visualizacao += compartilhamento
        #print(f'Quantidade de visualizações: {(calcular_visualização(valor)) + (calcular_compartilhamento(calcular_clique(calcular_visualização(valor)))))
        print(f'Quantidade de visualizações: {visualizacao}')

while True:

    valor_digitado = input('Digite o valor investido: R$ ')
    if valor_digitado.isdigit():
        valor_digitado = int(valor_digitado)
        calcular_total(valor_digitado)
        break
    else:
        print('\nPor favor, digite um número inteiro.\n')
        continue


'''
def _test():
    import doctest, calculadora
    return doctest.testmod(calculadora)

if __name__ == '__main__':
    _test()
'''

#Versão 1.0 
#Edinara Lima de Alencar