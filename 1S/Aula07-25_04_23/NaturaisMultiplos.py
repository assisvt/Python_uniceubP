'''- Elabore o programa que gere a sequência dos números naturais múltiplos
de 3 até 21.'''

print('- Números múltiplo de 3:')               # Cabeçalho.
for multiplo3 in range(0, 21 + 1, 3):           # for multiplo3 in range(22, 3):
    print(multiplo3)
print('\nEncerrou o programa.')

''' ----- ALTERAÇÕES:
a. Mostre também a soma dos valores da sequência gerada.  Saída:  Soma = 84
b. Mostre também a média dos valores da sequência gerada. Saída:  Média = 10.5 
c. Obtenha o mesmo resultado usando passo igual a 1       --- '''

# a.  COM PASSO 3
soma_multiplo = 0
print('- Números múltiplos de 3:')              # Cabeçalho.
for multiplo3 in range(0, 21 + 1, 3):           # for multiplo3 in range(22, 3):
    soma_multiplo += multiplo3
    if multiplo3 == 21:
        print(f'{multiplo3}.')
    else:
        print(f'{multiplo3},', end=" ") # O end=" " evita a quebra de linha
print('Somatório múltiplos de 3: ', soma_multiplo)
--

# b. COM PASSO 3
ct = 0
soma_multiplo = 0
print('- Números múltiplos de 3:')              # Cabeçalho.
for multiplo3 in range(0, 21 + 1, 3):           # for multiplo3 in range(22, 3): *obs: 0 tbm é múltiplo de 3
    soma_multiplo += multiplo3
    ct += 1
    if multiplo3 == 21:
        print(f'{multiplo3}.')
    else:
        print(f'{multiplo3},', end=" ") # O end=" " evita a quebra de linha
media = soma_multiplo/ct
print('Somatório múltiplos de 3: ', soma_multiplo)
print('Média múltiplos de 3: ', media)
--

# c. COM PASSO 1
ct = 0
soma_multiplo = 0
print('- Números múltiplos de 3:')              # Cabeçalho.
for multiplo3 in range(0, 21 + 1, 1):           
    if multiplo3 % 3 == 0:
        soma_multiplo += multiplo3
        ct += 1
        if multiplo3 == 21:
            print(f'{multiplo3}.')
        else:
            print(f'{multiplo3},', end=" ") # O end=" " evita a quebra de linha
media = soma_multiplo/ct
print('Somatório múltiplos de 3: ', soma_multiplo)
print('Média múltiplos de 3: ', media)
--

# simplificando/scrachado (sem vírgula) COM PASSO 1
ct = 0 
soma_multiplo = 0
print('- Números múltiplos de 3:')              # Cabeçalho.
for multiplo3 in range(0, 21 + 1, 1):           
    if multiplo3 % 3 == 0:
        soma_multiplo += multiplo3
        ct += 1
        print(multiplo3, end=" ") # O end=" " evita a quebra de linha
media = soma_multiplo/ct
print('\nSomatório múltiplos de 3: ', soma_multiplo)
print('Média múltiplos de 3: ', media)
