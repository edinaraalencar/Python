print("""3 - Crie uma função que retorne o resto da divisão do resultado da função 
da questão anterior por 2.\n""")

def função(a, b):
    return ((a * 2) * (b * 3))

def função2(função):
    return função % 2

print(f'O resto da divisão é: {função2(função(1,2))}')