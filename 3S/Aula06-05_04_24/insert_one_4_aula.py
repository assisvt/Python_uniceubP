"""                Comentários de várias linhas

  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

nome do programa: insert_one.py

- CRUD (acrônimo de Create, Read, Update e Delete) para as
quatro operações (insere, consulta, atualiza e remove)

Inserir um cliente na tabela tb_cliente: '123', 'Paula', 31

- Sintaxe 1:
sql= ''' insert into nome_tabela[(nome_coluna1, nome_coluna2,...)]
        values(valor1, valor2, ...) '''

- Sintaxe 2:
sql = "insert into nome_tabela values(valor1, valor2, ...)"

Obs.:
Os colchetes [ ] dentro de uma sintaxe, significa a parte opcional do comando
"""
import sqlite3                            # nome do programa: insert_one.py
conexao = sqlite3.connect('livraria.db')  # Conexão com a base livraria.db
cur = conexao.cursor()
sql = "insert into tb_cliente(cpf, nome, idade) values('123', 'Paula', 31)"
cur.execute(sql)
conexao.commit()            # Obrigatório, persistir os dados no banco
cur.close()
conexao.close()
print("Fechou a base de dados")

""" ----- ALTERAÇÕES:
a. Quando roda o insert a segunda vez dá erro. Porquê?
b. Insira o segundo cliente
c. Insira o terceiro cliente só com cpf e nome
d. Insira o quarto cliente só com cpf. Deu erro, porquê?
    ----- DICAS:
sqlite3.IntegrityError: UNIQUE constraint failed: tb_cliente.cpf        # a.
cur.execute('''create table if not exists tb_cliente (
    cpf text primary key,
Obs.: a chave primária não pode ter valor repetido
sql = "insert into tb_cliente(cpf, nome, idade) 
        values('132', 'Paula', 21)"                                     # b.
cur.execute(sql)
# sql = "insert into tb_cliente(cpf, nome) values('125', 'Paula')"      # c.
# sql = "insert into tb_cliente(cpf) values('125')"                     # d.
sqlite3.IntegrityError: NOT NULL constraint failed: tb_cliente.nome
Obs.: a coluna nome tem a constraint Not Null 
---

...
e. Mostre a quantidade de registros inseridos.
f. Mostre a quantidade de registros na tabela.
g. Insira um cliente sem usar o nome das colunas no comando insert.
h. Peça pro usuário digitar os dados para inserir na base.

    ----- DICAS:
...
print('Qtd. registros inseridos-rowcount:', cur.rowcount)               # e.
    # Qtd. de registros inseridos(1)
print('Qtd. registros na base-lastrowid:', cur.lastrowid)               # f.
    # Qtd. de registros na tabela (n)

# sql = "insert into tb_cliente values('122', 'Paula', 21)              # g
...                                                                      # h.
sql1 = "insert into tb_cliente(cpf, nome, idade) values(?, ?, ?)"
v_cpf = input('CPF: ')
v_nome = input('Nome: ')
v_idade = int(input('Idade: '))
cur.execute(sql1, (v_cpf, v_nome, v_idade))    # Parênteses obrigatórios
...

cur.execute(sql, v_cpf, v_nome, v_idade)    
    # TypeError: function takes at most 2 arguments (4 given)
cur.execute(sql, v_cpf, v_nome, v_idade, )  
    # TypeError: function takes at most 2 arguments (4 given)

-----
# from select_all_10 import Select

def qtd_registro():
    sql = "SELECT * from tb_cliente"  # Consulta a tabela tb_cliente
    cur.execute(sql)
    print('type(cur):', type(cur))
    registros = cur.fetchall()        # registros é uma lista.
    print('type(registros):', type(registros))
    # print(registros)
    qtd = len(registros)
    return qtd
# main do insert

from sqlite3 import Error
# main do insert
...
# Modo 1
sql="insert into tb_cliente(cpf, nome, idade) values('122', 'Paula', 21)"
# Modo 2
sql="insert into tb_cliente values('122', 'Paula', 21) 
try:
    cur=conexao.cursor()

    print('rowcount:', cur.rowcount)    # Qtd. de registros inseridos (-1)
    print('lastrowid:', cur.lastrowid)  # Qtd. de registros na base (None)
    cur.execute(sql)
    print('rowcount:', cur.rowcount)    # Qtd. de registros inseridos (1)
    print('lastrowid:', cur.lastrowid)  # Qtd. de registros na base (15)

    # o = Select()            # Testando ...
    # o.select_all()
    conexao.commit()
    print ("one record added successfully")       # Precisa testar
    print('Qtd = ', qtd_registro())
except Error as e:
    print('Mensagem de erro:')
    print(e)                    # table tb_cliente has no column named cpf1
    print(e.args[0])            # table tb_cliente has no column named cpf1
    conexao.rollback()
cur.close()
conexao.close()

"""

