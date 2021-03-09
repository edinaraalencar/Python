salario=1100

def adicional_salario(vendas, nome = 'Eudasio'): 
    if vendas > 550:
        global salario 
        salario += 550
        print (f'{nome} o seu salário é de: R${salario}')
    else:
        print (f'{nome} o seu salário é de: R${salario}')

#nome = input("\nDigite o nome do funcionario: ")        
vendas=float(input("Total de vendas do funcionario: "))
adicional_salario(vendas, 'Edinara')

