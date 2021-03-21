print("""4 - Faça uma função que receba uma lista e 3 números, esses números devem ser 
índices válidos dessa lista. A função deve retornar uma tupla composta pelos valores 
dos índices indicados.""")

numeros = [x for x in range(1, 11)] #Criando a lista com o metodo range

def num(numeros, a, b, c):
    L = []
    L.append(numeros[a]) #Adicionando os valores na lista do indice recebido como parametro
    L.append(numeros[b])
    L.append(numeros[c])
    numeros_novo = tuple(L) #Criando uma lista atraves do construtor tuple
    print(numeros_novo)

num(numeros, 2, 4, 5) #Passando uma lista e 3 indices como p-arametros para a função