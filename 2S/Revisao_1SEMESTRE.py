############################# pré prova ##########################################
'''
- Solução com lista:

- Construa o programa que encontre o menor valor e o maior valor de um conjunto
de valores inteiros digitados pelo usuário. A condição de saída será o valor -1
que não será considerado na pesquisa.
 --- ALTERAÇÕES:
a. Mostre também a quantidade de valores armazenados na lista (digitados).
b. Mostre também a soma de valores armazenados na lista (digitados).   
'''
lista = []
ct = 0  # a.
soma = 0
print('Digite [-1] para sair')
while True:
    valor = int(input("Valor inteiro: "))
    if valor == -1:
        break
    ct = ct + 1 # a.
    soma = soma + valor # b.
    lista.append(valor)  # Armazena o valor final da lista, conforme vai lendo os valores do input nesse caso
    # Fim da estrutura de repetição while
menor = min(lista)              # Menor
maior = max(lista)              # Maior
print("Menor valor:", menor)
print("Maior valor:", maior)
print('A quantidade de valores digitados é: ', ct)  # a.
print('A soma é:', soma) # b.

# Ou
lista = []
print('Digite [-1] para sair')
while True:
    valor = int(input("Valor inteiro: "))
    if valor == -1:
        break
    lista.append(valor)  # Armazena o valor final da lista, conforme vai lendo os valores do input nesse caso
    # Fim da estrutura de repetição while
menor = min(lista)      # Menor
maior = max(lista)      # Maior
ct = len(lista)    # a.  len retorna o número de elementos contidos numa lista
soma = sum(lista)  # b.   
media = soma/ct    # d.
print("Menor valor:", menor)
print("Maior valor:", maior)
print('A quantidade de valores digitados é: ', ct)  # a.
print('A soma dos elementos da lista é: ', soma)    # b.
print('A média dos elementos da lista é: ', media)  # d.
print('Valores armazenados na lista:')
for valor in lista:   # e.
    print(valor, end=' ')  # e.
--

'''
- Resolva com lista:
- Desenvolva o programa que leia vários números digitados pelo usuário e use
o valor -1 como condição (flag) de saída da estrutura de repetição.
Na tela de saída, mostre a quantidade de números digitados.'''

lista = []
print('Digite [-1] para sair')
while True:
    valor = int(input('Digite o valor:'))
    if valor == -1:
        break
    lista.append(valor)
ct = len(lista)
soma = sum(lista)              # a.
print('Quantidade de números:', ct)
print('Soma dos valores:', soma) # a.
print('Números na lista:\n', lista) # b.
--

'''
- Resolva com lista
- Desenvolva o programa que calcule a média aritmética de uma turma, onde
cada aluno realizou uma avaliação. Não sabemos a quantidade de alunos,
por isso usaremos o valor “-1” como condição (flag) de saída. Na tela de saída,
mostre a média aritmética da turma e a quantidade de alunos da turma. Sempre que
tivermos uma divisão, temos que verificar se o divisor é diferente de zero.
----- ALTERAÇÕES:
a. Se digite -1 na primeira leitura ocorre o erro: 
   "ZeroDivisionError: division by zero". Resolva esse problema. 
    Teste 3:    notas: -1                 Saída: Não existe divisão por zero
'''
lista = []
print('Digite [-1] para sair')

while True:
    nota = float(input('Digite a nota: '))
    if nota == -1:
        break
    lista.append(nota)
qtd_alunos = len(lista)
soma = sum(lista)

if qtd_alunos != 0:           # Lista não está vazia?                 
    media = soma/qtd_alunos
    print(f'Média da turma:  {media:.2f}')
    print('Quantidade de alunos: ', qtd_alunos)
else:
    print('Não existe divisão por zero.')

--

'''
- Resolver com lista

- Construa o programa que calcule a média aritmética dos números pares. O
usuário fornecerá os valores de entrada que pode ser um número qualquer par
ou ímpar. A condição de saída será o número 0 (zero).

- Dica: o operador modulo (%) pega o resto da divisão de dois números.
- Dica: media = soma / ct
 ----- Alterações:
a. Digite a condição de saída (zero) na primeira leitura. Corrija este erro.
b. Mostre todos os valores pares digitados.
'''
num_par = []
print('Digite [0] para sair')

while True:
    valor = int(input('Digite o valor: '))
    if valor == 0:
        break
    if valor %2 == 0:
        num_par.append(valor)
qtd_par = len(num_par)
soma_par = sum(num_par)
media_par = soma_par/qtd_par if qtd_par > 0 else 0
print(f'Média aritmética dos pares: {media_par:.2f}')
--

num_par = []
print('Digite [0] para sair')

while True:
    valor = int(input('Digite o valor: '))
    if valor == 0:
        break
    if valor %2 == 0:
        num_par.append(valor)

qtd_par = len(num_par)
soma_par = sum(num_par)
media_par = soma_par/qtd_par if qtd_par > 0 else 0

if qtd_par > 0:
    print(f"Os valores pares digitados foram: {num_par}")
    print("Média dos pares: %.2f" % media_par)
else:
    print("Nenhum número par foi digitado.")
-- 


'''
- Crie a função retorna_soma para somar dois valores. Ela recebe dois valores,
calcula a soma e retorna o resultado do cálculo.
A função main lê os dois valores inteiros, chama a função retorna_soma passando
os valores lidos e depois mostra o valor retornado pela função retorna_soma,
ou seja, o resultado obtido.
'''
# Define a função que recebe os parâmetros (valores) v1 e v2.
def retorna_soma(v1, v2):          # Assinatura da função
    soma = v1 + v2                 # A variável soma recebe o cálculo
    return soma                    # Retorna o valor calculado
    # Fim da funçao

# A função (def) só será executada quando for chamada dentro da função main.
if __name__ == '__main__':                    # mai + <tab> (atalho)
    valor1 = int(input('Primeiro valor: '))   # Indentação obrigatória.
    valor2 = int(input('Segundo valor: '))
    v_retorno = retorna_soma(valor1, valor2)  # Chama a função
    resultadoE = retorna_soma(2.1, 3.3)
    # A variável v_retorno recebe o valor retornado pela função (def)
    print("Soma = ", v_retorno)
    print('Soma esperada( 5.4) = ', resultadoE)
--


def retorna_soma(v1,v2):
    soma = v1+v2
    return soma
def retorna_subtrai(v1,v2):
    subtrai = v1 - v2
    return subtrai
if __name__ == '__main__':
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    opcao = int(input('[1] Somar\n[2] Subtrair\nOpção:'))
    cr_soma = retorna_soma(valor1, valor2)
    cr_subtrai = retorna_subtrai(valor1, valor2)
    if opcao == 1:
        print('Somar=', cr_soma)
    elif opcao == 2:
        print('Subtrair=', cr_subtrai)
    else:
        print('Opção inválida!')
--

'''2. Implemente uma função que recebe dois valores e retorna a multiplicação deles. 
A função main chama essa função duas vezes. Use inputs.'''

def dois_valores(v1, v2):
    multiplicacao = v1 * v2
    return multiplicacao

if __name__ == '__main__':
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    c_multiplicacao = dois_valores(valor1, valor2)
    print('A multiplicação dos dois valores digitados é:', c_multiplicacao)
--

'''1. Elabore o programa que gere a sequência do dobro dos 
números naturais até 10 na ordem crescente'''

print('Sequência do dobro dos números naturais até 10 na ordem crescente:')
for i in range(1, 11): # Range de 1 a 10, o último sempre exclui
    if i == 10:
        print(f'{2 * i}.') # add ponto final no último numero (10)
    else:
        print(f'{2 * i},', end=' ') # add virgula nos outros,
        # o end=' '  é usado para add espaços entre os numeros, em vez de pular linha

print('Fim do programa.')
--

'''
2. Implemente o programa em Python usando o for que calcula a soma dos primeiros n números
naturais, onde n é fornecido pelo usuário'''
soma = 0
n = int(input("Digite um número natural: "))
for i in range(1, n+1): # n+1 pq sempre exclui o último
# i representa cada valor no intervalo definido pela função range().
    soma += i
print('A soma dos  primeiros', n, 'números naturais é:', soma)
--


'''2.	Construa o programa que leia 3 números inteiros quaisquer e calcule o produto deles.
Use for.
'''
# inicializar a variável que armazenará o produto

# 2. LOOP PARA LER 3 NÚMEROS:
produto = 1
for i in range(1, 3+1):
    num = int(input('Insira um número inteiro: '))
    produto = produto * num # multiplicar o número pelo produto atual
print('O produto dos números é: ', produto)
