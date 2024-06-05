# >pip install mysql.connector
"""
OBS: DELETE, INSERT, UPDATE UTILZAR COMMIT

1. Criar database passando valores *
    a) Estabelecer conexão
    b) Criar cursor para executaar comandos sql
    c) execute cursor e feche cursor e conexao
2. Passar nome do database, acrescentando após host o nom do database
3. Criar tabela pasando um cursor difente da tabela criad anteriormente
4. Analisar os def que podem ser criados, de acordo com a questão para inserir dados, deletar, selecionar.

"""
import mysql.connector
def create_database():
    conexao_db = mysql.connector.connect(user='root',
                                         password=')
