# - Elabore o programa que gere a sequência dos números naturais ímpares até 13.

for impar in range (0, 14, 1):
    if impar %2 != 0:
        print(impar)
--

''' ----- ALTERAÇÕES:
a. Mostre também a quantidade de valores gerados. Saída: Quantidade = 7
b. Mostre também a soma dos valores da sequência. Saída: soma = 49
c. Refaça o exercício utilizando passo 2
d. Utilize a mesma ideia (de saltos de 2 elementos (passo = 2)) para substituir o for por  um
   while equivalente.   '''                                       


# a. USANDO passo = 1
ct_impar = 0                          # Antes do for
for impar in range (0, 14, 1):  # Fazendo for impar in range (0, 14, 1): dá o mesmo resultado, mas usando o 2 o loop começa em 1 e pula de 2 em 2, gerando apenas números ímpares.
    if impar % 2 != 0 and impar < 13:
        ct_impar = ct_impar + 1       # Dentro do for
        print(impar, end=", ")
    if impar % 2 != 0 and impar == 13:
        ct_impar = ct_impar + 1 
        print(impar, end=". ")
print('\nQuantidade: ', ct_impar)       # Depois do for
--
# simplificando:
ct_impar = 0
for impar in range(0, 14, 1):
    if impar % 2 != 0:
        ct_impar += 1
        if impar == 13: # if dentro do if
            print(f'{impar}.')
        else:
            print(f'{impar},', end=" ")   
print(f'Quantidade: {ct_impar}') # Não precisa pular a linha pq já vai na de baixo.'''
--

# b
soma_impar = 0
ct_impar = 0
for impar in range(0, 14, 1):
    if impar % 2 != 0: # SERIA REDUNDÂNCIA TER ESTRUTURA IF SE FOSSE DE 2 EM 2 "(0, 14, 2)", EM VEZ DE 1 EM 1,  NA LINHA ACIMA, LOGO O CÓDIGO NÃO RODARIA POIS 'for impar in range(0, 14, 2):'  JÁ PEGA SÓ OS IMPARES, caso o final fosse 1, TEM QUE USAR if PARA CONTAR SÓ OS ÍMPARES.
        ct_impar += 1
        soma_impar += impar
        if impar == 13: # IF obrigatório para ter o ponto final
            print(f'{impar}.')
        else:
            print(f'{impar},', end=" ")
            
print(f'Quantidade: {ct_impar}')
print(f'Somatório impares: {soma_impar}')
--

# c. Utilizando passo 2
soma_impar = 0
ct_impar = 0
for impar in range(1, 14, 2): # ou  (0, 14, 2)
    ct_impar += 1
    soma_impar += impar
    if impar == 13:
        print(f'{impar}.')
    else:
        print(f'{impar},', end=" ")
            
print(f'Quantidade: {ct_impar}')
print(f'Somatório impares: {soma_impar}')
--

# d. Utilizando while
soma_impar = 0
ct_impar = 0
num = 1 # Primeiro número impar da sequência, é identificado números ímpares até o break no 13
while True:
    if num % 2 != 0:
        ct_impar += 1
        soma_impar += num
        if num == 13:
            print(f'{num}.')
            break
        else:
            print(f'{num},', end=" ")
    num += 1
print(f'Quantidade: {ct_impar}')
print(f'Somatório impares: {soma_impar}')
--


# Simplificando/scrachado (sem vírgula)
print('Números ímpares até o 13: ')
soma_impar = 0
ct_impar = 0
for impar in range(1, 14, 2): # ou  (0, 14, 2)
    ct_impar += 1
    soma_impar += impar 
    print(impar, end=" ")
            
print(f'\nQuantidade: {ct_impar}')
print(f'Somatório impares: {soma_impar}')
