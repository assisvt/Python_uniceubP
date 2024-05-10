######################### def com mysql ##########################
import mysql.connector
def create_database():
    conexao_db = mysql.connector.connect(user= 'root',
                                         password= '',
                                         host='127.0.0.1')
    print('Conexão db:', conexao_db)
    cursor_db = conexao_db.cursor()   # cria um cursor para executar comandos SQL
    sql = "CREATE DATABASE IF NOT EXISTS db_loja_4"
    cursor_db.execute(sql)
    # # commit só uso no insert update e delete, não na criação de 
    cursor_db.close()
    conexao_db.close
    print('\nConexão db fechada.')
def create_connection():
    con = mysql.connector.connect(user= 'root', #user do servidor
                                  password='', # senha
                                  host= '127.0.0.1', # localhost
                                  database= 'db_loja_4')  # Nome do schema criado
    print('Conexão:', con)
    return con
def close_connection(): # Posso retirar essa função e colocar no final do main
    cursor.close()
    conexao.close()
    print('\nConexão Fechada.')
def create_table():
    sql = """ CREATE TABLE IF NOT EXISTS tab_produto(
    id INT NOT NULL AUTO_INCREMENT,
    NOME VARCHAR(45) NOT NULL UNIQUE,
    PRECO DECIMAL (9,2) NOT NULL,
    dt_validade DATE NULL,
    PRIMARY KEY (ID)
    )"""
    cursor.execute(sql)
    # commit só uso no insert update e delete, não na criação de 
def insert():
    a_nome= input('Nome produto: ')
    a_preco= float(input('Preço produto: '))
    a_data= input('Data. aaaa-mm-dd: ')
    sql = f"""insert into tab_produto(nome, preco, dt_validade) 
    VALUES ('{a_nome}', {a_preco}, '{a_data}')
"""
    cursor.execute(sql)
    conexao.commit()

def select(): # n precisa de commit
    sql = """select * from tab_produto"""
    cursor.execute(sql)
    l_registros = cursor.fetchall()
    print('-List of tuplas:')
    print(l_registros)
    print(' ')
    for record in l_registros:
        print(record)
    print('-Colunas, notação do vetor:')
    for record in l_registros:
        print("-ID:", record[0])
        print("Nome:", record[1])
        print("Price:", record[2])
        print("Data de validade:", record[3])
if __name__=='__main__':
    create_database()
    conexao = create_connection() # chama função
    cursor = conexao.cursor()
    create_table()
    insert()
    select()
    close_connection()
    

