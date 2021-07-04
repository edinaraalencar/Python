'''
Implementei o loop de até 4 compartilhamentos
Está dando erro no valor 12
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
    
    if ((visualizacao % 100) != 0): # Está certo !
        resto_visualizacao += visualizacao % 100

    #print(f'Resto visu em clique: {resto_visualizacao}')

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

    elif valor_digitado <= 9:
        visualizacao = calcular_visualização(valor_digitado)
        visualizacao_compartilhamento = calcular_visualizacao_compartilhamento(calcular_compartilhamento(calcular_clique(visualizacao)))
        print(f'Valor da visualização: {visualizacao + visualizacao_compartilhamento}')

    else:
        visualizacao = calcular_visualização(valor_digitado) # Antes era calcular visualização do compartilhamento
        visualizacao_compartilhamento = calcular_visualizacao_compartilhamento(calcular_compartilhamento(calcular_clique(calcular_visualização(valor_digitado))))
        
        soma = visualizacao + visualizacao_compartilhamento

        
        #print(f'Soma: {soma}')
        #print(f'Visualização: {visualizacao}')
        #print(f'Visualização Compartilhamento: {visualizacao_compartilhamento}')

        #print(f'Soma 1: {soma1}')

        i = 0
        

        soma1 = visualizacao_compartilhamento + resto_visualizacao
        #print(f'Soma1: {soma1}')
        resto_visu = resto_visualizacao
            
        while i < 3:      #Troca por while
            soma2 = calcular_clique(soma1) + resto_clique
            print(f'Soma 2: {soma2}')
            print(f'Soma Total: {soma}')
                
            if soma2 >= 20:
                soma3 = calcular_compartilhamento(soma2) + resto_compartilhamento
                print(f'Soma 3: {soma3}')
                print(soma)

                if soma3 >= 3:
                    soma4 = calcular_visualizacao_compartilhamento(soma3) + resto_visu
                    print(f'Resto visualização: {resto_visu}') # Com o valor 11 Está dando 80 e é 50
                    prox_visualizacao = calcular_visualizacao_compartilhamento(soma3)
                    print(f'Soma 4: {soma4}')
                    soma1 = soma4 # Tinha +
                    soma += prox_visualizacao
                    print(f'Soma Total2: {soma}')
                    i += 1 
                
                     
    #print(f'Total de visualizações: {visualizacao}')
    #print(f'Prox Visualização: {prox_visualizacao}')
        print(f'Soma Total: {soma}')
        


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