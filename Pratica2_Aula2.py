'''
Para todas as práticas utilize as 
funções criadas anteriormente

Crie uma função chamada Match que receba 
o seu estado civil(função) e o de outra pessoa, 
e retorne "Bora" se ambos forem solteiros ou 
"Deixa quieto" se algum for Casado
'''
estado_civil = None #Cria variavel e não atribui valor

def estadoCivil (estado_civil): #Cria a função e passa um argumento
    estado_civil = int (input ("Qual o estado civil-->")) #A variavel recebe o valor digitado
    return estado_civil #Guarda o valor digitado pelo usuario

#estadoCivil (estado_civil)

def match(user1, user2): #A função precisa receber 2 estados civil
    if (user1 == user2 == 1): 
        print("Bora")
    elif (user1 == user2 == 2):
        print("Deixa quieto")
    elif ((user1 == 2) and (user2 == 1)) or ((user2 == 2) and (user1 == 1)):
        print("Deixa quieto")
    else:
        print("Opção Inválida!") #Condição de controle de dados fora do esperado

print ("Opções:\n1 - solteiro\n2 - casado")
match(estadoCivil(estado_civil), estadoCivil(estado_civil)) #Função que recebe outra função como parametro


