"""
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

>pip install mysql-connector-python    - Solução 2, no terminal dos IDEs

"""

import mysql.connector
def create_database():
    conexao_db = mysql.connector.connect(user='root',  # user do servidor
                            password='',               # passwd='ceub123456'
                            host='127.0.0.1')          # host='localhost'
                            # database='')
    print('Conexão db:', conexao_db)  # Teste
    cursor_db = conexao_db.cursor()   # Cria cursor para executar comandos SQL
    sql = "CREATE DATABASE if not exists db_cadastro"  # O nome do database
    cursor_db.execute(sql)            # Executa o comando sql
    cursor_db.close()
    conexao_db.close()
    print('\nConexão db fechada.')

def create_connection():
    con = mysql.connector.connect(user='root',      # user do servidor
                            password='',            # passwd='ceub123456'
                            host='127.0.0.1',       # host='localhost'
                            database='db_cadastro')  # Nome do schema criado
    print('Conexão:', con)                          # Testando
    return con

def create_table():
    sql_cargo = """ CREATE TABLE IF NOT EXISTS td_cargo( 
    idt int NOT NULL AUTO_INCREMENT,  # Cria automaticamente a chava primária
    nome varchar(45) UNIQUE NOT NULL, # Valores sem repetição
    PRIMARY KEY (idt)                 # Define a chave primária
    )   """
    cursor.execute(sql_cargo)         # Primeiro, crie a tabela td_cargo
    sql_empregado = """ CREATE TABLE IF NOT EXISTS tb_empregado(
    idt int NOT NULL AUTO_INCREMENT,  # Cria automaticamente a chava primária
    nome varchar(45) NOT NULL,        # NOT NULL para valor obrigatório
    dta_nascimento date NULL,         # NULL para valor opcional
    genero enum('M', 'F') NOT NULL,   # Aceita 'M', 'm, 'F' ou 'f' 
    cod_cargo int NOT NULL,           # NOT NULL para valor obrigatório
    PRIMARY KEY (idt),                # Define a chave primária
    FOREIGN KEY(cod_cargo) REFERENCES td_cargo(idt)  # Define chave estrangeira
    )   """
    cursor.execute(sql_empregado)     # Depois, crie a tabela tb_empregado

def insert_cargo():                   # Solução 1
    a_nome = input('Nome do cargo: ')  # Insere primeiro na tabela domínio
    sql = f"""  insert into td_cargo (nome)
                values('{a_nome}')              """
    cursor.execute(sql)
    conexao.commit()                  # Confirma a alteração no database

def insert_empregado():                       # Solução 1
    a_nome = input('Nome empregado: ')
    a_dta_nascimento = input("Data nascimento: aaaa-mm-dd: ")
    a_genero = input("Gênero [M] ou [F]: ")
    a_cod_cargo = int(input('FK - Código Cargo: '))
    sql= f"""insert into tb_empregado (nome, dta_nascimento, genero, cod_cargo)
     values('{a_nome}', '{a_dta_nascimento}', '{a_genero}', {a_cod_cargo}) """
    cursor.execute(sql)
    conexao.commit()                # UPDATE/INSERT/DELETE Confirma a alteração no database

def select_all_emp():
    sql = ' SELECT * from tb_empregado '
    cursor.execute(sql)
    registros = cursor.fetchall()   # registros é uma lista de tuplas
    print('- List of tuplas:')      # Solução 1:
    print(registros)                # Mostra os registros na horizontal
    print('- Tuplas:')              # Solução 2:
    for record in registros:        # Mostra os registros na vertical
        print("- Id::", record[0])
        print("- Name", record[1])
        print("- Data nascimento:", record[2])
        print("- Gênero:", record[3])
        print("- Código cargo", record[4])
        print(" ")
def select_all_join():
    sql = """SELECT emp.nome, emp.dta_nascimento, emp.genero, carg.nome 
            FROM tb_empregado AS emp INNER JOIN td_cargo AS carg
            WHERE emp.cod_cargo = carg.idt
    """
    cursor.execute(sql)
    registros = cursor.fetchall()   # registros é uma lista de tuplas
    print("\n - Colunas, notação:")
    for record in registros: 
        print("Nome:", record[0])    
        print("Data nascimento:", record[1])  
        print("Genêro:", record[2])  
        print("Nome Cargo:", record[3]) 
        print(" ") 

def delete2(): # vai deletar tudo, toda a linha
    print('Valor para deletar: ')
    pesquisa = input('Nome:')
    sql = f"""delete from tb_empregado WHERE nome = '{pesquisa}'"""
    cursor.execute(sql)
    conexao.commit()

def delete():
    tabela = input("De qual tabela você deseja deletar? (cargo/empregado): ").lower()
    id_registro = input("Digite o ID de registro que deseja deletar: ")
    if tabela == "cargo":
        sql = f"Delete FROM td_cargo WHERE  idt = {id_registro}"
    elif tabela == "empregado":
        sql = f"DELETE from tb_empregado WHERE idt = {id_registro}"
    else:
        print("Tabela Inválida")
        return
    cursor.execute(sql)
    conexao.commit()
    print("Registro deletado com sucesso!")

def close_connection():
    cursor.close()
    conexao.close()
    print('\nConexão fechada.')


if __name__ == '__main__':
    create_database()               # Chama a função create_database
    conexao = create_connection()   # Chama a função
    cursor = conexao.cursor()
    create_table()                  # Chama a função
    # insert_cargo()                  # Chama a função
    # insert_empregado()            # Chama a função
    # select_all_emp()
    # select_all_join()
    # delete()
    delete2()
    close_connection()            # Chama a função close_connection
