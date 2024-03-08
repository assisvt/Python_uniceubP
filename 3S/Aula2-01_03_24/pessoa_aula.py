"""                Comentários de várias linhas.
  CEUB  -  Bacharelado em Ciência da Computação (BCC)  -  Prof. Barbosa
ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.

- Implemente:

- Desenvolva a estrutura de um sistema para cadastrar os seguintes dados
  de professores e funcionários de uma instituição de ensino:

  nome, quantidade de dependentes, salário fixo, quantidade de turmas e valor por turma.

1- Crie um projeto usando os conceitos de POO com herança (inheritance) contendo a
   superclasse (classe pai) Pessoa e duas subclasses (classes filhas) Professor e
   Funcionário.
2- Crie a superclasse Pessoa e o construtor com os atributos de instância nome
   e dependente, use valores defaults.
3- Crie os métodos get e set referente ao atributo nome e dependente. Faça crítica no
   set dependente.
4- Crie um objeto da classe Pessoa, cadastre uma pessoa para testar a classe Pessoa
5- A subclasse Professor tem os atributos de instância nome, dependente, qtd_turma
   e valor em reais por turma.
6- O construtor da subclasse Professor recebe os quatro parâmetros e chama o
   construtor da superclasse enviado o nome e a quantidade de dependente.
   E armazena o valor dos atributos qtd_turma e valor em reais por turma.
7- Use valores defaults (padrões) no construtor. Teste
8a- Cadastre um professor no sistema, ou seja, crie um objeto da subclasse Professor
8b- Use alguns métodos get e set dos atributos
9- Cadastre o segundo professor passando somente o nome e a qtd de dependentes
10- Cadastre o terceiro professor sem passar nenhum dado
11- Cadastre o quarto professor passando somente o nome e a qtd de turmas
12- Use alguns métodos get e set dos atributos
13- No método set referente ao atributo qtd_turma, faça pelo menos uma crítica.
14- Crie o método rendimentos, ele não recebe nada, calcula os rendimentos do
    professor e retorna o valor dos rendimentos do professor. O objetivo
    é calcular e retornar os rendimentos do professor que depende da
    quantidade de turmas e do valor que ele ganha por turma.
15- A subclasse Funcionário tem os atributos de instância nome, dependentes
    e salario fixo
- Crie o construtor (__init__) da subclasse com valores defaulf
17- Cadastre o funcionário 1 no sistema passando os três atributos
- Cadastre o funcionário 2 no sistema passando apenas dois atributo
- Cadastre o funcionário 3 no sistema sem passar os atributos
20- Use alguns métodos get e set dos atributos
- No método set referente ao atributo salario, faça pelo menos uma crítica.
22- Para cada dependente, a empresa vai dá um valor extra de cem reais.
- Crie o método salário total considerando o valor extra.
24- Crie o método mostra dados pra mostrar os atributos do professor e do funcionário
25- Elabore e implemente o enunciado de mais um método funcional que você acha
    importante para o sistema.
26- O sistema precisa informar quantas pessoas tem cadastradas (instanciadas).
27- Crie o atributo de classe e o método de classe necessários para atender essa
    necessidade.

"""


class Pessoa(object):                   # Superclasse (classe pai)
    def __init__(self, nome="", qtd_dependente=0):
        self.nome = nome                # Atributo de instância
        self.qtd_dependente = qtd_dependente
    def get_nome(self):                 # Consulta
        return self.nome
    # def set_nome(self, nv_nome):      # Altera, sem crítica
    #     self.nome = nv_nome
    def set_nome(self, nv_nome):        # Com crítica
        if type(nv_nome) == str:
            self.nome = nv_nome
        else:
            print('Erro (set_nome): tipo tem que ser str')
    def get_qtd_dependente(self):               # Sem crítica
        return self.qtd_dependente
    # def set_qtd_dependente(self, qtd_dependente):
    #     self.qtd_dependente = qtd_dependente
    def set_qtd_dependente(self, qtd_dependente):  # Com crítica
        if type(qtd_dependente) == int:
            self.qtd_dependente = qtd_dependente
        else:
            print("Erro: tipo deve ser inteiro.")
    def valor_extra(self):
        vl_extra = self.qtd_dependente * 100
        return vl_extra


class Professor(Pessoa):    # A subclasse Professor herda da superclasse Pessoa
    def __init__(self, nome="", qtd_dependente=0, qtd_turma=0, valor_turma=0):
        super().__init__(nome, qtd_dependente)  # Chama construtor da superclasse
        self.qtd_turma = qtd_turma
        self.valor_turma = valor_turma
    def get_qtd_turma(self):
        return self.qtd_turma
    # def set_qtd_turma(self, nova_qtd_turma):  # Solução 1, sem crítica
    #     self.qtd_turma = nova_qtd_turma
    def set_qtd_turmas(self, nova_qtd_turma):
        if nova_qtd_turma <= 0:                 # Solução 2
            print("Erro (set_qtd_turma2): quantidade de turmas não pode ser negativo.")
        else:
            self.qtd_turma = nova_qtd_turma
    def set_qtd_turma(self, nova_qtd_turma):    # Solução 3
        # if type(nova_qtd_turma) == int:
        if isinstance(nova_qtd_turma, int):
            self.qtd_turma = nova_qtd_turma
        else:
            print('Erro (set_qtd_turma3): tipo inválido.')
    def rendimentos(self):
        vl_rendimentos = self.qtd_turma * self.valor_turma
        return vl_rendimentos
    # def set_qtd_turma(self, nova_qtd_turma):  # Solução 4
    #     if isinstance(nova_qtd_turma, int):
    #         if nova_qtd_turma <= 0:
    #             print("Erro (set_qtd_turma4): Número de turmas inválido")
    #         else:
    #             self.qtd_turma = nova_qtd_turma
    #     else:
    #         print('Erro: tipo inválido.')
    # def set_qtd_turma(self, quantidade):      # Solução 5
    #     if quantidade < 5:
    #         print("O professor deve ter no mínimo 5 turmas")
    #     elif quantidade > 15:
    #         print("O professor pode ter no máximo 15 turmas")
    #     else:
    #         self.qtd_turma = quantidade
    #         print("Número de turmas válido")
    def salario_total(self):
        total = self.rendimentos() + self.valor_extra()
        return total
    def mostra_dados(self):
        print(self.get_nome())
        print(self.get_qtd_dependente())
        print(self.get_qtd_turma())


class Funcionario(Pessoa):
    def __init__(self, nome='', qtd_dependente=0, salario=2000.00):
        super().__init__(nome, qtd_dependente)
        self.salario = salario
    def get_salario(self):
        return self.salario
    # def set_salario(self, n_salario):             # Sem crítica
    #     self.salario = n_salario
    def set_salario(self, n_salario):               # Com crítica
        if type(n_salario) in (float, int):
            if n_salario > 0:
                self.salario = n_salario
            else:
                print('Erro (set_salario): salario tem que ser positivo.')
        else:
            print('Erro (set_salario): tipo deve ser int ou float')
    def salario_total(self):
        total = self.salario + self.valor_extra()
        return total
    def mostra_dados(self):
        print(self.get_nome())
        print(self.get_qtd_dependente())
        print(self.get_salario())


if __name__ == '__main__':                  # Atalho: main <tab>
    p = Pessoa('Alice', 0)
    print(p)
    p1 = Professor("Silvio Ferreira",1, 5)  # Cria objeto da classe Professor
    print('- Dados do professor ...')
    print(p1)
    print('Nome:', p1.get_nome())
    p1.set_nome('Bruno')
    print(f"Nome: {p1.get_nome()}")
    p1.set_nome(34)                         # Argumento errado
    print(f"Nome: {p1.get_nome()}", )
    p1.set_qtd_turma(6)
    print(f'Qtd turmas: {p1.get_qtd_turma()}')
    p1.set_qtd_turma('nome')                # Argumento errado
    print(f'Qtd turmas: {p1.get_qtd_turma()}')
    p2 = Professor("Alice Dutra", 1)
    print(f"Nome: {p2.get_nome()}")
    p3 = Professor()
    print(f"Nome: {p3.get_nome()} e qtd turmas: {p3.get_qtd_turma()}")
    p4 = Professor("Alice Dutra", qtd_turma=4)
    print(f"Nome: {p4.get_nome()} e qtd turmas: {p4.get_qtd_turma()}")
    print("Rendimentos:", p1.rendimentos())

    print('- Dados do funcionário ...')
    f1 = Funcionario("Roberto Dutra", 2, 2000.00)
    print(f"Nome: {f1.get_nome()}")
    f2 = Funcionario("Vinícius", 2)
    print(f"Nome: {f2.get_nome()}")
    f3 = Funcionario()
    print(f"Nome: {f2.get_nome()}")
    f1.set_salario(3000.0)
    print('Novo salário:', f1.get_salario())
    f1.set_salario('Nome')                  # Argumento errado
    print('Novo salário:', f1.get_salario())
    print(f"Nome do Funcionario: {f1.get_nome()}\nSalário:{f1.get_salario()}")
    f1.set_salario(3000)
    print(f"Sálario após alterar: {f1.get_salario()}")
    p1.rendimentos()
    p1.mostra_dados()
    f1.mostra_dados()
    print("Salário total:", p1.salario_total())
