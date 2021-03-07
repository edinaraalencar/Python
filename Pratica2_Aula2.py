'''
Para todas as práticas utilize as 
funções criadas anteriormente

Crie uma função chamada Match que receba 
o seu estado civil(função) e o de outra pessoa, 
e retorne "Bora" se ambos forem solteiros ou 
"Deixa quieto" se algum for Casado
'''
def match(user1, user2):
    if (user1 == 2) and (user2 == 2):
        print("Deixa quieto")
    elif (user1 == 1) and (user2 == 1):
        print("Bora")
    elif (((user1 == 1) and (user2 == 2)) or ((user1 == 2) and (user2 ==1))):
        print("Deixa Quieto")
    else:
        print("Opção inválida !")

#Função Principal
print("Digite 1 - Solteiro\n Digite 2 - Casado")
user1 = int (input("Digite o Estado Civil do Usuario 1"))
user2 = int (input("Digite o Estado Civil do Usuario 2"))
match(user1, user2)
