import sqlite3

CREATE_TABLE = "create table dados(nome text, email text)"

INSERT_DADOS = "insert into dados (nome, email) values (?, ?)"

SELECT_REPETIDOS = "select * from dados"

#DELETE_REPETIDOS = "delete from dados where"

def connect():
    return sqlite3.connect('dados.db')

def create(conexao):
    with conexao:
        conexao.execute(CREATE_TABLE)

def add_dados(conexao, nome, email):
    with conexao:
        conexao.execute(INSERT_DADOS, (nome, email))

def selecao(conexao):
    with conexao:
        return conexao.execute(SELECT_REPETIDOS).fetchall()


