import os
import sqlite3

os.remove('escola.db') if os.path.exists('escola.db') else None

conexao = sqlite3.connect('escola.db')  # conecta no bd, mas se ele não existir, ele é criado

#print(type(conexao))

cursor = conexao.cursor()  # Abre o cursor para percorrer o bd

#print(type(cursor))

sql_create = ("create table cursos "  # Cria uma tabela com instrução SQL com nome cursos
              "(id interger primary key, "  # Essas são as colunas, a primeira se chama id é do tipo int e é uma PK
              "titulo varchar(100), "  # Segunda coluna, nome titulo tipo char com ate 100 caracteres
              "categoria varchar(140))")  # Terceira coluna, nome categoria tipo char com ate 140 caracteres

cursor.execute(sql_create)  # Executa a criação da tabela das linhas anteriores, então o sql_create por si só não cria a tabela

sql_insert = 'insert into cursos values (?, ?, ?)'

recset = [(1000, 'Ciência de Dados', 'Data Science'),
          (1001, 'Big Data Fundamentos', 'Big Data'),
          (1002, 'Python Fundamentos', 'Análise de Dados')]  #Record Set, uma lista com as informações a serem gravadas no bd, cada elemento é uma tupla

for rec in recset:
    cursor.execute(sql_insert, rec)  #Insere os registros um a um iterando a lista recset

conexao.commit()  #Salva a inserção dos registros no bd
'''
sql_select = 'select * from cursos'  # * = todos

cursor.execute(sql_select)  #Executa o sql_select
dados = cursor.fetchall()  #Pega todos os registros e salva na var dados

for linha in dados:
    print(linha)
'''
recset = [(1003, 'Gestão de Dados com MongoDB', 'Big Data'),
          (1004, 'R Fundamentos', 'Análise de Dados')]

for rec in recset:
    cursor.execute(sql_insert, rec)

conexao.commit()

cursor.execute('select * from cursos')  #Executa o comando em sql
dados = cursor.fetchall()  #Pega todos os registros e salva na var dados

'''for linha in dados:
    print(linha)'''

conexao.close() #Fecha a conxão após o uso, boas práticas
