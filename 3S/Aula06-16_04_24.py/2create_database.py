"""                Comentários de várias linhas.
  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

- Instalar o package (pacote) mysql-connector-python:
Main Menu (botão, lado superior esquerdo): - Solução 1, no PyCharm
  File
    – settings
Project: NomeProjeto
    - Python Interpreter
Lado superior esquerdo 	(botão [+])
Available packages: ...
    botão: loaded list of packeges
        mysql-connector-python
    botão: Install package
----- ou
>pip install mysql-connector-python         - Solução 2, no terminal do IDE

- Implemente:
1. Crie o arquivo create_database.py
2. Crie a conexão com o MySQL Workbench
3. Crie a base de dados (database) db_nome_database
    Sintaxe: create database db_nome_database           """

import mysql.connector
conexao_db = mysql.connector.connect(user='root',       # user do servidor
                                password='',            # passwd='ceub123456'
                                host='127.0.0.1')       # host='localhost'
                                # database='')
print('Conexão:', conexao_db)                           # Testando
cursor_db = conexao_db.cursor()     # Cria o cursor para executar comandos SQL
sql = "CREATE DATABASE db_empresa"  # db_empresa é o nome do database
cursor_db.execute(sql)              # Executa o comando SQL
cursor_db.close()                   # Fecha os objetos criados
conexao_db.close()
print('\nConexão fechada.')
""" ----- ALTERAÇÕES:
a. Verifique se o database foi criado no MySQL Workbench.
b. Rode o programa novamente. Porque deu erro?
    ----- DICAS:
Navigator - schemas - botão atualizar                                   # a.
mysql.connector.errors.DatabaseError: 1007 (HY000):                     # b.
Can't create database 'db_empresa'; database exists
    Como evitar esse erro?                                                  
# sql = "CREATE DATABASE db_empresa"                        # Retirar      
sql = "CREATE DATABASE if not exists db_empresa"            # Incluir

"""
