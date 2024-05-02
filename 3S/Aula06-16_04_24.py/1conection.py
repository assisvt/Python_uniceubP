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
1. Crie o arquivo connection.py
2. Faça a conexão com o MySQL Workbench           """

import mysql.connector
conexao_db = mysql.connector.connect(user='root',       # user do servidor
                                password='',            # passwd='ceub123456'
                                host='127.0.0.1')       # host='localhost'
                                # database='')
print('Conexão:\n', conexao_db)                         # Testando
conexao_db.close()
print('\nConexão fechada.')
""" - Saída:
Conexão: 
<mysql.connector.connection.MySQLConnection object at 0x00000264B07FED60>

Conexão fechada.

"""
