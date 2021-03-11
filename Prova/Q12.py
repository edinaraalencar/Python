'''
12 - Escreva um programa que pergunte a distância que um passageiro deseja
percorrer em km. Calcule o preço da passagem, cobrando R $0.05 por metro para
viagens de até 200 km, e R $0.10 para viagens mais longas.
'''


km = float(input('Quantos km você vai percorrer?\n'))

if (km < 200):
    total = (0.05 * km * 1000)
    print(f'O valor cobrado será: \n{total:.2f} reais.')
else:
    total = (0.10 * km * 1000)
    print(f'O valor cobrado será: \n{total:.2f} reais.')