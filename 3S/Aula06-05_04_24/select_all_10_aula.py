"""                Comentários de várias linhas.

  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

Nome do programa: select_all.py

- CRUD (acrônimo de Create, Read, Update e Delete na língua Inglesa)
pras quatro operações (insere, consulta, atualiza e remove)

Implemente:
- Selecione e mostre todas as colunas e todos os registros da tabela

- Sintaxe:
sql = "select (* | nome_coluna1[, nome_coluna2, ...]) from nome_tabela"

Obs.:
os colchetes [ ] dentro de uma sintaxe, significa a parte opcional do comando

cur.execute(sql)

l_registros = cur.fetchall()
# Pega o resultado do select e coloca na lista registros
"""
import sqlite3                          # Nome do programa: select_all.py
conexao=sqlite3.connect('livraria.db')  # Conexão com base de dados livraria.db
cur = conexao.cursor()
sql = "select * from tb_cliente"        # Consulta a tabela tb_cliente
cur.execute(sql)
l_registros = cur.fetchall()  # Coloca o resultado do select na lista l_registros
print(l_registros)  # Mostra uma lista de tuplas com os registros na horizontal
cur.close()
conexao.close()
print("Fechou a base de dados")

""" ----- ALTERAÇÕES:
a. Mostre a lista de tuplas na vertical.
b. Mostre msg de tabela vazia.
c. No final, mostre a quantidade de registros. Use contador
d. No final, mostre a quantidade de registros. Não use contador
    ----- DICAS:
print('Consulta todos:')                                                # a.
for registro in l_registros:      # Mostra na vertical
    print(registro)
if len(l_registros) > 0:  # if l_registros != None:  # if l_registros:  # b.
    print('Consulta todos:')
    for registro in l_registros:  # Mostra na vertical
        print(registro)
else:
    print('Lista vazia.')
if l_registros:  # if l_registros != None:  # if len(l_registros) > 0:  # c.
    ct = 0
    print('Consulta todos:')
    for registro in l_registros:  # Mostra na vertical
        print(registro)
        ct += 1
    print("quantidade de registros:", ct)
else:
    print('Lista vazia.')
Obs.: use o len(lista)                                                  # d.
if len(l_registros) > 0:  # if l_registros != None:  # if l_registros: 
    print('Consulta todos:')
    for registro in l_registros:  # Mostra na vertical
        print(registro)
    print("Quantidade de registros:", len(l_registros))
else:
    print('Lista vazia.')

"""
