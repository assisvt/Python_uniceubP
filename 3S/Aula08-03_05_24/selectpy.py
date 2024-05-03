import mysql.connector 
conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1')
print('Conexão:', conexao)
cursor= conexao.cursor()
sql = """select * FROM db_loja_2.tb_produto"""
cursor.execute(sql)
l_registros = cursor.fetchall() 
"""print('-Listas das tuplas: ')
print(l_registros) # horizontal"""

# Mostrando os registros
for l_registro in l_registros:
    print(l_registro)

cursor.close()
conexao.close()

