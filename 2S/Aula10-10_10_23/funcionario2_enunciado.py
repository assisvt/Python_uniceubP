"""             Comentários de várias linhas.

  CEUB  -  FATECS  -  BCC  -  ADS  -  Programação  -  Prof. Barbosa
ctlr<d>, duplica linha. ctrl<y>, apaga linha. ctrl</>, comenta linha.

Continuação do heranca0_enunciado.py

- Com base nos conceitos de POO (Programação Orientada a Objetos), vamos
trabalhar com duas ou mais classes (entidades).
Implemente a entidade funcionario com estas características cpf, nome e
salario. E a entidade gerente com estas características cpf, nome,
salario, senha e quantidade de funcionários que ele gerencia.

- Implemente estes itens:

...
15-h1- Conceito de herança: eliminar código repetido e herdar atributos e métodos
16- A subclasse Gerente herda da superclasse Funcionario
17- Altere o construtor da subclasse Gerente.
18- Rode a função main com as alterações realizadas.

19-h2- Os funcionários recebem uma bonificação. Todos os tipos de funcionários
    recebem 10% do valor do salário. Então, crie o método bonificacao, ele não
    recebe nada e retorna o valor da bonificação.
20- Mostre a bonificacao das instâncias (objetos) f1 e g1.
21- Use o método __str__ para o gerente instanciado (objeto g1).
22- Dados incompletos. Por quê? Sobrescreva o método __str__ na classe gerente  
23- Altere o __str__ na subclasse (Gerente), aproveite o que já tem implentado
    no __str__ da superclasse
24- Utilize o método vars() ou __dict__ para acessar os atributos de Funcionario
    e Gerente.
    Ex.: print(vars(objeto))
         print(objeto.__dict__)

"""


class Funcionario(object):                       # Superclasse ou classe pai
    def __init__(self, cpf, nome, salario=0.0):  # Construtor com valor default
        self.cpf = cpf
        self.nome = nome                         # Atributos de instância
        self.salario = salario
    def get_cpf(self):                           # Consulta
        return self.cpf
    def set_cpf(self, novo_cpf):                 # Altera na memória
        self.cpf = novo_cpf
    def get_nome(self):
        return self.nome
    def set_nome(self, novo_nome):
        self.nome = novo_nome
    def get_salario(self):
        return self.salario
    def set_salario(self, novo_salario):
        self.salario = novo_salario
    def __str__(self):                          # Método mágico ou método dunder
        # s = 'Nome: ' + self.nome+ ',  CPF: ' + self.cpf +
        # ', salário: ' + str(self.salario)
        # s = "Nome: {}, CPF: {}, salario: {:.2f}"
        # .format(self.nome, self.cpf, self.salario)
        s = f"Nome: {self.nome}, CPF: {self.cpf}, salário: {self.salario:.2f}"
        return s                             # As linhas acima são equivalentes
    def bonificacao(self):
        vlr_bonificacao = self.salario * 0.10   # Usando uma variável
        return vlr_bonificacao
        # return self.salario * 0.10    # Equivalente as duas linhas anteriores


class Gerente(Funcionario):    # A subclasse Gerente herda da superclasse Funcionario
    def __init__(self, cpf, nome, salario, senha, qtd_gerencia):
        super().__init__(cpf, nome, salario)                 # Solução 1
        # Funcionario.__init__(self, cpf, nome, salario)     # Solução 2
        self.senha = senha
        self.qtd_gerencia = qtd_gerencia
    def get_qtd_gerencia(self):
        return self.qtd_gerencia
    def set_qtd_gerencia(self, nova_qtd):
        self.qtd_gerencia = nova_qtd
    def autentica(self):                                    # Solução 1
        senha = input("Senha: ")  # A variável senha só vale no autentica
        if senha == self.senha:   # O self.senha vale em toda a classe Gerente
            print("Acesso permitido.")
            return True
        else:
            print("Acesso negado.")
            return False
    def __str__(self):                  # Método mágico ou método dunder
        # s = f"Nome: {self.nome}, CPF: {self.cpf}, salario: {self.salario:.2f}" \
        #     f", Qtd.: {self.qtd_gerencia}"                 # (solução 1)
        s1 = super().__str__()  # Usa o __str__ da superclasse (solução 2)
        s = s1 + ", Qtd.: {}" .format(self.qtd_gerencia)
        s = f"{s1}, Qtd.: {self.qtd_gerencia}"
        return s


if __name__ == '__main__':
    f1 = Funcionario('123', 'Paulo', 1000.00)  # Cria um objeto da superclasse
    print(f1)                                  # print(f1.__str__())   # Teste
    # <__main__.Funcionario object at 0x00000159D5FFB2C8>
    print(f'- Funcionário 1:\nNome: {f1.get_nome()}')
    print(f'CPF: {f1.get_cpf()}')
    print('Salário:', f1.get_salario())
    f1.set_nome('Vinícius')
    print(f'Nome alterado: {f1.get_nome()}')
    g1 = Gerente('234', 'Paula', 3000.0, 's1', 5)  # Cria objeto da subclasse
    print(g1)                                   # print(g1.__str__()) # Teste
    print(f'- Gerente 1:\nCPF: {g1.get_cpf()}')
    print('Nome:', g1.get_nome())
    print('Salário:', g1.get_salario())
    print(g1.__str__())    # print(g1), conseguiu usando o __str__?
    r = g1.autentica()     # O método retorna True ou False
    print(r)
    print(g1.autentica())  # Linhas equivalentes
    # r = f1.autentica()   # Erro, class Funcionario não tem o método autentica
    # AttributeError: 'Funcionario' object has no attribute 'autentica'
    g2 = Gerente('34', 'Paulo', 5000.0, 's2', 3)
    print(g2.__str__())       # print(g2), conseguiu usando o __str__?
    print('- Gerente 2:\nCPF:', g2.get_cpf())
    print('Nome:', g2.get_nome())
    print('Salário:', g2.get_salario())
    # Herança 2
    bonificacao_f1 = f1.bonificacao()  # Usa a variável e objeto da superclasse
    print("Bonificação de f1", bonificacao_f1)
    print("Bonificação de g1", g1.bonificacao())  # usa com objeto da subclasse
    print(f1.__str__())         # print(f1)
    print(g1.__str__())         # print(g1)
    print(vars(f1))             # Métodos do Python, print(vars(objeto))
    print(f1.__dict__)
    # {'cpf': '123', 'nome': 'Paulo', 'salario': 1000.0}
    print(vars(g1))
    print(g1.__dict__)
    # {'cpf': '234', 'nome': 'Paula', 'salario': 3000.0, 'senha': 's1',
    # 'qtd_gerencia': 5}
