l_func = ["Edinara", "Eudasio", "Joao"]

print(l_func)

nome = input("Digite um nome: ")
for i in l_func:
    if nome in l_func:
        l_func.remove(nome)
    
    

print(l_func)