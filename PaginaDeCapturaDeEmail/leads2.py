import sqlite3
import sys
from PyQt5 import QtWidgets, uic
import banc
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QTableWidget, QPushButton, QVBoxLayout
from PyQt5 import QtGui
#Criação da classe principal

class janela2(QMainWindow):

    def __init__(self):
        super().__init__()
        self.titulo = 'Controle de Leads'
        self.setFixedSize(1370, 635)
        self.tableWidget = QTableWidget


# Criação das labels
        self.lb_1 = QLabel(self)
        self.lb_1.move(850, 80)
        self.lb_1.setStyleSheet('QLabel {color: black; font: bold; font-size:30px}')
        self.lb_1.resize(500, 100)
        self.lb_1.setText('Gerenciamento de Leads') 

# Criação dos botões
        btbusca = QPushButton('Mostrar E-mails', self)
        btbusca.move(780, 480)  
        btbusca.resize(250, 50)
        btbusca.setStyleSheet('''font: 15pt Arial;margin: 1px;
border-color: #0c457e; border-style: outset;
border-radius: 1px;border-width: 1px;color: black;
background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6); }
QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);''')
        btbusca.clicked.connect(self.btbusca_click)


        btdel = QPushButton('Deletar Repetidos', self)
        btdel.move(1056, 480)  
        btdel.resize(250, 50)
        btdel.setStyleSheet('''font: 15pt Arial;margin: 1px;
border-color: #0c457e; border-style: outset;
border-radius: 1px;border-width: 1px;color: black;
background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2198c0, stop: 1 #0d5ca6); }
QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0d5ca6, stop: 1 #2198c0);''')
        btdel.clicked.connect(self.btdel_click)

# Criação das imagens
        
        self.principal = QLabel(self)
        self.principal.move(1, 1)
        self.principal.setPixmap(QtGui.QPixmap('imagem_main.jpeg'))
        self.principal.resize(700, 700)

# Criação da tabela


        self.carregar_janela2()


    def btbusca_click(self):
        tela_dados.move(780, 225)
        tela_dados.show()
        banco = sqlite3.connect("dados.db")
        cursor = banco.cursor()
        cursor.execute('select * from dados')
        lidos = cursor.fetchall()

        # Jogando os itens na tabela
        tela_dados.tableWidget.setRowCount(len(lidos))
        tela_dados.tableWidget.setColumnCount(2)

        for i in range(0, len(lidos)):
            for j in range(0, 2):
                tela_dados.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))
        banco.close()


    def btdel_click(self):
        banco = sqlite3.connect("dados.db")
        cursor = banco.cursor()
        cursor.execute('select email, Count(email) from dados group by email having Count(email)>1')
        cursor.execute('delete from dados where email in (select email from dados group by email having Count(email)>1) and not nome in (select Min(nome) from dados group by email having Count(email)>1)')
        banco.commit()
        banco.close()
        
        # Repetindo a função de busca
        tela_dados2.move(780, 225)
        tela_dados2.show()
        banco = sqlite3.connect("dados.db")
        cursor = banco.cursor()
        cursor.execute('select * from dados')
        lidos = cursor.fetchall()

        # Jogando os itens na tabela
        tela_dados2.tableWidget.setRowCount(len(lidos))
        tela_dados2.tableWidget.setColumnCount(2)

        for i in range(0, len(lidos)):
            for j in range(0, 2):
                tela_dados2.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lidos[i][j])))
        banco.close()
        

    def carregar_janela2(self):
        self.setWindowTitle(self.titulo)
        self.show()


app = QtWidgets.QApplication([])

j2 = janela2()
tela_dados = uic.loadUi("dados.ui")
tela_dados2 = uic.loadUi("dados.ui")


sys.exit(app.exec_())

