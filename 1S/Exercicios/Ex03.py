'''1. Elabore o programa que gere a sequência do dobro dos 
números naturais até 10 na ordem crescente'''

print('Sequência do dobro dos números naturais até 10 na ordem crescente:')
for i in range(1, 11):
    if i == 10:
        print(f'{2 * i}.')
    else:
        print(f'{2 * i},', end=" ")
print('Fim do programa.')
--


'''
2. Implemente o programa em Python usando o for que calcula a soma dos primeiros n números
naturais, onde n é fornecido pelo usuário'''

soma = 0
n = int(input("Digite um número natural: "))
for i in range(1, n+1):
    soma += i
print('A soma dos  primeiros', n, 'números naturais é:', soma)
