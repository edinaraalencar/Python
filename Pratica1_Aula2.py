'''
Faça quatro funções que retornem respectivamente
(Nome, idade, Estado civil e Gênero)
'''
#Criando e inicializando as variaveis

meu_nome = "Edinara"
minha_idade = 22
meu_estado_civil = "a espera de um milagre"
meu_genero = "feminino"

#Criando as funções e armazenando os valores atraves do return

def nome(meu_nome):
    return meu_nome

def idade(minha_idade):
    return minha_idade

def estadoCivil (meu_estado_civil):
    return meu_estado_civil

def genero(meu_genero):
    return meu_genero

#Chamando cada uma das fuções

print("\n   Minha Biografia\n")
print (f'- Meu nome é {nome(meu_nome)}')
print (f'- Minha idade é {idade(minha_idade)} anos')
print (f'- Meu estado civil se resume em {estadoCivil(meu_estado_civil)}')
print (f'- Meu gênero é {genero(meu_genero)}')