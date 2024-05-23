"""
Conectar com sql:
>pip install mysql-connector-python    - Terminal dos IDEs

Enunciado: Sistema de cadastramento de marmitas online.
    Crie um sistema capaz de cadastrar marmitas. Para isso, é preciso criar um banco de
dados e implementar as funcionalidades necessárias para gerenciar as categorias de marmitas e 
as próprias marmitas.

O sistema criado deve ser capaz de:
    1. Cadastro de Categorias de Marmitas:
        -Permitir que o restaurante cadastre diferentes categorias de marmitas, como 
        "Fitness", "Vegetariana", "Tradicional", entre outras.
        -Cada categoria deve ter um nome único e não pode ser duplicada no sistema.
    2. Cadastro de Marmitas:
        -Permitir que o restaurante cadastre diferentes tipos de marmitas dentro de cada
         categoria.
        -Cada marmita deve ter um nome obrigatório, uma data de validade opcional, um tamanho 
        (Grande, Média ou Pequena) e deve estar associada a uma categoria existente 
    3. Consultar as Marmitas:
        -Permitir que o usuário visualize as marmitas no banco de dados.
"""

import mysql.connector
def create_database():
    conexao_db = mysql.connector.connect(user='root',  
                            password='',               
                            host='127.0.0.1')          
    print('Conexão db:', conexao_db)  
    cursor_db = conexao_db.cursor()  
    sql = "CREATE DATABASE if not exists db_cadastramento" 
    cursor_db.execute(sql)           
    cursor_db.close()
    conexao_db.close()
    print('\nConexão db fechada.')

def create_connection():
    con = mysql.connector.connect(user='root',     
                            password='',            
                            host='127.0.0.1',       
                            database='db_cadastramento')  
    print('Conexão:', con)                          
    return con

def create_table():
    sql_categoria = """ CREATE TABLE IF NOT EXISTS tb_categoria(  # Tabela de domínio
    id int NOT NULL AUTO_INCREMENT,         # # Cria automaticamente a chava primária (1A)
    nome varchar(45) UNIQUE NOT NULL,       # Valores sem repetição (2A)
    PRIMARY KEY (id)                        # Define a chave primária (1A)
    )   """
    cursor.execute(sql_categoria)        
    sql_marmita = """ CREATE TABLE IF NOT EXISTS tb_marmita(      # Tabela básica
    id int NOT NULL AUTO_INCREMENT,         # Cria automaticamente a chava primária (1B)
    nome varchar(45) NOT NULL,              # NOT NULL para valor obrigatório (2B)
    dt_validade date NULL,                  # NULL para valor opcional (3B)
    tamanho enum('G', 'M', 'P') NOT NULL,   # Coluna enum (4B)
    cod_categoria int NOT NULL,             # NOT NULL para valor obrigatório// pra criar a FK (5B)
    PRIMARY KEY (id),                       # Define a chave primária (1B)
    FOREIGN KEY(cod_categoria) REFERENCES tb_categoria(id)  # Define chave estrangeira (5B)
    )   """
    cursor.execute(sql_marmita)     # Depois, crie a tabela tb_empregado

def insert_categoria():                   # Solução 1
    a_nome = input('Nome da categoria: ')  # Insere primeiro na tabela domínio
    sql = f"""  insert into tb_categoria (nome)
                values('{a_nome}')              """
    cursor.execute(sql)
    conexao.commit()                  # Confirma a alteração no database

def insert_marmita():                       # Solução 1
    a_nome = input('Nome Marmita: ')
    a_dt_validade = input("Data validade: aaaa-mm-dd: ")
    a_tamanho = input("Tamanho [G]; [M]; [P]: ")
    a_cod_categoria = int(input('FK - Código Categoria: '))
    sql= f"""insert into tb_marmita (nome, dt_validade, tamanho, cod_categoria)
     values('{a_nome}', '{a_dt_validade}', '{a_tamanho}', {a_cod_categoria}) """
    cursor.execute(sql)
    conexao.commit()                # Confirma a alteração no database

def select_all_marmita():
    sql = ' select * from tb_marmita '
    cursor.execute(sql)
    registros = cursor.fetchall()   # registros é uma lista de tuplas
    print('- Lista de tuplas:')      # Solução 1:
    print(registros)                # Mostra os registros na horizontal
    print('- Tuplas:')              # Solução 2:
    for record in registros:        # Mostra os registros na vertical
        print(record)

def close_connection():
    cursor.close()
    conexao.close()
    print('\nConexão fechada.')

def main():
    while True:
        print("\n------------ Menu ------------")
        print("1. Inserir Categoria")
        print("2. Inserir Marmita")
        print("3. Visualizar Marmitas")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            insert_categoria()
        elif opcao == "2":
            insert_marmita()
        elif opcao == "3":
            select_all_marmita()
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == '__main__':
    create_database()               # Chama a função create_database
    conexao = create_connection()   # Chama a função
    cursor = conexao.cursor()
    create_table()                  # Chama a função
    main()

    close_connection()            # Chama a função close_connection

