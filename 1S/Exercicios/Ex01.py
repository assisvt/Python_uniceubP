'''1. Elabore um programa que calcula a área lateral de um cilindro, 
sabe-se que: Área Lateral Cilindro = 2pi.r.h'''

print('Introduza valores de Raio e de Altura para obter a área de um cilindro com esses respectivos valores.')
import math  # importa o módulo de mat para que eu possa usar "math.pi = valor de pi"
r = float(input('Digite o valor do raio: '))      # Introduz valor raio (r) aceitando ponto flutuante
h = float(input('Digite o valor da altura: '))   # Introduz valor altura (h) aceitando ponto flutuante
AreaLateral_Cilindro = (2 * math.pi * r * h) # Realiza o cáculo da fórmula
print(f'A área lateral do cilindro de raio {r} e altura {h} é:', AreaLateral_Cilindro) 
# Imprime o valor do cáculo realizado



''' 2. Implemente um programa que classifique 2 valores inteiros quaisquer em ordem crescente. Os valores serão
fornecidos pelo usuário '''

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
lista = [valor1, valor2]
lista.sort() # Comando que coloca os valores listados em ordem crescente
print('A ordem crescente dos dois valores digitados é:', lista)



'''3. Desenvolva o programa que leia vários valores reais e no final mostre as seguintes informações:
A quantidade de valores digitados;
A soma dos valores digitados;
A média aritmética dos valores digitados;
Obs.: use o valor 0 (zero) como condição de saída da estrutura de repetição. '''

ct = 0 # Variável "contador" inicial
soma = 0 # Variável "soma" inicial
print('Digite [0] para sair')
while True:
    valor = int(input('Digite o valor: '))
    if valor == 0:
        break # Sai de um estrutura de repetição
    ct = ct + 1 # contador, incrementa o ct
    soma = soma + valor
media = soma/ct
print('Quantidade de números digitados:', ct)
print('A soma dos números digitados é:', soma)
print('A media de todos os números digitados é:', media) 
