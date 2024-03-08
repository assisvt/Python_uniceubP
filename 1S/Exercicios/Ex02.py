'''1. Faça o programa que calcule o volume de uma esfera de raio R. O usuário fornecerá o dado necessário.      
Onde: volume = 4*pi*r^3/3'''	

print('Digite o valor do raio para calcular o volume da esfera')
import math # Importa o módulo de matemática para usarmos "math.pi = valor de pi"
raio = float(input('Digite o valor do raio: '))
volume = 4 * math.pi * (raio**3)/3
print(f'O volume da esfera, de raio {raio}, é', volume)
--

'''2. Construa o programa que calcule a média aritmética dos números pares e a média aritmética dos 
números ímpares. O usuário fornecerá os valores de entrada que pode ser um número qualquer par ou 
ímpar. A condição de saída será o número zero.''' 

print('Digite números inteiros para o cálculo da média aritmética dos respectivos valores pares e ímpares, ou [0] para encerrar.')
ct_par = 0 # Contagem dos pares
ct_impar = 0 # Contagem dos ímpares
soma_par = 0 # Soma dos pares
soma_impar = 0 # Soma dos impares
while True:
    num = int(input('Digite o número (ou 0 para encerrar): '))
    if num == 0: # Condição de saída
        break
    elif num %2 == 0: # Número par
        ct_par = ct_par + 1
        soma_par = soma_par + num
    else: # Qualquer número inteiro que não é par, logo, ímpar
        ct_impar = ct_impar + 1 
        soma_impar = soma_impar + num
media_par = soma_par/ct_par if ct_par > 0 else 0 # Cálculo da média ct_par > 0, se não, média = 0
media_impar = soma_impar/ct_impar if ct_impar > 0 else 0
print(f'A media dos números pares é {media_par}\ne, a média dos números ímpares, {media_impar}')
