class FiguraGeometrica:
    ct = 0
    def __init__(self, cor):
        self.cor = cor
        FiguraGeometrica.ct += 1
    def get_cor(self):
        return self.cor
    def contador(self):
        print("Qtd de objetos instanciados:", FiguraGeometrica.ct)

class Retangulo(FiguraGeometrica):
    def __init__(self, cor, base=0, altura=0):
        super().__init__(cor)
        self.base = base
        self.altura = altura
    def get_base(self):
        return self.base
    def set_altura(self, nova_altura):
        self.altura = nova_altura
    def area(self):
        area_obj = self.base * self.altura
        print("Área do objeto:", area_obj)
        return area_obj
    def mostra_dados(self):
        print("Cor:", self.cor)
        print("Base:", self.base)
        print("Altura:", self.altura)

class Circulo(FiguraGeometrica):
    def __init__(self, cor, raio=0):
        super().__init__(cor)
        self.raio = raio
    def set_raio(self, novo_raio):
        if novo_raio <= 0:
            print("Erro! incapaz de calcular raio com valore menores ou iguais a 0")
        else:
            self.raio = novo_raio
    def perimetro(self):
        perimetro = 2 * self.raio * 3.14
        return perimetro

if __name__ == '__main__':
    f1 = Retangulo("Verde", 4, 5)
    print("Retângulo 1:\n")
    f1.mostra_dados()
    f1.area()
    print("Base do Retângulo:", f1.get_base())
    print("Valores com nova altura:")
    f1.set_altura(8)
    f1.mostra_dados()
    f1.area()
    f1.contador()

    f2 = Circulo("Azul")
    print("Cor do Circulo:", f2.get_cor())

    f3 = Circulo("Vermelho", 3)
    print("Perímetro do Círculo:", f3.perimetro())
    f3.set_raio(5)
    print("Perímetro do novo Círculo:", f3.perimetro())
    f3.contador()

'''
# pip install mysql-connector-python
import mysql.connector

def create_database():
    conexao_db = mysql.connector.connect(user='root', password='', host='127.0.0.1')
    print('Conexão db:', conexao_db)
    cursor_db = conexao_db.cursor()
    sql = "CREATE DATABASE if not exists dab_loja"
    cursor_db.execute(sql)
    cursor_db.close()
    conexao_db.close()
    print('\nConexão Fechada')

def create_connection():
    con = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='dab_loja')
    print('Conexao:', con)
    return con

def create_table():
    sql = """CREATE TABLE if not exists tab_veiculos(
    id INT NOT NULL AUTO_INCREMENT,
    placa CHAR(7) NOT NULL UNIQUE,
    nome VARCHAR(45) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    dt_lancamento DATE NULL, 
    PRIMARY KEY (id)
    ) """
    cursor.execute(sql)

def insert_table():
    a_placa = input("Digite a placa de 4 números: ")
    a_nome = input("Digite o nome do veículo: ")
    a_preco = float(input("Digite o preço do veículo: "))
    a_data = input('Data. aaaa-mm-dd: ')
    sql = f"""INSERT INTO tab_veiculos (placa, nome, preco, dt_lancamento)
             VALUES ('{a_placa}','{a_nome}', {a_preco}, '{a_data}')
             """
    cursor.execute(sql)
    conexao.commit()

def select(): 
    sql = """select * from tab_veiculos"""
    cursor.execute(sql)
    l_registros = cursor.fetchall()
    print('-List of tuplas:')
    print(l_registros)

def close_connection():
    cursor.close()
    conexao.close()
    print('Conexao Fechada')

if __name__ == "__main__":
    create_database()
    conexao = create_connection()
    cursor = conexao.cursor()
    create_table()
    insert_table()
    select()
    close_connection()  
    '''
