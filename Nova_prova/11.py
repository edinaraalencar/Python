'''
11 - Escreva um programa que gere automaticamente uma lista com 100 inteiros e
faça o que se pede a seguir:
● Uma lista os quadrados dos itens da lista original
● Um dicionário que utilize os itens da lista como valor ou chave
'''

inteiros = [x for x in range(1, 101)]

quadrados = [x**2 for x in inteiros]


dic = {x : [quadrados] for x in inteiros}
   

print(inteiros)
print(quadrados)
print(dic)