print('Números naturais na vertical (até o 11):')
for i in range(0,11,1):
    print(i)
    # Fim da estrutura de repetição for
     # for i in range (0, 10+1): # for i in range(11)
print('Encerrou o programa.')
ct = 0
ct = ct + 1
print('A quantidade de número digitados foi')
-- 

print('- Números naturais na horizontal:')
for i in range(0, 10+1,1): # para cada item i no intervalo de 0 a 10
    print(i, end=" ") # 0 end=" " evita a quebra de linha, o default é end="\n"
print('\nEncerrou o programa.')
--

print('-Números naturais pare até 12')
for par in range (0, 13, 2): # for par in range(0, 12+1, 2):
    # o end=" " evita a quebra de linha, o padrão é end="\n"
    print(par, end=" ")  # Na horizontal
--

# Alterações: elabore um programa que gere a sequência dos números naturais ímpares até 13.
print('-Números naturais pare até 12')
for impar in range (1, 13+1, 2): 
    # o end=" " evita a quebra de linha, o padrão é end="\n"
    print(impar, end=" ")  # Na horizontal
--

print('- Números multiplos de 3:')
for multiplo3 in range(0, 21 +1,3):
    print(multiplo3)
print('\nEncerrou o programa')
--

x = int(input('Digite um número inteiro: '))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1: 
    print('Single')
--

# Mede algumas strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

inicio = int(input("Valor inicial: "))
fim = int(input('Valor final: '))
print("- Sequência de números inteiros: ")
for numero in range(inicio, fim + 1): # for numero in range(inicio, fim + 1, 1):
    print(numero)
