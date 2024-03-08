''' - Resolva sem lsita
- Elabore um programa que gere a sequência dos números inteiros de um em um, onde o usuário fornecerá os valores inicial e final da sequência.'''

inicio = int(input('Valor inicial da sequência: '))
fim = int(input('Valor final da sequência: '))
# Usando while
while inicio <= fim:
    print(inicio, end=" ")
    inicio += 1 # Tem que estar indentado aqui
'''
------- Alterações:
a. No final, mostre a quantidade de números gerados na sequência. Use contador "ct".
b. No final, mostre também a soma dos números gerados na sequência. Usa somador "soma".
c. Mostre a sequência dos números gerados na sequência horizontal.
d. MENTAL: responda sem rodar o programa. Se digitar dois valores iguais o que acontece?
e. MENTAL: se digitar o primeiro valor maior que o segundo valor, o que acontece?
'''
ct = 0
soma = 0
inicio = int(input('Valor inicial da sequência: '))
fim = int(input('Valor final da sequência: '))
print('Sequência de números inteiros: ')

for num in range(inicio, fim+1): # for numero in range(inicio, fim+1, 1):
    print(num, end=" ") #c.
    ct += 1
    soma += num
print('\nQuantidade de valores da valores gerados na sequência:', ct) # a.
print('Somatório dos valores digitados:', soma) # b.

'''
- Melhore o programa anterior, se o usuário fornecer o valor inicial menor que o valor final, gere a sequência na ordem crescente. E se o valor inicial for maior que o valor final, 
gere a sequência na ordem decrescente.
TESTE 1: Entrada: 1, 5              Saída: 1 2 3 4 5
TESTE 2: Entrada: 5, 1              Saída: 5 4 3 2 1
TESTE 3: Entrada: 5, 5              Saída: 5
'''
--
ct = 0
soma = 0 
inicio = int(input('Valor inicial da sequência: '))
fim = int(input('Valor final da sequência: '))
print('Sequência de números inteiros: ')

if inicio <= fim:  # inicio < fim (indica ordem crescente)
    for num in range(inicio, fim+1, 1): 
        print(num, end=" ")     
else:
    for num in range(inicio, fim-1, -1): # inicio > fim (indica ordem decrescente)
        print(num, end=" ")

'''
- Resolva sem lista
- Refaça um programa que calcule a média aritmética de uma turma com cinquenta alunos. Onde cada aluno realizou uma avaliação.
Observação: para facilitar os testes, troque o valor cinquenta por cinco.
TESTE 1: Entrada: 2, 4, 6, 8, 10.
TESTE 2: Entrada: 3, 4, 6, 8, 10 
'''

ct = 0
soma = 0
for i in range(1, 5+1, 1): # for i in range(1, 6):
    nota = float(input('Nota do aluno: '))
    soma += nota
    ct += 1
    # fim da repetição for
media = soma/ct
print(f'Média da turma = {media:.2f}')

'''
-----ALTERAÇÕES:
a. Deixe o usuário escolher a quantidade de alunos.

# - a. Faça a conversão  de graus Fahrenheit para Celsius.
# - b. Faça a soma
# - c. Melhor eo programa
'''

soma = 0
print('Fahreinheit | Celsius')           # Mostra o cabeçalho da tabela.
for fahrenheit in range(45, 80+1, 1):    # for fahrenheit in range (50, 81): 
    celsius= 5 / 9 * (fahrenheit - 32)   # celsius = 5 * (fahrenheit - 32)/ 9
    print(f'{fahrenheit:10.1f}  | {celsius:.4f}')
    soma += fahrenheit
print('A soma dos valores em fahrenheit é:', soma)
