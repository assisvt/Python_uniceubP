"""
- Desenvolva a função maximo que recebe dois números inteiros e retorna
o maior deles. Se os números forem iguais, retorne um deles.

A função main (programa) lê dois números, chama a função maximo passando
os dois  argumentos (os valores lidos) e gera a tela de saída com o valor
retornado pela função maximo.
Não use a função nativa (pronta) da linguagem Python.

Teste 1: Entrada: 2 e 3         Saída: Maior valor: 3
Teste 2: Entrada: 4 e 3         Saída: Maior valor: 4
Teste 3: Entrada: 5 e 5         Saída: Maior valor: 5            """
def maximo(num1, num2):         # Assinatura da função
    if num2 > num1:             # Se numero2 for maior que numero1
        maior = num2
    else:
        maior = num1
    return maior                # Retorna o maior valor
# Início da função main
if __name__ == '__main__':      # Atalho: mai <tab>
    numero1 = int(input("Primeiro número: "))
    numero2 = int(input("Segundo número: "))
    vl_retorno = maximo(numero1, numero2)
    # A variável vl_retorno recebe o valor retornado pela função
    print("\nMaior valor:", vl_retorno)
''' ----- ALTERAÇÕES:
a. Chame a função maximo pelo menos duas vezes.
    vl_retorno = maximo(10, 20)         # Acrescente no final do main. # a.
    print("\nMaior valor:", vl_retorno)
b. Refaça a função main (principal) sem usar a variável vl_retorno.    # b.
    # vl_retorno = maximo(numero1, numero2)
    # A variável vl_retorno recebe o valor retornado pela função
    print("\nMaior valor:", maximo(numero1, numero2))

'''
