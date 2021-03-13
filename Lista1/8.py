print("""8 - P = True e Q = False. Aplique De Morgan na seguinte proposição e atribua 
o valor a uma variável - ~(p ^ (p v q)), essa variável deve ser retornada partir de uma 
função\n""")

p = True
q = False
def deMorgan(p, q):
    negacao = not(p and (p or q))
    return negacao

print(f'O resultado dessa proposição ~(p ^ (p v q)) é: {deMorgan(p, q)}')