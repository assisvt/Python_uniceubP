l_notas = []
print('Digite [-1] para sair')
while True:
    nota = float(input('Nota do aluno: '))
    if nota == -1:
        break
    l_notas.append(nota)
qtd_alunos = len(l_notas)
soma_notas = sum(l_notas)
media = soma_notas/qtd_alunos
print('Média da turma:', qtd_alunos)
--

l_notas = []
print('Digite [-1] para sair ')
while True:
    nota = float(input('Nota do aluno: '))
    if nota == -1:
        break
    l_notas.append(nota)
import statistics
media = statistics.mean(l_notas)
print(media)
--

from statistics import mean
num_par = []
print('Digite [0] para sair')

while True:
    valor = int(input('Digite o valor: '))
    if valor == 0:
        break
    if valor %2 == 0:
        num_par.append(valor)
media = mean(num_par)
print(media) # Mostra media
print(f'Valores pares digitados: \n{num_par}') # Mostra elementos da lista
--

l_valor = []
print('Digite [0] para sair')
while True:
    valor = int(input('Valor inteiro: '))
    if valor == 0:
        break
    l_valor.append(valor)
menor_valor = min(l_valor)
print(('O menor valor é '), menor_valor)
--

from statistics import mean
l_altura = []
l_genero = []

print('Digite [0] para sair')
while True: 
    altura = float(input('Altura: '))
    if altura == 0:
        break
    l_altura.append(altura)
    genero = input('[m] para Masculino ou [f] para Feminino: ')
    l_genero.append(genero)
media = mean(l_altura)
m = l_genero.count('m')
f = l_genero.count('f')
porcentagem = (m/(m+f)) * 100
print('Maior altura do grupo:', max(l_altura))
print('Menor altura do grupo:', min(l_altura))
print('Quantidade de homens:', l_genero.count('m'))
print('Quantidade de mulheres:', l_genero.count('f'))
print(f'Média de altura do grupo: {media}')
print(f'Porcentagem de homens {porcentagem}')
