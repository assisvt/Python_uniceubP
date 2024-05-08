import mysql.connector 
conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1')
print('Conexão:', conexao)
cursor= conexao.cursor()
sql = """select * FROM db_restaurante.tb_restaurante"""
cursor.execute(sql)
registros = cursor.fetchall() 

if registros:
    print('- Registros na horizontal:')
    for registro in registros:
        for coluna, valor in zip(cursor.column_names, registro):
            print(f"{coluna}: {valor}", end=" | ")
    print()
   
    print('- Registros na vertical:')
    for registro in registros:
        for coluna, valor in zip(cursor.column_names, registro):
            print(f"{coluna}: {valor}")
        print()  # quebra de linha entre os registros
else:
    print("Tabela vazia.")

cursor.close()
conexao.close()
