########## If statement #################
valor = int(input("Digite um número: "))
if valor >= 100:
    print("O valor é maior ou igual a cem.")
else:
    print("Valor menor do que cem.")
print("Ademais, o valor que você escolheu foi:", valor)
--
# Faça um programa que calcule a média aritmética de um aluno que realizou duas avaliações.
# Além do valor da média, inclua na tela de saída uma das menssagens: "Aluno aprovado." ou "Aluno reprovado."
# aprovado: maior ou igual a 5
# reprovado: menor do que 5
nota1 = float(input("Qual foi a sua nota na primeira prova? "))
nota2 = float(input("Qual foi a sua nota na segunda prova? "))
media = (nota1 + nota2)/2 #parênteses obrigatórios
if media >= 5:
    print(f'Aluno aprovado com média = {media:.2f}')
else:
    print(f'Aluno reprovado com média = {media:.2f}')
# ALTERAÇÕES: mostre o valor da média aritmética com duas casas decimais
--
# Solução 1
# Elabore o programa que verifica se o valor inteiro fornecido pelo usuário é par ou ímpar.
# Analise o problema e verifique quais são os dados que o usuário precisa fornecer.
valor = int(input("Digite um número: ")) # receba o número digitado
resto = valor % 2 # pega o resto da divisão de dois números
if resto == 0: # verifica se o valor da variável resto = 0, se o número é par
    print("Número par.")
else: #caso contrário
    print("Número ímpar.")
 --
# solução 2 (mais formaado/resumido)
valor = int(input("Digite um número: "))
if valor % 2 == 0:
    print(f"O número {valor} é par")
else:
    print(f"Número {valor} é ímpar.")
--
# altura: X
# genero: 1 ou 2
altura = float(input("Altura: ")) #Lê, converte para float e atribui à variável
genero = int(input("[1]- para Masculino\n[2]- para Feminino\nOpção: "))
if genero == 1:
    peso_ideal = 72.7 * altura - 58
    print(f"Peso ideal = {peso_ideal:.2f} Kg" )
else:
    peso_ideal = 62.1 * altura - 44.7
    print(f"Peso ideal = {peso_ideal:.2f} Kg")
# obs: código genérico, se eu digitar qualquer outro valor diferente de 2,
# será selecionado o else que o peso da mulher
--
# Elabore o programa que verifics se o o usuário digitou a senha correta.
# Mostre a mensagem "senha incorreta." ou "Acesso liberado."
# Supondo que a senha correta seja 123.
'''senha = int(input("Digite a senha:  "))
if senha == 123:
    print("Acesso liberado.")
else:
    print("Senha incorreta.")'''

senha = str(input("Digite a senha: "))
if senha == "1b3":
    print("Acesso liberado.")
else:
    print("Senha incorreta.")
--
# Elabore um programa que leia um número qualquer e verifique se ele é positivo, nulo ou negativo.
num = int(input("Digite um número: "))
if num > 0:
    print("O número é positivo")
elif num < 0:
    print("O número é negativo")
else:
    print("O número é nulo")
