"""                   Comentários de várias linhas.
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

- Na base de dados db_empresa, crie a tabela funcionario com as colunas:
identificador, nome e salário.
Escolha a chave primária, uma coluna obrigatória e uma coluna opcional.

- Sintaxe:
CREATE TABLE tb_nome_tabela(
    nome_coluna tipo_coluna,
    ...,
    nome_coluna tipo_coluna,
    PRIMARY KEY (nome_coluna)
    )
- Implemente:
1. Crie o arquivo create_table.py
2. Faça a conexão incluindo o database criado
3. Crie a tabela                                    """

import mysql.connector
conexao = mysql.connector.connect(user='root',      # user do servidor
                            password='',            # passwd='ceub123456'
                            host='127.0.0.1',       # host='localhost'
                            database='db_empresa')  # Incluir o database
print('Conexão:', conexao)                          # Testando
cursor = conexao.cursor()   # Cria o cursor para executar comandos SQL
sql = ''' CREATE TABLE tb_funcionario(
          idt INT,                    # Chave primária
          nome VARCHAR(45) NOT NULL,  # Obrigatório
          salario DECIMAL(9,2) NULL,  # Opcional
          PRIMARY KEY (idt)           # not null é default na primary key
    ) '''
cursor.execute(sql)
cursor.close()
conexao.close()
print('\nConexão fechada.')
""" ----- ALTERAÇÕES:
a. Veja se o tabela foi criado no MySQL Workbench.
b. Rode o programa novamente. Porque deu erro?
    ----- DICAS:
Navigator - schemas - botão atualizar - db_empresa  -   tables      # a.
mysql.connector.errors.ProgrammingError: 1050 (42S01):              # b.
Table 'tb_funcionario' already exists
    Como evitar esse erro?                                              
# sql = '''   CREATE TABLE tb_funcionario(                  # Retirar
sql = '''   CREATE TABLE IF NOT EXISTS tb_funcionario(      # Incluir

"""
