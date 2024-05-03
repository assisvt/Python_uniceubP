import mysql.connector 
conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1')
print('Conexão:', conexao)
cursor= conexao.cursor()

sql= 'CREATE DATABASE IF NOT EXISTS db_loja_2'
cursor.execute(sql)

conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1',
                                  database= 'db_loja_2')
print('Conexão:', conexao)

cursor = conexao.cursor()
sql = """ CREATE TABLE IF NOT EXISTS tb_produto(    
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(80) NOT NULL UNIQUE,
    preco DECIMAL(9,2) NOT NULL,
    dt_validade DATE NULL,
    PRIMARY KEY (id))
"""
cursor.execute(sql)

var_1= input('Nome produto: ')
var_2= float(input('Preço produto: '))
var_3= input('Data. aaaa-mm-dd: ')
sql = f"""insert into tb_produto(nome, preco, dt_validade) 
    VALUES ('{var_1}', {var_2}, '{var_3}')
"""
cursor.execute(sql)
conexao.commit()

cursor.close()
conexao.close()

print('\nConexão fechada.')
