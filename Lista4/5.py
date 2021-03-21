print("""5- Escreva um programa que gere automaticamente uma lista com 40 inteiros e 
faça o que se pede a seguir:

a- imprima o primeiro quarto da lista
b -imprima o último quarto da lista
c -imprima os 5 itens do meio da lista
d -imprima a lista reversa
e - Imprima o primeiro e o último item da lista

Utilize list comprehension para :

f - Gerar uma lista com o quadrado de cada item da lista original
g - Gerar uma lista com apenas itens pares da lista original""")

inteiros = [x for x in range(1, 41)]
print(inteiros)
print(inteiros[0:10])
print(inteiros[30:40])
print(inteiros[18:23])
print(inteiros[ : :-1])
print(f'Primeiro item: [{inteiros[0]}], ultimo item:[{inteiros[39]}]')

quadrado = [x**2 for x in range(1, 41)]
print(quadrado)

pares = [x for x in range(1, 41) if x % 2 == 0]
print(pares)

