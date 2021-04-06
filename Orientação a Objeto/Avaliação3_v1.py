#Sistema de emprestimo de materiais e atendimento ao cliente
cont = 0 #Variavel para controle do numero de matricula


#SuperClasse
class Funcionario:
    def __init__(self, nome = None, matricula = 0, valor_hora = 5): #init da classe
        #Atributos da classe
       self.nome = nome
       self.matricula = matricula
       self.valor_hora = valor_hora
       


#SubClasse de Funcionario
class RH(Funcionario): #Passando a SuperClasse como argumento
    def __init__(self, nome = None, matricula = 0, valor_hora = 5, lista_contratados = []): #init da classe
       super().__init__(nome, matricula, valor_hora) # init da superclasse
       self.lista_contratados = lista_contratados


    #Método que contrata e fornece o numero de matricula
    def contratar(self): 
        self.nome = input("Digite o nome completo: ")
        if self.matricula == 0: #Só matricula se caso ele não tiver um numero de matricula
            global cont #Variavel contador criada para ser usada por todos os funcionarios 
            cont += 1 #Incrementa a variavel cada vez que o método for chamado
            self.matricula = cont 
            print(f'{self.nome} Contratado(a) \nNumero de Matricula: {self.matricula}\n')
            self.lista_contratados.append(self.nome) #Adiciona o nome em uma lista que sera usada para mostrar todos os funcionarios contratados
        else:
            print(f'{self.nome} já está contratado(a) !\n')

    
    #Método que descontrata e tira o nome da lista_contratados
    def descontratar(self): 
        if self.matricula > 0:       
            self.matricula = 0 #Atribui a matricula a zero para ele poder ser contratado novamente
            global cont
            cont -= 1 #Decrementa a variavel cada vez que o método for chamado
            print(f'{self.nome} você foi demitido(a). \n')

            for i in self.lista_contratados: #Percorre a lista de funcionarios
                if self.nome in self.lista_contratados: #Faz um teste se o nome do funcionario esta na lista
                    self.lista_contratados.remove(self.nome) #Se estiver na lista ele remove
        
        else:
            print(f'{self.nome} não está contratado(a). \n')

    
    #Método que mostra a lista de contratados
    def mostrar_contratados(self): 
            if cont > 0: #Executa se a lista tiver pelo menos 1 funcionário
                print(self.lista_contratados) 
                print("\n")
            else:
                print("Não existem funcionários contratados. \n")

class Vendedor(Funcionario):
    def __init__(self, nome = None, matricula = 0, valor_hora = 5):
        super().__init__(nome, matricula, valor_hora)

    
    def vender(self):
        print("Venda concluida com sucesso !")

    def comissão(self):
        print("Sua comissão de vendas é 10% ")


class Atendente(Vendedor, Funcionario):
    def __init__(self, nome = None, matricula = 0, valor_hora = 5, material = 5, lista_clientes = []):
        super().__init__(nome, matricula, valor_hora)
        self.material = material
        self.lista_clientes = lista_clientes
    
    def cadastrar_cliente(self):
        self.nome = input("Digite o nome completo: ")
        
        if self.nome not in self.lista_clientes: #Se o nome que deseja cadastrar não estiver na lista 
            print("Cliente cadastrado com sucesso !")
            self.lista_clientes.append(self.nome) #ele cadastra e insere na lista
        else:
            print("Cliente já cadastrado ") #Se não ele mostra essa mensagem

    def receber_pagamentos(self):
        print("Pagamento recebido com sucesso !")

    def liberar_material(self):
        if self.material > 0:
            print("Material liberado !")
            self.material -=1 #Decrementa do valor total de material
            print(self.material) #Material que ainda resta no estoque
        else:
            print("Material em falta. ")

    def comissão(self): #Encapsulamento com override da classe Vendedor
        print("Sua comissão é 5 % ")


class Cliente:
    def __init__(self, nome = None, endereço = None, rg = None, cpf = None, cod = 0):
        self.nome = nome
        self.endereço = endereço
        self.rg = rg
        self.cpf = cpf
        self.cod = cod


    def pagar_parcela(self):
        print("Parcela paga !")

    def solicitar_material(self):
        self.material = input("Digite qual material você deseja: ")
        print("Material solicitado. ")
        


#edinara = RH()
#edinara.contratar()
'''
tiago = Vendedor()
tiago.vender()
tiago.comissão()
'''
najla = Atendente()
najla.vender()
najla.comissão()
najla.cadastrar_cliente()
najla.cadastrar_cliente()
joao = Cliente()
joao.solicitar_material()
najla.liberar_material()
najla.receber_pagamentos()



