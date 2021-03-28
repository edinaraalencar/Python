'''
1 - Implemente a classe Funcionário com os seguintes atributos(matrícula, setor, 
valor_hora, número de faltas), construa métodos que você acha útil para essa classe.
'''

cont = 0 #Variavel para controle do numero de matricula

class Funcionario: #Classe principal
    def __init__(self, nome, setor = 1, valor_hora = 5, num_faltas = 0, matricula = 0, l_func = []):
        #Atributos
        self.setor = setor 
        self.valor_hora = valor_hora
        self.num_faltas = num_faltas
        self.matricula = matricula
        self.l_func = l_func
        self.nome = nome


    def mostrar_ficha(self): #Método
        if self.matricula > 0: #Teste feito em todos os métodos para saber se já está contratado
            print("FICHA DO FUNCIONÁRIO(A)")
            print(f"""
                Nome: {self.nome}
                Setor: {self.setor}
                Valor hora: {self.valor_hora}
                Numero faltas: {self.num_faltas}
                Matricula: {self.matricula}
                \n""")
        else:
            print(f'{self.nome} não está contratado(a). \n')


#Método que contabiliza e mostra o numero de matricula
    def contratar(self):
        if self.matricula == 0: #Só matricula se caso ele não tiver um numero de matricula
            global cont #Variavel contador criada para ser usada por todos os funcionarios 
            cont += 1 #Incrementa a variavel cada vez que o método for chamado
            self.matricula = cont 
            print(f'{self.nome} Contratado(a) \nNumero de Matricula: {self.matricula}\n')
            self.l_func.append(self.nome) #Adiciona o nome em uma lista que sera usada para mostrar todos os funcionarios contratados
        else:
            print(f'{self.nome} já está contratado(a) !\n')


#Método 
    def descontratar(self):
        if self.matricula > 0:       
            self.matricula = 0 #Atribui a matricula a zero para ele poder ser contratado novamente
            global cont
            cont -= 1 #Decrementa a variavel cada vez que o método for chamado
            print(f'{self.nome} você foi demitido(a). \n')

            for i in self.l_func: #Percorre a lista de funcionarios
                if self.nome in self.l_func: #Faz um teste se o nome do funcionario esta na lista
                    self.l_func.remove(self.nome) #Se estiver na lista ele remove
                    
        else:
            print(f'{self.nome} não está contratado(a). \n')


    def pagar(self):
        if self.matricula > 0:
            dias_trabalhados = int(input("Digite a quantidade de dias trabalhados: "))
            valor = dias_trabalhados * (self.valor_hora * 8) #8 é a quantidade de horas em 1 dia 
            print(f'{self.nome} seu salário do mês é: R$ {valor},00 \n')
        else:
            print(f'{self.nome} precisa ser contratado(a) primeiro. \n')


    def trocar_setor(self): 
        if self.matricula > 0:
            self.valor_hora = 7
            self.setor += 1
            print(f'{self.nome} Parabéns você foi promovido(a)! \n')
        else:
            print(f'{self.nome} precisa ser contratado(a) primeiro. \n')      


    def mostrar_funcionarios(self):
            if cont > 0: #Executa se a lista tiver pelo menos 1 funcionário
                print(self.l_func) 
                print("\n")
            else:
                print("Não existem funcionários contratados. \n")

edinara = Funcionario("Edinara")
eudasio = Funcionario("Eudasio")

edinara.contratar()
eudasio.contratar()
edinara.mostrar_funcionarios()
eudasio.mostrar_funcionarios()
edinara.descontratar()
edinara.mostrar_funcionarios()
eudasio.mostrar_funcionarios()
edinara.mostrar_ficha()
eudasio.trocar_setor()
eudasio.mostrar_ficha()