'''
Código está todo funcionando falta implementar a chamada das funções 
e o loop de até 4 compartilhamentos
'''



resto_visualizacao = 0
resto_clique = 0
resto_compartilhamento = 0

# Função que calcula quantidade de visualizações
def calcular_visualização(valor_investido):
    visualizacao =  valor_investido * 30 #  A cada 1 real investido 30 pessoas visualizam 

    return visualizacao

def calcular_clique(visualizacao):
    clique = 0
    global resto_visualizacao

    clique = (visualizacao // 100) * 12 #  A cada 100 pessoas que visualizam 12 clicam 
   
    if ((visualizacao % 100) != 0):
        resto_visualizacao += visualizacao % 100
        print('Dentro do se em calcular_clique')

    return clique

def calcular_compartilhamento(clique):
    compartilhamento = 0
    global resto_clique

    #print(f'Resto clique1: {resto_clique}')
    compartilhamento = (clique // 20) * 3

    if clique > 12:
        resto_clique += clique % 20
        print('Dentro do se em calcular_compartilhamento')
    print(f'Resto clique2: {resto_clique}')
    return compartilhamento

def calcular_visualizacao_compartilhamento(compartilhamento):
    visualizacao_compartilhamento = 0
    visualizacao_compartilhamento = compartilhamento * 40

    return visualizacao_compartilhamento

print(f'Visualização Final: {calcular_visualização(100)}')
print(f'Clique Final: {calcular_clique(3000)}')
print(f'Compartilhamento Final {calcular_compartilhamento(360)}')
print(f'Visualização Comp. Final: {calcular_visualizacao_compartilhamento(54)}')
print(f'Ultimo resto visu: {resto_visualizacao}')
print(f'Ultimo resto clique: {resto_clique}')
print(f'Ultimo resto compartilhamento: {resto_compartilhamento}')
print(f'Total De Visualizações: {calcular_visualização(100) + calcular_visualizacao_compartilhamento(calcular_compartilhamento(calcular_clique(calcular_visualização(100))))}')