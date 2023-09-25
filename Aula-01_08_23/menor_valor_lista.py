""" 
- Resolva com lista
- Construa o programa que encontre o menor valor de um conjunto de
valores inteiros digitados pelo usuário. Na condição de saída, use
o valor 0 (zero) que não será considerado na pesquisa.

Teste 1: valor: 2, 1, 3, 0 Saída: Menor = 1
Teste 2: valor: 1, 3, 2, 0 Saída: Menor = 1
Teste 3: valor: 3, 2, 1, 0 Saída: Menor = 1
Teste 4: valor: 0          Saída: Não foi digitado nenhum valor """

l_valor = list()            # Duas formas de criar uma lista vazia
# l_valor = []
print('Digite [0] para sair')              # Executa uma vez
while True:                                # Passa várias vezes
    valor = int(input("Valor inteiro: "))  # Recebe um valor
    if valor == 0:                         # Se valor igual a zero
        break                              # Saí do while
    l_valor.append(valor)                  # Armazena no final da lista
    # Fim da estrutura de repetição (while).
menor_valor = min(l_valor)                 # Solução 1, com variável
print("O menor valor é", menor_valor)
# - Teoria de listas:
# 5   3   10    7               <- Valores armazenados na lista
# 0   1   2     3               <- posições positivas da lista

''' --- ALTERAÇÕES:
a. Refaça as duas últimas linhas numa única linha de comando
b. Mostre também a quantidade de valores digitados.
c. Mostre a soma dos valoes digitados.
d. Mostre os valores digitados.
e. Se a condição de saída (zero) na primeira leitura, gera este erro: 
   ValueError: min() arg is an empty sequence
   Mostre a mensagem: "Não foi digitado nenhum valor."
    --- DICAS ABAIXO:
print("O menor valor é", min(l_valor))      # Sem variável   # a.
print('Quantidade de valores digitados: ', len(l_valor))     # b.
print('Soma: ', sum(l_valor))                                # c.
print(f"Os valores pares digitados:\n{l_valor}")             # d.
if len(l_valor) == 0:      # Verifica se a lista está vazia  # e.
    print("Nenhum valor válido recebido")
else:
    print("O menor valor é: ", min(l_valor))        
    print ('Quantidade de valores digitados: ', len(l_valor))

---

l_valor.sort()      # Solulção 2, usa o sort (ordem crescente)
print(f'o menor valor é {l_valor[0]}')

# 3   5   7    10     - Valores ordenado (lista.sort())


- Teoria list:
l = []
l.append(2)
len(l)
sum(l)
print(l)
min(l)

'''
