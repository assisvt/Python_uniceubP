""" 
- Resolva com lista
- Elabore o programa que leia a altura e o gênero (‘m’ para masculino
e ‘f’ para feminino) de um grupo de pessoas. Gere a tela de saída
com as seguintes informações: maior altura do grupo, menor altura
do grupo, quantidade de homens e quantidade de mulheres.

         - Entrada:                 - Saída:
Teste 1: 1.8, m; 1.6, f; 0          Maior=1.80 Menor=1.60 Masc.=1 Fem.= 1
Teste 2: 1.8, m; 1.9, f; 0          Maior=1.90 Menor=1.80 Masc.=1 Fem.= 1
Teste 3: 1.8, m; 1.6, f; 1.7, m; 0  Maior=1.80 Menor=1.60 Masc.=2 Fem.= 1
Teste 4: 1.8, m; 1.9, f; 1.6, f; 0  Maior=1.90 Menor=1.60 Masc.=1 Fem.= 2 """

l_altura = []                   # Duas formas de criar lista vazia
l_genero = list()
print('Digite [0] pra sair')
while True:                     # Início da estrutura de repetição
    altura = float(input("Altura: "))  # Indentação obrigatória.
    if altura == 0:             # Testa condição de saída
        break                   # Sai da estrutura de repetição
    l_altura.append(altura)     # Armazena a altura no final da lista
    genero = input("[m] para Masculino\n[f] para Feminino: ")
    l_genero.append(genero)     # fim do while
print("Maior altura no grupo:", max(l_altura))       # Maior valor na lista
print("Menor altura no grupo:", min(l_altura))       # Menor valor na lista
print("Quantidade de homens:", l_genero.count('m'))  # Qtd. de 'm' na lista
print("Quantidade de mulheres:", l_genero.count('f'))
# print("Quantidade de mulheres: {:d}" .format(l_genero.count('f')))
# print(f"Quantidade de mulheres: {l_genero.count('f')}")
''' --- ALTERAÇÕES:
a. Calcule e mostre também a média de alturas do grupo.
Teste 4:1.80, m, 1.60, f, 0  Saída: Maior=1.80 Menor=1.60 Masc.=1 Fem.=1 
        Média = 1.7
b. Calcule e mostre também a porcentagem de homens.
Teste5:
1.80, m, 1.60, f, 0 Saída:Maior=1.80 Menor=1.60 Masc.=1 Fem.=1 Média=1.7
        Porc = 50
c. Digite a condição de saída (zero) de primeira e evite os erros do Python.
   Mostre somente esta mensagem:    "Não foi digitado nenhum dado."

    --- DICAS ABAIXO:
soma = sum(l_altura)                                            # a.
ct = len(l_altura)
media = soma/ct
print ("Média das alturas:", media)
porc_m = l_genero.count('m') / len(l_genero) * 100              # b.
print('Porcentagem: ', porc_m) 
if len(l_altura) != 0:                                          # c.
    print ("Maior altura no grupo: ", maior)
    print ("Menor altura no grupo: ", menor)
    print ("Quantidade de homens: ", ct_masc)
    print ("Quantidade de mulheres: ", ct_fem)
    . . .          # Todo o código depois do while
else:
    print("Não foi digitado nenhum dado.")

-----
        
- Teoria:
test = "AuLa de python"
print(test.lower())       # Todas as letras minúsculas.
test = "AuLa de python"
print(test.upper())       # Todas as letras maiúsculas.
test = "AuLa de python"     
print(test.capitalize())  
# Primeira letra maiúscula e as outras letras minúsculas.
test = "AuLa de python"     
print(test.title())  
# Primeira letra de cada palavra maiúscula e as outras minúsculas.
# Saída:
# aula de python
# AULA DE PYTHON
# Aula de python
# Aula De Python

---

Obs.: se tentar usar o max, min ou count com lista vazia dá erro


- Teoria list:
l = []
l.append(2)
len(l)
sum(l)
print(l)
min(l)
max(l)
l.count('valor')

'''
