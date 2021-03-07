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
    elif ((user1 == 1 or 2) and (user2 == 2 or 1)):
        print("Deixa Quieto")
    else:                         #Essa condição não está sendo satisfeita
        print("Opção inválida !") #Quero que ela seja satisfeita usando 1 e 7

#Função Principal
print("Digite 1 - Solteiro\n Digite 2 - Casado")
user1 = int (input("Digite o Estado Civil do Primeiro Usuario: "))
user2 = int (input("Digite o Estado Civil do Segundo Usuario: "))
match(user1, user2)