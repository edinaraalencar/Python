'''
21 - Escreva as seguintes funções lambda.
 - Uma função que receba um nome e retorne o seu equivalente minúsculo
 - Uma função que receba dois parâmetros e retorne o primeiro como potência da
metade do segundo
'''

convertido = lambda nome: nome.lower()
    

parametro = lambda a, b: (b / 2) ** a

print(convertido("EDINARA"))
print(parametro(4, 4))
