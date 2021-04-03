cont = 0 #Variavel para controle do numero de matricula

#SuperClasse
class RH:
    def __init__(self, nome, matricula = 0, valor_hora = 5, lista_contratados = []): #init da classe
        #Atributos da classe
       self.nome = input("Digite o nome completo: ")
       self.matricula = matricula
       self.valor_hora = valor_hora
       self.lista_contratados = lista_contratados
       
       
   #Método que contrata e fornece o numero de matricula
    def _contratar(self):
        if self.matricula == 0: #Só matricula se caso ele não tiver um numero de matricula
            global cont #Variavel contador criada para ser usada por todos os funcionarios 
            cont += 1 #Incrementa a variavel cada vez que o método for chamado
            self.matricula = cont 
            print(f'{self.nome} Contratado(a) \nNumero de Matricula: {self.matricula}\n')
            self.lista_contratados.append(self.nome) #Adiciona o nome em uma lista que sera usada para mostrar todos os funcionarios contratados
        else:
            print(f'{self.nome} já está contratado(a) !\n')

    
    #Método que descontrata e tira o nome da lista_contratados
    def _descontratar(self):
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
    def _mostrar_contratados(self):
            if cont > 0: #Executa se a lista tiver pelo menos 1 funcionário
                print(self.lista_contratados) 
                print("\n")
            else:
                print("Não existem funcionários contratados. \n")


#SubClasse de RH
class Funcionario(RH): #Passando a SuperClasse como argumento
   def __init__(self, nome, matricula, valor_hora): #init da classe
       super().__init__(nome, matricula, valor_hora) # init da superclasse



       