import mysql.connector 
conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1')
print('Conexão:', conexao)
cursor= conexao.cursor()

sql= 'CREATE DATABASE IF NOT EXISTS db_restaurante'
cursor.execute(sql)

conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1',
                                  database= 'db_restaurante')
print('Conexão:', conexao)

cursor = conexao.cursor()
sql = """ CREATE TABLE IF NOT EXISTS tb_restaurante(    
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(80) NOT NULL UNIQUE,
    preco DECIMAL(9,2) NOT NULL,
    dt_validade DATE NULL,
    categoria VARCHAR(100) NULL,
    PRIMARY KEY (id))
"""
cursor.execute(sql)

sql = """INSERT INTO tb_restaurante(nome, preco, dt_validade, categoria) 
    VALUES ('Estrogonofe de Frango', 22.40, '2024-05-24', 'Sucessos')
"""
cursor.execute(sql)
conexao.commit()

sql = """INSERT INTO tb_restaurante(nome, preco, dt_validade, categoria) 
                         VALUES 
                            ('Frango com Quiabo', 18.90, '2024-05-24', 'Promoção'),
                            ('Lasanha Bolonhesa', 25.50, '2024-05-26', 'Massas')"""
cursor.execute(sql)
conexao.commit()

cursor.close()
conexao.close()

print('\nConexão fechada.')
