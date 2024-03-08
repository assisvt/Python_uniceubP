menor_valor = 99999999 # começa com o número bem grande pra ser trocado
ct = 0
soma = 0
# Menor valor = float(inf)
print('Digite [0] para sair')
while True:
    valor = int(input('Digite um valor: '))
    if valor == 0:
        break
    if valor < menor_valor:
        menor_valor = valor # Atualiza a variável menor_valor
    # Fim da estrutura de repetição (while)
    ct = ct + 1
    soma = soma + valor
media = soma/ct
if ct == 0:
    print('Não foi digitado nenhum valor.')
else:
    print('O menor valor é', menor_valor)
    print('A quantidade de valores digitados foi:', ct)
    print('A soma dos valores digitados é:', soma)
print('A media dos valores digitados é:', media)
--
menor_valor = 999999 #menor_valor = float{'inf'} começa com o número bem grande pra ser trocado
maior_valor = -99999 # começa com o número bem pequeno pra ser trocado
ct = 0
soma = 0
print('Digite [-1] para sair')
while True:
    valor = int(input('Digite um valor: '))
    if valor == -1:
        break
    if valor < menor_valor: # Se for menor, atualiza o valor da variável menor
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor
    ct = ct + 1
    soma = soma + valor
if ct == 0:
    print('Não foi digitado nenhum valor.')
else:
    media = soma/ct
    print('O menor valor é:', menor_valor)
    print('O maior valor é:', maior_valor)
    print('A quantidade de valores digitados foi:', ct)
    print('A soma dos valores digitados é:', soma)
    print('A média aritmética dos valores digitados é:', media)
