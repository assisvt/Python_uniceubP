""" 
- Com base nos conceitos de POO (Programação Orientada a Objetos), implemente
a entidade pessoa com estas características:
nome, peso, altura e ano de nascimento.

-Implemente os itens:

1- Crie o arquivo .py e a classe Pessoa
2- Crie o método construtor: ele recebe quatro parâmetros que serão armazenados nos atributos.
   No construtor, crie os quatro atributos da classe (nome, peso, altura e ano de nascimento)
3- No método main, crie (instancie) dois objetos da classe Pessoa e passe os argumentos.
4- Mostre o objeto criado, o objeto pessoa1, teste (rode) a classe
5- Crie os métodos get (consultar) e set (alterar) para os atributos nome e ano_nascimento.
   def get_nome_atributo1(self):                   # Modelo do método get (consulta)
       return self.nome_atributo1
   def set_nome_atributo1(self, valor):            # Modelo do método set (altera)
       self.nome_atributo1 = valor
6- No main, teste os métodos dos atributos da classe Pessoa (consulte e mostre)
   Mostre o atributo nome e mostre o atributo ano de nascimento
7- Use o método set para alterar o valor do atributo ano_nascimento para 2005. Teste
8- Crei o método set_nome com crítica, evitar dados inconsistentes. Teste
9- Crie o método IMC (Índice de Massa Corporal), ele recebe o objeto, calcula e retorna o valor
   do IMC. O IMC é calculado dividindo o peso (em kg) pela altura ao quadrado (em metros).
10- No programa (main), crie o objeto pessoa3 e passe os argumentos
11- Teste o item anterior, ou seja, mostre o valor dos atributos do objeto pessoa3
12- Altere o construtor para ele instanciar um objeto sem a ano_nascimento,
    valor default 2000. Ele recebe somente o nome, o peso e a altura. Teste
13- Sobrescreva o método especial __str__ . Ele recebe o objeto e retorna os dados de uma
     pessoa (nome, peso e ano de nascimento). Teste.
14- Crie o método calcula_idade, ele recebe o objeto e retorna a idade da pessoa. Teste abaixo:
    No final do main, altere a data da pessoa1 para: 2000. Qual a idade da pessoa1?

"""


import datetime
# O nome de classe começa com letra maiúscula e as outras letras minúsculas.
# class Pessoa:
# class Pessoa():
class Pessoa(object):  # Três formas equivalentes de criar a classe.
    # def __init__(self, nome, peso, altura, ano_nascimento):   # Método construtor
    def __init__(self, nome, peso, altura, ano_nascimento=2002):  # default
        self.nome = nome                                        # Atributos
        self.peso = peso
        self.altura = altura
        self.ano_nascimento = ano_nascimento
    def get_nome(self):                         # Métodos gets e sets
        return self.nome
    # def set_nome(self, novo_nome):              # Sem crítica
    #     self.nome = novo_nome
    def set_nome(self, novo_nome):                  # Com uma crítica
        # if type(novo_nome) == str:                # Duas linhas equivalentes
        if isinstance(novo_nome, str):
            self.nome = novo_nome
        else:
            print('Erro: nome deve ser string.')
    def get_peso(self):
        return self.peso
    def set_peso(self, novo_peso):
        self.peso = novo_peso
    def get_ano_nascimento(self):               # Consultar
        return self.ano_nascimento
    def set_ano_nascimento(self, novo_ano):     # Alterar
        self.ano_nascimento = novo_ano
    def imc(self):                                          # Método funcional
        # vl_imc = self.peso / self.altura ** 2             # 1
        # vl_imc = self.peso / pow(self.altura, 2)          # 2
        vl_imc = self.peso/(self.altura * self.altura) # 3(Parênteses obrigatórios)
        return vl_imc
        # return self.peso/(self.altura * self.altura)# 4(Parênteses obrigatórios)
    def __str__(self):                      # Sobrescreve o método especial __str__
        # s = self.get_nome()+' ' + str(self.peso) + ', ' + str(self.get_ano_nascimento())
        # s = "{} {}, {}" .format(self.nome, self.peso, self.ano_nascimento)  # .format
        # s = f"{self.get_nome()}, {self.peso} {self.get_ano_nascimento()}"   # gets
        s = f"{self.nome}, {self.peso}, {self.ano_nascimento}"                # f-string
        return s
        # return f"Nome: {self.nome}, Peso: {self.peso}, Nascimento: {self.ano_nascimento}"
    def calcula_idade(self):                     # Método funcional
        hoje = datetime.date.today()             # Data  de hoje (ano, mes, dia)
        idade = hoje.year - self.ano_nascimento  # year pega o ano de uma data
        return idade                             # Solução incompleta


if __name__ == '__main__':                          # Atalho: mai <tab>
    pessoa1 = Pessoa("Carlos", 71, 1.80, 2000)      # Chama o construtor __init__
    print("Objeto criado:", pessoa1)
    # print(pessoa1.__str__()) # Chama o método __str__
    # Saída do print anterior:    <__main__.Pessoa object at 0x0000014E7C0F9FD0>
    pessoa2 = Pessoa("Rogerio", 7, 1.82, 1995)      # Chama o construtor __init__
    print("Objeto criado:", pessoa2)
    nome = pessoa1.get_nome()                               # Usando variável
    print("- Pessoa 1:\nNome:", nome)
    # print("- Pessoa 1:\nNome:", pessoa1.get_nome())  # Igual as duas anteriores
    print("Ano Nascimento:", pessoa1.get_ano_nascimento())  # Direto no print
    pessoa1.set_ano_nascimento(2005)
    print("Ano Nascimento alterada:", pessoa1.get_ano_nascimento())  # Confirma
    pessoa1.set_nome("Rogério")                     # Tipo do argumento correto
    print('Nome alterado:', pessoa1.get_nome())     # Teste
    pessoa1.set_nome(2.3)                           # Tipo do argumento errado
    print('Nome:', pessoa1.get_nome())              # Teste
    print('IMC:', pessoa1.imc())                    # IMC: 21.91358024691358
    print(f'IMC: {pessoa1.imc()}')                  # IMC: 21.91358024691358
    print(f'IMC: {pessoa1.imc():.2f}')              # IMC: 21.91, f-string
    print(f'IMC: {pessoa2.imc():.2f}')              # IMC: 21.91, f-string
    pessoa3 = Pessoa("Maria", 63, 1.65, 2004)  # Chama método __init__ (construtor)
    print("- Pessoa 3:\nNome: ", pessoa2.get_nome())        # Teste
    print("dta_nascimento: ", pessoa2.get_ano_nascimento())
    pessoa4 = Pessoa("Ana", 61, 1.69)                       # Passando só três argumentos
    print('- Pessoa 4:\nData Nascimento:', pessoa3.get_ano_nascimento())
    print(pessoa4.__str__())                # Linhas equivalentes, __str__() é opcional
    print(pessoa4)
    print(pessoa1)
    pessoa1.set_ano_nascimento(2003)
    print("Idade, pessoa 1:", pessoa1.calcula_idade())
    print("Idade, pessoa 2:", pessoa2.calcula_idade())
    print("Idade, pessoa 3:", pessoa3.calcula_idade())
