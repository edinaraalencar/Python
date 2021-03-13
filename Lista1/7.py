print("""7 - Escreva uma função que receba a idade do usuário e indique se ele pode ou 
não encher a cara de cachaça.\n""")

def bebidas(idade):
    if idade >= 18:
        return "Você pode encher a cara de cachaça. "
    return "Você não pode encher a cara de cachaça. "
    
    
idade = int (input("Digite a sua idade: "))
print(bebidas(idade))
    