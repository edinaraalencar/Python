''' Projeto de criação de uma página de captura de e-mail

To do
- Alterar a paleta de cores
- Implementar a junção com o BD
- Chamar uma segunda janela de retorno para o usuário
- Desenvolver o rodapé
- Excluir dados iguais

Done
- botão principal
- Imagem
- 2 caixas de texto

Doing
Segunda janela

'''

import sys
import os
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit
from PyQt5 import QtGui
#Criação da classe principal

class janela(QMainWindow):

    def __init__(self):
        super().__init__()
        self.titulo = 'Aprendendo Python'
        self.setFixedSize(1370, 635)


# Criação da caixa de texto

        self.caixa_texto1 = QLineEdit(self)
        self.caixa_texto1.move(850, 350)
        self.caixa_texto1.resize(450, 50)
        
        self.caixa_texto2 = QLineEdit(self)
        self.caixa_texto2.move(850, 410)
        self.caixa_texto2.resize(450, 50)

# Criação do botão 

        bt1 = QPushButton('Baixar Material', self)
        bt1.move(850, 480)  
        bt1.resize(450, 50)
        #bt1.setStyleSheet('QPushButton {background-color:yellow; font: bold; fonte-size:50px}')

        bt1.setStyleSheet('''font: 15pt Arial;margin: 1px;
border-color: #0c457e; border-style: outset;
border-radius: 1px;border-width: 1px;color: black;
background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6); }
QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);''')
        bt1.clicked.connect(self.bt1_click)


# Criação da Label

        self.lb_1 = QLabel(self)
        self.lb_1.move(850, 150)
        self.lb_1.setStyleSheet('QLabel {color: black; font: bold; font-size:30px}')
        self.lb_1.resize(500, 100)
        self.lb_1.setText('Aprenda de uma vez como\nusar a Linguagem Python.')  # Não está aparecendo o texto completo 

        self.lb_2 = QLabel(self)
        self.lb_2.move(850, 250)
        self.lb_2.setStyleSheet('QLabel {color: black; font bold; font-size:20px}')
        self.lb_2.resize(500, 100)
        self.lb_2.setText('''Baixe o e-book e tenha acesso a um conteúdo
exclusivo que foi desenvolvido para você estudante
de programação com Python. ''') 

        self.lb_4 = QLabel(self)
        self.lb_4.move(850, 540)
        self.lb_4.setStyleSheet('QLabel {color: black; font bold; font-size:15px}')
        self.lb_4.resize(500, 100)
        self.lb_4.setText('Todos os direitos reservados.')

        self.lb_3 = QLabel(self)
        self.lb_3.move(900, 50)
        self.lb_3.setStyleSheet('QLabel {color: black; font: bold; font-size:30px}')
        self.lb_3.resize(500, 100)
        

# Criação das imagens
        
        self.principal = QLabel(self)
        self.principal.move(1, 1)
        self.principal.setPixmap(QtGui.QPixmap('imagem_main.jpeg'))
        self.principal.resize(700, 700)

        self.carregar_janela()

    def carregar_janela(self):
        self.setWindowTitle(self.titulo)
        self.show()


    def carregar_janela2(self):
        self.setWindowTitle('Tela 2')
        self.show()

    def bt1_click(self):
        nome = self.caixa_texto1.text()
        email = self.caixa_texto2.text()
        
        os.system('clear')

        titulo = ' Lista de Leads '
        print(f'{titulo:#^50}')
        print(f'Nome digitado: {nome}')
        print(f'E-mail digitado: {email}')

        self.carregar_janela2()
        self.lb_3.setText('Aproveite o seu material !')

        
   


app = QApplication(sys.argv)

j = janela()
sys.exit(app.exec_())


    