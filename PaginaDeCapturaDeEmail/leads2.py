import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QLineEdit
from PyQt5 import QtGui
#Criação da classe principal

class janela2(QMainWindow):

    def __init__(self):
        super().__init__()

        self.topo = 200
        self.esquerda = 200
        self.largura = 500
        self.altura = 300
        self.titulo = 'Aprendendo Python'

# Criação das imagens
        
        self.principal = QLabel(self)
        self.principal.move(1, 1)
        self.principal.setPixmap(QtGui.QPixmap('imagem_main.jpeg'))
        self.principal.resize(700, 700)

        self.carregar_janela2()

    def carregar_janela2(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

app = QApplication(sys.argv)

k = janela2()
sys.exit(app.exec_())

