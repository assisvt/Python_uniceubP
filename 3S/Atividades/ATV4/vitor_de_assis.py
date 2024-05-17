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
    # # commit só uso no insert update e delete, não na criação de algo
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
    id INT NOT NULL AUTO_INCREMENT,     # Cria a chava primária automatica 
    NOME VARCHAR(45) NOT NULL UNIQUE,   # Valores sem repetição obrigatório
    PRECO DECIMAL (9,2) NOT NULL,       # NOT NULL para valor obrigatório
    dt_validade DATE NULL,              # NULL para valor opcional
    PRIMARY KEY (ID)
    )"""
    cursor.execute(sql)
    # commit só uso no insert update e delete, não na criação de 

    sql = """ CREATE TABLE IF NOT EXISTS tab_marmita(    
    id INT NOT NULL AUTO_INCREMENT,   # Cria a chava primária automatica
    nome VARCHAR(80) NOT NULL UNIQUE, # Valores sem repetição obrigatório
    preco DECIMAL(9,2) NOT NULL,      # Valores sem repetição obrigatório
    dt_validade DATE NULL,            # NULL para valor opcional
    categoria VARCHAR(45) NULL,       # NULL para valor opcional
    PRIMARY KEY (id)
    )"""
    cursor.execute(sql)

def insert_produto():
    a_nome= input('Nome produto: ')
    a_preco= float(input('Preço produto: '))
    a_data= input('Data. aaaa-mm-dd: ')
    sql = f"""insert into tab_produto(nome, preco, dt_validade) 
    VALUES ('{a_nome}', {a_preco}, '{a_data}')
    """
    cursor.execute(sql)
    conexao.commit()

def insert_marmita():
    a_nome = input('Nome marmita: ')
    a_preco = float(input('Preço marmita: '))
    a_data = input('Data. aaaa-mm-dd: ')
    a_categoria = input('Categoria marmita: ')
    sql = f"""insert into tab_marmita(nome, preco, dt_validade, categoria) 
    VALUES ('{a_nome}', {a_preco}, '{a_data}', '{a_categoria}')
    """
    cursor.execute(sql)
    conexao.commit()

def select_produto(): # n precisa de commit
    sql = "select * from tab_produto"
    cursor.execute(sql)
    registros_produto = cursor.fetchall()
    print('- Registros da tabela tab_produto:')
    for record in registros_produto:
        print(record)
    print('-Colunas, notação do vetor:')
    for record in  registros_produto:
        print("-ID:", record[0])
        print("Nome:", record[1])
        print("Price:", record[2])
        print("Data de validade:", record[3])
    
def select_marmita():
    sql = "SELECT * FROM tab_marmita"
    cursor.execute(sql)
    registros_marmita = cursor.fetchall()
    
    print('- Registros da tabela tab_marmita:')
    for record in registros_marmita:
        print("ID:", record[0])
        print("Nome:", record[1])
        print("Preço:", record[2])
        print("Data de validade:", record[3])
        print("Categoria:", record[4])
    print()

def delete():
    tabela = input("De qual tabela você deseja deletar? (produto / marmita): ").lower()
    id_registro = input("Digite o ID do registro que deseja deletar: ")
    if tabela == "produto":
        sql = f"DELETE FROM tab_produto WHERE id = {id_registro}"
    elif tabela == "marmita":
        sql = f"DELETE FROM tab_marmita WHERE id = {id_registro}"
    else:
        print("Tabela inválida.")
        return

    cursor.execute(sql)
    conexao.commit()
    print("Registro deletado com sucesso!")

def main():
    while True:
        print("\n######### Menu ##############")
        print("1. Inserir Produto")
        print("2. Inserir Marmita")
        print("3. Visualizar Produtos")
        print("4. Visualizar Marmitas")
        print("5. Deletar Registro")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            insert_produto()
        elif opcao == "2":
            insert_marmita()
        elif opcao == "3":
            select_produto()
        elif opcao == "4":
            select_marmita()
        elif opcao == "5":
            delete()
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    
if __name__=='__main__':
    create_database()
    conexao = create_connection() # chama função
    cursor = conexao.cursor()
    create_table()
    main()
    close_connection()
    
