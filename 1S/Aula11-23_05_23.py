# Define a função que recebe os parâmetros v1 e v2.
def retorna_soma(v1, v2):       # A função recebe dois parâmetros
    soma = v1 + v2              # A variável soma recebe o cálculo
    return soma                 # Retorna o valor calculado, pode usar print(soma)
if __name__ == '__main__':
    valor1 = int(input('Primeiro valor: '))
    valor2 = int(input('Segundo valor: '))
    v_retorno = retorna_soma(valor1, valor2)
    print('Soma = ', v_retorno)
    v_retorno = retorna_soma(2.1, 3.3)
    print('Soma =', v_retorno)

''' Desenvolva a função maximo que recebe dois números inteiros e retorna o 
maior deles. Se os números forem iguais, retorna um deles. A função main(programa)
lê dois números, chama a função maximo passando os dois argumentos (os valores lidos)
e gera a tela de saída com o valor retornado pela função máximo. Não use a função nativa (pronta)
da linguagem python'''

def maximo(num1, num2):
    if num2 > num1:
        maior = num2
    else:
        maior = num1
    return maior
if __name__== '__main__':
    num1 = int(input('Primeiro valor: '))
    num2 = int(input('Segundo valor: '))
    valor_retorno = maximo(num1, num2)
    print('Maior valor:', valor_retorno)
- #OU  
# Essa não pede o que o enunciado manda mas dá o mesmo resultado
def maximo(v1, v2):
    if v1 >= v2:
        print(v1)
    else:
        print(v2)
if __name__ == '__main__':
    valor1 = int(input('Primeiro valor: '))
    valor2 = int(input('Segundo valor: '))
    maximo(valor1, valor2)
    # print(maximo) n precisa usar print dnv se já usei no def

'''
- Construa um programa com as três funções: soma(usei retorna_soma), subtrai
(usei retorna_subtrai) e main (programa principal). A função retorna_soma recebe dois
valores inteiros, realiza a soma e retorna o resultado do cálculo. A função
retorna_subtrai recebe dois valores inteiros, realiza a subtração deles e retorna o resultado do cálculo.
O programa (função main) lê dois valores inteiros digitados pelos usuários, chama a função 
retorna_soma passando os dois valores lidos e depois chama a função subtrai passando os dois 
valores lidos. A função main recebe o valor retornado pelas funções soma e subtrai e gera a tela de saída 
com essas informações. '''

def retorna_soma(a, b):
    soma = a + b # OU CRIAR APENAS UM: return v1 + v2
    return soma
def retorna_subtrai(a, b):
    subtrai = a - b  # pode usar variáveis iguais ao primerio def, como v1, v2, mas melhor não
    return subtrai
if __name__ == '__main__':
    valor1 = int(input('Primeiro valor: '))
    valor2 = int(input('Segundo Valor: '))
    vl_retorno_soma = retorna_soma(valor1, valor2)
    print('Soma = ', vl_retorno_soma)
    vl_retorno_subtrai = retorna_subtrai(valor1, valor2)
    print('Subtrai = ', vl_retorno_subtrai)
'''
- Altere o programa anterior, agor ao usuário vai escolher apenas uma operação.
a opção desejada será lida no programa que chama uma das funções (retorna_soma 
ou retorna_subtrai) passando os dois valores lidos como argumento
'''
def retorna_soma(a, b):
    soma = a + b 
    return soma
def retorna_subtrai(a, b):
    subtrai = a - b  
    return subtrai
if __name__ == '__main__':
    valor1 = int(input('Primeiro valor: '))
    valor2 = int(input('Segundo Valor: '))
    opcao = int(input('[1] Somar\n[2] Subtrair\nOpção: '))
    if opcao == 1:
        print('Soma:', retorna_soma(valor1, valor2))
    else:   
        print('Subtração:', retorna_subtrai(valor1, valor2))
--

def valor_absoluto(v):
    if v < 0:
        vlr_absoluto = -v
    else:
        vlr_absoluto = v 
    return vlr_absoluto
if __name__ == '__main__':
    valor = float(input('Digite um número: '))
    retorno = valor_absoluto(valor)
    # A variável retorno recebe o valor retornado pela função (def)
    print('Valor absoluto:', retorno) # Imprime o valor retornado pela função
