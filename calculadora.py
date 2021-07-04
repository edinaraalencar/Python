''' Penultima versão '''
resto_visualizacao = 0
resto_clique = 0

# Função que calcula quantidade de visualizações
def calcular_visualização(valor_investido):
    visualizacao =  valor_investido * 30 

    return visualizacao

def calcular_clique(visualizacao):
    global resto_visualizacao
    clique = (visualizacao // 100) * 12 
    
    if ((visualizacao % 100) != 0): 
        resto_visualizacao += visualizacao % 100

    return clique

def calcular_compartilhamento(clique):
    global resto_clique
    compartilhamento = (clique // 20) * 3
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

    elif valor_digitado > 6 and valor_digitado <= 9:
        visualizacao = calcular_visualização(valor_digitado)
        visualizacao_compartilhamento = calcular_visualizacao_compartilhamento(calcular_compartilhamento(calcular_clique(visualizacao)))
        print(f'Valor da visualização: {visualizacao + visualizacao_compartilhamento}')

    elif valor_digitado > 9 and valor_digitado <= 11:
        visualizacao = calcular_visualização(valor_digitado) 
        visualizacao_compartilhamento = calcular_visualizacao_compartilhamento(calcular_compartilhamento(calcular_clique(calcular_visualização(valor_digitado))))
        
        soma = visualizacao + visualizacao_compartilhamento
        i = 0
        soma1 = visualizacao_compartilhamento + resto_visualizacao
        resto_visu = resto_visualizacao
        resto_click = resto_clique

        while i < 2:      
            soma2 = calcular_clique(soma1) + resto_click
                
            if soma2 >= 20:
                soma3 = calcular_compartilhamento(soma2)

                if soma3 >= 3:
                    soma4 = calcular_visualizacao_compartilhamento(soma3) + resto_visualizacao
                    prox_visualizacao = calcular_visualizacao_compartilhamento(soma3)
                    soma1 = soma4 
                    soma += prox_visualizacao
                    i += 1 

                else:
                    soma -= prox_visualizacao
                    i += 1
        print(f'Soma Total: {soma}')        
    else:
        visualizacao = calcular_visualização(valor_digitado) 
        visualizacao_compartilhamento = calcular_visualizacao_compartilhamento(calcular_compartilhamento(calcular_clique(calcular_visualização(valor_digitado))))
        
        soma = visualizacao + visualizacao_compartilhamento
        i = 0
        soma1 = visualizacao_compartilhamento + resto_visualizacao
        resto_visu = resto_visualizacao
        resto_click = resto_clique

        while i < 3:      
            soma2 = calcular_clique(soma1) + resto_click
                
            if soma2 >= 20:
                soma3 = calcular_compartilhamento(soma2) + resto_compartilhamento

                if soma3 >= 3:
                    soma4 = calcular_visualizacao_compartilhamento(soma3) + resto_visu
                    prox_visualizacao = calcular_visualizacao_compartilhamento(soma3)
                    soma1 = soma4 
                    soma += prox_visualizacao
                    i += 1 
                
        print(f'Soma Total: {soma}')             
    

menu()