'''
1.	Elabore o programa que gere a sequência do dobro dos números naturais até 10 na
ordem crescente. Mostre também a soma da sequência gerada.
'''

# 1.
soma = 0  # inicializar a variável que armazenará a soma
for i in range(1, 11, 1): # números naturais de 1 a 10
    dobro = 2 * i
    soma = soma + dobro # adicionar o dobro à soma
    print(dobro)
print('Soma dos valores: ', soma)

'''
2.	Construa o programa que leia dez números inteiros quaisquer e calcule o produto deles.
Para facilitar os testes, resolva primeiro com três números. Use for.
'''
'# inicializar a variável que armazenará o produto

# 2. LOOP PARA LER 3 NÚMEROS:
produto = 1
for i in range(1, 3+1, 1): # OU for i in range(3): // loop para ler os 3 números
    num = int(input('Insira um número inteiro: '))
    produto *= num # multiplicar o número pelo produto atual
print('O produto dos números é: ', produto)

# LOOP PARA LER 10 NÚMEROS:
produto = 1
for i in range(1, 10+1, 1): # OU for i in range(10): // loop para ler os 10 números
    num = int(input("Insira um número inteiro: "))
    produto *= num # multiplicar o número pelo produto atual
print('O produto dos números é:', produto)
