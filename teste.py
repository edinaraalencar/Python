estado_civil = None #Cria variavel e não atribui valor

def estadoCivil (estado_civil): #Cria a função e passa um argumento
    estado_civil = input ("Qual o estado civil-->") #A variavel recebe o valor digitado
    return estado_civil #Guarda o valor digitado pelo usuario

#estadoCivil (estado_civil)

def match(eu, pessoa02): #A função precisa receber 2 estados civil
    if (eu == pessoa02 == 's'): 
        print("Bora")
    elif (eu == pessoa02 == 'c'):
        print("Deixa quieto")
    elif ((eu == 'c') and (pessoa02 == 's')) or ((pessoa02 == 'c') and (eu == 's')):
        print("Deixa quieto")
    else:
        print("Opção Inválida!") #Condição de controle de dados fora do esperado

print ("s=solteiro e c=casado")
match(estadoCivil(estado_civil), estadoCivil(estado_civil)) #Função que recebe outra função como parametro



