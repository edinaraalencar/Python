'''
Implementei a chamada das funções falta o loop de até 4 compartilhamentos
E testar com valores menores para ver se tem necessidade de acrecentar else nos controles
'''



resto_visualizacao = 0
resto_clique = 0
resto_compartilhamento = 0

# Função que calcula quantidade de visualizações
def calcular_visualização(valor_investido):
    visualizacao =  valor_investido * 30 #  A cada 1 real investido 30 pessoas visualizam 

    return visualizacao

def calcular_clique(visualizacao):
    global resto_visualizacao

    clique = (visualizacao // 100) * 12 #  A cada 100 pessoas que visualizam 12 clicam 
    
    #if ((visualizacao % 100) != 0): # Está certo !
    resto_visualizacao += visualizacao % 100

    return clique

def calcular_compartilhamento(clique):
    global resto_clique

    compartilhamento = (clique // 20) * 3

    #if ((clique % 20) != 0):
    resto_clique += clique % 20

    return compartilhamento

def calcular_visualizacao_compartilhamento(compartilhamento):
    visualizacao_compartilhamento = compartilhamento * 40

    return visualizacao_compartilhamento

def menu():
    
    while True:
        valor_digitado = input('Digite o valor investido: R$ ')

        if valor_digitado.isdigit():
            valor_digitado = int(valor_digitado)
            break
        else:
            print('\nPor favor, digite um número inteiro.\n')
            continue
    

    if valor_digitado <= 6:
        print(f'Valor da visualização: {calcular_visualização(valor_digitado)}')
    else:
        soma1 = (calcular_visualizacao_compartilhamento(calcular_compartilhamento(calcular_clique(calcular_visualização(valor_digitado)))) + resto_visualizacao)
        print(f'Soma 1: {soma1}')

        if soma1 >= 100:
            soma2 = calcular_clique(soma1) + resto_clique
            print(f'Soma 2: {soma2}')

            if soma2 >= 20:
                soma3 = calcular_compartilhamento(soma2) + resto_compartilhamento
                print(f'Soma 3: {soma3}')

                if soma3 >= 3:
                    soma4 = calcular_visualizacao_compartilhamento(soma3)
                    print(f'Soma 4: {soma4}')
                    soma1 += soma4
                    print(soma1)

        print(calcular_visualização(valor_digitado) + soma1)


'''
visualização = calcular_visualização(20)
clique = calcular_clique(visualização)
compartilhamento = calcular_compartilhamento(clique)
visualização_compartilhamento = calcular_visualizacao_compartilhamento(compartilhamento)

print(f'Visualização Final: {visualização}')
print(f'Clique Final: {clique}')
print(f'Compartilhamento Final {compartilhamento}')
print(f'Visualização Comp. Final: {visualização_compartilhamento}')
print(f'Ultimo resto visu: {resto_visualizacao}')
print(f'Ultimo resto clique: {resto_clique}')
print(f'Ultimo resto compartilhamento: {resto_compartilhamento}')
print(f'Total De Visualizações: {visualização + visualização_compartilhamento}')
'''

menu()