####################### def pt.1 ####################
def mostra_mensagem():                      # Assinatura da função
    print("Bem-vindo ao def do Python.")
# Chama a função dentro do main

if __name__ == '__main__':                  # Atalho: mai + tecla<tab>
    mostra_mensagem()                       # Chama a função sem passar nada'''
''' ----- ALTERAÇÕES:
a. Na função principal, mostre uma mensagem antes de chamar a função (def) 
b. Na função principal, mostre uma mensagem depois de chamar a função (def)
c. Crie mais uma função mostra_mensagem_2, ela recebe uma frase e mostra a frase
   recebida. Na função principal, chame a função passando uma mensagem.
d. No main, chame a função mostra_mensagem2 mais uma vez passando a mensagem.
e. No main, use o input para ler uma mensagem e chame a função mostra_mensagem2 
   mais uma vez passando a mensagem lida.'''
--
# a.
def mensagem():
    print('Bem-vindo ao def do Python.')
if __name__== '__main__':
    print('Mensagem antes da chamada da função')
    mensagem()
--
# b.
def mensagem():
    print('Bem-vindo ao def do Python.')
if __name__== '__main__':
    print('Mensagem antes da chamada da função.')
    mensagem()
    print('Mensagem depois da chamada da função.')
--

# a, b, c, d, e.
def mensagem():
    print('Bem vindo ao def de Python.')         
def mensagem2(msg):  # c.
    print(msg)       # c.
if __name__== '__main__':
    print('Mensagem antes da chamada da função.')   # a.
    mensagem()                                      # a.
    print('Mensagem depois da chamada da função.')  # b.
    mensagem2('Mensagem passada para função LETRA C')  # c.
    var = 'Mensagem passada para função LETRA D' # d.
    mensagem2(var)                               # d. 
    var = input('Mensagem LETRA E: ')            # e.
    mensagem2(var)                               # e.
    
############## def 2. #############################
'''- Crie somente uma função (def), ela que recebe um valor e mostrar o valor
recebido. A função main (principal) chama a função três vezes, passa um valor
inteiro, um valor float e depois um negativo.'''

def valor(p_valor): # Declara a função valor
    print('Parâmetro recebido:', p_valor)

if __name__=='__main__': # Chama a função dentro do main:
    # Primeira forma de fazer o exercício:
    valor(5)      # Chama a função
    valor(23.8)   # Chama a função
    valor(-3)     # Chama a função
'''
    # Segunda forma de fazer o exercício:
    mostra_valor(5)                     	# Chama a função, solução 1
    numero = 23.8
    mostra_valor(numero)                  	# Chama a função, solução 2
    negativo = -55
    mostra_valor(negativo)                  # Chama a função, solução 3
    mostra_valor(int(input("Digite um valor negativo")))  # Chama função solução 4 com input
'''
''' ----- ALTERAÇÕES:
a. Na função principal (main), mostre uma mensagem antes de chamar as funções 
b. Na função principal (main), mostre uma mensagem depois de chamar as funções
c. Na função principal (main), leia um valor inteiro e chame a função mais uma
   vez passando o valor lido.
d. Crie mais uma função mostra_dois_valores, ela recebe dois valores e mostra 
   os valores e chame a função.
e. Chame novamente a função mostra_dois_valores, o usuário digita os dois valores
   na função principal (main)   
   '''

def valor(p_valor): # Declara a função valor
    print('Parâmetro recebido:', p_valor)

def valor2(): 
    valor_lido = int(input('Digite um valor: '))   # c. 
    print('Valor lido:', valor_lido)               # c.

def dois_valores(valor_a, valor_b):               # d.
    print('Valor a:', valor_a)                    # d.
    print('Valor b:', valor_b)                    # d.

if __name__=='__main__': # Chama a função dentro do main:
    print('Mensangem antes da chamada das funções.')  # a.

    valor(5)       
    valor(23.8)   
    valor(-3)    
     
    valor2() # Chama a função valor2                # c.

    dois_valores(58,90) # Chama os dois valores q eu tenho que especificar quais são # d.

    v1 = input("Digite o novo valor a: ")            # Dentro da função principal.    # e.
    v2 = input("Digite o novo valor b: ")            # e.
    dois_valores(v1, v2) # Atualiza a função dois_valores da terceira def # e.

    print('Mensangem depois da chamada das funções.') # b.

##################### def pt.3 ######################
 def mostra_menssagem():
    print("Bem vindo ao def do Python.")
if __name__ == '__main__':
    print('Mensagem antes da chamada da função.')
    mostra_menssagem()
    print('Mensagem depois da chamada da função.')
def mostra_menssagem_2(msg):
    print(msg)
if __name__ == '__main__':
    mostra_menssagem_2('Menssagem passada para a função.')
    var = input('Digite uma menssagem: ')
    mostra_menssagem_2(var)
--

def mostra_menssagem():
    print("Bem vindo ao def do Python.")
def mostra_menssagem_2(msg):
    print(msg)

if __name__ == '__main__':
    print('Mensagem antes da chamada da função.')
    mostra_menssagem()
    print('Mensagem depois da chamada da função.')
    mostra_menssagem_2('Menssagem passada para a função.')
    var = input('Digite uma menssagem: ')
    mostra_menssagem_2(var)
--
def valor(v_valor):
    print('Parâmetro recebido:', v_valor)
if __name__ == '__main__':
    valor(5)
    valor2 = 23.8
    valor(valor2)
    valor3 = -4
    valor(valor3)
--

def valor(v_valor):
    print('Parâmetro recebido:', v_valor)
if __name__ == '__main__':
    valor(5)
    valor(23.8)
    valor(-55)
--

def valor(v_valor):
    print('Parâmetro recebido:', v_valor)
if __name__ == '__main__':
    valor(5)
    valor_float = 23.8
    valor(valor_float)
    valor_negativo = int(input('Digite um valor negativo: '))
--

def mostra_menssagem():
    print('Bem vindo ao def do Python.')
def mostra_menssagem_2(msg):
    print(msg)
def mostra_dois_valores(valor1, valor2):
    print('Valor1:', valor1)
    print('Valor2:', valor2)
if __name__ == '__main__':
    print('Mensagem antes da chamada da função.')
    mostra_menssagem()
    print('Mensagem depois da chamada da função.')
    mostra_menssagem_2('Menssagem passada para a função.')
    mostra_dois_valores(5, 10)
--

def valor(v_valor):
    print('Parâmetro recebido:', v_valor)
if __name__ == '__main__':
    v_valor = int(input('Digite um valor negativo: '))
--

def retorna_soma(v1, v2): # A função recebe 2 parâmetros
    soma = v1 + v2        # A variável soma recebe o cálculo
    return soma           # Retorna o valor calculado

def retorna_soma2(v3, v4):
    soma2 = v3 + v4
    return soma2
# Fim da função

if __name__ == '__main__':
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    v_retorno = retorna_soma(valor1, valor2) # Chama a função
    print('soma =', v_retorno)

    valor3 = float(input('Digite o terceiro valor: '))
    valor4 = float(input('Digite o quarto valor: '))
    v_retorno2 = retorna_soma2(valor3, valor4) # Chama a função
    print('soma =', v_retorno2)
