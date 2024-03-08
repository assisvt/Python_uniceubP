'''- Sintaxe da estrutura de repetição for (para):

Comandos antes do for                                   # Executa uma vez
...
for variavel in range(v_inicial ,v_final, v_passo):     # Executa várias vezes.
    comando dentro do for                               # ...
    . . .                                               # ...
    comando dentro do for                               # Executa várias vezes.
Comandos depois do for, quando sai do for               # Executa uma vez

- Onde:
v_inicial é o valor inicial (inclusive) dos valores do intervalo
v_final é o valor final (exclusive) dos valores do intervalo
v_passo é o valor do passo, do intervalo entre os valores do intervalo

Obs.: a função range retorna uma lista.

Para cada valor da variável no intervalo de v_inicial até v_final-1.'''


# - Elabore o programa que gere a sequência dos números naturais até 10 na vertical.
print('- Números naturais na vertical:')  
for num in range(0, 11, 1):  # for i in range (0, 10+1):     # for i in range(11):
    print(num)               # Mostra i na tela. O print quebra a linha por padrão
print('Encerrou o programa.')

''' ----- ALTERAÇÕES:
a. No final, mostre a quantidade de números da sequência. Use contador. 
   Saída:  Quantidade: 11
b. Refaça o programa utilizando while em vez de for.'''


# a.
ct = 0                                              # Antes do for                 # a.
print('- Números naturais na vertical:')  
for num in range(0, 11, 1):
    ct = ct + 1                                     # Dentro do for
    print(num)
print('Quantiadade de número digitados: ', ct)  # Depois do for          
print('Encerrou o programa.')
--

# b.      
ct = 0
print('-Números naturais na vertical: ')
while True:
    if ct == 11:
        break
    print(ct)
    ct = ct + 1
print('Encerrou o programa.')
print('Quantidade de números digitados:', ct)  
--

ct = 0                               # (Solução 2, semm break)              
while ct < 11:
    print(ct)
    ct += 1                                
print('Encerrou o programa.')
print('Quantidade de números digitados:', ct)      
