'''
1 - Implemente a classe Funcionário com os seguintes atributos(matrícula, setor, 
valor_hora, número de faltas), construa métodos que você acha útil para essa classe.
'''

cont = 0 #Variavel para controle do numero de matricula

class Funcionario: #Classe principal
    def __init__(self, setor = 1, valor_hora = 5, num_faltas = 0, matricula = 0): #Atributos
        self.setor = setor 
        self.valor_hora = valor_hora
        self.num_faltas = num_faltas
        self.matricula = matricula
      


    def mostrar_ficha(self): #Método
        print("FICHA DO FUNCIONÁRIO")
        print(f"""
            Setor: {self.setor}
            Valor hora: {self.valor_hora}
            Numero faltas: {self.num_faltas}
            Matricula: {self.matricula}
            """)

#Método que contabiliza e mostra o numero de matricula
    def contratar(self): 
        if self.matricula == 0: #Só matricula se caso ele não tiver um numero de matricula
            global cont #Variavel contador criada para ser usada por todos os funcionarios 
            cont += 1 #Incrementa a variavel cada vez que o método for chamado
            self.matricula = cont 
            print(f'Funcionário Contratado \nNumero de Matricula: {self.matricula}')
        else:
            print("Funcionário já contratado !")


#Método 
    def descontratar(self):
        if self.matricula > 0:
            self.matricula = 0 #Atribui a matricula a zero para ele poder ser contratado novamente
            global cont
            cont -= 1 #Decrementa a variavel cada vez que o método for chamado
            print("Funcionário Demitido" )
        else:
            print("O Funcionário não está contratado. ")


    def pagar(self):
        if self.matricula > 0:
            dias_trabalhados = int(input("Digite a quantidade de dias trabalhados: "))
            valor = dias_trabalhados * (self.valor_hora * 8) #8 é a quantidade de horas em 1 dia 
            print(f'Salário do mês: R$ {valor},00')
        else:
            print("O Funcionário precisa ser contratado primeiro. ")


    def trocar_setor(self): 
        if self.matricula > 0:
            self.valor_hora = 7
            self.setor += 1
            print("Parabéns você foi promovido! ")
        else:
            print("O Funcionário precisa ser contratado primeiro. ")      


    def mostrar_funcionarios(self):
            if self.matricula > 0:
                print(edinara.mostrar_ficha)
                print(eudasio.mostrar_ficha)

edinara = Funcionario()
eudasio = Funcionario()
joao = Funcionario()

edinara.contratar()
eudasio.contratar()
edinara.descontratar()
edinara.contratar()
joao.pagar()
