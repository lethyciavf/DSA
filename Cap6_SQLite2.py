#import os
import sqlite3
import time
from datetime import datetime
import random
import matplotlib as plt

#os.remove('dsa.db') if os.path.exists('dsa.db') else None
import matplotlib.pyplot as plt

conexao = sqlite3.connect('dsa.db')

cursor = conexao.cursor()


def cria_tabela():
    cursor.execute("CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT,"
                   "prod_nome TEXT, valor REAL)")


def insere_dados():
    cursor.execute("INSERT INTO produtos VALUES (11, '2018-05-02 14:32:11', 'Teclado', 90)")
    conexao.commit()


def data_insert_var():
    nova_data = datetime.now()
    novo_nome = 'Monitor'
    novo_valor = random.randrange(50, 100)
    cursor.execute("INSERT INTO produtos (date, prod_nome, valor) VALUES (?, ?, ?)", (nova_data, novo_nome, novo_valor))
    conexao.commit()


def cria_dados_randomicos():
    for i in range(10):
        data_insert_var()
        time.sleep(1)  #1s


def leitura_dados():
    cursor.execute("SELECT * FROM produtos")
    for linha in cursor.fetchall():
        print(linha)


def leitura_registros():
    cursor.execute("SELECT * FROM produtos WHERE valor > 60.0")
    for linha in cursor.fetchall():
        print(linha)


def leitura_colunas():
    cursor.execute("SELECT * FROM produtos")
    for linha in cursor.fetchall():
        print(linha[3])  #Da coluna 4 (index 3)


def atualiza_dados():
    cursor.execute("UPDATE produtos SET valor = 70.0 WHERE valor = 80.0")  #atualiza o valor da coluna valor onde o valor é igual a 80
    conexao.commit()


def remove_dados():
    cursor.execute("DELETE FROM produtos WHERE valor = 60.0")
    conexao.commit()


def gera_grafico():
    cursor.execute("SELECT id, valor FROM produtos")  #é como se o cursos selecionasse o que colocamos no execute
    ids = []
    valores = []
    dados = cursor.fetchall()  #e o fetch all "joga" esses valores pra uma var

    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])

    plt.bar(ids, valores)
    plt.show()


cria_tabela()  #Podemos deixar esse pois só criara um novo CASO NÃO EXISTA
#insere_dados()
#leitura_dados()
#leitura_registros()
#leitura_colunas()
#atualiza_dados()
#remove_dados()
gera_grafico()

#Manter sempre aqui, uma boa pratica
cursor.close()
conexao.close()
